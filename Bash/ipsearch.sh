#!/bin/bash

#This script searches the pcap file for occurrences of your ipaddress in traffic outgoing from your device
#Therefore, it first removes the ipaddress collumns to prevent them from being matched

FILENAME=$1
IPADDRESS="192.168.1.100"
#Open the file, listing only tcp or udp traffic outbout from our address, cut off the ip columns to not get 
#	false positives, then search for the ipaddress
RESULT=`tcpdump -Ann -r $FILENAME "((tcp or udp) and (src $IPADDRESS))" | cut -f 25- -d " " | grep -c "$IPADDRESS"`

#Print out the results of our search
echo "The IP address appeared: " $RESULT " times."

exit 0