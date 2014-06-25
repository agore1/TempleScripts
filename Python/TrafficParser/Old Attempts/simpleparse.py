__author__ = 'austin'

import dpkt
import dpkt.ethernet
import socket

# Open a file
pcapFile = open('/home/austin/Downloads/Temple Tools/pcap files/wlan.pcap')
pcap = dpkt.pcap.Reader(pcapFile)

#Check that network layer 2 is 802.11 wifi
print pcap.datalink()
if pcap.datalink() == dpkt.pcap.DLT_IEEE802_11_RADIO:
    print "This is a wifi capture!"

#print out the timestamp and buffer length for each packet
for ts, buf in pcap:
    # print ts, len(buf)
    tap = dpkt.radiotap.Radiotap(buf)
    # signal_ssi=(256-tap.ant_sig_present.db)
    # print tap
    tap_len = socket.ntohs(tap.length)
    wlan = dpkt.ieee80211.IEEE80211(buf)
    # print wlan

    tcp = wlan.data
    print tcp

#     #Check if network layer 2 for the packet is 802.11 wifi
#     l2 = dpkt.ieee80211.IEEE80211(buf)
#         print l2



