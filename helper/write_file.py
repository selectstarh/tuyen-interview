import json

def write_file(file_name, result):
    with open(file_name, 'w') as json_file:
        json_file.write(json.dumps(result))
