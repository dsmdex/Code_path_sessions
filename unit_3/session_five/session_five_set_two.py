# Problem Set Two

# Problem 1: Perfect Match
def match_made(dictionary):
	for key, value in dictionary.items():
		print( f"{key} and {value} are a perfect match.")

# Add code to your Replit so that your program prints out the following to the console:

# Peanut butter and Jelly are a perfect match.
# Spongebob and Patrick are a perfect match.
# Ash and Pikachu are a perfect match.
items_to_be_matched = {
	"Peanut Butter": "Jelly",
	"Spongebob": "Patrick",
	"Ash": "Pikachu"
}
match_made(items_to_be_matched)


# Problem 2: Remove Char
# Write a function remove_char() that takes in a string s and an integer n as parameters,
# The function returns a new string with the nth character removed where 0 < n < len(s).
def remove_char(s: str, n: int):
	if not s:
		return None
	
	new_string = ''
	
	for i in range(len(s)):
		if i != n:
			new_string += s[i]
	return new_string

some_string = "hih there old friend!"
print(remove_char(some_string, 2))


# Problem 3: Count Vowels
# Write a function vowel_count() that takes in a string s as a parameter and returns
# the number of vowels in the given string.
def vowel_count(string: str):
    vowels_to_look_for = ['a', 'e', 'i', 'o', 'u', 'y']
	
    count = 0

    for vowel in string:
        if vowel in vowels_to_look_for:
            count += 1
	
    return count

print(vowel_count(some_string))

# Problem 4: Reverse Sentence
# Write a function reverse_sentence() that takes in a string sentence as a parameter and
# returns the string with the sentence but with the order of the words reversed. 
# The sentence will only contain alphabetic characters and spaces to separate the words. 
# If there is only one word in the sentence, the function returns the original string.
def reverse_sentence(sentence: str) -> str:
    words = sentence.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

some_sentence = "we are testing out the function output for question 4"
print(reverse_sentence(some_sentence))


# Problem 5: String Compression
# Write a function that takes in a string my_str as a parameter and performs basic string 
# compression using counts of repeated characters.

# For example, the string "aabcccccaaa" would become "a2b1c5a3". If the compressed string 
# does not become smaller than the original string, return the original string. Assume the 
# string only has alphabetic characters.
def compress_string(my_str: str) -> str:
    if not my_str:
        return my_str

    compressed = []
    count = 1
    current_char = my_str[0]

    for i in range(1, len(my_str)):
        if my_str[i] == current_char:
            count += 1
        else:
            compressed.append(current_char + str(count))
            current_char = my_str[i]
            count = 1

    # Append the last character and its count
    compressed.append(current_char + str(count))

    # Join the compressed parts
    compressed_str = ''.join(compressed)

    # Return the shorter of the two
    return compressed_str if len(compressed_str) < len(my_str) else my_str
print(compress_string("aabbbaaacccccaaaadddfffffe"))
		

# Problem 6: Needle in a Haystack

# Write a function find_the_needle() that takes in two string parameters: 
# a needle and a haystack. The function returns the index of the first occurrence 
# of needle in haystack, or -1 if needle is not part of haystack.
def find_the_needle(needle: str, haystack: str):
    needle_pointer = 0
    haystack_pointer = -1
    
    for i, letter in enumerate(haystack):
        if letter == needle[needle_pointer]:
            needle_pointer += 1
            if haystack_pointer == -1:
                   haystack_pointer = i
            if needle_pointer == len(needle):
                  return haystack_pointer
        else:
            needle_pointer = 0
            haystack_pointer = -1
        
    return haystack_pointer

string = "haadsfsadfsadfasdfdsafasdfsadfdsfsdyneeedlehaystack"

print(find_the_needle("needle", string))