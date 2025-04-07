#!/bin/bash

echo "Enter the filename containing usernames:"
read filename

# Check if file exists
if [ ! -f "$filename" ]; then
    echo "File not found!"
    exit 1
fi

while IFS= read -r username; do
    if id "$username" &>/dev/null; then
        echo "User '$username' already exists. Skipping."
    else
        sudo useradd -m "$username"
        echo "User '$username' created successfully."
    fi
done < "$filename"
