#!/bin/bash
#This script searches for a variety of keywords, printing how many times each was found. 
#The search space is the entire pcap file, so this is unsuitable for looking for IP addresses, for example, 
#	whose appearance in the pcap file would be a false positive for actually being leaked over the network. 

FILENAME=$1
#imei for galaxy nexus is 351746051667742
#serial number for galaxy nexus is 0149C22118018016
#MAC address for the galaxy nexus is a0:0b:ba:e7:f5:d9
KEYWORDS=( mac imei user-agent "templetest79@gmail.com" "a0:0b:ba:e7:f5:d9" 351746051667742 0149C22118018016 )
# declare -a RESULTS
for i in "${KEYWORDS[@]}"
do
	#search the pcap file for the keyword, and list it's occurrences
	count=`tcpdump -Ann -r $FILENAME '(src 192.168.1.100 and (tcp or udp))' | grep -iEc "$i"`  
	echo $i "appeared: " $count " times."
	# RESULTS[$i]=$count
done

#print out the contents of the array
# for j in "${RESULTS[@]}"
# do
# 	echo {$KEYWORDS[$j]} "appeared: " ${RESULTS[$j]} " times."
	# echo ${RESULTS[$j]}
# done

exit 0



# BSSID:f8:d1:11:f6:f4:a6 SA:a0:0b:ba:e7:f5:d9 DA:f8:d1:11:f6:f4:a6