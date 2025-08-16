# Problem 1 - Hello Hello
def repeat_hello(n):
    '''recursive approach'''
    if n > 0:
        print("Hello")
        repeat_hello(n-1)

repeat_hello(5)

def repeat_hello_iterative(n):
    '''iterative approach'''
    i = n
    while i > 0:
        print("Hello")
        i -= 1

repeat_hello_iterative(5)


# Problem 2 - Facotorial Case
def factorial(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(-1))


# Problem 3 - Recursive Sum
def sum_list(lst: list):
    if not lst:
        return 0 
    return lst[0] + sum_list(lst[1:])

print(sum_list([1,2,3,4,5]))


# Problem 4 - Recursive Power of 2
def is_power_of_two(n):
    if n == 1:
        return True
    if n <= 0:
        return False
    if n % 2 != 0:
        return False
    return is_power_of_two(n//2)

print(is_power_of_two(8))

'''
Time Complexity
O(log n) — Each recursive call divides n by 2, so the number of calls is proportional to log₂(n).

Space Complexity
O(log n) — The recursion depth is log₂(n) because each call is stored on the call stack.
'''

# Problem 5 - Binary Search I

def binary_search(lst: list, target: type):
    left_pointer = 0
    right_pointer = len(lst) - 1

    while left_pointer <= right_pointer:
        middle_index = (left_pointer + right_pointer) // 2
        
        if lst[middle_index] == target:
            return middle_index
        elif lst[middle_index] < target:
            left_pointer = middle_index + 1
        else:
            right_pointer = middle_index - 1

    return -1


print(binary_search([1, 3, 5, 7, 9], 7))
print(binary_search([1, 3, 5, 7, 9], 4))

'''
Time Complexity
Each iteration cuts the search range in half.

If the list has n elements, the number of iterations is proportional to: log2𝑛
Worst case: O(log n)
Best case: O(1) (if the target is found in the first check)

Space Complexity
We only store a few variables (left_pointer, right_pointer, middle_index), regardless of n.

No recursion → no call stack growth.

Space: O(1) (constant space)
'''


# Problem 6 - Backwards Binary Search

def find_last(lst, target):
    left = 0
    right = len(lst) - 1
    occurrence = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if lst[mid] == target:
            occurrence = mid
            left = mid + 1  
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return occurrence

print(find_last([1,2,3,3,3,4,5], 3))

'''
Time: logn
Space: constant
'''


# Problem 7 - Find Floor

def find_floor(arr, x):
    low = 0
    high = len(arr) - 1
    floor_value = None  
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] <= x:
            floor_value = arr[mid]  
            low = mid + 1 
        else:
            high = mid - 1  
    
    return floor_value

'''
    Time Complexity: O(log n) because the algorithm still utilizes a binary search approach, which divides the search space in half each iteration.
    Space Complexity: O(1) as the solution does not require extra space proportional to the input size.
'''