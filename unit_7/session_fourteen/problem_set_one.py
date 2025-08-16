# Problem 1 - How Many 1s
def is_nested_parens(s):
    if s == '':
        return True
    if len(s) >= 2 and s[0] == '(' and s[-1] == ')':
        return is_nested_parens(s[1:-1])
    return False

print(is_nested_parens("())"))

'''

    Time Complexity: O(n) because each recursive call processes two fewer characters until the string is empty or invalid.
    Space Complexity: O(n) due to the recursion stack depth, potentially extending to the length of the string in deeply nested cases.

'''

# Problem 2 - How Many 1s
def count_ones(lst):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == 0:
            low = mid + 1
        else:
            high = mid - 1
    
    if low < len(lst) and lst[low] == 1:
        return len(lst) - low
    return 0

print(count_ones([0,0,0,0,1,1,1]))

# Problem 3 - Binary Search IV
def binary_search(nums, left, right, target):
    if left > right:
        return -1  

    mid = (left + right) // 2
    
    if nums[mid] == target:
        return mid
    
    if target < nums[mid]:
        return binary_search(nums, left, mid - 1, target)
    else:
        return binary_search(nums, mid + 1, right, target)

def binary_search_recursive(nums, target):
    return binary_search(nums, 0, len(nums) - 1, target)

# Problem 4: Count Rotations
def count_rotations(nums):
    low = 0
    high = len(nums) - 1
    while low <= high:
        if nums[low] <= nums[high]:
            return low
        mid = (low + high) // 2
        next_index = (mid + 1) % len(nums)  
        prev_index = (mid - 1 + len(nums)) % len(nums)  
        
       
        if nums[mid] <= nums[next_index] and nums[mid] <= nums[prev_index]:
            return mid
        elif nums[mid] > nums[high]:
            low = mid + 1  
        else:
            high = mid - 1  

    return 0  