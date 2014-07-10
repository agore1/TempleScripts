__author__ = 'austin'

from ua_parser import user_agent_parser

user_agent_string = u'Mozilla/5.0 (Linux; Android 4.3; Galaxy Nexus Build/JWR66Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.141 Mobile Safari/537.36'

result_dict = user_agent_parser.Parse(user_agent_string)

print result_dict