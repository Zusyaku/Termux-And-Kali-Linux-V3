# -*- coding: utf-8 -*-
# Coded By Aang Ardiansyah-XD
# Created Date 14-11-2021
import requests, re, os, time

banner=(
""" 
\x1b[0;97m───▄▄─▄████▄▐▄▄▄▌ ● Author   : Aang Ardiansyah-XD
──▐──████▀███▄█▄▌ ● Github   : Gthub.com/AngCyber
▐─▌──█▀▌──▐▀▌▀█▀  ● Facebook : Facebook.com/clubfunbike
─▀───▌─▌──▐─▌
─────█─█──▐▌█

\x1b[0;91m support python2 & python3
							""")                                               
urls="https://business.facebook.com/business_locations"
_ses=requests.Session()

def real_time():
	from time import time
	return str(time()).split('.')[0]

def convert(cok):
	__for=(
			'datr='+cok['datr']
		)+';'+(
			'c_user='+cok['c_user']
		)+';'+(
			'fr='+cok['fr']
		)+';'+(
			'xs='+cok['xs'] )
	return __for
	
def save_agent(_agent):
	while True:
		try:
			_choic=raw_input("\x1b[0;93m(+) simpan user agent [Y/T] :\x1b[0;92m ")
		except:
			_choic=input("\x1b[0;93m(+) simpan user agent [Y/T] :\x1b[0;92m ")
		if _choic in ['ya', 'y', 'Y']:
			with open('agent.txt', 'w') as f:
				f.write(_agent)
				f.close()
				return
		elif _choic in ['t', 'T']:
			return
		else:
			continue

def email():
	os.system('clear')
	print(banner)
	print ('\x1b[0;96m CARA AGAR TIDAK TERKENA CHECKPOINT ')
	print (' LOGIN AKUN DI BROWSER TERLEBIH DAHULU ')
	print (' LALU CARI USER AGENT KETIK "MY USER AGENT" ')
	print (' DI BROWSER YANG SUDAH LOGIN AKUN FACEBOOK\n')
	try:
		_agent=open('agent.txt').read()
	except:
		try:
			_agent=raw_input("\x1b[0;93m(+) user agent :\x1b[0;92m ")
			save_agent(_agent)
		except:
			_agent=input("\x1b[0;93m(+) user agent :\x1b[0;92m ")
			save_agent(_agent)
	try:
		user=raw_input("\x1b[0;93m(+) email/username :\x1b[0;92m ")
		pw=raw_input("\x1b[0;93m(+) password       :\x1b[0;92m ")
	except:
		user=input("\x1b[0;93m(+) email/username :\x1b[0;92m ")
		pw=input("\x1b[0;93m(+) kata sandi       :\x1b[0;92m ")
	try:
		_head={
			'Host':'m.facebook.com',
				'cache-control':'max-age=0',
			'upgrade-insecure-requests':'1',
				'user-agent':_agent,
			'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'sec-fetch-mode':'navigate',
				'sec-fetch-user':'?1',
			'sec-fetch-dest':'document',
				'accept-encoding':'gzip, deflate',
			'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
		}
		try:
			r=_ses.get("https://m.facebook.com/", headers=_head).text.encode('utf-8')
		except:
			r=_ses.get("https://m.facebook.com/", headers=_head).text
		_head2={
			'Host':'m.facebook.com',
				'user-agent':_agent,
			'content-type':'application/x-www-form-urlencoded',
				'x-fb-lsd':re.search('name="lsd" value="(.*?)"', str(r)).group(1),
			'accept':'*/*',
				'origin':'https://m.facebook.com',
			'sec-fetch-site':'same-origin',
				'sec-fetch-mode':'cors',
			'sec-fetch-dest':'empty',
				'referer':'https://m.facebook.com/',
			'accept-encoding':'gzip, deflate',
				'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
		}
		payload={
			"fb_dtsg":re.search('{"token":"(.*?)"', str(r)).group(1),
				"lsd":re.search('name="lsd" value="(.*?)"', str(r)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(r)).group(1),
				"m_ts":re.search('name="m_ts" value="(.*?)"', str(r)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(r)).group(1),
				"try_number":"0",
			"unrecognized_tries":"0",
				"prefill_contact_point":user,
			"prefill_source":"browser_dropdown",
				"prefill_type":"contact_point",
			"first_prefill_source":"browser_dropdown",
				"first_prefill_type":"contact_point",
			"had_cp_prefilled":True,
				"had_password_prefilled":False,
			"is_smart_lock":False,
				"bi_xrwh":"0",
			"__dyn":"",
				"__csr":"",
			"__req":"2",
				"__a":"",
			"__user":"0",
				"email":user,
			"encpass":"#PWD_BROWSER:0:"+real_time()+":"+pw
		}
		_ses.post("https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100", headers=_head2, data=payload)
		cok=_ses.cookies.get_dict()
		if 'c_user' in (cok):
			_head={
				'Host':'business.facebook.com',
					'cache-control':'max-age=0',
				'upgrade-insecure-requests':'1',
					'user-agent':'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36',
				'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
					'content-type' : 'text/html; charset=utf-8',
				'accept-encoding':'gzip, deflate',
					'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
			}    
			_r=_ses.get(urls, headers=_head)
			_p=re.search('(EAAG\w+)', _r.text)
			_token=_p.group(1)
			if 'EAA' in _token:
				print('\n\x1b[0;93m(+) Cookie :\x1b[0;92m '+convert(cok))
				print('\x1b[0;93m(+) Token  :\x1b[0;92m '+_token )
				exit()
		elif 'checkpoint' in (cok):
			exit('\x1b[0;91m(×) Akun kena cekpoin ngab!!')
		else:
			print('\x1b[0;91m(×) email/password salah kentod!!')
			time.sleep(3)
			menu()
	except AttributeError:
		print('\x1b[0;91m(×) email/password kentod!!')
		time.sleep(3)
		menu()

def cookie():
	os.system('clear')
	print(banner)
	try:
		_cookie=raw_input('\x1b[0;93m(+) cookie :\x1b[0;92m ')
	except:
		_cookie=input('\x1b[0;93m(+) cookie :\x1b[0;92m ')
	try:
		_head={
			'Host':'business.facebook.com',
				'cache-control':'max-age=0',
			'upgrade-insecure-requests':'1',
				'user-agent':'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36',
			'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
				'content-type' : 'text/html; charset=utf-8',
			'accept-encoding':'gzip, deflate',
				'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
			'cookie': _cookie
		}         
		_r=_ses.get(urls, headers=_head)
		_p=re.search('(EAAG\w+)', _r.text)
		_h=_p.group(1)
		if 'EAA' in _h:
			exit('\x1b[0;93m(+) Token :\x1b[0;92m '+_h)
	except (AttributeError, requests.exceptions.TooManyRedirects):
		print('\x1b[0;91m(×) cookie salah !')
		time.sleep(3)
		menu()
		
def menu():
	os.system("clear")
	print (banner)
	print("\x1b[0;96m(01) email/password to cookie & token")
	print("(02) cookie to token")
	print("(03) hapus user agent\n")
	while True:
		try:
			_cho=raw_input("(+) pilih : ")
		except:
			_cho=input("(+) pilih : ")
		if _cho in ['01', '1']:
			exit(email())
		elif _cho in ['02', '2']:
			exit(cookie())
		elif _cho in ['03', '3']:
			os.system('rm -rf agent.txt')
			print('(~) sukses menghapus')
			time.sleep(3)
			menu()
		else:
			continue

if __name__ == '__main__':
	menu()