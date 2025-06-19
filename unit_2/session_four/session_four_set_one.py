"""
Problem 1: Cast Vote
Write a function cast_vote() that records a vote for a candidate in an election. 
The function accepts a dictionary votes that maps candidates to their current number 
of votes and a string candidate that represents the candidate the user would like to 
vote for. If the candidate doesn't exist, add them to the dictionary. 
The function should return the updated dictionary.
"""
def cast_vote(votes: dict, candidate: str):
    if candidate not in votes:
        votes[candidate] = 1
    else:
        votes[candidate] += 1
    return votes

candidates = {
    "billy": 1,
    "bob" : 32,
    "joe": 10
}

print(cast_vote(candidates, "sarah"))
print(cast_vote(candidates, "joe"))

"""
Problem 2: Keys in Common
Write a function that takes in two dictionaries, dict1 and dict2 and finds all 
keys common to both dictionaries. The function returns a list of common keys.
"""
def keys_in_common(dict1: dict, dict2: dict):
    common_keys = []

    for key in dict1:
        if key in dict2:
            common_keys.append(key)
    
    return common_keys

candidates_1 = {
    "billy": 1,
    "sarah" : 32,
    "joe": 10
}
candidates_2 = {
    "billy": 1,
    "bob" : 32,
    "joe": 10
}

print(keys_in_common(candidates_1, candidates_2))

"""
Problem 3: Highest Priority Task
Given a dictionary tasks where keys are task names and values are priorities
(1-10, where 10 is the highest priority), write a function get_highest_priority_task()
that removes the task with the highest priority from the dictionary and returns its name.
If two tasks have the same priority, return the task that comes first in the alphabet.
"""
def highest_priority_task(tasks: dict):
    highest_task = 0
    highest_priority = None

    for task in tasks:
        if tasks[task] > highest_task:
            highest_task = tasks[task]
            highest_priority = task
    return highest_priority

task_dict = {
    "task1" : 2,
    "task2" : 3,
    "task4" : 1,
    "task5" : 10,
    "task6" : 8
}
print(highest_priority_task(task_dict))

"""
Problem 4: Frequency Count
Write a function that takes in a list of integers nums and counts the number of occurrences
of each integer. The function returns the result as a dictionary with integers as keys and 
their counts as values.
"""
def frequency_count(nums: list):
    integer_count = {}

    for num in nums:
        if num not in integer_count:
            integer_count[num] = 1
        else:
            integer_count[num] += 1
    return integer_count

random_nums = [1,2,2,3,23,21,3,1231,2,0,0,12,3]
print(frequency_count(random_nums))

"""
Problem 5: Find Majority Element
Write a function find_majority_element() that takes in a list of integers elements and 
finds the majority element in the list. A majority element is an element that appears 
more than n/2 times where n is the size of the list. If there is no majority element, return None.
"""
def find_majority_element(elements: list):
    elemnt_count = {}

    for num in elements:
        if num not in elemnt_count:
            elemnt_count[num] = 1
        else:
            elemnt_count[num] += 1
    
    n = len(elements) // 2

    highest_majority = None

    for key in elemnt_count:
        if elemnt_count[key] > n:
            highest_majority = key
    return highest_majority

print(find_majority_element(random_nums))
test = [11,1,1,12,1,3,4,1,1,1]
print(find_majority_element(test))


"""
Problem 6: Has Duplicates
Write a function hasDuplicates() that takes in a list of integers nums and a positive number
k as parameters. The function returns True if the list contains any duplicate elements within
the range 0 to k (inclusive). If k is greater than the list's length, the solution should 
check for duplicates in the complete list. The function should return False otherwise.
"""
def has_duplicates(nums: list, k: int):
    if k > len(nums):
        dupli_dict = {}

        for num in nums:
            if num not in dupli_dict:
                dupli_dict[num] = 1
            else:
                return True
        return False
    else:
        dupli_dict = {}
        for num in range(0, k):
            if num not in dupli_dict:
                dupli_dict[num] = 1
            else:
                return True
        return False


"""
Problem 7: Make Pairs
Write a function divideList() that takes in an integer list nums consisting of 2*n 
integers as parameters. The function divides nums into n pairs such that:
Each element belongs to exactly one pair
The elements present in a pair are equal
Return True if nums can be divided into n pairs, otherwise return False.
"""
def divide_list(nums: list):
    if len(nums) % 2 == 0:
        num_count = {}
        for num in nums:
            if num not in num_count:
                num_count[num] = 1
            else:
                num_count[num] += 1

        for key in num_count:
            if num_count[key] % 2 != 0:
                return False
        return True
    return False

nums = [3,2,3,2,2,2]
print(divide_list(nums))
nums = [3,2,3,2,2,2,3,2]
print(divide_list(nums))
