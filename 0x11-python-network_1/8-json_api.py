#!/usr/bin/python3
import requests
import sys

if len(sys.argv) == 2:
    letter = sys.argv[1]
else:
    letter = ""

url = "http://0.0.0.0:5000/search_user"
payload = {'q': letter}

response = requests.post(url, data=payload)

try:
    json_response = response.json()
    if json_response:
        print("[{}] {}".format(json_response['id'], json_response['name']))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
