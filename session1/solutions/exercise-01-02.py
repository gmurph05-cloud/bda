from exercise_01_02_lib import my_len
from exercise_01_02_lib import add_elements
from exercise_01_02_lib import find_position
from exercise_01_02_lib import count_conditionally
from exercise_01_02_lib import sum_all_even
from exercise_01_02_lib import return_position
from exercise_01_02_lib import find_target_coord

data = [10, 20, 30, 40, 50]

""" count = 0
for item in data:
    count += 1 """

#### 4. Example 1: Count elements
# +==========+==========+==========+==========+==========+
print(my_len(data=data))


#### 5. Example 2: Sum elements
# +==========+==========+==========+==========+==========+
total = 0
total = add_elements(data, total=total)

print("\n#### 5. Example 2: Sum elements: \n", total)

#### 6. Example 3: Find position of a target value
# +==========+==========+==========+==========+==========+
print("\n#### 6. Example 3: Find position of a target value")
target = 30
print("\nPosition number: ", find_position(data, target=target))

#Another common way to work with positions is:
for i in range(len(data)):
    print(i)

#### 7. Example 4: Traverse a matrix with nested loops
# +==========+==========+==========+==========+==========+
print("\n#### 7. Example 4: Traverse a matrix with nested loops\n")
matrix = [
    [10, 20],
    [30, 40]
]

for row in matrix:
    print(row)
    for value in row:
        print(value)

row_index = 0
col_index = 0

for row in matrix:
    print("row:", row_index)
    for value in row:
        print("col:", col_index, "value:", value)
        col_index += 1
    # Reset col_index for each new row.
    col_index = 0
    row_index += 1

#### 9. Exercise
# +==========+==========+==========+==========+==========+
'''
Tasks:

# 1. Write a function to count elements between `1` and `10` (inclusive) in `data = [30, 6, 9, 12, 15, 8]`.
# 2. Write a function to sum all even numbers in the same list.
# 3. Write a function that returns the position of the first value equal to `12` in the same list. If the value is not found, return `-1`.
# 4. For the matrix below, print the position of `25` as coordinates [2, 2] in the matrix (row, column), using 1-based indexing.
   
'''

# 1. Write a function to count elements between `1` and `10` (inclusive) in `data = [30, 6, 9, 12, 15, 8]`.
print("\n# 1. Write a function to count elements between `1` and `10` (inclusive) in `data = [30, 6, 9, 12, 15, 8]`.")
data = [30, 6, 9, 12, 15, 8]
print("\nCount: ", count_conditionally(data=data,min_val=1,max_val=10))

# 2. Write a function to sum all even numbers in the same list.
print("\n# 2. Write a function to sum all even numbers in the same list.")
print("\nSum of even numbers: ", sum_all_even(data=data) )


# 3. Write a function that returns the position of the first value equal to `12` in the same list. If the value is not found, return `-1`.
print("\n# 3. Write a function that returns the position of the first value equal to `12` in the same list. If the value is not found, return `-1`.")
data = [30, 6, 9, 12, 15, 8]
target = 12
print("\nPosition of 12: ", return_position(data=data,target=target))


# 4. For the matrix below, print the position of `25` as coordinates [2, 2] in the matrix (row, column), using 1-based indexing.
print("\n# 4. For the matrix below, print the position of `25` as coordinates [2, 2] in the matrix (row, column), using 1-based indexing.")
matrix = [
    [5, 10, 15],
    [20, 25, 30],
    [50, 75, 100],
]

target = 75
print("\nTarget = 75: ", find_target_coord(matrix=matrix, target=target))


