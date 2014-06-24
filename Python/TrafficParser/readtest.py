__author__ = 'austin'

import json
import pprint
with open("Results/visited_ips_results.csv", "rb") as result_file:
    src_dict = json.load(result_file)

print type(src_dict)
print src_dict
print type(src_dict['192.168.1.100'][0])

for entry in src_dict:
    print "This entry is", src_dict[entry]