from pyspark.sql import SparkSession
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
    .appName("Session09Exercise01")
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

events_df.printSchema()
events_df.show(5, truncate=False)

print("Rows:", events_df.count())
print("Columns:", events_df.columns)

events_df.createOrReplaceTempView("service_events")

spark.sql("""
    SELECT COUNT(*) AS row_count
    FROM service_events
""").show()

spark.sql("""
    SELECT DISTINCT service
    FROM service_events
    ORDER BY service
""").show()

spark.sql("""
    SELECT region, COUNT(*) AS row_count
    FROM service_events
    GROUP BY region
    ORDER BY row_count DESC
""").show()

spark.stop()
