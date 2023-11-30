#!/bin/bash

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Use curl to send a GET request and display the body if status code is 200
curl -s -o /dev/null -w "%{http_code}" "$1" | {
    read status
    if [ "$status" -eq 200 ]; then
        curl -s "$1"
    fi
}
