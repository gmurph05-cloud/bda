'''
#### 1. Goal

You will learn this exact sequence:

1. create data with a missing value
2. detect what is missing
3. update/fix the missing value
4. save cleaned data to disk
'''

import csv
import shutil
import subprocess
import tempfile
from pathlib import Path
import os

#### 2. Mini tutorial
# +==========+==========+==========+==========+==========+
# 1. create data with a missing value
movies = [
    {
        "title": "Howl's Moving Castle",
        "year": "2004",
        "director": "Hayao Miyazaki",
        "music_by": "",
    },
    {
        "title": "Kiki's Delivery Service",
        "year": "",
        "director": "Hayao Miyazaki",
        "music_by": "Joe Hisaishi",
    },
]

# 2. detect what is missing
for row in movies:
    for col, val in row.items():
        if val=="":
            print(f"\nValue is missing in row {row}")
            print(f"\nValue missing for \ncolumn: {col} \nvalue: {val} ")

# stelios solution
print("\# stelios solution\n")
for i, movie in enumerate(movies, start=1):
    if movie["music_by"].strip() == "":
        print(f"Record {i} missing field: music_by")
    if movie["year"].strip() == "":
        print(f"Record {i} missing field: year")
                  
# 3. update/fix the missing value
for row in movies:
    for col, val in row.items():
        if val == "":
            if col == "year":
                row[col] = "2026"  # Updated directly in the row dictionary
            if col == "music_by":
                row[col] = "John Williams"  # Updated directly in the row dictionary
            
            print(f"\nValue is replaced in row {row}")
            print(f"Column: {col} -> New Value: {row[col]}")
# 3. update/fix the missing value - stelios solution:
# print("\n# 3. update/fix the missing value - stelios solution:\n")
# if movies[0]["music_by"].strip() == "":
#     movies[0]["music_by"] = "Joe Hisaishi"

# if movies[1]["year"].strip() == "":
#     movies[1]["year"] = "1989"

# print(movies)

# 4. save cleaned data to disk
# 4.1. Define the folder and file path
folder_name = "data"
file_name = "movies_output.csv"
file_path = os.path.join(folder_name, file_name)

# 4.2. Create the 'solutions' folder if it doesn't exist yet
os.makedirs(folder_name, exist_ok=True)

# 4.3. Extract the headers (keys) from the first dictionary
headers = movies[0].keys()

# 4.4. Write the data to the CSV file
with open(file_path, "w", newline="", encoding="utf-8") as file:
    
    # Pass the file object and the headers to the DictWriter
    writer = csv.DictWriter(file, fieldnames=headers)

    # Write the header row (title, year, director, music_by)
    writer.writeheader()

    # Write all the dictionary rows at once
    writer.writerows(movies)

print(f"Success! File saved to: {file_path}")

#### 5. Keep a copy for safekeeping
# +==========+==========+==========+==========+==========+
movies = [
    {
        "title": "Howl's Moving Castle",
        "year": "2004",
        "director": "Hayao Miyazaki",
        "music_by": "",
    },
    {
        "title": "Kiki's Delivery Service",
        "year": "",
        "director": "Hayao Miyazaki",
        "music_by": "Joe Hisaishi",
    },
]

original_movies = [movie.copy() for movie in movies]
cleaned_movies = [movie.copy() for movie in movies]

if cleaned_movies[0]["music_by"].strip() == "":
    cleaned_movies[0]["music_by"] = "Joe Hisaishi"

if cleaned_movies[1]["year"].strip() == "":
    cleaned_movies[1]["year"] = "1989"

print("Original:", original_movies)
print("Cleaned:", cleaned_movies)

#### 6. Save cleaned dictionary to disk
# +==========+==========+==========+==========+==========+
import json

with open("data\movies_clean.json", "w", encoding="utf-8") as file:
    json.dump(cleaned_movies, file, ensure_ascii=False, indent=2)

print("Saved: movies_clean.json")

#### 7. Exercise: apply same logic to CSV dataset

# pip install huggingface_hub
# hf download Birkbeck/movies movies.csv --repo-type dataset --local-dir .

#### Choose 'paste as one line in CMD when prompted'
"""
hf download Birkbeck/studio_ghibli_movies studio_ghibli_movies.csv \
  --repo-type dataset \
  --local-dir . 
"""

