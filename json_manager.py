import json

def save_to_json(data, file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)