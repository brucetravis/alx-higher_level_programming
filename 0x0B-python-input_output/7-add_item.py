#!/usr/bin/python3
import sys
from os import path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

if __name__ == "__main__":
    # Check if the JSON file exists, and if not, create an empty list
    json_filename = "add_item.json"
    if path.exists(json_filename):
        my_list = load_from_json_file(json_filename)
    else:
        my_list = []

    # Add command-line arguments to the list
    for arg in sys.argv[1:]:
        my_list.append(arg)

    # Save the updated list to the JSON file
    save_to_json_file(my_list, json_filename)
