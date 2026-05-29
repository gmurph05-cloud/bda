### Session 7 | Part 2

> Data cleaning is not just replacing missing values. It is deciding what the data means, what is safe to change, and what should be left for review.

#### 1. Goal

In this tutorial, you will:

- identify missing values
- count missing cells
- filter rows with missing values
- fill missing values
- interpolate missing numeric values
- clean text columns
- group data using pandas
- remove duplicates and standardise column names

This part reuses the data-cleaning flow from the earlier analytic tools material and adapts it to the `Movies.json` dataset.

#### 2. Prerequisites

Before starting:

1. Open the `session7` folder in Visual Studio Code.
2. Activate your virtual environment.
3. Confirm dependencies are installed:

```bash
pip install -r requirements.txt
```

4. Create your exercise file:

```txt
session7/solutions/exercise-07-02.py
```

#### 3. Basics you should know

- `isnull()`: checks whether each value is missing.
- `isna()`: same idea as `isnull()`.
- `sum()`: counts `True` values when used after `isnull()`.
- `fillna(...)`: fills missing values.
- `dropna(...)`: removes rows or columns with missing values.
- `interpolate(...)`: estimates missing numeric values between known values.
- `loc[...]`: selects rows and columns by labels.
- `groupby(...)`: groups rows by a column.
- `value_counts()`: counts values in one column.
- `duplicated()`: checks duplicate rows.
- `str.strip()`: removes spaces at the start and end of text.

#### 4. Load and inspect the dataset

File: `session7/solutions/exercise-07-02.py`

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")

print(movies.head())
print(movies.dtypes)
print(movies.shape)
```

Task: Print the first 10 rows and the last 3 rows.

<details>
<summary>Show solution</summary>

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")

print(movies.head(10))
print(movies.tail(3))
```

</details>

#### 5. Find missing values

Use `isnull().sum()` to count missing values in each column.

File: `session7/solutions/exercise-07-02.py`

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")

print(movies.isnull().sum())
```

> [!NOTE]
>
> Questions:
>
> 1. Which columns have many missing values?
> 2. Which columns have no missing values?
> 3. Which missing values might matter for analysis?

Task: Print missing values for only `Distributor`, `Major Genre`, and `IMDB Rating`.

<details>
<summary>Show solution</summary>

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")

print(movies[["Distributor", "Major Genre", "IMDB Rating"]].isnull().sum())
```

</details>

#### 6. Count all missing cells

Count how many missing cells exist in the whole DataFrame.

File: `session7/solutions/exercise-07-02.py`

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")

missing_cells = movies.isnull().sum().sum()

print(missing_cells)
```

> [!TIP]
>
> The first `sum()` counts missing values per column.
>
> The second `sum()` adds the column totals together.

Task: Calculate the percentage of missing cells in the whole DataFrame.

<details>
<summary>Show solution</summary>

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")

missing_cells = movies.isnull().sum().sum()
total_cells = movies.shape[0] * movies.shape[1]
missing_percentage = (missing_cells / total_cells) * 100

print(missing_percentage)
```

</details>

#### 7. Filter rows with missing values

Find rows where the `Distributor` column is missing.

File: `session7/solutions/exercise-07-02.py`

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")

missing_distributor = movies[movies["Distributor"].isnull()]

print(missing_distributor[["Title", "Distributor"]])
```

Task: Find rows where `IMDB Rating` is missing.

<details>
<summary>Show solution</summary>

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")

missing_rating = movies[movies["IMDB Rating"].isnull()]

print(missing_rating[["Title", "IMDB Rating"]])
```

</details>

#### 8. Fill missing text values

For a text column, we can sometimes replace missing values with a clear label such as `missing`.

File: `session7/solutions/exercise-07-02.py`

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")

movies["Distributor"] = movies["Distributor"].fillna("missing")

