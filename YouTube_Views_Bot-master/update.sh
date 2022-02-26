#!/bin/bash
# Update Script for YouTube_Views_Bot
# Script created by @AbirHasan2005


dependencies() {

command -v git > /dev/null 2>&1 || { echo >&2 "Package GIT is not installed ... Unable to update ..."; exit 1; }

}

script() {

clear
printf "\n \e[1;92mUpdating \e[1;94mYouTube_Views_Bot\e[1;92m ...\n\n"
sleep 1.5
cd ..
rm -rf YouTube_Views_Bot
git clone https://github.com/AbirHasan2005/YouTube_Views_Bot
cd YouTube_Views_Bot

}

dependencies
script
