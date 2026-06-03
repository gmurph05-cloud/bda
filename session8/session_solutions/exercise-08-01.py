from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col, count, when


spark = (
    SparkSession.builder
    .appName("Session08Exercise01")
    .master("local[*]")
    .getOrCreate()
)

students = [
    ("Ava", "Data Analytics", 92, 12),
    ("Nikos", "Data Engineering", 85, 10),
    ("Maya", "Data Analytics", 78, 7),
    ("Leo", "Business", 88, 9),
    ("Iris", "Data Engineering", 95, 14),
    ("Elena", "Business", 81, 8),
    ("Omar", "Data Analytics", 90, 11),
    ("Sofia", "Data Engineering", 74, 6),
]

columns = ["name", "track", "score", "hours_studied"]

df = spark.createDataFrame(students, columns)

df.printSchema()
df.show(5)

df.filter(col("score") >= 85).show()

graded_df = df.withColumn(
    "result",
    when(col("score") >= 85, "pass").otherwise("review"),
)

graded_df.show()

graded_df.groupBy("track").agg(
    count("*").alias("student_count"),
    avg("score").alias("average_score"),
    avg("hours_studied").alias("average_hours_studied"),
).show()

spark.stop()
