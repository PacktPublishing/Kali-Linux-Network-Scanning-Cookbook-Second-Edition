#!/usr/bin/python

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

def rules(pkt):
	try:
		if (pkt[IP].dst=="172.16.69.133") and (pkt[ICMP]):
			print str(pkt[IP].src) + " is exploitable"
	except:
		pass

print "Listening for Incoming ICMP Traffic. Use Ctrl+C to stop listening"

sniff(lfilter=rules,store=0)