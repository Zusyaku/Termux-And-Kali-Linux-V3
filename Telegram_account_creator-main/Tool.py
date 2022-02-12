import os
RED='\033[31m'
RESET = "\033[0m"
GREEN='\033[32m'  
ORANGE= '\033[33m'
BLUE='\033[34m'
MAGENTA= '\033[35m'
CYAN='\033[36m'
WHITE= '\033[37m'
BLACK='\033[30m'
REDBG='\033[41m'
GREENBG='\033[42m'
ORANGEBG='\033[43m'  
BLUEBG='\033[44m'
MAGENTABG='\033[45m'
CYANBG='\033[46m'  
WHITEBG='\033[47m'
BLACKBG='\033[40m'
RESETBG='\e[0m\n'

def clr():
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')


banner = f"""{CYAN}                                 a8                         a8   
              ,dPYb,  ,dPYb,       ,d88    ,dPYb, ,dPYb,      ,d88   
              IP'`Yb  IP'`Yb      a8P88    IP'`Yb IP'`Yb     a8P88   
              I8  8I  I8  8I    ,d8" 88    I8  8I I8  8I   ,d8" 88   
              I8  8'  I8  8'   a8P'  88    I8  8' I8  8'  a8P'  88   
   ,ggggg,    I8 dP   I8 dP  ,d8"    88    I8 dP  I8 dP ,d8"    88   
  dP"  "Y8ggg I8dP    I8dP   888888888888  I8dP   I8dP  888888888888 
 i8'    ,8I   I8P     I8P            88    I8P    I8P           88   
,d8,   ,d8'  ,d8b,_  ,d8b,_          88   ,d8b,_ ,d8b,_         88   
P"Y8888P"    PI8"8888PI8"8888        88   8P'"Y888P'"Y88        88   
              I8 `8,  I8 `8,                                         
              I8  `8, I8  `8,                                        
              I8   8I I8   8I                                        
              I8   8I I8   8I                                        
              I8, ,8' I8, ,8'                                        
               "Y8P'   "Y8P'                                        
               
               {RESET}
               {RED}             OFF4ll4 Team       {RESET}

               {GREEN}      @offlin4ll4     @phoenix0l    {RESET}

Telegram Account Creator

Contact for getting tool :

Telegram : https://t.me/off4ll4

Telegram : https://t.me/offline4ll4

Telegram : https://t.me/phoenix0l

Youtube : https://www.youtube.com/channel/UCZm4QVtj2pYI2F5jjIoR95g

Instagram : https://www.instagram.com/off.line4ll4/
               """



clr()
print(banner)