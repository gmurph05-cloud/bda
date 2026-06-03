from pyspark.sql import SparkSession
from pyspark.sql.functions import avg


spark = (
    SparkSession.builder
    .appName("Session08LocalCheck")
    .master("local[*]")
    .getOrCreate()
)

data = [
    ("Athens", "Electronics", 1200.00),
    ("Athens", "Office", 35.00),
    ("Patras", "Furniture", 340.00),
    ("Heraklion", "Electronics", 620.00),
]

df = spark.createDataFrame(data, ["city", "category", "revenue"])

df.show()
df.groupBy("category").agg(avg("revenue").alias("average_revenue")).show()

spark.stop()
