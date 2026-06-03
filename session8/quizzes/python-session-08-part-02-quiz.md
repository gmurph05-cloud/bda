# Session 8 Part 2 Quiz (Spark SQL Analytics)

## Question 1

What does `createOrReplaceTempView("orders")` do?

- Registers a DataFrame so it can be queried with SQL
- Permanently uploads data to Google Drive
- Deletes duplicate rows
- Installs Spark SQL

Answer: 1
Type: single
Time: 45
Explanation: A temporary view lets Spark SQL query a DataFrame by name.

## Question 2

Which command runs a SQL query in PySpark?

- `spark.sql("SELECT * FROM orders")`
- `spark.query_csv("SELECT * FROM orders")`
- `sql.run("SELECT * FROM orders")`
- `orders.sql_only("SELECT *")`

Answer: 1
Type: single
Time: 45
Explanation: `spark.sql(...)` runs SQL and returns a Spark DataFrame.

## Question 3

What does `WHERE` do in SQL?

- Filters rows
- Starts Spark
- Creates a virtual environment
- Prints the schema

Answer: 1
Type: single
Time: 40
Explanation: `WHERE` keeps rows that match a condition.

## Question 4

Which SQL clause creates summaries by category or city?

- GROUP BY
- INSTALL BY
- NOTEBOOK BY
- SCHEMA BY

Answer: 1
Type: single
Time: 40
Explanation: `GROUP BY` groups rows so aggregate functions can summarize each group.

## Question 5

Which expression calculates revenue in the session dataset?

- `quantity * unit_price`
- `city * product`
- `category + city`
- `order_id / city`

Answer: 1
Type: single
Time: 45
Explanation: Revenue is quantity multiplied by unit price.

## Question 6

Which SQL query finds total revenue by city?

- `SELECT city, SUM(revenue) FROM orders GROUP BY city`
- `SELECT city FROM orders STOP BY revenue`
- `SELECT SUM(city) FROM orders GROUP BY revenue`
- `SELECT revenue FROM city GROUP BY orders`

Answer: 1
Type: single
Time: 60
Explanation: The query groups rows by city and sums revenue in each group.

## Question 7

What does `ORDER BY total_revenue DESC` do?

- Sorts results from highest total revenue to lowest
- Deletes total revenue
- Groups results by total revenue
- Converts SQL to Python

Answer: 1
Type: single
Time: 45
Explanation: `DESC` sorts descending.

## Question 8

Which aggregate function counts rows?

- COUNT
- WHERE
- ORDER
- VIEW

Answer: 1
Type: single
Time: 40
Explanation: `COUNT(*)` counts rows in a group or query result.

## Question 9

Why compare SQL syntax with DataFrame syntax?

- Both can answer analytics questions, and each style is useful in different situations
- SQL is always wrong in PySpark
- DataFrames cannot group rows
- Spark requires both styles in every script

Answer: 1
Type: single
Time: 50
Explanation: Spark supports both SQL and DataFrame APIs.

## Question 10

What happens to a temporary view when the Spark session stops?

- It is gone
- It becomes a permanent database
- It turns into a CSV file automatically
- It is committed to GitHub

Answer: 1
Type: single
Time: 45
Explanation: Temporary views live only inside the current Spark session.
