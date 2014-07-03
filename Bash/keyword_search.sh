#!/bin/bash

#This script searches for a keyword passes as an argument

FILENAME=$1
KEYWORD=$2
MACADDRESS=$3
#Check to see if an MACADDRESS variable was passed, and run the appropriate script if so
if [ $# -eq 3 ]
then
	# echo "((wlan SA $MACADDRESS) and (tcp or udp))"
	tcpdump -Ann -r $FILENAME "((wlan src $MACADDRESS) and (tcp or udp))" | grep --color -iE "$KEYWORD"
	# tcpdump -Ann -r $FILENAME "((wlan src $MACADDRESS) and (tcp or udp))" | grep --color -iEc "$KEYWORD"
else
	tcpdump -Ann -r $FILENAME "tcp or udp" | grep --color -iE "$KEYWORD"
	# tcpdump -Ann -r $FILENAME "tcp or udp" | grep --color -iEc "$KEYWORD"
fi
