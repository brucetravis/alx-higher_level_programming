#!/bin/bash

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Use curl to send a POST request with parameters and display the body
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
