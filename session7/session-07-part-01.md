### Session 7 | Part 1

> Pandas is a library for working with tables in Python. Do not rush through the output. Read the column names, read the data types, and ask what each command is showing you.

#### 1. Goal

In this tutorial, you will:

- import pandas
- load a JSON dataset as a DataFrame
- inspect rows, columns, data types, and summary statistics
- select columns and filter rows
- create simple new columns
- sort data and count categories
- use small pandas methods to answer dataset questions

This part reuses the same exercise style as the previous analytic tools material: load a dataset, inspect it, and answer questions with code.

#### 2. Prerequisites

Before starting:

1. Open the `session7` folder in Visual Studio Code.
2. Create and activate your virtual environment.
3. Install the requirements:

```bash
pip install -r requirements.txt
```

4. Create your exercise file:

```txt
session7/solutions/exercise-07-01.py
```

#### 3. Basics you should know

- `pandas`: a Python library for working with tabular data.
- `DataFrame`: a table with rows and columns.
- `Series`: one column from a DataFrame.
- `pd.read_json(...)`: loads a JSON file into a DataFrame.
- `pd.read_csv(...)`: loads a CSV file into a DataFrame.
- `head()`: shows the first rows.
- `tail()`: shows the last rows.
- `dtypes`: shows the data type of each column.
- `describe()`: gives summary statistics for numeric columns.
- `shape`: shows the number of rows and columns.

#### 4. Load the movies dataset

The dataset is already in:

```txt
session7/datasets/Movies.json
```

File: `session7/solutions/exercise-07-01.py`

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")

print(movies)
```

> [!TIP]
>
> If Python says the file cannot be found, check that you are running the script from the `session7` folder.

Task: Print only the first 10 rows after loading the dataset.

<details>
<summary>Show solution</summary>

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")

print(movies.head(10))
```

</details>

#### 5. Inspect the first and last rows

It is usually better to inspect a few rows instead of printing the whole dataset.

File: `session7/solutions/exercise-07-01.py`

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")

print(movies.head())
print(movies.tail(3))
```

Expected idea:

```txt
The first output shows the first 5 rows.
The second output shows the last 3 rows.
```

Task: Print the first 8 rows and the last 8 rows.

<details>
<summary>Show solution</summary>

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")

print(movies.head(8))
print(movies.tail(8))
```

</details>

#### 6. Inspect the schema

The schema tells us what columns exist and what type of data pandas thinks each column contains.

File: `session7/solutions/exercise-07-01.py`

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")

print(movies.shape)
print(movies.columns)
print(movies.dtypes)
```

> [!NOTE]
>
> Questions:
>
> 1. How many rows and columns are in the dataset?
> 2. Which columns are numeric?
> 3. Which columns contain text?

Task: Print only the number of rows, then print only the number of columns.

<details>
<summary>Show solution</summary>

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")

rows = movies.shape[0]
columns = movies.shape[1]

print(rows)
print(columns)
```

</details>

#### 7. Describe numeric data

Use `describe()` to summarise numeric columns.

File: `session7/solutions/exercise-07-01.py`

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")

print(movies.describe())
```

> [!NOTE]
>
> What are the minimum, maximum, and mean values for `IMDB Rating`?
>
> <details>
> <summary>Hint</summary>
>
> Look for the `IMDB Rating` column in the `describe()` output.
>
> </details>

Task: Print the mean, minimum, and maximum `Production Budget`.

<details>
<summary>Show solution</summary>

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")

print(movies["Production Budget"].mean())
print(movies["Production Budget"].min())
print(movies["Production Budget"].max())
```

</details>

#### 8. Select columns

You can select one column:

File: `session7/solutions/exercise-07-01.py`

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")

print(movies["Title"])
```

You can also select several columns:

```python
print(movies[["Title", "Release Date", "IMDB Rating"]])
```

Task: Select and print only `Title`, `Major Genre`, and `Distributor`.

<details>
<summary>Show solution</summary>

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")

print(movies[["Title", "Major Genre", "Distributor"]])
```

</details>

#### 9. Filter rows

Use a condition to keep only some rows.

File: `session7/solutions/exercise-07-01.py`

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")

high_rated = movies[movies["IMDB Rating"] >= 8]

print(high_rated[["Title", "IMDB Rating"]])
```

> [!TIP]
>
> Filtering is one of the most important pandas skills. Read the condition carefully:
>
> ```python
> movies["IMDB Rating"] >= 8
> ```
>
> This creates a True/False result for every row.

Task: Filter and print movies with `Running Time min` greater than or equal to `150`.

<details>
<summary>Show solution</summary>

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")

long_movies = movies[movies["Running Time min"] >= 150]

print(long_movies[["Title", "Running Time min"]])
```

</details>

