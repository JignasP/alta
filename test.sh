#!/bin/bash

b=/etc/NetworkManager/system-connections/<name>.nmconnection
value=`cat $b`
echo "$value"

files=$(sudo ls /etc/NetworkManager/system-connections/)
b=""

for file in $files
do
    a="$a $file $'\n'"
    

#    echo "$file"
done
echo "$a"

