import re
import os
from collections import defaultdict

# Получаем путь к текущей директории скрипта
current_dir = os.path.dirname(os.path.abspath(__file__))

# Создаем абсолютный путь к файлу 'log.txt' в той же директории, что и скрипт
file_path = os.path.join(current_dir, 'log.txt')

ip_addresses = []
with open(file_path, 'r') as file:
    for line in file:
        ips = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', line)
        ip_addresses.extend(ips)

ip_frequency = defaultdict(int)
for ip in ip_addresses:
    ip_frequency[ip] += 1

try:
    # Сконвертируем IP-адреса в числовой формат для правильной сортировки
    sorted_ips = sorted(ip_frequency.items(), key=lambda x: (-x[1], list(map(int, x[0].split('.'))))

    # Запись результатов в новый файл
    with open('ip_frequency.txt', 'w') as output_file:
        for ip, count in sorted_ips:
            output_file.write(f"{ip} {count}\n")
except Exception as e:
    print(f"Произошла ошибка: {e}")