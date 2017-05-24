#! /bin/bash

if [ ! $1 ]; then echo "Usage: #./script <file>"; exit; fi

file=$1

for x in $(grep open $file | grep 445 | cut -d " " -f 2); 
do 
	nmap --script smb-vuln-conficker.nse -p 445 $x --script-args=unsafe=1;
	nmap --script smb-vuln-cve2009-3103.nse -p 445 $x --script-args=unsafe=1;
	nmap --script smb-vuln-ms06-025.nse -p 445 $x --script-args=unsafe=1;
	nmap --script smb-vuln-ms07-029.nse -p 445 $x --script-args=unsafe=1;
	nmap --script smb-vuln-regsvc-dos.nse -p 445 $x --script-args=unsafe=1;
	nmap --script smb-vuln-ms08-067.nse -p 445 $x --script-args=unsafe=1;
done