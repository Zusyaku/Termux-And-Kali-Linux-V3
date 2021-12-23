#Youtube : Py
#Coded By Shin Code
#My Friend : Jenderal92 - h0d3_g4n - Moslem - Kiddenta - Naskleng45

import requests,re,random,sys,time

def Banner():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """
                Video Facebook Downloader | Python Code
"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)
Banner()


urlfb = raw_input('\033[36m'"URL VIDEO FB : ")

UA = {'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Referer': 'https://fdown.net/',
'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
'Cookie': '_ga=GA1.2.2094519438.1640138973; _gid=GA1.2.1078295655.1640138975; _gat_gtag_UA_44090370_1=1'}

fbdown = requests.post("https://fdown.net/download.php",data={"URLz": urlfb}, headers=UA).content
if 'Download Video in Normal Quality' in fbdown:
	RF = re.findall('id="sdlink" href="(.*?)" download="',fbdown)
	for DOWN in RF:
		CEK = DOWN.replace('amp;','')
		print("'\033[0m' Copy this link and put it in your browser :"'\033[32m' + CEK)
