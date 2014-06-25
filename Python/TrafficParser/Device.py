__author__ = 'austin'


class Device(object):
    """The member variables of this class are: ip address, mac address,
        visited IP addresses, number of packets sent, user agents """

    def __init__(self, ip_address=None, mac_address=None, packets_sent=None, user_agents=None):
        self.ip_address = ip_address
        self.mac_address = mac_address
        self.packets_sent = packets_sent
        self.user_agents = user_agents

test_device = Device()
print test_device.packets_sent
