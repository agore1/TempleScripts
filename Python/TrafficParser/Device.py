__author__ = 'austin'

from pprint import pformat


class Device(object):
    """The member variables of this class are: ip address, mac address,
        visited IP addresses, number of packets sent, user agents """

    def __init__(self, ip_address=None, mac_address=None, packets_sent=None, ips_visited=None,
                 keyword_dict=None):
        self.ip_address = ip_address
        self.mac_address = mac_address
        self.packets_sent = packets_sent
        self.user_agents = []
        self.ips_visited = ips_visited
        self.keyword_dict = keyword_dict
        self.os = ""
        self.hw_model = ""
        self.browsers = []

    def __str__(self):
        one_indent = "    "
        two_indent = "        "
        three_indent = "            "
        first_line = "MAC=" + self.mac_address + " IP Address= " + self.ip_address + " Packets Sent= " + \
                     str(self.packets_sent) + "\n"

        first_line += two_indent + "Device model: " + self.hw_model + one_indent + "OS: " + self.os + "\n"

        if self.user_agents:
            first_line += two_indent + "User Agents= " + pformat(self.user_agents, indent=8, width=100)

        second_line = two_indent + "The following keywords were found: \n"
        if self.keyword_dict:
            for keyword in self.keyword_dict:
                second_line += "            " + keyword + ":\n"
                for instance in self.keyword_dict[keyword]:
                    second_line += three_indent + instance + "\n"
        third_line = ""
        if self.ips_visited:
            third_line += two_indent + "The following IPs were visited:\n"
            for ip in self.ips_visited:
                third_line += three_indent + "IP: " + ip + "\n"
        return first_line + "\n" + second_line + third_line

    def add_user_agents(self, ua_dict_list):
        self.user_agents = ua_dict_list
        for ua_dict in ua_dict_list:
            if not self.hw_model:
                self.hw_model = ua_dict["device"]["family"]
            if not self.os:
                self.os = ua_dict["os"]["family"] + " " + ua_dict["os"]["major"] + "." + ua_dict["os"]["minor"]


def compareDevices(device1, device2):
    pass