import csv
import json

from files import CSV_FILE_PATH
from files import JSON_FILE_PATH
from src.users_func import select_values_and_create_new_json
from src.books_func import sort_books



# # Select from users needed values and make a new list
# input_file_json = JSON_FILE_PATH
file_output_users = "output_users.json"
# selected_keys_users = ["name", "gender", "address", "age", "address"]
#
# select_values_and_create_new_json(input_file_json, file_output_users, selected_keys_users)
#
#
# # Convert books to json
# input_file_csv = CSV_FILE_PATH
file_output_books = "output_books.json"
# selected_keys_books = ["Title", "Author", "Pages", "Genre"]
#
# sort_books(input_file_csv, file_output_books, selected_keys_books)

with open(file_output_users, 'r') as users_file:
    users_data = json.load(users_file)

with open(file_output_books, 'r') as books_file:
    books_data = json.load(books_file)

result = []


for user, book in zip(users_data, books_data):
    books = len(books_data)
    if books > 0:
        new_user = {
            "name": user["name"],
            "gender": user["gender"],
            "address": user["address"],
            "age": user["age"],
            "books": [
                {
                    "Title": book["Title"],
                    "Author": book["Author"],
                    "Pages": book["Pages"],
                    "Genre": book["Genre"]
                }
            ]
        }
        result.append(new_user)
        books -= 1

with open('result.json', 'w') as result_file:
    json.dump(result, result_file, indent=4)
