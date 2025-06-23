# Problem Set One

# Problem 1: Sum of Strings
# Write a function sum_of_number_strings() that takes in a list of strings 
# nums. Each string is a representations of integers. The function 
# should return the sum of these strings as an integer.
def sum_of_number_strings(nums):
    result = 0
    
    for num in nums:
        value = int(num)
        result += value
    return result 

nums = ["10", "20", "30"]
sum = sum_of_number_strings(nums)
print(sum)

# Problem 2: Remove Duplicates
# Write a function remove_duplicates() that takes in a sorted list of integers
# nums as a parameter and removes all duplicates in the list. The function returns the modified list.
def remove_duplicates(nums):
    return sorted(set(nums))

nums = [1,1,1,2,3,4,4,5,6,6]
no_dups = remove_duplicates(nums)
print(no_dups)


# Problem 3: Reverse Letters
# Write a function reverse_only_letters() that takes in a string s as a parameter. 
# The function reverses the order of the letters in the string and returns the new 
# string. Non-letter characters should remain in their original positions.
def reverse_only_letters(s):
    list_s = list(s)
    i, j = 0, len(s)-1
    while i < j:
        if not list_s[i].isalpha():
            i+=1
        elif not list_s[j].isalpha():
            j-=1
        else:
            list_s[i], list_s[j] = list_s[j], list_s[i]
            i+=1
            j-=1
    return "".join(list_s)

s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)

# Problem 5: Teemo's Attack
# In the game League of Legends, Teemo attacks his enemy Ashe with poison arrows. 
# Write a function find_poisoned_duration() that takes in two parameters: time_
# series (the time at which Teemo's attacks hits Ashe) and time_duration 
# (the duration of the poisoning effect). The function returns the total time 
# that Ashe is in a poisoned condition.
def find_poisoned_duration(time_series: list, duration: int) -> int:
    total_duration = 0

    if not time_series:
        return 0

    for i in range(len(time_series) - 1):
        interval = time_series[i + 1] - time_series[i]

        # If the next attack occurs during poison duration,
        # that last second isn't overlapped and shouldn't be double-counted
        if interval == duration:
            total_duration += duration - 1
        else:
            # Add the poisoned time between attacks, truncated if overlapping
            total_duration += min(interval, duration)
        
    # Always add full duration for the last attack
    total_duration += duration

    return total_duration


time_series = [1, 4, 9]
damage = find_poisoned_duration(time_series, 3)
print(damage) 


# Problem 6: Sum Unique Elements
# Write a function sum_of_unique_elements() that takes in two lists of integers, 
# lst1 and lst2, as parameters and returns the sum of the elements that are unique in lst1.

# An element is unique if:
#     it appears exactly once in lst1
#     it does not appear in lst2

def sum_of_unique_elements(lst1, lst2):
    unique_list = []

    for element in lst1:
        if element in unique_list:
            unique_list.remove(element)
        else:
            unique_list.append(element)
    
    sum_of_uniques = 0
    for element in unique_list:
        if element not in lst2:
            sum_of_uniques += element

    return sum_of_uniques


lstA = [1, 2 ,3, 4] 
lstB = [3, 4, 5, 6]
lstC = [7, 7, 7, 7]

sum1 = sum_of_unique_elements(lstA, lstB)
print(sum1)

sum2 = sum_of_unique_elements(lstC, lstB)
print(sum2)
