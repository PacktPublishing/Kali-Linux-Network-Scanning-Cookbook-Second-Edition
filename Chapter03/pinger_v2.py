#!/usr/bin/python

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

if len(sys.argv) != 2:
	print "Usage - ./pinger.py [filename]"
	print "Example - ./pinger.py iplist.txt"
	print "Example will perform an ICMP ping scan of the IP addresses listed in iplist.txt"
	sys.exit()

filename = str(sys.argv[1])
file = open(filename,'r')

for addr in file:
	ans=sr1(IP(dst=addr.strip())/ICMP(),timeout=1,verbose=0)
	if ans == None:
		pass
	else:
		print addr.strip()