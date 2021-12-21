#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests, re, sys, threading, threading, time, random, signal, os
from queue import Queue
requests.packages.urllib3.disable_warnings()

try:
        os.mkdir("androxgh0st")
except:
        pass

def handler(signum, frame):
    print("CTRL+Z Force Killed.")
    exit()

signal.signal(signal.SIGTSTP, handler)

def main(url):
        timeout = 5
        header = {"User-agent":"Linux Mozilla 5/0 androxgh0st"}
        try:
                finaly = url
                html = requests.get(finaly, headers=header, timeout=timeout).text
                if "component" in html and "com_" in html:
                        print(("\033[32;1m[+] "+finaly+" -> Joomla"))
                        jm = open("androxgh0st/joomla.txt","a")
                        jmc = open("androxgh0st/joomla.txt").read()
                        if finaly in jmc:
                                print(" \033[31;1m| Already Added In List")
                        else:
                                jm.write(finaly+"\n")
                                jm.close()
                                print(" | Added To List")
                elif "/wp-content/" in html:
                        print(("\033[32;1m[+] "+finaly+" -> Wordpress"))
                        wp = open("androxgh0st/wordpress.txt", "a")
                        wpc = open("androxgh0st/wordpress.txt").read()
                        if finaly in wpc:
                                print(" \033[31;1m| Already Added In List")
                        else:
                                wp.write(finaly+"\n")
                                wp.close()
                                print(" | Added To List")
                elif "/sites/default/" in html:
                        print(("\033[32;1m[+] "+finaly+" -> Drupal"))
                        dr = open("androxgh0st/drupal.txt","a")
                        drc = open("androxgh0st/drupal.txt").read()
                        if finaly in drc:
                                print(" \033[31;1m| Already Added In List")
                        else:
                                dr.write(finaly+"\n")
                                dr.close()
                                print(" | Added To List")
                elif "skin/frontend/" in html:
                        print(("\033[32;1m[+] "+finaly+" -> Magento"))
                        mg = open("androxgh0st/magento.txt","a")
                        mgc = open("androxgh0st/magento.txt").read()
                        if finaly in mgc:
                                print(" \033[31;1m| Already Added In List")
                        else:
                                mg.write(finaly+"\n")
                                mg.close()
                                print(" | Added To List")
                elif "var prestashop = {" in html and "shipping" in html:
                        print(("\033[32;1m[+] "+finaly+" -> PrestaShop"))
                        ps = open("androxgh0st/prestashop.txt","a")
                        psc = open("androxgh0st/prestashop.txt").read()
                        if finaly in psc:
                                print(" \033[31;1m| Already Added In List")
                        else:
                                ps.write(finaly+"\n")
                                ps.close()
                                print(" | Added To List")
                elif "vBulletin" in html or "vbulletin" in html:
                        print(("\033[32;1m[+] "+finaly+" -> vBulletin"))
                        ps = open("androxgh0st/vBulletin.txt","a")
                        psc = open("androxgh0st/vBulletin.txt").read()
                        if finaly in psc:
                                print(" \033[31;1m| Already Added In List")
                        else:
                                ps.write(finaly+"\n")
                                ps.close()
                                print(" | Added To List")
                else:
                        try:
                                html = requests.get(finaly+"/vendor/phpunit/phpunit/phpunit.xml", headers=header, timeout=timeout).text
                                html2 = requests.get(finaly+"/.env", headers=header, timeout=timeout).text
                                if "PHPUNIT_TESTSUITE" in html:
                                        print(("\033[32;1m[+] "+finaly+" -> Laravel"))
                                        ps = open("androxgh0st/laravel.txt","a")
                                        psc = open("androxgh0st/laravel.txt").read()
                                        if finaly in psc:
                                                print(" \033[31;1m| Already Added In List")
                                        else:
                                                ps.write(finaly+"\n")
                                                ps.close()
                                                print(" | Added To List")
                                elif "APP_KEY" in html2 or "APP_ENV" in html2:
                                        print(("\033[32;1m[+] "+finaly+" -> Laravel"))
                                        ps = open("androxgh0st/laravel.txt","a")
                                        psc = open("androxgh0st/laravel.txt").read()
                                        if finaly in psc:
                                                print(" \033[31;1m| Already Added In List")
                                        else:
                                                ps.write(finaly+"\n")
                                                ps.close()
                                                print(" | Added To List")
                                else:
                                        print(("\033[33;1m[+] "+finaly+" -> Other"))
                                        other = open("androxgh0st/other.txt","a")
                                        otherc = open("androxgh0st/other.txt").read()
                                        if finaly in otherc:
                                                print(" \033[31;1m| Already Added In List")
                                        else:
                                                other.write(finaly+"\n")
                                                other.close()
                                                print(" | Added To List")
                        except KeyboardInterrupt:
                                print("CTRL + C Closed")
                                exit()
                        except Exception as err:
                                print("\033[34m[!] Exception Error!\033[0m")
        except KeyboardInterrupt:
                print("CTRL + C Closed")
                exit()
        except Exception as err:
                print("\033[34m[!] Exception Error!\033[0m")

try:
        list = sys.argv[1]
        thre = sys.argv[2]
except:
        print("python3 androxgh0st.py [FILELIST] [THREAD]")
        exit()

try:
        asu = open(list).read().splitlines()
        jobs = Queue()
        def do_stuff(q):
                while not q.empty():
                        value = q.get()
                        if value.startswith("http://") or value.startswith("https://"):
                                main(value)
                        else:
                                value2 = "http://"+value
                                main(value2)
                        q.task_done()

        for trgt in asu:
                jobs.put(trgt)
        for i in range(int(thre)):
                worker = threading.Thread(target=do_stuff, args=(jobs,))
                worker.start()
                jobs.join()
except KeyboardInterrupt:
        print("CTRL + C Closed")
        exit()