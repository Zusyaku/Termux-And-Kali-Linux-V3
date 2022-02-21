import requests as req
from bs4 import BeautifulSoup as par

headers = {
	"Host":"mbasic.facebook.com",
	"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
	"origin":"https://www.facebook.com",
	"referer":"https://www.facebook.com",
	"sec-ch-ua":'";Not A Brand";v="99", "Chromium";v="94"',
	"upgrade-insecure-requests":"1",
	"user-agent":"Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5"
}
data = {}
class Main:
	
	def __init__(self,coki):
		self.coki = coki
	def gasken(self,jumlah,komen):
		coki = {"cookie":self.coki}
		session = req.Session(
		)
		soup = par(
			req.get(
				"https://mbasic.facebook.com/story.php?story_fbid=121925043701320&id=100076514745258&_rdr",cookies=coki
			).text,"html.parser"
		)
		link = soup.find(
			"form",{
				"method":"post"
			}
		).get(
			"action"
		)
		dstg = [
			"fb_dtsg","jazoest"
		]
		for x in soup.find_all(
			"input"
		):
			if x.get(
				"name"
			) in dstg:
				data.update(
					{
						x.get(
							"name"
						):x.get(
							"value"
						)
					}
				)
		data.update(
			{
				"comment_text":komen,
			}
		)
		for x in range(jumlah):
			kirim = session.post(
			"https://mbasic.facebook.com"+link,data=data,cookies=coki, headers=headers
			)
			x+=1
			if "Anda Tidak Dapat Berkomentar Saat Ini" in kirim.text:
				pass
			elif "Akun Anda Dikunci" not in kirim.text:
				if(x==1):
					print(f" \_> Spam berhasil {x} ")
				else:
					print(f" |_> Spam berhasil {x} ")
			else:
				exit("\n × Spam gagal akun mokad.\n")