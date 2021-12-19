import requests
import time
import os

def banner():
  os.system("clear")
  os.system("cat banner.txt")
  print("coded by youhacker55")

Red ="\u001b[31m"
Green ="\u001b[32m"
banner()
site = input("entre target website(example:http://127.0.0.1/):")

with open('admin.txt','r') as list:
  for i in list:
    time.sleep(1)
    x = i.rstrip('\n')
    check = requests.get(site+x)
    try:
      if check.status_code == 200:
        with open("live.txt",'a') as live:
          live.write(site+x+"\n")
        print(Green+site+x+ " 200 " + "saved to live.txt")
        live.close()
      else:
        print(Red+site+x + " 404")
    except ValueError:
      print(Red,"something wrong")
