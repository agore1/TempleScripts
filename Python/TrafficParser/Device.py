__author__ = 'austin'


class Device(object):
    """The member variables of this class are: ip address, mac address,
        visited IP addresses, number of packets sent, user agents """

    def __init__(self, ip_address=None, mac_address=None, packets_sent=None, user_agents=None, ips_visited=None):
        self.ip_address = ip_address
        self.mac_address = mac_address
        self.packets_sent = packets_sent
        self.user_agents = user_agents
        self.ips_visited = ips_visited

    def __str__(self):
        first_line = "MAC=" + self.mac_address + " IP Address= " + self.ip_address + " Packets Sent= " + \
                     str(self.packets_sent)
        if self.user_agents:
            first_line += " \n            User Agents= " + str(self.user_agents)
        second_line = ""
        if self.ips_visited:
            for ip in self.ips_visited:
                second_line += "            IP visited: " + ip + "\n"
        return first_line + "\n" + second_line