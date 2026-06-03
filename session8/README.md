## Welcome to Session 8

### Learning goals

By the end of Session 8, you should be able to:

- explain what Apache Spark is and why PySpark is useful
- run PySpark in Google Colab without installing Spark locally
- create and inspect Spark DataFrames
- transform data with `select`, `filter`, `withColumn`, and `groupBy`
- run SQL-style queries with Spark SQL
- install and test PySpark locally if you want a local development setup

### Recommended order

1. [Part 1: PySpark in Google Colab](./session-08-part-01.md)
2. [Part 2: SQL-style analytics with PySpark](./session-08-part-02.md)
3. [Part 3: Install Spark locally](./session-08-part-03.md)
4. [Homework](./session-08-homework.md)
5. Practice with [quizzes](./quizzes/) when ready.
6. Write your own work in [solutions](./solutions/).
7. Review [reference solutions](./session_solutions/) only after attempting tasks yourself.

### Quizzes

```bash
quizmd quizzes/python-session-08-part-01-quiz.md
quizmd quizzes/python-session-08-part-02-quiz.md
quizmd quizzes/python-session-08-part-03-quiz.md
quizmd quizzes/python-session-08-homework-quiz.md
```

### Notes

- Parts 1 and 2 are designed for Google Colab.
- Part 3 is optional for students who want to run PySpark locally.
- Tutorial and warm-up material is included directly inside each part markdown file.
- Keep your own solutions in separate files inside `solutions/`.
- Use exercise-style names in `solutions/`:
  - `exercise-08-01.py`
  - `exercise-08-02.py`
  - `exercise-08-03.py`
  - `exercise-08-homework.md`
- Reference answers are in `session_solutions/`.
- Install local dependencies with:
  - `pip install -r requirements.txt`
