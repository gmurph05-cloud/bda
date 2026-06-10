### Session 9 | Part 1

> In Part 1, you will load a CSV file with Spark, inspect it, and register it as a SQL view.

#### 1. Goal

You will:

- start a Spark session
- load a CSV file with an explicit schema
- inspect schema, rows, columns, and row count
- register a temporary SQL view
- run first Spark SQL checks
- connect the pattern to the final project Spark task

#### 2. Prerequisites

Before starting:

1. Finish Session 8.
2. Open [Google Colab](https://colab.research.google.com/) or work locally from the `session9` folder.
3. If you use Colab, upload `datasets/service_events.csv` into the notebook files panel.
4. If PySpark is not available, run:

```python
!pip install pyspark==4.1.2
```

5. Create a notebook named:

```txt
session-09-part-01-service-events
```

#### 3. Basics you should know

- Spark can infer CSV schemas, but an explicit schema is safer for important analytics.
- `header=True` tells Spark that the first CSV row contains column names.
- `TimestampType` stores date and time values.
- `createOrReplaceTempView` gives a DataFrame a SQL table name for the current Spark session.
- This session uses service logs. In the final project, the same ideas apply to market data.

Checkpoint question:

Why is an explicit schema useful when loading a CSV?

<details>
<summary>Show answer</summary>

It prevents Spark from guessing important data types incorrectly. This matters for numeric calculations, timestamps, and grouped analytics.

</details>

#### 4. Start Spark

Run:

```python
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("Session09Part01")
    .master("local[*]")
    .getOrCreate()
)
```

#### 5. Define the CSV schema

Run:

```python
from pyspark.sql.types import (
    DoubleType,
    IntegerType,
    StringType,
    StructField,
    StructType,
    TimestampType,
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
```

Checkpoint question:

Which columns must be numeric for later calculations?

<details>
<summary>Show answer</summary>

`request_count`, `error_count`, `latency_ms`, `bytes_in`, and `bytes_out` must be numeric because later calculations use division, sums, averages, and rankings.

</details>

#### 6. Load the CSV

In Colab, set the path to the uploaded file:

```python
events_path = "service_events.csv"
```

If you are working locally from the `session9` folder, use:

```python
events_path = "datasets/service_events.csv"
```

Then load the file:

```python
events_df = (
    spark.read
    .option("header", True)
    .schema(schema)
    .csv(events_path)
)
```

#### 7. Inspect the DataFrame

Run:

```python
events_df.printSchema()
events_df.show(5, truncate=False)

print("Rows:", events_df.count())
print("Columns:", events_df.columns)
```

Minimum expected idea:

```txt
Rows: 24
Columns include service, region, event_time, request_count, error_count, latency_ms, bytes_in, bytes_out
event_time is timestamp
```

Checkpoint question:

Which command proves that Spark has loaded all rows?

<details>
<summary>Show answer</summary>

`events_df.count()` proves how many rows Spark loaded.

</details>

#### 8. Register a SQL view

Run:

```python
events_df.createOrReplaceTempView("service_events")
```

Test the view:

```python
spark.sql("""
    SELECT service, region, event_time, request_count
    FROM service_events
    ORDER BY event_time
    LIMIT 10
""").show(truncate=False)
```

Checkpoint question:

Does `service_events` become a permanent database table?

<details>
<summary>Show answer</summary>

No. It is a temporary view for the current Spark session. It disappears when the Spark session stops.

</details>

#### 9. Exercise 1: Loading and checking service events

Create a final Colab section called `Exercise 1`.

Your notebook should:

1. Start Spark.
2. Define the explicit schema.
3. Load `service_events.csv`.
4. Print the schema, row count, and column names.
5. Register a temporary view named `service_events`.
6. Run SQL queries that answer:
   - How many rows are in the view?
   - Which services appear in the dataset?
   - How many rows does each region have?
7. Stop Spark at the end.

Suggested skeleton:

```python
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("Session09Exercise01")
    .master("local[*]")
    .getOrCreate()
)

# TODO: define schema
# TODO: load CSV
# TODO: inspect data
# TODO: create temp view
# TODO: run SQL checks

spark.stop()
```

Minimum completion checklist:

1. The schema uses numeric and timestamp types.
2. The row count prints.
3. The view name is exactly `service_events`.
4. At least three SQL checks run.
5. Spark is stopped at the end.

#### 10. Final project connection

In the final project, Team 3 starts by loading:

```txt
data/clean/cleaned_market_data.csv
```

The same pattern applies:

1. load the cleaned CSV with Spark
2. inspect schema, rows, and columns
3. register a temporary SQL view
4. run a small test query before deeper analytics

#### 11. Quiz

```bash
quizmd quizzes/python-session-09-part-01-quiz.md
```
