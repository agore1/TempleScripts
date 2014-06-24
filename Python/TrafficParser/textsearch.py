__author__ = 'austin'

# This script lists all the user agents that have been associated with each ip address.
import pyshark
import csv
from pprint import pprint

capture = pyshark.FileCapture('/home/austin/Downloads/Temple Tools/pcap files/wlan.pcap', display_filter='tcp or udp')

errors = 0
http_packets = 0
src_dict = {}

#For every packet, print out which layers are available. Use this to test if the tcpdump filter is working.
for packet in capture:
    #If there are 5 or more layers, then we know we have a packet with an IP layer for getting ip addresses
    if len(packet.layers) >= 5:
        try:
            user_agent = packet.http.user_agent
            src_ip = packet.ip.src
            http_packets += 1
        except AttributeError:
            errors += 1
            continue    # If looking up the src ip failed, don't complete the rest of this for iteration

        if src_ip in src_dict:
            if user_agent in src_dict[src_ip]:
                pass
            else:
                src_dict[src_ip].append(user_agent)
        else:
            src_dict[src_ip] = []
            src_dict[src_ip].append(user_agent)

print "The number of errors was: ", errors, " and the number of http packets was: ", http_packets

# pprint(src_dict)
# result_file = open("Results/useragents_results.csv", "wb")
# writer = csv.writer(result_file)
# for key, value in src_dict.items():
#     writer.writerow([key, value])
# result_file.close()