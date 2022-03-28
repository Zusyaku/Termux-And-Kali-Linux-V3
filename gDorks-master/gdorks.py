# gdorks - Vulnerable website scraper
# Author: WodX
# Version: 1.0.0

import requests
import re
import time
import random
import sys
import os

from colorama import Fore, init

__version__ = '1.0.8'

# globals
use_proxies = False
proxies = None
scrape = False
timeout = None

google_banner = r''' {2}_____             {5}_     
{2}|   __|{3}___ {4}___ {2}___{5}| |{3}___  {0}%s{1}v%s{0}%s
{2}|  |  |{3} . |{4} . |{2} . |{5} |{3} -_|
{2}|_____|{3}___|{4}___|{2}_  |{5}_|{3}___|
              {2}|___|       {0}by WodX
    {6}'''.format(Fore.WHITE, Fore.LIGHTMAGENTA_EX, Fore.BLUE, Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.RESET) % ('{', __version__, '}')

def error(message):
    print(f'{_timestamp()} {Fore.RESET}[{Fore.RED}ERROR{Fore.RESET}] {message}')

def warning(message):
    print(f'{_timestamp()} {Fore.RESET}[{Fore.YELLOW}WARNING{Fore.RESET}] {message}')

def info(message):
    print(f'{_timestamp()} {Fore.RESET}[{Fore.GREEN}INFO{Fore.RESET}] {message}')

def info_update(message):
    print(f'{_timestamp()} {Fore.RESET}[{Fore.GREEN}INFO{Fore.RESET}] {message}\r', end='')

def _timestamp():
    return f'{Fore.RESET}[{Fore.CYAN}{time.strftime("%H:%M:%S")}{Fore.RESET}]'

def _exit():
    print(f'\n[*] Ending @ {time.strftime("%H:%M:%S /%m-%d-%Y/")}\n')
    exit()

def scrape_urls(payload):
    while 1:
        headers = {
            'Host': 'www.google.com',
            'Referer': 'https://google.com/',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.56 Safari/536.5',
            'Connection': 'keep-alive',
            'Cookies': ''
        }
        try:
            # send request using proxy
            if use_proxies:
                proxy = random.choice(proxies)

                session = requests.Session()
                res = session.get('http://www.google.com', proxies={'https': 'http://' + proxy})

                cookies_str = ''
                for key, value in res.cookies.items():
                    cookies_str += f'{key}={value}; '

                headers['cookies'] = cookies_str[:-2]
                res = requests.get(f'http://www.google.com/search?num=100&q={payload}&gws_rd=cr', headers=headers, proxies={'https': 'http://' + proxy}, timeout=timeout if timeout else 10)
                
                # detect captcha block
                if 'Our systems have detected unusual traffic from your computer network' in res.text:
                    warning(f'Request blocked due to CAPTCHA, proxy: \'{proxy}\'')
                    
                    i = random.randint(1, 5)
                    for _ in range(i):
                        info_update(f'Resending HTTP request in {i}...')
                        i -= 1
                        time.sleep(1)
                    info_update(f'Resending HTTP request in 0...')
                    print()
                    continue
                break

            # send request without using proxy
            else:
                res = requests.get(f'http://www.google.com/search?num=100&q={payload}&gws_rd=cr', headers=headers, timeout=timeout if timeout else 10)
                
                # detect captcha block
                if 'Our systems have detected unusual traffic from your computer network' in res.text:
                    error('CAPTCHA has been detected! Try again using the \'--proxies\' argument to bypass this blocking')
                    _exit()
                break

        except Exception as e:
            if e == TimeoutError or e == requests.exceptions.ConnectionError:
                warning(f'Bad proxy: \'{proxy}\'')
            else:
                warning(f'An error occurred while sending HTTP request: {e}')

            i = random.randint(1, 5)
            for _ in range(i):
                info_update(f'Resending HTTP request in {i}...')
                i -= 1
                time.sleep(1)
            info_update(f'Resending HTTP request in 0...')
            print()

    return [x for x in re.findall(r'href="\/url\?q=(.+?)&amp', res.text)]

