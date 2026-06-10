# Session 9 Part 1 Quiz (Spark CSV Loading)

## Question 1

Why do we define an explicit schema before loading the CSV?

- To delete rows before loading
- To control column data types instead of relying on Spark guesses
- To turn Spark into pandas
- To create a GitHub repository

Answer: 2
Type: single
Time: 50
Explanation: An explicit schema helps Spark read timestamps and numeric columns correctly.

## Question 2

Which option tells Spark that the first CSV row contains column names?

- `.option("names", False)`
- `.option("columns", "first")`
- `.option("header", True)`
- `.schema("header")`

Answer: 3
Type: single
Time: 45
Explanation: `header=True` uses the first row as column names.

## Question 3

Which Spark type is appropriate for `event_time`?

- IntegerType
- FolderType
- GitType
- TimestampType

Answer: 4
Type: single
Time: 40
Explanation: `TimestampType` stores date and time values.

## Question 4

What does `events_df.printSchema()` show?

- Column names and data types
- Only the last row
- The current Colab username
- The saved CSV folder

Answer: 1
Type: single
Time: 45
Explanation: `printSchema` shows the DataFrame structure.

## Question 5

Which command counts rows in the DataFrame?

- `events_df.rows()`
- `events_df.count()`
- `events_df.total_columns()`
- `events_df.sql_count_only()`

Answer: 2
Type: single
Time: 45
Explanation: `count()` triggers Spark to count rows.

## Question 6

What does `createOrReplaceTempView("service_events")` do?

- Permanently saves the table to GitHub
- Converts the DataFrame to a Word document
- Gives the DataFrame a SQL name for the current Spark session
- Stops Spark

Answer: 3
Type: single
Time: 50
Explanation: A temporary view lets Spark SQL query the DataFrame by name.

## Question 7

Which query lists the distinct services?

- `SELECT ONLY service FROM service_events`
- `DISTINCT service IN service_events`
- `SHOW SERVICES FROM CSV`
- `SELECT DISTINCT service FROM service_events`

Answer: 4
Type: single
Time: 55
Explanation: `SELECT DISTINCT` returns unique values.

## Question 8

What happens to a temporary view when Spark stops?

- It becomes a permanent database table
- It disappears
- It writes itself to CSV
- It installs PySpark

Answer: 2
Type: single
Time: 45
Explanation: Temporary views live only inside the current Spark session.

## Question 9

Which dataset is used in Session 9 Part 1?

- `orders.csv`
- `Pokemon.csv`
- `service_events.csv`
- `Movies.json`

Answer: 3
Type: single
Time: 55
Explanation: Session 9 Part 1 uses the service activity log dataset named `service_events.csv`.

## Question 10

Why should Spark be stopped at the end?

- To release Spark session resources
- To delete the dataset
- To remove all Python packages
- To make SQL permanent

Answer: 1
Type: single
Time: 45
Explanation: `spark.stop()` releases resources used by the Spark session.
