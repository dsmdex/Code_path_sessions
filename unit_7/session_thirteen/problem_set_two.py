# Problem 1 - Counting Down
def countdown_recursive(n) -> None:
    '''Takes in a n int value and prints the number, makes a recursive call until n is 0.'''
    if n > 0:
        print(n)
        countdown_recursive(n-1)

countdown_recursive(5)

def countdown_iterative(n):
    '''Takes in a n int value and prints n, decrements until n is 0.'''
    while n > 0:
        print(n)
        n -= 1

countdown_iterative(5)

# Problem 2 - Fibonacci Case
# The solution is valid but highly inefficient...
def fibonacci(n) -> int:
    '''Takes in a n value and returns the value where n is.'''
    # base cases:
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)

'''
Time: O(2^n), since the recursion tree branches into two calls at each level
Space: O(n), due to the recursion stack depth
'''

test_fib = fibonacci(3)
print(test_fib)

# More efficient solution
# Problem 2 - Fibonacci with Memoization (using a dictionary for reference of existing values.)
def fibonacci(n, memo=None) -> int:
    '''Takes in n and returns the nth Fibonacci number using recursion + memoization.'''
    if memo is None:
        memo = {}

    # base cases
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    # check memo
    if n in memo:
        return memo[n]

    # compute + store in memo
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

'''
Time: O(n), because each Fibonacci number from 0 to n is computed once.
Space: O(n), because of recursion depth (stack) + memo dictionary.
'''

# Example test
print(fibonacci(3))   # 2
print(fibonacci(10))  # 55


# More efficient way
# Problem 2 - Fibonacci Iterative (Bottom-Up)
def fibonacci_iterative(n: int) -> int:
    '''Computes the nth Fibonacci number iteratively in O(n) time and O(1) space.'''
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    prev, curr = 0, 1  # f(0), f(1)
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr

    return curr


# Example test
print(fibonacci_iterative(3))   # 2
print(fibonacci_iterative(10))  # 55


# Problem 3 - Recursive Product
def list_product(lst) -> int:
    '''Returns the result of the given helper function, provides initial values.'''

    def helper(lst: list, left: int, right: int) -> int:
        '''Returns the product of all the elemnts in a given list.'''

        left_pointer = left
        right_pointer = right

        if left_pointer == right_pointer:
            return lst[left_pointer]
        else:
            return lst[left_pointer] * lst[right_pointer] * helper(lst, left_pointer + 1, right_pointer - 1)

    return helper(lst, 0, len(lst)-1)

'''
Time: O(n), since each recursive call processes two elements until the list is exhausted.
Space: O(n), due to recursion depth.
'''


product_test = list_product([1,2,3,4,5])
print(product_test)

# Problem 4 - Recursive power of 4
def is_power_of_four(n) -> bool:
    '''Returns a bool value if n is a power of 4, false otherwise.'''
    if n == 1:
        return True
    if n % 4 != 0 or n <= 0:
        return False
    return is_power_of_four(n // 4)

'''
Time: O(log₄ n) — each step divides n by 4, so roughly log₄(n) steps.
Space: O(log n) — recursion stack has one frame per division.
'''

test_4_power = is_power_of_four(16)
print(test_4_power)

# Problem 5 - Binary Search II
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1  # Base case: target not found within bounds

		# find middle index of list
    mid = (left + right) // 2
    
    # If the middle element is the target, return its index
    if arr[mid] == target:
        return mid
    # If the target is less than the middle element, search the left half
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    # If the target is greater than the middle element, search the right half
    else:
        return binary_search_recursive(arr, target, mid + 1, right)
    
'''
Time: O(log(n)) as we are halving each search
Space: O(log(n)) as the recursion stack depth = number of calls until base case.
'''

def binary_search_iterative(arr, target) -> int:
    left_pointer = 0
    right_pointer = len(arr) - 1

    while left_pointer <= right_pointer:
        middex = (left_pointer + right_pointer) // 2
        
        if arr[middex] == target:
            return middex
        elif arr[middex] < target:
            left_pointer = middex + 1
        else:
            right_pointer = middex - 1
        
    return -1
	
'''
Time: O(log(n)), since each iteration halves the search space
Space: O(1), only a few variables are used, no recursion stack
'''

# Problem 6 - Find Ceiling
def find_ceiling(lst, x) -> int:
    '''Returns the result of the helper function, sets the intial values for it.'''
    
    def helper(lst: list, x: int, left: int, right: int, candidate = -1) -> int:
        '''Returns the index where the smallest value in the lst is larger or equal to x. -1 if otherwise.'''

        if left > right:
            return candidate
        
        middex = (left + right) // 2
        
        if lst[middex] >= x:
            return helper(lst, x, left, middex - 1, middex)
        else:
            return helper(lst, x, middex + 1, right, candidate)

    return helper(lst, x, 0, len(lst) - 1, -1)

'''
Time: O(log(n)) as our search is halving with each time.
Space: O(log(n)) as our stack is proportional to our search.
'''

# Problem 7 - Ternary Search
def ternary_search(lst, target, left, right) -> int:
    '''Returns the index of the target if found, -1 otherwise.'''
    
    if left > right:
        return -1  # Base case: not found
    
    # Find two midpoints
    third = (right - left) // 3
    mid1 = left + third
    mid2 = right - third

    # Check both midpoints
    if lst[mid1] == target:
        return mid1
    if lst[mid2] == target:
        return mid2

    # If target is in the left third
    if target < lst[mid1]:
        return ternary_search(lst, target, left, mid1 - 1)
    # If target is in the right third
    elif target > lst[mid2]:
        return ternary_search(lst, target, mid2 + 1, right)
    # Otherwise, it must be in the middle third
    else:
        return ternary_search(lst, target, mid1 + 1, mid2 - 1)


'''
Time: O(log₃ n), because the list is divided into 3 parts each time.
Space: O(log n), due to recursion stack depth.
'''

# Example test
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(ternary_search(arr, 5, 0, len(arr)-1))  # 4
print(ternary_search(arr, 10, 0, len(arr)-1)) # -1
