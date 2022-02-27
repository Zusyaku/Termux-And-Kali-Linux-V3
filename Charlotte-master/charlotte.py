import requests, httplib, urllib
import socket
from platform import system
import os
import sys, time
import re
import threading
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import Style
from colorama import init
init(autoreset=True)
fr  =   Fore.RED
fh  =   Fore.RED
fc  =   Fore.CYAN
fo  =   Fore.MAGENTA
fw  =   Fore.WHITE
fy  =   Fore.YELLOW
fbl =   Fore.BLUE
fg  =   Fore.GREEN
sd  =   Style.DIM
fb  =   Fore.RESET
sn  =   Style.NORMAL
sb  =   Style.BRIGHT

user = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0"}

url = "http://www.zone-h.org/archive/notifier="
urll = "http://zone-h.org/archive/published=0"
url2 = "http://www.defacers.org/onhold!"
url4 = "http://www.defacers.org/gold!"
cookie = {
	"ZHE" : "a41a46c4e461527677fb0c4720fdfd78",
	"PHPSESSID" : "p209s29a1uqm0dsbhf8d2b94c1"
	}


def zonehh():
	print("""
	    |---| Grabb Sites From Zone-h |--|
		\033[91m[1] \033[95mGrabb Sites By Notifier
		\033[91m[2] \033[95mGrabb Sites By Onhold
		""")
	sec = int(raw_input("Choose Section Onii Chan: "))
	if sec == 1:
		notf = raw_input("\033[95mEnter notifier: \033[92m")

		for i in range(1, 51):
			dz = requests.get(url + notf +"/page=" + str(i), cookies=cookie)
			dzz = dz.content
			print(url + notf +"/page=" + str(i))
			if '<html><body>-<script type="text/javascript"' in dzz:
				print("Onii Chan Please Enter Cookie")
				sys.exit()
			elif '<input type="text" name="captcha" value=""><input type="submit">' in dzz:
				print("Onii Chan Please Change Capcha In Zone-H")
				sys.exit()
			else:
				Hunt_urls = re.findall('<td>(.*)\n							</td>', dzz)
				if '/mirror/id/' in dzz:
					for xx in Hunt_urls:
						qqq = xx.replace('...','')
						print '    ['  + '*' + '] ' + qqq.split('/')[0]
						with open(notf + '.txt', 'a') as rr:
							rr.write("http://" + qqq.split('/')[0] + '\n')
				else:
					print("Grabb Sites Compleated Arigatou Onii Chan ^_^")
					sys.exit()

	elif sec == 2:
		print(":* __Grabb Sites By Onhold__ ^_^")
		for qwd in range(1, 51):
			rb = requests.get(urll + "/page=" + str(qwd) , cookies=cookie)
			dzq = rb.content

			if '<html><body>-<script type="text/javascript"' in dzq:
				print("Onii Chan Please Change Capcha In Zone-H")
				sys.exit()

			elif "captcha" in dzq:
				print("Onii Chan Please Change Capcha In Zone-H")
			else:
				Hunt_urlss = re.findall('<td>(.*)\n							</td>', dzq)
				for xxx in Hunt_urlss:
					qqqq = xxx.replace('...','')
					print '    ['  + '*' + '] ' + qqqq.split('/')[0]
					with open('onhold_zone.txt', 'a') as rrr:
						rrr.write("http://" + qqqq.split('/')[0] + '\n')
	else:
		print("Oh Shit Onii-Chan")




def clearscrn():
    if system() == 'Linux':
        os.system('clear')
    if system() == 'Windows':
        os.system('cls')
        os.system('color a')
clearscrn()

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4. / 100)

def helper4():
	clearscrn()
	banner = """\033[33m\033[91m\033[93m

	==========================================================
	=======================Chatlotte==========================
	=Author : LoliC0d3	Telegram : t.me/LoliC0d3	 =
	=Team   : PhobiaXploit	Facebook : Facebook.com/LoliC0d3 =
	==========================================================
"""
	print("""\033[91m

	==========================================================
	=======================Chatlotte==========================
	=Author : LoliC0d3	Telegram : t.me/LoliC0d3  	 =
	=Team   : PhobiaXploit	Facebook : Facebook.com/LoliC0d3 =
	==========================================================

    [+]1. Zone-H Grabber
			""")
	try:
		qq = int(raw_input("\033[91m[-] \033[90mroot@Charlotte~#\033[95m : \033[90m"))
		if qq == 1:
			clearscrn()
			print(banner)
			zonehh()

	except:
		pass
helper4()
