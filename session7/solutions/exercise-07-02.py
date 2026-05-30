'''
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
'''

#### 4. Load and inspect the dataset
# ==========+==========+==========+==========+==========+
import pandas as pd

movies = pd.read_json("datasets/Movies.json")

print("\n\n#### 4. Load and inspect the dataset\n")
print("\n", movies.head())
print("\n", movies.dtypes)
print("\n", movies.shape)

# Task: Print the first 10 rows and the last 3 rows.
print("\n# Task: Print the first 10 rows and the last 3 rows.\n")
print("\nThe first 10 rows:\n", movies.head(10))
print("\nThe last 3 rows:\n", movies.head(3))

#### 5. Find missing values
# ==========+==========+==========+==========+==========+
# Use `isnull().sum()` to count missing values in each column.
print("\n\n#### 5. Find missing values\n")
print(movies.isnull().sum())

# 1. Which columns have many missing values?
print("\n1. Which columns have many missing values?\n")
print("\n", movies.isnull().sum() > 100)

# 2. Which columns have no missing values?
print("\n2. Which columns have no missing values?\n")
# print("\n", movies.isnull().sum() == 0)
# Create the mask (axis=1 looks across columns for each row)
no_missing_mask = movies.isnull().sum(axis=1) == 0
# Filter the DataFrame using the mask
complete_movies = movies[no_missing_mask]
print(complete_movies["Title"])

# 3. Which missing values might matter for analysis?
print("\n3. Which missing values might matter for analysis?\n")
# Select only numeric columns and count their missing values
movies_analysis = movies.select_dtypes(exclude=['object']).isnull().sum()
print("\n", movies_analysis)

# Task: Print missing values for only `Distributor`, `Major Genre`, and `IMDB Rating`.
print("\nTask: Print missing values for only `Distributor`, `Major Genre`, and `IMDB Rating`.\n")
print(movies[["Distributor","Major Genre","IMDB Rating"]].isnull().sum())

#### 6. Count all missing cells
# ==========+==========+==========+==========+==========+
# Count how many missing cells exist in the whole DataFrame.
missing_cells = movies.isnull().sum().sum()
print(f"\nCount how many missing cells exist in the whole DataFrame: {missing_cells}")
# > The first `sum()` counts missing values per column.
# > The second `sum()` adds the column totals together.

# Task: Calculate the percentage of missing cells in the whole DataFrame.
print("\nTask: Calculate the percentage of missing cells in the whole DataFrame")
total_cells = movies.shape[0] * movies.shape[1]
missing_percent = (missing_cells / total_cells) * 100
print(missing_percent, "%")
# Format to 0 decimal places using an f-string
print(f"{missing_percent:.0f}%")

#### 7. Filter rows with missing values
# ==========+==========+==========+==========+==========+
# Find rows where the `Distributor` column is missing.
print("\nFind rows where the `Distributor` column is missing.")
missing_distributor_rows = movies[movies["Distributor"].isnull()]
# print("\n", missing_distributor_rows)
print("\n", missing_distributor_rows[["Title","Distributor"]])

# Task: Find rows where `IMDB Rating` is missing.
print("\nTask: Find rows where `IMDB Rating` is missing.")
missing_imdb_rows = movies[movies["IMDB Rating"].isnull()]
print("\n", missing_imdb_rows[["Title","IMDB Rating"]])

#### 8. Fill missing text values
# ==========+==========+==========+==========+==========+
print("\n8. Fill missing text values")
movies["Distributor"] = movies["Distributor"].fillna("missing")
print("\n", movies[["Title","Distributor"]].tail())
print("\n", movies[movies["Distributor"] == "missing"][["Title","Distributor"]])

# Task: Fill missing `Major Genre` values with `missing` in a copy of the DataFrame.
print("\nTask: Fill missing `Major Genre` values with `missing` in a copy of the DataFrame.")
movies = pd.read_json("datasets/Movies.json")
movies_copy = movies.copy()
movies_copy["Major Genre"]= movies_copy["Major Genre"].fillna("missing")
print("\n", movies_copy.head())
print("\n",movies_copy[movies_copy["Major Genre"]=="missing"][["Title","Major Genre"]].head())