#### 10. Create a new column

Create a simple column that marks high-rated movies.

File: `session7/solutions/exercise-07-01.py`

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")

movies["High Rated"] = movies["IMDB Rating"] >= 8

print(movies[["Title", "IMDB Rating", "High Rated"]].head())
```

Task: Create a column called `Low Rated` that is `True` when `IMDB Rating` is less than `5`.

<details>
<summary>Show solution</summary>

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")

movies["Low Rated"] = movies["IMDB Rating"] < 5

print(movies[["Title", "IMDB Rating", "Low Rated"]].head())
```

</details>

#### 11. Count categories

Use `value_counts()` to count how often values appear in one column.

File: `session7/solutions/exercise-07-01.py`

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")

print(movies["Major Genre"].value_counts())
```

> [!NOTE]
>
> Which genre appears most often?

Task: Count how many movies there are for each `Distributor`, including missing values.

<details>
<summary>Show solution</summary>

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")

print(movies["Distributor"].value_counts(dropna=False))
```

</details>

#### 12. Sort rows

Use `sort_values()` to sort a DataFrame.

File: `session7/solutions/exercise-07-01.py`

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")

sorted_movies = movies.sort_values("IMDB Rating", ascending=False)

print(sorted_movies[["Title", "IMDB Rating"]].head(10))
```

Task: Sort movies by `Production Budget` from highest to lowest and print the first 10 rows.

<details>
<summary>Show solution</summary>

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")

sorted_budget = movies.sort_values("Production Budget", ascending=False)

print(sorted_budget[["Title", "Production Budget"]].head(10))
```

</details>

#### 13. Find the largest values

For a numeric column, `nlargest()` is a quick way to find top values.

File: `session7/solutions/exercise-07-01.py`

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")

big_budget = movies.nlargest(5, "Production Budget")

print(big_budget[["Title", "Production Budget"]])
```

Task: Use `nlargest()` to print the 5 movies with the highest `Worldwide Gross`.

<details>
<summary>Show solution</summary>

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")

top_worldwide = movies.nlargest(5, "Worldwide Gross")

print(top_worldwide[["Title", "Worldwide Gross"]])
```

</details>

#### 14. Combine conditions

Use `&` when both conditions must be true. Put each condition inside parentheses.

File: `session7/solutions/exercise-07-01.py`

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")

popular_action = movies[
    (movies["Major Genre"] == "Action")
    & (movies["IMDB Rating"] >= 7)
]

print(popular_action[["Title", "Major Genre", "IMDB Rating"]])
```

Task: Filter and print Comedy movies with `IMDB Rating` greater than or equal to `7`.

<details>
<summary>Show solution</summary>

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")

good_comedies = movies[
    (movies["Major Genre"] == "Comedy")
    & (movies["IMDB Rating"] >= 7)
]

print(good_comedies[["Title", "Major Genre", "IMDB Rating"]])
```

</details>

#### 15. Create a calculated column

Create a basic profit column using worldwide gross minus production budget.

File: `session7/solutions/exercise-07-01.py`

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")

movies["Profit Estimate"] = movies["Worldwide Gross"] - movies["Production Budget"]

print(movies[["Title", "Worldwide Gross", "Production Budget", "Profit Estimate"]].head())
```

> [!IMPORTANT]
>
> This is only an estimate. Real movie profit is more complicated than this.

Task: Create a column called `Budget in Millions` and print it with the movie title.

<details>
<summary>Show solution</summary>

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")

movies["Budget in Millions"] = movies["Production Budget"] / 1_000_000

print(movies[["Title", "Production Budget", "Budget in Millions"]].head())
```

</details>

#### 16. Exercise

Add your answers to:

```txt
session7/solutions/exercise-07-01.py
```

Tasks:

1. Load `datasets/Movies.json` into a DataFrame called `movies`.
2. Print the first 5 rows, the last 3 rows, and the number of rows and columns.
3. Print the data type of each column and summary statistics for numeric columns.
4. Print only the `Title`, `Release Date`, and `IMDB Rating` columns.
5. Filter and print movies with `IMDB Rating` greater than or equal to `8`.
6. Create a new column called `Long Movie` that is `True` when `Running Time min` is greater than or equal to `120`.
7. Count the number of movies per `Major Genre`.
8. Sort by `IMDB Rating`, print the top 10 rows, and add a short comment explaining why inspecting the schema is useful before cleaning data.

#### 17. Quiz

Complete the following quiz.

```bash
quizmd quizzes/python-session-07-part-01-quiz.md
```

If you want to choose a theme:

```bash
quizmd --theme light quizzes/python-session-07-part-01-quiz.md
quizmd --theme dark quizzes/python-session-07-part-01-quiz.md
```

You are now ready to move to the next tutorial.
