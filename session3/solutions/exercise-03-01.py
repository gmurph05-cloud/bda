#### 5. Files are iterators too
# +==========+==========+==========+==========+==========+
# 
print("\n#### 5. Files are iterators too")
with open("data/les_miserables.txt", "r", encoding="utf-8") as file:
    it = iter(file)
    print(next(it))
    print(next(it))
'''
# > Time: O(m) per line, where `m` is the length of the line being read.
# > Space: O(m), because only one line is held at a time.
'''

#### 6. Exercise: print the first record
# +==========+==========+==========+==========+==========+
print('''\n
Task:

1. Open `les_miserables.txt`.
2. Print only the first line.
3. Do not use `readlines()`.
''')

TEXT_FILE = "data/les_miserables.txt"

with open(TEXT_FILE, "r", encoding="utf-8") as file:
     first = next(file)
     print(first)

'''
# > Time: O(m), where `m` is the length of the first line of data.
# > Space: O(m).
'''
# > If the file is empty, `next(file)` will raise `StopIteration`. For a safer version:
TEXT_FILE = "data/les_miserables.txt"

with open(TEXT_FILE, "r", encoding="utf-8") as file:
    first = next(file, "")
    print(first)


#### 7. Exercise: find the first line containing text
# +==========+==========+==========+==========+==========+
# Find the first line containing `target = "Jean Valjean"`.
print('''\n# Find the first line containing `target = "Jean Valjean"`.\n''')

TEXT_FILE = "data/les_miserables.txt"
target = "Jean Valjean"
found = None

with open(TEXT_FILE, "r", encoding="utf-8") as file:
    for line in file:
        # Provide here your solution
        if target in line:
            found = line
            break

print(found)
# Best case time: O(m), if the match is near the start.
# Worst case time: O(n * m), if Python must check all `n` lines.
# Space: O(m), because only one line is processed at a time.


#### 8. Exercise: count all lines
# +==========+==========+==========+==========+==========+
# Count how many lines are in the file.
print("\n# Count how many lines are in the file.\n")

TEXT_FILE = "data/les_miserables.txt"
count = 0

with open(TEXT_FILE, "r", encoding="utf-8") as file:
    for line in file:
        # Provide here your solution
        count += 1
print(count)
# note: counter is efficient because only one line needs to be read at a time.
# Time: O(n), where `n` is number of lines.
# Space: O(1) extra space, ignoring the current line buffer.



# #### 9. Exercise: average line length 
# +==========+==========+==========+==========+==========+
# Compute the average line length.
print('''\n 
# #### 9. Exercise: average line length 
# +==========+==========+==========+==========+==========+
# Compute the average line length.
''')
TEXT_FILE = "data/les_miserables.txt"
total_length = 0
count = 0
line_length_min = 1000
line_length_max = 0

with open(TEXT_FILE, "r", encoding="utf-8") as file:
    for line in file:
        # Provide here your solution
        total_length += len(line)
        count += 1
        if len(line) > line_length_max:
            line_length_max = len(line)
        if len(line) < line_length_min:
            line_length_min = len(line)

average = total_length / count
print(f"{average} characters per line")
print(f"{line_length_min} characters for shortest line")
print(f"{line_length_max} characters for longest line")
# Do we need to store all lines?
# No. We only need a running total and a counter.
# Time: O(n), if we treat `len(line)` as constant per line for this discussion.
# More precisely: O(total characters).
# Space: O(1) extra space.


#### 10. When do we need to load all data?
# +==========+==========+==========+==========+==========+
print(
'''\n
#### 10. When do we need to load all data?

Sometimes streaming is not enough.

Use loading all data when you need:

- indexing, such as `lines[100]`
- sorting all lines
- repeated passes over the same data
- comparing each line with many other lines
- sending a selected batch of lines to another function
''')
TEXT_FILE = "data/les_miserables.txt"

with open(TEXT_FILE, "r", encoding="utf-8") as file:
    lines = file.readlines()

print(lines[100])
# Time: O(n), or more precisely O(total characters).
# Space: O(n * m), because all lines are stored.
'''
1. Reading the File: file.readlines()
Complexity: O(N)
Why: The readlines() method forces Python to read the entire file from disk into memory all at once. To do this, the engine must scan every single character in the file sequentially to parse line breaks (\n) and allocate memory for each string element in the resulting list. Therefore, the time scales linearly with the size of the file.

2. Accessing a Specific Line: lines[100]
Complexity: O(1) (Constant time)
Why: Python lists are implemented as contiguous arrays of memory references underneath the hood. When you look up an element by index (like lines[100]), Python calculates the memory address mathematically in a single operation. It does not matter if you look up index 0, 100, or 10000—the lookup time remains the same.

Summary of the Code's Resource Profile
Because the file read operation (O(N)) and the index lookup (O(1)) happen sequentially, we add their complexities together (O(N) + O(1)). The dominant term takes over, leading to the final rating.
Total Time Complexity: O(N) — Dominated entirely by reading the file into memory.
Total Space Complexity: O(N) — Because readlines() holds every single line simultaneously in a list inside your RAM. If the file is 500 MB, your script will immediately consume at least 500 MB of memory (often more due to Python string object overhead).
'''

#### 11. Generators with `yield`
# +==========+==========+==========+==========+==========+
# A generator is a function that produces values one at a time.
print('''\n
#### 11. Generators with `yield`
# +==========+==========+==========+==========+==========+
# A generator is a function that produces values one at a time.\n
''')
# `yield` is different from `return`:
# - `return` gives back one final value and stops the function.
# - `yield` gives back one value, pauses, and continues later.
# > A generator is useful when the dataset is large and you only need one item at a time.
def non_empty_lines(path):
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line != "":
                yield line

for line in non_empty_lines("data/les_miserables.txt"):
    print(line)
    break


#### 12. Exercise: Count non-empty lines containing a word
# +==========+==========+==========+==========+==========+
#Write a program that counts how many non-empty lines contain the word `"Jean"` using `yield`.
print('''\n
Write a program that counts how many non-empty lines contain the word `"Jean"` using `yield`.\n''')
TEXT_FILE = "data/les_miserables.txt"
target = "Jean"

def non_empty_lines(path, target):
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line != "" and target in line:
                yield line

count = 0

for line in non_empty_lines(TEXT_FILE, target=target):
    count += 1

print(f"\n {count}")
# Time: O(n * m), where `n` is the number of lines and `m` is the average line length.
# Space: O(m), because one stripped line is processed at a time.



#### 13. Practice: streaming or loading
# +==========+==========+==========+==========+==========+
