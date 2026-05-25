# Session 7 Part 1 quiz

## Question 1

What is a pandas DataFrame?

- A Python package manager.
- A table-like object with rows and columns.
- A folder that stores datasets.
- A command used to activate a virtual environment.

Answer: 2
Type: single
Time: 45
Explanation: A DataFrame is a labelled table of data.


## Question 2

Which command loads `Movies.json` into pandas?

- `pd.read_csv("datasets/Movies.json")`
- `pd.read_json("datasets/Movies.json")`
- `pd.open_json("datasets/Movies.json")`
- `pd.load("datasets/Movies.json")`

Answer: 2
Type: single
Time: 45
Explanation: JSON files can be loaded with `pd.read_json`.


## Question 3

What does `movies.shape` show?

- The number of missing values only.
- The first five rows.
- The number of rows and columns.
- The data type of each column.

Answer: 3
Type: single
Time: 45
Explanation: `shape` returns `(rows, columns)`.


## Question 4

Which command shows the data type of each column?

- `movies.dtypes`
- `movies.columns`
- `movies.head()`
- `movies.tail()`

Answer: 1
Type: single
Time: 45
Explanation: `dtypes` lists the inferred type of each column.


## Question 5

What does this code do?

```python
movies[movies["IMDB Rating"] >= 8]
```

- It deletes movies with low ratings.
- It filters rows where `IMDB Rating` is at least 8.
- It renames the `IMDB Rating` column.
- It sorts all movies by rating.

Answer: 2
Type: single
Time: 60
Explanation: The condition keeps only rows where the rating is greater than or equal to 8.


## Question 6

Why should you inspect a dataset before cleaning it?

- To understand columns, types, and possible problems.
- To make the file smaller.
- To avoid writing Python code.
- To remove all missing values automatically.

Answer: 1
Type: single
Time: 45
Explanation: Inspection helps you decide what cleaning is appropriate.


## Question 7

Which method counts how often each value appears in a column?

- `value_counts()`
- `shape()`
- `head()`
- `read_json()`

Answer: 1
Type: single
Time: 45
Explanation: `value_counts()` counts values in a Series.


## Question 8

Which command sorts movies by `IMDB Rating` from highest to lowest?

- `movies.sort_values("IMDB Rating", ascending=False)`
- `movies.sort_values("IMDB Rating", ascending=True)`
- `movies.value_counts("IMDB Rating")`
- `movies.head("IMDB Rating")`

Answer: 1
Type: single
Time: 60
Explanation: `ascending=False` sorts the largest values first.
