import requests
import ast
import faker
from re import findall as grep

ip = ""

def firstip():
	global ip
	ip = requests.get("https://ifconfig.me")
	return ip



def get_tor():
	session = requests.session()
	session.proxies = {'http':  'socks5://127.0.0.1:9050','https': 'socks5://127.0.0.1:9050'}
	return session



def check_ip():
	ip = firstip()
	torip = requests.get('https://ifconfig.me')
	if torip != ip:
		return "changed"
	elif torip == ip:
		return "not_changed"

def useragent_():
	obj = faker.Factory().create()
	useragent = obj.user_agent()
	return useragent

def print_status(status, iprange, ip):
	if status == "Bad":
		print(f"\033[34m[\033[31m!\033[34m]\033[37m {status} \033[34m| {ip} \033[34m| \033[31m{iprange}")
	elif status == "Good":
		print(f"\033[34m[\033[32m*\033[34m]\033[37m {status} \033[34m| {ip} \033[34m| \033[32m{iprange}")
	else:
		print(f"\033[34m[\033[33m-\033[34m]\033[37m {status} \033[34m| {ip} \033[34m| \033[33mError")

def write_text(filename,content):
	temp = open(filename,"a+")
	temp.write(content)
	temp.close()

def requester(ip):
	ip = ip.replace("\n","")
	begin, end = ip.split("-")
	session = get_tor()
	torip = session.get('https://ifconfig.me')
	check = check_ip()
	if check == "changed":
		useragent = useragent_()
		headers = f"""
	    'User-Agent': '{useragent}',
	    'Accept': '*/*',
	    'Accept-Language': 'en-US,en;q=0.5',
	    'Content-Type': 'application/x-www-form-urlencoded',
	    'X-Requested-With': 'XMLHttpRequest',
	    'Origin': 'https://tools.tracemyip.org',
	    'DNT': '1',
	    'Connection': 'keep-alive',
	    'Referer': 'https://tools.tracemyip.org/IPv4-range-to-CIDR-list/',
	    'Pragma': 'no-cache',
	    'Cache-Control': 'no-cache',
		"""
		data = f"""
		  'tlIPv4rCDRINP_1': '{begin}',
		  'tlIPv4rCDRINP_2': '{end}',
		  'tlIPv4rCDR_FID': '1',
		  'tlsFormTrg': '2'
		"""
		headers = ast.literal_eval("{"+headers+"}")
		data = ast.literal_eval("{"+data+"}")
		response = session.post('https://tools.tracemyip.org/IPv4-range-to-CIDR-list/', headers=headers, data=data)
		try:
			iprange = grep('class="tbsClass1tdO">(.*?)</td>',response.text)[0]
			print_status("Good",iprange,torip.text)
			write_text("ranges.txt",f"{iprange}| @f4c3r100\n")
		except:
			print_status("Bad",response.status_code,torip.text)
	elif check == "not_changed":
		#session = get_tor()
		pass
def main():
	obj = faker.Factory().create()
	x = open('list.txt','r').readlines()
	for _ in x:
		requester(_)


if __name__ == '__main__':
	main()