#!/bin/bash

<<EOF
var depencies

cara menggunakan nya

        var name : "halo world"
atau
        var::command name = echo "halo world"
EOF

@import text_display/IO.ECHO.sh text_display/colorama
@import util/IO.SYSTEM.VAR

_b=$(mode.bold: biru)    _un=$(mode.bold: ungu)
_ij=$(mode.bold: hijau)  _pu=$(mode.bold: putih)
_me=$(mode.bold: merah)  _st=$(default.color)
_ku=$(mode.bold: kuning) _cy=$(mode.bold: cyan)

var::found(){
	__lol__var_name="$1"
	__lol__var_input="${2:-None}"

#    shift || true
   if [[ -z "$__lol__var_name" ]]; then
   Tulis.strN "Not found in ${_b}-${_me}>${_st} Variable name does not exist\n\n${_cy} ( ${_pu}Name variabel not found ${_cy} )${_st}"; e="name not found";  exit 5
   fi
}

IO.var::sys(){
	local __lol__var_name
	local __lol__var_input
    local __lol__var="$1"
    local __lol__comm="$3"

    if [[ "$2" == "=" ]]; then
         s=
      else
           Tulis.strN "ERROR on $2\n${_b}<${_cy}(${_st} command${_me} not${_st} Found ${_cy})${_b}>$(default.color)"
             exit 3
      fi
    DEBUG "if argument two is = then it will continue command to be executed and saved in variables"
      if ! (${*:3} 2>/dev/null 1>/dev/null); then
         Tulis.strN "Command not found on ${_me}${*:3}${_st}"
          exit $?
      fi

	var::found "${__lol__var}" "${__lol__comm}"
	   if [[ -z $__lol__var ]]; then
	   	Tulis.str "Command not found\n\n${_me}*$(mode.normal: hitam)Variable names should not be empty${_me}*${_st}"; exit 5;
	   fi
	     printf -v "${__lol__var}" "%s" "$(${*:3})"
}

IO.var(){
	declare -g __lol__name="$1"
	declare -g __lol__argv="$2"
	set -- ${@:3}
	declare -g __lol__input="${@}"
     var::found "${__lol__name}" "${__lol__input}"
     # Came across this looking for something else.
     # While the post looks fairly old,
     # the easiest solution in bash
     # is illustrated below (at least bash 4) using set -- ${@:#}
     # where # is the starting number of the array element we want to preserve forward

    if [[ "$__lol__argv" == ":" ]]; then
         s=y
     else
         Tulis.strN "ERROR on ${_ij}var ${_cy}$1 ${_me}${2}${_st} ${__lol__input}\n\n${_cy}( ${_pu}kesalahan ${me}$2${_cy} )${_st}"
         e="${__lol__argv} Not recognizable"
          exit 7
     fi

        [[ -z "${__lol__name}" ]] && begin: Tulis.strN "Error on ${_ij}var ${_me}! ${_b}:${_st} $2\n\n$(mode.bold)( $(default.color)Name variable not found [ nama variabel tidak di temukan ] $(mode.bold: cyan))$(default.color)"; exit 6; __bash__
        eval "${__lol__name}""=""\"${__lol__input}\""
#      return 0
}

IO::system.var.get(){
   __lol__var_argv="$1"
   local regex_array="declare -([a-zA-Z-]+) $__lol__var_argv='(.*)'"
   local regex="declare -([a-zA-Z-]+) $__lol__var_argv=\"(.*)\""
   local regex_bash4="declare -([a-zA-Z-+]) $__lol__var_argv=(.*)"

   local escape="'\\\'"
   local escapeQuest='\\"'
   local singleslash='\'

   argv_definitation=$(declare -p $__lol__var_argv 2>/dev/null || true)

   [[ -z "$argv_definitation" ]] && { printf "\e[91m➥\e[00;97m Variable not defined\e[00m"; return 2; }

   if [[ "$argv_definitation" =~ $regex_array ]]; then
         deklarasi="${BASH_REMATCH[2]//$escape/}" # semuanya: apakah transformasi ini di butuhkan ?
   elif [[ "$argv_definitation" =~ $regex ]]; then
        deklarasi="${BASH_REMATCH[2]//$escape/}"
        deklarasi="${deklarasi//$escapeQuest/$singleslash}"
        deklarasi="${deklarasi//$escapeQuest/$sintleslash}"
   elif [[ "$argv_definitation" =~ $regex_bash4 ]]; then
        deklarasi="${BASH_REMATCH[2]}"
   fi

   Tulis.str "$deklarasi"
}

shopt -s expand_aliases

alias var::command="IO.var::sys"
alias var="IO.var"
alias IO.get:="IO::system.var.get"
