#!/bin/bash
#Git Scanner 
LISTS=$1

if [[ ! -f ${LISTS} ]]; then
	echo "ERROR: ${LISTS} not found"
	echo "usage: bash $0 list.txt"
	exit
fi

for SITE in $(cat $LISTS);
do
	if [[ $(curl -s -m 3 -A "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0" "${SITE}/.git/" -w %{http_code} -o /dev/null ) =~ '403' ]]; then
		echo "[+] MAYBE VULN: ${SITE}"
    fi

    if [[ $(curl --connect-timeout 3 --max-time 3 -kLs "${SITE}/.git/" ) =~ 'Index of /.git' ]]; then
		echo "[+] VULN: ${SITE}"
	else :
	fi
    
done
