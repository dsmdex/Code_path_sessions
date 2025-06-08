# Problem Set Two

# Problem 1 - Hello User!
def greet_user(name):
    print(f"Hello {name}")

greet_user("derek")

# Problem 2 - Calculate Difference
def difference(a,b):
    return b-a
print(difference(3,8))

# Problem 3 - List Concatenation
def concatenate_list(nums):
    ans = []
    n = len(nums)
    for i in range(n):
        ans.append(nums[i])
    for i in range(n):
        ans.append(nums[i])
    return ans
print(concatenate_list([1,2,3])) 

# Problem 4 - Sleep Assessment
def sleep_assessment(hours: int):
    if hours < 8:
        print("Oof, go back to bed!")
    elif hours >= 8 and hours <= 10:
        print("You got a good night's rest!")
    elif hours > 10:
        print("You're a sleepy prodigy!")
sleep_assessment(10)
sleep_assessment(4)
sleep_assessment(12)
sleep_assessment(9)

# Problem 5 - Calculate the TIp
def calculate_tip(bill: float, service_quality: str):
    if service_quality == "poor":
        return .10*bill
    elif service_quality == "average":
        return .15*bill
    elif service_quality == "excellent":
        return bill*.20
    else:
        return None
tip1 = calculate_tip(44.53, "average")
print(tip1)
tip2 = calculate_tip(44.53, "poor")
print(tip2)
tip3 = calculate_tip(44.53, "excellent")
print(tip3)

# Problem 6 - Rock, Paper, Scissors
def rock_paper_scissors(player1, player2):
    # player one winning scenarios
    if player1 == "rock" and player2 == "scissors":
        print("Player 1 wins!")
    elif player1 == "scissors" and player2 == "paper":
        print("Player 1 wins!")
    elif player1 == "paper" and player2 == "rock":
        print("Player 1 wins!")
    # both tie
    elif player1 == player2:
        print("It's a tie!")
    # player two winning secnarios
    else:
        print("Player 2 wins!")
rock_paper_scissors("rock", "rock")
rock_paper_scissors("scissors", "rock")
rock_paper_scissors("scissors", "paper")
rock_paper_scissors("rock", "paper")
rock_paper_scissors("paper", "rock")

# Problem 7 - Unscramble and Divide
def halve_lst(lst):
    result = []
    for i in lst:
        halved = int(i/2)
        result.append(halved)
    return result
print(halve_lst([2,4,6,8]))

# Problem 8 - Above the Treshold
def above_threshold(lst, threshold):
    new_list = []
    for i in lst:
        if i > threshold:
            new_list.append(i)
    return new_list
lst = [8,2,13,11,4,10,14]
new_lst = above_threshold(lst, 10)
print(new_lst)

# Problem 9 - Countdown
def countdown(m, n):
    for i in range(m, n-1, -1):
        print(i)
countdown(5,1)

# Problem 10 - Length of List
def power(base, exponent):
    return base**exponent
print(power(2,5))

# Problem 11: Length of List
def list_length(lst):
    size = 0
    while lst:
        size += 1
        lst.pop()
    return size
lst = [2,4,6,8,10]
length = list_length(lst)
print(length)

# Problem 12: Calculate Factorial
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(3))

# Problem 13: Calculate the Squares
def squares(nums: list):
    new_list = []
    for i in nums:
        squared = i*i
        new_list.append(squared)
    return new_list
print(squares([1,2,3,4]))

# Problem 14: Multiply List
def multiply_list(lst: list, multiplier: int):
    new_list = []
    for i in lst:
        result = i*multiplier
        new_list.append(result)
    return new_list
print(multiply_list([1,2,3],3))

# Problem 15 - Count Evans
def count_evens(lst: list):
    num_of_even = 0
    for i in lst:
        if i % 2 == 0:
            num_of_even += 1
    return num_of_even
lst1 = [1,5,7,9]
count1 = count_evens(lst1)
print(count1)

lst2 = [2,4,6,8]
count2 = count_evens(lst2)
print(count2)