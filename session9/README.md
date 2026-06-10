## Welcome to Session 9

### Learning goals

By the end of Session 9, you should be able to:

- load CSV data into Spark with a clear schema
- inspect rows, columns, data types, and row counts
- register Spark DataFrames as temporary SQL views
- create derived columns with Spark DataFrame functions
- extract date, hour, and day-of-week features from timestamps
- write grouped and sorted Spark SQL analytics queries
- build rankings with Spark window functions
- save a final Spark summary CSV for reporting

### Recommended order

1. [Part 1: Load service events with Spark](./session-09-part-01.md)
2. [Part 2: Derived columns and time features](./session-09-part-02.md)
3. [Part 3: Rankings and final summary tables](./session-09-part-03.md)
4. [Homework](./session-09-homework.md)
5. Practice with [quizzes](./quizzes/) when ready.
6. Write your own work in [solutions](./solutions/).
7. Review [reference solutions](./session_solutions/) only after attempting tasks yourself.

### Dataset

The tutorial dataset is:

```txt
datasets/service_events.csv
```

It contains small cloud service activity logs with service names, regions, timestamps, request counts, error counts, latency, and traffic columns.

Run local Python files from the `session9` folder so this path works as written:

```python
events_path = "datasets/service_events.csv"
```

In Google Colab, if you upload the CSV directly into the notebook files panel, use:

```python
events_path = "service_events.csv"
```

### Quizzes

```bash
quizmd quizzes/python-session-09-part-01-quiz.md
quizmd quizzes/python-session-09-part-02-quiz.md
quizmd quizzes/python-session-09-part-03-quiz.md
quizmd quizzes/python-session-09-homework-quiz.md
```

### Notes

- The tutorial parts are written for Google Colab first, but the same code also works locally.
- Part 3 shows patterns that are useful for the final project Spark analytics section.
- This session uses service logs instead of market data so you can practice the same Spark skills without copying final project answers.
- Keep your own solutions in separate files inside `solutions/`.
- Use exercise-style names in `solutions/`:
  - `exercise-09-01.py`
  - `exercise-09-02.py`
  - `exercise-09-03.py`
  - `exercise-09-homework.md`
- Reference answers are in `session_solutions/`.
- Install local dependencies with:
  - `pip install -r requirements.txt`
