__author__ = 'austin'

#This script runs all the search scripts, then calls assemble_results to produce the final output

from macsandips import macs_and_ips
from macfrequency import mac_frequency
from useragents import useragents
from visitedips import visited_ips
from assemble_results import assemble_results

filename = "youtube_1.pcap"
#Run scripts which generate output files.
print "Running macs_and_ips: "
macs_and_ips(filename)
print "Running mac_frequency"
mac_frequency(filename)
print "Running useragents"
useragents(filename)
print"Running visited_ips"
visited_ips(filename)
print"Assembling final results"
assemble_results()




