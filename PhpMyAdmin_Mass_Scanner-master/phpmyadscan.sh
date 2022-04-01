#!/bin/bash
#phpMyAdmin Mass Scanner By Adelittle
LISTS=$1

if [[ ! -f ${LISTS} ]]; then
	echo "ERROR: ${LISTS} not found"
	echo "usage: bash $0 list.txt"
	exit
fi

for SITE in $(cat $LISTS);
do
	if [[ $(curl --connect-timeout 3 --max-time 3 -kLs "${SITE}/phpMyAdmin/" ) =~ 'pma_username' ]]; then
		echo "[+] VULN: ${SITE}"
	else
		echo "NOT VULN: ${SITE} not vuln"
	fi
done
