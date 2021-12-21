#============== Moudles ===============#
import requests
from licensing.models import *
from licensing.methods import Key, Helpers
from colorama import Fore, Style, Back
from multiprocessing.dummy import Pool
import multiprocessing, time, datetime, ctypes
import re
import sys
import random
import time
import os
import threading
import queue, time
import urllib3, urllib
from datetime import datetime
from licensing.models import *
from licensing.methods import Key, Helpers
import requests, re, sys, random, os
from colorama import Fore, Back, init
from colorama.initialise import init
import timeit
from threading import Thread
count = len(open('list.txt').readlines(  ))
countlive = 0
countdd = 0
countall2 = 0
countrec = 0

init(autoreset=True)
from random import choice

init()
class bounce():
    countlive = 0
    countdd = 0
    countall2 = 0
    countrec = 0
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    live = '"Status":"Valid"'.encode()
    die = '"Status":"Invalid"'.encode()
    error = '"Status":"ConnectionFail"'.encode()
    inputQueue = queue.Queue()
    def __init__(self):            
        def slowprint(s):
            for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(1. / 10)
        def logo():
            init(autoreset=True)
            from random import choice
            os.system('cls')
            clear = "\x1b[0m"
            colors = [36, 32, 34, 35, 31, 37]

            x = """ 

                        ██╗  ██╗███╗   ███╗ █████╗ ██████╗ ██╗   ██╗███████╗██╗ 
                        ╚██╗██╔╝████╗ ████║██╔══██╗██╔══██╗██║   ██║██╔════╝██║ 
                         ╚███╔╝ ██╔████╔██║███████║██████╔╝██║   ██║█████╗  ██║ 
                         ██╔██╗ ██║╚██╔╝██║██╔══██║██╔══██╗╚██╗ ██╔╝██╔══╝  ██║ 
                        ██╔╝ ██╗██║ ╚═╝ ██║██║  ██║██║  ██║ ╚████╔╝ ███████╗███████╗
                            ╚═╝  ╚═╝╚═╝ ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚══════╝ 
                                                    [+]Support: @xmarval_support [+]
                                                    [+]Channel: @xMarvel_OfficIal[+] 

                                      +-------- With Great Power Comes Great Toolz! --------+

        			                  """
            for N, line in enumerate(x.split("\n")):
                sys.stdout.write(" \x1b[1;%dm%s%s\n " % (random.choice(colors), line, clear))
                time.sleep(0.05)

        logo()
        bl = Fore.BLACK
        wh = Fore.WHITE
        yl = Fore.YELLOW
        red = Fore.RED
        gr = Fore.GREEN
        ble = Fore.BLUE
        res = Style.RESET_ALL
        init(autoreset=True)
        self.mailist = input(f'{gr}  Give Me Your List{wh}/{red}root> {gr}${res} ')
        self.thread = '20'
        self.countList = len(list(open(self.mailist)))
        self.clean = 'n'
        if self.clean == 'y':
            self.clean_rezult()
        print('')

    def save_to_file(self, nameFile, x):
        kl = open(nameFile, 'a+')
        kl.write(x)
        kl.close()

    def clean_rezult(self):
        open('live.txt', 'w').close()
        open('die.txt', 'w').close()
        open('unknown.txt', 'w').close()

    def post_email(self, eml):
        try:
            r = requests.get('https://verify.gmass.co/verify?email='+eml+'&key=52d5d6dd-cd2b-4e5a-a76a-1667aea3a6fc',headers={'User-Agent': self.ua})
            if self.live in r.content:
                return 'live'
            elif self.error in r.content:
                return 'error'
            elif self.die in r.content:
                return 'die'
            else:
                return 'unknown'
        except:
            return 'unknown'

    def chk(self):
        while 1:
            global countall2
            global countdd
            global countlive
            global countrec
            eml = self.inputQueue.get()
            rez = self.post_email(eml)

            if rez == 'die':
                countall2 += 1
                countdd += 1
                print(Fore.CYAN + f'[Bounce Checker 1.0]' + Fore.WHITE + ' | ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + Fore.RED + f" | {eml} | Die  [ [ {countlive}/{count} ]")       
                ctypes.windll.kernel32.SetConsoleTitleW(f"[Bounce Checker 1.0] [ @xMarvel_OFFiCiAL] {countall2}/{count} | Live : {countlive} Recheck :{countrec} | Die : {countdd}")
                self.save_to_file('die.txt', eml+'\n')
            elif rez == 'live':
                countall2 += 1
                countlive += 1
                print(Fore.CYAN + f'[Bounce Checker 1.0]' + Fore.WHITE + ' | ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + Fore.GREEN + f" | {eml} | live  [ [ {countlive}/{count} ]")       
                ctypes.windll.kernel32.SetConsoleTitleW(f"[Bounce Checker 1.0] {countall2}/{count} | Live : {countlive} Recheck :{countrec} | Die : {countdd}")
                self.save_to_file('live.txt', eml+'\n')
            elif rez == 'unknown':
                countall2 += 1
                countdd += 1
                print(Fore.CYAN + '[Bounce Checker 1.0]' + Fore.WHITE + ' | ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + Fore.RED + f" | {eml} | die [  {countdd}/{count} ]")
                self.save_to_file('die.txt', eml+'\n')
            elif rez == 'error':
                countall2 += 1
                countdd += 1
                print(Fore.CYAN + '[Bounce Checker 1.0]' + Fore.WHITE + ' | ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + Fore.RED + f" | {eml} | error [  {countdd}/{count} ]")
                self.save_to_file('error.txt', eml+'\n')
            else:
                print('contact @xMarval_support')
            self.inputQueue.task_done()

    def run_thread(self):
        for x in range(int(self.thread)):
            t = threading.Thread(target=self.chk)
            t.setDaemon(True)
            t.start()
        for y in open(self.mailist, 'r').readlines():
            self.inputQueue.put(y.strip())
        self.inputQueue.join()

    def finish(self):
        print('')
        print('Checking', self.countList, 'emails has been Checked by xMarvel Checker')
        print('')
        print('Live Emails    : ', len(list(open('live.txt'))), 'emails')
        print('Die  Emails   : ', len(list(open('die.txt'))), 'emails')
        print('')
        input('Enter To Exit --> ')


heh = bounce()
heh.run_thread()
heh.finish()
