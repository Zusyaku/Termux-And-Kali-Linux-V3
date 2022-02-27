import random
import os
print ('''
    ___                __                 ______
   /   |_      _______/ /_____  __  __   / ____/__  ____
  / /| | | /| / / ___/ //_/ _ \/ / / /  / / __/ _ \/ __ \
 / ___ | |/ |/ (__  ) ,< /  __/ /_/ /  / /_/ /  __/ / / /
/_/  |_|__/|__/____/_/|_|\___/\__, /   \____/\___/_/ /_/
                             /____/
                             Author : LoliC0d3 - Tegal1337
''')
x = int(input("Input Count:"))

for i in range(x):
    chars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","/","/","+"]
    region = ["us-east-1",
    "us-east-2",
    "us-west-1",
    "us-west-2",
    "af-south-1",
    "ap-east-1",
    "ap-south-1",
    "ap-northeast-1",
    "ap-northeast-2",
    "ap-northeast-3",
    "ap-southeast-1",
    "ap-southeast-2",
    "ca-central-1",
    "eu-central-1",
    "eu-west-1",
    "eu-west-2",
    "eu-west-3",
    "eu-south-1",
    "eu-north-1",
    "me-south-1",
    "sa-east-1"]

    def aws_id():
        output = ''
        for i in range(16):
            output += random.choice(chars[0:36]).upper()
        return output

    def aws_key():
        output = ''
        for i in range(40):
            if i == 0 or i == 39:
                ranUpper = random.choice(chars[0:26]).upper()
                output += random.choice([ranUpper, random.choice(chars[0:36])])
            else:
                ranUpper = random.choice(chars[0:26]).upper()
                output += random.choice([ranUpper, random.choice(chars)])
        return output

    def aws_region():
        output = ''
        for i in region:
            output = random.choice(region)
        return output

    def print_key():
        # print("aws_access_key_id=" + aws_id())
        # print("aws_secret_access_key=" + aws_key())
        # print("region=" + str(shuffle(region[0:-20])))
        print ('AKIA'+aws_id()+ '|' + aws_key() + '|' + aws_region() )

    print_key()
    # print (*region, sep=",")
# print(len(region))