#### 9. Use `loc` to inspect or update a row
# ==========+==========+==========+==========+==========+
print("\n9. Use `loc` to inspect or update a row")
print("\nInspect: ")
print("\nmovies.loc[1]: \n",movies.loc[1])
print("\nUpdate:")
movies.loc[75,"Distributor"] = "___manual review___"
print("\n",movies.loc[75,["Title","Distributor"]])

# Task: Use `loc` to print only the `Title`, `Major Genre`, and `IMDB Rating` values for row `100`.
print("\nTask: Use `loc` to print only the `Title`, `Major Genre`, and `IMDB Rating` values for row `100`.")
print("\n", movies.loc[100, ["Title","Major Genre","IMDB Rating"]])


#### 10. Group values
# ==========+==========+==========+==========+==========+
# Use `value_counts()` to count movies per genre.
print("\n10. Group values.\nUse `value_counts()` to count movies per genre.")
print("\n", movies["Major Genre"].value_counts())
print("\n", movies["Major Genre"].value_counts(dropna=False))

#You can also use `groupby()`:
genre_counts = movies.groupby("Major Genre")["Title"].count()
print("\nmovies.groupby('Major Genre')['Title'].count()")
print("\n", genre_counts)

#Task: Group by `Distributor` and print the average `IMDB Rating` for each distributor.
print("\nTask: Group by `Distributor` and print the average `IMDB Rating` for each distributor.")
avg_imdb_rating_by_dist = movies.groupby("Distributor")["IMDB Rating"].mean()
print(avg_imdb_rating_by_dist)
# print(f"{avg_imdb_rating_by_dist:.0f}") # throws error


#### 11. Fill missing numeric values with a mean
# ==========+==========+==========+==========+==========+
# Use the mean of `IMDB Rating` to fill missing ratings in a test copy.
print("\n11. Fill missing numeric values with a mean")
movies_copy = movies.copy()
imdb_rating_avg = movies_copy["IMDB Rating"].mean()
movies_copy["IMDB Rating"] = movies_copy["IMDB Rating"].fillna(imdb_rating_avg)
print(imdb_rating_avg)
print("\n", movies_copy["IMDB Rating"].isnull().sum())

# Task: Fill missing `Rotten Tomatoes Rating` values with the median in a copy.
movies_copy = movies.copy()
rotten_tomotoes_rating_median = movies_copy["Rotten Tomatoes Rating"].median()
movies_copy["Rotten Tomatoes Rating"] = movies_copy["Rotten Tomatoes Rating"].fillna(rotten_tomotoes_rating_median)
print("\n# Task: Fill missing `Rotten Tomatoes Rating` values with the median in a copy.")
print("\nrotten_tomotoes_rating_median: ",rotten_tomotoes_rating_median)
# check if any null values remain
print("\n", movies_copy["Rotten Tomatoes Rating"].isnull().sum())


#### 12. Interpolate missing numeric values
# Interpolation fills missing numeric values by estimating between nearby known values.
# ==========+==========+==========+==========+==========+
scores = pd.DataFrame({
    "week": [1, 2, 3, 4, 5],
    "score": [50, None, 70, None, 90],
})

scores["score_interpolated"] = scores["score"].interpolate()

print("\n12. Interpolate missing numeric values")
print("\n", scores )

# Task: Add a new missing value example and interpolate it.
print("\nTask: Add a new missing value example and interpolate it.")
temperature = pd.DataFrame({
    "hour": [1, 2, 3, 4, 5],
    "temperature": [10, None, None, 16, 18],
})

temperature["temperature_interpolated"] = temperature["temperature"].interpolate()
print("\n", temperature)

