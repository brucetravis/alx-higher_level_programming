#!/usr/bin/python3
import urllib.request
import sys

if len(sys.argv) == 2:
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        # Check if the header is present
        if 'X-Request-Id' in response.headers:
            request_id = response.headers['X-Request-Id']
            print(request_id)
