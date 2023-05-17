import sys
import os
import json
import pathlib

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

curr_dir = str(pathlib.Path().resolve())
db_file_path = curr_dir + '/text.json'

from helper.read_file import read_file

text = read_file(db_file_path)

indexing_db = json.loads(text)

print(indexing_db)