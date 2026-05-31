'''
#### 4. Tasks

# 1. Load the dataset with `csv.reader`.
# 2. Print:
#    - the number of data rows (excluding header)
#    - the number of columns
# 3. Print the first 3 rows (including header).
# 4. Find and print the first movie where the `genres` column contains `Action`.
# 5. Compute and print the average of `rating_imdb` (ignore missing or invalid values).
# 6. Compute and print the average of one more numeric column (for example `runtime_min` or `metascore`, ignoring missing values).
# 7. Count how many movies have `rating_imdb >= 8.0`.
# 8. Report the time and space complexity for:
#    - first-match search task
#    - average computation task
'''

import csv
import os
import subprocess

FILE_PATH = "movies.csv"

# Dataset
#   Use: movies.csv from Birkbeck/movies
# hf download Birkbeck/movies movies.csv --repo-type dataset --local-dir .

# *** Gemini error fix***
# pip install huggingface_hub
# huggingface-cli download Birkbeck/movies movies.csv --repo-type dataset --local-dir .
# *** command line: Warning: `huggingface-cli` is deprecated and no longer works. Use `hf` instead.


# Tasks
# 1. Load the dataset with csv.reader.
with open("movies.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)

# **************************************************************************

# 2. Print:
#    - the number of data rows (excluding header)
#    - the number of columns
with open("movies.csv", "r", newline="", encoding="utf-8") as file:
    print('''
    # 2. Print:
    #    - the number of data rows (excluding header)
    #    - the number of column''')
    reader = csv.reader(file)
    header = next(reader)
    num_of_rows = 0
    num_of_cols = len(header)

    for row_number, row in enumerate(reader, start=2):
        num_of_rows += 1

    print(f'Number of rows: {num_of_rows} | Number of columns: {num_of_cols}')

# 3. Print the first 3 rows (including header).
with open("movies.csv", "r", newline="", encoding="utf-8") as file:
    print("\n,", "3. Print the first 3 rows (including header)")
    reader = csv.reader(file)
    num_of_rows = 0
    for row_num, row in enumerate(reader, start=1):
        if row_num <= 3:
            print(f'Row number: {row_num} | Row text: {row}')
            num_of_rows += 1
    
    
# **************************************************************************

# 4. Find and print the first movie where the genres column contains Action.
with open("movies.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    print("\n","4. Find and print the first movie where the genres column contains Action.")
    header = next(reader)
    counter = 0
    for row_num, row in enumerate(reader, start=2):
        if counter < 1:
            for col_num, col in enumerate(row, start=1):
                if "Action" in col:
                    print(f'First action movie: , {row}')
                    print(f'Genre: {col}')
                    counter += 1
                
# **************************************************************************
#              
# 5. Compute and print the average of rating_imdb (ignore missing or invalid values).
with open("movies.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)
    print("\n", "5. Compute and print the average of rating_imdb (ignore missing or invalid values).")

    # 1. Find the column index (do this once outside the main loop)
    rating_imdb_col_num = header.index("rating_imdb")

    rating_imdb_avg = 0.0
    valid_row_counter = 0

    # for row_num, row in enumerate(reader, start=1):
    #     for col_num, col in enumerate(row, start=1):
    #         if "rating_imdb" in col:
    #             rating_imdb_col_num = col_num
    #     break

    # Iterate through the data
    for row_num, row in enumerate(reader, start=2):
        # check if row is valid
        if len(row) > rating_imdb_col_num:
            raw_value = row[rating_imdb_col_num]

            try:
                # try to convert string to float
                rating = float(raw_value)
                rating_imdb_avg += rating
                valid_row_counter += 1
            except ValueError:
                # this executes if raw_value is "" or "N/A", etc
                continue

        # row_counter += 1
        # for col_num, col in enumerate(row, start=1):
        #     if col_num == rating_imdb_col_num:
        #         rating_imdb_avg = rating_imdb_avg + float(col)

    # Calculate and print average
    if valid_row_counter > 0:
        average = rating_imdb_avg / valid_row_counter
        print(f'Average IMDB Rating: {average:.2f} (based on {valid_row_counter} valid records)')
    else:
        print("No valid ratings found.")

# **************************************************************************

# 6. Compute and print the average of one more numeric column (for example runtime_min or metascore, ignoring missing values).
target_columns = ["rating_imdb", "runtime_min", "votes", "revenue_musd", "metascore"]

with open("movies.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)

    # Map column names to their index for fast lookup: O(1)
    col_indices = {name: header.index(name) for name in target_columns}
    
    # Initialize data store: { 'column_name': [sum, count] }
    stats = {name: [0.0, 0] for name in target_columns}

    for row in reader:
        for name, idx in col_indices.items():
            if len(row) > idx:
                try:
                    val = float(row[idx])
                    stats[name][0] += val # Add to sum
                    stats[name][1] += 1   # Increment count
                except ValueError:
                    continue

# Print results elegantly
print("\n", "6. Compute and print the average of one more numeric column (for example runtime_min or metascore, ignoring missing values).", "\n")
print(f"{'Column':<15} | {'Average':<10} | {'Valid Records'}")
print("-" * 45)
for name, (total, count) in stats.items():
    avg = total / count if count > 0 else 0
    print(f"{name:<15} | {avg:<10.2f} | {count}")

# **************************************************************************

# 7. Count how many movies have rating_imdb >= 8.0.
with open("movies.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)
    print("\n", "7. Count how many movies have rating_imdb >= 8.0.")

    # 1. Find the column index (do this once outside the main loop)
    rating_imdb_col_num = header.index("rating_imdb")

    valid_row_counter = 0
    rating_counter = 0 

    # Iterate through the data
    for row_num, row in enumerate(reader, start=2):
        # check if row is valid
        if len(row) > rating_imdb_col_num:
            raw_value = row[rating_imdb_col_num]
            valid_row_counter += 1
            
            try:
                # try to convert string to float
                rating = float(raw_value)
                if rating >= 8.0:
                    rating_counter += 1
            except ValueError:
                # this executes if raw_value is "" or "N/A", etc
                continue

    # Calculate total number of movies with rating >= 8.0
    if valid_row_counter > 0:
        print(f'Number of movies with rating_imdb >= 8.0: {rating_counter} (based on {valid_row_counter} valid records)')
    else:
        print("No valid ratings found.")

# **************************************************************************

# 8. Report the time and space complexity for:
#   - first-match search task
#   - average computation task

print("""
    # 8. Report the time and space complexity for:
    #   - first-match search task
    #   - average computation task
    # """)

print(f"""
      # first-match search task:
      # time complexity = O(n)
      # space complexity = O(1)
      # """)
print(f"""
      # average computation task:
      # time complexity = O(n)
      # space complexity = O(1)
      # """)

# **************************************************************************