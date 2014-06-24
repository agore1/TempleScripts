#!/bin/bash
echo "What single keyword would you like to search for?"
read SEARCHWORD
echo "What file would you like to search?"
read FILENAME
# echo $SEARCHWORD
# SEARCHWORD = \'$SEARCHWORD\'
# echo $SEARCHWORD
tcpdump -Ann -r /var/tmp/"$FILENAME".pcap 'tcp or udp' | grep -iE --context 5 "$SEARCHWORD" |less 