#!/usr/bin/python
import os, httplib
def banner():
    print '''
       _____ _          _ _   ______ _           _           
      / ____| |        | | | |  ____(_)         | |          
     | (___ | |__   ___| | | | |__   _ _ __   __| | ___ _ __ 
      \___ \| '_ \ / _ \ | | |  __| | | '_ \ / _` |/ _ \ '__|
      ____) | | | |  __/ | | | |    | | | | | (_| |  __/ |   
     |_____/|_| |_|\___|_|_| |_|    |_|_| |_|\__,_|\___|_|   '''
     
def clearing():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
banner()
website = raw_input('\n Enter Website >>>  ')
shells = ['/madspot.php','/mad.php','/404.php','/anon.php','/anonymous.php','/shell.php','/sh3ll.php','/madspotshell.php','/b374k.php','/c100.php','/priv8.php','/private.php','/cp.php','/cpbrute.php','/themes/404/404.php','/templates/atomic/index.php','/templates/beez5/index.php','/hacked.php','/r57.php','/wso.php','/WSO.php','/wso24.php','/wso26.php','/wso404.php','/sym.php','/symsa2.php','/sym3.php','/whmcs.php','/whmcskiller.php','/cracker.php','/1.php','/2.php','/sql.php','/gaza.php','/database.php','/a.php','/d.php','/dz.php','/cpanel.php','/system.php','/um3r.php','/zone-h.php','/c22.php','/root.php','/r00t.php','/doom.php','/dam.php','/killer.php','/user.php','/wp-content/plugins/disqus-comment-system/disqus.php','/cpn.php','/shelled.php','/uploader.php','/up.php','/xd.php','/d00.php','/h4xor.php','/tmp/mad.php','/tmp/1.php','/wp-content/plugins/akismet/akismet.php','/images/stories/w.php','/w.php','/downloads/dom.php','/templates/ja-helio-farsi/index.php','/wp-admin/m4d.php','/d.php']
foundshells = []

for shell in shells:
    site = website.replace('http://','')
    host = site + shell
    conn = httplib.HTTPConnection(site)
    conn.connect()
    request = conn.request('GET',shell)
    response = conn.getresponse()
    if response.status == 200:
        print '\n\t[+] Shell found %s \n' %host
        foundshells.append(host)
    else:
        print '[-] Not Found %s ' %host
fpth = os.getcwd()
fpth2 = fpth + '/found.txt'
fob = open(fpth2,'w')
fob.close()
fob = open(fpth2,'a')
fob.writelines(foundshells)
print 'Found shells saved on found.txt'
raw_input('\n Press enter to exit ... ')
exit()
