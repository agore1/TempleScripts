__author__ = 'austin'

import subprocess

# This script tests the useage of shell script calling from python.

keyword = "imei"
ipaddress = "192.168.1.100"
# ipaddress = "192.168.1.100"
# bash_command = "/home/austin/Documents/Temple/TempleScripts/Bash/multisearch.sh " \
#                "/var/tmp/3apps_zedge.pcap"
bash_command = "/home/austin/Documents/Temple/TempleScripts/Bash/keyword_search.sh " \
               "/var/tmp/3apps_zedge.pcap " + keyword + " " + ipaddress
print bash_command
process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
output = process.communicate()

print output[0]
occurrence_list = output[0].splitlines()
#Splits the string into a list based on newline characters, then get the last item
occurrences = occurrence_list[-1]
print occurrences

