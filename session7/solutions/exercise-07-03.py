### Session 7 | Part 3

#> NumPy is the foundation underneath much of the Python data stack. pandas is built on top of it, so learning NumPy helps you understand why pandas is fast with numeric data.

'''
#### 1. Goal

# In this tutorial, you will:

# - import NumPy
# - create NumPy arrays
# - inspect array shape and data type
# - perform vectorised calculations
# - select and filter array values
# - create simple 2D arrays
# - connect NumPy arrays back to pandas

#### 3. Basics you should know

- `NumPy`: a Python library for fast numeric arrays.
- `array`: a collection of values with the same general data type.
- `shape`: the size of an array in each dimension.
- `dtype`: the data type stored in an array.
- `vectorised operation`: an operation applied to many values at once.
- `boolean mask`: a True/False array used to filter values.
- `2D array`: a table-like array with rows and columns.

'''

import numpy as np

print(np.__version__)

#### 5. Create a NumPy array
# Create a simple array from a Python list.
# ==========+==========+==========+==========+==========+
print("\n#### 5. Create a NumPy array")
scores = np.array([72, 85, 91, 64, 78])

print("\nScores: ",scores)
print("\nScores types: ", type(scores))

#### 6. Inspect shape and data type
# Arrays have a shape and a data type.
# > For a one-dimensional array, the shape shows how many values are in the array.
# ==========+==========+==========+==========+==========+
print("\n#### 6. Inspect shape and data type")
scores = np.array([72, 85, 91, 64, 78])

print("\nScores shape: ", scores.shape)
print("\nScores dtype: ", scores.dtype)

#### 7. Basic statistics
# NumPy can calculate common statistics.
# ==========+==========+==========+==========+==========+
print("\n#### 7. Basic statistics")
scores = np.array([72, 85, 91, 64, 78])

print("\nnp.mean(scores): ", np.mean(scores))
print("\nnp.min(scores): ", np.min(scores))
print("\nnp.max(scores): ", np.max(scores))
print("\nnp.std(scores): ", np.std(scores))

#### 8. Vectorised calculations
# With NumPy, you can apply a calculation to the whole array at once.
# ==========+==========+==========+==========+==========+
print("\n8. Vectorised calculations")
scores = np.array([72, 85, 91, 64, 78])
scores_plus_5 = scores + 5

print("\nscores_plus_5 = scores + 5: \n", scores_plus_5)

#### 9. Boolean filtering
# Create a True/False mask, then use it to filter values.
# ==========+==========+==========+==========+==========+
print("\n9. Boolean filtering")
scores = np.array([72, 85, 91, 64, 78])

mask = scores >= 80

print("\nscores: ", scores)
print("\nmask: ", mask) 
print("\nscores[mask]: ", scores[mask])

#### 10. Create arrays with ranges
# Use `arange()` to create regular numeric sequences.
# ==========+==========+==========+==========+==========+
print("\n10. Create arrays with ranges")
numbers = np.arange(1, 11)

print("\np.arange(1, 11): ", numbers)
print("\nnumbers * 2: ", numbers * 2)


#### 11. Create a 2D array
# A 2D array is useful for matrix-style data.
# ==========+==========+==========+==========+==========+
print("\n11. Create a 2D array")
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
])

print(matrix)
print(matrix.shape)

#### 12. Select rows and columns
# Use row and column indexes to select values from a 2D array.
# ==========+==========+==========+==========+==========+
print("\n12. Select rows and columns")
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
])

print("\nmatrix[0, 0]: ", matrix[0, 0])
print("\nmatrix[0, :]: ", matrix[0, :])
print("\nmatrix[:, 1]: ", matrix[:, 1])

#### 13. Use NumPy with pandas data
# You can convert a pandas column to a NumPy array.
# ==========+==========+==========+==========+==========+
print("\n#### 13. Use NumPy with pandas data")
import numpy as np
import pandas as pd

