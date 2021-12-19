#!/usr/bin/env python3
import os, sys, getpass
from prettytable import PrettyTable

if not getpass.getuser() == 'root':
    print('[ERROR] Must run as root to read files'); sys.exit(1)

table = PrettyTable(['Num.', 'SSID', 'Key', 'Username', 'Password', 'Security', 'MAC address', 'Hidden']) # Header
table.align = "l" # Text Align left

wifi_list = []
count_wifi = 0

for path, subdirs, files in os.walk('/etc/NetworkManager/system-connections'):
    for name in files:
        count_wifi +=1
        wifi_list.append(path + '/' + name)

def print_table():
    c = 0
    for wifi in wifi_list:
        c +=1
        username = None
        password = None
        key = None
        security = None
        mac = None
        hidden = False

        f = open(wifi).readlines()
        for l in f:
            l = l.strip()
            if l.startswith('psk='):
                key = l.split('=')[1].strip()

            if l.startswith('identity='):
                username = l.split('=')[1].strip()

            if l.startswith('password='):
                password = l.split('=')[1].strip()

            if l.startswith('key-mgmt='):
                security = l.split('=')[1].strip()
            if l.startswith('mac-address='):
                mac = l.split('=')[1].strip()

            if l.startswith('hidden='):
                hidden = True

        result = int(c), wifi.split('/')[-1], key, username, password, security, mac, hidden
        table.add_row([result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7]])
    table.sortby = 'Num.'
    print(table)

print_table()
print('Found %i wifi passwords' % int(count_wifi))
