<p align="center">
<img src="https://i.ibb.co/fHMgR1K/images-q-tbn-ANd9-Gc-Svzf1k-D0-UFBj-n2k-IDxm-A7-SGm-Ieb5-PQ0th0w-usqp-CAU.jpg" alt="nekopoi"/>
</p>

### Features
----------
- [x] Scrap from url
----------
### Todo
----------
- [-] Search by genre
- [-] Search by query
- [-] Scrap from homepage
----------

### Example
```python
# Hentai Scraper
>>> from nekopoi import Hent
>>> sc = Hent("https://nekopoi.care/kono-kaisha-nanika-okashii-episode-2-subtitle-indonesia/").getto
>>> sc.to_json
# Hentai Scraper Using Proxy
>>> from nekopoi import Hent
>>> sc = Hent("https://nekopoi.care/kono-kaisha-nanika-okashii-episode-2-subtitle-indonesia/", proxy={"http": "http://host:port"}).getto
>>> sc.to_json

# Jav Scraper
>>> from nekopoi import Jav
>>> ja = Jav("https://nekopoi.care/ipx-700-jav-miu-shiramine-a-super-luxury-mens-beauty-treatment-salon-that-makes-beautiful-legs-glamorous-testicles/").getto
>>> ja.to_json
# Jav Scraper Using Proxy
>>> from nekopoi import Jav
>>> ja = Jav("https://nekopoi.care/ipx-700-jav-miu-shiramine-a-super-luxury-mens-beauty-treatment-salon-that-makes-beautiful-legs-glamorous-testicles/", proxy={"http": "http://host:port"}).getto
>>> ja.to_json

# 3D Hentai Scraper
>>> from nekopoi import ThreeD
>>> tridi = ThreeD("https://nekopoi.care/3d-hentai-hige-wo-soru-fucked-sayu-ogiwara/").getto
>>> tridi.to_json
# 3D Hentai Scraper Using Proxy
>>> from nekopoi import ThreeD
>>> tridi = ThreeD("https://nekopoi.care/3d-hentai-hige-wo-soru-fucked-sayu-ogiwara/", proxy={"http": "http://host:port"}).getto
>>> tridi.to_json
```

### Installation
```bash
> python3 -m pip install requests bs4
```
