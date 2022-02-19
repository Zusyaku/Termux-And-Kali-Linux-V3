#!/bin/bash

@import text_display/IO.ECHO text_display/colorama
Namespace.self: util/IO.EXCEPTION

#trap "__EXCEPTION_TYPE__=\"$_\" command_not_found_handle \$? \$BASH_COMMAND; exit" ERR
set -o errtrace #berguna untuk melacak melalui 'waktu perintah' dan fungsi lain nya
unset -f throw 2>/dev/null || true
alias throw="__EXCEPTION_TYPE__=${e:-di_panggil_secara manual} command_not_found_handle \$1"
Exception::key::sys(){
    echo -e "
[**] Signal sigint triger

           ${ll_me}<${ll_st}Keyboard exit${ll_me}>
           <${ll_st}keyboard Signal SIGINT${ll_me}>
           <${ll_st}Keyboard SIGNAL INT${ll_me}>${ll_st}

[KeyboardSignal]"
  exit $?
}

except::sys(){
	return 1
}
Exception::err(){
        echo -e "${ll_bi}[${ll_me}/${ll_me}/${ll_bi}]${ll_st} ErrorSyntax\n\n\t${ll_me}➥\e[00m ErrorLine ${ll_me}:${ll_st} ${exception[0]}\n\t${ll_ku}➥${ll_st} ${ll_cy}Source    ${ll_me}:${ll_st} ${source}\n\t${ll_ij}➥${ll_st} ErrorSyntax${ll_ij}[${ll_me}${Lineno}${ll_ij}]\n\t${ll_cy}➥${ll_st} ${ll_me}<${ll_st}Error_syntax${ll_me}>\n\t${ll_me}➥${ll_st} \e[91m[\e[97mTidak terkecuali pengencualian\e[91m]\e[92m> \e[00m${type}\n\t🔎 $(mode.normal: hitam)[]$(default.color) $(mode.bold: kuning)[$(mode.bold: putih)${0#*[\/]}$(mode.bold: merah):$(mode.bold: putih)${exception[0]}$(mode.bold: kuning)]\n\t$(mode.bold: ungu)➥$(mode.bold: cyan) Error code ($(mode.bold: putih)${exit_code}$(mode.bold: cyan))$(default.color)"
}
trap "Exception::key::sys" INT SIGINT
#trap "Exception::err;echo;echo;/data/data/com.termux/files/usr/libexec/termux/command-not-found \"$1\"" ERR
        command_not_found_handle(){
             # gunakan jika default tidak berubah
             local IFS=$' \t\n'

             error_=$1
             # abaikan kesalahn dari subkulit itu sendiri 
             if [[ "$*" = '( set -'*'; true)' ]]; then
                  return 0
              fi

             
              except::sys "$@" && return $? || true

             local exit_code=${1}
             local exit_code=$(echo "$exit_code")
             shift || true
             local lineno="${BASH_LINENO[0]}"
             local source="${BASH_SOURCE[1]}"
             local unfined="$*"
             local type=${__EXCEPTION_TYPE__:-"UNDIFINED_command"}
             if [[ "$unfined" == "("*")" ]]; then
                    type="Subkulit mengembalikan nilai bukan nol"
             fi

             if [[ -z "$unfined" ]]; then
                  unfined="$type"
              fi

             local -a exception=( "$lineno" "$unfined" "$source" )

             local -i Lineno=${exception[0]}
             
             local errline=$(sed "${lineno}q;d" "$source")
             local defaulterr_line="$errline"

             local -i linesTread=0

             while [[ $linesTread -lt 5 && $Lineno -gt 0 ]]; do
                    linesTread+=1
                    errline="$(sed "${Lineno}q;d" "$source" | tr -d '            \t')"
              done

            [[ -z "$errline" ]] && errline=${unfined}
             Exception::err
            echo -e "\e[91m=============================================================================================\e[00m"
            Tulis.strN "$(mode.normal: hitam)[] $(mode.bold: merah)${unfined}$(mode.bold: putih) : $(mode.bold: kuning)[$(mode.bold: hijau)${0#*[\/]}$(mode.bold: merah):$(mode.bold: putih)${exception[0]}$(mode.bold: kuning)] $(mode.bold: cyan)- $(mode.bold: biru)[$(mode.bold: putih)${errline}$(mode.bold: biru)]$(default.color) Exits_code$(mode.bold: kuning)[$(mode.bold: putih)${0#*[\/]}$(mode.bold: merah):$(mode.bold: putih)$?$(mode.bold: kuning)]$(default.color)"
            echo
                #/data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
             read -p "💲press Enter "
             echo "🌀 Continue..."
             echo
        }
