#!/bin/bash

# Check if URL is provided as argument
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send request to the URL, follow redirects, and display the size of the body in bytes
size=$(curl -sI "$1" | grep -i Content-Length | awk '{print $2}')
echo "$size"
