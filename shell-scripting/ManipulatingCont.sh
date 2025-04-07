#!/bin/bash

echo "Enter filename:"
read file

if [ -f "$file" ]; then
    echo "Choose operation: (1) Uppercase (2) Lowercase (3) Append"
    read op
    case $op in
        1) tr '[:lower:]' '[:upper:]' < "$file" ;;
        2) tr '[:upper:]' '[:lower:]' < "$file" ;;
        3) 
            echo "Enter text to append:"
            read text
            echo "$text" >> "$file"
            echo "Text appended."
            ;;
        *) echo "Invalid option." ;;
    esac
else
    echo "File not found."
fi
