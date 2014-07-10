__author__ = 'austin'

# This script lists all the user agents that have been associated with each ip address.
import pyshark
import json
from ua_parser import user_agent_parser

def useragents(filename, pathname):
    capture = pyshark.FileCapture(filename, display_filter='http')

    errors = 0
    http_packets = 0
    src_dict = {}  # A dict of mac address : list pairs. Lists contain all user-agent strings for a mac
    ua_result_dict = {}  # A dict of mac address: list pairs. List items are the parsed user-agent dicts.

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

    # Parse each UA string into a dict of different attributes
    for mac_address in src_dict:
        ua_string_list = src_dict[mac_address]
        for ua_string in ua_string_list:
            ua_dict = user_agent_parser.Parse(ua_string)
            if mac_address not in ua_result_dict:
                ua_result_dict[mac_address] = []
            ua_result_dict[mac_address].append(ua_dict)


    print "The number of errors was: ", errors, " and the number of http packets was: ", http_packets
    # pprint(ua_results_dict)


    with open(pathname + "/Results/useragents_results.txt", "wb") as result_file:
        json.dump(ua_result_dict, result_file)