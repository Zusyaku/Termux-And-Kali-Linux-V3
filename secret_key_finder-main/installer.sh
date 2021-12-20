#!/bin/bash

apt-get install -y curl grep python3 python3-pip git

mkdir -p ~/tools

cd ~/tools

git clone https://github.com/GerbenJavado/LinkFinder.git && cd LinkFinder && python3 setup.py install && pip3 install -r requirements.txt

cd ~/tools

git clone https://github.com/m4ll0k/SecretFinder.git secretfinder && cd secretfinder && pip3 install -r requirements.txt

