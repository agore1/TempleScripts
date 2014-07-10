__author__ = 'austin'

#This script tests the ability to get the pathname of a python file's location.

import os
import sys

pathname = os.path.dirname(os.path.realpath(sys.argv[0]))

print pathname
