#! /bin/bash

if [ ! $1 ]; then echo "Usage: #./script <port #> <filename>"; 
exit; fi

port=$1
file=$2

echo "Systems with port $port open:"

grep $port $file | grep open | cut -d " " -f 2
