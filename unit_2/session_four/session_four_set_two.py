"""
Problem 1: Update Score
Write a function update_score() that takes in a dictionary scores that maps player 
names to current scores, a string player, and an integer points as parameters. 
The function adds the points to the current score of player in the dictionary and 
returns the updated dictionary. If the player does not exist in scores, then add them.
"""
def update_score(scores: dict, player: str, points: int):
    if player not in scores:
        scores[player] = points
    else:
        scores[player] += points
    return scores
player_test = {
    "player1": 12,
    "player2": 250,
    "player3": 120,
    "player4": 80
}
print(update_score(player_test, "player1", 100))
print(update_score(player_test, "player5", 135))

"""
Problem 2: Dictionary Intersection
Write a function dict_intersection() that takes in two dictionaries as 
parameters and returns a new dictionary containing the key-value pairs 
found in both dictionaries.
"""
def dict_intersection(dict1: dict, dict2: dict):
    intersected_dict = {}

    for key, value in dict1.items():
        if key in dict2 and dict2[key] == value:
            intersected_dict[key] = value
    return intersected_dict


dict1 = {
    "test1": 123,
    "test2": 456,
    "test3": 789
}

dict2 = {
    "test4": 321,
    "test2": 456,
    "test6": 987
}

print(dict_intersection(dict1, dict2))

"""
Problem 3: Filter by Price
Write a function that takes in a dictionary of items and a price_
threshold as parameters.The function should iterate through the 
dictionary and remove all items that has a value less than 
price_threshold. The function also returns a list of all 
items that are removed. If no item satisfies the condition, return None.
"""
def filter_by_price(item_dict: dict, price_threshold: int):
    removed_items = []

    for key, value in item_dict.items():
        if value < price_threshold:
            removed_items.append(key)

    for item in removed_items:
        del item_dict[item]
    
    if removed_items:
        return removed_items
    return None
items = {
    "item1": 1,
    "item2": 2,
    "item3": 10,
    "item4": 15,
    "item5": 20,
    "item6": 9
}
print(filter_by_price(items, 9))


"""
Problem 4: Find Odd Occurrences
Write a function find_odd_occurrences() that takes in a list of integers
nums where all numbers occur an even number of times except for 
two unique numbers that occur an odd number of times. The function 
should find the two unique numbers and return them as a list. 
Assume each problem has exactly one solution.
"""




"""
Problem 5: Find Mode
Write a function find_mode() that takes in a non-empty list of 
integers lst as a parameter. The function returns the mode 
(the most frequently occurring number) and if there is a tie, 
return the element which appeared first in the list.
"""
def find_mode(lst: list):
    num_count = {}

    for number in lst:
        if number not in num_count:
            num_count[number] = 1
        else:
            num_count[number] += 1
    
    highest_count = 0
    highest_key = ''

    for key, value in num_count.items():
        if value > highest_count:
            highest_count = value
            highest_key = key
    return highest_key

num_lst = [1,1,1,1,2,2,2,2]
print(find_mode(num_lst))


"""
Problem 6: How Many Smaller
Write a function smallerNumbersThanCurrent() that takes in 
a list of numbers nums as a parameter.
For each nums[i], the function should find out how many 
numbers in the list are smaller than it.
(For each nums[i], count the number of valid j's such 
that j!=i and nums[j] < nums[i])
Return the answers in a list.
"""
def smaller_numbers_than_current(nums: list):
    result = []
    
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if i != j and nums[j] < nums[i]:
                count += 1
        result.append(count)
    
    return result


numbers = [1,2,3,4,5,6,7,8,9]
print(smaller_numbers_than_current(numbers))
nums = [8, 1, 2, 2, 3]
print(smaller_numbers_than_current(nums))

"""
Problem 7: Good Pairs
Write a function numIdenticalPairs() that takes in a 
list of integers nums and returns the 
number of good pairs.
A pair (i, j) is called good if nums[i] == nums[j] and i < j.
"""
def num_identical_pairs(nums: list):
    num_of_pairs = 0

    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] == nums[j] and i < j:
                num_of_pairs += 1
    return num_of_pairs

numbers = [1,1,1,3,4,5,6,4,3,5,6]
print(num_identical_pairs(numbers))