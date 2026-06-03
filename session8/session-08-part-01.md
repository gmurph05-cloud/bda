### Session 8 | Part 1

> In Part 1, you will run your first PySpark tutorial in Google Colab. The goal is to learn the Spark workflow before worrying about local installation.

#### 1. Goal

You will:

- explain what Apache Spark and PySpark are used for
- open a Google Colab notebook
- install PySpark in Colab
- start a local Spark session inside Colab
- create a Spark DataFrame from Python data
- inspect rows, columns, schema, and counts
- use simple DataFrame transformations
- stop Spark when you are done

#### 2. Prerequisites

Before starting:

1. Open [Google Colab](https://colab.research.google.com/) and log in using your personal Gmail account.
2. Create a new notebook.
3. Rename it:

```txt
session-08-part-01-pyspark-intro
```

4. Add a text cell at the top with:

```md
# Session 8 Part 1: PySpark in Google Colab
```

5. Run each code cell in order.

> [!NOTE]
>
> Colab sessions reset. If you reconnect later, run the install and Spark setup cells again.

#### 3. Basics you should know

- Apache Spark: a distributed data processing engine.
- PySpark: the Python API for Apache Spark.
- SparkSession: the main entry point for working with Spark from PySpark.
- DataFrame: a distributed table with rows and columns.
- transformation: a lazy operation that describes work, such as `filter`.
- action: an operation that triggers work, such as `show` or `count`.
- schema: the column names and data types in a DataFrame.
- local mode: Spark running on one machine, useful for learning and small practice jobs.

Checkpoint question:

What is the difference between a DataFrame and a regular Python list?

<details>
<summary>Show answer</summary>

A Python list lives in normal Python memory and is usually processed directly by Python. A Spark DataFrame represents table-like data that Spark can process using its execution engine, including on larger datasets and clusters.

</details>

#### 4. Install PySpark in Colab

Some Google Colab runtimes may already have PySpark available. Run this first to test it:

```python
from pyspark.sql import SparkSession
```

If the import works, continue to the next section.

If PySpark is not installed, run this in a Colab code cell:

```python
!pip install pyspark==4.1.2
```

After the install finishes, restart the runtime only if Colab asks you to.

Checkpoint question:

Why do we test the import before installing PySpark?

<details>
<summary>Show answer</summary>

Because the Colab environment can change. Testing first avoids installing a package that is already available, but the install command is still there as a fallback.

</details>

#### 5. Start Spark

Create a Spark session:

```python
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("Session08Part01")
    .master("local[*]")
    .getOrCreate()
)

spark
```

What this means:

1. `SparkSession.builder` starts the setup.
2. `appName(...)` gives the Spark job a readable name.
3. `master("local[*]")` tells Spark to use local mode with available CPU cores.
4. `getOrCreate()` starts Spark or reuses an existing session.

Checkpoint question:

What does `local[*]` mean in this tutorial?

<details>
<summary>Show answer</summary>

It means Spark runs locally inside the Colab runtime and can use the available local CPU cores. This is enough for learning PySpark without connecting to a real Spark cluster.

</details>

Checkpoint question:

Why do we use `getOrCreate()` instead of always creating a brand-new Spark session?

<details>
<summary>Show answer</summary>

In a notebook, cells can be run more than once. `getOrCreate()` reuses an existing Spark session if one already exists, which is friendlier for interactive notebook work.

</details>

#### 6. Create your first Spark DataFrame

Run:

```python
students = [
    ("Ava", "Data Analytics", 92),
    ("Nikos", "Data Engineering", 85),
    ("Maya", "Data Analytics", 78),
    ("Leo", "Business", 88),
    ("Iris", "Data Engineering", 95),
]

columns = ["name", "track", "score"]

df = spark.createDataFrame(students, columns)

df.show()
```

Expected idea:

```txt
Spark prints a table with name, track, and score.
```

Checkpoint question:

Why do we pass `columns` separately instead of leaving Spark to guess every column name?

<details>
<summary>Show answer</summary>

The rows are tuples, so they do not contain column names. Passing `columns` gives the DataFrame readable names such as `name`, `track`, and `score`.

</details>

Task: Add two more students to the `students` list and run the cell again.

<details>
<summary>Show solution idea</summary>

```python
students = [
    ("Ava", "Data Analytics", 92),
    ("Nikos", "Data Engineering", 85),
    ("Maya", "Data Analytics", 78),
    ("Leo", "Business", 88),
    ("Iris", "Data Engineering", 95),
    ("Elena", "Business", 81),
    ("Omar", "Data Analytics", 90),
]
```

</details>

#### 7. Inspect the DataFrame

Run:

```python
df.printSchema()
print("Rows:", df.count())
print("Columns:", df.columns)
```

What this shows:

1. `printSchema()` shows column names and inferred data types.
2. `count()` counts rows.
3. `columns` lists the column names.

Checkpoint question:

Which command is an action: `printSchema`, `count`, or `columns`?

<details>
<summary>Show answer</summary>

`count()` is the clearest action here because it asks Spark to compute a result from the data.

</details>

Checkpoint question:

Why is checking the schema useful before writing filters or calculations?

<details>
<summary>Show answer</summary>

The schema tells you which columns exist and what data type Spark thinks each column contains. This helps you avoid mistakes such as doing numeric comparisons on text columns.

</details>

#### 8. Select columns

Use `select` to choose columns:

```python
df.select("name", "score").show()
```

Checkpoint question:

Does `select("name", "score")` change the original `df`?

<details>
<summary>Show answer</summary>

No. Spark DataFrame operations return a new DataFrame. The original `df` still has all of its columns unless you assign the selected result to a variable.

</details>

Task: Show only the `name` and `track` columns.

<details>
<summary>Show solution</summary>

```python
df.select("name", "track").show()
```

</details>

#### 9. Select with expressions and conditions

`select` can do more than choose existing columns. It can also show calculated expressions.

Import `col` and `when`:

```python
from pyspark.sql.functions import col, when
```

Now select the name, the score, and a calculated score:

```python
df.select(
    "name",
    "score",
    (col("score") + 5).alias("score_plus_5")
).show()
```

Checkpoint question:

Why do we use `alias("score_plus_5")` here?

<details>
<summary>Show answer</summary>

The expression `col("score") + 5` would otherwise have a long generated name. `alias` gives the calculated column a clear name in the output.

</details>

You can also use a condition inside `select`:

```python
df.select(
    "name",
    "track",
    "score",
    when(col("score") >= 85, "pass").otherwise("review").alias("result")
).show()
```

What this shows:

1. `when(...)` checks a condition.
2. `otherwise(...)` gives the value when the condition is false.
3. `alias("result")` names the new output column.

Checkpoint question:

Does this conditional `select` permanently add the `result` column to `df`?

<details>
<summary>Show answer</summary>

No. It only shows a selected output with a calculated column. If you want to keep the new column, use `withColumn` and assign the result to a variable.

</details>

Task: Select `name`, `score`, and a new column named `score_level`.

Use:

- `"excellent"` when the score is at least `90`
- `"good"` when the score is at least `80`
- `"needs review"` for all other scores

<details>
<summary>Show solution</summary>

```python
df.select(
    "name",
    "score",
    when(col("score") >= 90, "excellent")
    .when(col("score") >= 80, "good")
    .otherwise("needs review")
    .alias("score_level")
).show()
```

</details>

#### 10. Filter rows

Use `filter` to keep rows that match a condition:

```python
df.filter(df["score"] >= 90).show()
```

Checkpoint question:

What rows should this filter keep?

<details>
<summary>Show answer</summary>

It should keep only students whose `score` is greater than or equal to `90`.

</details>

Task: Show students whose score is less than `85`.

<details>
<summary>Show solution</summary>

```python
df.filter(df["score"] < 85).show()
```

</details>

You can also filter first and then select only the columns you want to show:

```python
df.filter(col("score") >= 85).select("name", "track", "score").show()
```

Checkpoint question:

What is the difference between this code and `df.select("name", "track", "score")`?

<details>
<summary>Show answer</summary>

`df.select("name", "track", "score")` shows those columns for every row. `df.filter(col("score") >= 85).select(...)` first keeps only high-score rows, then shows the selected columns.

</details>

Task: Show only the `name` and `score` columns for students in the `Data Analytics` track.

<details>
<summary>Show solution</summary>

```python
df.filter(col("track") == "Data Analytics").select("name", "score").show()
```

</details>

#### 11. Create a new column

Import `col` and `when`:

```python
from pyspark.sql.functions import col, when

graded_df = df.withColumn(
    "result",
    when(col("score") >= 85, "pass").otherwise("review")
)

graded_df.show()
```

Checkpoint question:

Why do we save the result as `graded_df` instead of expecting `df` to change automatically?

<details>
<summary>Show answer</summary>

Spark DataFrames are immutable. `withColumn` returns a new DataFrame with the extra column, so assigning it to `graded_df` keeps the new version.

</details>

Task: Add a new column named `score_plus_5` that adds 5 points to each score.

<details>
<summary>Show solution</summary>

```python
df.withColumn("score_plus_5", col("score") + 5).show()
```

</details>

#### 12. Group and summarize

Use `groupBy` to summarize by category:

```python
df.groupBy("track").count().show()
```

Checkpoint question:

What does each row in this grouped result represent?

<details>
<summary>Show answer</summary>

Each row represents one `track`, plus the number of students in that track.

</details>

Now calculate average score by track:

```python
from pyspark.sql.functions import avg

df.groupBy("track").agg(avg("score").alias("average_score")).show()
```

Checkpoint question:

Why do we use `alias("average_score")`?

<details>
<summary>Show answer</summary>

Without an alias, Spark may show a generated column name such as `avg(score)`. The alias gives the summary column a clean readable name.

</details>

Task: Find the maximum score in each track.

<details>
<summary>Show solution</summary>

```python
from pyspark.sql.functions import max

df.groupBy("track").agg(max("score").alias("max_score")).show()
```

</details>

#### 13. Exercise 1: PySpark student summary

Create a final Colab section called:

```md
## Exercise 1
```

Your notebook should:

1. Install PySpark.
2. Start a Spark session.
3. Create a DataFrame with at least 8 students.
4. Include these columns:
   - `name`
   - `track`
   - `score`
   - `hours_studied`
5. Print the schema.
6. Show the first 5 rows.
7. Filter students with score `>= 85`.
8. Add a `result` column with `pass` or `review`.
9. Group by `track` and show:
   - number of students
   - average score
   - average hours studied
10. Stop Spark at the end.

Suggested skeleton:

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col, count, when


spark = (
    SparkSession.builder
    .appName("Session08Exercise01")
    .master("local[*]")
    .getOrCreate()
)

students = [
    # TODO: add at least 8 rows
]

columns = ["name", "track", "score", "hours_studied"]

df = spark.createDataFrame(students, columns)

# TODO: print schema
# TODO: show first 5 rows
# TODO: filter high scores
# TODO: add result column
# TODO: group by track

spark.stop()
```

Minimum completion checklist:

1. The notebook runs from top to bottom in Colab.
2. A Spark session starts successfully.
3. The DataFrame has at least 8 rows.
4. The summary groups by `track`.
5. Spark is stopped at the end.

<details>
<summary>Show hint</summary>

Use `df.show(5)` for the first 5 rows. Use `groupBy("track").agg(...)` for multiple summary calculations.

</details>

#### 14. Quiz

```bash
quizmd quizzes/python-session-08-part-01-quiz.md
```
