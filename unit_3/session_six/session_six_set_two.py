# Problem Set Two

# Problem 1: String to Integer
# Write a function string_to_integer_mapping() that takes in a string of digits s
# as a parameter and returns a list where each element is the integer value of 
# the corresponding digit in the string.
def string_to_integer_mapping(s: str):
    list_of_digits = []

    for digit in s:
        list_of_digits.append(int(digit))

    return list_of_digits

num_string = '12345'
print(string_to_integer_mapping(num_string))


# Problem 2: Delete Minimum
# Write a function delete_minimum_elements(nums) that takes in a list of integers 
# nums as a parameter and continuously removes the minimum element until the list 
# is empty. The function returns a new list of all the elements in nums in the 
# order in which they were removed.
def delete_minimum_elements(nums: list):
    removed_elements = []
    copy_of_nums = nums[:]

    for number in nums:
        min_num  = min(copy_of_nums)
        removed_elements.append(min_num)
        copy_of_nums.remove(min_num)
    
    return removed_elements

nums = [5,3,2,8,3,1]
removed_lst = delete_minimum_elements(nums)
print(removed_lst)



# Problem 3: Longest Common Prefix
# Write a function longest_common_prefix() that takes in a list of strings strings 
# as a parameter. The function returns the longest common prefix (not substring) 
# of all strings and if there are none, it returns an empty string "".
def longest_common_prefix(strings: list):
    if not strings:
        return ""

    # Start with the first string as the prefix
    prefix = strings[0]

    for string in strings[1:]:
        # Reduce the prefix until it matches the beginning of each string
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix


string_test = ['dfsf','sfddsfs','sdfds']
print(longest_common_prefix(string_test))


# Problem 4: Consecutive Characters
# Write a function count_consecutive_characters() that takes in a string str1 as 
# a parameter and returns the count of the most frequent consecutive character.
def count_consecutive_characters(str1: str):
    consecutive_list = []
    
    count = 1
    character = str1[0]

    for i in range(1, len(str1)):
        if str1[i] == character:
            count += 1
        else:
            consecutive_list.append((character, count))
            count = 1
            character = str1[i]

    return max(consecutive_list, key=lambda x: x[1])

test_s = 'adsfdsbbedffsttttteeeeg'
print(count_consecutive_characters(test_s))


# Problem 5: Partition Labels
# Write a function partition_labels() that takes in a string s as a parameter. 
# s consists of lowercase letters and represents the order of characters as 
# they appear in a document. The function partitions s into as many parts as 
# possible so that each unique letter appears in at most one part, and 
# returns a list of integers representing the size of these parts.
def partition_labels(s: str):
    last_index = {char: idx for idx, char in enumerate(s)}  # Step 1: last occurrence of each char
    result = []
    start = end = 0

    for idx, char in enumerate(s):
        end = max(end, last_index[char])  # Expand end to the furthest last occurrence seen so far
        if idx == end:  # When current index reaches the end of the partition
            result.append(end - start + 1)
            start = idx + 1  # Start new partition

    return result


# Problem 6: Interleave Lists
# Write a function interleave_lists() that accepts two lists as parameters. 
# The function should return a new list that combines the given lists by 
# alternating which list it takes its next element from. It will take 
# elements in order, and if one list is longer it will append the 
# remaining elements to the end of the interleaved list
def interleave_lists(list_one: list, list_two: list):
    interleaved_list = []
    max_length = max(len(list_one), len(list_two))

    for i in range(max_length):
        if i < len(list_one):
            interleaved_list.append(list_one[i])
        if i < len(list_two):
            interleaved_list.append(list_two[i])

    return interleaved_list

list1 = [1, 3, 5]
list2 = [2, 4, 6, 8, 10]
print(interleave_lists(list1, list2))