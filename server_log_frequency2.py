import re
from collections import defaultdict

file_path = 'log.txt'

ip_frequency = defaultdict(int)
excluded_ips = {"192.168.0.0"}

with open(file_path, 'r') as file:
    for line in file:
        ips = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', line)
        for ip in ips:
            if ip not in excluded_ips:
                ip_frequency[ip] += 1

# Сортируем IP-адреса сначала по убыванию количества упоминаний, затем лексикографически
sorted_ip_frequency = sorted(ip_frequency.items(), key=lambda x: (-x[1], x[0]))

# Группируем IP-адреса по количеству упоминаний
grouped_ips = defaultdict(list)
for ip, count in sorted_ip_frequency:
    grouped_ips[count].append(ip)

# Пересортировываем IP с одинаковым количеством упоминаний по убыванию
final_sorted_ips = []
for count in sorted(grouped_ips.keys(), reverse=True):
    same_count_ips = sorted(grouped_ips[count], reverse=True)
    for ip in same_count_ips:
        final_sorted_ips.append((ip, count))

# Записываем результаты в файл
with open('ip_frequency.txt', 'w') as output_file:
    for ip, count in final_sorted_ips:
        output_file.write(f"{ip} {count}\n")