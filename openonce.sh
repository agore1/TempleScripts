#!/bin/bash

#Try opening the tcpdump file just once, then applying a variety of filters to it. 
FILENAME=$1
count=`tcpdump -Ann -r $FILENAME '(src 192.168.1.100 and (tcp or udp))'`
echo $count | head