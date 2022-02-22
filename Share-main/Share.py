### Import module 
import os
try:
    import requests
except ImportError:
    print(" Module requests belum terinstall")
    os.system('pip install requests')
import os, sys, requests, time, json, datetime

# INI KOMBINASI WARNA OKH:V
O ='\x1b[1;96m' 
P ='\033[0;00m' 
J ='\033[0;33m'
S ='\033[0;00m'
N ='\x1b[0m' 
I ='\033[0;32m'
C ='\033[0;36m'
M ='\033[0;31m'
U ='\033[0;33m'
K ='\033[0;33m'
#P='\033[0;37m'
P='\033[00m'
h='\033[0;90m'
Q="\033[00m"
kk='\033[0;32m'
ff='\033[0;36m'
G='\033[0;36m'
p='\033[00m'
h='\033[0;90m'
Q="\033[00m"
i='\033[0;32m'
mm='\033[0;36m'
m='\033[0;31m'
O ='\033[0;33m'
H='\033[0;33m'
B ='\033[0;36m'
#P='\033[0;37m'
k ='\033[00m'
h ='\033[0;90m'
Q ="\033[00m"
kk='\033[0;32m'
ff='\033[0;36m'
R ='\033[0;36m'                                                                                                              
h ='\033[0;90m'
W ="\033[0;00m"
i ='\033[0;32m'
mm='\033[0;36m'
m ='\033[0;31m'
c ='\033[0;32m'
C ='\033[0;32m'
O ='\033[0;33m'
H ='\033[0;33m'
G ='\033[0;36m'
p ='\033[0;00m'
b ='\033[0;36m'                                          
m ='\033[0;31m'
N ='\x1b[0m'                                              
I ='\033[0;32m'
k ='\033[0;33m'
o ='\033[0;31m'                                           
U ='\033[0;33m'
K ='\033[0;33m'
# BUAT JALAN
def jalan(z):
    for e in z :
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.0001)
        
# Buat pembersih
def clear():
    os.system("cls" if os.name == "nt" else "clear")
    
# BUAT BANNER
banner = """
\033[1;36m______________                        ________                _____
__  ___/___  /_ ______ ______________ ___  __ \______ __________  /_
_____ \ __  __ \_  __ `/__  ___/_  _ \__  /_/ /_  __ \__  ___/_  __/
____/ / _  / / // /_/ / _  /    /  __/_  ____/ / /_/ /_(__  ) / /_
/____/  /_/ /_/ \__,_/  /_/     \___/ /_/      \____/ /____/  \__/

\033[0;00m[\033[0;33m•\033[0;00m]\033[0;36m-------------------------------------------------------------\033[0;00m[\033[0;33m•\033[0;00m]
\033[0;36m |
\033[0;00m[\033[0;33m•\033[0;00m]\033[0;00m AUTHOR   \033[0;35m: \033[0;32mJEECK X NANO,\033[0;33m MR.RISKY, ALDI BACHTIAR 
\033[0;00m[\033[0;33m•\033[0;00m]\033[0;00m GITHUB   \033[0;35m: \033[0;00mhttps://github.com/Jeeck-XN
\033[0;00m[\033[0;33m•\033[0;00m]\033[0;00m WHATSAPP \033[0;35m: \033[0;00m+6281392505882
\033[0;36m |
"""

# Buat menu 
def menu():
    clear()
    jalan(banner)
    token = input("\033[0;00m[\033[0;33m•\033[0;00m]\033[0;00m Masukan token : ")
    print("\033[0;00m[\033[0;33m•\033[0;00m]\033[0;00m Token berhasil")
#p    bot()
    try:
        k = requests.get('https://graph.facebook.com/me?access_token='+token) #<<<<<<<<< INI BUAT NGECEK NAMA USER DLL YA GUYS
        nan = json.loads(k.text)
        name = nan['name']
        idfb = nan['id']
        link = nan['link']
        email = nan['email']
        print("\033[0;00m[\033[0;33m•\033[0;00m]\033[0;00m Berhasill Login")
        time.sleep(3)
    except:
        print("\033[0;00m[\033[0;33m•\033[0;00m]\033[0;00m Token modar")
        os.sys.exit()
    os.system("clear")
    jalan(banner) # <<<<<< INFORMASI AKUN :V LAWACK KEK GITU AINK DI BILANK RECOD :V DASAR
    print("\033[0;00m[\033[0;33m•\033[0;00m]\033[0;00m Username  : %s "%(name))
    print("\033[0;00m[\033[0;33m•\033[0;00m]\033[0;00m Userid    : %s "%(idfb))
    print("\033[0;00m[\033[0;33m•\033[0;00m]\033[0;00m Link      : %s "%(link))
    print("\033[0;00m[\033[0;33m•\033[0;00m]\033[0;00m Email     : %s "%(email))
    print(" \033[0;36m| ")
    nanoid = input("\033[0;00m[\033[0;33m•\033[0;00m]\033[0;00m Id postingan : ")
    waktu = int(input("\033[0;00m[\033[0;33m•\033[0;00m]\033[0;00m Waktu pershare : "))
    print(" \033[0;36m| ")
    asu = 0
    asu = asu + 1
    while True:
        requests.get('https://graph.facebook.com/v2.0/me/feed?method=post&privacy={"value":"EVERYONE"}&message=&link=https://mbasic.facebook.com/'+str(nanoid)+'&access_token='+str(token)) #<<<<<<<<< INI URL UNTUK TANCAP GAS KE SHARE
        print("\033[0;36m[\033[0;33m•\033[0;36m]\033[0;33m <<<•>>> \033[0;36m[\033[0;00m BERHASILL \033[0;36m]\033[0;33m <<<•>>> \033[0;36m[ \033[0;00m%s \033[0;36m]"%(str(nanoid)))
#        
menu()
