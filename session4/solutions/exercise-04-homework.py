#### 3. What to do
'''
1. Start watching the video.
2. When the interviewer gives the coding problem and before the engineers complete the solution, pause the video.
3. Try to solve the problem yourself in Python.
4. Take notes while you work:
   - What did you understand the problem to be?
   - What examples or edge cases did you test mentally?
   - What was your first idea?
   - Did you improve or change your approach?
   - What is the time and space complexity of your solution?
5. Resume the video and watch how the engineers solve it.
6. Compare your solution with theirs.
7. Write a short reflection on what you would do differently in an interview next time.
'''


'''
Scenario A: The Input Array is Sorted (Two-Pointer Approach)
If the array is already sorted, we can use a two-pointer technique to find the pair in linear time without extra space.
'''

def has_pair_with_sum_sorted(data, target_sum):
    """
    Determines if a sorted list contains a pair of elements that equal a target sum.

    This function uses a two-pointer approach, starting at both ends of the list and moving inward. It relies on the input being sorted to determine which pointer to shift.

    Args:
        data: A list of integers sorted in ascending order.
        target_sum: The integer value that the pair of numbers must add up to.

    Returns:
        True if there are two distinct indices i and j such that 
        data[i] + data[j] == target_sum, False otherwise.

    Complexity:
        Time Complexity: O(N) because it scans the array at most once.
        Space Complexity: O(1) auxiliary space as it only uses pointers.

    Examples:
        >>> has_pair_with_sum_sorted([1, 2, 3, 9], 8)
        False
        >>> has_pair_with_sum_sorted([1, 2, 4, 4], 8)
        True
        >>> has_pair_with_sum_sorted([], 8)
        False
    """
    if not data:
        return False
        
    low = 0
    high = len(data) - 1
    
    while low < high:
        current_sum = data[low] + data[high]
        
        if current_sum == target_sum:
            return True
        elif current_sum > target_sum:
            high -= 1  # Sum is too large; move the upper bound down
        else:
            low += 1   # Sum is too small; move the lower bound up
            
    return False

'''
Scenario B: The Input Array is Unsorted (Hash Set Approach)
When the array is unsorted, we track the complements (or previously seen numbers) using a look-up table to maintain linear efficiency.
'''

def has_pair_with_sum_unsorted(data, target_sum):
    """
    Determines if an unsorted list contains a pair of elements that equal a target sum.

    This function utilizes a hash set lookup table to store the mathematical complements needed to reach the target sum, allowing it to find a valid pair in a single linear pass without requiring a pre-sorted array.

    Args:
        data: A list of integers (can be unsorted, positive, or negative).
        target_sum: The integer value that the pair of numbers must add up to.

    Returns:
        True if there are two distinct indices i and j such that 
        data[i] + data[j] == target_sum, False otherwise.

    Complexity:
        Time Complexity: O(N) average time due to O(1) hash set operations.
        Space Complexity: O(N) worst-case space to store elements in the hash set.

    Examples:
        >>> has_pair_with_sum_unsorted([3, 5, 1, 4], 8)
        True
        >>> has_pair_with_sum_unsorted([9, 1, 2, 3], 8)
        False
        >>> has_pair_with_sum_unsorted([4], 8)
        False
    """
    seen_elements = set()
    
    for value in data:
        # Check if the needed match (complement) has already been seen
        complement = target_sum - value
        if value in seen_elements:
            return True
        # Store the complement (or current value) for future lookups
        seen_elements.add(complement)
        
    return False

