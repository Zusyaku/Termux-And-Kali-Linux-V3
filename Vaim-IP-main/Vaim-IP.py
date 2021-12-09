import datetime
import os, sys
import random
from time import sleep
#colours ------------code's--- 
r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
d = "\033[2;37m"
R = "\033[1;41m"
Y = "\033[1;43m"
B = "\033[1;44m"
w = "\033[1;37m"
#------------------------------



#script banner--------------------------
logo = """\033[1;37m
\033[1;37m[!] \033[1;31mThis is use for Testing...
\033[1;37m
┌-=============================      -   
=      \033[1;31m . ┌──────── \033[1;37mVAIM-IP          -   
=  \033[1;31m .┌───  \033[1;37mB-HAT HACKERS ACTIVE NOW  -   \033[34m[✔] https://github.com/VaimpierOfficial    [✔]
\033[1;37m=    SCANING TOOL                    -   \033[34m[✔]            Version 1.0                 [✔]
\033[1;37m= \033[1;31m . └──── \033[1;37mBY Vaimpier Ritik         -   \033[91m[X] Please Don't Use For illegal Activity  [X]
\033[1;37m= \033[1;31m .     └─── \033[1;37mVERSION 1.0            -
\033[1;37m└-=============================      -
\033[1;31m    
Disclaimer: \033[1;32mthis tool is designed for Prank
	    testing in an authorized simulated cyberattack
	    Attacking targets without prior mutual consent
            is illegal!                                                               
\033[1;37m                                    
\033[97m """

#ALL comment are under tested so ignore him when i update it then its help me out to think better so thanks for using tool
#we will update soon
#we will add spoofing x bombing 
#soon
#by vaimpier ritik
#-------------------------------------------




#script banner fuction---
def banner():
    print(logo)

def bye():
	os.system("clear")
	banner()
	string = """ 
	\033[1;37mDeveloper  \033[1;34m: \033[1;31mVaimpier Ritik

	\033[1;37mGithub     \033[1;34m: \033[1;31mVaimpierOfficial

	\033[1;37mInstagram  \033[1;34m: \033[1;31mvaimpier_ritik

	\033[1;37mE-mail     \033[1;34m: \033[1;31mvaimpierritik@gmail.com  
	"""
	for letter in string:
	  sleep(0.01) 
	  sys.stdout.write(letter)
	  sys.stdout.flush()
	print("\n")

def backie():
	ritik_welcome = [

	'Thanks for using our tool', 
	'Keep using this tool Thanks Brother !!!', 
	'Bye dear :)', 
	'Hope you enjoy with this tool',
	'We are Vaimpier :) Bye',
	'Thankyou so much dear :)',
	'Keep learning keep hacking :)',
	'Bye :) Next Update soon',
	'We have many tools like this subscribe our channel to get more',
	'Have a Good day dear :) ',
	'Vaimpier Ritik says :) Thanks dear Bye :_)'


	]

	print(r+"└─"+w+"[!] "+y+random.choice(ritik_welcome))
	back=input(r+"..└─"+w+"\033[1;37mBack [ y / n ]: "+r)
	if back=='y' or back=='Y':
		os.system("clear")
		ip()
	if back=='n' or back=='N':
		backie()
	else:
		backie()

def ip():
	os.system("clear")
	banner()
	print(r+"└─"+w+"\033[1;37m[ 1 ] IP Track: ")
	print(r+"└─"+w+"\033[1;37m[ 2 ] Own IP Track: ")
	print(r+"└─"+w+"\033[1;37m[ 3 ] About: ")

	opp=int(input(r+"└─"+w+"\033[1;37mEnter Desire Option: "+r))	
	if opp==1:
		os.system("clear")
		banner()
		os.system("sudo php Vaimip.php")
	elif opp==2:
		os.system("sudo php Vaimip2.php")
	elif opp==3:
		bye()
		print("\n")
	else:
		ip()
	backie()

if __name__ == '__main__':
	ip()
	
	