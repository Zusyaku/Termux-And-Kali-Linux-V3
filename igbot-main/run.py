#si coeg ngintip wae
import os,sys,time,requests,json,re,random
from time import sleep
from concurrent.futures import ThreadPoolExecutor
b="\033[94m"
c="\033[96m"
g="\033[92m"
r="\033[91m"
p="\033[1;97m"
d="\033[00m"
ab="\033[90m"
dn=f"{d}[{g}√{d}]{p}"
er=f"{d}[{r}!{d}]{p}"
pr=f"{d}[{c}?{d}]{p}"
ig="https://www.instagram.com{}"
id_find=[]
id_flwr=[]
id_flwg=[]
id_people=[]
done=0
die=0
#####################awalan####################
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def baner():
    clear()
    print(f"""{p}

           {c}╔╗ {p}┌─┐┌┬┐  {c}╦{p}┌─┐┌─┐┬ ┬
           {c}╠╩╗{p}│ │ │   {c}║{p}│ ┬├┤ ├─┤
           {c}╚═╝{p}└─┘ ┴   {c}╩{p}└─┘└─┘┴ ┴
{ab}-----------------------------------------------
{d}Donate   : {g}https://saweria.co/FahmiDevs
{d}Message  : {g}https://wa.me/62881024612817
{d}Restapi  : {g}https://ainxbot-id.herokuapp.com
{d}Youtube  : {g}https://youtube.com/KuhakuTermux
{d}Github   : {g}https://github.com/Ainx-BOT
{d}Facebook : {g}https://facebook.com/kang.ngeue.313
{ab}-----------------------------------------------""")

def process(ok,fail):
    for i in list("\|/-•"):
        print(f"\r{p}[{c}{i}{p}]success : {g}{ok}{p} failed : {r}{fail}",end="")
        sleep(0.2)

def cblg():
    lg=input(f"{pr}Coba lagi? ({d}{c}y{d}/{c}n{p}) : {c}")
    if lg == "y" or lg == "Y":
        os.system("python run.py")
    elif lg == "n" or lg == "N":
        baner()
        sys.exit(er+"Bye Bro jangan lupa kasih bintang github saya:)")
    else:
         print(er+"Pilih yg bener coeg")
         sleep(1)
         cblg()

def dct1(url):
    data=re.findall(r'window._sharedData = (.*?);</script>',url)[0]
    data=json.loads(data)
    return data

def dct2(url,type):
    data=re.findall(r"window.__additionalDataLoaded\W'"+type+"',(.*?)\W;</script>",url)[0]
    data=json.loads(data)
    return data
#################logininfo#######################
def login():
    try:
       ck=open("cookies").read()
    except FileNotFoundError:
       ck=input(f"{er}Put your cookies\n{pr} {ab}>>> {c}")
    cokie={'cookie':f'{ck}'}
    req=ses.get(ig.format("/"),cookies=cokie)
    js=dct1(req.text)
    if js["config"]["viewer"] == None:
       print(f"{er}Invalid cookies")
       sleep(2)
       os.system("rm cookies")
       os.system("python run.py")
    else:
       with open("cookies","w") as lg:
            lg.write(cokie["cookie"])
       name=js["config"]["viewer"]["username"]
       return {"name":name,"cookie":cokie["cookie"],"csrf":req.cookies["csrftoken"]}

