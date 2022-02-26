#!/bin/bash
# Testing setup script by AbirHasan2005
# If you find any problem or coding mistake in this script than please report in Telegram Group: http://t.me/linux_repo
# This script could be very unstable


printf "\n\e[1;92m"
printf "Running setup ...\n"
sleep 3
printf "Must have a stable internet connection ...\n"
sleep 3
printf "Updating ...\n"
sleep 2
sudo apt-get update
sudo apt-get install -f
printf "\n\n\e[1;92m"
printf "Installing packages ...\n"
sleep 3
sudo apt-get install -y wget unzip xvfb libxi6 libgconf-2-4 python3-pip default-jdk libxss1 libappindicator1 libindicator7 google-chrome-stable
printf "\n\n\e[1;92m"
printf "Running \e[1;93mwget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb\e[1;92m command ...\n"
sleep 3
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
printf "\n\n\e[1;92m"
printf "Running \e[1;93msudo dpkg -i google-chrome*.deb\e[1;92m command ...\n"
sleep 3
sudo dpkg -i google-chrome*.deb
printf "\n\n\e[1;92m"
printf "Running \e[1;93mwget -N http://chromedriver.storage.googleapis.com/2.26/chromedriver_linux64.zip\e[1;92m command ...\n"
sleep 3
wget -N http://chromedriver.storage.googleapis.com/2.26/chromedriver_linux64.zip
printf "\n\n\e[1;92m"
printf "Unzipping chromedriver_linux64.zip ..."
sleep 2
unzip chromedriver_linux64.zip
printf "\n\n\e[1;92m"
printf "Setting up chromedriver ...\n"
sleep 3
chmod +x chromedriver
sudo mv -f chromedriver /usr/local/share/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
printf "\n\n\e[1;92m"
printf "Trying to install pyvirtualdisplay & selenium ...\n"
sleep 2
pip3 install pyvirtualdisplay selenium
pip install pyvirtualdisplay selenium
printf "\n\n\e[1;92m"
printf "Running other setups ...\n"
sleep 3
sudo curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
sudo echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
printf "\n\n\e[1;92m"
printf "Recommanded to download \e[1;95mselenium-server-standalone-3.13.0.jar\e[1;92m\nIf you not feel useful you can skip this ...\n"
read -p $'\nDo you want to download this?(y/n): \e[1;93m' input

if [[ $input == y || $input == Y ]]; then
	printf "\n\n\e[1;92m"
	printf "Downloading \e[1;95mselenium-server-standalone-3.13.0.jar\e[1;92m via wget ..."
	sleep 3
	wget https://selenium-release.storage.googleapis.com/3.13/selenium-server-standalone-3.13.0.jar
	printf "\n\n\e[1;92m"
	printf "Setup complete ...\n"
	sleep 1.8
else
	printf "\n\n\e[1;92m"
	printf "All done ...\n"
	sleep 1
	printf "Setup complete ...\n"
	sleep 1.8
fi