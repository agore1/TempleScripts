__author__ = 'austin'

# This script searches for all MAC source addresses and records their number of appearances in a csv file.
import pyshark
import operator
import csv

capture = pyshark.FileCapture('/home/austin/Downloads/Temple Tools/pcap files/youtube_1.pcap', display_filter='tcp or udp')

errors = 0
src_dict = {}

# print vars(capture[0].wlan)
# print "The addr is ", capture[0].wlan.addr
# print "The da is ", capture[0].wlan.da
# print "The sa is ", capture[0].wlan.sa
print "The bssid is ", capture[0].wlan.bssid


#For every packet, print out which layers are available. Use this to test if the tcpdump filter is working.
for packet in capture:
    #If there are 4 or more layers, then we know we have a packet with an IP layer for getting ip addresses
    if len(packet.layers) >= 4:
        try:
            source_address = packet.wlan.sa
            if source_address in src_dict:
                src_dict[source_address] += 1
            else:
                src_dict[source_address] = 1

        except AttributeError:
            errors += 1

print "The number of errors was: ", errors

sorted_src_list = sorted(src_dict.iteritems(), key=operator.itemgetter(1), reverse=True)

file = open("Results/find_macs_results.csv", "w")
w = csv.writer(file)
w.writerows(sorted_src_list)
file.close()
