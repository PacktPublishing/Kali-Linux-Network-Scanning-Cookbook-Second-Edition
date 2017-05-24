#!/usr/bin/python

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

SYN = IP(dst="172.16.69.128")/TCP(dport=80,flags='S')

print "-- SENT --"
SYN.display()

print "\n\n-- RECEIVED --"
response = sr1(SYN,timeout=1,verbose=0)
response.display()

if int(response[TCP].flags) == 18:
 print "\n\n-- SENT --"
 ACK = IP(dst="172.16.69.128")/TCP(dport=80,flags='A',ack=(response[
 TCP].seq + 1))
 response2 = sr1(ACK,timeout=1,verbose=0)
 ACK.display()
 print "\n\n-- RECEIVED --"
 response2.display()
else:
 print "SYN-ACK not returned"
