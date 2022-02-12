g="\033[1;32m"
r="\033[1;31m"
b="\033[1;34m"
w="\033[0m"
o="\033[1;33m"

echo -e $w"["$g"INFO"$w"]"$b"Installing python! Please wait"$w
sleep 0.2
apt install python -y
echo -e $w"["$g"INFO"$w"]"$b"Installing lolcat and ruby! Please wait"$w
apt install ruby
gem install lolcat
sleep 0.2
echo -e $w"["$g"INFO"$w"]"$b"Installing figlet! Please wait"$w
apt install figlet
echo -e "\e[034m"  "Installing youtube-dl\n"
pip install youtube-dl
echo -e $w"["$g"INFO"$w"]"$b"Creating youtube directory! For download the videos!"$w
sleep 0.2
mkdir ~/storage/shared/Youtube
echo -e $w"["$g"INFO"$w"]"$b"Creating youtube-dl folden! Please wait!"$w
mkdir -p ~/.config/youtube-dl
mkdir ~/bin
mv termux-url-opener ~/bin/
clear
echo -e "\n"
figlet -f big 'Done!!!' | lolcat -p 1.0
echo -e "\e[032m" "Now you can share any Youtube video with Termux and you will be ask to select the quality of your downloaded video and after that, It will be automatically Downloaded"
