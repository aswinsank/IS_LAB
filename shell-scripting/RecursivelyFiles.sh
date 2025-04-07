#!/bin/bash

echo "Enter directory:"
read dir
echo "Enter filename pattern (e.g., *.txt):"
read pattern

if [ -d "$dir" ]; then
    find "$dir" -type f -name "$pattern"
else
    echo "Directory not found."
fi
