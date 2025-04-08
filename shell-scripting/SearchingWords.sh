#!/bin/bash

echo "Enter filename:"
read file
echo "Enter word to search:"
read word

if [ -f "$file" ]; then
    grep --color=always -n "$word" "$file"
else
    echo "File not found."
fi

