#!/usr/bin/python3 

import requests
import os
import time
import sys
import threading
import queue
import socket
import ast
from re import findall as grep
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

def banner():
	os.system('clear')
	print("""
\033[31m██╗██████╗    ████████╗ ██████╗  ██████╗ ██╗     ███████╗
██║██╔══██╗   ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
██║██████╔╝█████╗██║   ██║   ██║██║   ██║██║     ███████╗
██║██╔═══╝ ╚════╝██║   ██║   ██║██║   ██║██║     ╚════██║
██║██║           ██║   ╚██████╔╝╚██████╔╝███████╗███████║
╚═╝╚═╝           ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
                                                         
\033[35;1m   .- - - - - - - - - .- - - - - - - - - - - - - - .
\033[35m   |                   |                            | 
\033[35m   | \033[34m[\033[32m1\033[34m] \033[37m- \033[33mReverse IP  \033[35m| \033[34m[\033[32m2\033[34m] \033[37m- \033[33mGet IP From URL List \033[35m|
\033[35m   |                   |                            |
\033[35m   | - - - - - - - - - '- - - - - - - - - - - - - - |
\033[35m   |                   |                            |
\033[35m   | \033[34m[\033[32m4\033[34m] \033[37m- \033[33mIP Ranger   \033[35m| \033[34m[\033[32m3\033[34m] \033[37m- \033[33mGet URL From IP List \033[35m|
\033[35m   |                   |                            |
\033[35m   '- - - - - - - - - -'- - - - - - - - - - - - - - '


\033[34mReverse IP : 

\033[37mIf you want to reverse IP then you will get domains.
You just need a big list of ip addresses to reverse them manually.


\033[34mGet IP From URL List:

\033[37mIf you want from URLs the IPs you gonna use this self.module.


\033[34mGet URL From IP List:

\033[37mThis will give you URLs from a ip list.


\033[34mIP Ranger:

\033[37mIP Ranger create ip ranges from ex.: 192.168.0.1 to 192.168.0.255
		\n\n""")



