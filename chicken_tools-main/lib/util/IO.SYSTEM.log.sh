#!/bin/bash

Bash.import: text_display/IO.ECHO text_display/colorama

declare -Ag __lol__logscopes

IO.LOG.Namescope(){
	local scopeName="$1"
	local __source__="${BASH_SOURCE[0]}"
	__lol__logscopes["$__source__"]="$scopeName"
}

SYSTEM.sleep(){
	local times="${@}"

	while read -t ${times}; do
	   DEBUG "its, work"
	 done
}

system.error.stdout(){
	local __lol__get_msg="$@"
	declare -g err="$(mode.bold: kuning)[$(mode.bold: merah)Error$(mode.bold: kuning)]$(default.color)"

	Tulis.strN "${err} ${__lol__get_msg}"
}

system.info.stdout(){
	declare -g varname="$@"
	declare -g info="$(mode.bold: kuning)[$(mode.bold: hijau)INFO$(mode.bold: kuning)]$(default.color)"

	Tulis.strN "$info ${varname}"
}

alias Namespace.self:="IO.LOG.Namescope"
alias time.sleep:="SYSTEM.sleep"
alias delay:="sleep"
alias @="#"
alias println_err="system.error.stdout"
alias println_info="system.info.stdout"

Namespace.self: util/IO.SYSTEM.log
