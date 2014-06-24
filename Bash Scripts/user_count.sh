#!/bin/bash
USERCOUNT = 0
USERCOUNT=`tcpdump -nA -r /var/tmp/wlan.pcap 'tcp or udp' | grep -Eic 'User-Agent'`
echo "The number of User-Agent mentions was $USERCOUNT"

exit 0