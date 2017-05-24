#! /bin/bash

if [ ! $1 ]; then echo "Usage: #./script <file>"; exit; fi

file=$1

for x in $(grep open $file | grep 80 | cut -d " " -f 2); 
do 
	echo "Nikto scanning the following host: $x"	
	nikto -h $x -F text -output /tmp/nikto-scans/$x.txt
done
