# Problem 1 - Hello Hello
def repeat_hello_iterative(n: int) -> print:
    i = 0

    while i < n:
        print("Hello")
        i += 1
    
    print()

repeat_hello_iterative(5)

def repeat_hello_recursive(n) -> print:
    if n == 0:
        return
    else:
        print("Hello")
        repeat_hello_recursive(n-1)

repeat_hello_recursive(5)

# Problem 2 - Facotorial Case
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

# Problem 3 - Recursive Sum
def sum_list(lst: list):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])

'''
Time: O(n^2) (because of recursive call and slicing at every step).
Space: O(n^2) (stack + new list copies).
'''

test_list = [1,2,3,4,5]
print(sum_list(test_list))

# Problem 4 - Recursive Power of 2
def is_power_of_two(n):
    '''Returns True if n is a solution '''
    if n == 1:
        return True
    if n % 2 != 0 or n<=0:
        return False
    return is_power_of_two(n // 2)

'''
Time: O(log(n)), since n is divided by 2 in each recursive call.
Space: O(log(n)), because the recursion depth is proportional to log₂(n).
'''


# Problem 5 - Binary Search I
def linear_search(lst: list, target: type) -> object:
    '''If target is found, return the index, -1 otherwise'''
    index = 0

    for i in lst:
        if i == target:
            return index
        index += 1
    return -1

'''
Time: O(n), must traverse the entire list in the worst case scenario
Space: O(1), only variable initialized and incremented is index variable
'''

lst = [1, 3, 5, 7, 9, 11, 13, 15]
target = 11

print(linear_search(lst, target))

def binary_search_iterative(lst: list, target: int) -> int:
    '''Returns the index is the target is found, -1 otherwise.'''
    left_end = 0
    right_end = len(lst) - 1
    mid_point = (left_end + right_end) // 2

    while left_end <= right_end:
        if lst[mid_point] == target:
            return mid_point
        elif lst[mid_point] < target:
            left_end = mid_point + 1
            mid_point = (left_end + right_end) // 2
        elif lst[mid_point] > target:
            right_end = mid_point - 1
            mid_point = (left_end + right_end) // 2
    return -1

'''
Time: O(log(n)), as we check for the value at mid_point of lst, each new case reduces the lst by half.
Space: O(1), only the pointers are updated, no new data structures created.
'''

lst = [1, 3, 5, 7, 9, 11, 13, 15]
target = 11


def find_last(lst: list, target: int) -> int:
    """Returns the index of the last occurrence of target in lst, or -1 if not found."""

    def helper(left: int, right: int) -> int:
        if left > right:
            return -1

        mid = (left + right) // 2

        if lst[mid] == target:
            # check if this is the last occurrence
            if mid == len(lst) - 1 or lst[mid + 1] > target:
                return mid
            else:
                # search right half
                return helper(mid + 1, right)
        elif lst[mid] < target:
            return helper(mid + 1, right)
        else:  # lst[mid] > target
            return helper(left, mid - 1)

    return helper(0, len(lst) - 1)

'''
Time: O(log(n)), each recursion call halves the list
Space: O(log(n)), due to recursion stack
'''


# Problem 7 - Find Floor
def find_floor(lst: list, x: int) -> int:
    """
    Returns the index of the floor of x in lst.
    The floor is the largest element <= x.
    Returns -1 if no floor exists.
    """

    def helper(left: int, right: int, candidate: int = -1) -> int:
        if left > right:
            return candidate  # return the best candidate found so far

        mid = (left + right) // 2

        if lst[mid] <= x:
            # this mid could be the floor, but maybe there's a larger one on the right
            return helper(mid + 1, right, mid)
        else:
            # mid is too big, search left half
            return helper(left, mid - 1, candidate)

    return helper(0, len(lst) - 1)

'''
Time: O(log n), because each recursive call halves the search space.
Space: O(log n), due to recursion stack.
'''

lst = [1, 2, 8, 10, 11, 12, 19]
x = 5

