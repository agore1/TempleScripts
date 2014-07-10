#!/bin/bash
#This test script runs a program on all of the files in a directory

FILES=/var/tmp/*.pcap
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
ANALYZER=$DIR/../Python/TrafficParser/

for f in $FILES
do
	echo "Analyzing file $f"
	python $ANALYZER./run_all.py $f
done

ls $ANALYZER