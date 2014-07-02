__author__ = 'austin'

# This script lists all the user agents that have been associated with each ip address.
import pyshark
import csv
from pprint import pprint
import json

def useragents(filename):
    capture = pyshark.FileCapture(filename, display_filter='tcp or udp')

    errors = 0
    http_packets = 0
    src_dict = {}

    for packet in capture:
        #If there are 5 or more layers, then we know we have a packet with an IP layer for getting ip addresses
        if len(packet.layers) >= 5:
            try:
                user_agent = packet.http.user_agent
                mac_address = packet.wlan.sa
                http_packets+=1
            except AttributeError:
                errors += 1
                continue    # If looking up the src ip failed, don't complete the rest of this for iteration

            if mac_address in src_dict:
                if user_agent in src_dict[mac_address]:
                    pass
                else:
                    src_dict[mac_address].append(user_agent)
            else:
                src_dict[mac_address] = []
                src_dict[mac_address].append(user_agent)

    print "The number of errors was: ", errors, " and the number of http packets was: ", http_packets
    # pprint(src_dict)


    with open("Results/useragents_results.txt", "wb") as result_file:
        json.dump(src_dict, result_file)