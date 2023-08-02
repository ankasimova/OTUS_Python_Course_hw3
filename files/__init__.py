import os

FILES_DIR = os.path.dirname(__file__)

def files_path(file_name):
    return os.path.join(FILES_DIR, file_name)

JSON_FILE_PATH = files_path(file_name='users.json')
CSV_FILE_PATH = files_path(file_name='books.csv')

