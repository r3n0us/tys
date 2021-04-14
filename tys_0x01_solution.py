#!/usr/bin/env python3
from scapy.all import *
pkts = rdpcap("tys_0x01_c2.pcapng")
keys = ""
encoded_text = ""


def xor(key, enc_text):
    cnt = 0
    plain_text = ""
    for c in range(0, len(enc_text), 1):
        plain_text += chr( ord(key[cnt]) ^ ord(enc_text[c]) )
        cnt += 1
        if cnt == len(key):
            cnt = 0
    print(plain_text)


for pkt in pkts:
    if pkt.haslayer('Raw') and pkt.getlayer('Raw').load[0] == 0x02:
        keys = pkt.getlayer('Raw').load[2:int(pkt.getlayer('Raw').load[1])+2]
        keys = keys.decode('utf-8')
    elif pkt.haslayer('Raw') and pkt.getlayer('Raw').load[0] == 0x04:
        encoded_text = pkt.getlayer('Raw').load[2:int(pkt.getlayer('Raw').load[1])+2]
        encoded_text = encoded_text.decode('utf-8')
        xor(keys, encoded_text)
