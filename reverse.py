import socket
import threading
from multiprocessing import Pool 
from multiprocessing.dummy import Pool as ThreadPool
from colorama import Fore, init, Style
init(autoreset=True)
try:
  open('ips.txt', 'a')
except:
  pass

def domaintoip(listnya):
  try:
    getip = socket.gethostbyname(listnya)
    if getip in open('ips.txt', 'r').read():
      pass
    else:
      print "Retrieve IP: {}{}{}".format(Fore.YELLOW, Style.BRIGHT, getip)
      open('ips.txt', 'a').write(getip+'\n')
  except:
    pass
  
print "{}{}MASS DOMAIN TO IP".format(Fore.YELLOW, Style.BRIGHT)
listnya = open(raw_input(Fore.RED+Style.BRIGHT+"Give Me list to get IP's : "),'r').read().replace('http://', '').replace('https://', '').splitlines()
Thread = raw_input(Fore.WHITE+'Thread :~# ')
pool = ThreadPool(int(Thread))
pool.map(domaintoip, listnya)
pool.close()
pool.join()