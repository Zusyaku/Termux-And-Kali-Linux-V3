# Made by Nanta XE
# Team: Xiuz Code
# OPEN SOURCE

import os
import json
import time
import subprocess
import re
import hashlib
import random

########
for xiuz in ['requests', 'bs4']:
	while 1:
		try:
			exec(f'import {xiuz}')
			break
		except:
			subprocess.check_output(f'python3 -m pip install {xiuz}'.split())
#########
def randomhash():
	h = hashlib.new('sha1')
	h.update(str(random.random()).encode())
	return h.hexdigest()

class Twitter:
	def __init__(self):
		self.url    = 'https://twsaver.com/'
		self.banner = '•——————————————————————————•\n| Twitter Video Downloader |\n•——————————————————————————•\n|     Author: Nanta XE     |\n|      Team: XiuzCode      |\n•——————————————————————————•\n'
		self.s      = requests.Session()
		self.fn     = ''
		self.ext    = ''

	def download(self):
		print (self.banner)
		self.s.headers.update({'User-Agent': 'Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko; googleweblight) Chrome/38.0.1025.166 Mobile Safari/535.19'})
		link = str(input('! Hanya untuk video twitter, bukan foto.\n~> Link video: '))
		if 'twitter.com' not in link: exit('! Bukan link twitter')
		q = self.s.get(self.url)
		q = bs4.BeautifulSoup(q.text, 'html.parser')
		token = q.find('input', {'type': 'hidden', 'name': 'token', 'id': 'token'})['value']
		post_url = self.url + 'system/action.php'
		data = {}
		data.update({'url': link, 'token': token})
		try:
			q = self.s.post(post_url, data = data).json()
		except json.decoder.JSONDecodeError:
			exit('! Error saat mengambil data')
		z = q.get('links')
		if z:
			for x,y in enumerate(z):
				idx = x + 1
				quality = y['quality']
				size = y['size']
				print (f'{idx}. {quality} - {size}')
			c = input('[pilih]> ')
			try: c = int(c) - 1
			except: exit('! Gunakan angka.')
			self.ext = '.' + z[c]['type']
			self.dl_file(z[c]['url'])
		else:
			exit('! Link download tidak ditemukan.')

	def dl_file(self, url):
		file_data = requests.get(url, stream = True)
		cl = file_data.headers.get('content-length')
		self.fn = randomhash() + self.ext
		df = f'download/{self.fn}'
		with open(df, 'wb') as down:
			print (f'+ Mengunduh {self.fn}')
			if cl is None: down.write(file_data.content)
			else:
				ac = 0
				cl = int(cl)
				for xa in file_data.iter_content(chunk_size=4096):
					ac += len(xa)
					down.write(xa)
					bar = 10
					load = int(bar * ac / cl)
					strips = '=' * load + ' ' * (bar - load)
					percent = f'{int(ac / cl * 100)}%'
					print (f'\r[{strips}] {percent}', end = "")
			down.close()
			print ('')

if '__main__' == __name__:
	os.system('clear')
	try: os.mkdir('download')
	except: pass
	app = Twitter()
	try: app.download()
	except KeyboardInterrupt: exit()
