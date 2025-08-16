# Problem 1 - Counting Down
def countdown(n):
    if n > 0:
        print(n)
        countdown(n-1)

countdown(5)

def countdown_iterative(n):
    i = n
    
    while i > 0:
        print(i)
        i -= 1

countdown_iterative(5)


# Problem 2 - Fibonacci Case
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))


# Problem 3 - Recursive Product

def list_product(lst):
    if not lst:
        return 1
    return lst[0] * list_product(lst[1:])

print(list_product([1,2,3,4,5]))

# Problem 4 - Recursive power of 4
def is_power_of_four(n):
    if n == 1:
        return True
    if n <= 0:
        return False
    if n%4 != 0:
        return False
    return is_power_of_four(n//4)

print(is_power_of_four(256))
    

# Problem 5 - Binary Search II

'''
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

def binary_search(lst, target):
    left = 0
    right = len(lst) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return True
        elif lst[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return False
    
print(binary_search([1, 3, 5, 7, 9, 11, 13, 15], target = 11))

'''

    Time Complexity: O(log n) because each iteration approximately halves the number of elements to be searched.
    Space Complexity: O(1) because the iterative approach does not use additional space proportional to the input size.

'''

# Problem 6 - Find Ceiling
def find_ceiling(lst, x):
    low = 0
    high = len(lst) - 1
    result = -1  
    
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] < x:
            low = mid + 1
        else:
            result = mid  
            high = mid - 1 
    
    return result

"""

    Time Complexity: O(log n) because the algorithm still utilizes a binary search approach, which divides the search space in half each iteration.
    Space Complexity: O(1) as the solution does not require extra space beyond a few counter variables.

"""

# Problem 7 - Ternary Search

def ternary_search(lst, target):
    low, high = 0, len(lst) - 1
    
    while low <= high:
        
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3
        
       
        if lst[mid1] == target:
            return mid1  
        if lst[mid2] == target:
            return mid2  
        
        
        if target < lst[mid1]:
            high = mid1 - 1  
        elif target > lst[mid2]:
            low = mid2 + 1  
        else:
            low = mid1 + 1  
            high = mid2 - 1
    
    return -1  

'''

    Time Complexity: O(log_3 n) (base 3), because it divides the search space into thirds each time.
    Space Complexity: O(1), because the solution only uses a few variables to store the indices and comparison results, regardless of the size of the input array.

'''
