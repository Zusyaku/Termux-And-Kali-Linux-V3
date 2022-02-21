import requests as req, re, os, time
from bs4 import BeautifulSoup as par

data = {}
try:
	lah = open("tumbal/coki.text","r").read()
	login = req.get("https://mbasic.facebook.com",cookies={"cookie":lah}).text
	if "mbasic_logout_button" in login:
		pass
	elif "Akun Anda Dikunci" in login:
		os.system("rm -rf tumbal/coki.text")
		exit(" × Tumbal mokad.")
	else:
		os.system("rm -rf tumbal/coki.text")
		exit(" × Cookies invalid")
except FileNotFoundError:
	os.system("clear")
	print(" ! Anda belum login\n")
	tumbal = input(" > Masukan cookies: ")
	cokii = {"cookie":tumbal}
	login = req.get("https://mbasic.facebook.com",cookies=cokii).text
	if "mbasic_logout_button" in login:
		print(" √ Login berhasil")
		time.sleep(3)
		os.system("mkdir tumbal")
		open("tumbal/coki.text","a").write(tumbal)
	elif "Akun Anda Dikunci" in login:
		exit(" × Tumbal terkunci.")
	else:
		exit(" × Login gagal periksa kembali cookies anda.")

os.system('clear')
print(" * Bot share facebook! Pastikan postingan dipublikan.\n")
komen = input(" > Link postingan: ")
jumlah = int(input(" > Jumlah share: "))
print("")

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
			"https://mbasic.facebook.com"+link,data=data,cookies=coki
			)
			x+=1
			if "Anda Tidak Dapat Berkomentar Saat Ini" in kirim.text:
				os.system("rm -rf tumbal/coki.text")
				exit(" × Akun terkena limit harap ganti tumbal!")
			elif "Akun Anda Dikunci" not in kirim.text:
				if(x==1):
					print(f" \_> Share berhasil {x} ")
				else:
					print(f" |_> Share berhasil {x} ")
			else:
				os.system("rm -rf tumbal/coki.text")
				exit("\n × Share gagal tumbal mokad.\n ! Login dengan tumbal baru\n")
		print("\n √ Program finished")

if __name__=="__main__":
	Main(open("tumbal/coki.text","r").read()).gasken(jumlah,komen)
	