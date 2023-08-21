import json
import pytest

from files import JSON_FILE_PATH, CSV_FILE_PATH
from result import RESULT_FILE_PATH


#Check the result file contains all users from the basic file
def test_users_count():
    with open(JSON_FILE_PATH, 'r') as users_file:
        users_data = json.load(users_file)
        return users_data
        users_count = len(read_json)

    with open(RESULT_FILE_PATH, 'r') as result_file:
        result_data = json.load(result_file)
        result_users_count = len(result_data)

    assert users_count == result_users_count


#Check all books are shared between users
def test_books_count():
    with open(CSV_FILE_PATH, 'r') as books_file:
        books_count = sum(1 for line in books_file) - 1

    with open(RESULT_FILE_PATH, 'r') as result_file:
        result_data = json.load(result_file)

    result_total_books = 0

    for user in result_data:
        if 'books' in user:
            result_total_books += len(user['books'])

    assert books_count == result_total_books


#Check the structure of the result file is correct
def test_result_file_struct():
    with open(RESULT_FILE_PATH, 'r') as result_file:
        result_data = json.load(result_file)
        required_keys = ['name', 'gender', 'address', 'age', 'books']
        for dict in result_data:
            assert all(key in dict for key in required_keys)


