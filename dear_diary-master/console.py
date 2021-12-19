#!/usr/bin/python
import os, sys, getpass, time, hashlib, webbrowser
from Crypto import Random
from Crypto.Cipher import AES

def pad(s):
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

def encrypt(message, key, key_size=256):
    message = pad(message)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(message)

def decrypt(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return plaintext.rstrip(b"\0")

def encrypt_file(file_name, key):
    with open(file_name, 'rb') as fo:
        plaintext = fo.read()
    enc = encrypt(plaintext, key)
    with open(file_name + ".zez", 'wb') as fo:
        fo.write(enc)

def decrypt_file(file_name, key):
    with open(file_name, 'rb') as fo:
        ciphertext = fo.read()
    dec = decrypt(ciphertext, key)
    with open(file_name[:-4], 'wb') as fo:
        fo.write(dec)

def schrijven():
    regels = []
    titel = raw_input('Titel: ')

    # Bestand informatie
    regels.append('Auteur: ' + getpass.getuser())
    regels.append('Titel: ' + titel)
    regels.append('Datum: ' + time.strftime('%d-%m-%Y') + ' ' + time.strftime('%X'))
    regels.append(' ') # Blank

    try:
        while True:
            plaintxt = raw_input('>> ')
            regels.append(plaintxt)

    except KeyboardInterrupt:
        # Write and Quit
        print('\n')
        passwd = getpass.getpass("Password: ")
        key = hashlib.sha256(passwd).digest()

        # Debug
        #print("Wachtwoord: ", key)

        # Tel het aantal regels
        print('\nRegels: %i' % len(regels))

        # Schrijf de Regels
        with open('./%s_%s.diary' % (time.strftime('%d-%m-%Y'), titel), 'w+') as f:
            for l in regels:
                f.write(l + '\n')
            f.close()

        # Encrypt the file
        enc = './%s_%s.diary' % (time.strftime('%d-%m-%Y'), titel)
        print('Saved: ' + enc)
        encrypt_file(enc, key)
        os.remove(enc) # Verwijder plain bestand

def dagboek_lezen():
    tel_boeken = -1
    dagboeken = []

    for path, subdirs, files in os.walk('.'):
        for name in files:
            if name.endswith('.diary.zez'):
                tel_boeken += 1
                dagboeken.append(path + '/' + name)

    c = -1
    for items in dagboeken:
        c +=1
        print('\t\033[1;96m%i)\033[0m ' % int(c) + items)

    try:
        num = input('[#?] ')

        # Opgeven wachtwoord
        passwd = getpass.getpass("Password: ")
        key = hashlib.sha256(passwd).digest()

        # Debug
        #print("Wachtwoord: ", key)

        # Ontsleutelen
        de_enc = dagboeken[int(num)]
        decrypt_file(de_enc, key)

        # Lezen
        dagboek = open(dagboeken[int(num)].split('.zez')[0]).read()

        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('\n')
        print(dagboek)
        print('\n')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

        # Verwijder het ontsleutelde dagboek
        os.remove(dagboeken[int(num)].split('.zez')[0])

    except KeyboardInterrupt:
        return
    except Exception as e:
        print('[Error] %s\n' % e)
        num = input('#?: ')

# Standaard sleutel om bestanden te versleutelen.
key = b'\x01\xeb\xff\xe2\xca#\xacT\xf3\xfeKh\xc1{\x8b\x86\xa5\x96\\0\xbf\x93E\xa1\xce\xc9\x9e\xb8e\x11\xa1\x8a'

opt = True

# Banner
print('''
\033[1;31m
 ad8888888888ba
dP'         `"8b,
8  ,aaa,       "Y888a     ,aaaa,     ,aaa,  ,aa,
8  8' `8           "8baaaad""""baaaad""""baad""8b
8  8   8              """"      """"      ""    8b
8  8, ,8         ,aaaaaaaaaaaaaaaaaaaaaaaaddddd88P
8  `"""'       ,d8""
Yb,         ,ad8"
 "Y8888888888P"
\033[0m
''')

try:
    # Menu
    while opt:
        print("""

    \033[1;42mOpties:\033[0m
        \033[1;34m1)\033[0m Versleutel een bestand
        \033[1;34m2)\033[0m Ontsleutel een bestand
        \033[1;34m3)\033[0m Versleutel alle bestanden in een map
        \033[1;34m4)\033[0m Ontsleutel alle bestanden in een map
        \033[1;34m5)\033[0m Schrijven en versleutelen
        \033[1;34m6)\033[0m Dagboek lezen

        \033[1;34m99)\033[0m Afsluiten
        """)
        opt = raw_input("[#?] ")
        if opt == "1":
            enc = raw_input("Path to file (encrypt): ")

            # Set key
            passwd = getpass.getpass("Password: ")
            key = hashlib.sha256(passwd).digest()

            encrypt_file(enc, key)
            os.remove(enc)
        elif opt == "2":
            de_enc = raw_input("Path to file (decrypt): ")

            # Set key
            passwd = getpass.getpass("Password: ")
            key = hashlib.sha256(passwd).digest()

            decrypt_file(de_enc + ".zez", key)
            os.remove(de_enc + ".zez")
        elif opt == "3":
            counter = 0
            enc = raw_input("Path to directory (encrypt): ")

            passwd = getpass.getpass("Password: ")
            key = hashlib.sha256(passwd).digest()

            for path, subdirs, files in os.walk(enc):
                for name in files:
                    if name.endswith(".zez"):
                        print("[ Skipped ] %s" % name)
                    elif "." in name:
                        encrypt_file(os.path.join(path, name), key)
                        print("[ Encrypting ] %s" % name)
                        counter = counter+1
                        os.remove(os.path.join(path, name))

            print("\n[ Done ] Encrypted %i files" % counter)
        elif opt == "4":
            counter = 0
            de_enc = raw_input("Path to directory (decrypt): ")

            # Set key
            passwd = getpass.getpass("Password: ")
            key = hashlib.sha256(passwd).digest()

            for path, subdirs, files in os.walk(de_enc):
                for name in files:
                    # If it has an extention, it must be a file
                    if name.endswith(".zez"):
                        decrypt_file(os.path.join(path, name), key)
                        print("[ Decrypting ] %s" % name)
                        counter = counter+1
                        os.remove(os.path.join(path, name))
                    else:
                        print("[ Skipped ] %s" % name)
            print("\n[ Done ] Decrypted %i files" % counter)
        elif opt == "5":
            schrijven()
        elif opt == "6":
            dagboek_lezen()
        else:
            print("[!] Invalid selection!")

except KeyboardInterrupt:
    print("\n")
    sys.exit(0)
