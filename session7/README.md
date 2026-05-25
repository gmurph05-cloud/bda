## Welcome to Session 7

### Learning goals

By the end of Session 7, you should be able to:

- explain what pandas is useful for in data analytics work
- create and inspect `Series` and `DataFrame` objects
- load tabular data and select rows and columns
- identify common data quality problems
- clean missing values, duplicates, inconsistent text, and incorrect data types
- fill missing numeric values using interpolation
- use NumPy arrays for simple numeric work

### Recommended order

1. [Part 1: Introduction to pandas](./session-07-part-01.md)
2. [Part 2: Introduction to data cleaning](./session-07-part-02.md)
3. [Part 3: Introduction to NumPy](./session-07-part-03.md)
4. [Homework](./session-07-homework.md)
5. Practice with [quizzes](./quizzes/) when ready.
6. Write your own work in [solutions](./solutions/).
7. Review [reference solutions](./session_solutions/) only after attempting tasks yourself.

### Datasets

The session datasets are in [datasets](./datasets/):

- `Movies.json`
- `Pokemon.csv`

Load them directly from your Python files with:

```python
movies = pd.read_json("datasets/Movies.json")
pokemon = pd.read_csv("datasets/Pokemon.csv", encoding="cp1252")
```

Run your Python files from the `session7` folder so these paths work as written.

### Notes

- Tutorial and warm-up material is included directly inside each part markdown file.
- Keep your own solutions in separate files inside `solutions/`.
- Use exercise-style names in `solutions/` (for example `exercise-07-01.py`, `exercise-07-02.py`, `exercise-07-03.py`, `exercise-07-homework.py`).
- Reference answers are in `session_solutions/`.
- Class datasets for this session are inside [datasets](./datasets/).
- Do not commit `.venv/` to GitHub.
- Install the requirements with:
  - `pip install -r requirements.txt`
