#!/bin/bash
# Please do not copy any codes from here without giving me proper credits
# This is my hard work
# By @AbirHasan2005
# Github: https://github.com/AbirHasan2005/CoronaStats

# This tool executes some page links via CURL



# Main Help from Website:

# Use curl package on Linux or Termux to get this.

# Source 1 stats - updated once a day from John Hopkins University
# https://corona-stats.online

# ---------------------------------------------------------------------------------

# (DEFAULT SOURCE)
# Source 2 stats - updated every 15 minutes from worldometers.info
# https://corona-stats.online?source=2

# ---------------------------------------------------------------------------------

# Country wise stats

## Format:
# https://corona-stats.online/[countryCode]
# https://corona-stats.online/[countryName]

## Example: From source 1
# https://corona-stats.online/Italy?source=1
# https://corona-stats.online/UK?source=1

## Example: From source 2 (DEFAULT)
# https://corona-stats.online/italy
# https://corona-stats.online/italy?source=2
# https://corona-stats.online/UK?source=2
# https://corona-stats.online/UK

# ---------------------------------------------------------------------------------

# State wise api (Only for US as of now)

## Format:
# https://corona-stats.online/states/[countryCode]
# https://corona-stats.online/states/[countryName]

## Example: From source 1
# https://corona-stats.online/us
# https://corona-stats.online/USA?format=json
# https://corona-stats.online/USA?minimal=true

# ---------------------------------------------------------------------------------

# Minimal Mode - remove the borders and padding from table

## Example:
# https://corona-stats.online?minimal=true
# https://corona-stats.online/Italy?minimal=true           (with country filter)
# https://corona-stats.online?minimal=true&source=1        (with source)
# https://corona-stats.online/uk?source=2&minimal=true     (with source and country)

# ---------------------------------------------------------------------------------

# Get data as JSON - Add ?format=json

## Example:
# https://corona-stats.online?format=json
# https://corona-stats.online/Italy?format=json            (with country filter)
# https://corona-stats.online/?source=2&format=json        (with source)
# https://corona-stats.online/uk?source=2&format=json      (with source and country)

# ---------------------------------------------------------------------------------

# Get top N countries - Add ?top=N

## Example:
# https://corona-stats.online?top=25
# https://corona-stats.online?source=1&top=10               (with source)
# https://corona-stats.online/uk?minimal=true&top=20        (with minimal)


# ---------------------------------------------------------------------------------

# Confirmed Cases Graph (WIP)

## Format:
# https://corona-stats.online/[countryName]/graph
# https://corona-stats.online/[countryCode]/graph

## Example:
# https://corona-stats.online/italy/graph
# https://corona-stats.online/china/graph

# Join My Telegram Group: http://t.me/linux_repo




dependencies() {

command -v curl > /dev/null 2>&1 || { echo >&2 "package CURL is not installed ... Aborting ..."; exit 1; }

}


trap 'printf "\n";partial;exit 1' 2

