from core import *
from core.get_themes import *
from core.get_plugins import *


def main():
    try:
        print('''

        welcome to priv8 website grabber
        what you need bos?

        1. Grab from themes
        2. Grab from plugins 
        3, remove duplicate 
        4. host to ip ( mass )

        ''')
        pilihan = int(input('nomor : '))
        if pilihan == 1:
            ch = str(input('link or page (l/p) : ')).lower()
            if ch == 'l':
                link = input('enter your link : ')
                
                with ThreadPoolExecutor(max_workers=20) as anjg:
                    kam = kambing(1)
                    for x in link:
                      anjg.submit(kam.grab_themes(link))

            elif ch.startswith('p'):
                jumlah = int(input('page : '))
                kambing(jumlah).mulai_cari(jumlah)
            else:
                print('salah ')
        elif pilihan == 2:
            ch = str(input('link or page (l/p) : ')).lower()
            if ch == 'l':
                link = input('link : ')
                with ThreadPoolExecutor(max_workers=12) as anjg:
                    gib = gibhan(1)
                anjg.submit(gib.grab_plugins(link))
            elif ch.startswith('p'):
                p = int(input('Page : '))
                gibhan(p).gas_keun(p)
            else:
                print('salah ')
        elif pilihan == 3:
            f = input('file (.txt) : ')
            hasil = set(open(f,'r').readlines())
            for zz in hasil:
                open('hasil_dup.txt','a').write(zz+'\n')
        elif pilihan == 4:
            your_file = input('file (.txt) ')
            if os.path.exists(your_file):
                for l in open(your_file,'r').readlines():
                    anjg = l.rstrip().replace('http://','').replace('https://','')
                    hasil = socket.gethostbyname(anjg)
                    print(anjg,' ',hasil)
    
    except Exception as e:
        print(e)
    main()

    
  
main()