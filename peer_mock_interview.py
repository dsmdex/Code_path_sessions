# Peer Mock Interview

'''
Given a string s consisting of lowercase and/or uppercase English letters and digits, 
return all possible strings that can be formed by changing the case of the letters in s. 
You may not alter the order of characters in the string, and digits should remain unchanged.
Input: s = "a1b2"
Output: ["a1b2", "A1b2", "a1B2", "A1B2"]
Input: s = "3z4"
Output: ["3z4", "3Z4"]
Input: s = "12345"
Output: ["12345"]

def possible_strings(s: str):
    all_combinations = ['']
    
    if not s:
        return all_combinations
    
    
    for char in s:
        if not char.isalpha():
            all_combinations[0].append(char)
        else:
            upper_case = char.upper()
            lower_case = char.lower()
            all_combinations[0].append[(upper_case)
            all_combinations[0].append(lower_case)
            
    return all_combinations
s = "12345"       
print(possible_strings(s))  
'''

'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Input: haystack = "leetcode", needle = "leeto"
Output: -1
'''

#U: If substring exists -> return index, otherwise return -1 empty strings, needle empty -> return haystack, haystack is empty return -1

#M: two pointer method: sliding window check for substrings -> length of the window to be the size of the needle, if sliding window reaches the end, and nothing is found return -1 



    