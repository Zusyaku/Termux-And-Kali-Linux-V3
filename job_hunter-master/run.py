#!/usr/bin/env python3
import os, sys, time,argparse
from urllib.request import urlopen
from bs4 import BeautifulSoup

def parse_args():
    # Create the arguments
    parser = argparse.ArgumentParser(prog='Job Hunter')
    parser.add_argument("-jt", "--jobtitle", help="Job Title. Example: -jt System Administrator/Ethical hacker/Linux System Administrator")
    parser.add_argument("-l", "--location", help="Location. Example: -l Berlin")
    parser.add_argument("-z", "--zipcode", help="Zipcode. Example: -z 3078TR")
    parser.add_argument("-i", "--interval", help="Interval to search for jobs in seconds (default: 10). Example: -i 10")
    return parser.parse_args()

args = parse_args()

global companies
global titles
global locations
global websites
global links
companies = []
titles = []
locations = []
websites = []
links = []

def get_pages(url, jobtitle, location):
    # Get the up to 5 pages
    soup = BeautifulSoup(urlopen(url), 'html.parser')
    find_pages = soup.find_all('span', attrs={'class': 'pn'})

    pages = []
    for page in find_pages:
        pages.append(page.text.strip())

    # TRY to delete it, if it can't be deleted, there is most likely just one page
    try:
        del pages[-1] # Remove 'Next' from list, I need values, not strings.
        max_pages = int(max(pages))
    except:
        max_pages = 0


    c = 0
    for i in range(1,int(max_pages) + 1):
        link = 'https://www.indeed.nl/jobs?q=%s&l=%s&start=%i' % (jobtitle, location, c)
        search_indeed(link, jobtitle)
        c +=10

def search_indeed(url, jobtitle):
    #print('Searching page [%i] on url [%s]' % (int(page), url))
    soup = BeautifulSoup(urlopen(url), 'html.parser')

    #print('[i] Searching for jobs as [%s] on Indeed.nl' % jobtitle)

    find_company_names = soup.find_all('span', attrs={'class': 'company'})
    find_job_titles = soup.find_all('a', attrs={'data-tn-element': 'jobTitle'})


    for href in soup.find_all('a', attrs={'data-tn-element': 'jobTitle'}, href=True):
        links.append('https://www.indeed.nl' + href['href'])

    for i in find_company_names:
        companies.append(i.text.strip())
        websites.append('https://www.indeed.nl')

    for i in find_job_titles:
        titles.append(i.text.strip())

    try:
        for location in soup.find_all('div', attrs={'style': 'display: none'}):
            locations.append(location['data-rc-loc'])
    except:
        pass

    result(jobtitle)

def result(jobtitle):
    c = 0
    filepath = './log.csv'

    # Check if logfile exists, if not, create it
    if not os.path.isfile(filepath):
        with open(filepath, 'w+') as f:
            f.write('Num.,Query,Job Title,Company,Website,Link\n')
            f.close()
        print('[+] Created logfile at %s' % filepath)

    for i in range(len(companies)):
        result = str(c) + ')', jobtitle, titles[i], companies[i], locations[i], links[i]
        check = open(filepath).read()

        # If it's not a duplicate, print and save result
        if not companies[i] in check:
            c +=1
            print('%s %s %s %s %s' % (result[0].ljust(10), result[1].ljust(30), result[2].ljust(60), result[3].ljust(40), result[4].ljust(40)))
            with open(filepath, 'a+') as f:
                f.write('%s,%s,%s,%s,%s,%s\n' % (result[0], result[1], result[2], result[3], result[4], result[5]))
                f.close()

if not args.interval:
    interval = 10
else:
    interval = args.interval

# Run
#if args.jobtitle == None or args.location == None or args.zipcode == None:
if args.jobtitle == None or args.location == None:
    print('[ERROR] Please give a jobtitle, location...')
else:
    try:
        job = args.jobtitle.split('/')
        for i in job:
            print('[i] Monitoring for jobs as %s' % i)

        try:
            while True:
                for i in job:
                    i = i.replace(' ','+')
                    url = 'https://www.indeed.nl/jobs?q=%s&l=%s' % (i, args.location)
                    get_pages(url, i, args.location)
                time.sleep(interval)
        except KeyboardInterrupt:
            try:
                f = open('./log.csv').readlines()
                print('Logged %i jobs!' % len(f))
            except:
                pass
            print('[i] Stopped...\n')

    except Exception as e:
        print(e)
        print('[i] Monitoring for jobs as %s' % args.jobtitle)
        try:
            while True:
                url = 'https://www.indeed.nl/jobs?q=%s&l=%s' % (args.jobtitle, args.location)
                get_pages(url, args.jobtitle, args.location)
                time.sleep(interval)
        except KeyboardInterrupt:
            try:
                f = open('./log.csv').readlines()
                print('Logged %i jobs!' % len(f))
            except:
                pass
            print('[i] Stopped...\n')
