# Problem Set One

# Problem 1: Print List
def print_list(lst):
    for item in lst:
        print(item)
print_list(["squirtle", "gengar", "charizard", "pikachu"])


# Problem 2: Print Doubled List
def doubled(lst):
    if not lst:
        return None
    for item in lst:
        print(item * 2)
doubled(lst = [1,2,3])


# Problem 3: Return Doubled List
def doubled(lst):
    new_list = []
    if len(lst) == 0:
        return None
    for i in lst:
        result = i*2
        new_list.append(result)
    return new_list
print(doubled([1,2,3]))


# Problem 4: Flip Signs
def flip_sign(lst):
    flipped_lst = []
    for item in lst:
        result = item * -1
        flipped_lst.append(result)
    return flipped_lst
print(flip_sign([1,-2,-3,4]))


# Problem 5: Max Difference
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

# Problemn 6: Below Threshold
def count_less_than(numbers, threshold):
    less_than_list = []

    for i in numbers:
        if i < threshold:
            less_than_list.append(i)
    return less_than_list
count_less_than([12,8,2,4,4,10], 5)

# Problem 7: Evens List
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
def multiples_of_five():
    for item in range(1, 101):
        if item % 5 == 0:
            print(item)
multiples_of_five()


# Problem 9: Divisors
def find_divisors(n):
    for item in range (1, n + 1):
        if (n % item == 0):
            print(item)
find_divisors(6)


# Problem 10: FizzBuzz
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
def print_indices(lst):
    for i in range(len(lst)):
        print(i)
lst = [5,1,3,8,2]
print_indices(lst)


# Problem 12: Linear Search
def linear_search(lst, target):
    for i, item in enumerate(lst):
        if item == target:
            return i   
    return -1
print(linear_search([1, 4, 5, 2, 8], 5))        


