#!/bin/bash

# Check if URL argument is provided
if [ -z "$1" ]; then
    # Print usage message if URL is not provided
    echo "Usage: $0 <URL>"
    exit 1
fi

# Use curl to send a request and display the size of the body in bytes without headers
curl -s "$1" | wc -c
