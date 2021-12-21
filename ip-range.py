#!/usr/bin/python3

from netaddr import IPAddress

netmasks = []

def save(file, content):
	temp = open(file, 'a+')
	temp.write(content)
	temp.close()


x = input('\033[34m[ENTER YOUR IPS]:\033[31m ')
ips_ = open(x, 'r')
ips = ips_.readlines()
k = "=" * 20
print("\033[33m"+k+"\033[0m")
ips = list(dict.fromkeys(ips))
for ip in ips:
	first = '.'.join(ip.split(".")[:3])+".0-"
	second = '.'.join(ip.split(".")[:3])+".255"
	first_temp = first.split("-")[0]
	netmasks.append(first_temp)
	print("\033[32m" + first + second + "\033[0m")
	save("IPv4-Range.txt", f"{first}{second}\n")

print("\033[33m"+k+"\033[0m")


for ip in netmasks:
	temp = str(ip)+"/24"
	print("\033[32m"+str(temp)+"\033[0m")
	save("Netmask.txt",f"{temp}\n")