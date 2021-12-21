import asyncio
import os
import sys
import time

import colorama
import pypeln as pl
from aiohttp import ClientSession, TCPConnector
from fake_useragent import UserAgent


colorama.init()
reset = '\033[0m'
fg = [
    '\033[91;1m',
    '\033[92;1m',
    '\033[93;1m',
    '\033[94;1m',
    '\033[95;1m',
    '\033[96;1m',
    '\033[97;1m'
]
ua = UserAgent()


class YahooChecker:
    def __init__(self):
        self.banner()
        self.load()
        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(self.run())
        loop.run_until_complete(future)

    def banner(self):
        #region Banner
        print('''{0}▓██   ██▓ ▄▄▄       ██░ ██  ▒█████   ▒█████      ▄████▄   ██░ ██ ▓█████  ▄████▄   ██ ▄█▀▓█████  ██▀███  
 ▒██  ██▒▒████▄    ▓██░ ██▒▒██▒  ██▒▒██▒  ██▒   ▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
  ▒██ ██░▒██  ▀█▄  ▒██▀▀██░▒██░  ██▒▒██░  ██▒   ▒▓█    ▄ ▒██▀▀██░▒███   ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
  ░ ▐██▓░░██▄▄▄▄██ ░▓█ ░██ ▒██   ██░▒██   ██░   ▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
  ░ ██▒▓░ ▓█   ▓██▒░▓█▒░██▓░ ████▓▒░░ ████▓▒░   ▒ ▓███▀ ░░▓█▒░██▓░▒████▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
   ██▒▒▒  ▒▒   ▓▒█░ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░    ░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
 ▓██ ░▒░   ▒   ▒▒ ░ ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░      ░  ▒    ▒ ░▒░ ░ ░ ░  ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
 ▒ ▒ ░░    ░   ▒    ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒     ░         ░  ░░ ░   ░   ░        ░ ░░ ░    ░     ░░   ░
 ░ ░           ░  ░ ░  ░  ░    ░ ░      ░ ░     ░ ░       ░  ░  ░   ░  ░░ ░      ░  ░      ░  ░   ░
 ░ ░                                            ░                       ░

\t{1}Created By : {2}SH0G0 {3}TG (@makishima_sh0g0) {4}| {2}Fastest {1}Yahoo Valid {3}Email {4}and {3}Phone Number {1}Checker
'''.format(fg[0], fg[5], fg[1], fg[6], fg[4]))
        #endregion Banner

    def load(self):
        is_targets = False
        while not is_targets:
            print('\t{0}┌╼[ {1}SH0G0 {0}]╾─╼[ {2}Enter {3}Emails/Phone Numbers{2} List {4}Filename {0}]\n\t└───╼ {1}'.format(fg[5], fg[1], fg[6], fg[3], fg[2]), end='')
            filename = input('').replace('"', '').replace('\'', '')
            if '.txt' not in filename:
                filename = filename + '.txt'
            if not os.path.isfile(filename):
                print('\t{0}[ {1}ERROR{0} ] {0}- {1}File {0}({3}{4}{0}){1} Not Found!'.format(fg[5], fg[0], fg[3], fg[2], filename), end='\r')
                time.sleep(0.5)
                print(' ' * (45 + len(filename)))
                continue
            else:
                with open(filename) as file:
                    self.targets = [x.split(':')[0].lower() for x in file.read().splitlines() if x]
                if len(self.targets) < 2:
                    print('\t{0}[ {1}ERROR{0} ] {0}- {1}Please enter {2}emails/phone numbers {1}list on {0}({3}{4}{0}){1}!'.format(fg[5], fg[0], fg[3], fg[2], filename), end='\r')
                    time.sleep(0.5)
                    print(' ' * (55 + len(filename)))
                    continue
                is_targets = True
        self.targets_fn = filename.split('.')[0]

    async def run(self):
        async with ClientSession(connector=TCPConnector(limit=None, ssl=False)) as session:
            payload = {
                'browser-fp-data': {
                    'language':'en-US',
                    'colorDepth': 24,
                    'deviceMemory': 8,
                    'pixelRatio': 1,
                    'hardwareConcurrency': 12,
                    'timezoneOffset': '-480',
                    'timezone': 'Asia/Singapore',
                    'sessionStorage': 1,
                    'localStorage': 1,
                    'indexedDb': 1,
                    'openDatabase': 1,
                    'cpuClass': 'unknown',
                    'platform': 'Win32',
                    'doNotTrack': '1',
                    'plugins': {
                        'count': 3,
                        'hash': 'e43a8bc708fc490225cde0663b28278c'
                    },
                    'canvas': 'canvas winding:yes~canvas',
                    'webgl': 1,
                    'webglVendorAndRenderer': 'Google Inc. (NVIDIA)~ANGLE (NVIDIA, NVIDIA GeForce RTX 3070 Direct3D11 vs_5_0 ps_5_0, D3D11-27.21.14.6627)',
                    'adBlock': 0,
                    'hasLiedLanguages': 0,
                    'hasLiedResolution': 0,
                    'hasLiedOs': 0,
                    'hasLiedBrowser': 0,
                    'touchSupport': {
                        'points': 0,
                        'event': 0,
                        'start': 0
                    },
                    'fonts': {
                        'count': 48,
                        'hash': '62d5bbf307ed9e959ad3d5ad6ccd3951'
                    },
                    'audio': '124.04347527516074',
                    'resolution': {
                        'w': '1920',
                        'h': '1080'
                    },
                    'availableResolution': {
                        'w': '1040',
                        'h': '1920'
                    },
                    'ts': {
                        'serve': 1620489627957,
                        'render': 1620489626853
                    }
                },
                'crumb': '',
                'acrumb': '',
                'sessionIndex': '',
                'displayName': '',
                'deviceCapability': {
                    'pa': {
                        'status': False
                    }
                },
                'countryCodeIntl': 'AS',
                'username': '',
                'passwd': '',
                'signin': 'Next'
            }
            async def create_session(user_agent):
                header = {
                    'User-Agent': user_agent
                }
                async with session.get('https://login.yahoo.com', headers=header) as query:
                    response = await query.text()
                    d1 = response.split('name="crumb" value="')[1].split('"')[0]
                    d2 = response.split('name="acrumb" value="')[1].split('"')[0]
                    d3 = response.split('name="sessionIndex" value="')[1].split('"')[0]
                    return (d1, d2, d3)
                    
            async def status(response, target):
                if not target.startswith('+'):
                    target = f'+{target}'
                if 'Sorry, we don&#x27;t recognize this' in response:
                    print('\t{0}[DEAD]{1}╾┄╼{2}[{3}{5}{1}/{3}{6}{2}]{1}╾┄╼{2}[{4}{7}{2}]'.format(
                        fg[0], fg[4], fg[5], fg[2], fg[6], (self.targets.index(target) + 1), len(self.targets), target
                    ))
                elif '/account/challenge/recaptcha/redirect?done' in response:
                    print('\t{0}[LIVE]{1}╾┄╼{2}[{3}{5}{1}/{3}{6}{2}]{1}╾┄╼{2}[{4}{7}{2}]'.format(
                        fg[1], fg[4], fg[5], fg[2], fg[6], (self.targets.index(target) + 1), len(self.targets), target
                    ))
                    with open(f'LIVE({self.targets_fn}).txt', 'a+') as file:
                        file.write(f'{target}\n')

            async def check(target):
                try:
                    target = target.replace('+', '')
                    user_agent = ua.chrome
                    d1, d2, d3 = await create_session(user_agent)
                    payload['crumb'] = d1
                    payload['acrumb'] = d2
                    payload['sessionIndex'] = d3
                    payload['username'] = target
                    headers = {
                        'DNT': '1',
                        'Host': 'login.yahoo.com',
                        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
                        'sec-ch-ua-mobile': '?0',
                        'Sec-Fetch-Dest': 'document',
                        'Sec-Fetch-Mode': 'navigate',
                        'Sec-Fetch-Site': 'none',
                        'Sec-Fetch-User': '?1',
                        'Upgrade-Insecure-Requests': '1',
                        'User-Agent': user_agent
                    }
                    async with session.post('https://login.yahoo.com', data=payload, headers=headers) as query:
                        response = await query.text()
                        await status(response, target)
                except Exception as error:
                    print(error)
                    return None

            print('\t{0}┌╼[ {1}SH0G0 {0}]╾─╼[ {2}Enter {3}Workers{2} {4}Count {0}]\n\t└───╼ {1}'.format(fg[5], fg[1], fg[6], fg[3], fg[2]), end='')
            count = int(input('').replace('"', '').replace('\'', ''))
            await pl.task.each(
                check, self.targets, workers=count,
            )


if __name__ == '__main__':
    try:
        YahooChecker()
    except KeyboardInterrupt:
        sys.exit()
