#!system/bin/sh
pkg install root-repo -y
pkg install unstable-repo -y
pkg install x11-repo -y
pkg update && pkg upgrade -y
pkg install git python -y
termux-setup-storage -y
pip install --upgrade pip
pip install aniso8601
pip install beautifulsoup4
pip install bs4
pip install cached-property
pip install certifi
pip install charset-normalizer
pip install click
pip install greenlet
pip install html5lib
pip install idna
pip install itsdangerous
pip install Jinja2
pip install MarkupSafe
pip install msgpack
pip install pycurl
pip install pytz
pip install requests
pip install six
pip install soupsieve
pip install spark-parser
pip install urllib3
pip install webencodings
pip install Werkzeug
pip install xdis
pip install futures
clear
python braje.py
