#!/bin/bash

files=$(sudo /etc/NetworkManager/system-connections/)

for file in $files
do
    echo "$file"
done
