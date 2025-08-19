# Problem 1: Prime Number
def is_prime(n: int) -> bool:
    """Takes in an integer n and returns True if the number is a prime number, false otherwise."""
    
    divisor = n
    count = 0
    while divisor > 1:
        if n % divisor == 0:
            count += 1
        if count > 1:
            return False
        divisor -= 1
    return True

print(is_prime(5))
print(is_prime(12))
print(is_prime(9))

'''
Time Complexity: O(n) — checks all divisors from n down to 2.
Space Complexity: O(1) — only a few integer variables are used.
'''


# Problem 2: Two-Pointer Reverse List
def reverse_list(lst: list) -> list:
    """Reverse a list without slicing but with two-pointer technique"""
    pointer_one, pointer_two = 0, len(lst) - 1

    while pointer_one < pointer_two:
        lst[pointer_one], lst[pointer_two] = lst[pointer_two], lst[pointer_one]
        pointer_one += 1
        pointer_two -= 1

    return lst

list_test = [1,2,3,4,5]
print(reverse_list(list_test))

'''
Time Complexity: O(n) — each element is swapped once.
Space Complexity: O(1) — in-place swaps, no extra storage.
'''

# Problem 3: Evaluating Solutions
def reverse_list(lst) -> list:
    '''Removes a list utilizing the slicing technqiue'''
    # Create a new reversed list
    reversed_lst = lst[::-1]
    # Copy the elements back into the original list
    for i in range(len(lst)):
        lst[i] = reversed_lst[i]

    return lst

list_test = [1,2,3,4,5]
print(reverse_list(list_test))

'''
Time Complexity: O(n) — slicing creates a copy, then another loop copies elements back.
Space Complexity: O(n) — extra list of size n is created.
'''

# Problem 4: Move Even Integers
def sort_array_by_parity(nums: list) -> list:
    '''Takes in a list of numbers, the orders them from even first, followed with odd afterwards.'''
    end_pointer = len(nums) - 1
    even_list = []
    odd_list = []

    while end_pointer >= 0:
        if nums[end_pointer] % 2 == 0:
            even_list.append(nums[end_pointer])
        else:
            odd_list.append(nums[end_pointer])
        end_pointer -= 1
    return even_list + odd_list

nums = [3,1,2,4]
nums2 = [0]
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))


'''
Time Complexity: O(n) — scans list once, then concatenates two lists.
Space Complexity: O(n) — creates even_list and odd_list.
'''

# Problem 4: More efficient approach
def sort_array_by_parity(nums: list) -> list:
    left, right = 0, len(nums) - 1
    
    while left < right:
        if nums[left] % 2 == 0:
            left += 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1
    return nums

# Test cases
nums = [3, 1, 2, 4]
nums2 = [0]
print(sort_array_by_parity(nums))   # Example: [4,2,1,3] or [2,4,3,1] (order of evens/odds may vary)
print(sort_array_by_parity(nums2))  # [0]

'''
Time Complexity: O(n) — each element is checked/swapped at most once.
Space Complexity: O(1) — swaps done in-place, no extra lists.
'''

# #Problem 5: Palindrome
def first_palindrome(words: list) -> str:
    '''Returns the first palindromic string witihin the provided list, empty string otherwise.'''

    def palindrome_check(word):
        '''Checks to see if the passed word is a palindrome.'''
        first_pointer = 0
        last_pointer = len(word) - 1

        while first_pointer < last_pointer:
            if word[first_pointer] != word[last_pointer]:
                return False
            else:
                first_pointer += 1
                last_pointer -= 1
        return True

    for word in words:
        if palindrome_check(word):
            return word
    return ''

words = ["abc","car","ada","racecar","cool"]
palindrome1 = first_palindrome(words)
print(palindrome1)

words2 = ["abc","racecar","cool"]
palindrome2 = first_palindrome(words2)
print(palindrome2)

words3 = ["abc", "def", "ghi"]
palindrome3 = first_palindrome(words3)
print(palindrome3)
    
'''
Time Complexity: O(n) — n = total number of characters across all words; each character checked at most once.
Space Complexity: O(1) — only pointers and counters are used, no extra storage.
'''

# Problem 6: Remove Duplicates with O(1)
def remove_duplicates(nums: list) -> list:
    if not nums:
        return []

    write_index = 0
    for read_index in range(1, len(nums)):
        if nums[read_index] != nums[write_index]:
            write_index += 1
            nums[write_index] = nums[read_index]

    # Remove everything after the last unique element
    del nums[write_index + 1:]
    return nums

# Test
nums = [1,1,2,3,4,4,4,5]
result = remove_duplicates(nums)
print(result)  # [1,2,3,4,5]
print(nums)    # same list modified in-place

'''
Complexity
Time: O(n) — scan list once + delete the tail once.
Space: O(1) — everything is done in-place, no extra array.
'''