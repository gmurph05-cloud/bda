
'''
To get Java 17 (or later) working in your VS Code CMD terminal, you need to install it on your actual computer system. Once installed, any terminal you open—includi

Step 1: Install Java using Windows Package Manager
Since you are already in the CMD terminal, the fastest way to install Java 17 without dealing with downloading installers manually is to use Microsoft's built-in tool, winget.

Run this command in your VS Code terminal:
winget install Oracle.JDK.17
(Alternatively, if you want the absolute latest version instead of 17, you can run winget install Oracle.JDK.21 for Java 21, which is the next long-term support version).

Step 2: Restart the Terminal
After the installation completes, the current terminal window won't know it's there yet. 1. Look at the top right of your VS Code terminal panel and click the Trash Can icon to kill the current terminal.
2. Open a new terminal (`Ctrl + Shift + ``).

Step 3: Verify the Installation
In your new terminal, type the following to make sure Windows and VS Code can see it:
java -version
You should see an output that looks like this:
java version "17.0.x" 202x-xx-xx LTS
Java(TM) SE Runtime Environment (build 17.0.x+x-LTS-xx)
Java HotSpot(TM) 64-Bit Server VM (build 17.0.x+x-LTS-xx, mixed mode, sharing)

Step 4: Get the VS Code Extension (Highly Recommended)
To actually write and run Java comfortably in VS Code, you'll want the official tools.

# 1. Click on the Extensions icon on the left sidebar of VS Code (the 4 squares).
# 2. Search for Extension Pack for Java (published by Microsoft).
# 3. Click Install.

This pack includes everything you need to get syntax highlighting, code completion, and a "Run" button for Java files, entirely independent of your Python setup!
'''
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