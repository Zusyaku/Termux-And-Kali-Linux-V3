#!/usr/bin/python
# Create by Kingtebe
import os,re,sys,time,json,random
try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    exit("# Module bs4 and requests not installed!")

C = "\x1b[1;96m"
P = "\x1b[1;97m"
B = "\x1b[1;90m"
K = "\x1b[1;93m"
H = "\x1b[0;92m"
M = "\x1b[1;91m"

user = [
 "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 RuxitSynthetic/1.0 v7526349725985634568 t3659150847447165606 athe94ac249 altpriv cvcv=2 smf=0",
 "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 RuxitSynthetic/1.0 v7047530094306945960 t4109306862226254733 athe94ac249 altpriv cvcv=2 smf=0",
 "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v2699432088408596775 t1865758485807943117 ath1fb31b7a altpriv cvcv=2 smf=0",
 "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v8656436791680077687 t5654132216862743399 ath259cea6f altpriv cvcv=2 smf=0",
]

def countdown(second):
    while second:
        mins,secs = divmod(second,60)
        timer = "\x1b[1;96m[\x1b[1;93m•\x1b[1;96m] \x1b[1;97mWaiting ⟨\x1b[0;92m{:02d}:{:02d}\x1b[1;97m⟩ ".format(mins,secs)
        print(timer,end="\r")
        time.sleep(1)
        second -= 1

def login(email):
    global ses
    acak = random.choice(user)
    with requests.Session() as ses:
         ses.headers.update({"user-agent":acak,"x-requested-with":"XMLHttpRequest"})
         url = ses.get("https://pastebin.com/raw/AVMzMcq1").text
         req = BeautifulSoup(ses.post(url,data={"email":email,"start":"Start+Now"}).text,"html.parser")
         balance = req.find("div",class_="form-group").text
         return balance.strip()

def claim(email,captcha):
    masuk = login(email)
    os.system('cls' if os.name=='nt' else 'clear')
    print(f"\n {C}╔═╗{P}┌─┐┌─┐┌┬┐┌─┐┬┌┐┌  {C}╔╗ {P}┬ ┬┬  ┬ {K}' {P}┌─┐\n {C}║  {P}├─┤├─┘ │ ├─┤││││  {C}╠╩╗{P}│ ││  │   {P}└─┐\n {C}╚═╝{P}┴ ┴┴   ┴ ┴ ┴┴┘└┘  {C}╚═╝{P}└─┘┴─┘┴─┘ {P}└─┘ {P}v{C}1.0\n{B}~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~~ ~~~ ~~~ ~~~{P}\n{C}[{K}•{C}] {P}Author {B}: {P}Kingtebe\n{C}[{K}•{C}] {P}Github {B}: {P}github/Musk-ID\n{C}[{K}•{C}] {P}Group  {B}: {P}https://t.me/Captain_bulls"+f"\n\n{C}[{K}+{C}] {P}Login as {H}"+ str(email).replace(f"{email}"[4:10],"xxxxxx")+f"\n{C}[{K}+{C}] {P}Balance {H}"+ str(masuk)+f"\n{C}[{K}+{C}] {P}Starting bot...\n");time.sleep(1.5)
    while True:
        print(f"{C}[{K}!{C}] {P}Trying bypass captcha   ",flush=True,end="\r")
        req = ses.post(captcha,data={"cID":"0","rT":"1","tM":"light"}).json()
        satu = req[0];dua = req[1];tiga = req[2];empat = req[3];lima = req[4]
        req = ses.post(captcha,data={"cID":"0","pC":satu,"rT":"2"})
        if req.status_code != 200:
           continue
        url = ses.get("https://pastebin.com/4LrHgqVq").text
        req = ses.post(url,data={"captcha-hf":satu,"captcha-idhf":"0","claim":"Claim+Now"}).text
        timer = re.search("FlipClock(([^>]+)),\s{",req).group(1).removeprefix("(")
        par = BeautifulSoup(req,"html.parser")
        if par.find("div",class_='alert alert-success').text is None:
           print(f"{C}[{K}!{C}] {P}Bypass captcha failed    ",flush=True,end="\r")
           continue
        else:
           earn = par.find("div",class_='alert alert-success').text
           low = login(email)
           print(f"{C}[{K}✓{C}] {P}"+ str(earn)+ f" {B}- {P}"+ str(low))
           countdown(int(timer))

def mainbot():
    os.system('cls' if os.name=='nt' else 'clear')
    print(f"\n {C}╔═╗{P}┌─┐┌─┐┌┬┐┌─┐┬┌┐┌  {C}╔╗ {P}┬ ┬┬  ┬ {K}' {P}┌─┐\n {C}║  {P}├─┤├─┘ │ ├─┤││││  {C}╠╩╗{P}│ ││  │   {P}└─┐\n {C}╚═╝{P}┴ ┴┴   ┴ ┴ ┴┴┘└┘  {C}╚═╝{P}└─┘┴─┘┴─┘ {P}└─┘ {P}v{C}1.0\n{B}~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~~ ~~~ ~~~ ~~~{P}\n{C}[{K}•{C}] {P}Author {B}: {P}Kingtebe\n{C}[{K}•{C}] {P}Github {B}: {P}github/Musk-ID\n{C}[{K}•{C}] {P}Group  {B}: {P}https://t.me/Captain_bulls\n")
    email = input(f"{C}[{K}•{C}] {P}Input email{B}: {P}")
    if email in ("",""):exit(f"{C}[{K}!{C}] {P}Jangan kosong bangsat\n")
    elif "@" not in email:exit(f"{C}[{K}!{C}] {P}Isi email menggunakan format {P}({K}@{P}) bangsat\n")
    with requests.Session() as ses:
         url = ses.get("https://pastebin.com/raw/sKTDD2e0").text
         claim(email,url)

if __name__=='__main__':
    mainbot()