class main():
	inputQueue = queue.Queue()
	
	def __init__(self):
		banner()
		self.module = input("\033[34m[\033[33m*\033[34m] \033[37mEnter Option:\033[36m ")
		exp = input("\033[34m[\033[33m*\033[34m] \033[37mIP List or Webiste List ? \033[34m[\033[32mWEBSITE=1 \033[37m| \033[32mIP=2\033[34m]:\033[36m ")
		if exp == "1":
			self.combo = input("\033[34m[\033[33m*\033[34m]\033[37m Input URL List:\033[32m ")
			self.thread = input("\033[34m[\033[33m*\033[34m]\033[37m Input threads:\033[32m ")
			self.countList = len(list(open(self.combo)))

		elif exp == "2":
			self.combo = input("\033[34m[\033[33m*\033[34m]\033[37m Input IP List:\033[32m ")
			self.thread = input("\033[34m[\033[33m*\033[34m]\033[37m Input threads:\033[32m ")
			self.countList = len(list(open(self.combo)))

	def result(self, fname, sx):
		o = open(fname, "a+")
		o.write(sx)
		o.close()

	def reverse_ip(self,cmb):

		session = requests.session()
		global item
		ip = cmb
		r = session.get("https://dnslytics.com/",timeout=3)
		cookies = "'__cfduid': '{}'".format(r.cookies['__cfduid'])
		cookies = "{"+cookies+"}"
		cookies = ast.literal_eval(cookies)

		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0','Accept': '*/*','Accept-Language': 'en-US,en;q=0.5','Referer': 'https://dnslytics.com/reverse-ip/3.225.76.86','Content-Type': 'application/x-www-form-urlencoded','Origin': 'https://dnslytics.com','DNT': '1','Connection': 'keep-alive','Upgrade-Insecure-Requests': '1','TE': 'Trailers'}
		data = "'reverseip': '{}'".format(ip)
		data = "{"+data+"}"
		data = ast.literal_eval(data)
		response = session.post('https://dnslytics.com/reverse-ip',timeout=3, headers=headers, cookies=cookies, data=data)
		lists = grep('<input type="hidden" name="domsearch" value="(.*?)">',response.text)
		for item in lists:
			if "." in item:
				return "live",item				
			elif not "." in item:
				lists.remove(item)
				return "dead"

	def get_ip_from_domain(self,cmb):
		site = cmb
		o = socket.gethostbyname(site)
		try:
			o
			return 'live',o

		except Exception:
			return 'dead'

	def get_url_from_ip(self,cmb):
		ip = cmb
		session = requests.session()
		try:
			url = "https://dnschecker.org/"
			req = session.get(url, timeout=3)
			__cfduid = req.cookies['__cfduid']
			cookies = "'__cfduid':'{}'".format(__cfduid)
			cookies = "{"+cookies+"}"
			cookies = ast.literal_eval(cookies)
			headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0','Accept': 'application/json, text/javascript, */*; q=0.01','Accept-Language': 'en-US,en;q=0.5','csrftoken': 'null','X-Requested-With': 'XMLHttpRequest','Origin': 'https://dnschecker.org','DNT': '1','Connection': 'keep-alive','Referer': 'https://dnschecker.org/ip-to-hostname.php','Cache-Control': 'max-age=0','TE': 'Trailers'}
			csrf = session.post('https://dnschecker.org/ajax_files/gen_csrf.php', timeout=3, headers=headers, cookies=cookies)
			c = grep('"csrf":"(.*?)"',csrf.text)[0]
			headerss = f"'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0','Accept': 'application/json, text/javascript, */*; q=0.01','Accept-Language': 'en-US,en;q=0.5','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','csrftoken': '{c}','X-Requested-With': 'XMLHttpRequest','Origin': 'https://dnschecker.org','DNT': '1','Connection': 'keep-alive','Referer': 'https://dnschecker.org/ip-to-hostname.php?query={ip}'"
			header = "{"+headerss+"}"
			data = f"'ip': '{ip}'"
			data = "{"+data+"}"
			ss = session.post('https://dnschecker.org/ajax_files/ip_to_hostname.php', timeout=3, headers=headers, cookies=cookies, data=data)
			domain = grep('"hostname":"(.*?)"',ss.text)[0]
			return 'live',domain
		except Exception as e:
			print(e)
			return 'dead'

	def ipranger(self,cmb):
		try:
			ip = cmb
			x = ip.split(".")
			x.pop(3)
			ip = ".".join(x)
			for i in range(1,255):
				rangek = f"{ip}.{i}"
				return 'live',rangek

		except Exception as e:
			print(e)
			return 'dead'

	def chk(self):
		while 1:
			cmb = self.inputQueue.get()
			if self.module == "1":
				result = self.reverse_ip(cmb)
			if self.module == "2":
				result = self.get_ip_from_domain(cmb)
			if self.module == "3":
				result = self.get_url_from_ip(cmb)
			if self.module == "4":
				result = self.ipranger(cmb)

			if result == 'dead':
				self.result("die.txt", cmb+"\n")
				if self.module == "1":
					print(f"\033[34m[\033[32m*\033[34m] \033[37mREVERSE IP - \033[31m{cmb} \033[37m| \033[37mURL - \033[31mNOT FOUND \033[37m| \033[34m[\033[33m(\033[31mDEAD\033[33m)\033[34m]")
				if self.module == "2":
					print(f"\033[34m[\033[32m*\033[34m] \033[37mDOMAIN - \033[31m{cmb} \033[37m| \033[37mIP - \033[31mNOT FOUND \033[37m| \033[34m[\033[33m(\033[31mDEAD\033[33m)\033[34m]")
				if self.module == "3":
					print(f"\033[34m[\033[32m*\033[34m] \033[37mIP - \033[31m{cmb} \033[37m| \033[37mURL - \033[31mNOT FOUND \033[37m| \033[34m[\033[33m(\033[31mDEAD\033[33m)\033[34m]")
				if self.module == "4":
					print(f"\033[34m[\033[32m*\033[34m] \033[37mIP RANGER - \033[31m{cmb} \033[37m| \033[37mIP RANGE - \033[31mNOT FOUND \033[37m| \033[34m[\033[33m(\033[31mDEAD\033[33m)\033[34m]")

			if result == 'live':
				if self.module == "1":
					item = self.reverse_ip()
					print(f"\033[34m[\033[32m*\033[34m] \033[37mREVERSE IP - \033[32m{cmb} \033[37m| \033[37mURL - \033[32m{item} \033[37m| \033[34m[\033[33m(\033[32mLIVE\033[33m)\033[34m]")
					self.result("reversed_ip.txt", cmb)
				if self.module == "2":
					o = self.get_ip_from_domain()
					print(f"\033[34m[\033[32m*\033[34m] \033[37mDOMAIN - \033[32m{cmb} \033[37m| \033[37mIP - \033[32m{o} \033[37m| \033[34m[\033[33m(\033[32mFOUND\033[33m)\033[34m]")
					self.result("ip_from_domain.txt", cmb)

				if self.module == "3":
					domain = self.get_url_from_ip()
					print(f"\033[34m[\033[32m*\033[34m] \033[37mIP - \033[32m{cmb} \033[37m| \033[37mDOMAIN - \033[32m{domain} \033[37m| \033[34m[\033[33m(\033[32mFOUND\033[33m)\033[34m]")
					self.result("url_from_ip.txt", cmb)
				if self.module == "4":
					rangek = self.ipranger()
					print(f"\033[34m[\033[32m*\033[34m] \033[37mIPRANGER - \033[32m{cmb} \033[37m| \033[37mDOMAIN - \033[32m{rangek} \033[37m| \033[34m[\033[33m(\033[32mFOUND\033[33m)\033[34m]")
					self.result("ipranges.txt", cmb)


	def run_thread(self):
		for x in range(int(self.thread)):
			t = threading.Thread(target=self.chk)
			t.setDaemon(True)
			t.start()
		for y in open(self.combo, 'r').readlines():
			self.inputQueue.put(y.strip())
		self.inputQueue.join()

main().run_thread()
