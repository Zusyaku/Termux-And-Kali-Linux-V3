# PyCrack MD5 Hash Cracker
# Version 1.0.0
# Coded by BlackMan in Python 2.7.5
# Download : http://sourceforge.net/projects/md5crack/
# File     : pycrack.py

#IMPORTS
import hashlib
import os
import sys
import datetime

#GLOBAL
startTime = datetime.datetime.now()

#DEBUG MESSAGES
def action(msg)    : print '[#] - ' + msg
def alert(msg)     : print '[+] - ' + msg
def error(msg)     : print '[!] - ' + msg
def errorExit(msg) : raise SystemExit('[!] - ' + msg)

#MD5 STRING
def md5(string): return hashlib.md5(string).hexdigest()

#PERMUTATION BUILDER
def xpermutation(characters, size):
    if size == 0:
        yield []
    else:
        for x in xrange(len(characters)):
            for y in xpermutation(characters[:x] + characters[x:], size - 1):
                yield [characters[x]] + y

#BRUTE FORCE
def bruteForce(hash):
    attempt = 0
    characters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    maxLength = xrange(0,25)
    stringBuilder = ''
    for length in maxLength:
        for x in xpermutation(characters, length):
            permutation = stringBuilder + ''.join(x)
            attempt = attempt + 1
            if md5(permutation) == hash:
                end_time = str(datetime.datetime.now() - startTime).split('.')[0]
                print '[' + str(attempt) + '] - ' + permutation + ' - CRACKED! Took ' + end_time
                raw_input('\nPress the <ENTER> key to EXIT...')
                sys.exit()
            else:
                print '[' + str(attempt) + '] - ' + permutation
    errorExit('Failed to brute force hash.')

#START
if os.name == 'nt' : os.system('cls')
else : os.system('clear')
print ''.rjust(56, '#')
print '#' + ''.center(54) + '#'
print '# PyCrack MD5 Hash Cracker'.ljust(55) + '#'
print '# Version 1.0.0'.ljust(55) + '#'
print '# Coded by InvisibleMan in Python 2.7.5'.ljust(55) + '#'
print '# Download : http://sourceforge.net/projects/md5crack/'.ljust(55) + '#'
print '#' + ''.center(54) + '#'
print ''.rjust(56, '#')
if sys.version_info.major != 2 or sys.version_info.minor != 7:
    errorExit('Requires Python version 2.7')
if len(sys.argv) == 2:
    if len(sys.argv[1]) == 32 and sys.argv[1].isalnum():
        bruteForce(sys.argv[1])
    else:
        error('Invalid MD5 hash!')
        errorExit('Usage : crack.py [HASH]')
else:
    error('Missing command line arguments.')
    errorExit('Usage : pycrack.py [HASH]')