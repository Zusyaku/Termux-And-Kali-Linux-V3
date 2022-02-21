import requests as req, re, os

class Main:
	
	def __init__(
		self,username
	):
		self.username = username
	def getProfile(
		self
	):
		r = req.get(
			f"https://instagram.com/{self.username}/?__a=1"
		).text
		try:
			_link = re.findall(
				'\"profile_pic_url_hd\"\:\"(.*?)\"',str(
					r
				)
			)[0]
		except:
			exit(
				"[!] Username tidak ditemukan."
			)
		with open(
			f"/sdcard/download/profile_{self.username}.jpg", "wb"
		) as f:
			__get_picture_hd = req.get(
				_link
			).content
			f.write(
				__get_picture_hd
			)
		return f"[✓] Foto disimpan di folder download\n * Nama file: profile_{self.username}.jpg "

os.system('clear')
if __name__=="__main__":
	print(
		" * Download profile picture Instagram HD\n"
	)
	_username = input(
		"[+] Username Instagram target: "
	)
	print(
		Main(
			_username
		).getProfile()
	)
