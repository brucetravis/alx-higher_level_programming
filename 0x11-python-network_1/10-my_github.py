#!/usr/bin/python3
import requests
import sys

if len(sys.argv) == 3:
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))

    try:
        json_response = response.json()
        print(json_response.get('id', 'None'))
    except ValueError:
        print("None")
