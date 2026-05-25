# Session 7 Part 2 - Exercise solution

import pandas as pd


movies = pd.read_json("datasets/Movies.json")

print("Missing values per column:")
print(movies.isnull().sum())

print("\nTotal missing cells:")
print(movies.isnull().sum().sum())

print("\nRows where Major Genre is missing:")
print(movies[movies["Major Genre"].isnull()][["Title", "Major Genre"]])

clean_movies = movies.copy()

clean_movies["Major Genre"] = clean_movies["Major Genre"].fillna("missing")
clean_movies["Distributor"] = clean_movies["Distributor"].fillna("missing")

mean_rating = clean_movies["IMDB Rating"].mean()
clean_movies["IMDB Rating"] = clean_movies["IMDB Rating"].fillna(mean_rating)

print("\nSmall interpolation example:")
scores = pd.DataFrame({
    "week": [1, 2, 3, 4, 5],
    "score": [50, None, 70, None, 90],
})
scores["score_interpolated"] = scores["score"].interpolate()
print(scores)

runtime_test = movies.copy()
runtime_test["Running Time min"] = runtime_test["Running Time min"].interpolate()

print("\nMissing running times after interpolation:")
print(runtime_test["Running Time min"].isnull().sum())

clean_movies.columns = (
    clean_movies.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_", regex=False)
    .str.replace(".", "", regex=False)
)

print("\nCleaned column names:")
print(clean_movies.columns)

print("\nDuplicate rows:")
print(movies.duplicated().sum())

deduplicated_movies = movies.drop_duplicates()
print("\nRows after dropping duplicates:")
print(deduplicated_movies.shape)

text_clean_movies = movies.copy()
text_clean_movies["Distributor"] = text_clean_movies["Distributor"].str.strip()
text_clean_movies["Major Genre"] = text_clean_movies["Major Genre"].str.strip()

print("\nText-cleaned sample:")
print(text_clean_movies[["Distributor", "Major Genre"]].head())

movies_with_rating = movies.dropna(subset=["IMDB Rating"])

print("\nRows before and after dropping missing IMDB Rating:")
print(movies.shape)
print(movies_with_rating.shape)

median_rotten = movies["Rotten Tomatoes Rating"].median()
rotten_test = movies.copy()
rotten_test["Rotten Tomatoes Rating"] = rotten_test["Rotten Tomatoes Rating"].fillna(median_rotten)

print("\nMissing Rotten Tomatoes Rating after median fill:")
print(rotten_test["Rotten Tomatoes Rating"].isnull().sum())

print("\nMissing values after selected cleaning:")
print(clean_movies.isnull().sum())

print("\nMovies per Major Genre:")
print(movies["Major Genre"].value_counts(dropna=False))

# One risk of filling missing numeric values with the mean is that it can hide
# missing data and make the column look less variable than it really is.
#
# Interpolation is useful when numeric values have a meaningful order, such as
# weekly measurements or time-series observations.
