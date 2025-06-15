# Problem Set Two

# Problem 1 - Convert Temperature
def convertTemp(celsius: float):
    celsius_final = round(celsius, 2)

    kelvin = celsius_final + 273.15
    fahrenheit = celsius_final * 1.80 + 32.00

    ans = [kelvin, fahrenheit]

    return ans
print(convertTemp(23.00))


# Problem 2 - Average Score
def average(scores: list):
    sum = 0
    for i in scores:
        sum += i
    return sum/len(scores)
print(average([84,73,92,95,88]))


# Problem 3 - Increment by 1
def increment_values(lst: list):
    new_list = []
    for i in lst:
        result = i+1
        new_list.append(result)
    return new_list
print(increment_values([3,5,8,2]))


# Problem 4 - Check for Number
def check_num(lst, num):
    if num in lst:
        return True
    return False
print(check_num([5,2,3,9,10], 9))


# Problem 5 - Missing Number
def missing_number(nums: list):
    sorted_nums = sorted(nums)
    start = min(sorted_nums)
    end = max(sorted_nums)
    for i in range(start, end + 1):
        if i not in sorted_nums:
            print(i)
missing_number([2,4,1,0,5,20])


# Problem 6 - Reverse List
def reverse_list(lst):
    reversed_list = []

    for i in range(1, len(lst) + 1):
        reversed_list.append(lst[-i])
    return reversed_list
print(reverse_list([1,2,3,4,5]))


# Problem 7 - Get Odd Numbers
def get_odds(nums: list):
    odd_list = []

    for i in nums:
        if i % 2 != 0:
            odd_list.append(i)
    return odd_list
print(get_odds([2,5,1,8,6,5]))


# Problem 8 - Multiplication Table
def multiplicationTable(num: int):
    for i in range(1, 11):
        print(num*i)
multiplicationTable(7)


# Problem 9 - Create Number
def list_to_number(digits: list):
    result = ''
    for i in digits:
        result += str(i)
    return int(result)
print(list_to_number([1,0,3]))


# Problem 10 - Move Zeroes
def move_zeroes(nums: list):
    new_list = []
    zero_list = []

    for i in nums:
        if i == 0:
            zero_list.append(i)
        else:
            new_list.append(i)
    return new_list + zero_list
print(move_zeroes([1,0,2,3,0,0,4]))


# Problem 11 - Odd Indices
def print_odd_indices(nums: list):
    for i, item in enumerate(nums):
        if i % 2 != 0:
            print(item)
print_odd_indices([3,4,8,1,5,2])

# Problem 12 - List Occurrences
def find_all_occurrences(lst: list, target: int):
    indices_list = []

    for i in range(len(lst)):
        if lst[i] == target:
            indices_list.append(i)
    return indices_list
print(find_all_occurrences([1,2,6,5,2,1,3,2,2], 2))