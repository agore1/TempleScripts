__author__ = 'austin'

#This script runs all the search scripts, then calls assemble_results to produce the final output
import sys
from macsandips import macs_and_ips
from macfrequency import mac_frequency
from useragents import useragents
from visitedips import visited_ips
from assemble_results import assemble_results
import os

#Find the directory of this file, for accessing and saving results
pathname = os.path.dirname(os.path.realpath(sys.argv[0]))

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    print "Please enter one argument: a pcap filename."
    sys.exit()

#A list of keywords to search the packets for
keywords = ["imei", "mac", "android"]


#Run scripts which generate output files.
print "Running macs_and_ips: "
macs_and_ips(filename, pathname)
print "Running mac_frequency"
mac_frequency(filename, pathname)
print "Running useragents"
useragents(filename, pathname)
print"Running visited_ips"
visited_ips(filename, pathname)
print"Assembling final results"
assemble_results(filename, pathname)





