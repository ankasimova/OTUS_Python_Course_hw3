from files import CSV_FILE_PATH, JSON_FILE_PATH
from csv import DictReader
import json



with open(JSON_FILE_PATH, 'r') as users_file:
    new_users = []
    for user in json.load(users_file):
        new_users.append(
            {
                "name": user["name"],
                "gender": user["gender"],
                "address": user["address"],
                "age": user["age"],
                "books": []
            }
        )


with open(CSV_FILE_PATH, 'r') as books_file:
    new_books = []
    for book in list(DictReader(books_file)):
        new_books.append(
            {
                "title": book["Title"],
                "author": book["Author"],
                "pages": book["Pages"],
                "genre": book["Genre"]
            }
        )

while new_books:
    for user in new_users:
        if len(new_books) > 0:
            user["books"].append(new_books.pop())


with open("result.json", "w") as result_file:
    result_file.write(json.dumps(new_users, indent=4))

