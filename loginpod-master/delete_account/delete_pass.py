import sys

passwd = []
with open(".add_account/password") as file:
    for line in file: 
        line = line.strip()
        passwd.append(line)

remove_nmb = int(sys.argv[1])
value = passwd[remove_nmb]
passwd.remove(value)

for i in range(len(passwd)):
 print passwd[i]
