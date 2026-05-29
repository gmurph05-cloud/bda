# Session 7 Homework - Reference solution

import pandas as pd


pokemon = pd.read_csv("datasets/Pokemon.csv", encoding="cp1252")

print("First 10 rows:")
print(pokemon.head(10))

print("\nLast 5 rows:")
print(pokemon.tail(5))

print("\nRows and columns:")
print(pokemon.shape)

print("\nOriginal columns:")
print(pokemon.columns)

print("\nOriginal data types:")
print(pokemon.dtypes)

pokemon = pokemon.rename(
    columns={
        "#": "pokemon_id",
        "Name": "name",
        "Type 1": "type_1",
        "Type 2": "type_2",
        "Total": "total",
        "HP": "hp",
        "Attack": "attack",
        "Defense": "defense",
        "Sp. Atk": "sp_atk",
        "Sp. Def": "sp_def",
        "Speed": "speed",
        "Stage": "stage",
        "Legendary": "legendary",
    }
)

print("\nRenamed columns:")
print(pokemon.columns)

print("\nMissing values before cleaning:")
print(pokemon.isnull().sum())

pokemon["type_2"] = pokemon["type_2"].fillna("None")

print("\nMissing values after cleaning type_2:")
print(pokemon.isnull().sum())

print("\nSummary statistics:")
print(pokemon.describe())

highest_attack = pokemon.loc[pokemon["attack"].idxmax()]
highest_defense = pokemon.loc[pokemon["defense"].idxmax()]
highest_speed = pokemon.loc[pokemon["speed"].idxmax()]

print("\nHighest attack:")
print(highest_attack[["name", "attack"]])

print("\nHighest defense:")
print(highest_defense[["name", "defense"]])

print("\nHighest speed:")
print(highest_speed[["name", "speed"]])

print("\nPokemon per type_1:")
print(pokemon["type_1"].value_counts())

print("\nAverage total score per type_1:")
average_total_by_type = pokemon.groupby("type_1")["total"].mean().sort_values(ascending=False)
print(average_total_by_type)

pokemon["power_score"] = pokemon["attack"] + pokemon["defense"] + pokemon["speed"]

print("\nTop 10 Pokemon by power_score:")
print(pokemon.sort_values("power_score", ascending=False)[["name", "type_1", "power_score"]].head(10))

pokemon.to_csv("solutions/pokemon_clean.csv", index=False)

# Reflection answers:
# 1. The type_2 column needed the most obvious cleaning because many Pokemon do
#    not have a second type, so those values were missing.
# 2. Renaming columns is useful because simple lowercase names with underscores
#    are easier to type and less likely to cause mistakes in code.
# 3. The highest average total score can be checked from average_total_by_type.
# 4. power_score ignores hp, special attack, special defense, stage, type, and
#    context, so it is only a simple ranking, not a complete strength measure.
