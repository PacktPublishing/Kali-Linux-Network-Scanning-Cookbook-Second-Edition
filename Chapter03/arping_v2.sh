#!/bin/bash

if [ "$#" -ne 1 ]; then
echo "Usage - ./arping.sh [input file]"
echo "Example - ./arping.sh iplist.txt"
echo "Example will perform an ARP scan of all IP addresses defined in 
iplist.txt"
exit
fi

file=$1

for addr in $(cat $file); do
arping -c 1 $addr | grep "bytes from" | cut -d " " -f 5 | cut -d "(" -f 2 | cut -d ")" -f 1 &
done
