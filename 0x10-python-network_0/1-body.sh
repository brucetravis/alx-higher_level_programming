#!/bin/bash

# Check if URL argument is provided
if [ -z "$1" ]; then
    # Print usage message if URL is not provided
    echo "Usage: $0 <URL>"
    exit 1
fi

# Use curl to send a GET request and display "Route 2" if the status code is 200
curl -s -o /dev/null -w "%{http_code}" "$1" | {
    read status
    if [ "$status" -eq 200 ]; then
        # Output "Route 2"
        echo "Route 2"
    fi
}
