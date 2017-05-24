# Kali Linux Network Scanning Cookbook - Second Edition
This is the code repository for [Kali Linux Network Scanning Cookbook - Second Edition](https://www.packtpub.com/networking-and-servers/kali-linux-network-scanning-cookbook-second-edition?utm_source=github&utm_medium=repository&utm_campaign=9781787287907), published by [Packt](https://www.packtpub.com/?utm_source=github). It contains all the supporting project files necessary to work through the book from start to finish.
## About the Book
With the ever-increasing amount of data flowing in today’s world, information security has become vital to any application. This is where Kali Linux comes in. Kali Linux focuses mainly on security auditing and penetration testing. This step-by-step cookbook on network scanning trains you in important scanning concepts based on version 2016.2. It will enable you to conquer any network environment through a range of network scanning techniques and will also equip you to script your very own tools.

Starting with the fundamentals of installing and managing Kali Linux, this book will help you map your target with a wide range of network scanning tasks, including discovery, port scanning, fingerprinting, and more. You will learn how to utilize the arsenal of tools available in Kali Linux to conquer any network environment. The book offers expanded coverage of the popular Burp Suite and has new and updated scripts for automating scanning and target exploitation. You will also be shown how to identify remote services, how to assess security risks, and how various attacks are performed. You will cover the latest features of Kali Linux 2016.2, which includes the enhanced Sparta tool and many other exciting updates.

This immersive guide will also encourage the creation of personally scripted tools and the skills required to create them.

## Instructions and Navigation
All of the code is organized into folders. For example, Chapter02.



The code will look like the following:
```
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
```



## Related Kali Linux Products
* [Learning Network Penetration Testing with Kali Linux [Video]](https://www.packtpub.com/networking-and-servers/learning-network-penetration-testing-kali-linux-video?utm_source=github&utm_medium=repository&utm_campaign=9781787129481)

* [Kali Linux Intrusion and Exploitation Cookbook](https://www.packtpub.com/networking-and-servers/kali-linux-intrusion-and-exploitation-cookbook?utm_source=github&utm_medium=repository&utm_campaign=9781783982165)

* [Kali Linux 2 - Assuring Security by Penetration Testing - Third Edition](https://www.packtpub.com/networking-and-servers/kali-linux-2-assuring-security-penetration-testing-third-edition?utm_source=github&utm_medium=repository&utm_campaign=9781785888427)

### Suggestions and Feedback
[Click here](https://docs.google.com/forms/d/e/1FAIpQLSe5qwunkGf6PUvzPirPDtuy1Du5Rlzew23UBp2S-P3wB-GcwQ/viewform) if you have any feedback or suggestions.
