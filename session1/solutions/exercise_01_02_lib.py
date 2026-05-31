#### 4. Example 1: Count elements
def my_len(data):
    count = 0
    for item in data:
        count += 1
    return count

def add_elements(data, total):
    for item in data:
        total += item

    return total

def find_position(data, target):
    pointer = 0
    for item in data:
        if item == target:
            break
        else:
            pointer += 1
    return pointer

#### 9. Exercise
# 1. Write a function to count elements between `1` and `10` (inclusive) in `data = [30, 6, 9, 12, 15, 8]`.
def count_conditionally(data, min_val,max_val):
    count = 0
    num_filtered = []
    for num in data:
        if num >= min_val and num <= max_val:
            num_filtered.append(num)
            count += 1
    print("\nNumbers: ", num_filtered)
    return count

# 2. Write a function to sum all even numbers in the same list.
def sum_all_even(data):
    total = 0
    numbers = []
    for num in data:
        if num % 2 == 0:
            numbers.append(num)
            total += num
    print("\nNumbers: ",numbers)
    return total

# 3. Write a function that returns the position of the first value equal to `12` in the same list. If the value is not found, return `-1`.
def return_position(data, target):
    position = 0
    for num in data:
        if num==target:
            return position
        else:
            position += 1
    return "Number not found"

def find_target_coord(matrix, target):
    for row_idx, row in enumerate(matrix, start=1):
        for col_i, value in enumerate(row, start=1):
            if value == target:
                return [row_idx, col_i]
    return "Target not found."
    




