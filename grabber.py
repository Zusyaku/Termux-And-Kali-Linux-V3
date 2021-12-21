import requests
import re

def getlist():
	try:
		for i in range(15):
			i = int(i)+1
			header = {'User-agent':'Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; HM NOTE 1W Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.0.5.850 U3/0.8.0 Mobile Safari/534.30'}
			resp = requests.get('https://www.cubdomain.com/domains-registered-dates/'+str(i), headers=header).text
			pages = re.findall('">(.*?)</a>\n</div>\n<div class', resp)
			for data in pages:
				if '/' in data or '=' in data or 'Download Extension' in data:
					pass
				else:
					print(data)
					open('registered-data.txt','a').write(str(data)+'\n')
					registered.append(data)
	except:
		pass

def grabber():
	try:
		print("\t\033[92m [ ! ] Enter date format yyyy-mm-dd (Example: 2021-10-01) !")
		date = input('\tEnter registered date : ')
		hwm = input('\tHowmany page you want grab (Example: 15) : ')
		print("\033[0m")
		for i in range(int(hwm)):
			i = int(i)+1
			headr = {'User-agent':'Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; HM NOTE 1W Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.0.5.850 U3/0.8.0 Mobile Safari/534.30'}
			response = requests.get('https://www.cubdomain.com/domains-registered-by-date/'+str(date)+'/'+str(i), headers=headr).text
			page = re.findall('">(.*?)</a>\n</div>', response)
			for dom in page:
				if '/' in dom or '=' in dom or 'Download Extension' in dom:
					pass
				else:
					print(dom)
					open('domain.txt','a').write(str(dom)+'\n')
					domain.append(dom)
					pge.append(i)
	except:
		pass

banner = """ 
\033[1;35;40m


▒███████▒▓█████  ██▀███   ▒█████       ▄████  ██▀███   ▄▄▄       ▄▄▄▄    ▄▄▄▄   ▓█████  ██▀███  
▒ ▒ ▒ ▄▀░▓█   ▀ ▓██ ▒ ██▒▒██▒  ██▒    ██▒ ▀█▒▓██ ▒ ██▒▒████▄    ▓█████▄ ▓█████▄ ▓█   ▀ ▓██ ▒ ██▒
░ ▒ ▄▀▒░ ▒███   ▓██ ░▄█ ▒▒██░  ██▒   ▒██░▄▄▄░▓██ ░▄█ ▒▒██  ▀█▄  ▒██▒ ▄██▒██▒ ▄██▒███   ▓██ ░▄█ ▒
  ▄▀▒   ░▒▓█  ▄ ▒██▀▀█▄  ▒██   ██░   ░▓█  ██▓▒██▀▀█▄  ░██▄▄▄▄██ ▒██░█▀  ▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄  
▒███████▒░▒████▒░██▓ ▒██▒░ ████▓▒░   ░▒▓███▀▒░██▓ ▒██▒ ▓█   ▓██▒░▓█  ▀█▓░▓█  ▀█▓░▒████▒░██▓ ▒██▒
░▒▒ ▓░▒░▒░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒░▒░▒░     ░▒   ▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░▒▓███▀▒░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░
░░▒ ▒ ░ ▒ ░ ░  ░  ░▒ ░ ▒░  ░ ▒ ▒░      ░   ░   ░▒ ░ ▒░  ▒   ▒▒ ░▒░▒   ░ ▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░
░ ░ ░ ░ ░   ░     ░░   ░ ░ ░ ░ ▒     ░ ░   ░   ░░   ░   ░   ▒    ░    ░  ░    ░    ░     ░░   ░ 
  ░ ░       ░  ░   ░         ░ ░           ░    ░           ░  ░ ░       ░         ░  ░   ░     
░                                                                     ░       ░                 

\033[0;37;40m
\033[1;32;40m
\tTool Information :
\t❖ Tool Name : Zero Grabber
\t❖ Description : Mass grabbing site from cubdomain
\t❖ Creator : Soul Kings
\t❖ Telegram : @soul_kings
\t❖ Version : 1.0 [FREE]
\t[ ! ] NOTE : Don't selling this tool!

\tJoin our telegram channel : @raid_store
\n\t [ 1 ] Get Registered Data\n\t [ 2 ] Mass Grabbing Site\n
\033[0;37;40m
"""
registered=[]
domain=[]
pge=[]
print(banner)
pilih = input('\tEnter number : ')
if int(pilih) == 1:
	getlist()
	print("\n\033[92mGot  "+str(len(registered))+" Registered Date - saved: registered-date.txt\033[0m")
elif int(pilih) == 2:
	grabber()
	print("\n\033[92mGot  "+str(len(domain))+" Domain from - saved: domain.txt\033[0m")
else:
	print("\033[91mPlease input a valid number\033[0m")
	exit()