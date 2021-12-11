# -*- coding: utf-8 -*-

import os
import sys
import fileinput

N = '\033[0m'
D = '\033[90m'
W = '\033[1;37m'
B = '\033[1;34m'
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'

ask = G + '[' + W + '?' + G + '] '
sukses = G + '[' + W + '√' + G + '] '
eror = R + '[' + W + '!' + R + ']'

banner = """
{}         _debo_{}        _________________
{}        mrDEBO02{}      |                 |
{}       @p~qp~~qDe{}   ._| {}Encrypt Decrypt {}|
{}       M{}({}@{})({}@{}) {}M|{}  /  |_________________|
{}       @,{}----.{}BO|{}_/
{}      DE^{}\__/{}  bOO
     DEb        DeBo
    dEB          dEBo
   dEB            DEBo
   DEB            DEBO
{}   DeB            debO
{} __|'\ .        |\{}dE bOO
{} |    `.       | `' \{}dB
{}_)      \.{}___.{},|     .'
\____   ){}MRDEBO{}|   .'
     `-'       `--'

{}{}╔════════════════════════════════════════╗\n\033[1;97m{}{}║\033[1;93m* \033[1;97mAuthor  \033[1;91m: \033[1;96mMR.DEBO \033[1;97m                    ║\n\033[1;97m║\033[1;93m* \033[1;97mGithub  \033[1;91m: \033[1;96mhttps://github.com/MrDebo\033[1;97m   ║\n\033[1;97m║\033[1;93m* \033[1;97mFB      \033[1;91m: \033[1;92m\033[4mhttps://fb.me/mas.debo.02\033[0m   \033[1;97m║\n\033[1;97m║\033[1;93m* \033[1;97mVersion \033[1;91m: \033[1;92m\033[4m2.2\033[0m                         \033[1;97m║\n\033[1;97m{}{}╚════════════════════════════════════════╝

""".format(D,W,D,W,D,W,Y,W,D,W,D,W,D,W,D,W,D,Y,D,W,D,Y,D,G,W,G,D,G,W,G,Y,D,Y,D,Y,D,Y,D,Y)

banner2 = """
   {}[{}1{}]{} Encrypt      {}[{}2{}]{} Decrypt
""".format(G,W,G,W,G,W,G,W)

print banner
print banner2

def dekrip():
   try:
       sc = raw_input(ask + W + "Script " + G + "> " + W)
       f = open(sc,'r')
       filedata = f.read()
       f.close()

       newdata = filedata.replace("eval","echo")

       out = raw_input(ask + W + "Output" + G + " > " + W)
       f = open(out,'w')
       f.write(newdata)
       f.close()

       os.system("touch tes.sh")
       os.system("bash " + out + " > tes.sh")
       os.remove(out)
       os.system("mv -f tes.sh " + out)
       print (sukses + "Done..")

   except KeyboardInterrupt:
       print (eror + " Stopped!")
   except IOError:
       print (eror + " File Not Found!")

def enkrip():
   try:
       script = raw_input(ask + W + "Script " + G + "> " + W)
       output = raw_input(ask + W + "Output " + G + "> " + W)
       os.system("bash-obfuscate " + script + " -o " + output )
       print (sukses + "Done..")
   except KeyboardInterrupt:
       print (eror + " Stopped!")
   except IOError:
       print (eror + " File Not Found!")


takok = raw_input(W + "Pilih" + G + " > ")

if takok == "1" or takok == "01":
   enkrip()
elif takok == "2" or takok == "02":
   dekrip()
else:
   print (eror + " Wrong input")
