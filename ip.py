#! /usr/bin/python3
# AUTHOR : E55db081d05f58a
# SOURCE : https://pastebin.com/5zkdQWZj

import os,sys,random

if sys.platform == "linux":
    os.system('clear')
elif sys.platform == "windows":
    os.system('cls')

banner = """
\033[31;1m\t\t  ___ ____   ____            
\033[31;1m\t\t |_ _|  _ \ / ___| ___ _ __  
\033[31;1m\t\t  | || |_) | |  _ / _ \ '_ \ 
\033[31;1m\t\t  | ||  __/| |_| |  __/ | | |
\033[31;1m\t\t |___|_|    \____|\___|_| |_|
\033[0m
\033[34m\t\tAUTHOR :\033[37m E55db081d05f58a\033[0m
\033[34m\t\tSOURCE :\033[37m https://pastebin.com/5zkdQWZj\033[0m
\033[34m\t\tREBORN :\033[37m F4c3r100\033[0m

\033[31;1mNOTICE: \033[0m\033[33;3;5mTHIS TOOL WAS WRITTEN IN PYTHON2 AND IS CONVERTED TO PYTHON3\033[0m
"""

def gen():
    b = os.urandom(32);
    rs = random.SystemRandom();
    r_i = rs.randint(0, sys.maxsize);
    a = str(r_i >> 24 & 0xFF);
    b =  str(r_i >> 16 & 0xFF);
    c =  str(r_i >> 8 & 0xFF);
    d =  str(r_i & 0xFF);
    octe = r_i%3;
    ip = a+"."+b+"."+c+"."+d
    return ip

def save_result(content):
    content = str(content) + "\n"
    temp = open("IPs-Generated.txt", "a+")
    temp.write(content)
    temp.close()
  
def main():
    print(banner)
    times = int(input("\033[37;1mHow many IPs do you want ?:\033[34m "))
    question = input("\033[37;1mRemove old file?\033[34m[\033[32mY\033[37m/\033[31mN\033[34m]\033[37m: ")
    if question == "Y" or question == "y":
        os.remove("IPs-Generated.txt")
    
    print("")
    for i in range(1,int(times)):
        ip = gen();
        print(f"\033[0m\033[34m[\033[32m{i}\033[34m|\033[32m{int(times)}\033[34m] \033[37mGenerated IP : \033[32m{ip}\033[0m")
        save_result(ip)

    filepath = os.getcwd() + "/IPs-Generated.txt"
    print(f"\n\033[34m[\033[32m+\033[34m] \033[37mIPs saved to \033[32m{filepath}\033[37m.\n")
  
if __name__=="__main__":
    main()