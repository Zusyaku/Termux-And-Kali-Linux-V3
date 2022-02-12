import requests
from bs4 import BeautifulSoup
import os
import time
import random
import sys

Green="\033[1;33m"
Blue="\033[1;34m"
Grey="\033[1;30m"
Reset="\033[0m"
Red="\033[1;31m"
Purple="\033[0;35m"


os.system("clear")
print("# \033[1;34m[ 1 ] >> \033[1;36;40mTermux")
print("# \033[1;34m[ 2 ] >> \033[1;36;40mLinux")
print("# \033[1;34m[ 3 ] >> \033[1;36;40mOther")

op=int(raw_input("Options: "))

if(op==1):
 print "good."
elif(op==2):
 print "okay."
elif(op==3):
 print "succes."
