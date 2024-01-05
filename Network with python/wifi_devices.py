import sys
from scapy.all import * 
import scapy.all as scapy

IFACE_NAME = "Intel(R) Centrino(R) Advanced-N 6205"

devices = set()

def packetHandler(pkt):
    if pkt.haslayer(scapy.Dot11):
        dot11_layer = pkt.getlayer(scapy.Dot11)
        
        if dot11_layer.addr2 and (dot11_layer.addr2 not in devices):
            devices.add(dot11_layer.addr2)
            print(len(devices), dot11_layer.addr2, dot11_layer.payload.name)
            
sniff(iface = IFACE_NAME, count = 100, prn = packetHandler)