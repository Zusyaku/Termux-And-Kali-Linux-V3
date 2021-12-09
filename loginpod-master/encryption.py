#!/usr/bin/python

import sys
crypt = []
special=["35","97","37","74","99","38","37"]
for i in range(len(special)):
 special[i]=int(special[i])
special_index=0
password=list(sys.argv[6])
length=len(password)
key_index=1
for i in range(length):
 password[i] = ord(password[i])
for i in range(length):
 if key_index == 6:
  key_index=1
 if special_index == 7:
  special_index=0
 crypt.append(password[i]+int(sys.argv[key_index]))
 crypt.append(special[special_index])
 key_index += 1
 special_index += 1
print('\n\nCrypt > ',end="")
for j in range(length*2):
 print (chr(crypt[j]),end="")
print('\n')
