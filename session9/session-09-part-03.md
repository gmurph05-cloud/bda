### Session 9 | Part 3

> In Part 3, you will build ranked summary tables and save a final Spark result.

#### 1. Goal

You will:

- build one-row-per-service summary tables
- use `stddev` to measure variability
- use Spark window functions for rankings
- join several rankings into a final summary
- identify the busiest hour for each service
- save a Spark result as CSV
- learn the difference between Spark output folders and single CSV files

#### 2. Prerequisites

Before starting:

1. Finish [Part 2](./session-09-part-02.md).
2. Load and enrich `service_events.csv`.
3. Make sure your enriched DataFrame includes:

```txt
error_rate, total_bytes, traffic_mb, latency_band, event_date, event_hour, day_of_week
```

#### 3. Basics you should know

- A grouped summary turns many event rows into one row per group.
- `stddev` measures how much values vary.
- A window function can rank rows without collapsing the whole DataFrame.
- `dense_rank` gives equal values the same rank and does not leave gaps.
- Spark normally saves CSV output as a folder containing part files.

#### 4. Create the enriched DataFrame

Run this setup if you need a clean start:

```python
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
    .appName("Session09Part03")
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

events_df = spark.read.option("header", True).schema(schema).csv("datasets/service_events.csv")

events_enriched_df = (
    events_df
    .withColumn("error_rate", when(col("request_count") > 0, col("error_count") / col("request_count")).otherwise(0))
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
```

In Colab, change the CSV path to:

```python
.csv("service_events.csv")
```

#### 5. Build the base service summary

Run:

```python
from pyspark.sql.functions import avg, count, stddev, sum

service_summary_df = events_enriched_df.groupBy("service").agg(
    count("*").alias("total_records"),
    sum("request_count").alias("total_requests"),
    sum("error_count").alias("total_errors"),
    avg("error_rate").alias("average_error_rate"),
    avg("latency_ms").alias("average_latency_ms"),
    stddev("latency_ms").alias("latency_stddev"),
    sum("traffic_mb").alias("total_traffic_mb"),
)

service_summary_df.show()
```

Checkpoint question:

Why is this table useful for reporting?

<details>
<summary>Show answer</summary>

It gives one row per service, so a reader can compare services quickly without looking through every raw event row.

</details>

#### 6. Add rankings with window functions

Run:

```python
from pyspark.sql.functions import dense_rank
from pyspark.sql.window import Window

traffic_window = Window.orderBy(col("total_traffic_mb").desc())
variability_window = Window.orderBy(col("latency_stddev").desc())
reliability_window = Window.orderBy(col("average_error_rate").asc())

ranked_summary_df = (
    service_summary_df
    .withColumn("traffic_rank", dense_rank().over(traffic_window))
    .withColumn("latency_variability_rank", dense_rank().over(variability_window))
    .withColumn("reliability_rank", dense_rank().over(reliability_window))
)

ranked_summary_df.orderBy("traffic_rank").show()
```

What the ranks mean:

1. `traffic_rank = 1`: highest total traffic.
2. `latency_variability_rank = 1`: most variable latency.
3. `reliability_rank = 1`: lowest average error rate.

#### 7. Find the busiest hour per service

Run:

```python
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

busiest_hour_df.show()
```

Checkpoint question:

Why does this window use `partitionBy("service")`?

<details>
<summary>Show answer</summary>

It ranks hours separately inside each service, so each service gets its own busiest hour.

</details>

#### 8. Build the final service summary

Run:

```python
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
```

#### 9. Save the summary

Spark writes CSV output as a folder of part files:

```python
final_summary_df.coalesce(1).write.mode("overwrite").option("header", True).csv("results/service_summary_spark")
```

For a small class exercise, you can copy the part file to a single named CSV:

```python
from pathlib import Path
import shutil

output_folder = Path("results/service_summary_spark")
single_csv = Path("results/service_summary.csv")

part_file = next(output_folder.glob("part-*.csv"))
shutil.copy(part_file, single_csv)

print(f"Saved {single_csv}")
```

Checkpoint question:

Why does Spark save a folder instead of one CSV file by default?

<details>
<summary>Show answer</summary>

Spark is designed for distributed processing. Different workers can write different part files in the output folder.

</details>

#### 10. Exercise 3: Ranked service summary

Create a final Colab section called:

```md
## Exercise 3
```

Your notebook should:

1. Load and enrich the service events data.
2. Build a one-row-per-service summary.
3. Add traffic, latency variability, and reliability ranks.
4. Find the busiest hour per service.
5. Join the busiest hour into the final summary.
6. Save `results/service_summary.csv`.
7. Print one short interpretation:
   - Which service has the most traffic?
   - Which service has the most variable latency?
   - Which service is most reliable by average error rate?
8. Stop Spark at the end.

Minimum completion checklist:

1. The final table has one row per service.
2. The final table includes all required rank columns.
3. The busiest hour is calculated with a partitioned window.
4. A CSV result is saved.
5. Spark is stopped at the end.

#### 11. Final project connection

The final project asks for:

```txt
volatility ranking
activity ranking
time-based activity analysis
final ranked market summary
```

This part practices the same structure with different names:

```txt
latency variability ranking
traffic ranking
busiest service hour
final ranked service summary
```

Do not copy these exact service questions into the final project. Use the pattern to build the required market-data analysis.

#### 12. Quiz

```bash
quizmd quizzes/python-session-09-part-03-quiz.md
```