#### 13. Interpolate a movie column in a copy
# ==========+==========+==========+==========+==========+
print("\n13. Interpolate a movie column in a copy")
test_movies = movies.copy()
test_movies["Running Time min"] = test_movies["Running Time min"].interpolate()
print("\ntest_movies['Running Time min'].isnull().sum(): ", test_movies["Running Time min"].isnull().sum())
print("\n", test_movies[["Title","Running Time min"]].head(10))
print("\n", test_movies[["Title","Running Time min"]].tail(10))

# Task: Compare missing `Running Time min` values before and after interpolation.
print("\nTask: Compare missing `Running Time min` values before and after interpolation.")
test_movies = movies.copy()

before = test_movies["Running Time min"].isnull().sum()
test_movies["Running Time min"] = test_movies["Running Time min"].interpolate()
after = test_movies["Running Time min"].isnull().sum()

print("\nNull values Before interpolation: \n", before)
print("\nNull values After interpolation: \n", after)


#### 14. Clean column names
# Column names with spaces and capital letters are harder to type. Create a cleaned copy with simpler column names.
# ==========+==========+==========+==========+==========+
print("\n14. Clean column names")
clean_movies = movies.copy()

clean_movies.columns = (
    clean_movies.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_", regex=False)
    .str.replace(".","", regex=False)
)
print("\nClean movies columns: \n", clean_movies.columns )

# Task: After cleaning column names, print the first five values from the new `major_genre` column.
print("\nTask: After cleaning column names, print the first five values from the new `major_genre` column.")
print("\n", clean_movies.head(5))
print("\n", clean_movies["major_genre"].head(5))

#### 15. Remove duplicate rows
# Duplicates can make counts and averages incorrect.
# ==========+==========+==========+==========+==========+
print("\n15. Remove duplicate rows")
movies = pd.read_json("datasets/Movies.json")
print(movies.duplicated().sum())
clean_movies = movies.drop_duplicates()
print(clean_movies.shape)

# Task: Print the duplicate rows themselves.
print("\n# Task: Print the duplicate rows themselves.")
movies = pd.read_json("datasets/Movies.json")
duplicates = movies[movies.duplicated()]
print(duplicates)

#### 16. Clean text values
# Text columns may contain extra spaces or inconsistent capitalisation.
# ==========+==========+==========+==========+==========+
print("\n16. Clean text values")
movies = pd.read_json("datasets/Movies.json")
clean_movies["Distributor"] = clean_movies["Distributor"].str.strip()
clean_movies["Major Genre"] = clean_movies["Major Genre"].str.strip()
print("\nClean text values: ", clean_movies[["Distributor","Major Genre"]].head())

# Task: Strip spaces and convert `Major Genre` to lowercase in a copy.
print("\nTask: Strip spaces and convert `Major Genre` to lowercase in a copy.")
movies = pd.read_json("datasets/Movies.json")
movies_copy = movies.copy()
movies_copy["Major Genre"] = movies_copy["Major Genre"].str.strip()
movies_copy["Major Genre"] = movies_copy["Major Genre"].str.lower()
## clean_movies["Major Genre"] = clean_movies["Major Genre"].str.strip().str.lower()
print("\n", movies_copy[["Title","Major Genre"]].head(15))


#### 17. Drop rows when a column is essential
# Sometimes it is better to remove rows where an important value is missing.
# ==========+==========+==========+==========+==========+
print("\n17. Drop rows when a column is essential")
movies = pd.read_json("datasets/Movies.json")
movies_with_rating = movies.dropna(subset=["IMDB Rating"])
print("\nmovies shap: ",movies.shape)
print("\nmovies_with_rating shape: ", movies_with_rating.shape)

# Task: Drop rows where `Title` is missing and print the before/after shapes.
print("\nTask: Drop rows where `Title` is missing and print the before/after shapes.")
movies = pd.read_json("datasets/Movies.json")
movies_with_title = movies.dropna(subset=["Title"])
print("\n movies all - shape: ", movies.shape)
print("\n movies with titles - shape: ", movies_with_title.shape)


