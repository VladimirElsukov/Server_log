import re
from collections import defaultdict

ip_addresses = []
with open('log.txt', 'r') as file:
    for line in file:
        ips = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', line)
        for ip in ips:
            ip_addresses.append(ip)