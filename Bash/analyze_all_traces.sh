#!/bin/bash
#This test script runs a program on all of the files in a directory

#The PCAP Files are assumed to reside in the /var/tmp directory
FILES=/var/tmp/*.pcap
#This command finds the pathname of current directory, so that the following scripts can be executed relative to it
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
ANALYZER=$DIR/../Python/TrafficParser/

for f in $FILES
do
	echo "Analyzing file $f"
	python $ANALYZER./run_all.py $f
done

# ls $ANALYZER