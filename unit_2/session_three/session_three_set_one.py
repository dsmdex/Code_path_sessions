# Problem Set One

# Problem One: Subsequence
def is_subsequence(lst, sequence):
    # pointer
    sequence_index = 0

    for num in lst:
        if sequence[sequence_index] == num:
            sequence_index += 1
        if sequence_index == len(sequence):
            return True
    return False
    
lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(is_subsequence(lst, sequence))


# Problem 2: Create a Dictionary
def create_dictionary(keys, values):
    new_dict = {}
    for i in range(len(keys)):
        new_dict[keys[i]] = values[i]
    return new_dict

keys = ["peanut", "dragon", "star", "pop", "space"]
values = ["butter", "fly", "fish", "corn", "ship"]
print(create_dictionary(keys, values))


# Problem 3: Print Pair
def print_pair(dict, target):
    if target in dict:
        print(f"Key: {target}\nValue: {dict[target]}")
    else:
        print("That pair does not exist")

dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print_pair(dictionary, "patrick")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")


# Problem 4: Keys Versus Values
def keys_v_values(dicti):
    sum_of_keys = 0
    sum_of_values = 0

    for key, value in dicti.items():
        sum_of_keys += key
        sum_of_values += value
    if sum_of_keys > sum_of_values:
        print("keys")
    elif sum_of_keys < sum_of_values:
        print("values")
    else:
        print("the keys are equal")

dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
greater_sum = keys_v_values(dictionary1)

dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
greater_sum = keys_v_values(dictionary2)


# Problem 5: Restock Inventory
def restock_inventory(current_inventory, restock_list):
    for key, value in restock_list.items():
        if key not in current_inventory:
            current_inventory[key] = value
        current_inventory[key] += value
    return current_inventory

current_inventory = {
    "apples": 30,
    "bananas": 15,
    "oranges": 10
}

restock_list = {
    "oranges": 20,
    "apples": 10,
    "pears": 5
}

print(restock_inventory(current_inventory, restock_list))


# Problem 6: Calculate GPA
def calculate_gpa(report_card):
    gpa = 0
    grade_score = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}
    for grade in report_card.values():
        gpa += int(grade_score[grade])
    return gpa/len(report_card)

report_card = {"Math": "A", "Science": "C", "History": "A", "Art": "B", "English": "B", "Spanish": "A"}
print(calculate_gpa(report_card))


# Problem 7: Best Book
def highest_rated(books):
    highest_rated = books[0]

    for dicti in books:
        if dicti["rating"] > highest_rated["rating"]:
            highest_rated = dicti
    print(highest_rated)

books = [
    {"title": "Tomorrow, and Tomorrow, and Tomorrow",
     "author": "Gabrielle Zevin",
     "rating": 4.18
    },
    {"title": "A Fortune For Your Disaster",
     "author": "Hanif Abdurraqib",
     "rating": 4.47
    },
    {"title": "The Seven Husbands of Evenlyn Hugo",
     "author": "Taylor Jenkins Reid",
     "rating": 4.40
    }
]

highest_rated(books)


# Problem 8: Index-Value Map
def index_to_value_map(lst):
    dicti = {}
    for index, element in enumerate(lst):
        dicti[index] = element
    print(dicti)

lst = ["apple", "banana", "cherry"]

index_to_value_map(lst)