#### 8. Exercise tasks
# +==========+==========+==========+==========+==========+
GHIBLI_MOVIES = "data\studio_ghibli_movies.csv"
# 1. Load the `studio_ghibli_movies.csv` dataset with `csv.DictReader`.
# original_movies_ghibli = [movie.copy() for movie in movies]
# copy_movies_ghibli = GHIBLI_MOVIES

print("\n# 2. Find missing values by column and print where they are (line number + movie title).\n")
with open(GHIBLI_MOVIES,"r", newline="") as file:
    reader = csv.DictReader(file)
    # 2. Find missing values by column and print where they are (line number + movie title).

    # enumerate gives you the line number (idx) and the row data
    for idx, row in enumerate(reader, start=2):
        # print(row)
        for col, val in row.items():
            if val == "":
                print("\nMissing Value Found:")
                print(f"Line Number (Row Index): {idx}")
                print(f"Movie Title: {row.get('title', 'Unknown')}")
                print(f"Column: {col}")
                print("-" * 30)

# 3. Fix missing values (for this dataset, check `year` and `music_by`).

# 4. Calculate:
#    - average of `year`
#    - how many times Miyazaki appears as director
with open(GHIBLI_MOVIES, "r", newline="") as file:
    reader = csv.DictReader(file)
    year_total = 0
    year_count = 0
    avg_of_year = 0
    count_director = 0
    for row in reader:
        for col, val in row.items():
            if col == "year" and val != "":
                year_total += int(val)
                year_count += 1

            if "Miyazaki" in val:
                count_director += 1

    avg_of_year = round(year_total / year_count)
    print(f"\n- average of `year`: {avg_of_year}")
    print(f"\n- how many times Miyazaki appears as director:\n {count_director}")

# 5. Save cleaned rows into a new file:
#    - `studio_ghibli_movies_clean.csv`

import csv
import os

def fix_ghibli_movies(input_path, output_path):
    # Verified facts from the internet mapping movie titles to their missing attributes
    internet_facts = {
        "Howl's Moving Castle": {"music_by": "Joe Hisaishi"},
        "Kiki's Delivery Service": {"year": "1989"},
        "Ponyo": {"year": "2008"}
    }
    
    cleaned_rows = []
    headers = []
    
    # 1. Read the incomplete data into memory
    with open(input_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames  # Preserve original headers
        
        for row in reader:
            title = row.get("title")
            
            # Check if this movie has a missing point that we have facts for
            if title in internet_facts:
                for col, correct_value in internet_facts[title].items():
                    # If the value is empty, replace it directly inside the row dictionary
                    if row[col] == "":
                        row[col] = correct_value
                        print(f"Fixed '{title}': Populated missing {col} with '{correct_value}'")
                        
            cleaned_rows.append(row)
            
    # 2. Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # 3. Write the fully updated rows to a new external file
    with open(output_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(cleaned_rows)
        
    print(f"\nSuccess! Fixed file saved to: {output_path}")

# --- Execute the function ---
INPUT_FILE = GHIBLI_MOVIES
OUTPUT_FILE = "data/studio_ghibli_movies_clean.csv"

fix_ghibli_movies(INPUT_FILE, OUTPUT_FILE)
                

# 6. Re-check missing values after cleaning and print remaining missing count.
print("\n# 6. Re-check missing values after cleaning and print remaining missing count.\n")
FILE_PATH = OUTPUT_FILE
def check_missing_vals(file_path):
    with open(file_path,"r", newline="") as file:
        reader = csv.DictReader(file)
        # 2. Find missing values by column and print where they are (line number + movie title).

        # enumerate gives you the line number (idx) and the row data
        missing_val_count = 0
        for idx, row in enumerate(reader, start=2):
            # print(row)
            for col, val in row.items():
                if val == "":
                    print("\nMissing Value Found:")
                    print(f"Line Number (Row Index): {idx}")
                    print(f"Movie Title: {row.get('title', 'Unknown')}")
                    print(f"Column: {col}")
                    print("-" * 30)
                    missing_val_count += 1
        if missing_val_count == 0:
            print("\nNo missing values found.")

check_missing_vals(FILE_PATH)

# 7. What are the time and space complexities of your full script?