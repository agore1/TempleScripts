__author__ = 'austin'

# This script lists all the destination IPs that are requested by each src IP
import pyshark
import csv
import json


def visited_ips(filename, pathname):
    capture = pyshark.FileCapture(filename, display_filter='tcp or udp')

    errors = 0
    src_dict = {}

    bssid = capture[0].wlan.bssid

    #For every packet, print out which layers are available. Use this to test if the tcpdump filter is working.
    for packet in capture:
        #If there are 4 or more layers, then we know we have a packet with an IP layer for getting ip addresses
        if len(packet.layers) >= 4:
            try:
                dst_ip = packet.ip.dst
                src_mac = packet.wlan.sa
            except AttributeError:
                errors += 1
                continue    # If looking up the src and dst ips failed, don't complete the rest of this for iteration

            # Don't consider packets sent out by the Access point, only ones sent by the phone
            if src_mac != bssid:
                if src_mac in src_dict:
                    if dst_ip in src_dict[src_mac]:
                        pass
                    else:
                        src_dict[src_mac].append(dst_ip)
                else:
                    src_dict[src_mac] = []
                    src_dict[src_mac].append(dst_ip)

    print "The number of errors was: ", errors
    # pprint(sorted_src_list)
    # result_file = open("Results/visited_ips_results.csv", "wb")
    # writer = csv.writer(result_file)
    # for key, value in src_dict.items():
    #     writer.writerow([key, value])
    # result_file.close()

    with open(pathname + "/Results/visited_ips_results.txt", "wb") as result_file:
        json.dump(src_dict, result_file)
