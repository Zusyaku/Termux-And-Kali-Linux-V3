import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import sys , random


grabbed_site = []
my_session = requests.Session()
my_session.headers.update({'User-Agent':'Mozilla/5.0 (Windows NT 5.1; U; pl) Opera 8.54'})
user_agents = [kontol.rstrip() for kontol in open('user-agents.txt','r').readlines()]
#print(user_agents)

class gibhan:
    def __init__(self,page):
        self.page = page 
    

    def gas_keun(self,page):
        try:
            for pg in range(1,page+1):
                cek_page = my_session.get('https://themesinfo.com/wordpress-plugins/{}'.format(str(pg)),headers={'User-Agent':random.choice(user_agents)})
                if cek_page.status_code == 200:
                    sabun_lama = BeautifulSoup(cek_page.text,'html.parser')
                    h3_tag = sabun_lama.find_all('h3',{'class':'plugin_h3'})
                    with ThreadPoolExecutor(max_workers=40) as babi:
                        for jumlah_page in range(len(h3_tag)):
                            next_link = h3_tag[jumlah_page].find('a')['href']
                            babi.submit(self.grab_plugins,next_link)
                else:print('[E] Error Code {}'.format(cek_page.status_code))
        except Exception as identifier:
            print(identifier)
        
    
    def grab_plugins(self,linknya):
        ke_page = 0
        while True:
            try:
                ke_page += 1 
                sys.stdout.write('\r[+] Sites Grabbed {}'.format(len(grabbed_site)))
                cek_link = my_session.get(linknya+'/{}'.format(str(ke_page)),headers={'User-Agent':random.choice(user_agents)})
                if cek_link.status_code == 200:
                    sabun_baru = BeautifulSoup(cek_link.text,'html.parser')
                    h2_tag = sabun_baru.find_all('h2',{'class':'theme_web_h2'})
                    for jumlah_web in range(len(h2_tag)):
                        raw_link = h2_tag[jumlah_web].text
                        grabbed_site.append(raw_link)
                        open('result/plugins.txt','a').write(raw_link+'\n')
                else:break
                sys.stdout.flush()
            except Exception as identifier:
                print(identifier)

