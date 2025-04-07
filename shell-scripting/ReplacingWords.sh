#!/bin/bash

echo "Enter filename:"
read file
echo "Enter word to replace:"
read old
echo "Enter new word:"
read new

if [ -f "$file" ]; then
    sed -i "s/$old/$new/g" "$file"
    echo "Replaced all occurrences of '$old' with '$new'."
else
    echo "File not found."
fi
