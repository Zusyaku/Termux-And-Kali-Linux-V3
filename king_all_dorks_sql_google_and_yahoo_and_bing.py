#!/usr/bin/python
# By Skandare & ThE Sa3iD
# skandare@hotmail.it
import urllib2
import re
import time
import sys
import os
if os.name == 'nt':
	os.system('color a')
	os.system('cls')
else:
	os.system('clear')
print '''
       _                        _                    	
      | | Python     _   _     | |           		
  ___ | |  _  _____ | \ | |  __| | _____   ___  ____ 	
 /___)| |_/ )(____ ||  \| | / _  |(____ | / __)/ ___)	
|___ ||  _ ( / ___ || |\  |( (_| |/ ___ || |  |  ___)	
(___/ |_| \_)\_____||_| \_| \____|\_____||_|v2 \____) 	

--------------------------------------------------------------------------------

	[+] KinG All Dorks google and yahoo and bing ^_^
	
'''
dork = raw_input("Dork ? : ")
time.sleep(1)
print '(1)google  , (2)Bing  ,  (3)Yahoo , (4)ASK'
sietsearch = raw_input("srach ? : ")
time.sleep(1)

# def for yahoo.com
def yahoo():
	try:
		for yahoocom in range(1,1000):
			srachyaaho = urllib2.urlopen('http://search.yahoo.com/search;_ylt=A0oG7mY5vS9O9h0A1S1XNyoA?p='+dork+'&ei=UTF-8&vm=r&fr=moz35&xargs=0&pstart=1&b='+str(yahoocom)+'1&xa=e3Awd3h7whaNaN2Z9krI0A--,1311837881')
			data_yaho = srachyaaho.read()
			find_yaho = re.findall('class=url><b>(.+?)</b>',data_yaho)
			file_siet = open('siet.txt', 'a')
			for yaho_top in find_yaho:
				cat_yaho = "http://"+yaho_top+"/\n"
				print cat_yaho
				file_siet.write(cat_yaho)
				time.sleep(1)
				
	except IOError:
		print "Done"

def bing():
	try:
		for bingfor in range(1,2000):
			bingurl = urllib2.urlopen('http://www.bing.com/search?q='+dork+'&go=&filt=all&first='+str(bingfor)+'1&FORM=PERE2')
			bingread = bingurl.read()
			findbing = re.findall('class="sb_tlst"><h3><a href="(.*?)"',bingread)
			
			for bingget in findbing:
				file_siet = open('siet.txt', 'a')
				bing_getmysiet = bingget
				#bing_ok = bing_getmysiet.split('/')
				print bing_getmysiet
				#print "http://"+bing_ok[2]+"/"
				#file_siet.write("http://"+bing_ok[2]+"/\n")
				time.sleep(1)
	except:
		print "done"
def google():
	try:
		for googlefor1 in range(1,2000):
			amazonurl = urllib2.urlopen('http://www.google.com/search?hl=en&q='+dork+'&start='+str(googlefor1)+'0')
			#http://www.google.be/search?hl=en&q='+dork+'&start=20
			get_sorcgoogle = amazonurl.read()
			findgoosorcgo = re.findall('class="r"><a href="(.*?)"',get_sorcgoogle)
			for getmysietfoof in findgoosorcgo:
				google_file = open('google_siet.txt','a')
				getmysietfoof1 = getmysietfoof.split('/')
				print "http://"+getmysietfoof1[2]+"/"
				google_file.write("http://"+getmysietfoof1[2]+"/\n")
				time.sleep(1)
				google_file.close()
	except:
		print "done"
def ask():
		try:
			for ask_for in range(1,1000):
				ask_url = urllib2.urlopen('http://www.ask.com/web?q='+dork+'&qsrc=1&frstpgo=0&o=0&l=dir&qid=F8FB1F2372E93231E0EDD6BEB4A5B24F&page='+str(ask_for)+'&jss=')
				ask_read = ask_url.read()
				ask_find = re.findall('<a id="r0_t" href="(.*?)"',ask_read)
				for ask_for2 in ask_find:
					ask_file = open('ask.txt','a')
					ask_com = ask_for2.split('/')
					print "http://"+ask_com[2]+"/"
					ask_file.write("http://"+ask_com[2]+"/\n")
					time.sleep(1)
					ask_file.close()
		except IOError:
			print "[+] done \n"
if sietsearch == '3':
	yahoo()
elif sietsearch == '2':
	bing()
elif sietsearch == "1":
	google()
elif sietsearch == '4':
	ask()
#file_siet.close()