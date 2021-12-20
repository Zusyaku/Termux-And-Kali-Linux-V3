#!/bin/bash

tar=$1

echo -e "\e[33m[+] Fetching URL's From Target\e[0m"
curl -s "$tar" > urls-resp.log
curl -s "$tar" | grep -Eo "(http|https)://[a-zA-Z0-9./?=_%:-]*" | sort -u | grep -i "\.js\|\.svg\|\.css\|\.xml\|\.html" | tee urls.log
echo "$tar" | tee -a urls.log
echo -e "\n\e[33m[+] Please wait... While urls's validation is in process\e[0m"
while IFS= read Url; do curl "$Url" -s; done < urls.log >> urls-resp.log

echo -e "\n\e[33m[+] Executing Secretfinder Tool on Fetched URL's\e[0m"
python3 ~/tools/secretfinder/SecretFinder.py -i urls-resp.log -o cli
