### Session 8 | Homework

> In this homework, you will use PySpark in Google Colab to build a small SQL-style analytics report.

#### 1. Goal

You will:

- create a PySpark DataFrame in Colab
- add a calculated column
- register a temporary SQL view
- write analytics queries with Spark SQL
- explain one result in plain English

#### 2. What to do

Create a Colab notebook named:

```txt
session-08-homework-pyspark-analytics
```

Your notebook should:

1. Install PySpark.
2. Start a Spark session.
3. Create a DataFrame with at least 12 rows.
4. Use a dataset about one of these topics:
   - online orders
   - student scores
   - movie ratings
   - app events
5. Add at least one calculated column.
6. Register a temporary SQL view.
7. Write at least 4 SQL queries.
8. Include at least one grouped summary with `GROUP BY`.
9. Include at least one sorted result with `ORDER BY`.
10. Stop Spark at the end.

#### 3. File to submit in this repository

Create this file:

```txt
session8/solutions/exercise-08-homework.md
```

Your markdown file should include:

~~~md
# Session 8 Homework

## Colab notebook

Link:

## Dataset topic

Describe your rows and columns.

## Calculated column

What column did you add, and how did you calculate it?

## SQL queries

Paste your 4 SQL queries.

## Results

Explain 2 interesting results in plain English.

## Reflection

What felt easier in Spark SQL than DataFrame syntax? What felt harder?
~~~

#### 4. Rules

- Use PySpark.
- Use Google Colab unless you completed the local setup in Part 3.
- Use at least 12 rows.
- Do not use pandas for the main analytics queries.
- Stop Spark at the end of the notebook.

#### 5. Share your work

Post your completed `session8/solutions/exercise-08-homework.md` in the class discussion forum.

#### 6. Quiz

```bash
quizmd quizzes/python-session-08-homework-quiz.md
```
