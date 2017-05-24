#!/usr/bin/python

from scapy.all import *
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
import sys

if len(sys.argv) != 2:
	print "Usage - ./ttl_id.py [IP Address]"
	print "Example - ./ttl_id.py 10.0.0.5"
	print "Example will perform ttl analysis to attempt to determine whether the system is Windows or Linux/Unix"
	sys.exit()

ip = sys.argv[1]

ans = sr1(IP(dst=str(ip))/ICMP(),timeout=1,verbose=0)
if ans == None:
	print "No response was returned"
elif int(ans[IP].ttl) <= 64:
	print "Host is Linux/Unix"
else:
	print "Host is Windows"