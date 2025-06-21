# Problem Set One

# Problem 1: Calling Mississippi
# In a new Replit, copy and paste the following function:
# Call the function so that it prints out the following to the console 
# (without calling the function more than once)
def count_mississippi(limit):
    for num in range(1, limit):
        print( f"{num} mississippi")
count_mississippi(6)


# Problem 2: Swap Ends
# Write a function swap_ends() that accepts a string my_str as a parameter and 
# returns a new string where the first and last characters from my_str are swapped.
def swap_ends(my_str):
    firstVal = my_str[0]
    lastVal = my_str[len(my_str)-1]
    middleVal = my_str[1:len(my_str)-1]
    return lastVal + middleVal + firstVal

my_str = "boat"
swapped = swap_ends(my_str)
print(swapped)


# Problem 3: Is Pangram
# Write a function is_pangram() that takes in a string my_str as a parameter 
# and returns True if the string is a pangram and False if not. A pangram is 
# a sentence containing every letter in the English alphabet. 
def is_pangram(my_str):
    alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z'
]

    for letter in alphabet:
        if letter in my_str:
            alphabet.remove(letter)
        print(alphabet)
    if not alphabet:
        return True
    return False


my_str = "The quick brown fox jumps over the lazy dog"
print(is_pangram(my_str))

str2 = "The dog jumped"
print(is_pangram(str2))

# Problem 4: Reverse String
# Write a function reverse_string() that takes a string my_str as a parameter 
# and returns the string reversed.
def reverse_string(my_str: str):
    reversed_string = ""
    
    for index in range(len(my_str) - 1, -1, -1):
        reversed_string += my_str[index]
        
    return reversed_string


my_str = "live"
print(reverse_string(my_str))


# Problem 5: First Unique
# Write a function first_unique_char() that given a string my_str as a parameter, 
# it finds the first non-repeating character in it and returns its index. 
# If it does not exist, then return -1.
def first_unique_char(my_str):
    seen = {}
    
    for i in my_str:
        if i not in seen:
            seen[i] = 1
        elif i in seen:
            seen[i] += 1
    
    unique = -1
    for key, value in seen.items():
        # we can do this lol, dicts are ordered (and you good lol)
        if value == 1:
            unique = my_str.index(key) #fireeee WAIT I THINK THATS CORRECT !!!
            return unique 
        # omg now we just need the index LOL
        # haha no worries
        # YESSSSSS
        # we made it just in time haha
    return unique
 #good work frrr!!! just in time!
    # thanks for the good vibes!
my_str = "leetcode"
print(first_unique_char(my_str))


# Problem 6: Minimum Distance
# Write a function min_distance() that takes in a list of strings words and two 
# strings word1 and word2' as parameters. The function should return the minimum 
# distance between word1 and word2 in the list of words. The distance between one 
# word and an adjacent word in the list is 1.
def min_distance(words: list, word1: str, word2: str) -> int:
    index_one = None
    index_two = None
    min_dist = float('inf')  # Start with a very large number

    for i in range(len(words)):
        if words[i] == word1:
            index_one = i
        elif words[i] == word2:
            index_two = i

        if index_one is not None and index_two is not None:
            dist = abs(index_one - index_two)
            min_dist = min(min_dist, dist)

    return min_dist if min_dist != float('inf') else -1  # -1 if not found


words = ["the", "quick", "brown", "fox", "jumped", "the"]
dist1 = min_distance(words, "quick", "jumped")
dist2 = min_distance(words, "the", "jumped")
print(dist1)
print(dist2)

words2 = ["code", "path", "code", "contribute",  "practice"]
dist3 = min_distance(words2, "code", "practice")
print(dist3)