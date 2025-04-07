#!/bin/bash

echo "Enter filename to backup:"
read file

if [ -f "$file" ]; then
    cp "$file" "$file.bak"
    echo "Backup created: $file.bak"
else
    echo "File not found."
fi
