#!/bin/bash
# (c) @AbirHasan2005

clear
printf "\n Running Setup for LR-YTDL ... \n"
sleep 2
cd ~
apt update && apt upgrade -y
apt install python wget dos2unix -y
pip3 install --upgrade youtube-dl
clear
printf "\n Setting Up Storage ... \n"
sleep 2
printf "\n Please Allow Storage Access! \n"
sleep 1
termux-setup-storage
printf "\n Please Wait ... \n"
mkdir ~/storage/shared/YouTube-DL
mkdir -p ~/.config/youtube-dl
mkdir ~/bin
wget https://github.com/AbirHasan2005/LR-YTDL/raw/master/youtube-dl -O ~/bin/termux-url-opener
dos2unix ~/bin/termux-url-opener
printf "\n Setup Complete, Enjoy! \n\n"
