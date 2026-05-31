#### 3. Basics you should know
# +==========+==========+==========+==========+==========+
person = {
    "name": "Stelios",
    "age": 20, # I wish
    "city": "London"
}

# Access values
print(person["name"]) 

# Add new values
person["job"] = "Developer"

# Update existing values
person["city"] = "Athens"

# remove values:
del person["city"]

# Loop through dictionary using `items()`
for key, value in person.items():
    print(key, value)

#### 4. Read CSV rows as dictionaries
# +==========+==========+==========+==========+==========+
# *** Gemini error fix***
# pip install huggingface_hub
# hf download Birkbeck/movies movies.csv --repo-type dataset --local-dir .
# *** command line: Warning: `huggingface-cli` is deprecated and no longer works. Use `hf` instead.

import csv
import shutil
import subprocess
import tempfile
from pathlib import Path

FILE_PATH = Path("solutions\movies.csv")
INCOMPLETE_PATH = Path("data/movies_incomplete/movies.csv")

#### 4. Read CSV rows as dictionaries
with open(FILE_PATH, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

#### 5. Print one named column
# +==========+==========+==========+==========+==========+
with open(FILE_PATH, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["genres"])

#### 6. Count rows using a counter
# +==========+==========+==========+==========+==========+
count = 0
with open(FILE_PATH, "r", newline="",encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["year"] == "2020":
            count += 1
            print(f"\n {row["title"]} > {row["year"]} | Count:  {count}")

#### 7. Find first match with `break`
# Find the first row where `genres` contains `Action`. Fill up the missing code.
# +==========+==========+==========+==========+==========+
with open(FILE_PATH, "r", newline="",encoding="utf-8") as file:
    reader = csv.DictReader(file)
    print("\n# Find the first row where `genres` contains `Action`. Fill up the missing code.")
    for row in reader:
        if "Action" in row["genres"]:
            print(f"{row["title"]} | {row["genres"]}")
            break

#### 9. Exercise
# +==========+==========+==========+==========+==========+
'''
Use the `Birkbeck/movies` dataset from Hugging Face.

# 1. Examine the field names using `reader.fieldnames`. Print the names.
# 2. Print only the first 5 data rows.
# 3. Count how many movies are from the `USA`.
# 4. Find and print the first movie where `genres` is exactly `Action`.
# 5. Find and print the first movie where `Action` appears inside `genres`.
# 6. In one short comment, explain one benefit of `DictReader` over `csv.reader`.
# 7. What are the time and space complexities of your script(s)?

Use the `Birkbeck/movies_incomplete` dataset from Hugging Face.
Download it into a separate folder so it does not overwrite `movies.csv`:

mkdir -p data/movies_incomplete
hf download Birkbeck/movies_incomplete movies.csv --repo-type dataset --local-dir data/movies_incomplete
'''

# 1. Examine the field names using `reader.fieldnames`. Print the names.
print("\n# 1. Examine the field names using `reader.fieldnames`. Print the names.\n")
with open(FILE_PATH, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for name in reader.fieldnames:
        print(name)

# 2. Print only the first 5 data rows.
print("\n# 2. Print only the first 5 data rows.\n")
with open(FILE_PATH, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    count = 0
    for row in reader:
        if count < 5:
            print(row)
            count += 1


# 3. Count how many movies are from the `USA`.
print("\n# 3. Count how many movies are from the `USA`.\n")
with open(FILE_PATH, "r", newline="", encoding="utf-8") as file:
    count = 0
    reader = csv.DictReader(file)
    for row in reader:
        if row["country"]=="USA":
            count += 1
    print(count)

# 4. Find and print the first movie where `genres` is exactly `Action`.
print("\n# 4. Find and print the first movie where `genres` is exactly `Action`.\n")
with open(FILE_PATH, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["genres"]=="Action":
            print(row)
            break


# 5. Find and print the first movie where `Action` appears inside `genres`.
print("\n# 5. Find and print the first movie where `Action` appears inside `genres`.\n")
with open(FILE_PATH, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if "Action" in row["genres"]:
            print(row)
            break


# 6. In one short comment, explain one benefit of `DictReader` over `csv.reader`.
print("\n# 6. In one short comment, explain one benefit of `DictReader` over `csv.reader`.\n")
print('''
# With DictReader you can access data using column names like row['title'], but with csv.reader you must use index numbers like row[1], which breaks if the column order changes.
      ''')


# 7. What are the time and space complexities of your script(s)?
print("\n# 7. What are the time and space complexities of your script(s)?\n")
print("\nTime Complexity: O(n)")
print("\nSpace Complexity: O(1)")

# Use the `Birkbeck/movies_incomplete` dataset from Hugging Face.
# Download it into a separate folder so it does not overwrite `movies.csv`:
'''
mkdir -p data/movies_incomplete
hf download Birkbeck/movies_incomplete movies.csv --repo-type dataset --local-dir data/movies_incomplete
'''
# 1. Find the missing data point and print row and column.
print("\n1. Find the missing data point and print row and column.\n")
with open(INCOMPLETE_PATH, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # row.items() gives you (column_header, cell_value)
        for col_name, value in row.items():
            # Check if the cell is an empty string
            if value == "":
                print(f"Missing data found in Column: '{col_name}'")
                print(f"Row data: {row}\n")
                break

# 2. Find the average of `votes` from `data/movies_incomplete/movies.csv`. Why does the naive script fail? How can you fix it?
print("\n2. Find the average of `votes` from `data/movies_incomplete/movies.csv`. Why does the naive script fail? How can you fix it?\n")
with open(INCOMPLETE_PATH, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    total_votes = 0
    count = 0
    for row in reader:
        for col, val in row.items():
            if col=="votes" and val!="":
                val = float(val)
                count += 1
                total_votes += val
                # print(val)
    print(f"\nAverage votes: {total_votes/count}")

