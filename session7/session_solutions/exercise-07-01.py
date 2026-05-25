# Session 7 Part 1 - Exercise solution

import pandas as pd


movies = pd.read_json("datasets/Movies.json")

print("First 5 rows:")
print(movies.head())

print("\nLast 3 rows:")
print(movies.tail(3))

print("\nRows and columns:")
print(movies.shape)

print("\nColumn data types:")
print(movies.dtypes)

print("\nSummary statistics:")
print(movies.describe())

print("\nSelected columns:")
print(movies[["Title", "Release Date", "IMDB Rating"]])

print("\nMovies with IMDB Rating >= 8:")
high_rated = movies[movies["IMDB Rating"] >= 8]
print(high_rated[["Title", "IMDB Rating"]])

movies["Long Movie"] = movies["Running Time min"] >= 120

print("\nLong movie flag:")
print(movies[["Title", "Running Time min", "Long Movie"]].head())

print("\nMovies per Major Genre:")
print(movies["Major Genre"].value_counts(dropna=False))

print("\nTop 10 movies by IMDB Rating:")
top_rated = movies.sort_values("IMDB Rating", ascending=False)
print(top_rated[["Title", "IMDB Rating"]].head(10))

print("\nLargest production budgets:")
big_budget = movies.nlargest(5, "Production Budget")
print(big_budget[["Title", "Production Budget"]])

print("\nAction movies with IMDB Rating >= 7:")
popular_action = movies[
    (movies["Major Genre"] == "Action")
    & (movies["IMDB Rating"] >= 7)
]
print(popular_action[["Title", "Major Genre", "IMDB Rating"]])

movies["Profit Estimate"] = movies["Worldwide Gross"] - movies["Production Budget"]

print("\nProfit estimate:")
print(movies[["Title", "Worldwide Gross", "Production Budget", "Profit Estimate"]].head())

print("\nRandom sample:")
print(movies.sample(5, random_state=7))

print("\nUnique distributors:")
print(movies["Distributor"].nunique())

print("\nAverage running time:")
print(movies["Running Time min"].mean())

print("\nShortest 5 movies:")
print(movies.nsmallest(5, "Running Time min")[["Title", "Running Time min"]])

movies["Rating Rounded"] = movies["IMDB Rating"].round()

print("\nRounded ratings:")
print(movies[["Title", "IMDB Rating", "Rating Rounded"]].head())

# Inspecting the schema is useful because it shows column names, data types,
# and possible columns that need cleaning before analysis.
