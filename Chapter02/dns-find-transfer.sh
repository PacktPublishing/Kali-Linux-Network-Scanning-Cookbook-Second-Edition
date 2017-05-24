#!/bin/bash

if [ ! $1 ]; then 
echo "Usage: #./dns-find-transfer.sh <domain>"; 
exit; 
fi


for server in $(host -t ns $1 |cut -d" " -f4);do
printf $server | sed 's/.$//'
host -l $1 $server |grep "Address: " | cut -d: -f2 | sed 's/...$//'
done

