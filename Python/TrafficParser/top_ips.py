__author__ = 'austin'

# This script searches for all the IP source addresses and returns the number of packets originating from each

import pyshark
import operator
import json

capture = pyshark.FileCapture('/home/austin/Downloads/Temple Tools/pcap files/wlan.pcap', display_filter='tcp or udp')

errors = 0
src_dict = {}
dst_dict = {}

#For every packet, print out which layers are available. Use this to test if the tcpdump filter is working.
for packet in capture:
    #If there are 4 or more layers, then we know we have a packet with an IP layer for getting ip addresses
    if len(packet.layers) >= 4:
        try:
            # print packet.ip.dst  # TODO: why does packet.ip produce 6 errors, while packet[3] produces only 4?
            #Add the src ip addresses to a dictionary for uniqueness
            if packet.ip.src in src_dict:
                src_dict[packet.ip.src] += 1
            else:
                src_dict[packet.ip.src] = 1

            #Add the dst ip addresses to a dictionary for uniqueness
            if packet.ip.dst in dst_dict:
                dst_dict[packet.ip.dst] += 1
            else:
                dst_dict[packet.ip.dst] = 1

        except AttributeError:      # In case the packet doesn't have a destination or source ip address
            errors += 1


print "The number of errors was: ", errors
#Save the sorted results of the ip search to a file
# sorted_dst_dict = sorted(dst_dict.iteritems(), key=operator.itemgetter(1), reverse=True)
# pprint(sorted_dst_dict)
# print sorted_dst_dict
# sorted_src_dict = sorted(src_dict.iteritems(), key=operator.itemgetter(1), reverse=True)
# pprint(sorted_src_dict)

# file = open("Results/top_ips_results.csv", "w")
# w = csv.writer(file)
# w.writerows(sorted_src_dict)
# file.close()

# print dir(capture[0])   # print all available methods and fields

with open("Results/top_ips_results.txt", "wb") as result_file:
    json.dump(src_dict, result_file)