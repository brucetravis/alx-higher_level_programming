#!/bin/bash

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Use curl to send a request and display only the status code
curl -s -o /dev/null -w "%{http_code}" "$1"
