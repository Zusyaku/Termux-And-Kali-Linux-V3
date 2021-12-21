import urllib2
import re
import random


#Decoded by DayWalker
#Repaired by MrBlackX
#Contat : rafsanzani.suhada99@gmail.com



class reverse(object):
	def run(self, target):
	print ""
	if target.startswith("http://"):
		target = target.replace("http://", "")
	elif target.startswith("https://"): 
		target = target.replace("https://", "")
	else:
		pass

	url = "http://viewdns.info/reverseip/?host={}&t=1".format(target)

	try:
		opener = urllib2.build_opener()
		opener.addheaders = [('User-agent','Mozilla/5.0 (Mobile; rv:14.0) Gecko/14.0 Firefox/14.0')]
		response = opener.open(url)
		data = response.read()
		comp = re.compile("<td")
		baglantilar = comp.findall(data)
		for i in baglantilar:
			i = i.replace("", "").replace("<td", "")
			if i.startswith("http://"):
				pass
			else:
				i = "http://"+i 
			
			if "Domain" not in i:
				print(i)     
	except:
		print("Something’s went wrong ..")
		pass


if __name__ == ‘__main__’:
	a = input("\n\t Target : ")
 	reverse().run(a)