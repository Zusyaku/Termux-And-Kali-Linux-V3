#!/bin/bash

ll_ij="\e[92m"
ll_bi="\e[94m"
ll_me="\e[91m"
ll_ku="\e[94m"
ll_cy="\e[96m"
ll_st="\e[00m"
sys::@file(){
	local __ll__str_arg="$(pwd)/lib/$1"

#    local patch__ll__=$( cd "$(pwd)/${BASH_SOURCE[0]%/*}" )

#	if [[ ! -f "${__ll__str_arg}" ]]; then
#	   echo "[**] Sepertinya tidak ada module $1"
#	   exit 1
#	 fi
   for file in $(echo "$__ll__str_arg" | sed -e 's/.sh/''/g'); do
     if [[ ! -f "${file}.sh" ]]; then
        echo "[**] Sepertinya tidak ada module $@"
        exit 2
    fi
       file=$(echo "${file}.sh")
#	 source "$file" "$@">/dev/null 2>&1 || {
#	 	echo -e "[**] Error\n\t<Source Not found>\n\t<Source no indetifikasi>\n[ErrorSource]> sepertinya library tidak cocok dengan bash"
##	 	exit 44
#	 }
	 builtin source "$file" "$@"
  done
	 __ll__str_arg=(${__ll__str_arg})
}

shopt -s expand_aliases
#trap "Exception::err;echo;echo;/data/data/com.termux/files/usr/libexec/termux/command-not-found \"$1\"" ERR

#if [[ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]]; then
@system::require(){
	local file_patch="$1"

	if [[ -d "$file_patch" ]]; then
	    if [[ ${reloading} != true ]] && [[ ! -z "${file_patch}" ]] && builtin source "$file_patch" || { echo "Nothing"; exit 5; }; then
	       return 2
	    fi
	  else
	      source $(pwd)/${file_patch}
	   fi
}
#fi

system::import(){
	for libPatch in "$@"; do
	   sys::@file "$libPatch"
	done
    	
}

system::handle(){
	local handlePatch
	for handlePatch in "$@"; do
	    sys::@file "$handlePatch"
	done
}

throw(){ eval 'echo "EXCEPTION: $e ($*)" 1>&2; read -s'; }

Namespace.self:(){ :; }
alias Bash.import:="system::import"
alias @require="reloading=true @system::require"
alias begin:="{"
alias __bash__="};"
alias DEBUG=": #"
alias DEBUG=": "
alias @import="system::handle"
