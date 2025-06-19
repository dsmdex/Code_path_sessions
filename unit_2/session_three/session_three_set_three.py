# Problem Set Three

# Problem 1: Mountain Peak
# Mountain list is defined as a list that has at least three elements, where there exists
#   some index (i) with 0 < i < len(lst) - 1, such that every element is less than the element
#       after it. 
# Given a list as a parameter, write a function that returns the highest index peak
def peak_index_in_mountain_list(lst: list):
    highest_index = 0

    for i in range(1, len(lst)):
        previous_element = lst[i-1]
        if lst[i] > previous_element:
            highest_index = i
    return highest_index

print(peak_index_in_mountain_list([0,3,8,0]))

# Problem 2: Build Inventory
# Write a function build_inventory() that takes in a list of product_names and a corresponding list 
# of product_prices as parameters. The function returns a dictionary representing the inventory of a 
# small store. Each product name in product_names should be a key in the dictionary and the 
# corresponding value should be the item price.
def build_inventory(product_names: list, product_prices: list):
    product_dict = {}

    for i in range(len(product_names)):
        product_dict[product_names[i]] = product_prices[i]
    return product_dict

product_names = ["Apple", "Banana", "Orange"]
product_prices = [0.99, 0.50, 0.75]
print(build_inventory(product_names, product_prices))

# Problem 3 - Update or Warn
# Write a function update_or_warn() that takes in a dictionary records,
#  a key item, and a new value update_value as parameters. The function updates the value of item in records with update_value if item exists. If item does not exist, it should print "<item> not found!".
def update_or_warn(records: dict, item: int, update_value: int):
    if item not in records:
        return(f"{item} not found!")
    else:
        records[item] = update_value
    return records

records = {"apple": 1, "banana": 2, "orange": 3}
print(update_or_warn(records, "banana", 5))

print(update_or_warn(records, "grape", 4))


# Problme 4 - Attendance Rate 
# Write a function attendance_rate() that takes in a dictionary attendance_list as a parameter. 
# The function maps student names to their attendance status ("Present" or "Absent"), and returns 
# the percentage of students who are present.
def attendance_rate(attendance_list: list):
    students_present = 0

    for key in attendance_list:
        if attendance_list[key] == "Present":
            students_present += 1
    return str((students_present/len(attendance_list))*100) + "%"

attendance_list = {
    "Bluey": "Present", 
    "Bingo": "Absent", 
    "Snickers": "Present", 
    "Winton": "Absent"
}

print(attendance_rate(attendance_list))

# Problem 5 - Average Book Ratings
# Write a function average_book_ratings(), that calculates the average rating for each
#  book in a collection. The function takes one parameter: a dictionary book_ratings where
#  each key-value pair represents a book title and a list of its ratings, respectively. 
# Ratings are represented as floating-point numbers. The function should return a new 
# dictionary with book titles as keys and their average rating.
def average_book_ratings(book_ratings):
    average_book_rating = {}

    for book in book_ratings:
        book_avg = 0
        score_count = 0
        for rating in book_ratings[book]:
            book_avg += rating
            score_count += 1 
        book_avg = round((book_avg/score_count), 1)
        average_book_rating[book] = book_avg
        book_avg = 0
    return average_book_rating

book_ratings = {
    "The Great Gatsby": [4.5, 3.0, 5.0],
    "To Kill a Mockingbird": [4.8, 5.0, 4.0, 4.9]
}

print(average_book_ratings(book_ratings))

# Problem 6 - Odd Keys Even Values
# Write a function odd_keys_even_values() that takes in dictionary as a parameter, 
# a dictionary with integer keys and values. The function returns a list of keys 
# that are odd where their corresponding values are even.
def odd_keys_even_values(dictionary: dict):
    odd_even_list = []

    for key, value in dictionary.items():
        if not key % 2 == 0 and value % 2 == 0:
            odd_even_list.append(key)
    return odd_even_list 

dictionary = {1: 2, 2: 6, 3: 5, 4: 4, 5: 8}
final_list = odd_keys_even_values(dictionary)
print(final_list)


# Problem 7 - Best Team
# You're developing an analytics tool for a sports league. Your task is to write a function
#  named team_with_best_average_score() that returns the team with the highest average score
#  over a season. The function should accept a list of dictionaries named games as a parameter.
# Each dictionary represents data from a game, including the "team_name", and the "score" they 
# achieved in that game. The function calculates the average score for each team across all games
#  and returns the team with the highest average score.
def team_with_best_average_score(games: list):
    total_score = {}
    
    for dicti in games:
        if dicti["team_name"] not in total_score:
            total_score[dicti["team_name"]] = [dicti["score"], 1]
        else:
            total_score[dicti["team_name"]][0] += dicti["score"]
            total_score[dicti["team_name"]][1] += 1

    avg_score = {}

    avg = 0
    for team in total_score:
        avg = total_score[team][0]/total_score[team][1]
        avg_score[team] = avg
        avg = 0
    
    highest_score = 0
    team_with_highest_score = ''

    for key in avg_score:
        if avg_score[key] > highest_score:
            highest_score = avg_score[key]
            team_with_highest_score = key

    return team_with_highest_score
 
games = [
    {"team_name": "Lions",
     "score": 23
    },
    {"team_name": "Tigers", 
     "score": 30
    },
    {"team_name": "Lions", 
     "score": 27
    },
    {"team_name": "Bears", 
     "score": 20
    },
    {"team_name": "Tigers", 
     "score": 24
    },
    {"team_name": "Bears", 
     "score": 22
    }
]

print(team_with_best_average_score(games))


# Problem 8 - First Unique Items
# Write a function find_unique_items() that takes two lists list_a and list_b as parameters. 
# The function identifies unique items from the lists and returns a dictionary with the items 
# as keys and a boolean value as the value indicating whether the item is unique to the first 
# list (True) or not (False).
def find_unique_items(list_a: list, list_b: list):
    unique_dict = {}
    
    for i in range(len(list_a)):
        if list_a[i] not in list_b:
            unique_dict[list_a[i]] = True
        if list_b[i] not in list_a:
            unique_dict[list_b[i]] = False

    return unique_dict

list_a = ["apple", "banana", "carrot"]
list_b = ["apple", "banana", "date"]

print(find_unique_items(list_a, list_b))
 