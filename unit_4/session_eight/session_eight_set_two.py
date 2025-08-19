# Problem 1: Perfect Number
def is_perfect_number(n: int) -> bool:
    divisor = 1

    sum = 0
    while divisor != n:
        if n % divisor == 0:
            sum += divisor
        divisor += 1

    if sum == n:
        return True
    return False

print(is_perfect_number(6))
print(is_perfect_number(28))
print(is_perfect_number(9))

'''
Time Complexity: O(n) — the loop runs n-1 times.
Space Complexity: O(1) — only a few integer variables (divisor and sum) are used.
'''

# More efficient way to implement problem one
import math

def is_perfect_number(n: int) -> bool:
    if n <= 1:
        return False

    total = 1  # 1 is always a divisor
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            total += i
            paired_divisor = n // i
            if paired_divisor != i:  # avoid adding the square root twice
                total += paired_divisor

    return total == n

'''
Time: O(√n) — loop goes up to the square root of n.
Space: O(1) — only a few variables (total, i, paired_divisor).
'''

# Problem 2: 2-Pointer Palindrome
def is_palindrome(s: str) -> bool:
    '''Takes in a string and returns True if the string is a palindrome, false otherwise.'''

    first_pointer = 0
    second_pointer = len(s) - 1

    while first_pointer < second_pointer:
        if s[first_pointer] != s[second_pointer]:
            return False
        first_pointer += 1
        second_pointer -= 1
    return True

s = "amanaplanacanalpanama"
s2 = "helloworld"

print(is_palindrome(s))
print(is_palindrome(s2))

'''
Time: O(n) - must check each elements on both ends, which checks the whole string
Space: O(1) - does not create any new data structures, just two variables to track indices 
'''

# Problem 4: Make Palindromes
def make_palindrome(s: str) -> str:
    list_s = list(s)  # convert string to list
    first_pointer = 0
    second_pointer = len(s) - 1

    while first_pointer < second_pointer:
        if list_s[first_pointer] != list_s[second_pointer]:
            smaller = min(list_s[first_pointer], list_s[second_pointer])
            list_s[first_pointer] = smaller
            list_s[second_pointer] = smaller
        first_pointer += 1
        second_pointer -= 1

    return ''.join(list_s)  # convert list back to string

# Tests
print(make_palindrome("egcfe"))  # "efcfe"
print(make_palindrome("abcd"))   # "abba"
print(make_palindrome("seven"))  # "seees"


'''
Time Complexity: O(n) — each character is checked exactly once.
Space Complexity: O(n) — storing the string as a list for in-place modifications.
'''

# Problem 5: Reverse Vowels
def reverse_vowels(s: str) -> str:
    '''Takes in a string s and returns a string with all the vowels in the string reversed.'''
    list_s = list(s)
    first_pointer = 0
    second_pointer = len(s) - 1

    def is_vowel(character: str) -> bool:
        'Checks if the given character is a vowel.'
        vowels = ['a','e','i','o','u']

        if character in vowels:
            return True
        return False
    
    while first_pointer < second_pointer:
        if is_vowel(list_s[first_pointer]) and is_vowel(list_s[second_pointer]):
            list_s[first_pointer], list_s[second_pointer] = list_s[second_pointer], list_s[first_pointer]
            first_pointer += 1
            second_pointer -= 1
        elif is_vowel(list_s[first_pointer]):
            second_pointer -= 1
        elif is_vowel(list_s[second_pointer]):
            first_pointer += 1
        else:
            first_pointer += 1
            second_pointer -= 1
    return ''.join(list_s)

s1 = "hello"
print(reverse_vowels(s1))

s2 = "leetcode"
print(reverse_vowels(s2))

'''
Time Complexity: O(n) — each character is visited at most once by the two pointers.
Space Complexity: O(n) — you convert the string to a list to allow in-place swaps.
'''

# Problem 6: Two-Pointer Remove Element
def removeElement(nums: list, val: int) -> int:
    write_index = 0
    for read_index in range(len(nums)):
        if nums[read_index] != val:
            nums[write_index] = nums[read_index]
            write_index += 1
    del nums[write_index:]
    return len(nums), nums


nums = [5, 4, 4, 3, 4, 1]
print(removeElement(nums, 4))

'''
Time: O(n) → each element is scanned once, and the del of the tail is O(1) amortized.
Space: O(1) → only two pointers used, no extra array.
'''