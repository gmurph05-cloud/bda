# Session 8 Homework

## Colab notebook

Link: https://colab.research.google.com/drive/1KtsDBgAkMWTUI08GsNK01r3xO1Zutxu5?usp=sharing

## Dataset topic

Describe your rows and columns.

---

## Online Orders Dataset

### Row Description

Each row represents a **single item within a unique transaction**. If a customer bought multiple distinct products in one session, they would appear as separate rows with the same order ID.

### Column Specifications

| Column Name  | Data Type (Inferred) | Description                                           | Example Value   |
| ------------ | -------------------- | ----------------------------------------------------- | --------------- |
| `order_id`   | Integer              | A unique identifier for the transaction.              | `1001`          |
| `city`       | String               | The US city where the order was placed or shipped.    | `"New York"`    |
| `product`    | String               | The name of the specific item purchased.              | `"Laptop"`      |
| `category`   | String               | The retail department the product belongs to.         | `"Electronics"` |
| `quantity`   | Integer              | The number of units purchased for this specific item. | `1`             |
| `unit_price` | Double / Float       | The price of a single unit of the product in USD.     | `799.99`        |

---

## Student Scores Dataset

### Row Description

Each row captures a **student's performance in an individual academic subject**. This long-format structure allows multiple rows per student ID, making it ideal for tracking subject-specific metrics.

### Column Specifications

| Column Name    | Data Type (Inferred) | Description                                                          | Example Value |
| -------------- | -------------------- | -------------------------------------------------------------------- | ------------- |
| `student_id`   | Integer              | A unique identifier assigned to each student.                        | `1`           |
| `student_name` | String               | The first name of the student.                                       | `"Koshala"`   |
| `class_grade`  | String               | The high school grade level the student is enrolled in.              | `"10th"`      |
| `subject`      | String               | The academic discipline being assessed.                              | `"Math"`      |
| `score`        | Integer              | The final grade numerical score (out of 100).                        | `85`          |
| `passed`       | Boolean              | Flag indicating if the score meets the passing threshold ($\ge 60$). | `True`        |

---

## Movie Ratings Dataset

### Row Description

Each row logs a **single review or rating submitted by a user for a specific movie**. Users can appear multiple times if they have rated more than one film.

### Column Specifications

| Column Name      | Data Type (Inferred) | Description                                           | Example Value  |
| ---------------- | -------------------- | ----------------------------------------------------- | -------------- |
| `user_id`        | Integer              | A unique identifier for the community member.         | `501`          |
| `movie_title`    | String               | The official title of the rated film.                 | `"The Matrix"` |
| `genre`          | String               | The primary cinematic genre of the movie.             | `"Sci-Fi"`     |
| `rating`         | Integer              | The user score measured on a 1-to-5 star scale.       | `5`            |
| `review_year`    | Integer              | The calendar year the user submitted the rating.      | `2026`         |
| `is_recommended` | Boolean              | Indicates whether the user gave a positive thumbs-up. | `True`         |

---

## App Events Dataset

### Row Description

Each row records a **discrete telemetry event or action** taken by a user inside a digital application interface. This tracks user clickstreams sequentially.

### Column Specifications

| Column Name        | Data Type (Inferred) | Description                                                  | Example Value |
| ------------------ | -------------------- | ------------------------------------------------------------ | ------------- |
| `event_id`         | String               | A unique hexadecimal or alphanumeric string per action.      | `"ev_01"`     |
| `user_id`          | Integer              | The unique account identifier of the active user.            | `101`         |
| `device_type`      | String               | The hardware ecosystem used to access the application.       | `"Mobile"`    |
| `event_type`       | String               | The specific action type performed by the user.              | `"login"`     |
| `page_url`         | String               | The relative website path where the event fired.             | `"/home"`     |
| `session_duration` | Integer              | The time in seconds the user spent active during that event. | `12`          |

## Calculated column

What column did you add, and how did you calculate it?

```python
df_orders = df_orders.withColumn("revenue", col("quantity") * col("unit_price"))
df_orders.show()
```

## SQL queries

Paste your 4 SQL queries.

```python
df_orders.createOrReplaceTempView("orders")

spark.sql("""
    SELECT *
    FROM orders
""").show()

spark.sql("""
    SELECT order_id, city, product, revenue
    FROM orders
    WHERE revenue >= 50
""").show()

spark.sql("""
    SELECT order_id, city, product, revenue
    FROM orders
    WHERE city == "London"
""").show()

spark.sql("""
    SELECT
        city,
        COUNT(*) AS order_count,
        ROUND(SUM(revenue), 2) AS total_revenue
    FROM orders
    GROUP BY city
    ORDER BY total_revenue DESC
""").show()
```

## Results

Explain 2 interesting results in plain English.

1. Regional Revenue and Order Volume
   The final aggregation query provides a clear picture of which locations are driving your business. By grouping data by city, this query surfaces your top-performing markets.

```python
   spark.sql("""
    SELECT
        city,
        COUNT(*) AS order_count,
        ROUND(SUM(revenue), 2) AS total_revenue
    FROM orders
    GROUP BY city
    ORDER BY total_revenue DESC
""").show()
```

2. High-Value vs. Low-Value Customer Segments
   The second and third queries create a stark contrast by filtering data based on price thresholds versus geographic boundaries.

```python
spark.sql("""
    SELECT order_id, city, product, revenue
    FROM orders
    WHERE revenue >= 50
""").show()

spark.sql("""
    SELECT order_id, city, product, revenue
    FROM orders
    WHERE city == "London"
""").show()
```

```txt
+--------+------+--------------+-------+
|order_id|  city|       product|revenue|
+--------+------+--------------+-------+
|    1001|London|        Laptop| 799.99|
|    1003|London|    Headphones|  120.0|
|    1006|  Rhye|  Coffee Maker|  89.99|
|    1008|London|    Smartphone| 699.99|
|    1009|  Rhye|      Yoga Mat|   50.0|
|    1012|London|Wireless Mouse|  122.5|
+--------+------+--------------+-------+

+--------+------+--------------+-------+
|order_id|  city|       product|revenue|
+--------+------+--------------+-------+
|    1001|London|        Laptop| 799.99|
|    1003|London|    Headphones|  120.0|
|    1008|London|    Smartphone| 699.99|
|    1012|London|Wireless Mouse|  122.5|
+--------+------+--------------+-------+
```

## Reflection

What felt easier in Spark SQL than DataFrame syntax? What felt harder?

- **Simultaneous Operations in SQL:** Creating a new column, grouping by another, and rounding the results can all happen concurrently in a clean, highly visual layout.
- **Chained DataFrame Syntax:** You often end up chaining an unreadable mountain of methods together (e.g., `.groupBy().agg().withColumnRenamed().orderBy()`), where missing a single closing parenthesis `)` breaks the entire block.
- **Intuitive Logical Conditions:** Writing complex, multi-layered conditional logic is usually much more natural and intuitive to structure in SQL than in DataFrame syntax.
