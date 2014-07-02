#!/bin/bash

#This script aggregates all the other search scripts. 
FILENAME=$1
#This command finds the pathname of current directory, so that the following scripts can be executed relative to it
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
$DIR/multisearch.sh $FILENAME
$DIR/ipsearch.sh $FILENAME
exit 0

