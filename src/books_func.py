import csv
import json


def sort_books(input_file, output_file, selected_keys):
    data = []
    with open(input_file, 'r') as books:
        read_file = csv.DictReader(books)
        for row in read_file:
            data.append(row)

    selected_data = []
    for item in data:
        selected_item = {key: item[key] for key in selected_keys if key in item}
        selected_data.append(selected_item)

    with open(output_file, 'w') as f:
        json.dump(selected_data, f, indent=4)
