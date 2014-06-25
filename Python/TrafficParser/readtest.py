__author__ = 'austin'

import json
from Device import Device

#Read individual files back into dicts
with open("Results/macs_and_ips_results.txt", "rb") as macs_ips:
    macs_ips_dict = json.load(macs_ips)
with open("Results/useragents_results.txt", "rb") as useragents:
    macs_useragents_dict = json.load(useragents)
with open("Results/mac_frequency_results.txt", "rb") as macs_frequency:
    macs_frequency_dict = json.load(macs_frequency)

devices_dict = {}

# Create devices with Macs and Ip addresses
for mac in macs_ips_dict:
    print "This entry ", mac, " has the value: ",  macs_ips_dict[mac]
    new_device = Device(ip_address=macs_ips_dict[mac], mac_address=mac)
    devices_dict[mac] = new_device  # Store the new device into the dict, with the key being it's mac address

# Match the MAC addresses between the existing device dict and new useragents dict
for mac in macs_useragents_dict:
   if mac in devices_dict:
       devices_dict[mac].user_agents = macs_useragents_dict[mac]

# Add packet sent count to devices, matched on MAC addresses
for mac in macs_frequency_dict:
    if mac in devices_dict:
        devices_dict[mac].packets_sent = macs_frequency_dict[mac]


# Do a simple printing of the device characteristics
for device in devices_dict:
    print devices_dict[device].ip_address, devices_dict[device].mac_address, devices_dict[device].user_agents, devices_dict[device].packets_sent