#curl -sqH'Accept: application/json' 'https://leakix.net/search?q=*&scope=service'|jq
import requests, json
import os
from colorama import Fore
from multiprocessing.dummy import Pool

jkt48 = {
  'api-key':'GG2BlpFVpRg3tg6Hr8NIrtJHRXGdMkliEJwUWTrhMVliHvvK', # change your api key
  'Accept':'application/json'
}

banner ="""

                                                                  .-'''-.             
              .---..---.                                         '   _    \           
/|        .--.|   ||   |             _..._                     /   /` '.   \          
||        |__||   ||   |           .'     '.                  .   |     \  '          
||        .--.|   ||   |          .   .-.   .              .| |   '      |  '.-,.--.  
||  __    |  ||   ||   |    __    |  '   '  |    __      .' |_\\    \\     / / |  .-. | 
||/'__ '. |  ||   ||   | .:--.'.  |  |   |  | .:--.'.  .'     |`.   ` ..' /  | |  | | 
|:/`  '. '|  ||   ||   |/ |   \\ | |  |   |  |/ |   \\ |'--.  .-'   '-...-'`   | |  | | 
||     | ||  ||   ||   |`" __ | | |  |   |  |`" __ | |   |  |                | |  '-  
||\\    / '|__||   ||   | .'.''| | |  |   |  | .'.''| |   |  |                | |      
|/\\'..' /     '---''---'/ /   | |_|  |   |  |/ /   | |_  |  '.'              | |      
'  `'-'`                \\ \\._,\\ '/|  |   |  |\\ \\._,\\ '/  |   /               |_|      
                         `--'  `" '--'   '--' `--'  `"   `'-'                         
A Private Method to get fresh ips

"""
print (banner)
try:
	q = input(' root@DavidBilla:~# Query : ')
	thread = input('root@DavidBilla:~# Thread : ')
	DB = int(thread)
	VB = Pool(DB)
	if q:
		pass
	else:
		q = '*'
	all_page = 500
	for t in range(all_page):
		print((Fore.LIGHTGREEN_EX+'Page :')+str(t))
		u = 'https://leakix.net/search?page='+str(t)+'&q='+q+'&scope=leak'
		x = requests.get(u, headers=jkt48);
		try:
			j = json.loads(x.text)
			for z in j:
				if ':' in z:
					pass
				else:
					print(Fore.CYAN+z['ip'])
					fx = open("ips-result.txt", "a")
					fx.write(z['ip']+" \n")
					fx.close()
		except:
			print(Fore.RED+"Limit Page !")
			#exit()
except:
	print(Fore.RED+'Error'+Fore.WHITE)

