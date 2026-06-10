### Session 9 | Part 2

> In Part 2, you will create derived columns and time features in Spark.

#### 1. Goal

You will:

- add calculated columns with `withColumn`
- use `when` for category labels
- calculate safe rates and traffic totals
- extract date, hour, and day of week from timestamps
- run SQL summaries using the new columns
- compare service-log features with final project market-data features

#### 2. Prerequisites

Before starting:

1. Finish [Part 1](./session-09-part-01.md).
2. Start Spark and load `service_events.csv` with the same schema.
3. Register the loaded DataFrame as `service_events`.

#### 3. Basics you should know

- `withColumn` adds or replaces a DataFrame column.
- `when(...).otherwise(...)` creates conditional values.
- `round` makes numeric output easier to read.
- `to_date`, `hour`, and `date_format` extract useful time features.
- Derived columns should be created before writing grouped analytics.

#### 4. Load the starting DataFrame

Use the same setup from Part 1. If you are continuing in the same notebook, you can reuse your existing `events_df`.

If needed, run:

```python
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
    .appName("Session09Part02")
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
```

In Colab, change the path to:

```python
.csv("service_events.csv")
```

#### 5. Add error and traffic columns

Run:

```python
from pyspark.sql.functions import col, round, when

events_enriched_df = (
    events_df
    .withColumn(
        "error_rate",
        when(col("request_count") > 0, col("error_count") / col("request_count")).otherwise(0),
    )
    .withColumn("total_bytes", col("bytes_in") + col("bytes_out"))
    .withColumn("traffic_mb", col("total_bytes") / 1048576)
)

events_enriched_df.select(
    "service",
    "request_count",
    "error_count",
    round("error_rate", 4).alias("error_rate"),
    round("traffic_mb", 2).alias("traffic_mb"),
).show(8)
```

Checkpoint question:

Why do we check `request_count > 0` before calculating `error_rate`?

<details>
<summary>Show answer</summary>

It avoids dividing by zero. Even if this dataset has positive request counts, this is a safer habit for real analytics work.

</details>

#### 6. Add a latency band

Run:

```python
events_enriched_df = events_enriched_df.withColumn(
    "latency_band",
    when(col("latency_ms") < 100, "fast")
    .when(col("latency_ms") < 160, "normal")
    .otherwise("slow"),
)

events_enriched_df.select("service", "latency_ms", "latency_band").show(8)
```

Checkpoint question:

Which final project column is similar to this kind of category label?

<details>
<summary>Show answer</summary>

`candle_direction` is similar. It labels each row based on a condition: up, down, or flat.

</details>

#### 7. Add time features

Run:

```python
from pyspark.sql.functions import date_format, hour, to_date

events_enriched_df = (
    events_enriched_df
    .withColumn("event_date", to_date(col("event_time")))
    .withColumn("event_hour", hour(col("event_time")))
    .withColumn("day_of_week", date_format(col("event_time"), "E"))
)

events_enriched_df.select(
    "event_time",
    "event_date",
    "event_hour",
    "day_of_week",
).show(8, truncate=False)
```

#### 8. Register the enriched view

Run:

```python
events_enriched_df.createOrReplaceTempView("service_events_enriched")
```

Then query the new columns:

```python
spark.sql("""
    SELECT
        service,
        ROUND(AVG(error_rate), 4) AS average_error_rate,
        ROUND(AVG(latency_ms), 2) AS average_latency_ms,
        ROUND(SUM(traffic_mb), 2) AS total_traffic_mb
    FROM service_events_enriched
    GROUP BY service
    ORDER BY average_error_rate DESC
""").show()
```

#### 9. Time-based SQL summary

Run:

```python
spark.sql("""
    SELECT
        event_hour,
        SUM(request_count) AS total_requests,
        ROUND(SUM(traffic_mb), 2) AS total_traffic_mb
    FROM service_events_enriched
    GROUP BY event_hour
    ORDER BY total_requests DESC
""").show()
```

Checkpoint question:

Why is `event_hour` useful for service analytics?

<details>
<summary>Show answer</summary>

It lets us compare activity by hour and identify when the system is busiest.

</details>

#### 10. Exercise 2: Derived columns and time analysis

Create a final Colab section called:

```md
## Exercise 2
```

Your notebook should:

1. Load the service events CSV.
2. Add `error_rate`, `total_bytes`, `traffic_mb`, and `latency_band`.
3. Add `event_date`, `event_hour`, and `day_of_week`.
4. Register a temporary view named `service_events_enriched`.
5. Write SQL queries that answer:
   - Which service has the highest average error rate?
   - Which service has the highest average latency?
   - Which hour has the most requests?
   - Which region has the most traffic?
6. Show a preview proving the derived columns exist.
7. Stop Spark at the end.

Minimum completion checklist:

1. Derived numeric columns are calculated in Spark.
2. Time features are created from `event_time`.
3. At least four SQL queries run.
4. At least one query groups by `event_hour`.
5. Spark is stopped at the end.

#### 11. Final project connection

The final project asks you to create or verify:

```txt
price_range, price_change, percent_change, candle_direction
trade_date, trade_hour, day_of_week
```

The service-log columns in this part practice the same skill:

```txt
error_rate, total_bytes, traffic_mb, latency_band
event_date, event_hour, day_of_week
```

The names are different, but the Spark pattern is the same.

#### 12. Quiz

```bash
quizmd quizzes/python-session-09-part-02-quiz.md
```
