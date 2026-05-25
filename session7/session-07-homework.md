### Session 7 | Homework

> In this homework, you will use pandas to inspect, clean, and summarise a dataset. Work slowly and check your output after every step.

#### 1. Goal

You will:

- load a CSV file with pandas
- inspect rows, columns, and data types
- clean column names
- handle missing values
- calculate basic statistics
- group data by category
- create a new calculated column
- save a cleaned dataset

#### 2. Dataset

Use this file:

```txt
session7/datasets/Pokemon.csv
```

This CSV uses an older text encoding. Load it like this:

```python
import pandas as pd

pokemon = pd.read_csv("datasets/Pokemon.csv", encoding="cp1252")
```

Run your script from the `session7` folder:

```bash
python solutions/exercise-07-homework.py
```

#### 3. File to submit

Create this file:

```txt
session7/solutions/exercise-07-homework.py
```

#### 4. Tasks

Complete all 10 tasks in your Python file.

1. Load `Pokemon.csv` into a DataFrame called `pokemon`.
2. Print the first 10 rows and the last 5 rows.
3. Print the number of rows and columns.
4. Print the column names and data types.
5. Rename the columns so they are easier to use in Python:
   - `#` -> `pokemon_id`
   - `Name` -> `name`
   - `Type 1` -> `type_1`
   - `Type 2` -> `type_2`
   - `Total` -> `total`
   - `HP` -> `hp`
   - `Attack` -> `attack`
   - `Defense` -> `defense`
   - `Sp. Atk` -> `sp_atk`
   - `Sp. Def` -> `sp_def`
   - `Speed` -> `speed`
   - `Stage` -> `stage`
   - `Legendary` -> `legendary`
6. Check missing values in every column. Fill missing `type_2` values with `"None"`.
7. Print summary statistics for the numeric columns.
8. Find and print:
   - the Pokemon with the highest `attack`
   - the Pokemon with the highest `defense`
   - the Pokemon with the highest `speed`
9. Group by `type_1` and print:
   - the number of Pokemon per type
   - the average `total` score per type, sorted from highest to lowest
10. Create a new column called `power_score` using this formula:

```python
power_score = attack + defense + speed
```

Then print the top 10 Pokemon by `power_score` and save the cleaned DataFrame to:

```txt
session7/solutions/pokemon_clean.csv
```

#### 5. Reflection

At the bottom of your Python file, add comments answering these questions:

1. Which column needed the most obvious cleaning?
2. Why is it useful to rename columns before analysis?
3. Which `type_1` has the highest average `total` score?
4. What is one limitation of ranking Pokemon only by `power_score`?

#### 6. Rules

- Use pandas.
- Do not edit the original dataset in `datasets/`.
- Keep your solution in `solutions/`.
- Use clear variable names.
- Print enough output to show that each task works.
- Add short comments where you make a cleaning decision.

#### 7. Reminder

Try the homework yourself before checking the reference solution.
