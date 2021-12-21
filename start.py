import requests
import os, sys
from colorama import init
from concurrent.futures import ThreadPoolExecutor, as_completed
init(autoreset=True)

def reverseip(ip):
	try:
		onx = requests.get("https://soulapizy.000webhostapp.com/zerorev/?ip=" + ip)
		if "null" in onx.text:
			print('\r\033[91m  Got Nothing\033[0m »»————> ' + ip)
			bad.append(ip)
		else:
			print('\r\033[92m  Got {0} Domain\033[0m »»————> {1}'.format(str(len(onx.text)), ip))
			good.append(ip)
			open('domain.txt','a').write(str(onx.text)+'\n')
	except:
		pass
		
def subdomain(domain):
	try:
		zny = requests.get("https://soulapizy.000webhostapp.com/zerorev/?domain=" + domain)
		if "null" in zny.text:
			print('\r\033[91m  Got Nothing\033[0m »»————> ' + domain)
			bad.append(domain)
		else:
			print('\r\033[92m  Got {0} Domain\033[0m »»————> {1}'.format(str(len(zny.text)), domain))
			good.append(domain)
			open('subdomain.txt','a').write(str(zny.text)+'\n')
	except:
		pass
			

def tlds(dom):
	try:
		xny = requests.get("https://soulapizy.000webhostapp.com/zerorev/?tlds=" + dom)
		if "null" in xny.text:
			print('\r\033[91m  Got Nothing\033[0m »»————> ' + dom)
			bad.append(dom)
		else:
			print('\r\033[92m  Got {0} Subdomain\033[0m »»————> {1}'.format(str(len(xny.text)), dom))
			good.append(dom)
			open('tlds.txt','a').write(str(xny.text)+'\n')
	except:
		pass
			

def domtoip(domtip):
	try:
		ook = requests.get("https://soulapizy.000webhostapp.com/zerorev/?getip=" + domtip)
		if domtip in ook.text:
			print('\r\033[91m  BAD\033[0m »»————> ' + domtip)
			bad.append(domtip)
		else:
			print('\r\033[92m  GOOD\033[0m »»————> {0}'.format(domtip))
			good.append(domtip)
			open('ips.txt','a').write(str(ook.text))
			open('http-ips.txt','a').write("http://"+str(ook.text))
	except:
		pass
			
zerorev = """ 
\033[1;35;40m

▒███████▒▓█████  ██▀███   ▒█████   ██▀███  ▓█████ ██▒   █▓    ██ ▄█▀ ██▓▄▄▄█████▓
▒ ▒ ▒ ▄▀░▓█   ▀ ▓██ ▒ ██▒▒██▒  ██▒▓██ ▒ ██▒▓█   ▀▓██░   █▒    ██▄█▒ ▓██▒▓  ██▒ ▓▒
░ ▒ ▄▀▒░ ▒███   ▓██ ░▄█ ▒▒██░  ██▒▓██ ░▄█ ▒▒███   ▓██  █▒░   ▓███▄░ ▒██▒▒ ▓██░ ▒░
  ▄▀▒   ░▒▓█  ▄ ▒██▀▀█▄  ▒██   ██░▒██▀▀█▄  ▒▓█  ▄  ▒██ █░░   ▓██ █▄ ░██░░ ▓██▓ ░ 
▒███████▒░▒████▒░██▓ ▒██▒░ ████▓▒░░██▓ ▒██▒░▒████▒  ▒▀█░     ▒██▒ █▄░██░  ▒██▒ ░ 
░▒▒ ▓░▒░▒░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░░ ▒░ ░  ░ ▐░     ▒ ▒▒ ▓▒░▓    ▒ ░░   
░░▒ ▒ ░ ▒ ░ ░  ░  ░▒ ░ ▒░  ░ ▒ ▒░   ░▒ ░ ▒░ ░ ░  ░  ░ ░░     ░ ░▒ ▒░ ▒ ░    ░    
░ ░ ░ ░ ░   ░     ░░   ░ ░ ░ ░ ▒    ░░   ░    ░       ░░     ░ ░░ ░  ▒ ░  ░      
  ░ ░       ░  ░   ░         ░ ░     ░        ░  ░     ░     ░  ░    ░           
░                                                     ░                          

\033[0;37;40m
\033[1;32;40m
Tool Information :
	❖ Name : Zero Reverse Kit
	❖ Description : Fastest Reverse Kit Tool!
	❖ Creator : Soul Kings
	❖ Telegram : @soul_kings
	❖ Version : 1.0 [FREE]
	[!] NOTE : Don't selling this tool!

Join our telegram channel : @raid_store


 [ 1 ] Reverse IP <————«« Unlimited Reverse IP\n [ 2 ] Get Subdomain List <————«« Get all subdomains for a given domain\n [ 3 ] Get tlds <————«« Get all tlds found for a given domain\n [ 4 ] Domain to IP (Support Url, Domain & Subdomain) <————«« Get IP from domain, url or subdomain \n\033[0;37;40m
""" 
good=[]
bad=[]
print(zerorev)
pilih = input('Enter number : ')
list=[reverseip,subdomain,tlds,domtoip]
if int(pilih) not in range(1,5):exit("\033[91m Invalid number, please enter between 1-5 number. ")
files = input('[!] List (example : list.txt) : ')
thrd = int(input("[!] Threads : "))
ofx= []
with open(files) as combo:
	for line in combo.readlines():
		if len(line) > 3:
			ofx.append(line.strip())
try:
	def runner():
		threads= []
		with ThreadPoolExecutor(max_workers=thrd) as thread:
			for couple in ofx:
				threads.append(thread.submit(list[int(pilih)-5],couple))
				
	runner()
	print("\033[92m  Total Good : " + str(len(good)) + "\033[0m\n\033[1;35;40m  Total Bad : " + str(len(bad)) + "\033[1;35;40m")
except Exception as e:
	print(e)
