#!/bin/bash

echo "Enter filename:"
read file

if [ -f "$file" ]; then
    lines=$(wc -l < "$file")
    words=$(wc -w < "$file")
    chars=$(wc -m < "$file")
    echo "Lines: $lines"
    echo "Words: $words"
    echo "Characters: $chars"
else
    echo "File not found."
fi
