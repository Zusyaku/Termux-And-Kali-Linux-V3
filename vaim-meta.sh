
#!/bin/bash

col='\e[1;77m'

red='\033[1;31m'
blue='\033[0;34m'
end='\e[0m'

android_term() {
clear
apt update
apt upgrade
pkg install php
pkg install curl
pkg install wget
apt install unstable-repo
apt install metasploit
clear

}

computer(){
clear
sudo curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && \
sudo chmod 755 msfinstall && \
sudo ./msfinstall

}

menu() {
clear


printf "\n"
printf "$blue        ██╗   ██╗ █████╗ ██╗███╗   ███╗██████╗ ██╗███████╗██████╗       \n"
printf "$blue        ██║   ██║██╔══██╗██║████╗ ████║██╔══██╗██║██╔════╝██╔══██╗      \n"
printf "$blue        ██║   ██║███████║██║██╔████╔██║██████╔╝██║█████╗  ██████╔╝      \n"
printf "$blue        ╚██╗ ██╔╝██╔══██║██║██║╚██╔╝██║██╔═══╝ ██║██╔══╝  ██╔══██╗      \n"
printf "$blue         ╚████╔╝ ██║  ██║██║██║ ╚═╝ ██║██║     ██║███████╗██║  ██║      \n"
printf "$blue          ╚═══╝  ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝      \n"
printf "\e[0m \n"




printf "\033[1;32m$col 1.) INSTALL METASPLOIT $end \n"
printf "\033[1;32m$col 2.) EXIT $end \n"
echo " "
read -p '>>> SELECT ANYONE >>> ' pack

if [ "$pack" -eq "1" ];
then
	clear
        printf "\033[1;32m$col [+] ANDROID $end \n "
        printf "\033[1;32m$col[+] COMPUTER $end \n "
        printf "\n"
	read -p '>>> SELECT OPTION ( ANDROID / COMPUTER ) >>> ' op
        
        if [[ "$op" -eq "android" || "$op" -eq "Android" || "$op" -eq "ANDROID" ]];
        then
                cd
                android_term
		clear
		printf "OKAY !!! YOUR METASPLOIT INSTALLATED SUCESSFULLY SO PUT COMMAND 'msfconsole' FOR USING \n"
		printf "\n"
        elif [[ "$op" -eq "computer" || "$op" -eq "Computer" || "$op" -eq "COMPUTER" ]];
        then
                cd
                computer
		clear
		printf "OKAY !!! YOUR METASPLOIT INSTALLATED SUCESSFULLY SO PUT COMMAND 'msfconsole' FOR USING \n"
		printf "\n "
        else
                menu
        fi

elif [ "$pack" -eq "2" ];then
        clear
        exit
        exit
        exit
        exit
fi

}

menu


