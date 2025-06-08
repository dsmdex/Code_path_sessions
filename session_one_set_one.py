# Problem Set One

# Problem 1 - Hello World!
def hello_world():
    print("Hello World!")
hello_world()

# Problem 2 - Today's Mood
def todays_mood():
    mood = "smiley emoji"
    print(f"Today's mood: {mood}")
todays_mood()

# Problem 3 - Lunch Menu
def print_menu(menu):
    print(f"Lunch today is: {menu}")
print_menu("soup")

# Problem 4 - Sum of two Integers
def sum (a,b):
    return a+b
print(sum(1,2))

# Problem 5 - Product of two Integers
def product(a,b):
    return a*b
print(product(22,7))

# Problem 6 - Classify Age
def classify_age(age):
    if age < 18:
        return "child"
    else:
        return "adult"
print(classify_age(17))
print(classify_age(18))

# Problem 7 - What time is it?
def what_time_is_it(hour):
    if hour == 2:
        return "taco time"
    elif hour == 12:
        return "peanut butter jeally time"
    else:
        return "nap time"
time = what_time_is_it(2)
print(time)
time = what_time_is_it(7)
print(time)
time = what_time_is_it(12)
print(time)

# Problem 8 - Blackjack
def blackjack(score):
    if score == 21:
        print("Blackjack!")
    elif score > 21:
        print("Bust!")
    elif score >= 17 and score < 21:
        print("Nice Hand!")
    elif score < 17:
        print("Hit Me!")

blackjack(24)
blackjack(19)
blackjack(21)
blackjack(10)

# Problem 9 - First Item
def get_first(lst):
    if lst:
        return lst[0]
    else:
        return
print(get_first([1,2,3,4,5]))

# Problem 10 - Last item
def get_last(lst):
    if lst:
        return lst[-1]
    return
print(get_last([1,2,3,4]))

# Problem 11 - Counter
def counter(stop):
    for i in range(1, stop+1):
        print(i)
counter(10)

# Problem 12 - Sum of 1 to 10
def sum_ten():
    sum = 0
    for i in range(1,11):
        sum += i
    return sum
print(sum_ten())

# Problem 13 - Total Sum
def sum_positive_range(stop):
    sum = 0
    for i in range(1, stop+1):
        sum += i
    return sum

# Problem 14 - Total Sum in Rnage
def sum_range(start, stop):
    sum = 0
    for i in range(start, stop+1):
        sum += i
    return sum
print(sum_range(3,9))

# Problem 15 - Negative Numbers
def print_negative(lst):
    for i in lst:
        if i < 0:
            print(i)
print_negative([3,-2,2,1,-5])