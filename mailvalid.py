import os,sys,requests,json

banner = """ 
\033[1;35;40m

 ██▓▒███████▒ ▄▄▄       ███▄    █  ▄▄▄       ███▄ ▄███▓ ██▓
▓██▒▒ ▒ ▒ ▄▀░▒████▄     ██ ▀█   █ ▒████▄    ▓██▒▀█▀ ██▒▓██▒
▒██▒░ ▒ ▄▀▒░ ▒██  ▀█▄  ▓██  ▀█ ██▒▒██  ▀█▄  ▓██    ▓██░▒██▒
░██░  ▄▀▒   ░░██▄▄▄▄██ ▓██▒  ▐▌██▒░██▄▄▄▄██ ▒██    ▒██ ░██░
░██░▒███████▒ ▓█   ▓██▒▒██░   ▓██░ ▓█   ▓██▒▒██▒   ░██▒░██░
░▓  ░▒▒ ▓░▒░▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░▓  
 ▒ ░░░▒ ▒ ░ ▒  ▒   ▒▒ ░░ ░░   ░ ▒░  ▒   ▒▒ ░░  ░      ░ ▒ ░
 ▒ ░░ ░ ░ ░ ░  ░   ▒      ░   ░ ░   ░   ▒   ░      ░    ▒ ░
 ░    ░ ░          ░  ░         ░       ░  ░       ░    ░  
    ░                                                      
\033[0;37;40m
\033[1;32;40m
Tool Information :
- Tool Name : Izanami Email Validator
- Creator : Soul Kings
- Telegram : @soul_kings
- Version : 1.0 [FREE]

Join our telegram channel : @raid_store
\033[0;37;40m
"""
api = "https://soulapizy.000webhostapp.com/emailvalidator/"

#Main
print(banner)

#Open Number List
filename = input("Input Email List (Exemple: list.txt) : ")
try:
    file = open(filename,"r")
except:
    sys.exit("[!] Error. No File Exist")
combo = file.readlines()
file.close()

for line in combo:
    line = line.strip()
    data = {"email": line}
    try:
        response = requests.post(api, data=data).text
    except:
        print("[!] Stopped.")
        combo.append(line)
        break
    if "Success" in response:
        print('\r[\033[92m ' + response + ' \033[0m] ')
        open('hits.txt','a').write(str(line)+'\n')
        open('full-hits.txt','a').write(str('[ ' + response + ' ]')+'\n')
    elif "Bad" in response:
        print('\r[\033[91mBad\033[0m] ' + line)
    else:
        print('\r[\033[91mBan\033[0m] ' + line)

print("Done....")