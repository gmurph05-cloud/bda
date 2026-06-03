### Session 8 | Part 3

> In Part 3, you will install and test PySpark locally. This part is optional if you prefer to keep using Google Colab.

#### 1. Goal

You will:

- check that Python is installed
- check that Java is installed
- create a local virtual environment
- install PySpark from `requirements.txt`
- run a small local PySpark script
- troubleshoot common setup problems

#### 2. Prerequisites

Before starting:

1. Open the `session8` folder in Visual Studio Code.
2. Open a terminal from inside `session8`.
3. Confirm your path:

```bash
pwd
```

It should end with:

```txt
/bda/session8
```

#### 3. Basics you should know

- PySpark runs Python code that communicates with Spark on the Java Virtual Machine.
- Java must be available for local Spark.
- A virtual environment keeps project dependencies separate.
- Colab handles most setup for you; local setup gives you more control.

#### 4. Check Python and Java

Run:

```bash
python3 --version
java -version
```

Expected idea:

```txt
Python prints a 3.x version.
Java prints a version and does not say command not found.
```

> [!NOTE]
>
> Current PySpark releases require a modern Python version and Java 17 or later. If Java is missing, install a current LTS Java release before continuing.

#### 5. Create and activate a virtual environment

macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

#### 6. Install requirements

Run:

```bash
pip install -r requirements.txt
```

This installs:

```txt
pyspark==4.1.2
quizmd
```

#### 7. Create a local verification script

Create this file:

```txt
session8/solutions/exercise-08-03.py
```

Add:

```python
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
```

Run:

```bash
python3 solutions/exercise-08-03.py
```

Minimum completion checklist:

1. The script starts Spark.
2. A table prints with city, category, and revenue.
3. A grouped average prints by category.
4. The script exits without leaving Spark running.

#### 8. Common troubleshooting

If `java` is not found:

```txt
Install Java 17 or later, then open a new terminal.
```

If PySpark cannot start:

```txt
Check that Java works with java -version.
Check that your virtual environment is activated.
Run pip install -r requirements.txt again.
```

If Python cannot find your file:

```txt
Run the script from inside the session8 folder.
```

#### 9. Quiz

```bash
quizmd quizzes/python-session-08-part-03-quiz.md
```
