# Problem Set Three

# Problem 1: Remove Vowels
# Write a function remove_vowels() that takes in a string s as a parameter 
# and returns a new string with all the vowels removed. For the purposes of 
# this exercise, consider a, e, i, o, and u as vowels and not y. The function 
# should preserve the case of the original letters.
def remove_vowels(s: str):
    vowel_less_string = ''
    vowels_to_see = ['a','e','i','o','u']

    for letter in s:
        if letter not in vowels_to_see:
            vowel_less_string += letter
    
    return vowel_less_string

vowel_string = 'excalibur'
print(remove_vowels(vowel_string))
print()

# Problem 2: Missing Integer
# Write a function find_missing_positive() that takes in a sorted list of 
# integers nums that always starts at 1, and returns the smallest missing positive integer.
def find_missing_positive(nums: list):
    nums.sort()

    max_element = max(nums)

    for i in range(1, max_element + 1):
        if i not in nums:
            return i
    
number_test = [2,3,4,5,6,7,9,1,9,5]
print(find_missing_positive(number_test))

# Problem 3: Word Follows Pattern
# Write a function wordPattern() that takes in a string pattern and a string s as parameters. 
# The function returns True if s follows the pattern and False otherwise. 
# The string follows the pattern if there is a 1:1 correspondence between a 
# letter in the pattern and a non-empty word in s.
def wordPattern(pattern, s):
    words = s.split()
    if len(pattern) != len(words):
        return False
    
    pattern_map = {}
    for index, word in enumerate(words):
        p_char = pattern[index]
        # Did we already use this char for another word?
        if p_char not in pattern_map:
            pattern_map[p_char] = word
        elif pattern_map[p_char] != word:
            return False

    # We couldn't find any mis-matches
    return True

pattern = "abba"
s = "dog cat cat dog"
print(wordPattern(pattern, s))
s2 = "dog cat cat fish"
print(wordPattern(pattern, s2))

pattern2 = "aaaa"
s3 = "dog cat dog cat"
print(wordPattern(pattern2, s3))
s4 = "dog dog dog dog"
print(wordPattern(pattern2, s4))
    

# Problem 4: Binary Substrings
# Write a function binary_substrings_count() that takes in a string s representing a binary 
# number as a parameter. The function counts the number of substrings that satisfy all 
# of the following conditions:
#     contains an equal number of 0s and 1s
#     all the 0s in the substring are grouped consecutively
#     all the 1s in the substrings are grouped consecutively

def binary_substrings_count(s):
    prev_run_length = 0
    curr_run_length = 1
    count = 0
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            curr_run_length += 1
        else:
            prev_run_length = curr_run_length
            curr_run_length = 1
        if prev_run_length >= curr_run_length:
            count += 1
    return count

s = "00110011"
print(binary_substrings_count(s))

s2 = "10101"
print(binary_substrings_count(s2))

s3 = "1111"
print(binary_substrings_count(s3))



# Write a function exclusive_elements() that takes in two integer 
# lists lst1 and lst2 as parameters and returns a new list that 
# contains the elements that are exclusively in one list only 
# (elements that are in lst1 but not in lst2 and elements 
# that are in lst2 but not in lst1)
def exclusive_elements(lst1, lst2):
    exclusive_lst1 = []
    exclusive_lst2 = []
    
    # Find elements in lst1 that are not in lst2
    for item in lst1:
        if item not in lst2:
            exclusive_lst1.append(item)
    
    # Find elements in lst2 that are not in lst1
    for item in lst2:
        if item not in lst1:
            exclusive_lst2.append(item)
    
    return exclusive_lst1 + exclusive_lst2

lst1 = [3,1,8,10]
lst2 = [4,5,3,7,8]
excl_lst = exclusive_elements(lst1, lst2)
print(excl_lst)


# Problem 6: Flowerbed
# Imagine you have a flowerbed in which some of the plots are planted, and some are not. 
# Flowers cannot be planted in adjacent plots.
# Write a function can_place_flowers() that takes in an integer list flowerbed containing 
# 0's and 1's, (where 0 is an empty plot and 1 is a planted plot) and an integer n that 
# represents the number of new flowers wanting to be planted as parameters. The function 
# should return True if n new flowers can be planted in the flowerbed without violating 
# the no-adjacent-flowers rule and False otherwise.
def can_place_flowers(flowerbed, n):
    count = 0  # Count of flowers that can be planted
    length = len(flowerbed)

    for i in range(length):
        # Check if the current plot is empty
        if flowerbed[i] == 0:
            # Check the previous and next plot, considering the edge cases
            prev_empty = i < 0 or flowerbed[i - 1] == 0
            next_empty = i >= length or flowerbed[i + 1] == 0
            
            # If both adjacent plots are empty, plant a flower here
            if prev_empty and next_empty:
                flowerbed[i] = 1  # Mark this plot as planted
                count += 1  # Increment the count of flowers that can be planted
                
                # If we've planted enough flowers, return true immediately
                if count >= n:
                    return True

    # After checking all plots, if we've planted enough flowers, return true; otherwise, false
    return count >= n

flowerbed = [1,0,0,0,1]
approved = can_place_flowers(flowerbed, 1)
approved2 = can_place_flowers(flowerbed, 2)
print(approved)
print(approved2)
