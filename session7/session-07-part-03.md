### Session 7 | Part 3

> NumPy is the foundation underneath much of the Python data stack. pandas is built on top of it, so learning NumPy helps you understand why pandas is fast with numeric data.

#### 1. Goal

In this tutorial, you will:

- import NumPy
- create NumPy arrays
- inspect array shape and data type
- perform vectorised calculations
- select and filter array values
- create simple 2D arrays
- connect NumPy arrays back to pandas

#### 2. Prerequisites

Before starting:

1. Open the `session7` folder in Visual Studio Code.
2. Activate your virtual environment.
3. Confirm dependencies are installed:

```bash
pip install -r requirements.txt
```

4. Create your exercise file:

```txt
session7/solutions/exercise-07-03.py
```

#### 3. Basics you should know

- `NumPy`: a Python library for fast numeric arrays.
- `array`: a collection of values with the same general data type.
- `shape`: the size of an array in each dimension.
- `dtype`: the data type stored in an array.
- `vectorised operation`: an operation applied to many values at once.
- `boolean mask`: a True/False array used to filter values.
- `2D array`: a table-like array with rows and columns.

#### 4. Import NumPy

Most Python code imports NumPy using the alias `np`.

File: `session7/solutions/exercise-07-03.py`

```python
import numpy as np

print(np.__version__)
```

#### 5. Create a NumPy array

Create a simple array from a Python list.

File: `session7/solutions/exercise-07-03.py`

```python
import numpy as np

scores = np.array([72, 85, 91, 64, 78])

print(scores)
print(type(scores))
```

#### 6. Inspect shape and data type

Arrays have a shape and a data type.

File: `session7/solutions/exercise-07-03.py`

```python
import numpy as np

scores = np.array([72, 85, 91, 64, 78])

print(scores.shape)
print(scores.dtype)
```

> [!NOTE]
>
> For a one-dimensional array, the shape shows how many values are in the array.

#### 7. Basic statistics

NumPy can calculate common statistics.

File: `session7/solutions/exercise-07-03.py`

```python
import numpy as np

scores = np.array([72, 85, 91, 64, 78])

print(np.mean(scores))
print(np.min(scores))
print(np.max(scores))
print(np.std(scores))
```

#### 8. Vectorised calculations

With NumPy, you can apply a calculation to the whole array at once.

File: `session7/solutions/exercise-07-03.py`

```python
import numpy as np

scores = np.array([72, 85, 91, 64, 78])
scores_plus_5 = scores + 5

print(scores_plus_5)
```

This is shorter and usually faster than writing a loop.

#### 9. Boolean filtering

Create a True/False mask, then use it to filter values.

File: `session7/solutions/exercise-07-03.py`

```python
import numpy as np

scores = np.array([72, 85, 91, 64, 78])

mask = scores >= 80

print(mask)
print(scores[mask])
```

#### 10. Create arrays with ranges

Use `arange()` to create regular numeric sequences.

File: `session7/solutions/exercise-07-03.py`

```python
import numpy as np

numbers = np.arange(1, 11)

print(numbers)
print(numbers * 2)
```

#### 11. Create a 2D array

A 2D array is useful for matrix-style data.

File: `session7/solutions/exercise-07-03.py`

```python
import numpy as np

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
])

print(matrix)
print(matrix.shape)
```

#### 12. Select rows and columns

Use row and column indexes to select values from a 2D array.

File: `session7/solutions/exercise-07-03.py`

```python
import numpy as np

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
])

print(matrix[0, 0])
print(matrix[0, :])
print(matrix[:, 1])
```

> [!TIP]
>
> `matrix[0, :]` means row 0 and all columns.
>
> `matrix[:, 1]` means all rows and column 1.

#### 13. Use NumPy with pandas data

You can convert a pandas column to a NumPy array.

File: `session7/solutions/exercise-07-03.py`

```python
import numpy as np
import pandas as pd

pokemon = pd.read_csv("datasets/Pokemon.csv", encoding="cp1252")

attack_values = pokemon["Attack"].to_numpy()

print(attack_values[:10])
print(np.mean(attack_values))
```

#### 14. Exercise

Add your answers to:

```txt
session7/solutions/exercise-07-03.py
```

Tasks:

1. Import NumPy as `np`.
2. Create an array called `scores` with at least 8 numeric values.
3. Print the array, shape, and data type.
4. Print the mean, minimum, maximum, and standard deviation.
5. Create a new array called `scores_plus_10`, then filter and print only scores greater than or equal to `80`.
6. Create an array with numbers from `1` to `20`, then print only the even numbers.
7. Create a 3 by 3 matrix, print its shape, print the first row, and print the second column.
8. Load `Pokemon.csv` with pandas, convert the `Attack` column to a NumPy array, print the average attack, print attack values greater than or equal to `120`, and add a short comment explaining one difference between a Python list and a NumPy array.

#### 15. Quiz

Complete the following quiz.

```bash
quizmd quizzes/python-session-07-part-03-quiz.md
```

If you want to choose a theme:

```bash
quizmd --theme light quizzes/python-session-07-part-03-quiz.md
quizmd --theme dark quizzes/python-session-07-part-03-quiz.md
```

You are now ready for the homework or class challenge.
