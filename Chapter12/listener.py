#!/usr/bin/python

from scapy.all import *
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

def rules(pkt):
    try:
        if ((pkt[IP].dst=="172.16.69.133") and (pkt[ICMP]) and pkt[IP].ttl <= 15):
            print str(pkt[IP].src) + " is exploitable"
        except:
            pass

print "Listening for Incoming ICMP Traffic. Use Ctrl+C to stop scanning"

sniff(lfilter=rules,store=0)