from pyspark.sql import SparkSession
from pyspark.sql.functions import col, date_format, hour, round, to_date, when
from pyspark.sql.types import (
    DoubleType,
    IntegerType,
    StringType,
    StructField,
    StructType,
    TimestampType,
)


spark = (
    SparkSession.builder
    .appName("Session09Exercise02")
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

events_enriched_df.select(
    "service",
    "event_time",
    "event_date",
    "event_hour",
    "day_of_week",
    round("error_rate", 4).alias("error_rate"),
    round("traffic_mb", 2).alias("traffic_mb"),
    "latency_band",
).show(10, truncate=False)

events_enriched_df.createOrReplaceTempView("service_events_enriched")

spark.sql("""
    SELECT
        service,
        ROUND(AVG(error_rate), 4) AS average_error_rate
    FROM service_events_enriched
    GROUP BY service
    ORDER BY average_error_rate DESC
""").show()

spark.sql("""
    SELECT
        service,
        ROUND(AVG(latency_ms), 2) AS average_latency_ms
    FROM service_events_enriched
    GROUP BY service
    ORDER BY average_latency_ms DESC
""").show()

spark.sql("""
    SELECT
        event_hour,
        SUM(request_count) AS total_requests
    FROM service_events_enriched
    GROUP BY event_hour
    ORDER BY total_requests DESC
""").show()

spark.sql("""
    SELECT
        region,
        ROUND(SUM(traffic_mb), 2) AS total_traffic_mb
    FROM service_events_enriched
    GROUP BY region
    ORDER BY total_traffic_mb DESC
""").show()

spark.stop()
