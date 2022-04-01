#!/usr/bin/bash
#FellFreeToRecode
cyan='\e[0;36m'
green='\e[0;34m'
okegreen='\033[92m'
lightgreen='\e[1;32m'
white='\e[1;37m'
red='\e[1;31m'
yellow='\e[1;33m'
BlueF='\e[1;34m'
clear
BANNERS () {
printf "${lightgreen}==============================
         Nakanosec Tools
        BugCrowd In Scope Grabber
${white}         -Nakanosec.com-${lightgreen}
==============================\n
"
}
BANNERS

OPTIONS () {
printf "${white}[${lightgreen}>${white}] ${lightgreen}USERNAME TARGET${white} (ex: https://bugcrowd.com/${lightgreen}eero${white}) :${lightgreen} "
read nama
}
OPTIONS
curl=$(curl -kls "https://bugcrowd.com/${nama}" | grep "<code>" | sed -e 's/<[^>]*>//g' > temp.txt);
printf "${white}[${lightgreen}+${white}]${lightgreen} Result${white}\n"
cat temp.txt
printf "${white}[${lightgreen}+${white}]${lightgreen} Done${white} \n"