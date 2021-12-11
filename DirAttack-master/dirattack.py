#!/usr/bin/python3

from optparse import OptionParser
from datetime import datetime
from os import path,popen,system,getuid
from sys import argv,stdout
import urllib.request,re,sys,textwrap

"""

dirAttack V.0.1 (Free and Open source tools)

Author  : Ms.ambari
Youtube : 'https://www.youtube.com/channel/UCNMD5U02GFeWLqmrl_XSPGQ' (Ms.ambari)
Email   : ambari.developer@gmail.com
github  : /Ranginang67
---
Support dan dukung gua dengan cara subcribe ke channel yutub gua ya :)
agar gua bisa berkarya dan semangat untuk membuat segala sesuatu untuk kalian...
Jangan lupa juga check github gua. disana ada lumayan banyak tools tools yang bisa kalian gunakan.
oh iya kalian bisa gabung di grup wasap Ms.ambari official, Link ivite ada di channel yutub gua :)
kalian bisa bertanya seputar programing,Linux,Termux DLL.

"""

p = OptionParser("USAGE: "+path.basename(argv[0])+" -u <url> <options>")
p.add_option(
  "-u","--url",help="your target url https,http or www",action="store_true"
  )
p.add_option(
  "-w","--word",help="Your wordlist path",action="store_true"
  )
p.add_option(
  "-d","--wdef",help="Use default wordlist",action="store_true"
  )
p.add_option(
  "-r","--remove",help="To remove This tools from your system",action="store_true"
)
(options,args) = p.parse_args()

platform = "linux" if path.exists("/usr/bin/") else "termux"
data = {
  "linux":{
    "wordlist":"/usr/share/DirAttack/config/wordlist.txt"
  },
  "termux":{
    "wordlist":"/data/data/com.termux/files/usr/share/DirAttack/config/wordlist.txt"
  },
  "path":{
    "linux":"/usr/share/DirAttack/",
    "termux":"/data/data/com.termux/files/usr/share/DirAttack/"
  },
  "width":popen("stty size","r").read().split()[1]
}
if options.remove:
  if platform is "linux":
    if getuid() != 0:
      exit("Please run as root to remove this tool.")
    system("rm /usr/share/icons/dirattack.png && rm -rf /usr/share/applications/dirattack.desktop")
  if platform is "termux":
    system("rm -rf /data/data/com.termux/files/usr/bin/dirattack")
  system("rm -rf %s && rm -rf /usr/bin/dirattack"%data["path"][platform][0:len(data["path"][platform])-1])
  exit(0)

if not len(args) or not options.word and not options.wdef or not options.url:
  exit("Try: --help")

if options.url and options.word:
  data[platform]["wordlist"] = args[1]

data["site"] = args[0]

# check exists wordlist
if not path.exists(data[platform]["wordlist"]):
  exit("Error: Wordlist not found: "+data[platform]["wordlist"])

# check valid url
try:
  print(" * Checking URL ...",end="\r")
  urllib.request.urlopen(data["site"])
except Exception as err:
  if type(err).__name__ == "ValueError":
    exit("\033[KError: Invalid URL.")
  if type(err).__name__ == "HTTPError":
    exit("\033[KError: Site Forbidden")
  else:
    exit("\033[KError: URL does not exists")

with open(data[platform]["wordlist"],"r+") as w:
  w = w.readlines()
  print("\033[K"+\
    "-"*25\
    +"\n\n * Starting At{}{}\n * Target{}{}\n * With{}{}\n\n{}"\
  .format(": ".rjust(4),datetime.now().strftime("%H:%M:%S"),": ".rjust(9),data["site"],": ".rjust(11),str(len(w))+" Wordlist","-"*25))
  for i in open(data["path"][platform]+"config/filename.txt","r+").readlines():
    i = i.strip()
    for j in open(data["path"][platform]+"config/ext.txt","r+").readlines():
      j = j.strip()
      w.append(i+j)
  for wlist in set(w):
    wlist = wlist.strip()
    target = data["site"]+"/"+wlist
    if data["site"][len(data["site"]) -1] in ["/","//"]:
      target = data["site"]+wlist
    print(" "+textwrap.shorten("* Searching : %s"%target,width=int(data["width"])-5,placeholder="..."),end="\r")
    stdout.write("\033[K")
    try:
      urllib.request.urlopen(target)
    except Exception:
      pass
    except KeyboardInterrupt:
      exit()
    else:
      print("\033[1;32m * \033[0mFound {} {}".format(":".rjust(5),target))