print(movies[["Title", "Distributor"]].tail())
```

> [!IMPORTANT]
>
> Filling missing values is a decision. Do not fill values automatically without thinking about whether the replacement is honest and useful.

Task: Fill missing `Major Genre` values with `missing` in a copy of the DataFrame.

<details>
<summary>Show solution</summary>

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")
clean_movies = movies.copy()

clean_movies["Major Genre"] = clean_movies["Major Genre"].fillna("missing")

print(clean_movies[["Title", "Major Genre"]].head())
```

</details>

#### 9. Use `loc` to inspect or update a row

You can use `loc` to inspect a row by index.

File: `session7/solutions/exercise-07-02.py`

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")

print(movies.loc[75])
```

You can also update a specific cell:

```python
movies.loc[75, "Distributor"] = "manual review"
print(movies.loc[75, ["Title", "Distributor"]])
```

Task: Use `loc` to print only the `Title`, `Major Genre`, and `IMDB Rating` values for row `100`.

<details>
<summary>Show solution</summary>

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")

print(movies.loc[100, ["Title", "Major Genre", "IMDB Rating"]])
```

</details>

#### 10. Group values

Use `value_counts()` to count movies per genre.

File: `session7/solutions/exercise-07-02.py`

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")

print(movies["Major Genre"].value_counts(dropna=False))
```

You can also use `groupby()`:

```python
genre_counts = movies.groupby("Major Genre")["Title"].count()
print(genre_counts)
```

Task: Group by `Distributor` and print the average `IMDB Rating` for each distributor.

<details>
<summary>Show solution</summary>

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")

average_rating_by_distributor = movies.groupby("Distributor")["IMDB Rating"].mean()

print(average_rating_by_distributor)
```

</details>

#### 11. Fill missing numeric values with a mean

Use the mean of `IMDB Rating` to fill missing ratings in a test copy.

File: `session7/solutions/exercise-07-02.py`

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")

test_movies = movies.copy()
mean_rating = test_movies["IMDB Rating"].mean()
test_movies["IMDB Rating"] = test_movies["IMDB Rating"].fillna(mean_rating)

print(mean_rating)
print(test_movies["IMDB Rating"].isnull().sum())
```

> [!NOTE]
>
> Why use `test_movies = movies.copy()`?
>
> <details>
> <summary>Show answer</summary>
>
> It lets you try a cleaning decision without changing the original DataFrame.
>
> </details>

Task: Fill missing `Rotten Tomatoes Rating` values with the median in a copy.

<details>
<summary>Show solution</summary>

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")
test_movies = movies.copy()

median_rotten = test_movies["Rotten Tomatoes Rating"].median()
test_movies["Rotten Tomatoes Rating"] = test_movies["Rotten Tomatoes Rating"].fillna(median_rotten)

print(test_movies["Rotten Tomatoes Rating"].isnull().sum())
```

</details>

#### 12. Interpolate missing numeric values

Interpolation fills missing numeric values by estimating between nearby known values.

File: `session7/solutions/exercise-07-02.py`

```python
import pandas as pd

scores = pd.DataFrame({
    "week": [1, 2, 3, 4, 5],
    "score": [50, None, 70, None, 90],
})

scores["score_interpolated"] = scores["score"].interpolate()

print(scores)
```

Expected idea:

```txt
The missing score between 50 and 70 becomes 60.
The missing score between 70 and 90 becomes 80.
```

> [!IMPORTANT]
>
> Interpolation is useful when the order of rows matters, for example dates, weeks, or measurements over time. It is not always appropriate for categories.

Task: Add a new missing value example and interpolate it.

<details>
<summary>Show solution</summary>

```python
import pandas as pd

temperature = pd.DataFrame({
    "hour": [1, 2, 3, 4, 5],
    "temperature": [10, None, None, 16, 18],
})

temperature["temperature_interpolated"] = temperature["temperature"].interpolate()

print(temperature)
```

</details>

#### 13. Interpolate a movie column in a copy

Try interpolation on `Running Time min` in a copy of the movie data.

File: `session7/solutions/exercise-07-02.py`

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")

test_movies = movies.copy()
test_movies["Running Time min"] = test_movies["Running Time min"].interpolate()

