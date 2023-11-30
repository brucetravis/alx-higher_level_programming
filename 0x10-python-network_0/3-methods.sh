#!/bin/bash

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Use curl to send an OPTIONS request and display allowed methods
curl -sI -X OPTIONS "$1" | grep -i Allow | awk '{print $2}'
