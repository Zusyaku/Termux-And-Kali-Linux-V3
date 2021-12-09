import sys

passwd = []
with open(".add_account/password") as file:
    for line in file: 
        line = line.strip()
        passwd.append(line)
print passwd[int(sys.argv[1])]
