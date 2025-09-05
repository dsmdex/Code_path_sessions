# Problem Set Three

# Problem 1: In the Stars
def insert_stars_recursive(s: str) -> print:
    '''Takes in a str (s) and prints the string with asterisks between each character.'''
    if len(s) <= 1:
        return s
    else:
        return s[0] + '*' + insert_stars_recursive(s[1:])
    
print(insert_stars_recursive('abc'))

def insert_start_iterative(s: str) -> print:
    '''Takes in a str (s) and prints the string with asterisks in between each character.'''
    if len(s) <= 1:
        return s
    else:
        read_pointer = 0
        while read_pointer <= len(s) - 1:
            print(s[read_pointer], end="*" if read_pointer < len(s) - 1 else "\n")
            read_pointer += 1

'''
Time: O(n) worst case involves iterating the entire string
Space: O(1) no new variables are created in memory
'''

insert_start_iterative('abc')


# Problem 2: String Length Case
def string_length(s: str, i: int) -> int:
    '''Returns the string length of a given string (s)'''
    if not s:
        return 0
    elif i == len(s) - 1:
        return 1
    else:
        return 1 + string_length(s, i+1)
    
'''
Time: O(n), since we make n recursive calls, each doing O(1) work.
Space: O(n), due to the recursion call stack.
'''

print(string_length('hello', 0))


# Problem 3: Recursive Digits Sum
def sum_digits(n: int) -> int:
    '''Calculates and returns the sum of the digits of n.'''
    if n == 0:
        return 0
    else:
        last_digit = n % 10
        remaining_number = n // 10
        return last_digit + sum_digits(remaining_number)
    
'''
Time: O(log(n)), since the number of recursive calls equals the number of digits in n.
Space: O(log(n)), due to the recursion call stack.
'''

    
print(sum_digits(444))


# Problem 4: Recursive Count 7s
def count_sevens(n: int) -> int:
    '''Returns the count of 7s that exist in n.'''
    if n <= 0:
        return 0
    else:
        last_digit = n % 10
        leftover_digits = n // 10
        return (1 if last_digit == 7 else 0) + count_sevens(leftover_digits)

'''
Time: O(log(n)), because the number of recursive calls equals the number of digits in n.
Each step removes one digit (n // 10), so the recursion depth is proportional to the number of digits.
Space: O(log(n)), for the recursion stack, since each digit requires one frame.
'''

print(count_sevens(727))

# Problem 5: Binary Search III
def binary_search_recursive(lst: list, target: int, left: int, right: int) -> bool:
    """
    Returns True if target is found in lst, False otherwise.
    Recursive implementation.
    """
    # Base case: search space is empty
    if left > right:
        return False

    # Find middle index
    mid = (left + right) // 2

    # Check if middle element is the target
    if lst[mid] == target:
        return True
    # If target is smaller, search the left half
    elif lst[mid] > target:
        return binary_search_recursive(lst, target, left, mid - 1)
    # If target is larger, search the right half
    else:
        return binary_search_recursive(lst, target, mid + 1, right)
    
'''
Time: O(log(n)), because each recursive call halves the search space.
Space: O(log(n)), due to the recursion stack depth.
'''

print(binary_search_recursive([1, 3, 5, 7, 9, 11, 13, 15], 11, 0, 7))


def binary_search_iterative(lst: list, target: int) -> bool:
    """
    Returns True if target is found in lst, False otherwise.
    Iterative implementation.
    """
    left = 0
    right = len(lst) - 1

    while left <= right:
        # Recalculate middle each iteration
        mid = (left + right) // 2

        if lst[mid] == target:
            return True
        elif lst[mid] < target:
            # Move left pointer to the right half
            left = mid + 1
        else:
            # Move right pointer to the left half
            right = mid - 1

    # Target not found
    return False

'''
Time: O(log(n)), since each iteration halves the search space.
Space: O(1), only a few variables are used, no recursion stack.
'''


# Example usage
print(binary_search_iterative([1, 3, 5, 7, 9, 11, 13, 15], 11))


# Problem 6: Find Missing
def find_missing(nums: list) -> int:
    """
    Given a sorted list of distinct integers in the range [0, n], return the missing number
    """
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        # If value matches its index, missing number is on the right
        if nums[mid] == mid:
            left = mid + 1
        # Otherwise, missing number is on the left (or at mid)
        else:
            right = mid - 1

    # After loop, 'left' points to the missing number
    return left

'''
Time: O(log n) — each iteration halves the search space.
Space: O(1) — only a few variables (left, right, mid) are used.
'''


# Example usage
print(find_missing([0, 1, 2, 4, 5, 6]))  # Output: 3
print(find_missing([0, 1, 3, 4, 5]))     # Output: 2
print(find_missing([1, 2, 3]))           # Output: 0
print(find_missing([0, 1, 2, 3]))        # Output: 4


# Problem 7: Square Root
def integer_sqrt(x: int) -> int:
    """
    Returns the integer square root (floor) of x.
    If x is a perfect square, returns sqrt(x). Otherwise, returns the floor.
    """
    if x < 2:
        return x  # sqrt(0)=0, sqrt(1)=1

    left = 1
    right = x // 2
    result = 0  # stores the largest integer whose square <= x

    while left <= right:
        mid = (left + right) // 2
        square = mid * mid

        if square == x:
            return mid  # perfect square found
        elif square < x:
            result = mid  # mid could be the floor of sqrt(x)
            left = mid + 1  # search higher
        else:
            right = mid - 1  # search lower

    return result  # floor of sqrt(x)


# Example usage
print(integer_sqrt(0))   # 0
print(integer_sqrt(1))   # 1
print(integer_sqrt(8))   # 2
print(integer_sqrt(16))  # 4
print(integer_sqrt(20))  # 4


'''
Time: O(log x), because we halve the search space each step.
Space: O(1), only a few variables are used.
'''