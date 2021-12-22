#!/usr/bin/env python
#
#    This script will download all images from given tumblr website
#   Devilzc0de(c) 2012
#
#
import urllib
import urllib2
import sys
import os
import re
from math import fabs

pageStart = 1
pageEnd = 999
pageNum = 1
failed_counter = 0
last_page = ''
ver = '0.2'

def get_link(siteName):
    global pageNum, failed_counter, last_page

    html_url = 'http://' + siteName + '.tumblr.com/page/' + str(pageNum)
    print('[+] page\t: ' + html_url)
    html_page = get_file(html_url)
    
    num_images = get_images(siteName, html_page)
    
    if num_images == 0:
        failed_counter += 1
    if fabs(len(html_page) - len(last_page)) <= 13:
        failed_counter += 1
    if failed_counter == 3:
        create_index_html(siteName)
        print('[-] exit\t: ' + str(failed_counter) + ' pages without images')
        raise SystemExit
    last_page = html_page
    pageNum +=1
    

def get_images(siteName, html_page):
    global failed_counter
    mObj = re.findall(r'<img([^>]*)src=\"([^\"]*)\"([^>]*)>', html_page)    
    count = 0
    if mObj:
        for i in mObj:
            img = i[1]
            # avatar_394f5be4958e_40.png
            if not re.match(r'.*avatar_[a-fA-F0-9]{12}_.*', img):
                save_file(siteName, img)
                count += 1
    else:
        failed_counter += 1
    return count
        
def save_file(siteName, url):
    filename = os.path.basename(url)
    if not os.path.isfile(siteName + '/' + filename):
        print('[+] image\t: ' + url)
        urllib.urlretrieve(url, siteName + '/' + filename)
        
def get_file(url):
    res = urllib2.urlopen(url)
    html = res.read()
    return html

def make_dir(d):
    if not os.path.exists(d):
        os.makedirs(d)

def show_usage():
    global ver
    print('\tusage : python ' + os.path.basename(sys.argv[0]) + ' [site] [start page] [end page]\n')
    print('\tex    : python ' + os.path.basename(sys.argv[0]) + ' example1.tumblr.com 1 50')
    print('\tex    : python ' + os.path.basename(sys.argv[0]) + ' example2.tumblr.com\n\n')
    
    raise SystemExit
    
def create_index_html(siteName):
    dirs = os.listdir(siteName)
    
    fObj = open(siteName + '.html', "w")
    
    for img in dirs:
        fObj.write('<img src=' + siteName + '/' + img + ' /><br /><br />')
    fObj.close()
    print('[+] result\t: ' + siteName + '.html')
        
if __name__=='__main__':
    print('\nDownload images from tumblr - ver ' + ver + '\n')
    
    
    if(len(sys.argv)==2):
        siteName = sys.argv[1].lower()
    elif(len(sys.argv)==3):
        siteName = sys.argv[1]
        pageStart = int(sys.argv[2])
    elif(len(sys.argv)==4):
        siteName = sys.argv[1]
        pageStart = int(sys.argv[2])
        pageEnd = int(sys.argv[3])
    else:
        show_usage()
    
    pageNum = pageStart
    siteName = re.sub(r'\.tumblr\.com','', siteName)
    siteName = re.sub(r'http://','', siteName)
    siteName = re.sub(r'/','', siteName)
    
    html_url = 'http://' + siteName + '.tumblr.com'
    print('[+] site\t: ' + html_url)
    try:
        for page in range(pageStart, pageEnd+1):
            make_dir(siteName)
            get_link(siteName)
    except:
        print('\n')