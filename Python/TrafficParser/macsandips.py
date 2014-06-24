__author__ = 'austin'
# This script produces a file of MAC source addresses and their corresponding IP source addresses
# THe results are stored in a dict with keys as the MAC address and IP source addresss as value

import pyshark
import operator
import csv

capture = pyshark.FileCapture('/home/austin/Downloads/Temple Tools/pcap files/youtube_1.pcap', display_filter='tcp or udp')

errors = 0
src_dict = {}  # Stores the MAC IP address pairs

# print vars(capture[0].wlan)
# print "The addr is ", capture[0].wlan.addr
# print "The da is ", capture[0].wlan.da
# print "The sa is ", capture[0].wlan.sa
bssid = capture[0].wlan.bssid
print "The bssid is ", bssid


#For every packet, print out which layers are available. Use this to test if the tcpdump filter is working.
for packet in capture:
    #If there are 4 or more layers, then we know we have a packet with an IP layer for getting ip addresses
    if len(packet.layers) >= 4:
        try:
            src_mac = packet.wlan.sa
            src_ip = packet.ip.src
            if src_mac != bssid:
                #print "The source mac is: ", src_mac, " and the source IP is: ", src_ip
                if src_mac in src_dict:
                    pass
                else:
                    src_dict[src_mac] = src_ip

        except AttributeError:
            errors += 1

print "The number of errors was: ", errors

sorted_src_list = sorted(src_dict.iteritems(), key=operator.itemgetter(1), reverse=True)
print sorted_src_list

result_file = open("macs_and_ips_results.csv", "w")
w = csv.writer(result_file)
w.writerows(sorted_src_list)
result_file.close()
