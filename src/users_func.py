import json


def select_values_and_create_new_json(input_file, output_file, selected_keys):
    with open(input_file, 'r') as f:
        data = json.load(f)

    selected_data = []
    for item in data:
        selected_item = {key: item[key] for key in selected_keys if key in item}
        selected_data.append(selected_item)

    with open(output_file, 'w') as f:
        json.dump(selected_data, f, indent=4)

