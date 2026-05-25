# Session 7 Part 3 - Exercise solution

import numpy as np
import pandas as pd


scores = np.array([72, 85, 91, 64, 78, 88, 93, 70])

print("Scores:")
print(scores)

print("\nShape and data type:")
print(scores.shape)
print(scores.dtype)

print("\nBasic statistics:")
print("Mean:", np.mean(scores))
print("Minimum:", np.min(scores))
print("Maximum:", np.max(scores))
print("Standard deviation:", np.std(scores))

scores_plus_10 = scores + 10

print("\nScores plus 10:")
print(scores_plus_10)

print("\nScores >= 80:")
print(scores[scores >= 80])

numbers = np.arange(1, 21)

print("\nNumbers from 1 to 20:")
print(numbers)

print("\nEven numbers:")
print(numbers[numbers % 2 == 0])

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])

print("\nMatrix:")
print(matrix)

print("\nMatrix shape:")
print(matrix.shape)

print("\nFirst row:")
print(matrix[0, :])

print("\nSecond column:")
print(matrix[:, 1])

pokemon = pd.read_csv("datasets/Pokemon.csv", encoding="cp1252")
attack_values = pokemon["Attack"].to_numpy()

print("\nAverage Pokemon attack:")
print(np.mean(attack_values))

print("\nPokemon attack values >= 120:")
print(attack_values[attack_values >= 120])

# A Python list can store mixed types and is very flexible. A NumPy array is
# designed for fast numeric operations over many values at once.
