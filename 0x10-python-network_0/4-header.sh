#!/bin/bash

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Use curl to send a GET request with a custom header and display the body
curl -s -H "X-School-User-Id: 98" "$1"
