#!/usr/bin/python3
import requests
import sys

if len(sys.argv) == 3:
    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}
    response = requests.post(url, data=payload)

    print("Your email is:", response.text)
