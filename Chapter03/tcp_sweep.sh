#!/bin/bash

if [ "$#" -ne 1 ]; then
echo "Usage - ./tcp_sweep.sh [/24 network address]"
echo "Example - ./tcp_sweep.sh 172.16.36.0"
echo "Example will perform a tcp ping sweep of the 172.16.36.0/24
network and output to an output.txt file"
exit
fi

prefix=$(echo $1 | cut -d '.' -f 1-3)

for addr in $(seq 1 254); do
hping3 $prefix.$addr -c 1 >> handle.txt;
done

grep len handle.txt | cut -d " " -f 2 | cut -d "=" -f 2 >> output.txt
rm handle.txt