menu() {

printf "\n\e[0;91m>>>Please read \e[1;91mREADME.md\e[0;91m file before using this script<<<"
printf "\n\e[1;96m"
printf "\n ░█▀▀░█▀█░█▀▄░█▀█░█▀█░█▀█░█▀▀░▀█▀░█▀█░▀█▀░█▀▀"
printf "\n ░█░░░█░█░█▀▄░█░█░█░█░█▀█░▀▀█░░█░░█▀█░░█░░▀▀█"
printf "\n ░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀░▀░▀░▀░▀▀▀░░▀░░▀░▀░░▀░░▀▀▀"
printf "\e[1;95m\n	   CoronaStats \e[1;96mv2.1-Stable \e[0;92mby\e[1;94m @AbirHasan2005\n\n\e[1;92m[\e[1;93m01\e[1;92m] \e[1;93mCountry wise stats\e[0m			\e[1;92m[\e[1;93m02\e[1;92m] \e[1;93mLoad Corona-Stats Source 1 (updated once a day from John Hopkins)\n"
printf "\e[1;92m[\e[1;93m03\e[1;92m] \e[1;93mConfirmed Cases Graph (WIP)\e[0m	\e[1;92m[\e[1;93m04\e[1;92m] \e[1;93mLoad Corona-Stats Source 2 (updated every 15 minutes from worldometers.info)\n"
printf "\e[1;92m[\e[1;93m05\e[1;92m] \e[1;93mState wise api (Only for US)       \e[1;92m[\e[1;93m06\e[1;92m] \e[1;93mMinimal Mode - remove the borders and padding from table\n"
printf "\e[1;92m[\e[1;93m07\e[1;92m] \e[1;93mGet Top [Number] List		\e[1;92m[\e[1;93m08\e[1;92m] \e[1;93mContact & Social Sites\n"
printf "\e[1;92m[\e[1;93m09\e[1;92m] \e[1;93mUpdate				\e[1;92m[\e[1;93m10\e[1;92m] \e[1;93mSetup for Termux(Android)\n"
printf "\n\e[1;92m[\e[1;93m00\e[1;92m] \e[1;93mExit\e[0m"
read -p $'\n\n\e[1;92m[\e[0m\e[1;77m*\e[0m\e[1;92m]\e[1;93m Choose an option: \e[1;92m' option

if [[ $option == 1 || $option == 01 ]]; then
printf "\n\n\e[1;92mEnter your country name/code ...\nExamples: BD, UK, US, IND, JP etc. [Country Code]\n           Bangladesh, India, Italy, Japan etc. [Country Name]"
read -p $'\n\n\e[1;92m[\e[0m\e[1;77m*\e[0m\e[1;92m]\e[1;93m Enter your country name/code: \e[1;92m' optiona
printf "\n\n\e[1;92mPlease Wait ...\nShowing from source 2\e[0m\n"
sleep 5
curl https://corona-stats.online/$optiona?source=2
menu

elif [[ $option == 2 || $option == 02 ]]; then
printf "\n\e[1;92mPlease wait ...\nLoading Corona-Stats Source 1\n\e[0m"
sleep 5
curl https://corona-stats.online
menu

elif [[ $option == 3 || $option == 03 ]]; then
printf "\n\n\e[1;92mEnter your country name/code ...\nExamples: BD, UK, US, IND, JP etc. [Country Code]\n           Bangladesh, India, Italy, Japan etc. [Country Name]"
read -p $'\n\n\e[1;92m[\e[0m\e[1;77m*\e[0m\e[1;92m]\e[1;93m Enter your country name/code: \e[1;92m' optionb
printf "\n\n\e[1;92mPlease Wait ...\nShowing results ...\e[0m\n"
sleep 5
curl https://corona-stats.online/$optionb/graph
menu

elif [[ $option == 4 || $option == 04 ]]; then
printf "\n\e[1;92mPlease wait ...\nLoading Corona-Stats Source 2\n\e[0m"
sleep 5
curl https://corona-stats.online?source=2
menu

elif [[ $option == 5 || $option == 05 ]]; then
printf "\n\n\e[1;92mEnter your country name/code ...\nExamples: BD, UK, US, IND, JP etc. [Country Code]\n           Bangladesh, India, Italy, Japan etc. [Country Name]"
read -p $'\n\n\e[1;92m[\e[0m\e[1;77m*\e[0m\e[1;92m]\e[1;93m Enter your country name/code: \e[1;92m' optionc
printf "\n\n\e[1;92mPlease Wait ...\nShowing results ...\e[0m\n"
sleep 5
curl https://corona-stats.online/states/$optionc
menu

elif [[ $option == 6 || $option == 06 ]]; then
printf "\n\n\e[1;92mPlease Wait ...\nShowing results ...\e[0m\n"
sleep 5
curl https://corona-stats.online?minimal=true
menu

elif [[ $option == 7 || $option == 07 ]]; then
printf "\n\n\e[1;92mEnter any number to make top list ...\nExamples: 5, 10, 15, 17, 20. 25 etc."
read -p $'\n\n\e[1;92m[\e[0m\e[1;77m*\e[0m\e[1;92m]\e[1;93m Enter number: \e[1;92m' optiond
printf "\n\n\e[1;92mPlease Wait ...\nShowing results ...\e[0m\n"
sleep 5
curl https://corona-stats.online?top=$optiond
menu

elif [[ $option == 8 || $option == 08 ]]; then
printf "\n\n\e[0;92mGithub: \e[1;96mhttps://github.com/AbirHasan2005\n\e[0;92mInstagram: \e[1;96mhttps://instagram.com/AbirHasan2005\n\e[0;92mTwitter: \e[1;96mhttps://twitter.com/AbirHasan2005\n\e[0;92mTelegram: \e[1;96mhttp://t.me/AbirHasan2005\n\n\e[1;92mTelegram Group: \e[1;96mhttp://t.me/linux_repo\n\e[1;92mTelegram Channel: \e[1;96mhttp://t.me/teletechstore\n\n\e[1;92mBlog: \e[1;96mhttps://teletechstore.blogspot.com\n\e[0m"
menu

elif [[ $option == 9 || $option == 09 ]]; then
printf "\n\e[1;91mUpdate will delete current directory ...\nand then it will install this dircetory again from GitHub ...\n"
sleep 2
printf "\n\e[1;92mRunning \e[1;94mupdate.sh\e[1;92m script\n\e[0m"
sleep 3
bash update.sh
cd ..
cd CoronaStats

elif [[ $option == 10 ]]; then
printf "\n\e[1;92mRunning Termux Setup ...\n\e[1;92m"
sleep 2
apt install update && apt install upgrade -y
apt install curl git -y
printf "\n\e[1;92mRecommaned to rotate to Landscape mode in Mobile Phone(Horizontal Mode) to get better view ...\n\e[0m"
menu

elif [[ $option == 0 || $option == 00 ]]; then
printf "\n\e[1;92mFor any problem report, help, suggestion & chat\njoin Telegram Group: \e[1;96mhttp://t.me/linux_repo\e[0m\n"
sleep 1
printf "\n\e[0;91mExiting ...\n\e[0m"
exit 1

else
printf "\n\e[1;93m [\e[1;91m!\e[1;93m] Invalid option!\n\n\e[1;92mFor any kind of help join Telegram Group: \e[4;96mhttp://t.me/linux_repo\e[0m\n"
sleep 1

fi
}
dependencies
menu