pokemon = pd.read_csv("datasets/Pokemon.csv", encoding="cp1252")

attack_values = pokemon["Attack"].to_numpy()

print("\nattack_values[:10]: ", attack_values[:10])
print("\nnp.mean(attack_values): ", np.mean(attack_values))

#### 14. Exercise
# ==========+==========+==========+==========+==========+
'''
Tasks:

# 1. Import NumPy as `np`.
# 2. Create an array called `scores` with at least 8 numeric values.
# 3. Print the array, shape, and data type.
# 4. Print the mean, minimum, maximum, and standard deviation.
# 5. Create a new array called `scores_plus_10`, then filter and print only scores greater than or equal to `80`.
# 6. Create an array with numbers from `1` to `20`, then print only the even numbers.
# 7. Create a 3 by 3 matrix, print its shape, print the first row, and print the second column.
# 8. Load `Pokemon.csv` with pandas, convert the `Attack` column to a NumPy array, print the average attack, print attack values greater than or equal to `120`, and add a short comment explaining one difference between a Python list and a NumPy array.
'''

# 1. Import NumPy as `np`.
print("\n# 1. Import NumPy as `np`.")
import numpy as np


# 2. Create an array called `scores` with at least 8 numeric values.
print("\n# 2. Create an array called `scores` with at least 8 numeric values.")
scores = np.array([40, 50, 60, 70, 80, 90, 100, 110])
print("\nscores: ", scores)


# 3. Print the array, shape, and data type.
print("\n# 3. Print the array, shape, and data type.")
print("\nArray: ", scores)
print("\nArray shape: ", scores.shape)
print("\nArray type: ", type(scores) )


# 4. Print the mean, minimum, maximum, and standard deviation.
print("\n# 4. Print the mean, minimum, maximum, and standard deviation.")
print("\nScores mean: ", np.mean(scores))
print("\nScores minimum", np.min(scores))
print("\nScores maximum", np.max(scores))
print("\nScores standard deviation", np.std(scores))


# 5. Create a new array called `scores_plus_10`, then filter and print only scores greater than or equal to `80`.
print("\n# 5. Create a new array called `scores_plus_10`, then filter and print only scores greater than or equal to `80`.")
scores_plus_10 = scores >= 80
print("\nscores_plus_10: ", scores[scores_plus_10])


# 6. Create an array with numbers from `1` to `20`, then print only the even numbers.
print("\n# 6. Create an array with numbers from `1` to `20`, then print only the even numbers.")
one_twenty = np.arange(1,20)
one_twenty_even = one_twenty[one_twenty % 2 == 0]
print("\none_twenty", one_twenty)
print("\none_twenty_even", one_twenty_even)


# 7. Create a 3 by 3 matrix, print its shape, print the first row, and print the second column.
print("\n# 7. Create a 3 by 3 matrix, print its shape, print the first row, and print the second column.")
three_squared = np.array([
    [10, 20, 30], 
    [40, 50, 60], 
    [70, 80, 90]])
print("\nthree_squared: \n", three_squared)
print("\nthree_squared - first row: \n", three_squared[0,:])
print("\nthree_squared - second column: \n", three_squared[:,1])


# 8. Load `Pokemon.csv` with pandas, convert the `Attack` column to a NumPy array, print the average attack, print attack values greater than or equal to `120`, and add a short comment explaining one difference between a Python list and a NumPy array.
print("\n# 8. Load `Pokemon.csv` with pandas, convert the `Attack` column to a NumPy array, print the average attack, print attack values greater than or equal to `120`, and add a short comment explaining one difference between a Python list and a NumPy array.")
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
attack = pokemon["Attack"].to_numpy()
print("\nPokemon: \n", pokemon)
print("\nPokemon attack: \n", attack)

# Difference: NumPy arrays require all elements to be the same data type (homogenous) for faster mathematics calculations, 
# while Python lists can hold a mix of different data types (heterogeneous).

