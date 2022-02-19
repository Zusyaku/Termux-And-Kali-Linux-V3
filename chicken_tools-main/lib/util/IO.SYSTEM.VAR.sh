#!/bin/bash

<<EOF
var depencies

cara menggunakan nya

        var name : "halo world"
atau
        var::command name = echo "halo world"
EOF

@import text_display/IO.ECHO.sh text_display/colorama
@import util/IO.SYSTEM.VAR util/IO.SYSTEM.log

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
        printf -v "${__lol__name}" "%s" "${__lol__input}"
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

system.var.array(){
	# get all array
	local __array__="${*:3}"
	local __nama__array_="$1"
	local __options__="$2"
	
	# system 1 verifikasi penggunaan block array
	if ! (Tulis.strN "$__array__" | grep -o "{" > /dev/null 2>&1); then
		pre_element="1"
	elif ! (Tulis.strN "$__array__" | grep -o "}" > /dev/null 2>&1); then
		pre_element=$((pre_element + 1))
	else
		pre_element="ok"
	fi;
		# ambil hasil
		if [[ $pre_element == ok ]]; then
			get_valid=0
		else
			get_valid=1
		fi
	# eksekusi hasil verifikasi
	if [[ ! $get_valid == 0 ]]; then
		println_err " $(mode.bold: kuning)[$(mode.bold: putih)${BASH_LINENO[0]}$(mode.bold: merah):$(mode.bold: putih)${BASH_SOURCE[1]}$(mode.bold: kuning)]$(mode.bold: merah) !"
		println_err " $(mode.bold: kuning)[$(mode.bold: putih)${BASH_LINENO[0]}$(mode.bold: merah):$(mode.bold: putih)${BASH_SOURCE[1]}$(mode.bold: kuning)]$(mode.bold: putih) app array ${*:3}"
		println_err " $(mode.bold: kuning)[$(mode.bold: putih)${BASH_LINENO[0]}$(mode.bold: merah):$(mode.bold: putih)${BASH_SOURCE[1]}$(mode.bold: kuning)]$(mode.bold: putih) error syntax into $(mode.bold: merah)${*:3}"
		println_err " $(mode.bold: kuning)[$(mode.bold: putih)${BASH_LINENO[0]}$(mode.bold: merah):$(mode.bold: putih)${BASH_SOURCE[1]}$(mode.bold: kuning)]$(mode.bold: putih) block array not found"
		println_err " $(mode.bold: kuning)[$(mode.bold: putih)${BASH_LINENO[0]}$(mode.bold: merah):$(mode.bold: putih)${BASH_SOURCE[1]}$(mode.bold: kuning)]$(mode.bold: putih) how to use $(mode.bold: hijau) var::array: $(mode.bold: cyan){$(mode.bold: putih) halo foo bar $(mode.bold: cyan) }$(default.color)"
	fi;
		app_array_=$(Tulis.str "$__array__" | sed -e 's/[{}]/''/g') # menghapus block array
		if [[ -z "$app_array_" || ${#app_array_} == 0 ]]; then
			lvalue=None
		else
			lvalue=$(echo -n "$app_array_")
		fi;

		if [[ -z "$__nama__array_" ]]; then
			uname_array="array"
		else
			uname_array="$__nama__array_"
		fi

		if [[ ! "$__options__" == "=" ]]; then
			println_err " $(mode.bold: kuning)[$(mode.bold: putih)${BASH_LINENO[0]}$(mode.bold: merah):$(mode.bold: putih)${BASH_SOURCE[1]}$(mode.bold: kuning)]$(mode.bold: merah) !"
	        println_err " $(mode.bold: kuning)[$(mode.bold: putih)${BASH_LINENO[0]}$(mode.bold: merah):$(mode.bold: putih)${BASH_SOURCE[1]}$(mode.bold: kuning)]$(mode.bold: putih) app array ${2}"
        	println_err " $(mode.bold: kuning)[$(mode.bold: putih)${BASH_LINENO[0]}$(mode.bold: merah):$(mode.bold: putih)${BASH_SOURCE[1]}$(mode.bold: kuning)]$(mode.bold: putih) error syntax into $(mode.bold: merah)${2}"
            println_err " $(mode.bold: kuning)[$(mode.bold: putih)${BASH_LINENO[0]}$(mode.bold: merah):$(mode.bold: putih)${BASH_SOURCE[1]}$(mode.bold: kuning)]$(mode.bold: putih) block array not found"
	        println_err " $(mode.bold: kuning)[$(mode.bold: putih)${BASH_LINENO[0]}$(mode.bold: merah):$(mode.bold: putih)${BASH_SOURCE[1]}$(mode.bold: kuning)]$(mode.bold: putih) how to use $(mode.bold: hijau) var::array: $(mode.bold: kuning)loop $(mode.bold: biru)= $(mode.bold: cyan){$(mode.bold: putih) halo foo bar $(mode.bold: cyan) }$(default.color)"
		else
			get_array_elips=" $lvalue "
			IFS=$'\n' GLOBERIGNORE="*" eval "$uname_array=($get_array_elips)" # mengubah isi dari variabel app_array ke array
		fi
}

shopt -s expand_aliases

alias var::command="IO.var::sys"
alias var="IO.var"
alias io.get="IO::system.var.get"
alias var::array:="system.var.array"
