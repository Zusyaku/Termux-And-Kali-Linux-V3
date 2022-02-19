@import text_display/IO.ECHO text_display/colorama
@import util/IO.FUNC util/IO.TYPE util/IO.SYSTEM.var util/IO.SYSTEM.log

system.get.all(){
	var url : "${@}"
	
	var __parse__ : ${url#*//}
	var __parse__ : ${url#*@}
	var __parse__ : ${url#*//}

	var __lol__get_user : ${__parse__%@*}
	var __lol__get_host : ${__parse__%%/*}; [[ ${__parse__} == *":"* ]] && var host : ${host%:*}
	var __lol__get_path : ${__parse__#*/}
	var __lol__get_proto : ${url%:*}
	[[ ${__parse__#://} == *":"* ]] && var __parse__ : ${__parse__##*:} && var __lol__get_port : ${__parse__%%/*}
	
}

system.url.select(){
	read -s _url
	global: _opsi = "$1"
	global: _select = "${@:2}"

	if [[ -z "$_url" ]]; then
		_url=""
	fi

	system.get.all ${_url}

	if [[ $_opsi == to ]]; then
		 __lol__mode="get"
	else
		println_err " urlparser% $(mode.bold: merah)${1}$(mode.bold: kuning) ${*:2}$(mode.bold: kuning) [$(mode.bold: putih)${BASH_SOURCE[1]}$(mode.bold: merah):$(mode.bold: putih)${BASH_LINENO[0]}$(mode.bold: kuning)]$(default.color) Command Not Found into $(mode.bold: merah)$1$(default.color)"
		exit 2
	fi

	if [[ $_select == protocol ]]; then
		Tulis.strN "$_url" | sed "s;$_url;$__lol__get_proto;g"
	elif [[ $_select == hostname ]]; then
		Tulis.strN "$_url" | sed "s;$_url;$__lol__get_host;g"
	elif [[ $_select == user ]]; then
		Tulis.strN "$_url" | sed "s;$_url;$__lol__get_user;g"
	elif [[ $_select == path ]]; then
		Tulis.strN "$_url" | sed "s;$_url;$__lol__get_path;g"
	elif [[ $_select == port ]]; then
		Tulis.strN "$_url" | sed "s;$_url;$__lol__get_port;g"
	else
		Tulis.strN "$_url" | sed "s;$_url;None;g"
	fi
}

system.urlencode() {
    # echo <string> | urlencode
    read urlstring
    local length="${#urlstring}"
    for (( i = 0; i < length; i++ )); do
        local c="${1:i:1}"
        case $c in
            [a-zA-Z0-9.~_-]) printf "$c" ;;
            *) printf '%%%02X' "'$c" ;;
        esac
    done
}
 
system.urldecode() {
    # echo <string> | urldecode
 	read stringurl
    local url_encoded="${stringurl//+/ }"
    if [[ -z "$stringurl" ]]; then
    	Tulis.strN "$stringurl" | sed 's;$stringurl;None;g'
    else
    	Tulis.str '%b' "${url_encoded//%/\\x}"
    fi
}

IO.AS "system.url.select" to "urlparser%"
IO.AS "system.urldecode" to "urldecode"
IO.AS "system.urlencode" to "urlencode"
