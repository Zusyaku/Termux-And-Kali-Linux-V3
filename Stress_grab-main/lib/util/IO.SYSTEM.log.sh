#!/bin/bash

Bash.import: text_display/IO.ECHO
Bash.import: util/IO.TYPE util/IO.SYSTEM.var
Bash.import: util/IO.FUNC

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
	var __lol__get_msg : "$@"
	global: err = "$(mode.bold: kuning)[$(mode.bold: merah)Error$(mode.bold: kuning)]$(default.color)"

	Tulis.strN "${err} ${__lol__get_msg}"
}

system.info.stdout(){
	global: varname = "$@"
	global: info = "$(mode.bold: kuning)[$(mode.bold: hijau)INFO$(mode.bold: kuning)]$(default.color)"

	Tulis.strN "$info ${varname}"
}

IO.AS "IO.LOG.Namescope" to "Namespace.self:"
IO.AS "SYSTEM.sleep" to "time.sleep:"
IO.AS "sleep" to "delay:"
IO.AS "#" to "@"
IO.AS "system.error.stdout" to "println_err"
IO.AS "system.info.stdout" to "println_info"

Namespace.self: util/IO.SYSTEM.log
