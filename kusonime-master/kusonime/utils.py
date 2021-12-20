from requests import Session, get
from bs4 import GuessedAtParserWarning, BeautifulSoup as bs
from typing import Union
from re import search
from warnings import filterwarnings
from .kuso import KusoInfo, KusoSearch
filterwarnings("ignore", category=GuessedAtParserWarning)

class Scrap(Session):

    def __init__(self, url: Union[str]) -> None:
        """
        :url: String
        :e.g:
        from kusonime import Scrap
        scrap = Scrap("https://kusonime.com/kawaisou-batch-sub-indo/")
        scrap.to_json
        """
        super().__init__()
        self.url = url
        self.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36 OPR/67.0.3575.137"})

    def __title(self, text: Union[str]) -> str:
        """
        Delete "Batch (BD|Subtitle) ....." from text
        :text: String
        """
        text = text if "Batch" not in text else text.split("Batch")[0].strip()
        return text if "BD" not in text else text.split("BD")[0].strip()

    def __split(self, text: Union[str]) -> str:
        """
        Split text
        :text: String
        """
        return text.split(":")[1].lstrip()

    def __synopsis(self, title: Union[str], text: Union[str]) -> str:
        """
        :text: String
        """
        if (fix := search("Fix (\d+)", text)):
            text = text.split(fix.group())[0].strip()
            if "credit:" in text.lower() or "credit :" in text.lower():
                text = text.lower().split("credit")[0].title()
        elif f"Download {title}" in text:
            text = text.split(f"Download")[0].strip()
            if "credit:" in text.lower() or "credit :" in text.lower():
                text = text.lower().split("credit")[0].title()
        elif "credit:" in text.lower() or "credit :" in text.lower():
            text = text.lower().split("credit")[0].title()
        return text

    def fetch(self, download: Union[bool]=True) -> KusoInfo:
        """
        Fetch infomartion anime from kusonime
        Set to False if you don't want to show download url
        :download: Boolean
        :return: AnimeInfo
        """
        try:
            html = self.get(self.url).text
            parse = bs(html, "html.parser").find("div", {"class": "venser"})
            info = KusoInfo()
            info.title = self.__title(parse.h1.text)
            info.title_jp = self.__split(parse.p.text)
            info.thumbnail = parse.img.get("src")
            info.genres = [g.text for g in list(parse.p.next_siblings)[0].select("a")]
            info.seasons = self.__split(list(parse.p.next_siblings)[1].text)
            info.producers = self.__split(list(parse.p.next_siblings)[2].text)
            info.type = self.__split(list(parse.p.next_siblings)[3].text)
            info.status = self.__split(list(parse.p.next_siblings)[4].text)
            info.total_epidode = self.__split(list(parse.p.next_siblings)[5].text)
            info.score = self.__split(list(parse.p.next_siblings)[6].text)
            info.duration = self.__split(list(parse.p.next_siblings)[7].text)
            info.released_on = self.__split(list(parse.p.next_siblings)[8].text)
            try:
                info.synopsis = self.__synopsis("%s %s" % (info.title, "\n".join([i.text.strip() for i in bs(search(search(r"<strong>(.+?)</strong>", html).group()+"(.*?)<p style=\"text-align: center;\">", html).group(1)).select("p")])))
            except:
                info.synopsis = self.__synopsis(info.title, list(parse.find("div", {"class": "info"}).next_siblings)[1].text)
            if download:
                info.download = {}
                for y in parse.select("div[class=\"smokeurl\"]"):
                    info.download[y.strong.text] = {}
                    for z in y.select("a"):
                        info.download[y.strong.text].update({z.text: z.get("href")})
            return info
        except Exception as e:
            print(e)
            return Exception("Error while scraping")

class Recom:

    def __init__(self, page: Union[int]=1) -> None:
        """
        :page: Integer
        :e.g:
        from kusonime import Recom
        rec = Recom(2).fetch
        rec[0].to_json
        """
        self.url = "https://kusonime.com/{0}"
        self.page = page

    @property
    def fetch(self) -> list:
        if self.page < 1:
            self.url = self.url
        elif self.page > 319:
            self.url = self.url.format("page/319/")
        else:
            self.url = self.url.format(f"page/{self.page}/")

        try:
            return [Scrap(i.get("href")).fetch() for i in bs(get(self.url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36 OPR/67.0.3575.137"}).text, "html.parser").find("div", {"class": "recomx"}).select("a")]
        except Exception as e:
            print(e)
            return Exception("Error while scraping")

class Search:

    def __init__(self, query: Union[str], page: Union[int]=1) -> None:
        """
        :query: String
        :page: Integer
        """
        self.page = page
        self.query = query
        self.url = "https://kusonime.com/page/{0}/?s={1}&post_type=post"

    @property
    def fetch(self) -> KusoSearch:
        try:
            parse = bs(get(self.url.format(self.page, self.query), headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36 OPR/67.0.3575.137"}).text, "html.parser").find("div", {"class": "venser"})
            search = KusoSearch()
            if (res := parse.select("a")):
                search.result = [Scrap(i.get("href")).fetch() for i in res if i.img]
                if res[-1].text == "Next Page »":
                    self.page += 1
                    search.next_page = self.fetch
            return search
        except Exception as e:
            print(e)
            return Exception("Anime not found")
