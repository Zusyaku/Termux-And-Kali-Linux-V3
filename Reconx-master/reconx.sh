#!/bin/bash
#ReconX v1.0
#Purpose- Automation Some Recon Proccess.
#Coded By- Sourav Bagh Aka-SouravSec
#Instagram: @itninja.official , @souravbaghz
#Blog- www.souravsec.com
#Website- www.cyberholic.net
#Speacial Thanks To All Those Developers Who Made Awesome Recon Tools For Us
#Copying Someone's Else Code Doesn't Make You Coder

greet="Welcome"
user=$(whoami)

#Creating an directory to store subdomainslist///
mkdir -p output
mkdir -p output/subdomains
mkdir -p output/ASN
mkdir -p output/resolver
clear

#Simple Banner///
logo(){ 
	clear
 echo -e "\e[36m
  ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗     ██╗  ██╗
  ██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║     ╚██╗██╔╝
  ██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║█████╗╚███╔╝ 
  ██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║╚════╝██╔██╗ 
  ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║     ██╔╝ ██╗
  ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝     ╚═╝  ╚═╝\e[0m\e[1m
  \e[41m[+].....:Made With 💖 For Bug Hunters Community:.....[+]\e[0m
  [+]............... Coded By Sourav Bagh .............[+]\e[0m"
}

#Exploitation Logo///
exptlogo(){
	echo -e "\e[31m
  -------------------------------------------------------------------------------------------------	
  
  ▓█████ ▒██   ██▒ ██▓███   ██▓     ▒█████   ██▓▄▄▄█████▓ ▄▄▄     ▄▄▄█████▓ ██▓ ▒█████   ███▄    █ 
  ▓█   ▀ ▒▒ █ █ ▒░▓██░  ██▒▓██▒    ▒██▒  ██▒▓██▒▓  ██▒ ▓▒▒████▄   ▓  ██▒ ▓▒▓██▒▒██▒  ██▒ ██ ▀█   █ 
  ▒███   ░░  █   ░▓██░ ██▓▒▒██░    ▒██░  ██▒▒██▒▒ ▓██░ ▒░▒██  ▀█▄ ▒ ▓██░ ▒░▒██▒▒██░  ██▒▓██  ▀█ ██▒
  ▒▓█  ▄  ░ █ █ ▒ ▒██▄█▓▒ ▒▒██░    ▒██   ██░░██░░ ▓██▓ ░ ░██▄▄▄▄██░ ▓██▓ ░ ░██░▒██   ██░▓██▒  ▐▌██▒
  ░▒████▒▒██▒ ▒██▒▒██▒ ░  ░░██████▒░ ████▓▒░░██░  ▒██▒ ░  ▓█   ▓██▒ ▒██▒ ░ ░██░░ ████▓▒░▒██░   ▓██░
  ░░ ▒░ ░▒▒ ░ ░▓ ░▒▓▒░ ░  ░░ ▒░▓  ░░ ▒░▒░▒░ ░▓    ▒ ░░    ▒▒   ▓▒█░ ▒ ░░   ░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
   ░ ░  ░░░   ░▒ ░░▒ ░     ░ ░ ▒  ░  ░ ▒ ▒░  ▒ ░    ░      ▒   ▒▒ ░   ░     ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░
     ░    ░    ░  ░░         ░ ░   ░ ░ ░ ▒   ▒ ░  ░        ░   ▒    ░       ▒ ░░ ░ ░ ▒     ░   ░ ░ 
     ░  ░ ░    ░               ░  ░    ░ ░   ░                 ░  ░         ░      ░ ░           ░ 
  -------------------------------------------------------------------------------------------------
  -------------------------------------------------------------------------------------------------   \e[0m"
}


#ASN Finder- Step-1 | Asset Finder///
assetfinder(){
  #Banner For Asset Finder///
  echo
  echo -e "  [+] \e[93m$option- Asset Discovery\e[0m "
  echo "  +-------------------------------------------------------+"

#Taking Input From User///
echo "  [ Give Only Org Name eg. tesla ]"
  read -p "  [Target Org Name:] " targetorg
  
  if [ -z "$targetorg" ];
 then
   echo -e "\e[91m[Not Given Target Org Name]\e[0m"
   echo -e " \e[91m[+] Quiting...\e[0m"
   sleep 1
   menu
 else
   echo
 fi

clear

  #Banner For ASN Finder///
  echo -e "\e[93m                                               
 _____ _____ _____    _____ _       _         
|  _  |   __|   | |  |   __|_|___ _| |___ ___ 
|     |__   | | | |  |   __| |   | . | -_|  _|
|__|__|_____|_|___|  |__|  |_|_|_|___|___|_|  
  :::.....Searching.For.ASN.Numbers.....:::                                    
\e[0m"

  #Start Amass for searching ASNs and storing into /output/orgASN.txt
  mkdir -p output/ASN
  mkdir -p output/ASN/$targetorg
  
  amass intel -org $targetorg | grep -Eo '[0-9]{1,9}' | tee output/ASN/$targetorg/ASNs.txt

  #Finding Domain from ASNs List///
   echo "[ASNs Found for $targetorg - Done]"
   echo ""
   echo "[+] ASN Lookup Is Running..."
   cat output/ASN/$targetorg/ASNs.txt | while read line || [[ -n $line ]];
 do
   amass intel -asn $line
   read -p "[+] Hit Enter to Go Back " -t 60
 done
   

}

#Subdomain Enumeration Part ///
subdomainenum(){
#Taking Input for target host///
 echo ""
 echo -e "  [+]\e[93m $option- Subdomain Finder\e[0m"
 echo "  +-------------------------------------------------------+"
 echo "  [without http:// eg. xyz.com]"
 read -p "  [Target Domain:]" host

 if [ -z "$host" ];
 then
	 echo -e "\e[91m[Not Given Target Domain]\e[0m"
         echo -e " \e[91m[+] Quiting...\e[0m"
         sleep 1
	 menu
 else
	 echo  "[+] Finding Subdomains for:$host"
 fi

 
#Starting Subfinder///
#Get it from https://github.com/projectdiscovery/subfinder
clear
logo
echo ""
echo -e "  \e[93mSubdomains By Subfinder\e[0m"
echo "+---------------------------------------------------+"
sleep 1
subfinder -d $host -o output/subdomains/$host.txt
echo "[+] Finished"


#Starting Crt.sh///
#
echo ""
echo -e "  \e[93mSubdomains By Crt.sh\e[0m"
echo "+---------------------------------------------------+"
sleep 1
curl -fsSL "https://crt.sh/?q=$host" | pup 'td :contains(".$host") text{}' | sort -n | uniq -c | sort -rn | column -t | cut -c 5- > output/subdomains/$host-1.txt
cat output/subdomains/$host-1.txt
echo "[+] Finished"


#Starting Amass Passive Enumeration///
#Get it from https://github.com/OWASP/Amass
echo ""
echo -e "  \e[93mStarting Amass\e[0m"
amass enum --passive -d $host -o output/subdomains/$host-2.txt
echo "+---------------------------------------------------+"
echo "[+] Finished  "

#Output FileList Management///
echo "[+] Sorting All The Subdomains into /output/subdomains/$host.txt"
sleep 1
cd output/subdomains
cat $host.txt $host-1.txt $host-2.txt | sort -u >$host-sorted.txt
rm -rf $host.txt $host-1.txt $host-2.txt
mv $host-sorted.txt $host.txt

#Starting Knockpy///
#Get it from https://github.com/guelfoweb/knock
echo ""
echo -e "  [+] \e[93mSubdomain By Knock\e[0m"
echo "+---------------------------------------------------+"
python src/knock/knockpy/knockpy.py $host
echo "  [+] Finished"


#Logs Output Files saved here///
echo -e "\e[34mSubdomain lists saved in /output/$host.txt\e[0m"
read -p "  [+] Hit Enter to Go Back " -t 100

}


#Resolver/////////////////////////
resolver(){
echo 
echo -e "  [+]\e[93m $option- Resolver\e[0m"
echo "  +-------------------------------------------------------+"
echo "  [+]can be found in output/subdomains/target.com.txt"
read -p "  [DomainList:] " DOMAINLIST
echo "  [+] Set to $DOMAINLIST Done. "


        if [ -z "$DOMAINLIST" ];
         then
             echo -e "  \e[91m[Domain List is required.]"
             echo -e "  [+] Quiting ...\e[0m"
             sleep 1
             menu
         else
             echo "+--------------------------------------+"
fi

echo "  [+] eg. target.txt"
read -p "  [OutputFileName:] " OUTPUT

cp $DOMAINLIST src/massdns/


./src/massdns/bin/massdns -r src/massdns/lists/resolvers.txt -o S $DOMAINLIST -w $OUTPUT


cat $OUTPUT | sed 's/A.*// ; s/CN.*// ; s/\..$//' > output/resolver/$OUTPUT

rm -rf $OUTPUT
echo
cat output/resolver/$OUTPUT

sleep 2
echo "[+] DNS Resolved in output/resolver/"

read -p "  [+] Hit Enter to Go Back " -t 100
}
# Reverse IP Lookup ///
reverseiplookup(){
	echo
	echo -e "  [+] \e[93m$option- Reverse IP Lookup\e[0m"
        echo "  +-------------------------------------------------------+"
	read -p "  [IP:] " IP

	if [ -z "$IP" ];
 then
   echo -e "  \e[91m[Not Given Target IP]\e[0m"
   echo -e "  \e[91m[+] Quiting...\e[0m"
   sleep 1
   menu
 else
   echo "+-------------------------------------------------+"
 fi
	
	curl https://api.hackertarget.com/reverseiplookup/?q=$IP
	echo ""
	    read -p "[+] Hit Enter to Continue " -t 100
}

# DNS Lookup ///
dnslookup(){
        echo
        echo -e "  [+] \e[93m$option- DNS Lookup\e[0m"
        echo "  +-------------------------------------------------------+"
	read -p "  [DNS:]" DNS

	if [ -z "$DNS" ];
 then
   echo -e "  \e[91m[Not Given Target DNS]\e[0m"
   echo -e "  \e[91m[+] Quiting...\e[0m"
   sleep 1
   menu
else 
	echo "+---------------------------------------------+"
fi

	curl http://api.hackertarget.com/dnslookup/?q=$DNS
	echo ""
	    read -p "[+] Hit Enter to Continue " -t 100

}



#EXPLOITATION_PART ///////////////////////////////////////

# SubTakeover ///
subtakeover(){
         echo "  [+] Not Added Yet"
         sleep 1
}

# Apache Struts2 RCE ///
struts2pwn(){


	echo "  [1] Vulnerability Checker"
	echo "  [2] RCE Exploiter"
	echo "  [0] Go Back"
	echo "  ============================================"
    read -p "  >>> " optionrce

    #Vulnerabily Checker///
	if [[ $optionrce = 1 || $optionrce = 01 ]]
	then
		read -p "  [URL:] " structurl
		
		if [ -z "$structurl" ];
        then
            echo -e "  \e[91m[LOL! Blank URL]\e[0m"
            echo -e "  \e[91m[+] Going Back...\e[0m"
            sleep 1
            clear
            exptlogo
            struts2pwn
        else
   	        echo
        fi

		python src/struts-pwn/struts-pwn.py --check -u $structurl
		echo ""
		read -p "[+] Hit Enter to Continue " -t 100


	elif [[ $optionrce = 2 || $optionrce = 02 ]] 
	then
		read -p "  [URL:] " structurl

		if [ -z "$structurl" ];
        then
               echo -e "  \e[91m[LOL! Blank URL]\e[0m"
               echo -e "  \e[91m[+] Going Back...\e[0m"
               sleep 1
               clear
               exptlogo
               struts2pwn
            else
   	        echo
   	    fi
        
		read -p "  [Command:] " rcecmd
		python src/struts-pwn/struts-pwn.py -u $structurl -c $rcecmd
		echo ""
		read -p "[+] Hit Enter to Continue " -t 1000
		exploitation


	elif [[ $optionrce = 0 || $optionrce = 00 ]] 
	then
		exploitation
		


	else
		echo "Invalid Option..."
		sleep 1
		clear
		exptlogo
		struts2pwn

	fi	
		
}


#Exploitation Menu //////////
exploitation(){
	clear
	exptlogo
        echo -e ""
        echo -e "  \e[31m\e[1m[1] SPF Record Checker\e[0m   - Check SPF is Missing or not. "  #SPF Missing
	echo -e "  \e[31m\e[1m[2] DNS Zone Transfer\e[0m    - Check ZoneTransfer is Possible or not "   #Zone Transfer
        echo -e "  \e[31m\e[1m[3] Subdomain Takeover\e[0m   - Check TakeOver is possible or not. "    #Subdomain Takeover Possibility
	echo -e "  \e[31m\e[1m[4] Apache Structs2 RCE\e[0m  - Exploit For Apache Structs2 RCE. "  #RCE Checker Apache
	echo -e "  \e[31m\e[1m[0] Go Back\e[0m              - Back To Main Menu. "
	read -p "  [Enter Option:] " exploitnum

	if [[ $exploitnum = 2 || $exploitnum = 02 ]]
	then
		clear
		exptlogo
		echo " [+] $exploitnum- Zone Transfer is selected."
		read -p "  [Domain:] " zonedns
        
            if [ -z "$zonedns" ];
            then
                echo -e "  \e[91m[LOL! Blank Domain]\e[0m"
                echo -e "  \e[91m[+] Going Back...\e[0m"
                sleep 1
                exploitation
            else
   	            echo
            fi

		curl https://api.hackertarget.com/zonetransfer/?q=$zonedns
		echo
		read -p "[+] Hit Enter to Go Back " -t 200
		exploitation


    elif [[ $exploitnum = 1 || $exploitnum = 01 ]]; 
    then
        clear
    	exptlogo
    	echo "  [+] $exploitnum- SPF Records Checker is selected"
    	read -p "  [Domain:] " spfdns

    		if [ -z "$spfdns" ];
            then
                echo -e "  \e[91m[LOL! Blank Domain]\e[0m"
                echo -e "  \e[91m[+] Going Back...\e[0m"
                sleep 1
                exploitation
            else
            	echo
            fi

        host -t txt $spfdns
        echo
        read -p "[+] Hit Enter to Go Back " -t 200
		exploitation


    elif [[ $exploitnum = 3 || $exploitnum = 03 ]]
        then
            clear
            exptlogo
            echo "  [+] $exploitnum- Subdomain TakeOver is selceted."
            subtakeover
            exploitation
    elif [[ $exploitnum = 4 || $exploitnum = 04 ]]
     	then
     		clear
     		exptlogo
     		echo "  [+] $exploitnum- Structs2 RCE is selected."
     		struts2pwn
     		exploitation


    elif [[ $exploitnum = 0 || $exploitnum = 00 ]]
	then
		clear
	    menu


	else
		echo "Invalid Option..."
		sleep 1
		clear
		exploitation
	
	fi		
}

# Main Menu ///
menu(){
	logo
	echo -e "  \e[1m[+] CHOOSE FROM MENU:                      Beta v1.0 [+]           "
	echo "  ========================================================"
	echo "  [1] Reverse IP Lookup    - Get Domain List of an IP."   #IP Lookup
	echo "  [2] DNS Lookup           -                              "
	echo "  [3] Asset Discovery      - Get ASNs & domains from ASNs."  #Finds ASN no.
	echo "  [4] Subdomain Finder     - Get Subdomains into Text File." #Finds Subdomain and puts into a text file
        echo "  [5] Resolver             - DNS Resolve."                    #DNS Resolver
	echo "  [8] Exploitation (beta)  - Some Vulnerability Scanners."    #Vulnerability Scanner
	echo -e "  [0] Exit                 - Exit the tool.\e[0m"
	read -p "  [Select Option] " option

	if [[ $option = 1 || $option = 01 ]]
	then
		reverseiplookup
		sleep 2
		menu

	elif [[ $option = 2 || $option = 02 ]]
	then
	    dnslookup
	    sleep 2
	    menu

	elif [[ $option = 3 || $option = 03 ]]
	then
	    assetfinder
	    sleep 2
	    menu

	elif [[ $option = 4 || $option = 04 ]]
	then
	    subdomainenum
	    sleep 2
	    menu

        elif [[ $option = 5 || $option = 05 ]]
        then
            resolver
            menu

	elif [[ $option = 8 || $option = 08 ]]
	then    
	    exploitation
	    menu


    elif [[ $option = 0 || $option = 00 ]]
	then    
	    clear
	    exit


	else
		echo "Invalid Option..."
		sleep 1
		clear
		menu
	fi	
	        	
}

#Menu for Categoriged Work///
menu



