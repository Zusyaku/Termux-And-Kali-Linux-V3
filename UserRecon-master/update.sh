#!/bin/bash
# Update Script for UserRecon v2.1-Stable
# Script created by @AbirHasan2005


dependencies() {

command -v git > /dev/null 2>&1 || { echo >&2 "Package GIT is not installed ... Unable to update ..."; exit 1; }

}

script() {

clear
printf "\n \e[1;92mUpdating \e[1;94mUserRecon\e[1;92m ...\n\n"
sleep 1.5
cd ..
rm -rf UserRecon
git clone https://github.com/AbirHasan2005/UserRecon
cd UserRecon
chmod +x userrecon.sh
printf "\n\e[1;92mRestarting ...\n\e[0m"
bash userrecon.sh
cd ..

}

dependencies
script

