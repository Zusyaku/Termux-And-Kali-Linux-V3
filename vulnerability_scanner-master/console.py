#!/usr/bin/env python3
# Version: 0.3.1 (Beta test)
# ToDo: Fix 'All' for select script

import sys, os, threading, subprocess, time, datetime
from tqdm import tqdm
from collections import Counter

banner = '''
\033[1;93m
               _   _        __      ___
     /\       | | (_)       \ \    / (_)
    /  \   ___| |_ ___   ____\ \  / / _  _____      __
   / /\ \ / __| __| \ \ / / _ \ \/ / | |/ _ \ \ /\ / /
  / ____ \ (__| |_| |\ V /  __/\  /  | |  __/\ V  V /
 /_/____\_\___|\__|_| \_/ \___| \/   |_|\___| \_/\_/\033[0m
\033[1;94m  / ____|                    (_) |
 | (___   ___  ___ _   _ _ __ _| |_ _   _
  \___ \ / _ \/ __| | | | '__| | __| | | |
  ____) |  __/ (__| |_| | |  | | |_| |_| |
 |_____/ \___|\___|\__,_|_|  |_|\__|\__, |
                                     __/ |
                                    |___/
\033[0m
\033[1;90m-------------------------------------------------------\033[0m
'''

# Time and date format
def time_full():
    ts = time.time()
    return datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y %H:%M:%S')

def time_date():
    ts = time.time()
    return datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')

#csv_file = input('CSV file location: ')
csv_path = sys.argv[0].replace('console.py', 'targets.csv')

if not os.path.isfile(csv_path):
    print(' \033[1;91m[ ERROR ]\033[0m File "%s" does not exist!' % csv_path)
    sys.exit(1)
else:
    f = open(csv_path).readlines()
    print('\n \033[1;92m[ FILE FOUND ]\033[0m >> ./%s\n' % csv_path)
    #print(f)

counter = -1
targets = [] # Client IP's
clients = [] # Client names

for i in f:
    counter +=1
    i = i.replace('"', ''); i = i.split(',')
    targets.append(i[0].rstrip())
    clients.append(i[1].rstrip())
    #print(i[0].strip()) # Debug

del targets[0] # Delete header > not a target
del clients[0] # Delete header > not a client

# Debug
#for l in targets:
#    print(l)

print(' \033[1;92m[ %i Addresses FOUND ]\033[0m\n' % counter)

count_scripts = -1
script_list = []

script_list.append('None'); count_scripts += 1
script_list.append('All >> Not working, TBA'); count_scripts += 1

print('\033[1;94mSelect script: \033[0m')

for path, subdirs, files in os.walk('.'):
    for name in files:
        if name.endswith('.nse'):
            count_scripts += 1
            script_list.append(path + '/' + name)

c = -1
for items in script_list:
    c +=1
    print('\t\033[1;96m%i)\033[0m ' % int(c) + items)

try:
    num = input('NSE script: ')
except Exception as e:
    num = 0

if int(num) == 0:
    print('\033[1;95m [ NO SCRIPT ]\033[0m '); script = ''
else:
    print('\033[1;92m [ LOADED ]\033[0m ' + script_list[int(num)])
    script = '-sV --script ' + script_list[int(num)]

p_range = input('Range: ')
if p_range:
    print('\033[1;95m [ RANGE ] %s\033[0m ' % p_range); p_range = '-p ' + p_range
else:
    print('\033[1;95m [ NO RANGE ]\033[0m '); p_range = ''

print(banner)

#print('\nScan started: %s' % time_full())

# Create dir to save results
if not os.path.isdir('result/'):
    os.makedirs('result/')

header = 'Client'.ljust(30), 'Address'.ljust(30), 'Port'.ljust(15), 'Service'.ljust(40), 'Status'

print('\n\n\033[1;93m{0[0]} {0[1]} {0[2]} {0[3]} {0[4]}\033[0m'.format(header))

# Create final result file
with open('final - ' + time_date() + '.txt', 'a+') as f:
    f.write('{0[0]} {0[1]} {0[2]} {0[3]} {0[4]}\n'.format(header))
    f.close()

client_id = 0 # ID for list: clients = []
port = ''
ports = []
status = []
d = [] # list for addresses when a range is given (ex. 192.168.0.0/24)
fid = 0

with tqdm(total=(len(targets)), desc='Progress') as bar:
    for l in targets:
        try:
            start = datetime.datetime.now()
            if '/' in l:
                save_file = l.replace('/', '-') # '/' is a illegal character for file names, replace it with a dash (-)
            else:
                save_file = l

            # Starts Scan
            _scan = subprocess.Popen(['nmap %s %s %s --system-dns --open -vv > result/%s.txt' % (script, p_range, l, save_file)], stdout=subprocess.PIPE, shell=True).wait()

            result = open('result/%s.txt' % save_file, 'r').readlines()
            for i in result:
                if i.startswith('Nmap scan report for '):
                    d.append(i.split(' ')[-1].replace('(', '').replace(')', '').strip())

                if i[0].isdigit():
                    #print(i)
                    if not 'unrecognized' in i:
                        port = i.split('/')[0].strip()
                        if port[1].startswith('u'):
                            t = '/udp'
                            ports.append(port + t)
                            status.append('\033[1;92m[ NOT VULNERABLE ]\033[0m')
                        else:
                            t = '/tcp'
                            ports.append(port + t)
                            status.append('\033[1;92m[ NOT VULNERABLE ]\033[0m')

                elif 'State: LIKELY VULNERABLE' in i:
                    rep = len(ports) -1
                    status[int(rep)] = '\033[1;91m[ LIKELY VULNERABLE ]\033[0m'
                elif 'State: VULNERABLE' in i:
                    rep = len(ports) -1
                    status[int(rep)] = '\033[1;91m[ VULNERABLE ]\033[0m'

                service = script.replace('-sV --script ', '')
                client = clients[int(client_id)]

                #port = '' # Reset port

            # Print final result for each port
            for i in ports:
                if d: # If it was a range, 'd' contains addresses
                    for ip in d: # print result for each ip in range that was scanned
                        final = clients[int(client_id)].ljust(30) + d[0].ljust(30) + ports[int(fid)].ljust(15) + service.ljust(40) + status[int(fid)]
                        tqdm.write('%s' % final)
                        d.remove(d[0]) # Remove the first item until no items left
                else:
                    final = clients[int(client_id)].ljust(30) + l.ljust(30) + ports[int(fid)].ljust(15) + service.ljust(40) + status[int(fid)]
                    #print(final)
                    tqdm.write('%s' % final)
                    #with open('final - ' + time_date() + '.txt', 'a+') as f:
                    #    f.write(final); f.close()
                fid +=1#; print(fid)
            fid = 0
            client_id +=1
            ports = []; status = []
            #print('\n')
            #tqdm.write('\n')
            bar.update(1)
        except Exception as e:
            tqdm.write('\033[1;91m[ ERROR ]\033[0m %s' % e)
            pass
        counter -= 1
    tqdm.write('\n\nScan ended in %s' % (datetime.datetime.now()-start))
    tqdm.write('\n\n\033[1mResults saved to:\033[0m result/\n')
tqdm.write('\033[1mFinal result saved to:\033[0m ./final - %s.txt\n' % time_date())
