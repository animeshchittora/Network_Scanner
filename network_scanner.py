#!/usr/bin/env python
import scapy.all as scapy

def scan(ip):
	arp_request = scapy.ARP(pdst=ip)

	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")


	arp_request_broadcaast = broadcast/arp_request


	answer_list = scapy.srp(arp_request_broadcaast,timeout=1,verbose=False)[0]

	print("IP\t\t\tMac Adress\n-------------------------")

	for element in answer_list:
		print (element[1].psrc+"\t\t"+element[1].hwsrc)


ip = raw_input("PUT in format IP/CIDR value:  ")
scan(ip)
