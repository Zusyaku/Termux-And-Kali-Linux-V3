import requests as req, re, os

os.system("clear")

print("""
 _______ __ __     __          __    
|_     _|__|  |--.|  |_.-----.|  |--.
  |   | |  |    < |   _|  _  ||    < 
  |___| |__|__|__||____|_____||__|__|
                                     
 * Download foto profile target, Tiktok. *
	Dev: github.com/Latip176
""")

user = input('[+] Masukan username tiktok: ').replace('@','')
r = req.get(f"https://www.tiktok.com/@{user}",headers={"user-agent":"chrome"}).text
try:
	link = re.findall('\<img\ loading\=\"lazy\" src\=\"(.*?)\" class\=\"tiktok.*?\"\/\>',str(r))[0]
	with open(f"/sdcard/download/{user}.jpeg","wb") as f:
		f.write(req.get(link).content)
except:
	exit('[!] Username tidak ditemukan')
inf = re.findall('\<meta\ data\-rh\=\"true\" name\=\"description" content\=\"(.*?)\"\/\>',str(r))[0].split(' | ')
nama = inf[0].replace('di TikTok','').replace('on TikTok','')
inf2 = inf[1].replace('Suka','Likes').replace('Penggemar','Followers').replace('Fans','Followers')
print(f'[✓] Nama: {nama}\n[=] Info: {inf2}\n * Success download. Foto di simpan di folder download!\n * Nama file Foto {user}.jpeg\n')