print(test_movies["Running Time min"].isnull().sum())
print(test_movies[["Title", "Running Time min"]].head(10))
```

> [!NOTE]
>
> This is for practice. In real analysis, always ask whether interpolation makes sense for the column.

Task: Compare missing `Running Time min` values before and after interpolation.

<details>
<summary>Show solution</summary>

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")

test_movies = movies.copy()

before = test_movies["Running Time min"].isnull().sum()
test_movies["Running Time min"] = test_movies["Running Time min"].interpolate()
after = test_movies["Running Time min"].isnull().sum()

print(before)
print(after)
```

</details>

#### 14. Clean column names

Column names with spaces and capital letters are harder to type. Create a cleaned copy with simpler column names.

File: `session7/solutions/exercise-07-02.py`

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")
clean_movies = movies.copy()

clean_movies.columns = (
    clean_movies.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_", regex=False)
    .str.replace(".", "", regex=False)
)

print(clean_movies.columns)
```

Task: After cleaning column names, print the first five values from the new `major_genre` column.

<details>
<summary>Show solution</summary>

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")
clean_movies = movies.copy()

clean_movies.columns = (
    clean_movies.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_", regex=False)
    .str.replace(".", "", regex=False)
)

print(clean_movies["major_genre"].head())
```

</details>

#### 15. Remove duplicate rows

Duplicates can make counts and averages incorrect.

File: `session7/solutions/exercise-07-02.py`

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")

print(movies.duplicated().sum())

clean_movies = movies.drop_duplicates()

print(clean_movies.shape)
```

Task: Print the duplicate rows themselves.

<details>
<summary>Show solution</summary>

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")

duplicates = movies[movies.duplicated()]

print(duplicates)
```

</details>

#### 16. Clean text values

Text columns may contain extra spaces or inconsistent capitalisation.

File: `session7/solutions/exercise-07-02.py`

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")
clean_movies = movies.copy()

clean_movies["Distributor"] = clean_movies["Distributor"].str.strip()
clean_movies["Major Genre"] = clean_movies["Major Genre"].str.strip()

print(clean_movies[["Distributor", "Major Genre"]].head())
```

Task: Strip spaces and convert `Major Genre` to lowercase in a copy.

<details>
<summary>Show solution</summary>

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")
clean_movies = movies.copy()

clean_movies["Major Genre"] = clean_movies["Major Genre"].str.strip().str.lower()

print(clean_movies["Major Genre"].head())
```

</details>

#### 17. Drop rows when a column is essential

Sometimes it is better to remove rows where an important value is missing.

File: `session7/solutions/exercise-07-02.py`

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")

movies_with_rating = movies.dropna(subset=["IMDB Rating"])

print(movies.shape)
print(movies_with_rating.shape)
```

Task: Drop rows where `Title` is missing and print the before/after shapes.

<details>
<summary>Show solution</summary>

```python
import pandas as pd

movies = pd.read_json("datasets/Movies.json")

movies_with_title = movies.dropna(subset=["Title"])

print(movies.shape)
print(movies_with_title.shape)
```

</details>

#### 18. Exercise

Add your answers to:

```txt
session7/solutions/exercise-07-02.py
```

Tasks:

1. Load `datasets/Movies.json`.
2. Print missing values per column.
3. Count the total number of missing cells in the DataFrame.
4. Print rows where `Major Genre` is missing.
5. Create a copy of the DataFrame called `clean_movies`.
6. Fill missing `Major Genre` and `Distributor` values with `missing`.
7. Fill missing `IMDB Rating` values with the mean rating in a copy.
8. Create a small `scores` DataFrame, use interpolation to fill missing scores, and add comments explaining one risk of mean filling and when interpolation is useful.

#### 19. Quiz

Complete the following quiz.

```bash
quizmd quizzes/python-session-07-part-02-quiz.md
```

If you want to choose a theme:

```bash
quizmd --theme light quizzes/python-session-07-part-02-quiz.md
quizmd --theme dark quizzes/python-session-07-part-02-quiz.md
```

You are now ready to move to the next tutorial.
