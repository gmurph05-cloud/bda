### Session 8 | Part 2

> In Part 2, you will use Spark SQL and DataFrame operations to answer analytics questions.

#### 1. Goal

You will:

- create a larger PySpark DataFrame
- register a temporary SQL view
- run SQL queries with `spark.sql`
- filter, sort, group, and aggregate data
- compare SQL syntax with PySpark DataFrame syntax
- build a small analytics summary

#### 2. Prerequisites

Before starting:

1. Finish [Part 1](./session-08-part-01.md).
2. Open the same Google Colab notebook or create a new one.
3. Install PySpark if is needed and your the runtime was reset:

```python
!pip install pyspark==4.1.2
```

4. Start Spark:

```python
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("Session08Part02")
    .master("local[*]")
    .getOrCreate()
)
```

#### 3. Basics you should know

- temporary view: a SQL name for a Spark DataFrame.
- `createOrReplaceTempView`: registers a DataFrame so SQL can query it.
- `spark.sql(...)`: runs a SQL query and returns a Spark DataFrame.
- `WHERE`: filters rows.
- `GROUP BY`: creates grouped summaries.
- `ORDER BY`: sorts results.
- aggregate function: a function such as `COUNT`, `AVG`, `SUM`, `MIN`, or `MAX`.

#### 4. Create an analytics dataset

Run:

```python
orders = [
    (1, "Athens", "Laptop", "Electronics", 1, 1200.00),
    (2, "Athens", "Mouse", "Electronics", 2, 25.00),
    (3, "Thessaloniki", "Desk", "Furniture", 1, 240.00),
    (4, "Patras", "Chair", "Furniture", 4, 85.00),
    (5, "Athens", "Notebook", "Office", 10, 3.50),
    (6, "Heraklion", "Monitor", "Electronics", 2, 310.00),
    (7, "Patras", "Pen Pack", "Office", 5, 6.00),
    (8, "Thessaloniki", "Keyboard", "Electronics", 1, 75.00),
    (9, "Athens", "Desk Lamp", "Furniture", 3, 32.00),
    (10, "Heraklion", "Notebook", "Office", 20, 3.25),
]

columns = ["order_id", "city", "product", "category", "quantity", "unit_price"]

orders_df = spark.createDataFrame(orders, columns)
orders_df.show()
```

Add a revenue column:

```python
from pyspark.sql.functions import col

orders_df = orders_df.withColumn("revenue", col("quantity") * col("unit_price"))
orders_df.show()
```

#### 5. Register a SQL view

Run:

```python
orders_df.createOrReplaceTempView("orders")
```

Now query the view:

```python
spark.sql("""
    SELECT *
    FROM orders
""").show()
```

Checkpoint question:

Does `orders` become a permanent database table?

<details>
<summary>Show answer</summary>

No. It is a temporary view for the current Spark session. If the session stops, the temporary view is gone.

</details>

#### 6. Filter with SQL

Run:

```python
spark.sql("""
    SELECT order_id, city, product, revenue
    FROM orders
    WHERE revenue >= 100
""").show()
```

Task: Show only orders from `Athens`.

<details>
<summary>Show solution</summary>

```python
spark.sql("""
    SELECT order_id, city, product, revenue
    FROM orders
    WHERE city = 'Athens'
""").show()
```

</details>

#### 7. Group with SQL

Run:

```python
spark.sql("""
    SELECT
        category,
        COUNT(*) AS order_count,
        ROUND(SUM(revenue), 2) AS total_revenue
    FROM orders
    GROUP BY category
    ORDER BY total_revenue DESC
""").show()
```

Task: Group by `city` and show total revenue per city.

<details>
<summary>Show solution</summary>

```python
spark.sql("""
    SELECT
        city,
        ROUND(SUM(revenue), 2) AS total_revenue
    FROM orders
    GROUP BY city
    ORDER BY total_revenue DESC
""").show()
```

</details>

#### 8. Compare SQL and DataFrame syntax

SQL version:

```python
spark.sql("""
    SELECT category, AVG(revenue) AS average_revenue
    FROM orders
    GROUP BY category
""").show()
```

DataFrame version:

```python
from pyspark.sql.functions import avg

orders_df.groupBy("category").agg(
    avg("revenue").alias("average_revenue")
).show()
```

What this shows:

1. Both styles can answer the same question.
2. SQL is familiar if you know database queries.
3. DataFrame syntax is useful when writing Python pipelines.

#### 9. Exercise 2: SQL analytics report

Create a final Colab section called:

```md
## Exercise 2
```

Your notebook should:

1. Create the `orders_df` DataFrame.
2. Add the `revenue` column.
3. Register the DataFrame as a temporary view named `orders`.
4. Write SQL queries that answer:
   - Which city has the highest total revenue?
   - Which category has the most orders?
   - Which products have revenue greater than `100`?
   - What is the average unit price per category?
5. Write one equivalent DataFrame query for one of the SQL queries.
6. Stop Spark at the end.

Suggested skeleton:

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col, count, sum


spark = (
    SparkSession.builder
    .appName("Session08Exercise02")
    .master("local[*]")
    .getOrCreate()
)

# TODO: create orders_df
# TODO: add revenue
# TODO: create temp view
# TODO: run SQL analytics queries
# TODO: write one equivalent DataFrame query

spark.stop()
```

Minimum completion checklist:

1. SQL queries run without errors.
2. The view name is exactly `orders`.
3. Revenue is calculated as `quantity * unit_price`.
4. At least four analytics questions are answered.
5. One SQL query has an equivalent DataFrame version.

#### 10. Quiz

```bash
quizmd quizzes/python-session-08-part-02-quiz.md
```
