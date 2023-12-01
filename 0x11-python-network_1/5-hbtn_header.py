#!/usr/bin/python3
import requests
import sys

if len(sys.argv) == 2:
    url = sys.argv[1]

    response = requests.get(url)
    
    # Check if the header is present
    if 'X-Request-Id' in response.headers:
        request_id = response.headers['X-Request-Id']
        print(request_id)
