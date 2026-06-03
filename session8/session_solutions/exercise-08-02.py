from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col, count, sum


spark = (
    SparkSession.builder
    .appName("Session08Exercise02")
    .master("local[*]")
    .getOrCreate()
)

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
orders_df = orders_df.withColumn("revenue", col("quantity") * col("unit_price"))
orders_df.createOrReplaceTempView("orders")

spark.sql("""
    SELECT
        city,
        ROUND(SUM(revenue), 2) AS total_revenue
    FROM orders
    GROUP BY city
    ORDER BY total_revenue DESC
    LIMIT 1
""").show()

spark.sql("""
    SELECT
        category,
        COUNT(*) AS order_count
    FROM orders
    GROUP BY category
    ORDER BY order_count DESC
    LIMIT 1
""").show()

spark.sql("""
    SELECT product, revenue
    FROM orders
    WHERE revenue > 100
    ORDER BY revenue DESC
""").show()

spark.sql("""
    SELECT
        category,
        ROUND(AVG(unit_price), 2) AS average_unit_price
    FROM orders
    GROUP BY category
    ORDER BY average_unit_price DESC
""").show()

orders_df.groupBy("city").agg(
    sum("revenue").alias("total_revenue"),
    count("*").alias("order_count"),
    avg("unit_price").alias("average_unit_price"),
).orderBy(col("total_revenue").desc()).show()

spark.stop()
