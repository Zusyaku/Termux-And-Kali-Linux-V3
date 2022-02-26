#!/bin/bash
# This is in development. I'm working on it.
# Github: https://github.com/AbirHasan2005/PowerLevel10K

# ------------------------------------------------------------------------------------------

# Please give me credits if you use any codes from here.
# Templates from ohmyzsh(GitHub: https://github.com/ohmyzsh/ohmyzsh)
# PowerLevel10K ZSH theme from romkatv(GitHub: https://github.com/romkatv/powerlevel10k)

# ------------------------------------------------------------------------------------------

# This script created by @AbirHasan2005
# Telegram Group: http://t.me/linux_repo
# Don't forget to give credits.

# ------------------------------------------------------------------------------------------

# setup.sh for the users who not downloaded & setup powerlevel10k
# Script Starts
clear
printf "\n\e[1;94m   PowerLevel10K \e[1;95mv1.4-BETA\e[1;92m by \e[1;96m@AbirHasan2005\n\e[0m"
printf "\n\e[1;92mDid you setup .oh-my.zsh before?\n\n"
read -p $'\n\e[1;92m[\e[1;93m01\e[1;92m] Yes    [\e[1;93m02\e[1;92m] No    [\e[1;93m03\e[1;92m] Exit\n\n\e[1;92m[\e[0m\e[1;77m*\e[0m\e[1;92m]\e[1;93m Choose an option: \e[1;92m' optiona

if [[ $optiona == 2 || $optiona == 02 ]]; then
printf "\n\n\e[1;92mThis script will not work if you setuped powerlevel10k & oh-my-zsh before ...\n\e[0m"
sleep 5
apt update && apt upgrade -y # Update Termux
apt install nano git zsh -y # Install important packages
git clone https://github.com/ohmyzsh/ohmyzsh.git ~/.oh-my-zsh # Clone from GitHub
cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc # Copy
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/themes/powerlevel10k # Clone from GitHub
chsh -s zsh # ZSH Start
printf "\n\e[1;96mPlease Set \e[0mZSH_THEME\e[0;92m=\e[1;93m"powerlevel10k/powerlevel10k" \e[1;96min \e[1;94m~/.zshrc\e[1;96m ...\n\e[0m"
sleep 5
printf "\n\n\e[1;92mDo you want to open \e[1;94m.zshrc\e[1;92m file now for edit?\n"
read -p $'\n\e[1;92m[\e[1;93m01\e[1;92m] Yes	[\e[1;93m02\e[1;92m] No\n\n\e[1;92m[\e[0m\e[1;77m*\e[0m\e[1;92m]\e[1;93m Choose an option: \e[1;92m' option

if [[ $option == 1 || $option == 01 ]]; then
printf "\n\n\e[1;92mOpening \e[1;94m.zshrc\e[1;92m with NANO ...\e[0m\n"
sleep 3
nano .zshrc # Edit via NANO package
sleep 1
printf "\n\e[1;92mPlease Restart Termux ...\n\e[0m"
exit 1

elif [[ $option == 2 || $option == 02 ]]; then
printf "\n\n\e[1;92mOkay ...\n\e[0m"
exit 1

else # For Option
printf "\n\e[1;93m [\e[1;91m!\e[1;93m] Invalid option!\n\n\e[1;92mFor any kind of help join Telegram Group: \e[4;96mhttp://t.me/linux_repo\e[0m\n"
sleep 1
fi

elif [[ $optiona == 1 || $optiona == 01 ]]; then
printf "\n\n\e[1;92mThis script will not work if you setuped powerlevel10k before ...\n\e[0m"
sleep 5
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/themes/powerlevel10k # Clone from GitHub
printf "\n\e[1;96mPlease Set \e[0mZSH_THEME\e[0;92m=\e[1;93m"powerlevel10k/powerlevel10k" \e[1;96min \e[1;94m~/.zshrc\e[1;96m ...\n\e[0m"
sleep 5
printf "\n\n\e[1;92mDo you want to open \e[1;94m.zshrc\e[1;92m file now for edit?\n"
read -p $'\n\e[1;92m[\e[1;93m01\e[1;92m] Yes    [\e[1;93m02\e[1;92m] No\n\n\e[1;92m[\e[0m\e[1;77m*\e[0m\e[1;92m]\e[1;93m Choose an option: \e[1;92m' optionb

if [[ $optionb == 1 || $optionb == 01 ]]; then
printf "\n\n\e[1;92mOpening \e[1;94m.zshrc\e[1;92m with NANO ...\e[0m\n"
sleep 3
nano .zshrc # Edit via NANO package
sleep 1
printf "\n\e[1;92mPlease Restart Termux ...\n\e[0m"
exit 1

elif [[ $optionb == 2 || $optionb == 02 ]]; then
printf "\n\n\e[1;92mOkay ...\n\e[0m"
exit 1

else # For Optionb
printf "\n\e[1;93m [\e[1;91m!\e[1;93m] Invalid option!\n\n\e[1;92mFor any kind of help join Telegram Group: \e[4;96mhttp://t.me/linux_repo\e[0m\n"
sleep 1
fi

elif [[ $optiona == 3 || $optiona == 03 ]]; then
printf "\n\n\e[1;92mJoin Telegram Group for feedback and chat: \e[1;96mhttp://t.me/linux_repo\n\e[0m"
exit 1

else # For Optiona
printf "\n\e[1;93m [\e[1;91m!\e[1;93m] Invalid option!\n\n\e[1;92mFor any kind of help join Telegram Group: \e[4;96mhttp://t.me/linux_repo\e[0m\n"
sleep 1
fi
# Script Ends

# ------------------------------------------------------------------------------------------

# If you find any problem in this script than please report that problem in any social site from below:
# Telegram Group(Recommanded for fast respond): http://t.me/linux_repo
# Twitter: https://twitter.com/AbirHasan2005 @AbirHasan2005
# Instagram: https://instagram.com/AbirHasan2005 @AbirHasan2005
