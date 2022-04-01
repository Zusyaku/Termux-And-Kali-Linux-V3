from core import *

import random 

if os.path.exists('result') == False:
    os.system('mkdir result')

my_session = requests.Session()
user_agents = [kontol.rstrip() for kontol in open('user-agents.txt','r').readlines()]

jumlah_grabbed = []
class kambing:
    def __init__(self,page):
        self.page = page 
    
    def mulai_cari(self,page):
        for i in range(1,page+1):
            try:
                print('Sedang berjalan ...')
                cek_url = my_session.get('https://themesinfo.com/{}'.format(str(page)),headers={'User-Agent':random.choice(user_agents)})
                if cek_url.status_code == 200:
                    sabun = BeautifulSoup(cek_url.text,'html.parser')
                    get_tag = sabun.find_all('div',{'class':'main_div_inline'})
                    if len(get_tag) != 0:
                        link_text = get_tag[0].find_all('a',title=True,class_=False)
                        #print(len(link_text))
                        with ThreadPoolExecutor(max_workers=400) as babi:
                          for abcd in range(len(link_text)):
                              next_link = link_text[abcd]['href']
                              babi.submit(self.grab_themes,next_link)
                    else:
                        print("[E] Enough ")
                else:print('[E] Enough ')
            except Exception as e:

                print('[E] Error ',e)

    # mengumpulkan web dari themes 
    def grab_themes(self,link_url):
        itung = 0 # buat loop 
        while True:
            try:
                itung += 1
                sys.stdout.write('\r[+] Sites Grabbed : {} ({})'.format(len(jumlah_grabbed),itung))
                cek_link = my_session.get(link_url+'/{}'.format(str(itung)),headers={'User-Agent':random.choice(user_agents)})
                if cek_link.status_code == 200:
                    #print(200)
                    sabun = BeautifulSoup(cek_link.text,'html.parser')
                   # print(sabun.find_all('h2'))
                    get_link = sabun.find_all('h2',{'class':'theme_web_h2'})
                    for jumlah_nya in range(len(get_link)):
                        raw_link = get_link[jumlah_nya].text
                        jumlah_grabbed.append(raw_link);print(raw_link) 
                        open('result/themes.txt','a').write(raw_link+'\n')
                else:
                    break
                sys.stdout.flush()
            except Exception as identifier:
                print(identifier)
    
