<p align="center">
<img src="https://kusonime.com/wp-content/uploads/2017/07/cropped-KUSONIME-Funcion-192x192.png" alt="kuso-logo"/>
</p>

### Features
----------
- [x] Scrap from url
- [x] Scrap from recommendation
- [x] Search by query
----------
### Todo
----------
- [+] Search by genre
----------

### Example
```python
# Get download url
>>> from kusonime import Scrap
>>> sc = Scrap("https://kusonime.com/kawaisou-batch-sub-indo/").fetch()
>>> sc.to_json

# Not get download url
>>> from kusonime import Scrap
>>> sc = Scrap("https://kusonime.com/kawaisou-batch-sub-indo/").fetch(False)
>>> sc.to_json

# Scrap from recommendation
>>> from kusonime import Recom
>>> sc = Recom(2).fetch # get from page 2
>>> sc[0].to_json

# Search by query
>>> from kusonime import Search
>>> s = Search("maou").fetch[0]
>>> s.to_json

# Search by query (next_page)
>>> from kusonime import Search
>>> s = Search("maou").fetch
>>> r = s.next_page[0]
>>> r.to_json
```

### Installation
```bash
> python3 -m pip install -r requirements.txt
```
