#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests, os, argparse, hashlib, time

parse = argparse.ArgumentParser()
parse.add_argument('-m', help='crack method', dest='mode')
parse.add_argument('-s', help='hash to crack', dest='hash')
args = parse.parse_args()

mode = args.mode
hashtext = args.hash

B  = '\033[1;34'
C  = '\033[1;36m'
G  = '\033[1;34m'
OG = '\033[92m'
LG = '\033[1;32m'
W  = '\033[1;37m'
R  = '\033[1;31m'
Y  = '\033[1;33m'

def banner():
    os.system('clear')
    print("")
    print(R+"    ハ"+Y+"ッ"+G+"シ"+C+"ュ"+OG+"キ"+LG+"ラー"+W)
    print("")

def hashbrute():
    ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    string_list = ascii_letters
    
    def generateHashFromString(hashtype, cleartextString):
        if hashtype == "md5":
            return hashlib.md5(cleartextString.encode()).hexdigest()
        elif hashtype == "sha1":
            return hashlib.sha1(cleartextString.encode()).hexdigest()
        elif hashtype == "sha224":
            return hashlib.sha224(cleartextString.encode()).hexdigest()
        elif hashtype == "sha256":
            return hashlib.sha256(cleartextString.encode()).hexdigest()
        elif hashtype == "sha384":
            return hashlib.sha384(cleartextString.encode()).hexdigest()
        elif hashtype == "sha512":
            return hashlib.sha512(cleartextString.encode()).hexdigest()
        else:
            pass
    def reverseString(string):
        return string[::-1]
    def IndexErrorCheck(index_input):
        if len(string_list) <= index_input:
            pass
        else:
            return string_list[index_input]
    def StringGenerator(string):
        if len(string) <= 0:
            string.append(string_list[0])
        else:
            # error checking needs to be done, otherwise a ValueError will raise
            string[0] = IndexErrorCheck((string_list.index(string[0]) + 1) % len(string_list))
            if string_list.index(string[0]) == 0:
                return [string[0]] + StringGenerator(string[1:])
        return string
    def decrypt():
        generated_string = []
        while True:
            generated_string = StringGenerator(generated_string)
            formatted_string = reverseString("".join(generated_string))
            hashes = generateHashFromString(hashtype, formatted_string)
            print(C+" "+hashes+W+" [ "+R+formatted_string+W+" ]")
            if hashes == hashtext:
                print("")
                print(C+" [+]"+W+" String"+R+" : "+W+formatted_string)
                break
    decrypt()

def md5decrypt():
    email = "bransen.vikranth@logdots.com"
    code = "49898fab6e014903"
    result = requests.get('https://md5decrypt.net/en/Api/api.php?hash=%s&hash_type=%s&email=%s&code=%s' % (hashtext, hashtype, email, code)).text
    if len(result) != 0:
        print("")
        print(C+" [+]"+W+" Result"+R+" : "+W+result)
    else:
        if mode == 'default':
            print(Y+' //'+W+' I can\'t do it, trying bruteforce')
            time.sleep(1)
            print("")
            hashbrute()

banner()

if len(hashtext) == 32:
    hashtype = 'md5'
elif len(hashtext) == 40:
    hashtype = 'sha1'
elif len(hashtext) == 64:
    hashtype = 'sha256'
elif len(hashtext) == 96:
    hashtype = 'sha384'
elif len(hashtext) == 128:
    hashtype = 'sha512'
else:
    print(hashtext+" Not a valid Hash")

print(Y+' //'+W+' Hash : '+hashtext)
print(Y+' //'+W+' Type : '+hashtype)
print("")
print(Y+' //'+W+' Trying to get a shot')

if not mode:
    mode = "default"
    md5decrypt()
elif mode == 'brute':
    hashbrute()
elif mode == 'shot':
    md5decrypt()
