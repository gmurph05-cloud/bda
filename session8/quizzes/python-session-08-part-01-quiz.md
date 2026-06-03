# Session 8 Part 1 Quiz (PySpark in Colab)

## Question 1

What is PySpark?

- A Python API for Apache Spark
- A package for editing images
- A local-only spreadsheet program
- A JavaScript web framework

Answer: 1
Type: single
Time: 40
Explanation: PySpark lets Python code use Apache Spark.

## Question 2

Why are we using Google Colab in Part 1?

- So students can run PySpark without local Spark installation
- So SQL is disabled
- So Python files cannot be created
- So Spark runs only on phones

Answer: 1
Type: single
Time: 45
Explanation: Colab provides a temporary environment where PySpark can be installed and practiced quickly.

## Question 3

Which object is the main entry point for PySpark work in this session?

- SparkSession
- DataFolder
- RequestLock
- QuizRunner

Answer: 1
Type: single
Time: 40
Explanation: `SparkSession` is used to create DataFrames and run Spark operations.

## Question 4

Which command creates a Spark DataFrame from Python rows and column names?

- `spark.createDataFrame(rows, columns)`
- `spark.readPython(rows, columns)`
- `DataFrame.open(rows, columns)`
- `spark.make_csv(rows, columns)`

Answer: 1
Type: single
Time: 45
Explanation: `createDataFrame` creates a Spark DataFrame from local Python data.

## Question 5

What does `df.printSchema()` show?

- The notebook title
- Column names and data types
- The current Git branch
- Only the first row

Answer: 2
Type: single
Time: 45
Explanation: The schema describes the DataFrame columns and their types.

## Question 6

Which operation filters students with scores of at least 90?

- `df.filter(df["score"] >= 90)`
- `df.select("score" >= 90)`
- `df.groupBy("score" >= 90)`
- `df.stop(90)`

Answer: 1
Type: single
Time: 50
Explanation: `filter` keeps rows that match the condition.

## Question 7

What does `withColumn` do?

- Adds or replaces a column
- Deletes the whole DataFrame
- Installs PySpark
- Opens Google Colab

Answer: 1
Type: single
Time: 45
Explanation: `withColumn` returns a DataFrame with a new or replaced column.

## Question 8

Which function is used in Part 1 to calculate average score by track?

- `avg`
- `install`
- `schema`
- `notebook`

Answer: 1
Type: single
Time: 40
Explanation: `avg` is an aggregate function imported from `pyspark.sql.functions`.

## Question 9

Why should we call `spark.stop()` at the end?

- To release the Spark session resources
- To delete the notebook
- To install Java
- To convert Spark code into pandas automatically

Answer: 1
Type: single
Time: 45
Explanation: Stopping Spark releases resources used by the Spark session.

## Question 10

Which statement best describes Spark local mode in this session?

- Spark runs on the current machine for practice
- Spark always uses a remote production cluster
- Spark cannot run DataFrames
- Spark only runs SQL and no Python

Answer: 1
Type: single
Time: 45
Explanation: `local[*]` runs Spark locally, which is useful for learning.
