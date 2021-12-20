from requests import get, post
from bs4 import BeautifulSoup as bs
from .utils import extracts, extractFromSearch, extractFromSchedule

class OtakuDesu:

    def __init__(self) -> None:
        self.BaseUrl = 'https://otakudesu.moe'
        self.SearchUrl = 'https://otakudesu.moe?s=%s&post_type=anime'
        self.scheduleUrl = 'https://otakudesu.moe/jadwal-rilis/'

    def search(self, query:str):
        return extractFromSearch(bs(post(self.SearchUrl % query).text, 'html.parser').find('ul', {'class': 'chivsrc'}).findAll('li'))

    def byUrl(self, url:str):
        if self.BaseUrl + '/anime' not in url:assert Exception('Url is invalid')
        return extracts(url).extract

    @property
    def getSchedule(self):
        return extractFromSchedule(bs(get(self.scheduleUrl).text, 'html.parser').find('div', {'class': 'venutama'}).findAll('ul'))
