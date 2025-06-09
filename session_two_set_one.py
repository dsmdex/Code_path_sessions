# Problem Set One

# Problem 1: Print List
def print_list(lst):
    for item in lst:
        print(item)
print_list(["squirtle", "gengar", "charizard", "pikachu"])


# Problem 2:
def doubled(lst):
    if not lst:
        return None
    for item in lst:
        print(item * 2)
doubled(lst = [1,2,3])


# Problem 3: Return Doubled List
# Modify the function doubled() so that instead of printing the items, it returns a new list of the doubled numbers.
def doubled(lst):
    new_list = []
    if len(lst) == 0:
        return None
    for i in lst:
        result = i*2
        new_list.append(result)
    return new_list
print(doubled([1,2,3]))


# Problem 4:
def flip_sign(lst):
    flipped_lst = []
    for item in lst:
        result = item * -1
        flipped_lst.append(result)
    return flipped_lst
print(flip_sign([1,-2,-3,4]))


# Problem 5:
# Write a function max_difference() that takes in a list of integers lst and returns the difference between the smallest and largest value in the list.
def max_difference(lst):
    smallest = lst[0]
    largest = 0
 
    for item in lst:
        if (item < smallest):
            smallest = item
        elif (item > largest):
            largest = item
    return largest - smallest
print(max_difference([5,22,8,10,2]))


# Problem 7: Evens List
# Write a function get_evens() that takes in a list of integers lst as a parameter and returns a list of all even numbers in the list.
def get_evens(lst):
    evens_list = []
    if len(lst) == 0: # if not lst: simpler approach
        return None
    for i in lst:
        if i % 2 == 0:
            evens_list.append(i)
    return evens_list
print(get_evens([1,2,3,4]))


# Problem 8: Multiples of Five
# Write a function multiples_of_five() that prints out multiples of 5 between 1 and 100 (inclusive).
def multiples_of_five():
    for item in range(1, 101):
        if item % 5 == 0:
            print(item)
multiples_of_five()


# Problem 9: Divisors
# Write a function find_divisors() that takes in an integer n as a parameter that returns a list of all divisors of n.
def find_divisors(n):
    for item in range (1, n + 1):
        if (n % item == 0):
            print(item)
find_divisors(6)


# Problem 10: FizzBuzz
# Write a function fizzbuzz() that takes in an integer n as a parameter and prints the numbers from 1 to n.
# For multiples of 3, print "Fizz" instead of the number.
# For multiples of 5, print "Buzz" instead of the number.
def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
fizzbuzz(13)


# Problem 11: Print the Index
# Write a function print_indices() that takes in an integer list lst as a parameter and prints out the index of each item in the given list.
# Use the function range() to loop through the list indices.
def print_indices(lst):
    for i in range(len(lst)):
        print(i)
lst = [5,1,3,8,2]
print_indices(lst)


# Problem 12: Linear Search
# Write a function linear_search() that takes in a list lst and value target as parameters. 
# The function returns the index of target in lst if found. If target is not found in lst, return -1.
def linear_search(lst, target):
    for i, item in enumerate(lst):
        if item == target:
            return i   
    return -1
print(linear_search([1, 4, 5, 2, 8], 5))        


