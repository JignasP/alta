#!/bin/bash

# Get the file names from the specified directory into an array
file_array=(/etc/NetworkManager/system-connections/*.nmconnection)

# Loop through the array and search for 'psk=' in each file
for file in "${file_array[@]}"
do
  echo "$file:"| cut -d'/' -f5| cut -d'.' -f1
  grep "psk=" "$file" | cut -d= -f2
  echo ""
done
