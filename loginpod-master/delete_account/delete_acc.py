import sys

accounts = []
with open(".add_account/account") as file:
    for line in file: 
        line = line.strip()
        accounts.append(line)

remove_nmb = int(sys.argv[1])
remove_nmb -= 1
value = accounts[remove_nmb]
accounts.remove(value)

for i in range(len(accounts)):
 print accounts[i]
