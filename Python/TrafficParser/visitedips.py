__author__ = 'austin'

# This script lists all the destination IPs that are requested by each src IP
import pyshark
import csv
import json

capture = pyshark.FileCapture('/home/austin/Downloads/Temple Tools/pcap files/youtube_1.pcap', display_filter='tcp or udp')

errors = 0
src_dict = {}

#For every packet, print out which layers are available. Use this to test if the tcpdump filter is working.
for packet in capture:
    #If there are 4 or more layers, then we know we have a packet with an IP layer for getting ip addresses
    if len(packet.layers) >= 4:
        try:
            src_ip = packet.ip.src
            dst_ip = packet.ip.dst

        except AttributeError:
            errors += 1
            continue    # If looking up the src and dst ips failed, don't complete the rest of this for iteration

        # print "The source ip is: ", src_ip, " and the dst ip is: ", dst_ip
        if src_ip in src_dict:
            if dst_ip in src_dict[src_ip]:
                pass
            else:
                src_dict[src_ip].append(dst_ip)
        else:
            src_dict[src_ip] = []
            src_dict[src_ip].append(dst_ip)

print "The number of errors was: ", errors
# pprint(sorted_src_list)
# result_file = open("Results/visited_ips_results.csv", "wb")
# writer = csv.writer(result_file)
# for key, value in src_dict.items():
#     writer.writerow([key, value])
# result_file.close()

with open("Results/visited_ips_results.txt", "wb") as result_file:
    json.dump(src_dict, result_file)
