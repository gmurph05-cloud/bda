#### 4. Iterables and iterators
# An **iterator** remembers its current position, making it ideal when we want to move through a sequence index by index.

numbers = [1, 2, 3]

""" for number in numbers:
    print(number) """

numbers = [1, 2, 3]
it = iter(numbers)

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3

'''
After the last value, `next(it)` raises `StopIteration`. A `for` loop handles this automatically.
'''

