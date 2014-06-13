#!/bin/bash

#This script aggregates all the other search scripts. 
FILENAME=$1
./multisearch.sh $FILENAME
./ipsearch.sh $FILENAME
exit 0