__author__ = 'austin'


import dpkt
import binascii

f = open('/home/austin/Downloads/Temple Tools/pcap files/wlan.pcap')
pc = dpkt.pcap.Reader(f)
dl = pc.datalink()
if pc.datalink() == 127: #Check if RadioTap
        for timestamp, rawdata in pc:
                tap = dpkt.radiotap.Radiotap(rawdata)
                signal_ssi=-(256-tap.ant_sig.db)        #Calculate signal strength
                t_len=binascii.hexlify(rawdata[2:3])    #t_len field indicates the entire length of the radiotap data, including the radiotap header.
                t_len=int(t_len,16)                     #Convert to decimal
                wlan = dpkt.ieee80211.IEEE80211(rawdata[t_len:])
                print wlan
                # if wlan.type == 0 and wlan.subtype == 4: # Indicates a probe request
                #     ssid = wlan.ies[0].info
                #     mac=binascii.hexlify(wlan.mgmt.src)
                #     print "%s, %s (%d dBm)"%(mac,ssid,signal_ssi)