import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import sys,os,socket

my_session = requests.Session()
my_session.headers.update({'User-Agent':'Mozilla'})
