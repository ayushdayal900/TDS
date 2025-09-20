#!/bin/bash

# Loop through all files recursively in current directory and subdirectories
find . -type f | while read -r file; do
  dir=$(dirname "$file")
  base=$(basename "$file")
  
  # Rename file by shifting digits: 0→1, 1→2, ..., 9→0
  newbase=$(echo "$base" | perl -pe 'tr/0123456789/1234567890/')
  
  # Only rename if filename changes
  if [[ "$base" != "$newbase" ]]; then
    mv "$dir/$base" "$dir/$newbase"
  fi
done

