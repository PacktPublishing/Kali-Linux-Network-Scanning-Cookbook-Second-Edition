#!/usr/bin/python

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

def ipid(zombie):
 reply1 = sr1(IP(dst=zombie)/TCP(flags="SA"),timeout=2,verbose=0)
 send(IP(dst=zombie)/TCP(flags="SA"),verbose=0)
 reply2 = sr1(IP(dst=zombie)/TCP(flags="SA"),timeout=2,verbose=0)
 if reply2[IP].id == (reply1[IP].id + 2):
  print "IPID sequence is incremental and target appears to be idle. ZOMBIE LOCATED"
  response = raw_input("Do you want to use this zombie to perform a scan? (Y or N): ")
  if response == "Y":
   target = raw_input("Enter the IP address of the target system: ")
   zombiescan(target,zombie)
  else:
   print "Either the IPID sequence is not incremental or the target is not idle. NOT A GOOD ZOMBIE"

def zombiescan(target,zombie):
 print "\nScanning target " + target + " with zombie " + zombie
 print "\n---------Open Ports on Target--------\n"
 for port in range(1,100):
  try:
   start_val = sr1(IP(dst=zombie)/TCP(flags="SA",dport=port),timeout=2,verbose=0)
   send(IP(src=zombie,dst=target)/TCP(flags="S",dport=port),verbose=0)
   end_val = sr1(IP(dst=zombie)/TCP(flags="SA"),timeout=2,verbose=0)
   if end_val[IP].id == (start_val[IP].id + 2):
    print port
  except:
   pass

print "-----------Zombie Scan Suite------------\n"
print "1 - Identify Zombie Host\n"
print "2 - Perform Zombie Scan\n"
ans = raw_input("Select an Option (1 or 2): ")
if ans == "1":
 zombie = raw_input("Enter IP address to test IPID sequence: ")
 ipid(zombie)
else:
 if ans == "2":
  zombie = raw_input("Enter IP address for zombie system: ")
  target = raw_input("Enter IP address for scan target: ")
  zombiescan(target,zombie)
