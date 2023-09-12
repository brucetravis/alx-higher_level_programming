#!/usr/bin/python3
"""
Adds command line arguments to a Python list and saves it to a JSON file.
"""

import sys
import os.path
import json

# File path for the JSON file
file_path = "add_item.json"

# Initialize an empty list or load existing data from the JSON file
if os.path.exists(file_path):
    with open(file_path, 'r') as json_file:
        my_list = json.load(json_file)
else:
    my_list = []

# Append command-line arguments to the list
for arg in sys.argv[1:]:
    my_list.append(arg)

# Save the updated list to the JSON file
with open(file_path, 'w') as json_file:
    json.dump(my_list, json_file)
