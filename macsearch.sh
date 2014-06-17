#This script searches for all the MAC addresses sent over the network. 

FILENAME=$1

#Open the tcpdump with ethernet (MAC) codes printed -e
#cut out the relevant columns (MAC)
#translate them all into a vertical vector, then sort horizontally, then elimintate 
#non unique values 
COUNT=`tcpdump -enn -r "$FILENAME" 'tcp or udp' | cut -f 21-23 -d " " | tr ' ' '\n' |\
 sort | uniq -c | sort -nr`

SSID=`echo "$COUNT" | head -n1 | cut -f 2- -d ":"`
echo The MAC Address of the AP is: $SSID

# echo All MAC addresses found: "$COUNT"

echo "The MAC addresses found that aren't the AP are:"
#Remove all the nonuniform Addresses, eg ones that don't start with DA or S
MACS=`echo "$COUNT" | sed "/$SSID/d" | cut -f 2- -d \: --only-delimited | sort | uniq`
echo "$MACS"
echo "$MACS" > mac_search_result.txt
