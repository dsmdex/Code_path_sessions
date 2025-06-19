"""
Problem 1: Return Book
Write a function return_book() that accepts a string title and a dictionary library as parameters.
 library maps book titles to the number of copies the library currently has in stock. The function
   should increment the quantity of the book title in library by 1 and return the updated dictionary.
    If title is not in the library, then add it and set quantity to 1.
"""
def return_book(title:str, library: dict):
    if title not in library:
        library[title] = 1
    else:
      library[title] += 1
    return library
books = {
   "book1": 1,
   "book2": 2,
   "book3": 9,
   "book5": 1
}

print(return_book("book4", books))

"""
Problem 2: Dictionary Difference
Write a function dict_difference() that takes two dictionaries and returns a new dictionary
 that contains only the key-value pairs found exclusively in the first dictionary but not 
 in the second.
"""
def dict_difference(dict1: dict, dict2: dict):
  dict1_pairs_only = {}

  for key in dict1:
    if key not in dict2:
      dict1_pairs_only[key] = dict1[key]
  return dict1_pairs_only

dict_one = {"key1": 1, "key2": 3, "key5": 5}
dict_two = {"key1": 2, "key4": 2, "key3": 9}
print(dict_difference(dict_one, dict_two))


"""
Problem 3: Take from Stock
Write a function pop_stock() that takes a dictionary of items items that keeps track of an 
item and its stock quantity, an item_name, and a quantity to be removed as parameters. The 
function should remove the specified quantity for that item.
If the item does not exist, return the string "Item does not exist."
If the specified quantity is greater than the stock, return a string "Not enough stock."
If the specified item and quantity do exist within items, decrement the item's stock by the 
specified quantity and return the updated dictionary.
"""
def pop_stock(items: dict, item_name: str, quantity: int):
  if item_name not in items:
    return f"{item_name} does not exist."
  if quantity > items[item_name]:
     return f"Not Enough Stock."
  else:
     items[item_name] -= quantity
  return items
books = {
   "book1": 1,
   "book2": 2,
   "book3": 9,
   "book5": 1
}

print(pop_stock(books, "book3", 5))


"""
Problem 4: Group By Frequency
Write a function group_by_frequency() that takes in a list lst and returns a dictionary where 
keys represent the frequency of unique elements within lst and values represent a list of 
elements with the same frequency.
"""
def group_by_frequency(lst):
    freq_map ={}

    for elem in lst:
        if elem not in freq_map:
           freq_map[elem] = 1
        else:
           freq_map[elem] += 1

    group_by_freq = {}

    for elem, count in freq_map.items():
        if count not in group_by_freq:
          group_by_freq[count] = []
        group_by_freq[count].append(elem)

    return dict(group_by_freq)
  

list_of_ele = [1,1,1,4,5,1,9,9,9,9]
print(group_by_frequency(list_of_ele))


"""
Problem 5: No Duplicates Allowed
Write a function that takes in a list of integers nums as a parameter and removes all 
duplicates. The function should return a list containing the unique elements in the order
 of their last occurrence in the original list.
"""
def no_duplicates(nums: list):
  unique_list = []

  for number in nums:
    if number not in unique_list:
      unique_list.append(number)
  return unique_list

numby = [1,1,1,1,1,5,1,6,7,4,5,6,2]
print(no_duplicates(numby))


"""
Problem 6: First Repeating Element
Write a function find_min_index_of_repeating() that takes in an integer list nums as a 
parameter and returns the minimum index of an element that has a duplicate value. The 
function should only do a single traversal of the list. If there are no repeating 
elements, return None.
"""
def find_min_index(nums: list):
  if not nums:
     return None
  
  for index in range(len(nums)):
     element_count = 0
     for element in nums:
        if nums[index] == element:
           element_count += 1
     if element_count > 1:
        return f"index: {index}"
     
element_list = [1,2,3,5,4,2,3,4,0]
print(find_min_index(element_list))


"""
Problem 7: Target Sum
Write a function two_sum() that takes in a list of integers nums and an integer 
target as parameters. The function should return the indices of the two numbers 
that add up to target. You may assume that each input would have exactly one 
solution and you may not use the same element twice. The function can return 
the indices in any order.
"""
def two_sum(nums: list, target: int):
  
  for i, number_i in enumerate(nums):
    for j, number_j in enumerate(nums):
      if i != j:
         if number_i + number_j == target:
            return (f"index {i} and index {j}")
  return "No index return the target"
         
numbo = [1,5,2,6,2,5,7,3,5,1,45,2]
print(two_sum(numbo, 4))