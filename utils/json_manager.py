import json


def save_to_json(data, file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)


def read_json(json_path):
    with open(json_path, "r") as jsonFile:
        data = json.load(jsonFile)

    return data
