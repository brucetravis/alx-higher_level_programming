#!/bin/bash

# Check if both URL and filename arguments are provided
if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Usage: $0 <URL> <JSON_FILE>"
    exit 1
fi

# Read the JSON content from the file
json_content=$(cat "$2")

# Use curl to send a JSON POST request and display the body
response=$(curl -s -X POST -H "Content-Type: application/json" -d "$json_content" "$1")

# Check if the response contains "Not a valid JSON"
if [[ "$response" == *"Not a valid JSON"* ]]; then
    echo "Not a valid JSON"
else
    echo "$response"
fi
