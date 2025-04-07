#!/bin/bash

echo "Enter filename to read:"
read filename

if [ -f "$filename" ]; then
    while IFS= read -r line; do
        echo "$line"
    done < "$filename"
else
    echo "File does not exist."
fi
