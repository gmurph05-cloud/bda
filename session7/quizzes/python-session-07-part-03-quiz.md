# Session 7 Part 3 quiz

## Question 1

What is NumPy mainly used for?

- Fast numeric work with arrays.
- Creating virtual environments.
- Styling markdown files.
- Running Git commands.

Answer: 1
Type: single
Time: 45
Explanation: NumPy is designed for efficient numeric arrays and calculations.


## Question 2

What is the common import alias for NumPy?

- `import numpy as np`
- `import numpy as pd`
- `import np as numpy`
- `import array as np`

Answer: 1
Type: single
Time: 45
Explanation: NumPy is almost always imported with the alias `np`.


## Question 3

What does `array.shape` show?

- The size of the array in each dimension.
- The first value in the array.
- The average value in the array.
- The file path of the array.

Answer: 1
Type: single
Time: 45
Explanation: `shape` describes the dimensions of the array.


## Question 4

What is a vectorised operation?

- An operation applied to many values at once.
- A command that deletes missing values.
- A way to rename DataFrame columns.
- A special kind of markdown heading.

Answer: 1
Type: single
Time: 60
Explanation: Vectorised operations let NumPy calculate across arrays without an explicit Python loop.


## Question 5

What does this code print?

```python
scores = np.array([70, 85, 90])
print(scores[scores >= 80])
```

- `[85 90]`
- `[70 85 90]`
- `[True True False]`
- `[70]`

Answer: 1
Type: single
Time: 60
Explanation: The boolean condition keeps only values greater than or equal to 80.


## Question 6

How can you convert a pandas column to a NumPy array?

- `df["column"].to_numpy()`
- `df["column"].to_list_array()`
- `np.read_column(df, "column")`
- `df.numpy["column"]`

Answer: 1
Type: single
Time: 45
Explanation: pandas Series objects have a `to_numpy()` method.
