# Created at: 2018-02-25 14:25:47
# Author : Pirmansx
import marshal, platform
from py_compile import compile as com
from sys import argv as D
from sys import exit
from random import randint as R
from os import remove
from os import rename

def tampil(x):
    w = 'amhkbpc'
    for i in w:
        x = x.replace('?%s' % i, '\x1b[%d;1m' % (90 + w.index(i)))

    x += '\x1b[0m'
    x = x.replace('?0', '\x1b[0m')
    print x


if platform.python_version().split('.')[0] != '2':
    tampil('?m[!] kamu menggunakan python versi 3 silahkan menggunakan versi 2')
    exit()

def baliho():
    tampil('?k+--------------------------------+\n|           ?p-?mPIRMANSX?p-           ?k|\n|   ?hhttps://github.com/pirmansx  ?k|\n+--------------------------------+')


if len(D) < 3:
    baliho()
    tampil('?hCara menggunakan:\n\t?bpython2 ME.py [file] [mode]\n?m*?cMode:  ?h1 ?c-> ?hCepat\n\t?k2 ?c-> ?kSedang\n\t?m3 ?c-> ?mLambat\n?hContoh: ?apython2 ME.py /sdcard/file.py 2')
    exit()
try:
    s = open(D[1], 'r').read()
except:
    baliho()
    tampil('?m[!] Gagal membuka ?c' + D[1])
    exit()

if D[2] not in ('1', '2', '3'):
    baliho()
    tampil('?m[!] Mode ?c%s?m tidak ada' % D[2])
    exit()
try:
    c = compile(s, '<script>', 'exec')
except:
    baliho()
    tampil('?mFile tidak support')
    exit()

d = marshal.dumps(c)
r = lambda : R(0, 255)
k = []
for i in range(255):
    k.append(r())

def enc(d, k):
    e = ''
    i, j = (0, 0)
    while 1:
        if i >= len(d):
            break
        if j >= len(k):
            j = 0
        e += chr(ord(d[i]) ^ k[j])
        i += 1
        j += 1

    return e


def enc0(d, k):
    x = []
    K = []
    for i in d:
        x.append(str(ord(i)))

    x = '[' + (',').join(x) + ']'
    for i in k:
        K.append(str(i))

    s = 'import marshal\nd = ' + x + "\ne = ''\ni,j = 0,0\nk = [" + (',').join(K) + ']\nwhile 1:\n\tif i >= len(d):break\n\tif j >= len(k):j = 0\n\te += chr(d[i]^k[j])\n\ti += 1\n\tj += 1\nexec(marshal.loads(e))'
    c = compile(s, '<script>', 'exec')
    d = marshal.dumps(c)
    return d


for i in range(int(D[2]) + 1):
    d = enc0(enc(d, k), k)

D = D[1] + 'e'
open(D, 'w').write('import marshal;exec(marshal.loads(' + repr(d) + '))')
baliho()
try:
    com(D)
    rename(D + 'c', ('').join(D.split('.')[:1]) + '_enc.pyc')
    remove(D)
    tampil('?h[v] Berhasil membuat file ?c' + ('').join(D.split('.')[:1]) + '_enc.pyc')
except:
    tampil('?mGAGAL meyimpan ?c' + D[:-1])
