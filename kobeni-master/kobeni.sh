#!/bin/bash
# Bash Menu Script Example
cat << "EOF"

  _   _       _                                   
 | \ | |     | |                                  
 |  \| | __ _| | ____ _ _ __   ___  ___  ___  ___ 
 | . ` |/ _` | |/ / _` | '_ \ / _ \/ __|/ _ \/ __|
 | |\  | (_| |   < (_| | | | | (_) \__ \  __/ (__ 
 |_| \_|\__,_|_|\_\__,_|_| |_|\___/|___/\___|\___|
             source code exposed scanner                
    nakanosec.com - zerobyte.id - zerostore.org
              Adelittle - MD15 - Dinar                                  
                                                  
EOF
PS3='Please enter your choice: '
options=("Git Scan" "Bazaar Scan" "Mercury Scan" "Svn Scan" "Quit")
select opt in "${options[@]}"
do
    case $opt in
        "Git Scan")
printf "\n[>] Target List                   : "
read targetmu
	for targetna in $(cat $targetmu); do
	if [[ $(curl -s -m 3 -A "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0" "${targetna}/.git/" -w %{http_code} -o /dev/null ) =~ '403' ]]; then
		echo "[+] MAYBE VULN: ${targetna}"
    fi

    if [[ $(curl --connect-timeout 3 --max-time 3 -kLs "${targetna}/.git/" ) =~ 'Index of' ]]; then
		echo "[+] VULN: ${targetna}"
	else :
	fi
done
            ;;
        "Bazaar Scan")
printf "\n[>] Target List                   : "
read targetmu
	for targetna in $(cat $targetmu); do
	if [[ $(curl -s -m 3 -A "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0" "${targetna}/.bzr/" -w %{http_code} -o /dev/null ) =~ '403' ]]; then
		echo "[+] MAYBE VULN: ${targetna}"
    fi

    if [[ $(curl --connect-timeout 3 --max-time 3 -kLs "${targetna}/.bzr/" ) =~ 'Index of' ]]; then
		echo "[+] VULN: ${targetna}"
	else :
fi
done
            ;;
        "Mercury Scan")
printf "\n[>] Target List                   : "
read targetmu
	for targetna in $(cat $targetmu); do
	if [[ $(curl -s -m 3 -A "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0" "${targetna}/.hg/hgrc/" -w %{http_code} -o /dev/null ) =~ '403' ]]; then
		echo "[+] MAYBE VULN: ${targetna}"
    fi

    if [[ $(curl --connect-timeout 3 --max-time 3 -kLs "${targetna}/.hg/hgrc/" ) =~ '[paths]' ]]; then
		echo "[+] VULN: ${targetna}"
	else :
fi
done

            ;;
        "Svn Scan")
printf "\n[>] Target List                   : "
read targetmu
	for targetna in $(cat $targetmu); do
	if [[ $(curl -s -m 3 -A "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0" "${targetna}/.svn/" -w %{http_code} -o /dev/null ) =~ '403' ]]; then
		echo "[+] MAYBE VULN: ${targetna}"
    fi

    if [[ $(curl --connect-timeout 3 --max-time 3 -kLs "${targetna}/.svn/" ) =~ 'Index of' ]]; then
		echo "[+] VULN: ${targetna}"
	else :
fi
done
            ;;
        "Quit")
            break
            ;;
        *) echo "invalid option $REPLY";;
    esac
done