def main():
    # --- Test Cases from the Video ---
    # Case 1: Expected to be False (No pair adds up to 8)
    list_no_pair = [1, 2, 3, 9]
    
    # Case 2: Expected to be True (4 + 4 = 8)
    list_with_pair = [1, 2, 4, 4]
    
    # Edge Case: Expected to be False (Cannot reuse the same index/element)
    list_single_four = [1, 2, 3, 4]
    
    target = 8

    print("TESTING SCENARIO A: SORTED ARRAY")
    print("==================================================")
    
    result_sorted_1 = has_pair_with_sum_sorted(list_no_pair, target)
    print(f"Input: {list_no_pair}, Target: {target}")
    print(f"Result: {result_sorted_1} (Expected: False)\n")
    
    result_sorted_2 = has_pair_with_sum_sorted(list_with_pair, target)
    print(f"Input: {list_with_pair}, Target: {target}")
    print(f"Result: {result_sorted_2} (Expected: True)\n")

    print("TESTING SCENARIO B: UNSORTED ARRAY")
    print("==================================================")
    
    # We scramble the original video arrays to demonstrate the unsorted logic
    unsorted_no_pair = [9, 2, 1, 3]
    unsorted_with_pair = [4, 2, 1, 4]
    
    result_unsorted_1 = has_pair_with_sum_unsorted(unsorted_no_pair, target)
    print(f"Input: {unsorted_no_pair}, Target: {target}")
    print(f"Result: {result_unsorted_1} (Expected: False)\n")
    
    result_unsorted_2 = has_pair_with_sum_unsorted(unsorted_with_pair, target)
    print(f"Input: {unsorted_with_pair}, Target: {target}")
    print(f"Result: {result_unsorted_2} (Expected: True)\n")
    
    
    print("TESTING EDGE CASE: SINGLE APPERANCE OF HALF-SUM ")
    print("==================================================")
    
    result_edge = has_pair_with_sum_unsorted(list_single_four, target)
    print(f"Input: {list_single_four}, Target: {target}")
    print(f"Result: {result_edge} (Expected: False)")

if __name__ == "__main__":

    main()


# 4. Take notes while you work:
'''
   - What did you understand the problem to be?
   >>> The goal is to determine whether a given collection of integers contains at least one pair of distinct elements (meaning you cannot reuse the element at the exact same index twice) that add up exactly to a given target sum. The function should return a boolean (True or False)
   - What examples or edge cases did you test mentally?
   >>> No Matching Pair: [1, 2, 3, 9] with a target sum of 8 (Should return False)
   >>> Matching Pair: [1, 2, 4, 4] with a target sum of 8 (Should return True using the two separate 4s)
   >>> Single/Empty Elements: An empty list [] or a list with a single element [8]. The loop boundary conditions (low < high or an empty iteration) ensure these safely return False without causing index errors
   >>> Negatives/Positives: Assumed integers can be negative, meaning a sum could decrease or increase dynamically
   - What was your first idea?
   >>> using nested loops to compare every single possible pair against each other
   - Did you improve or change your approach?
   - What is the time and space complexity of your solution?
   >>> Sorted Version: 
   >>> Time Complexity: O(N) because it scans the array sequentially at most once
   >>> Space Complexity: O(1) auxiliary space as it only uses pointers
   >>> Unsorted Version:
   >>> Time Complexity: O(N) because hash set insertion and lookup operations average O(1) constant time 
   >>> Space Complexity: O(N) because in the worst-case scenario, you might store all elements in the hash set before finding a match or finishing the loop
'''

# 7. Write a short reflection on what you would do differently in an interview next time.
'''
# Ask Proactive Clarifying Questions Early: 
# Before writing a single line of code, explicitly ask about properties of the data (e.g., Is it sorted? Are there negative numbers or floating points? How should empty inputs or non-existent pairs be treated?)

# Think Out Loud Constantly: 
# Verbalize the thought process—including the flaws of a brute-force approach. Saying "This is an O(N^2) approach which isn't efficient, let's see how we can optimize it" allows the interviewer to see my analytical progression and offer course-correcting hints if I stall.

# Trace Code with Test Cases Manually: 
# Once the code is written, do not just say "I'm done." Instead, construct a dry-run matrix or trace example blocks step-by-step through the loops to verify index behaviours, variable updates, and edge cases. This demonstrates the need for quality assurance and testing code as you progress.

'''