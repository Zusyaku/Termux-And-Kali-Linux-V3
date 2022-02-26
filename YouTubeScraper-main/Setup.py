# -*- coding: utf-8 -*-
#!/bin/env python3
# Telegram Group: http://t.me/cyberclans
# Please give me credits if you use any codes from here.

import os, sys
import configparser
re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
def banner():
	os.system('clear')
	print(f"""
	{re}╔═╗{cy}┌─┐┌┬┐┬ ┬┌─┐
	{re}╚═╗{cy}├┤  │ │ │├─┘
	{re}╚═╝{cy}└─┘ ┴ └─┘┴   v1.0
	""")
banner()
print(gr+"[+] Installing requierments ...")
os.system('python -m pip install pandas')
os.system('pip install apiclient')
os.system('pip install --upgrade google-api-python-client')
banner()
os.system("touch config.data")
cpass = configparser.RawConfigParser()
cpass.add_section('cred')
xid = input(gr+"[+] Enter Api Key : "+re)
cpass.set('cred', 'id', xid)
xhash = input(gr+"[+] Enter Video ID : "+re)
cpass.set('cred', 'hash', xhash)
setup = open('config.data', 'w')
cpass.write(setup)
setup.close()
print(gr+"[+] Setup complete!")
print(gr+"[+] Now you can run YouTube Scraper!")
print(gr+"[+] Make sure to read README.md before using this tool.")
print(gr+"[+] https://github.com/palahsu/YouTubeScraper/blob/master/README.md")
print("\033[92m[+] Telegram Group: \033[96mhttp://t.me/cyberclans\033[0m")
