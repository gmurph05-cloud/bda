### Session 7 | Homework
# ==========+==========+==========+==========+==========+

#### 1. Goal
# ==========+==========+==========+==========+==========+
'''
# You will:

# - load a CSV file with pandas
# - inspect rows, columns, and data types
# - clean column names
# - handle missing values
# - calculate basic statistics
# - group data by category
# - create a new calculated column
# - save a cleaned dataset
'''


#### 4. Tasks
# ==========+==========+==========+==========+==========+
'''
Complete all 10 tasks in your Python file.

# 1. Load `Pokemon.csv` into a DataFrame called `pokemon`.
# 2. Print the first 10 rows and the last 5 rows.
# 3. Print the number of rows and columns.
# 4. Print the column names and data types.
# 5. Rename the columns so they are easier to use in Python:
#    - `#` -> `pokemon_id`
#    - `Name` -> `name`
#    - `Type 1` -> `type_1`
#    - `Type 2` -> `type_2`
#    - `Total` -> `total`
#    - `HP` -> `hp`
#    - `Attack` -> `attack`
#    - `Defense` -> `defense`
#    - `Sp. Atk` -> `sp_atk`
#    - `Sp. Def` -> `sp_def`
#    - `Speed` -> `speed`
#    - `Stage` -> `stage`
#    - `Legendary` -> `legendary`
# 6. Check missing values in every column. Fill missing `type_2` values with `"None"`.
# 7. Print summary statistics for the numeric columns.
# 8. Find and print:
#    - the Pokemon with the highest `attack`
#    - the Pokemon with the highest `defense`
#    - the Pokemon with the highest `speed`
# 9. Group by `type_1` and print:
#    - the number of Pokemon per type
#    - the average `total` score per type, sorted from highest to lowest
# 10. Create a new column called `power_score` using this formula:
# power_score = attack + defense + speed
# Then print the top 10 Pokemon by `power_score` and save the cleaned DataFrame to: session7/solutions/pokemon_clean.csv
'''

# 1. Load `Pokemon.csv` into a DataFrame called `pokemon`.
# ==========+==========+==========+==========+==========+
import pandas as pd
# pip install chardet to detect csv encoding
import chardet

# Read the first 10,000 bytes to guess the encoding
with open("datasets/Pokemon.csv", "rb") as f:
    raw_data = f.read(10000)
    result = chardet.detect(raw_data)

print(f"Predicted Encoding: {result['encoding']}")
print(f"Confidence: {result['confidence'] * 100}%")

pokemon = pd.read_csv("datasets/Pokemon.csv", encoding="cp1252")

# 2. Print the first 10 rows and the last 5 rows.
# ==========+==========+==========+==========+==========+
print("\n# 2. Print the first 10 rows and the last 5 rows.")
print("\nfirst 10 rows: \n", pokemon.head(10))
print("\nthe last 5 rows: \n", pokemon.tail(5))


# 3. Print the number of rows and columns.
# ==========+==========+==========+==========+==========+
print("\n# 3. Print the number of rows and columns.")
print("\nnumber of rows and columns: ", pokemon.shape)


# 4. Print the column names and data types.
# ==========+==========+==========+==========+==========+
print("\n# 4. Print the column names and data types.\n")
print(pokemon.info())



# 5. Rename the columns so they are easier to use in Python:
# ==========+==========+==========+==========+==========+
print("\n# 5. Rename the columns so they are easier to use in Python:\n")
pokemon.columns = pokemon.columns.str.strip()
pokemon.columns = pokemon.columns.str.lower()
pokemon.columns = pokemon.columns.str.replace(" ","_")
pokemon.columns = pokemon.columns.str.replace(".","")
print(pokemon)

# 6. Check missing values in every column. Fill missing `type_2` values with `"None"`.
# ==========+==========+==========+==========+==========+
print("\n# 6. Check missing values in every column. Fill missing `type_2` values with `'None'`.")
print("\nBefore filling missing\n", pokemon.isnull().sum())
pokemon["type_2"] = pokemon["type_2"].fillna("None")
print("\n", pokemon)
print("\nAfter filling missing: \n", pokemon.isnull().sum())


# 7. Print summary statistics for the numeric columns.
# ==========+==========+==========+==========+==========+
print("\n# 7. Print summary statistics for the numeric columns.")
print("\n", pokemon.describe())
print("\n", pokemon.describe()["stage"])
print("\n", pokemon.describe()[["defense", "attack", "speed"]])


# 8. Find and print:
#    - the Pokemon with the highest `attack`
#    - the Pokemon with the highest `defense`
#    - the Pokemon with the highest `speed`
# ==========+==========+==========+==========+==========+
print('''
# 8. Find and print:
#    - the Pokemon with the highest `attack`
#    - the Pokemon with the highest `defense`
#    - the Pokemon with the highest `speed`
''')
print("\nthe Pokemon with the highest `attack`: ", pokemon["attack"].max())
print("\nthe Pokemon with the highest `defense`: ", pokemon["defense"].max())
print("\nthe Pokemon with the highest `speed`: ", pokemon["speed"].max())


# 9. Group by `type_1` and print:
#    - the number of Pokemon per type
#    - the average `total` score per type, sorted from highest to lowest
# ==========+==========+==========+==========+==========+
print('''
# 9. Group by `type_1` and print:
#    - the number of Pokemon per type
#    - the average `total` score per type, sorted from highest to lowest
''')
pokemon_type_1_count = pokemon.groupby("type_1").count()
print("\nthe number of Pokemon per type:\n", pokemon_type_1_count)
print("\nthe number of Pokemon per type:\n", pokemon_type_1_count["total"])


# 10. Create a new column called `power_score` using this formula:
# power_score = attack + defense + speed
# Then print the top 10 Pokemon by `power_score` and save the cleaned DataFrame to: session7/solutions/pokemon_clean.csv
# ==========+==========+==========+==========+==========+
print('''
# 10. Create a new column called `power_score` using this formula:
# power_score = attack + defense + speed
# Then print the top 10 Pokemon by `power_score` and save the cleaned DataFrame to: session7/solutions/pokemon_clean.csv
''')

power_score = pokemon["attack"] + pokemon["defense"] + pokemon["speed"]
print("\nPokemon: \n", pokemon.head(10))
print("\ntop 10 Pokemon by `power_score`\n", power_score.head(10))
pokemon.to_csv("solutions/pokemon_clean.csv")