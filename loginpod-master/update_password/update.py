import sys

passwd = []
with open(".add_account/password") as file:
    for line in file: 
        line = line.strip()
        passwd.append(line)
passwd[int(sys.argv[1])] = sys.argv[2]
length = len(passwd)
for i in range(length):
 print passwd[i]
