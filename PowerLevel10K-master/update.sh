#!/bin/bash
# Update Script for PowerLevel10K v2.1-Stable
# Script created by @AbirHasan2005


dependencies() {

command -v git > /dev/null 2>&1 || { echo >&2 "Package GIT is not installed ... Unable to update ..."; exit 1; }

}

script() {

clear
printf "\n \e[1;92mUpdating \e[1;94mPowerLevel10K\e[1;92m ...\n\n"
sleep 1.5
cd ..
rm -rf PowerLevel10K
git clone https://github.com/AbirHasan2005/PowerLevel10K
cd PowerLevel10K
chmod +x setup.sh
printf "\n\e[1;92mRestarting ...\n\e[0m"
bash setup.sh
cd ..

}

dependencies
script

