# -*- coding: utf-8 -*-

"""
SQLVuln
-------
simple tool to scanning sql injection vulnerability
and this tool is very easy to use.

Author: Ms.ambari
Github: /Ranginang67
YouTube: Ms.ambari
"""

import sys

if sys.version_info < (3,0):
    sys.exit("Please use python 3")

import os, re
import urllib.request
import random
import urllib3
import datetime

class SqlScan:

    __counter = 1
    __maxPage = 2
    __hasil = []
    __vuln = []
    __nothing = []
    __error = []
    
    __mysql_error = [ # do you have another error of sql ? add here ...
        "You have an error in your SQL syntax",
        "MySQL server version for the right syntax to use near",
        "SELECT * FROM"]

    @classmethod
    def dorking(cls,dork=None,max_page=2):
        cls.__maxPage = max_page
        while(cls.__counter < cls.__maxPage):
            try:
                url = "http://www1.search-results.com/web?q="+dork+"&page="+str(cls.__counter)
                req = urllib.request.urlopen(url);
                results = req.read()
                results = results.decode("utf8")
                regx = re.findall(r"<a.class=\"algo-[\D]*\".href=\"(.*?)\"",results)
                for i in regx:
                    cls.__hasil.append(i)
                cls.__counter += 1
            except (Exception, KeyboardInterrupt):
                exit(0)

    # set color
    __danger = "\033[31m"
    __success = "\33[32m"
    __reset = "\033[0m"
    
    @classmethod
    def show(cls,text,exp=None):
        x = None
        if exp in ["err","error","e"]: x = "[ "+cls.__danger+"✕ "+cls.__reset+"] ERROR "+cls.__danger+"=> "+cls.__reset
        else: x = "["+cls.__success+" ✓"+cls.__reset+" ] OK! "+cls.__success+"=> "+cls.__reset
        print(str(x)+" "+text)

    @classmethod
    def scan(cls):
        date = "="*20 + " " + datetime.datetime.now().strftime("%d %h-%m-%Y") # Print this variable to showing date and time now.
        try:
            (dork, max_p) = str(input("Enter your Dork [ ex: product.php?id= ]: ")), int(input("Max page [ integer ]: "))
            cls.dorking(dork,max_p)
            for target in set(cls.__hasil):
                try:
                    req = urllib.request.urlopen(target+"'")
                    html = req.read()
                    html = html.decode("utf8")
                    for sql_error in cls.__mysql_error:
                        if re.search(r""+sql_error.lower(),html.lower()):
                            cls.__vuln.append(target)
                            cls.show(str(target))
                            break
                        else:
                            cls.__nothing.append(target)
                            continue
                except (Exception) as e:
                    cls.__error.append(target)
                    cls.show(str(str(target)+" [ "+cls.__danger+str(e)+cls.__reset)+" ]","e")
                except KeyboardInterrupt:
                    sys.exit("\n")
        except KeyboardInterrupt:
            sys.exit("\n")

        print("\n\nScanning success..\nVuln: {}\nNot vuln: {}\nError: {}".format(
            len(set(cls.__vuln)),
            len(set(cls.__nothing)),
            len(set(cls.__error))))

SqlScan().scan()
