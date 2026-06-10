### Session 9 | Homework

> In this homework, you will build a small advanced Spark analytics report using service activity logs.

#### 1. Goal

You will:

- load a CSV file with Spark
- create derived numeric and category columns
- create time features
- run Spark SQL grouped analytics
- build rankings with window functions
- save a final one-row-per-service summary
- explain the results in plain English

#### 2. What to do

Create a Colab notebook named:

```txt
session-09-homework-advanced-spark
```

Use the dataset:

```txt
datasets/service_events.csv
```

If you use Colab, upload the CSV file to the notebook first.

Use this path in Colab after uploading the file:

```python
events_path = "service_events.csv"
```

Use this path locally from the `session9` folder:

```python
events_path = "datasets/service_events.csv"
```

Your notebook should:

1. Install PySpark if needed.
2. Start a Spark session.
3. Load the CSV using an explicit schema.
4. Print the schema, row count, and column names.
5. Add:
   - `error_rate`
   - `total_bytes`
   - `traffic_mb`
   - `latency_band`
   - `event_date`
   - `event_hour`
   - `day_of_week`
6. Register a temporary view named `service_events_enriched`.
7. Write at least six Spark SQL queries.
8. Include at least three grouped summaries.
9. Include at least two sorted rankings.
10. Include at least one time-based query using `event_hour` or `event_date`.
11. Build a final one-row-per-service summary with rank columns.
12. Save the final result as:

```txt
results/service_summary.csv
```

13. Stop Spark at the end.

#### 3. Required questions

Answer these in your notebook:

1. Which service has the highest total traffic?
2. Which service has the highest average latency?
3. Which service has the lowest average error rate?
4. Which hour has the most requests overall?
5. Which region has the highest total traffic?
6. How many fast, normal, and slow latency rows are there?

Then create a final summary table with one row per service including:

```txt
service, total_records, total_requests, total_errors, average_error_rate,
average_latency_ms, latency_stddev, total_traffic_mb,
busiest_hour, traffic_rank, latency_variability_rank, reliability_rank
```

#### 4. File to submit in this repository

Create this file:

```txt
session9/solutions/exercise-09-homework.md
```

Your markdown file should include:

~~~md
# Session 9 Homework

## Colab notebook

Link:

## Dataset loaded

Describe the CSV path, row count, and columns.

## Derived columns

List the derived columns you created and what each one means.

## SQL queries

Paste your six Spark SQL queries.

## Final summary

Paste or describe your final one-row-per-service summary.

## Results

Explain three interesting findings in plain English.

## Final project connection

Explain how this homework prepares you for the Spark analytics part of the final project.
~~~

#### 5. Rules

- Use PySpark.
- Use Google Colab unless you completed local setup.
- Do not use pandas for the main analytics queries.
- Use Spark SQL for at least six queries.
- Use a Spark window function for at least one ranking.
- Save the final summary CSV.
- Stop Spark at the end.

#### 6. Final project preparation

This homework is not the final project. It uses a different dataset and different questions.

However, it prepares you for the final project because you practice:

- full CSV loading in Spark
- schema and row-count checks
- derived analytics columns
- time features
- grouped SQL summaries
- ranked summary tables
- saving a final CSV result

#### 7. Quiz

```bash
quizmd quizzes/python-session-09-homework-quiz.md
```
