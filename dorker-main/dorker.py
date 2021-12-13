import argparse
import sys
from helium import *
import time
import os 

prev_url = -1
final = []
driver = -1

def banner():
    print("""
    ______ ___________ _   __ ___________ 
    |  _  \  _  | ___ \ | / /|  ___| ___ |
    | | | | | | | |_/ / |/ / | |__ | |_/ /
    | | | | | | |    /|    \ |  __||    / 
    | |/ /\ \_/ / |\ \| |\  \| |___| |\ \ 
    |___/  \___/\_| \_\_| \_/\____/\_| \_|             

        Created by @0xdln and @0xrj_
    """)

def parser_error(self):
    banner()
    print("Usage: python " + sys.argv[0] + " [Options] use -h for help")
    sys.exit()


def parse_args():
    parser = argparse.ArgumentParser(epilog='\tExample: \r\npython ' + sys.argv[0] + " -d 'THE-DORK-YOU-WANT'")
    parser.error = parser_error
    parser._optionals.title = "OPTIONS"
    parser.add_argument('-f', '--dorkfile', required=False)
    parser.add_argument('-d', '--dork', required=False)
    parser.add_argument('-o', '--output', required=False)
    args = parser.parse_args()
    return args


def input_(dork):
    helium.write(dork)
    helium.press(ENTER)
    time.sleep(2)

def re_enter():
    global prev_url
    global driver
    driver = helium.start_firefox(headless=False)
    time.sleep(5)
    go_to(prev_url)
    flow()


def urlExtract():
    global final
    urls = helium.find_all(S('.yuRUbf'))
    url = [i.web_element.find_element_by_tag_name('a').get_attribute('href') for i in urls]
    if (url == []):
        kill_browser()
        re_enter()
    url = clean(url)
    final.extend(url)

def pages():
    global driver
    global prev_url
    while True:
        try:
            prev_url = driver.current_url
            helium.scroll_down(num_pixels=100000)
            helium.click('Next')
            time.sleep(2)
            urlExtract()
        except:
            break


def clean(li):
    li = set(li)
    return list(li)

def flow():
    urlExtract()
    time.sleep(2)
    pages()
    try:
        kill_browser()
    except:
        pass

def exechaha(args,dorks):
    global driver
    if(args.dorkfile):
        with open(dorks) as f:
            while True:
                line = f.readline()
                if not line:
                    break
                else:
                    driver = helium.start_firefox(headless=False)
                    go_to('www.google.com')
                    input_(line)
                    time.sleep(5)
                    flow()

    else:
        line = args.dork
        driver = helium.start_firefox(headless=True)
        time.sleep(5)
        go_to('www.google.com')
        input_(line)
        time.sleep(5)
        flow()
        
def main():
    banner()
    global final
    args = parse_args()
    dorks = args.dorkfile
    exechaha(args,dorks)
    if(args.output):
        file1 = open(args.output+'.txt', 'w')
        for i in clean(final):
            file1.write(i.strip()+'\n')
        file1.close()
    else:
        for i in clean(final):
            print(i)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n[ERR]: Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
