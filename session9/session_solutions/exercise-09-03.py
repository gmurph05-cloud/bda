from pathlib import Path
import shutil

from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    avg,
    col,
    count,
    date_format,
    dense_rank,
    hour,
    round,
    stddev,
    sum,
    to_date,
    when,
)
from pyspark.sql.types import (
    DoubleType,
    IntegerType,
    StringType,
    StructField,
    StructType,
    TimestampType,
)
from pyspark.sql.window import Window


spark = (
    SparkSession.builder
    .appName("Session09Exercise03")
    .master("local[*]")
    .getOrCreate()
)

schema = StructType([
    StructField("event_id", IntegerType(), True),
    StructField("service", StringType(), True),
    StructField("region", StringType(), True),
    StructField("event_time", TimestampType(), True),
    StructField("request_count", IntegerType(), True),
    StructField("error_count", IntegerType(), True),
    StructField("latency_ms", DoubleType(), True),
    StructField("bytes_in", DoubleType(), True),
    StructField("bytes_out", DoubleType(), True),
])

events_df = (
    spark.read
    .option("header", True)
    .schema(schema)
    .csv("datasets/service_events.csv")
)

events_enriched_df = (
    events_df
    .withColumn(
        "error_rate",
        when(col("request_count") > 0, col("error_count") / col("request_count")).otherwise(0),
    )
    .withColumn("total_bytes", col("bytes_in") + col("bytes_out"))
    .withColumn("traffic_mb", col("total_bytes") / 1048576)
    .withColumn(
        "latency_band",
        when(col("latency_ms") < 100, "fast")
        .when(col("latency_ms") < 160, "normal")
        .otherwise("slow"),
    )
    .withColumn("event_date", to_date(col("event_time")))
    .withColumn("event_hour", hour(col("event_time")))
    .withColumn("day_of_week", date_format(col("event_time"), "E"))
)

service_summary_df = events_enriched_df.groupBy("service").agg(
    count("*").alias("total_records"),
    sum("request_count").alias("total_requests"),
    sum("error_count").alias("total_errors"),
    avg("error_rate").alias("average_error_rate"),
    avg("latency_ms").alias("average_latency_ms"),
    stddev("latency_ms").alias("latency_stddev"),
    sum("traffic_mb").alias("total_traffic_mb"),
)

traffic_window = Window.orderBy(col("total_traffic_mb").desc())
variability_window = Window.orderBy(col("latency_stddev").desc())
reliability_window = Window.orderBy(col("average_error_rate").asc())

ranked_summary_df = (
    service_summary_df
    .withColumn("traffic_rank", dense_rank().over(traffic_window))
    .withColumn("latency_variability_rank", dense_rank().over(variability_window))
    .withColumn("reliability_rank", dense_rank().over(reliability_window))
)

hourly_requests_df = events_enriched_df.groupBy("service", "event_hour").agg(
    sum("request_count").alias("hourly_requests")
)

hour_window = Window.partitionBy("service").orderBy(col("hourly_requests").desc())

busiest_hour_df = (
    hourly_requests_df
    .withColumn("hour_rank", dense_rank().over(hour_window))
    .filter(col("hour_rank") == 1)
    .select("service", col("event_hour").alias("busiest_hour"))
)

final_summary_df = (
    ranked_summary_df
    .join(busiest_hour_df, on="service", how="left")
    .select(
        "service",
        "total_records",
        "total_requests",
        "total_errors",
        round("average_error_rate", 4).alias("average_error_rate"),
        round("average_latency_ms", 2).alias("average_latency_ms"),
        round("latency_stddev", 2).alias("latency_stddev"),
        round("total_traffic_mb", 2).alias("total_traffic_mb"),
        "busiest_hour",
        "traffic_rank",
        "latency_variability_rank",
        "reliability_rank",
    )
    .orderBy("traffic_rank")
)

final_summary_df.show(truncate=False)

output_folder = Path("results/service_summary_spark")
single_csv = Path("results/service_summary.csv")

if output_folder.exists():
    shutil.rmtree(output_folder)

final_summary_df.coalesce(1).write.mode("overwrite").option("header", True).csv(str(output_folder))

if single_csv.exists():
    single_csv.unlink()

part_file = next(output_folder.glob("part-*.csv"))
shutil.copy(part_file, single_csv)

print(f"Saved {single_csv}")

top_traffic = final_summary_df.orderBy("traffic_rank").first()
top_variability = final_summary_df.orderBy("latency_variability_rank").first()
top_reliability = final_summary_df.orderBy("reliability_rank").first()

print(f"Top traffic service: {top_traffic['service']}")
print(f"Most variable latency service: {top_variability['service']}")
print(f"Most reliable service: {top_reliability['service']}")

spark.stop()
