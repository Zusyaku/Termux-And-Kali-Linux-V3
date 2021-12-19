import os, sys, shutil, sqlite3, win32crypt, json, base64, ctypes
import ctypes.wintypes
from prettytable import PrettyTable
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import (Cipher, algorithms, modes)

APP_DATA_PATH= os.environ['LOCALAPPDATA']
DB_PATH = r'Microsoft\Edge\User Data\Default\Login Data'

NONCE_BYTE_SIZE = 12

def encrypt(cipher, plaintext, nonce):
    cipher.mode = modes.GCM(nonce)
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext)
    return (cipher, ciphertext, nonce)

def decrypt(cipher, ciphertext, nonce):
    cipher.mode = modes.GCM(nonce)
    decryptor = cipher.decryptor()
    return decryptor.update(ciphertext)

def get_cipher(key):
    cipher = Cipher(algorithms.AES(key), None, backend=default_backend())
    return cipher

def dpapi_decrypt(encrypted):
    class DATA_BLOB(ctypes.Structure):
        _fields_ = [('cbData', ctypes.wintypes.DWORD), ('pbData', ctypes.POINTER(ctypes.c_char))]

    p = ctypes.create_string_buffer(encrypted, len(encrypted))
    blobin = DATA_BLOB(ctypes.sizeof(p), p)
    blobout = DATA_BLOB()
    retval = ctypes.windll.crypt32.CryptUnprotectData(
        ctypes.byref(blobin), None, None, None, None, 0, ctypes.byref(blobout))
    if not retval:
        raise ctypes.WinError()
    result = ctypes.string_at(blobout.pbData, blobout.cbData)
    ctypes.windll.kernel32.LocalFree(blobout.pbData)
    return result

def get_key():
    jsn = None
    with open(os.path.join(os.environ['LOCALAPPDATA'],
        r"Microsoft\Edge\User Data\Local State"),encoding='utf-8',mode ="r") as f:
        jsn = json.loads(str(f.readline()))
    return jsn["os_crypt"]["encrypted_key"]

def aes_decrypt(encrypted_txt):
    encoded_key = get_key()
    encrypted_key = base64.b64decode(encoded_key.encode())
    encrypted_key = encrypted_key[5:]
    key = dpapi_decrypt(encrypted_key)
    nonce = encrypted_txt[3:15]
    cipher = get_cipher(key)
    return decrypt(cipher,encrypted_txt[15:],nonce)

def get_edge_db():
    _full_path = os.path.join(APP_DATA_PATH,DB_PATH)
    _temp_path = os.path.join(APP_DATA_PATH,'sqlite_file')
    if os.path.exists(_temp_path):
        os.remove(_temp_path)
    shutil.copyfile(_full_path,_temp_path)
    show_password(_temp_path)

def show_password(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute('select signon_realm,username_value,password_value from logins')
    data = cursor.fetchall()

    c = 0
    table = PrettyTable(['id', 'Link', 'Username', 'Password'])
    table.title = 'Edge Passwords'
    table.align = "l"

    for row in data:
        site = row[0]
        name = row[1]
        value = edge_decrypt(row[2])
        table.add_row([int(c), site, name, value])
        c+=1

    print(table)
    print('Found %i saved password(s) in Edge db' % int(c))

    conn.close()
    os.remove(db_file)

def edge_decrypt(encrypted_txt):
    try:
        if encrypted_txt[:4] == b'\x01\x00\x00\x00':
            decrypted_txt = dpapi_decrypt(encrypted_txt)
            return decrypted_txt.decode()
        elif encrypted_txt[:3] == b'v10':
            decrypted_txt = aes_decrypt(encrypted_txt)
            return decrypted_txt[:-16].decode()
    except WindowsError:
        return None

if __name__=="__main__":
    get_edge_db()