#### 18. Exercise
# ==========+==========+==========+==========+==========+
print("\n18. Exercise")
print("\n")


# Tasks:
# ==========+==========+==========+==========+==========+
'''
# 1. Load `datasets/Movies.json`.
# 2. Print missing values per column.
# 3. Count the total number of missing cells in the DataFrame.
# 4. Print rows where `Major Genre` is missing.
# 5. Create a copy of the DataFrame called `clean_movies`.
# 6. Fill missing `Major Genre` and `Distributor` values with `missing`.
# 7. Fill missing `IMDB Rating` values with the mean rating in a copy.
# 8. Create a small `scores` DataFrame, use interpolation to fill missing scores, and add comments explaining one risk of mean filling and when interpolation is useful.
'''
# ==========+==========+==========+==========+==========+

# 1. Load `datasets/Movies.json`.
import pandas as pd

movies = pd.read_json("datasets/Movies.json")


# 2. Print missing values per column.
print("\n# 2. Print missing values per column.")
print(movies.isnull().sum())

# 3. Count the total number of missing cells in the DataFrame.
print("\n# 3. Count the total number of missing cells in the DataFrame.")
print(movies.shape)
print(movies.isnull().sum().sum())


# 4. Print rows where `Major Genre` is missing.
print("\n# 4. Print rows where `Major Genre` is missing.")
print(movies[movies["Major Genre"].isnull()][["Title","Major Genre"]])


# 5. Create a copy of the DataFrame called `clean_movies`.
print("\n# 5. Create a copy of the DataFrame called `clean_movies`.")
clean_movies = movies.copy()
print("\n", clean_movies.head(3))


# 6. Fill missing `Major Genre` and `Distributor` values with `missing`.
print("\n# 6. Fill missing `Major Genre` and `Distributor` values with `missing`.")
clean_movies[["Major Genre", "Distributor"]] = clean_movies[["Major Genre", "Distributor"]].fillna("missing")
print("\n",clean_movies[clean_movies["Major Genre"]=="missing"][["Title","Major Genre"]])
print("\n",clean_movies[clean_movies["Distributor"]=="missing"][["Title","Distributor"]])
print("\n",clean_movies[clean_movies["Distributor"]=="missing"][["Title","Major Genre","Distributor"]])


# 7. Fill missing `IMDB Rating` values with the mean rating in a copy.
print("\n# 7. Fill missing `IMDB Rating` values with the mean rating in a copy.")
movies_ratings_mean = movies_copy["IMDB Rating"].mean()
movies_copy["IMDB Rating"] = movies_copy["IMDB Rating"].fillna(movies_ratings_mean)
print("\n", movies_copy["IMDB Rating"].mean())
print("\n",movies_copy["IMDB Rating"].isnull().sum())
print("\n",movies_copy.head())
print("\n", movies_copy[movies_copy["IMDB Rating"] == movies_copy["IMDB Rating"].mean()])


# 8. Create a small `scores` DataFrame, use interpolation to fill missing scores, and add comments explaining one risk of mean filling and when interpolation is useful.
print("\n# 8. Create a small `scores` DataFrame, use interpolation to fill missing scores, and add comments explaining one risk of mean filling and when interpolation is useful.")
scores = pd.DataFrame({
    "week": [1, 2, 3, 4, 5],
    "score": [60, None, 80, None, 100],
})
scores_end_none = pd.DataFrame({
    "week": [1, 2, 3, 4, 5],
    "score": [60, None, 80, 90, None],
})
scores_start_none = pd.DataFrame({
    "week": [1, 2, 3, 4, 5],
    "score": [None, 70, 80, 90, 100],
})

scores["score_interpolated"] = scores["score"].interpolate()
scores["score_interpolated_end"] = scores_end_none["score"].interpolate()
scores["score_interpolated_start"] = scores_start_none["score"].interpolate()
print("\n", scores)
