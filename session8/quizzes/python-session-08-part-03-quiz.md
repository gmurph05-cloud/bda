# Session 8 Part 3 Quiz (Local PySpark Setup)

## Question 1

Why does local PySpark need Java?

- Spark runs on the Java Virtual Machine
- Java replaces Python syntax
- Java stores the quiz answers
- Java is only needed for Markdown files

Answer: 1
Type: single
Time: 45
Explanation: Local Spark uses the JVM, and PySpark communicates with it from Python.

## Question 2

Which command checks the installed Java version?

- `java -version`
- `pip java`
- `python java`
- `spark version java`

Answer: 1
Type: single
Time: 40
Explanation: `java -version` prints the Java version if Java is installed.

## Question 3

Why create a virtual environment?

- To keep this session's Python dependencies separate
- To delete Java
- To make Colab mandatory
- To convert Markdown to SQL

Answer: 1
Type: single
Time: 45
Explanation: A virtual environment isolates project packages.

## Question 4

Which command installs the session requirements?

- `pip install -r requirements.txt`
- `python requirements.txt`
- `java install requirements.txt`
- `git install requirements.txt`

Answer: 1
Type: single
Time: 45
Explanation: `pip install -r requirements.txt` installs packages listed in the requirements file.

## Question 5

Where should students run `python3 solutions/exercise-08-03.py` from?

- Inside the `session8` folder
- Inside the `.git` folder
- From Google search
- From the operating system trash

Answer: 1
Type: single
Time: 45
Explanation: Running from `session8` keeps relative paths and session instructions simple.

## Question 6

What should the local verification script do?

- Start Spark, create a small DataFrame, summarize it, and stop Spark
- Delete the virtual environment
- Upload all files to Colab
- Install pandas only

Answer: 1
Type: single
Time: 50
Explanation: The local script checks that PySpark can start and run a small job.

## Question 7

What should you check first if PySpark cannot start locally?

- Whether Java works with `java -version`
- Whether the quiz title is long enough
- Whether the notebook has emojis
- Whether SQL keywords are lowercase

Answer: 1
Type: single
Time: 45
Explanation: Missing or incompatible Java is a common local Spark setup issue.

## Question 8

Which file lists the local dependencies for Session 8?

- `requirements.txt`
- `README.sql`
- `spark.lock`
- `java.md`

Answer: 1
Type: single
Time: 40
Explanation: The requirements file lists packages to install with pip.

## Question 9

What does `spark.stop()` do in the local verification script?

- Releases the Spark session resources
- Deletes `requirements.txt`
- Removes Java from the computer
- Converts the script into a notebook

Answer: 1
Type: single
Time: 45
Explanation: `spark.stop()` shuts down the Spark session created by the script.

## Question 10

If Python says it cannot find `solutions/exercise-08-03.py`, what should you check?

- That you are running the command from inside the `session8` folder
- That SQL has a `GROUP BY`
- That Colab is closed
- That the file has exactly 12 rows

Answer: 1
Type: single
Time: 45
Explanation: The command in the tutorial assumes the terminal is currently inside `session8`.
