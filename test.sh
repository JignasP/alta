# alta
# Copyright © 2023, Jignas Paturu

#!/bin/bash
file_array=(/etc/NetworkManager/system-connections/*.nmconnection)

i=0
list=()
pass=()
for file in "${file_array[@]}"
do
  temp=$(echo "$file:" | cut -d'/' -f5 | cut -d'.' -f1)
  list+=("$temp")
  temp=$(grep "psk=" "$file" | cut -d= -f2)
  pass+=("$temp")
  i=$((i+1))
done
printf '%s\n'
max_width_username=$(printf '%s\n' "${list[@]}" | awk '{ print length }' | sort -rn | head -n 1)
max_width_password=$(printf '%s\n' "${pass[@]}" | awk '{ print length }' | sort -rn | head -n 1)


printf "%-${max_width_username}s  %-${max_width_password}s\n" "username" "password"
printf "%-${max_width_username}s  %-${max_width_password}s\n" "________" "________"

for ((i=0; i<${#list[@]}; i++)); do
  printf "%-${max_width_username}s  %-${max_width_password}s\n" "${list[$i]}" "${pass[$i]}"
done
