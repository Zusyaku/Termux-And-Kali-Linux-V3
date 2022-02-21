import re, requests as req
from bs4 import BeautifulSoup as par

ip,on,jir,c=[],[],"",0
data={}

banner = """
 __________  ___             
/_  __/ __ \/ _ \            
 / / / /_/ / ___/ Coded By: Latip176          
/_/__\____/_/                   

[ Top 25 Server Mcpe Populer Indonesia! ]
"""
class Main:
	
	def get(self):
		global jir,c
		soup = par(req.get("https://minecraftpocket-servers.com/country/indonesia/").text,"html.parser")
		for button in soup.find_all({"div":"d-inline-block d-md-none mt-2"}):
			get=button.find({"button":"btn btn-secondary btn-sm"})
			dataOn=re.findall('\<i aria-hidden=\"true\" class=\".+\"><\/i>\s+(.+)<\/button>',str(get))
			dataIp=re.findall('<\/span><\/a>\s+(.*)<\/button>', str(get))
			for _ip in dataIp:
				if _ip!=jir:
					jir=_ip
					break
				ip.append(_ip)
			for _on in dataOn:
				on.append(_on)
		data.update({"ip":ip,"on":on})
		for x in data["ip"]:
			print(f"[{str(c)}] SERVER:",data["ip"][c],"| PLAYER_ONLINE:",data["on"][c])
			c+=1

if __name__=="__main__":
	print(banner)
	Main().get()