def userinfo(user):
    req=ses.get(ig.format(f"/{user}/?__a=1"),cookies=cokie).text
    js=json.loads(req)["graphql"]["user"]
    try:
        name=js["full_name"]
    except:
        name=None
    try:
        id=js["id"]
    except:
        id=None
    try:
        flwr=js["edge_followed_by"]["count"]
    except:
        flwr=None
    try:
        flwg=js["edge_follow"]["count"]
    except:
        flwg=None
    print(f"""{p}
Login as  : {c}{name}{p}
ID        : {c}{id}{p}
Followers : {c}{flwr}{p}
Following : {c}{flwg}{p}
{ab}-----------------------------------------------{p}""")
####################dump######################
def post_people(url):
    req=ses.get(url,cookies=cokie).text
    js=json.loads(req)
    if not "data" in js:
       id=js["graphql"]["user"]["id"]
       data=js["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"]
       next=js["graphql"]["user"]["edge_owner_to_timeline_media"]["page_info"]
    else:
       id=js["data"]["user"]["edge_owner_to_timeline_media"]["edges"][0]["node"]["owner"]["id"]
       data=js["data"]["user"]["edge_owner_to_timeline_media"]["edges"]
       next=js["data"]["user"]["edge_owner_to_timeline_media"]["page_info"]
    for x in data:
        id_people.append(x["node"]["id"])
        print(f"\r{pr}Getting Data : {c}{len(id_people)}",end="")
    if next.get("has_next_page") == True:
       next=next.get("end_cursor").replace("==","%3D%3D")
       post_people(f"https://www.instagram.com/graphql/query/?query_hash=8c2a529969ee035a5063f2fc8602a0fd&variables=%7B%22id%22%3A%22{id}%22%2C%22first%22%3A12%2C%22after%22%3A%22{next}%22%7D")
    return id_people

