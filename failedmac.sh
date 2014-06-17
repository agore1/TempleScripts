#This script searches for all the MAC addresses sent over the network. 

FILENAME=$1

raw=`tcpdump -enn -r "$FILENAME" 'tcp or udp' | cut -f 21-23 -d " " | sort | uniq -c | sort -nr | head` 

echo $raw
#Read each line in the raw variable
while read -r line; 
do
    echo "$line"
    words=`echo "$line" | wc -w` #check to see if there are three words

    if[ $words -eq 3]
    	then

    fi

done <<< "$raw"


exit 0


#first thing: just get all the mac addresses. Maybe just cut the tcp dump, uniq it, then remove the bogus ones. 
