# Problem 1: Neatly Nested
def is_nested(paren_s) -> bool:
    '''Returns bool value of len condition or the bool value of the helper function.'''
    if len(paren_s) % 2 != 0:
        return False
    
    def helper(paren_s, left, right):
        '''Takes in a string and returns a bool deremining if the string contains 
        a valid pairing of () or none, false if mixed an no pair.'''
        if  left > right:
            return True
        if paren_s[left] == "(" and paren_s[right] == ")":
            return helper(paren_s, left + 1, right - 1)
        else:
            return False
        
    return helper(paren_s, 0, len(paren_s) - 1)

'''
Time: n/2 -> which reduces to n, so O(n)
Space: O(n) for each recursive call added to the stack.
'''

print(is_nested(''))


# Problem 2: How many 1s
def count_ones(lst: list) -> int:
    '''Returns the count of how many 1s exist in a sorted array of 0s and 1s.'''

    def helper(left, right):
        if left > right:
            # index of first 1
            return left
        mid = (left + right) // 2
        if lst[mid] == 1:
            return helper(left, mid - 1)  
        else:
            return helper(mid + 1, right) 

    first_one_index = helper(0, len(lst) - 1)
    return len(lst) - first_one_index

'''
Time: O(log(n)) as we are splitting our search in each recursive call
Space: O(log(n)) for the frames that are added to the stack, proportional to each instance a call is made.
'''

print(count_ones([0, 0, 0, 0, 1, 1, 1]))  
print(count_ones([0, 0, 0, 0]))         
print(count_ones([1, 1, 1, 1]))         
print(count_ones([]))             


# Problem 3: Binary Search IV
def binary_search(nums: list, target: int) -> int:
    