#!/bin/bash
#set -xe
#main.sh

if [[ ! -f "$(command -v setterm)" ]];
then
    echo "setterm tidak terinstall silakan install util-linux"
     exit 127
elif [[ ! -f "$(command -v curl)" ]];
then
    echo "curl tidak terinstall silakan install curl"
    exit 127
elif [[ ! -f "$(command -v nmap)" ]];
then
    echo "nmap tidak terinstall silakan install nmap"
     exit 127
elif [[ ! -f "$(command -v nc)" ]];
then
     echo "nc tidak terinstall silakan install nmap-ncat ncat-openbsd"
     exit 127
else
     ( sleep 0.1 )
 fi

b=$(setterm --foreground blue --bold on)    m=$(setterm --foreground magenta --bold on)
ij=$(setterm --foreground green --bold on)  cy=$(setterm --foreground cyan --bold on)
ku=$(setterm --foreground yellow --bold on) pu=$(setterm --foreground white --bold on)
me=$(setterm --foreground red --bold on)    st=$(setterm --foreground default)

################################
#       code by polygon        #
# name : track domain          #
# version : 0.1                #
################################

#### variable

bashname=$(basename $0)
dt=/data/data/com.termux/files/usr/bin/nms
date=$(date +%r)
loop=true
url="curl"


#Random agent
#UA=$($url --silent \
#          --ssl \
#          --tlsv1.3 \
#          --insecure \
#          --location \
#          --url "https://raw.githubusercontent.com/petros077/ua.txt/main/trash.txt"

key=$(echo "a2V5Y2RuLXRvb2xzOmh0dHBzOi8vdmVla3J1bS5naXRodWIuaW8K" | b${a2V5Y2RuLXRvb2xzOmh0dHBzOi8vdmVla3J1bS5naXRodWIuaW8K:-}a${a2V5Y2RuLXRvb2xzOmh0dHBzOi8vdmVla3J1bS5naXRodWIuaW8K:-}s${a2V5Y2RuLXRvb2xzOmh0dHBzOi8vdmVla3J1bS5naXRodWIuaW8K:-}e64 -d -i)
                                     									               
# mechanize
function rat(){
    $url --silent \
         --request GET \
         --location \
         --header "User-Agent: ${key}" https://tools.keycdn.com/geo.json?host={$1} | \
	sed -e 's/[{}]/''/g' | awk -v k="text" '{n=split($0,a,","); for (i=1; i<=n; i++) print a[i]}' | \
	grep 'isp\|country_name\|city\|ip\|latitude\|longitude\|region_name\|continent_name\|metro_code' | \
	sed -e 's/"/''/g' | sed -e 's/:/ : /g'

	return 0
}

function usag {
cat <<EOF

track locator | usag : retcat get <target domain>

_________________________________________________
--h, help      | bantuan
--check, lives     | cek down target website
_________________________________________________
[!] Team      : Helixs-crew & COINTER TEAM
[!] me github : https://github.com/Bayu12345677

              Code by ©Polygon

EOF
}

function valid {
	type=${1}

	   if [[ ! -f "debug.txt" ]]; then rm -rf debug.txt; else rm -rf debug.txt; fi
    debug="debug.txt"
	   get=$(nc -vz ${type} 443 2>debug.txt)
int=$(cat ${debug} | grep -o "succeeded")

    [[ s="${int}" ]]

       if [[ $int =~ 'succeeded' ]];
       then
         printf "\n%s=============%s[%s cek server %s]%s==========%s\n" $ku $m $pu $m $ku $st
         printf "\n%s[%s$(date +%r)%s] %s[%sStatus%s]%s~%s>%s %s[%s\e[0;1;41mhost is up\e[0m%s]%s\n\n" $me $ku $me $ij $ku $ij $m $me $m $st $m $st; rm -rf debug.txt
         printf "%s=============%s[%s cek server %s]%s==========%s\n\n" $ku $m $pu $m $ku $st
         return 0
       else
           printf "\n%s=============%s[%s cek server %s]%s==========%s\n" $ku $m $pu $m $ku $st
           printf "\n%s[%s$(date +%r)%s] %s[%sStatus%s]%s~%s>%s %s[%s\e[0;1;41mhost is down\e[0m%s]%s\n\n" $me $ku $me $ij $ku $ij $m $me $b $st $b $st; rm -rf debug.txt
           printf "%s=============%s[%s cek server %s]%s==========%s\n\n" $ku $m $pu $m $ku $st
           return 127
         fi
   if [[ -f "debug.txt" ]];then rm -rf debug.txt; else rm -rf debug.txt; fi
}

while true :; do

      case $1 in
                --help|-h){ ( usag ) } 
                            break ;;
                --check|-c){ ( valid $2 ) } 
                           break ;;
                get){ ( printf "==================[ result ]==================\n`rat $2`\n==================[ result ]==================" | $dt -f green ) }
                     break ;;
                     *){ ( usag ) }
                        break ;;
                esac

           done