def flwr_people(url,id):
    req=ses.get(url,headers={"Host":"i.instagram.com","origin":"https://www.instagram.com","user-agent":us,"accept":"*/*","x-asbd-id":"198387","x-ig-app-id":"1217981644879628","referer":"https://www.instagram.com/"+username,"accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},cookies=cokie).text
    data=json.loads(req)
    for x in data["users"]:
        id_flwr.append(str(x["pk"])+"|"+x["full_name"])
        print(f"\r{pr}Getting Data : {c}{len(id_flwr)}",end="")
    if data["big_list"] == True:
       next=data["next_max_id"]
       flwr_people(f"https://i.instagram.com/api/v1/friendships/{id}/followers/?count=12&max_id={next}&search_surface=follow_list_page",id)
    return id_flwr

def flwg_people(url,id):
    req=ses.get(url,headers={"Host":"i.instagram.com","origin":"https://www.instagram.com","user-agent":us,"accept":"*/*","x-asbd-id":"198387","x-ig-app-id":"1217981644879628","referer":"https://www.instagram.com/"+username,"accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},cookies=cokie).text
    data=json.loads(req)
    for x in data["users"]:
        id_flwg.append(str(x["pk"])+"|"+x["full_name"])
        print(f"\r{pr}Getting Data : {c}{len(id_flwg)}",end="")
    if data["big_list"] == True:
       next=data["next_max_id"]
       flwg_people("https://i.instagram.com/api/v1/friendships/"+id+"/following/?count=12&max_id="+next,id)
    return id_flwg
#################mainbot######################
def like(id):
    global done,die
    req=ses.post(f"https://www.instagram.com/web/likes/{id}/like/",headers={"Host":"www.instagram.com","content-length":"0","origin":"https://www.instagram.com","x-requested-with":"XMLHttpRequest","content-type":"application/x-www-form-urlencoded","accept":"*/*","user-agent":us,"x-asbd-id":"198387","x-csrftoken":cstoken,"x-ig-app-id":"1217981644879628","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},cookies=cokie).text
    if "ok" in req:
      done+=1
    else:
      die+=1
    process(done,die)

def komen(id,text):
    global done,die
    req=ses.post(f"https://www.instagram.com/web/comments/{id}/add/",data={"comment_text":text,"replied_to_comment_id":""},headers={"Host":"www.instagram.com","origin":"https://www.instagram.com","x-requested-with":"XMLHttpRequest","content-type":"application/x-www-form-urlencoded","accept":"*/*","user-agent":us,"x-asbd-id":"198387","x-csrftoken":cstoken,"x-ig-app-id":"1217981644879628","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},cookies=cokie).text
    if text or "ok" in req:
       done+=1
    else:
       die+=1
    process(done,die)

def find(url):
    req=ses.get(url,cookies=cokie).text
    js=json.loads(req)
    if js["users"] == []:
       print(f"{er}People not found")
       sleep(2)
       menu()
    else:
       for x in js["users"]:
           id_find.append(x["user"]["username"]+"|"+x["user"]["full_name"])
           print(f"\r{pr}Getting User : {c}{len(id_find)}",end="")
       return id_find
def flw(id,name):
    global done,die
    req=requests.post(f"https://www.instagram.com/web/friendships/{id}/follow/",headers={"Host":"www.instagram.com","content-length":"0","origin":"https://www.instagram.com","x-requested-with":"XMLHttpRequest","x-instagram-ajax":"6de3d310f878","content-type":"application/x-www-form-urlencoded","accept":"*/*","user-agent":us,"x-asbd-id":"198387","x-csrftoken":cstoken,"x-ig-app-id":"1217981644879628","referer":"https://www.instagram.com/"+username+"/followers/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},cookies=cokie).text
    if "following" in req:
       print(f"\r{dn}Follback {ab}=> {c}{name}")
       done+=1
    else:
       die+=1
    process(done,die)
def unflw(id,name):
   global done,die
   req=requests.post("https://www.instagram.com/web/friendships/"+id+"/unfollow/",headers={"Host":"www.instagram.com","content-length":"0","origin":"https://www.instagram.com","x-requested-with":"XMLHttpRequest","x-instagram-ajax":"5e8fd79a0a83","content-type":"application/x-www-form-urlencoded","accept":"*/*","user-agent":us,"x-asbd-id":"198387","x-csrftoken":cstoken,"x-ig-app-id":"1217981644879628","referer":"https://www.instagram.com/"+username+"/following/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},cookies=cokie).text
   if "ok" in req:
      print(f"\r{dn}Unfollow {ab}=> {c}{name}")
      done+=1
   else:
      die+=1
   process(done,die)
def delpost(id):
    global done,die
    req=requests.post("https://www.instagram.com/create/"+id+"/delete/",headers={"Host":"www.instagram.com","content-length":"0","origin":"https://www.instagram.com","x-requested-with":"XMLHttpRequest","x-instagram-ajax":"5e8fd79a0a83","content-type":"application/x-www-form-urlencoded","accept":"*/*","user-agent":us,"x-asbd-id":"198387","x-csrftoken":cstoken,"x-ig-app-id":"1217981644879628","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},cookies=cokie).text
    if '"did_delete":true' in req:
       done+=1
    else:
       die+=1
    process(done,die)
####################menu#######################
def menu():
    try:
       ainx=ses.get("https://www.instagram.com/p/CXPB5k2BvLX/",cookies=cokie).text
       js=dct2(ainx,"/p/CXPB5k2BvLX/")
       idainx=id=js["graphql"]["shortcode_media"]["id"]
       ses.post(f"https://www.instagram.com/web/likes/{idainx}/like/",headers={"Host":"www.instagram.com","content-length":"0","origin":"https://www.instagram.com","x-requested-with":"XMLHttpRequest","content-type":"application/x-www-form-urlencoded","accept":"*/*","user-agent":us,"x-asbd-id":"198387","x-csrftoken":cstoken,"x-ig-app-id":"1217981644879628","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},cookies=cokie)
       txt=["Hi bang fahmi tools nya keren banget!","tools nya sangat berguna!","Hi i'm user tools Ainx-BOT","semoga rejeki bang fahmi di lancarin amin","tools yang sangat bagus!"]
       random_komen=random.choice(txt)
       ses.post(f"https://www.instagram.com/web/comments/{idainx}/add/",data={"comment_text":random_komen,"replied_to_comment_id":""},headers={"Host":"www.instagram.com","origin":"https://www.instagram.com","x-requested-with":"XMLHttpRequest","content-type":"application/x-www-form-urlencoded","accept":"*/*","user-agent":us,"x-asbd-id":"198387","x-csrftoken":cstoken,"x-ig-app-id":"1217981644879628","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},cookies=cokie)
       ses.post("https://www.instagram.com/web/friendships/51135840524/follow/",headers={"Host":"www.instagram.com","content-length":"0","origin":"https://www.instagram.com","x-requested-with":"XMLHttpRequest","x-instagram-ajax":"6de3d310f878","content-type":"application/x-www-form-urlencoded","accept":"*/*","user-agent":us,"x-asbd-id":"198387","x-csrftoken":cstoken,"x-ig-app-id":"1217981644879628","referer":"https://www.instagram.com/apzfahmi/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},cookies=cokie)
    except:
       pass
    baner()
    userinfo(username)
    print(f"""{p}
{c}01{ab}. {p}spam like in people
{c}02{ab}. {p}spam comment in people
{c}03{ab}. {p}spam comment in target post
{c}04{ab}. {p}mass follow back
{c}05{ab}. {p}mass unfollow all following
{c}06{ab}. {p}mass delete post
{c}07{ab}. {p}find people
{c}08{ab}. {p}remove useragent & cookies
{c}00{ab}. {p}exit
{ab}-----------------------------------------------""")
    pilih_menu()

def pilih_menu():
    choice=input(f"{pr}Select : {c}")
    if choice == "00" or choice == "0":
       baner()
       sys.exit(f"{er}Bye bro jangan lupa kasih bintang github saya:)")
    elif choice == "01" or choice == "1":
       name=input(f"{er}Put your username target\n{pr} {ab}>>> {c}")
       usr=post_people(ig.format(f"/{name}/?__a=1"))
       print()
       try:
           jum=input(f"{pr}Like Count : {c}")
           jum=int(jum)
       except ValueError:
           print(f"{er}Masukin jumlah post yg mau di likenya coeg")
           jum=input(f"Like Count : {c}")
           jum=int(jum)
       print(f"{ab}-----------------------------------------------")
       try:
           with ThreadPoolExecutor(max_workers=30) as ex:
                for x in usr[:jum]:
                    ex.submit(like,(x))
           print()
           cblg()
       except Exception as e:
           print()
           print(f"{er}{e}")
           cblg()
    elif choice == "02" or choice == "2":
       name=input(f"{er}Put your username target\n{pr} {ab}>>> {c}")
       usr=post_people(ig.format(f"/{name}/?__a=1"))
       print()
       txt=input(f"{pr}Comment Here : {c}")
       try:
           jum=input(f"{pr}Comment Count : {c}")
           jum=int(jum)
       except ValueError:
           print(f"{er}Masukin jumlah post yg mau di komennya coeg")
           jum=input(f"{pr}Comment Count : {c}")
           jum=int(jum)
       print(f"{ab}-----------------------------------------------")
       try:
           with ThreadPoolExecutor(max_workers=30) as ex:
                for x in usr[:jum]:
                    ex.submit(komen,(x),(txt))
           print()
           cblg()
       except Exception as e:
           print()
           print(f"{er}{e}")
           cblg()
    elif choice == "03" or choice == "3":
       url=input(f"{er}Put your url post target\n{pr}{ab} >>> {c}")
       if "ig_web_copy_link" in url:
          url=url.replace("?utm_source=ig_web_copy_link","")
       req=ses.get(url,cookies=cokie).text
       ty=url.replace("https://www.instagram.com","")
       js=dct2(req,ty)
       id=js["graphql"]["shortcode_media"]["id"]
       txt=input(f"{pr}Comment Here : {c}")
       try:
          jum=input(f"{pr}Comment Count : {c}")
          jum=int(jum)
       except ValueError:
          print(f"{er}Masukin jumlah komen nya coeg")
          jum=input(f"{pr}Comment Count : {c}")
          jum=int(jum)
       print(f"{ab}-----------------------------------------------")
       try:
          with ThreadPoolExecutor(max_workers=30) as ex:
              for _ in range(jum):
                 ex.submit(komen,(id),(txt))
          print()
          cblg()
       except Exception as e:
          print()
          print(f"{er}{e}")
          cblg()
    elif choice == "04" or choice == "4":
         id=ses.get(ig.format(f"/{username}/?__a=1"),cookies=cokie).json()["graphql"]["user"]["id"]
         usr=flwr_people(f"https://i.instagram.com/api/v1/friendships/{id}/followers/?count=12&search_surface=follow_list_page",id)
         print()
         try:
             jum=input(f"{pr}Follback Count : {c}")
             jum=int(jum)
         except ValueError:
             print(f"{er}Masukin jumlah yg mau di follback nya coeg")
             jum=input(f"{pr}Follback Count : {c}")
             jum=int(jum)
         print(f"{ab}-----------------------------------------------")
         try:
            with ThreadPoolExecutor(max_workers=30) as ex:
                 for x in usr[:jum]:
                     user=x.split("|")
                     ex.submit(flw,(user[0]),(user[1]))
            print()
            cblg()
         except Exception as e:
            print()
            print(f"{er}{e}")
            cblg()
    elif choice == "05" or choice == "5":
         id=ses.get(ig.format(f"/{username}/?__a=1"),cookies=cokie).json()["graphql"]["user"]["id"]
         usr=flwg_people(f"https://i.instagram.com/api/v1/friendships/{id}/following/?count=12",id)
         print()
         try:
            jum=input(f"{pr}Unfollow Count : {c}")
            jum=int(jum)
         except ValueError:
            print(f"{er}Masukin jumlah yg mau di unfollow nya coeg")
            jum=input(f"{pr}Unfollow Count : {c}")
            jum=int(jum)
         print(f"{ab}-----------------------------------------------")
         try:
            with ThreadPoolExecutor(max_workers=30) as ex:
                for x in usr[:jum]:
                    user=x.split("|")
                    ex.submit(unflw,(user[0]),(user[1]))
            print()
            cblg()
         except Exception as e:
            print()
            print(f"{er}{e}")
            cblg()
    elif choice == "06" or choice == "6":
         usr=post_people(ig.format(f"/{username}/?__a=1"))
         print()
         try:
            jum=input(f"{pr}Delete Count : {c}")
            jum=int(jum)
         except ValueError:
            print(f"{er}Masukin jumlah post yg mau di hapus nya coeg")
            jum=input(f"{pr}Delete Count : {c}")
            jum=int(jum)
         print(f"{ab}-----------------------------------------------")
         try:
            with ThreadPoolExecutor(max_workers=30) as ex:
                 for x in usr[:jum]:
                     ex.submit(delpost,(x))
            print()
            cblg()
         except Exception as e:
            print()
            print(f"{er}{e}")
            cblg()
    elif choice == "07" or choice == "7":
       name=input(f"{er}Find by name\n{pr} {ab}>>> {c}")
       usr=find(ig.format(f"/web/search/topsearch/?context=blended&query={name}&rank_token=0.4226156467468136"))
       print()
       print(f"{ab}-----------------------------------------------")
       for x in usr:
           user=x.split("|")
           print(f"{p}Username : {c}{user[0]}\n{p}Nickname : {c}{user[1]}")
           print(f"{ab}-----------------------------------------------")
       print(f"{er}Please copy the username")
       input(f"{p}[ {c}Press Enter To Back {p}]")
       os.system("python run.py")
    elif choice == "08" or choice == "8":
       print(f"{ab}-----------------------------------------------")
       print(f"\r{er}Please wait...")
       os.system("rm useragent")
       os.system("rm cookies")
       ses.headers.clear()
       print(f"\r{dn}Done.")
       sleep(2)
       os.system("python run.py")
    else:
       print(f"{er}Wrong input")
       pilih_menu()
if __name__=="__main__":
   baner()
   try:
       us=open("useragent").read()
   except FileNotFoundError:
       us=input(f"{er}Put your user-agent\n{pr} {ab}>>> {c}")
   with open("useragent","w") as ug:
        ug.write(us)
   ses=requests.Session()
   ses.headers.update({"user-agent":us})
   try:
       masuk=login()
       username=masuk["name"]
       cstoken=masuk["csrf"]
       cokie={'cookie':f'{masuk["cookie"]}'}
       menu()
   except Exception as e:
       sys.exit(f"{er}{e}")

