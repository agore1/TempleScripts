__author__ = 'austin'
#This script uses a bash script to quickly search a pcap file for occurrences of a keyword or list of keywords.

import subprocess
import json


def keyword_search(mac_address, filename, keywords):
    results_dict = {}
    for keyword in keywords:
        bash_command = "/home/austin/Documents/Temple/TempleScripts/Bash/keyword_search.sh " + \
                       filename + " " + keyword + " " + mac_address
        print "Searching " + filename + " for the keyword:\"" + keyword + "\" from the mac address: " + mac_address
        process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
        output = process.communicate()

        # print output[0]
        occurrence_list = output[0].splitlines()
        print "The number of occurrences of the keyword: \" " + keyword + " \" was: " + str(len(occurrence_list))
        results_dict[keyword] = occurrence_list
    return results_dict


#A simple test, opens a dict with macs and ips, searches the file for keywords sent from each mac, and prints them out
# with open("Results/macs_and_ips_results.txt", "rb") as macs_ips:
#         macs_ips_dict = json.load(macs_ips)
#
# testfile = "/var/tmp/3apps_zedge.pcap"
# testkeywords = ["imei", "android"]
# for mac in macs_ips_dict:
#     occurrences_dict = keyword_search(mac, testfile, testkeywords)
#     for keyword in occurrences_dict:
#         if occurrences_dict[keyword]:
#             print "Here are the occurrences of: " + keyword + "\n" + str(occurrences_dict[keyword])
#         else:
#             print "The keyword " + keyword + " had no occurrences for the MAC Address: " + mac
#
