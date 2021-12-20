from json import dumps, loads
from types import SimpleNamespace as SN
from bs4 import BeautifulSoup as bs
from requests import get
from concurrent.futures import ThreadPoolExecutor
import validators

class extracts:

    def __init__(self, url) -> None:
        self.url = None
        self.content = None
        self.title = None
        if validators.url(url) and 'https://otakudesu.moe' in url:
            self.url = url
            self.content = bs(get(self.url).text, 'html.parser').find('div', {'class': 'venser'})
            self.anu = list(self.content.find('div', {'class': 'infozingle'}).strings)
            self.title = self.anu[1].strip(': ')

    @property
    def extract(self):
        if self.url:
            sinfo = list(self.content.find('div', {'class': 'infozingle'}).strings)
            genres = []
            linkdl = self.extractLink
            for _ in self.content.findAll('a', {'rel': 'tag'}):
                if _['href'] == ' ':pass
                else:genres.append(_.text)
            results = {'title': self.title, 'thumbnail': self.content.img['src'], 'jp_title': sinfo[3].strip(': '), 'rating': sinfo[5].strip(': '), 'producers': sinfo[7].strip(': '), 'type': sinfo[9].strip(': '), 'status': sinfo[11].strip(': '), 'episodes': sinfo[13].strip(': '), 'duration': sinfo[15].strip(': '), 'release_date': sinfo[17].strip(': '), 'genres': genres, 'synopsis': self.content.find('div', {'class': 'sinopc'}).text, 'downloads': linkdl, 'studio': sinfo[19].strip(': ')}
            return loads(dumps(results), object_hook=lambda d: SN(**d))

    @property
    def extractLink(self):
        meki = {}
        puki = {}
        deel = {}
        try:
            for _ in self.content.findAll('a', {'target': '_blank', 'data-wpel-link': 'internal'})[:-3]:
                if ':' in _.text:pass
                else:
                    for e in bs(get(_['href']).text, 'html.parser').find('div', {'class': 'download'}).findAll('ul'):
                        for __ in e.findAll('li'):
                            for ___ in __.findAll('a'):
                                deel.update({___.text.lower(): ___['href']})
                            puki.update({'_'+'_'.join(__.strong.text.lower().split(' ')): deel})
                            deel = {}
                        meki.update({'eps'+''.join(filter(str.isdigit, _.text.split('Episode')[1].split()[0])) if 'batch' not in _.text.lower() and 'episode' in _.text.lower() else 'batch': puki})
            return meki
        except AttributeError:
            return []

    def __str__(self) -> str:
        return '<[title: %s]>' % self.title

    def __repr__(self) -> dict:
        return self.__str__()

class extractFromSearch:

    def __init__(self, content) -> None:
        self.result = []
        for _ in content:
            with ThreadPoolExecutor(max_workers=3) as moe:
                if 'anime' in _.a['href']:self.result.append(moe.submit(extracts, _.a['href']).result().extract)

    def __str__(self) -> str:
        return '<[result: %s]>' % self.result.__len__()

    def __repr__(self) -> str:
        return self.__str__()

class extractFromSchedule:

    def __init__(self, content) -> None:
        self.result = {}
        count = 0
        days = ['senin','selasa','rabu','kamis','jumat','sabtu','minggu','random']
        res = []
        for _ in content:
            for __ in _.findAll('a'):
                with ThreadPoolExecutor(max_workers=3) as moe:
                    if 'anime' in __['href']:res.append(moe.submit(extracts, __['href']).result().extract)
            self.result.update({days[count]: res})
            count += 1
            res = []
        # self.result = loads(dumps(self.result), object_hook=lambda d: SN(**d))

    def __str__(self) -> str:
        return '<[result: %s]>' % self.result.__len__()

    def __repr__(self) -> str:
        return self.__str__()
