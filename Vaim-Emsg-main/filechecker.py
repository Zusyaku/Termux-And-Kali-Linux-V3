#modules---------
import os, sys
#----------------


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

#checking file values--
if int(len(email)) == int(len(password)) and int(len(host)) == int(len(port)):
	pass
else:
	os.system("clear")
	for j in range(0, 4):
		print(r+"└─"+w+"[!]"+r+"Bro try with delete your config file :)\n")
	os.system("bash setup.sh")
#-----------------------

print(w+"[ # ] "+r+"Good now add mail happy bombing :) \n")
os.system("bash config.sh")
