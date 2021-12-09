#!/bin/bash

function check(){

if [[ -f "email.conf" ]]; then
	printf "└─[ ✔ ] Email.conf\n";
else
	printf "└─[ ✖ ] Email.conf Failed\n";
	clear
	sleep 1
	printf "└─[ ! ] Please Try with Delete your config and save from error :_) \n";
	sleep 2
	menu
fi

if [[ -f "pass.conf" ]]; then
	printf "└─[ ✔ ] Pass.conf\n";
else
	printf "└─[ ✖ ] Pass.conf Failed\n";
	clear
	sleep 1
	printf "└─[ ! ] Please Try with Delete your config and save from error :_) \n";
	sleep 2
	menu
fi

if [[ -f "hosts.conf" ]]; then
	printf "└─[ ✔ ] Hosts.conf\n";
else
	printf "└─[ ✖ ] Hosts.conf Failed\n";
	clear
	sleep 1
	printf "└─[ ! ] Please Try with Delete your config and save from error :_) \n";
	sleep 2
	menu
fi

if [[ -f "ports.conf" ]]; then
	printf "└─[ ✔ ] Ports.conf\n";
else
	printf "└─[ ✖ ] Ports.conf Failed\n";
	clear
	sleep 1
	printf "└─[ ! ] Please Try with Delete your config and save from error :_) \n";
	sleep 2
	menu
fi	

}

function menu(){

printf "└─Do you want to delete your old config files ( y / n ): ";
read -p ">>>>>> " ans

if [[ $ans == *'Y'* ]] || [[ $ans == *'y'* ]]; then
	rm -f email.conf pass.conf hosts.conf ports.conf
	bash config.sh

else
	check
	python3 filechecker.py
	
fi

}

menu
