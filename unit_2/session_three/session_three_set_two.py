# Problem Set Two

# Problem 1: Is Monotonic
def is_monotonic(nums):
    # pointer
    prev_element_inc = nums[0]
    prev_element_dec = nums[0]

    mono_inc = 0
    mono_dec = 0

    if not nums:
        return False

    for i in range(1, len(nums)):
        if nums[i] >= prev_element_inc:
            prev_element_inc = nums[i]
            mono_inc += 1
        if nums[i] <= prev_element_dec:
            prev_element_dec = nums[i]
            mono_dec += 1

    if mono_inc == len(nums) - 1:
        return True
    elif mono_dec == len(nums) - 1:
        return True
    else:
        return False

nums1 = [1,2,2,3,10]
print(is_monotonic(nums1))

nums2 = [12,9,8,3,1]
print(is_monotonic(nums2))

nums3 = [1,1,1]
print(is_monotonic(nums3))

nums4 = [1,9,8,3,5]
print(is_monotonic(nums4))

# Problem 2: Student Directory
def student_directory(student_names):
    stu_dictionary = {}
    count = 1

    if not student_names:
        return None

    for student in student_names:
        stu_dictionary[student] = count
        count += 1
    
    return stu_dictionary

student_names = ["Ada Lovelace", "Tu Youyou", "Mae Jemison", "Rajeshwari Chatterjee", "Alan Turing"]

print(student_directory(student_names))


# Problem 3: Dictionary Description
def get_description(info: dict, keys: list):
    for key in keys:
        if key not in info:
            print(None)
        else:
            print(info[key])

info = {"name": "Tom", "age": "30", "occupation": "engineer"}
keys = ["name", "occupation", "salary"]
get_description(info, keys)


# Problem 4: Sum Even Values
def sum_even_values(int_dict: dict):
    sum = 0

    for key in int_dict:
        sum += int_dict[key]
    return sum

dictionary = {"a": 4, "b": 1, "c": 2, "d": 8, }
print(sum_even_values(dictionary))


# Problem 5: Merge Catalogs
def merge_catalogs(catalog1: dict, catalog2: dict):
    for key, value in catalog2.items():
        catalog1[key] = value
    return catalog1

catalog1 = {"apple": 1.0, "banana": 0.5}
catalog2 = {"banana": 0.75, "cherry": 1.25}

print(merge_catalogs(catalog1, catalog2))


# Problem 6: Items to Restock
def get_items_to_restock(products: dict, restock_threshold: int):
    restock_list = []

    if not products:
        return []
    for key in products:
        if products[key] < restock_threshold:
            restock_list.append(key)
    return restock_list

products = {"Product1": 10, "Product2": 2, "Product3": 5, "Product4": 3}
restock_threshold = 5

print(get_items_to_restock(products, restock_threshold))


# Problem 7: Best Movie Genre
def most_popular_genre(movies: list):
    genre_count_n_score = {}

    for movie in movies:
        genre = movie["genre"]
        rating = movie["rating"]

        if genre not in genre_count_n_score:
            genre_count_n_score[genre] = [rating, 1]
        else:
            genre_count_n_score[genre][0] += rating
            genre_count_n_score[genre][1] += 1

    best_genre = ""
    best_avg = 0

    for genre, (total_rating, count) in genre_count_n_score.items():
        avg_rating = total_rating / count
        if avg_rating > best_avg:
            best_avg = avg_rating
            best_genre = genre

    return best_genre, round(best_avg, 1)


movies = [
    {"title": "Inception",
     "genre": "Science Fiction",
     "rating": 8.8
    },
    {"title": "The Matrix", 
     "genre": "Science Fiction",
     "rating": 8.7
    },
    {"title": "Pride and Prejudice", 
     "genre": "Romance",
     "rating": 7.8
    },
    {"title": "Sense and Sensibility", 
     "genre": "Romance",
     "rating": 7.7
    }
]

print(most_popular_genre(movies))


# Problem 8: Quality Control
def quality_control(product_scores: dict, threshold: int):
    pass_fail_dict = {}

    for key in product_scores:
        if product_scores[key] < threshold:
            pass_fail_dict[key] = "fail"
        else:
            pass_fail_dict[key] = "pass"
    return pass_fail_dict

scores = {"x0123": 75, "x0124": 40, "x0125": 90, "x0126": 55}
threshold = 60

print(quality_control(scores, threshold))