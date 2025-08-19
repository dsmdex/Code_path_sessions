# Problem 1: Highest Exponent
def find_highest_exponent(base: int, limit: int) -> int:
    exp = 0
    while base ** (exp + 1) <= limit:
        exp += 1
    return exp

exp = find_highest_exponent(2, 100)
print(exp)

exp2 = find_highest_exponent(3, 5)
print(exp2)

'''
Time: O(log₍base₎(limit)) → which we usually simplify to O(log n).
Space: O(1) since we’re only using a counter.
'''

# Problem 2: Two-Pointer Target Sum
def two_sum(nums: list, target: int) -> list:
    nums = set(nums)
    nums = list(nums)
    nums.sort()
    left, right = 0, len(nums) - 1

    while left < right:
        curr_sum = nums[left] + nums[right]
        if curr_sum == target:
            return [left, right]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return []


nums = [2,7,11,15, 7]
sol1 = two_sum(nums, 9)
print(sol1)
sol2 = two_sum(nums, 18)
print(sol2)

'''
Time Complexity:
Sorting dominates → O(n log n)

Space Complexity:
The set copy costs O(n) (since you store all numbers again).
'''

# Problem 3: Evaluates Two Sum
def two_sum(nums, target):
    prev_map = {}  # Value to index mapping
    
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[nums[i]] = i

'''
Time: O(n) → each number is checked and inserted once
Space: O(n) → the dictionary stores up to n elements
'''

# Problem 5: Reverse Prefix
def reverse_prefix(word: str, ch: str) -> str:
    """Reverses the segment of word from start up to the first occurrence of ch. Returns original word if ch not found."""
    
    def reverse_string(sub: str) -> str:
        word_to_list = list(sub)
        pointer_one = 0
        pointer_two = len(sub) - 1

        while pointer_one < pointer_two:
            word_to_list[pointer_one], word_to_list[pointer_two] = word_to_list[pointer_two], word_to_list[pointer_one]
            pointer_one += 1
            pointer_two -= 1
        return ''.join(word_to_list)
    
    read_index = 0
    while read_index < len(word):  # fixed: include last character
        if word[read_index] == ch:
            return reverse_string(word[:read_index + 1]) + word[read_index + 1:]
        read_index += 1

    return word


# Tests
word = "abcdefd"
rev_word = reverse_prefix(word, "d")
print(rev_word)  # "dcbaefd"

word2 = "helloworld"
rev_word2 = reverse_prefix(word2, "w")
print(rev_word2)  # "wollehorld"

word3 = "xyzxyz"
rev_word3 = reverse_prefix(word3, "a")
print(rev_word3)  # "xyzxyz" (no change)


'''
Time Complexity: O(n)  
    - We scan the string once to find the character (O(n))  
    - We reverse at most n characters in the prefix (O(n))  
    → Total: O(n)

Space Complexity: O(n)  
    - We create a list for the prefix to reverse (O(n))  
    - The final string concatenation also creates a new string (O(n))  
    → Total: O(n)
'''

# Problem 6: Squash Spaces
def squash_spaces(s: str) -> str:
    s = list(s)           # convert string to list so we can modify in-place
    write_index = 0       # points to where the next valid character goes
    n = len(s)
    
    i = 0                 # read pointer
    while i < n:
        if s[i] != ' ':                    # case 1: normal character
            s[write_index] = s[i]         # write it
            write_index += 1
        elif write_index > 0 and s[write_index - 1] != ' ':  # case 2: first space after a word
            s[write_index] = ' '          # write a single space
            write_index += 1
        # else: skip extra spaces
        i += 1                             # move read pointer forward
    
    # remove trailing space if any
    if write_index > 0 and s[write_index - 1] == ' ':
        write_index -= 1
    
    return ''.join(s[:write_index])        # build final string

# Tests
print(squash_spaces("  hello    world  "))  # "hello world"
print(squash_spaces("  what  about  this    ?"))  # "what about this ?"
print(squash_spaces("this is my sentence"))  # "this is my sentence"

'''
Time: O(n) → one pass through the string
Space: O(n) → converting string to list
'''