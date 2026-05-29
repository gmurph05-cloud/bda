import pandas as pd

movies = pd.read_json("datasets/Movies.json")

print(movies)

# 5. Inspect the first and last rows
# print(movies.head(8))
# print(movies.tail(8))

#  6. Inspect the schema
# print(movies.shape)
# print(movies.columns)
# print(movies.dtypes)

# Task: Print only the number of rows, then print only the number of columns.
# print(f"Number of rows : {movies.shape[0]}")
# print(f"Number of columns : {movies.shape[1]}")

# 7. Describe numeric data
# print(movies.describe())
# What are the minimum, maximum, and mean values for IMDB Rating?
# print(f"\nIMDB Rating - Minimum values: {movies['IMDB Rating'].min()}")
# print(f"\nIMDB Rating - Maximum values: {movies['IMDB Rating'].max()}")
# print(f"\nIMDB Rating - Mean values: {movies['IMDB Rating'].mean()}")

# 8. Select columns
# print(f"Title: {movies["Title"]}")
# # You can also select several columns:
# print("\nSelect 'Title', 'Release Date', 'IMDB Rating':\n")
# print(movies[['Title', 'Release Date', 'IMDB Rating']])

# 9. Filter rows
# high_rated = movies[movies["IMDB Rating"] >= 8]
# print("\nHigh Rated movies >= 8:\n")
# print(high_rated[["Title", "IMDB Rating"]])

# Task: Create a column called Low Rated that is True when IMDB Rating is less than 5.
# movies["Low Rated"] = movies["IMDB Rating"] < 5
# print(movies[["Title", "IMDB Rating", "Low Rated"]].head())

# 11. Count categories
# Use value_counts() to count how often values appear in one column.
# print(f"Major Genre: {movies['Major Genre'].value_counts()}")
# print(movies['Major Genre'].value_counts())

#Which genre appears most often?
# print("\n", movies['Major Genre'].value_counts().head(1))

# Task: Count how many movies there are for each Distributor, including missing values.
# print(movies.info())
# WRONG - print(movies.groupby('Distributor').value_counts())
# print(movies["Distributor"].value_counts(dropna=False))

# 12. Sort rows
# sorted_movies = movies.sort_values("IMDB Rating", ascending=False)
# print(sorted_movies[["Title", "IMDB Rating"]].head(10))

# Task: Sort movies by Production Budget from highest to lowest and print the first 10 rows.
# sorted_movies = movies.sort_values("Production Budget", ascending=False)
# print(sorted_movies[["Title", "Production Budget"]].head(10))

# Format with commas and no decimal places
# formatted_output = sorted_movies[["Title", "Production Budget"]].head(10).style.format({
#     "Production Budget": "${:,.0f}"
# })

# Add .to_string() right here:
# print(formatted_output.to_string())

# 13. Find the largest values
# For a numeric column, nlargest() is a quick way to find top values.
# big_budget = movies.nlargest(5, "Production Budget")
# print(big_budget[["Title", "Production Budget"]])

# Task: Use nlargest() to print the 5 movies with the highest Worldwide Gross.
# print("Highest Worldwide Gross: \n")
# highest_worldwide_gross = movies.nlargest(5, "Worldwide Gross")
# print(highest_worldwide_gross[["Title", "Worldwide Gross"]])
# print("\n")
# formatted_output = highest_worldwide_gross[["Title", "Worldwide Gross"]].head(10).style.format({
#     "Worldwide Gross": "${:,.0f}"
# })
# print(formatted_output.to_string())

# 16. Exercise
'''
Tasks:

# 1. Load datasets/Movies.json into a DataFrame called movies.
# 2. Print the first 5 rows, the last 3 rows, and the number of rows and columns.
# 3. Print the data type of each column and summary statistics for numeric columns.
# 4. Print only the Title, Release Date, and IMDB Rating columns.
# 5. Filter and print movies with IMDB Rating greater than or equal to 8.
# 6. Create a new column called Long Movie that is True when Running Time min is greater than or equal to 120.
# 7. Count the number of movies per Major Genre.
# 8. Sort by IMDB Rating, print the top 10 rows, and add a short comment explaining why inspecting the schema is useful before cleaning data.
'''

# 1. Load datasets/Movies.json into a DataFrame called movies.
print("\n1. Load datasets/Movies.json into a DataFrame called movies.\n")
movies_exercise = pd.read_json("datasets\Movies.json")

# 2. Print the first 5 rows, the last 3 rows, and the number of rows and columns.
print("\n2. Print the first 5 rows, the last 3 rows, and the number of rows and columns.\n")
print("\n", movies_exercise.head(5))

# 3. Print the data type of each column and summary statistics for numeric columns.
print("\n3. Print the data type of each column and summary statistics for numeric columns\n")
print("\n", movies_exercise.info())

# 4. Print only the Title, Release Date, and IMDB Rating columns.
print("\n4. Print only the Title, Release Date, and IMDB Rating columns.\n")
print("\n", movies_exercise[["Title","Release Date","IMDB Rating"]] )

# 5. Filter and print movies with IMDB Rating greater than or equal to 8.
'''
movies = pd.read_json("datasets/Movies.json")

high_rated = movies[movies["IMDB Rating"] >= 8]

print(high_rated[["Title", "IMDB Rating"]])
'''
print("\n5. Filter and print movies with IMDB Rating greater than or equal to 8.\n")
# Create a boolean mask for movies with a rating >= 8
highest_rated_mask = movies_exercise["IMDB Rating"] >= 8
# Use the mask to filter the original DataFrame and print the relevant columns
print(movies_exercise[highest_rated_mask][["Title", "IMDB Rating"]])

# 6. Create a new column called Long Movie that is True when Running Time min is greater than or equal to 120.
movies_exercise["Long Movie"] = movies_exercise["Running Time min"] >= 120
print("\# 6. Create a new column called Long Movie that is True when Running Time min is greater than or equal to 120.\n")
print("\n", movies_exercise[["Title", "Running Time min","Long Movie"]])
long_movie_mask = movies_exercise["Running Time min"] >= 120
print("\n", movies_exercise[long_movie_mask][["Title", "Running Time min","Long Movie"]])

# 7. Count the number of movies per Major Genre.
print("\n7. Count the number of movies per Major Genre.\n")
print(movies_exercise.value_counts("Major Genre"))

# 8. Sort by IMDB Rating, print the top 10 rows, and add a short comment explaining why inspecting the schema is useful before cleaning data.
print("\n8. Sort by IMDB Rating, print the top 10 rows, and add a short comment explaining why inspecting the schema is useful before cleaning data.\n")
print("\nInspecting the schema before cleaning is useful because you need to know how complete or incomplete the data is, and what needs cleaning e.g. strings that should be numbers.\nData cleaning is not just replacing missing values. It is deciding what the data means, what is safe to change, and what should be left for review.\n")
print(movies_exercise.sort_values("IMDB Rating", ascending=False).head(10))