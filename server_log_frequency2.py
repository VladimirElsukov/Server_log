import re
import os
from collections import defaultdict

# Получаем путь к текущей директории скрипта
current_dir = os.path.dirname(os.path.abspath(__file__))

# Создаем абсолютный путь к файлу 'log.txt' в родительской директории
file_path = os.path.join(os.path.dirname(current_dir), 'log.txt')

ip_addresses = []
with open(file_path, 'r') as file:
    for line in file:
        ips = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', line)
        ip_addresses.extend(ips)

ip_frequency = defaultdict(int)
for ip in ip_addresses:
    ip_frequency[ip] += 1

try:
    # Сортировка IP-адресов по убыванию частоты упоминаний и IP-адреса по убыванию
    sorted_ips = sorted(ip_frequency.items(), key=lambda x: (-x[1], x[0]))
    # Запись результатов в новый файл
    with open('ip_frequency.txt', 'w') as output_file:
        for ip, count in sorted_ips:
            output_file.write(f"{ip} {count}\n")
except Exception as e:
    print(f"Произошла ошибка: {e}")