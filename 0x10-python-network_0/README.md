#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
