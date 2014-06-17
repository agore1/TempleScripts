#!/bin/bash
#This script lists all the source IP addresses, and how many packets they sent, and sorts them in descending order, then prints the results to a file. 

FILENAME=$1

tcpdump -nn -r "$FILENAME" 'tcp or udp' | cut -f 22- -d " " | cut -f 1-4 -d "." | sort | uniq -c | sort -nr | head > top_ips_result.txt
exit 0