def main():
    global use_proxies, proxies, scrape, timeout

    init(convert=True)
    
    # banner
    print('''
       {3}_         {5}_       
{2} ___ {3}_| |{4}___ {2}___{5}| |_ {3}___  {0}%s{1}v1.0.0{0}%s
{2}| . |{3} . |{4} . |{2}  _|{5} '_|{3}_ -|
{2}|_  |{3}___|{4}___|{2}_| {5}|_,_|{3}___|
{2}|___|                     {0}by WodX                    
    {6}'''.format(Fore.WHITE, Fore.LIGHTMAGENTA_EX, Fore.BLUE, Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.RESET) % ('{', '}'))

    # handle command arguments
    options = ['-h', '--help', '-s', '-p', '--proxies', '--proxyscrape', '-d', '--dork', '-s', '--scrape', '-t', '--timeout']
    if len(sys.argv) < 2:
        print(f'Usage: python {sys.argv[0]} [options]\n')
        print(f'Use \'python {sys.argv[0]} --help\' for list of options.\n\n')
        input('Press Enter to continue...')
        exit()

    if '--help' in sys.argv or '-h' in sys.argv:
        print(f'Usage: python {sys.argv[0]} [options]\n')
        print('Options:')
        print('  -h, --help            Show list of options')
        print()
        print('  Request:')
        print('    -s, --scrape        Scrape sites from Google searches')
        print('    -d, --dork          Add string to dork payloads. Example: \'site:example.com\'')
        print('    -t, --timeout       Set HTTP request timeout')
        print()
        print('  Proxies:')
        print('    -p, --proxies       Send requests through proxies')
        print('    --proxyscrape       Use proxies from ProxyScrape.com')
        exit()

    proxy_file_index = -1
    if '--proxies' in sys.argv or '-p' in sys.argv:
        use_proxies = True

        for i in range(len(sys.argv)):
            if sys.argv[i] == '--proxies' or sys.argv[i] == '-p':
                try:
                    proxy_file_index = i + 1
                    file_name = sys.argv[proxy_file_index]

                    if file_name == '--proxyscrape':
                        try:
                            res = requests.get('https://api.proxyscrape.com?request=displayproxies&proxytype=http&timeout=2500')
                            
                            proxies = []
                            for proxy in res.text.split('\n'):
                                proxy = proxy.strip()
                                if proxy:
                                    proxies.append(proxy)

                            info(f'{len(proxies)} proxies scraped from ProxyScrape.com')

                            # save proxies
                            _time = time.strftime("%d-%m-%Y %H.%M.%S")
                            file_name = f'{os.getcwd()}\\proxies\\proxyscrape {_time}\\proxies.txt'
                            
                            if not os.path.exists(f'{os.getcwd()}\\proxies'):
                                os.mkdir(f'{os.getcwd()}\\proxies')

                            if not os.path.exists(f'{os.getcwd()}\\proxies\\proxyscrape {_time}'):
                                os.mkdir(f'{os.getcwd()}\\proxies\\proxyscrape {_time}')
                            
                            with open(file_name, 'w') as file:
                                for i, proxy in enumerate(proxies):
                                    file.write(proxy)
                                    if i < len(proxies) - 1:
                                        file.write('\n')

                            info(f'Proxies cached in file @ \'{file_name}\'')
                            print()

                        except Exception as e:
                            error(f'An error occurred while downloading proxies from ProxyScrape.com: {e}')
                            exit()

                    else:
                        if os.path.exists(file_name):
                            proxies = []

                            for j, line in enumerate(open(file_name).readlines()):
                                line = line.strip()
                                if line:
                                    if re.match(r'(^[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}:[0-9]{1,5}$|^[0-9a-zA-Z_]+:[0-9a-zA-Z_]+@[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}:[0-9]{1,5}$)', line):
                                        proxies.append(line)
                                    else:
                                        warning(f'Invalid proxy @ line {j}: \'{line}\'')

                            info(f'{len(proxies)} proxies loaded\n')
                    
                        else:
                            print(f'[-] File path not found @\'{file_name}\'')
                            exit()
                    break

                except Exception:
                    print(f'[-] Missing argument: {sys.argv[i].lower()} [<path>/--proxyscrape]')
                    exit()

    dork_string = None
    dork_index = -1
    if '-d' in sys.argv or '--dork' in sys.argv:
        for i in range(len(sys.argv)):
            if sys.argv[i] == '-d' or sys.argv[i] == '--dork':
                try:
                    dork_index = i + 1
                    dork_string = sys.argv[dork_index]
                    break
                except Exception:
                    print(f'[-] Missing argument: {sys.argv[i].lower()} [<str>]')
                    exit()

    timeout = None
    timeout_index = -1
    if '-t' in sys.argv or '--timeout' in sys.argv:
        for i in range(len(sys.argv)):
            if sys.argv[i] == '-t' or sys.argv[i] == '--timeout':
                try:
                    timeout_index = i + 1
                    timeout = sys.argv[timeout_index]
                    try:
                        timeout = int(timeout)
                        if timeout < 1:
                            raise Exception
                    except:
                        print(f'[-] Invalid timeout value: {timeout}')
                        exit()
                    break
                except Exception:
                    print(f'[-] Missing argument: {sys.argv[i].lower()} [<seconds>]')
                    exit()

    if not '-s' in sys.argv and not '--scrape' in sys.argv:
        print('[-] Missing argument: [-s/--scrape]')
        exit()

    for i in range(1, len(sys.argv)):
        if not sys.argv[i].lower() in options and i != proxy_file_index and i != dork_index and i != timeout_index:
            print(f'[-] Invalid command argument: {sys.argv[i].lower()}')
            exit()

    print(f'[*] Starting @ {time.strftime("%H:%M:%S /%m-%d-%Y/")}\n')

    if dork_string and not re.match(r'^[a-zA-Z]+:(.*)$', dork_string):
        warning(f'Dork string \'{dork_string}\' looks strange\n')

    if timeout and timeout > 10:
        warning(f'Timeout value is set to a high value: \'{timeout}\' seconds\n')

    # load payloads
    info(f'Loading {Fore.BLUE}G{Fore.RED}o{Fore.YELLOW}o{Fore.BLUE}g{Fore.GREEN}l{Fore.RED}e {Fore.RESET}dorking payloads (file exposure, login page, password exposure, phpinfo(), SQL error exposure, SQL injection, cross-site scripting (XSS))')
    try:
        payload_file = open('payloads/file-exposure.txt').readlines()
        payload_login = open('payloads/login-pages.txt').readlines()
        payload_password = open('payloads/password-exposure.txt').readlines()
        payload_phpinfo = open('payloads/phpinfo.txt').readlines()
        payload_sqle = open('payloads/sql-errors.txt').readlines()
        payload_sqli = open('payloads/sql-injection.txt').readlines()
        payload_xss = open('payloads/xss.txt').readlines()
    except:
        error(f'Missing files @ \'{os.getcwd()}\\payloads\'')

    # create directory name for cached vulnerable website URLs
    dir_name = f'{os.getcwd()}\\output\\{time.strftime("%d-%m-%Y %H.%M.%S")}'

    # file exposure scrape
    info(f'Scraping file exposing sites - {len(payload_file)} payloads(s) loaded')
    urls = []
    for payload in payload_file:
        payload = payload.strip()

        if dork_string:
            payload = dork_string + ' ' + payload

        info(f'Trying file exposure payload \'{payload}\'')
        for url in scrape_urls(payload):
            urls.append(url)
        info(f'{len(urls)} file exposing site(s) scraped using payload \'{payload}\'')

    info(f'Caching scraped file exposing sites to directory: \'{dir_name}\\file-exposure.txt\'')
    with open(dir_name + '\\file-exposure.txt', 'w') as file:
        for url in urls:
            file.write(url + '\n')

    # login sites scrape
    info(f'Scraping login sites - {len(payload_login)} payloads(s) loaded')
    urls = []
    for payload in payload_login:
        payload = payload.strip()

        if dork_string:
            payload = dork_string + ' ' + payload

        info(f'Trying login payload \'{payload}\'')
        for url in scrape_urls(payload):
            urls.append(url)
        info(f'{len(urls)} login site(s) scraped using payload \'{payload}\'')

    info(f'Caching scraped login sites to directory: \'{dir_name}\\login-pages.txt\'')
    with open(dir_name + '\\login-pages.txt', 'w') as file:
        for url in urls:
            file.write(url + '\n')

    # password exposure scrape
    info(f'Scraping password exposing sites - {len(payload_password)} payloads(s) loaded')
    urls = []
    for payload in payload_password:
        payload = payload.strip()

        if dork_string:
            payload = dork_string + ' ' + payload

        info(f'Trying password exposure payload \'{payload}\'')
        for url in scrape_urls(payload):
            urls.append(url)
        info(f'{len(urls)} password exposing site(s) scraped using payload \'{payload}\'')

    info(f'Caching scraped password exposing sites to directory: \'{dir_name}\\password-exposure.txt\'')
    with open(dir_name + '\\password-exposure.txt', 'w') as file:
        for url in urls:
            file.write(url + '\n')

    # phpinfo() scrape
    info(f'Scraping phpinfo() vulnerable sites - {len(payload_phpinfo)} payloads(s) loaded')
    urls = []
    for payload in payload_phpinfo:
        payload = payload.strip()

        if dork_string:
            payload = dork_string + ' ' + payload

        info(f'Trying phpinfo() payload \'{payload}\'')
        for url in scrape_urls(payload):
            urls.append(url)
        info(f'{len(urls)} phpinfo() site(s) scraped using payload \'{payload}\'')

    info(f'Caching scraped phpinfo() sites to directory: \'{dir_name}\\phpinfo.txt\'')
    with open(dir_name + '\\phpinfo.txt', 'w') as file:
        for url in urls:
            file.write(url + '\n')
    
    # sql error exposure
    info(f'Scraping SQL error exposing sites - {len(payload_sqle)} payloads(s) loaded')
    urls = []
    for payload in payload_sqle:
        payload = payload.strip()

        if dork_string:
            payload = dork_string + ' ' + payload

        info(f'Trying SQL error payload \'{payload}\'')
        for url in scrape_urls(payload):
            urls.append(url)
        info(f'{len(urls)} SQL error exposing site(s) scraped using payload \'{payload}\'')

    info(f'Caching scraped SQL error exposing sites to directory: \'{dir_name}\\sql-error.txt\'')
    with open(dir_name + '\\sql-error.txt', 'w') as file:
        for url in urls:
            file.write(url + '\n')

    # sql injection scrape
    info(f'Scraping SQL injection vulnerable sites - {len(payload_sqli)} payloads(s) loaded')
    urls = []
    for payload in payload_sqli:
        payload = payload.strip()

        if dork_string:
            payload = f'{dork_string} {payload}'

        info(f'Trying SQL injection payload \'{payload}\'')
        for url in scrape_urls(payload):
            urls.append(url)
        info(f'{len(urls)} SQL injection vulnerable site(s) scraped using payload \'{payload}\'')

    info(f'Caching scraped SQL injection vulnerable sites to directory: \'{dir_name}\\sql-injection.txt\'')
    with open(dir_name + '\\sql-injection.txt', 'w') as file:
        for url in urls:
            file.write(url + '\n')

    # xss scrape
    info(f'Scraping cross-site scripting (XSS) vulnerable sites - {len(payload_xss)} payloads(s) loaded')
    urls = []
    for payload in payload_xss:
        payload = payload.strip()

        if dork_string:
            payload = dork_string + ' ' + payload

        info(f'Trying cross-site scripting (XSS) payload \'{payload}\'')
        for url in scrape_urls(payload):
            urls.append(url)
        info(f'{len(urls)} cross-site scripting (XSS) vulnerable site(s) scraped using payload \'{payload}\'')

    info(f'Caching scraped cross-site scripting (XSS) vulnerable sites to directory: \'{dir_name}\\xss.txt\'')
    with open(dir_name + '\\xss.txt', 'w') as file:
        for url in urls:
            file.write(url + '\n')

    info(f'Scraping finished! Thank you for using {Fore.BLUE}g{Fore.RED}d{Fore.YELLOW}o{Fore.BLUE}r{Fore.GREEN}k{Fore.RED}s')

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        error(f'An error occurred: {e}')
    except KeyboardInterrupt:
        pass
    _exit()