#!/bin/bash
@import text_display/IO.ECHO util/IO.SYSTEM.var
Namespace.self: util/IO.TYPE
sys::var:(){
    local status argv
    argv="$1"
    target_argv="$2"
    local deference=${3:-true}

    if [[ $argv == "n"* ]]; then
        flag_type=$(Tulis.strN reference)
    elif [[ $argv == "a"* ]]; then
        flag_type=$(Tulis.strN array)
    elif [[ $argv == "A"* ]]; then
        flag_type=$(Tulis.strN map)
    elif [[ $argv == "i"* ]]; then
        flag_type=$(Tulis.strN integer)
    elif [[ $argv == "ai"* ]]; then
        flag_type=$(Tulis.strN integerArray)
    elif [[ $argv == "Ai"* ]]; then
        flag_type=$(Tulis.strN integerMap)
    else
        flag_type=$(Tulis.strN string)
    fi

#   eval $argv>/dev/null 2>&1

#if [[ $? == 0 ]]; then
#      s=$(eval "$argv")
#      printf ${s:-None}
#      return $?
# else
#      shift $((1+1))
#      [ -n "${argv}" ] && { return $?; }
# fi

#   argv_defined=$(declare -p $argv 2> /dev/null || true)

   local regex_array="declare -([a-zA-Z-]+) $argv='(.*)'"
   local regex="declare -([a-zA-Z-]+) $argv=\"(.*)\""
   local regex_bash4="declare -([a-zA-Z-+]) $argv=(.*)"

   local escape="'\\\'"
   local escapeQuest='\\"'
   local singleslash='\'

   argv_definitation=$(declare -p $argv 2>/dev/null || true)

   if [[ -z "$argv_definitation" ]]; then printf "\e[91m➥\e[00;97m Variable not defined\e[00m"; return 2; fi
   
   if [[ "$argv_definitation" =~ $regex_array ]]; then
         deklarasi="${BASH_REMATCH[2]//$escape/}"
                                                                                       # semuanya: apakah transformasi ini di butuhkan ?
   elif [[ "$argv_definitation" =~ $regex ]]; then
        deklarasi="${BASH_REMATCH[2]//$escape/}"
        deklarasi="${deklarasi//$escapeQuest/$singleslash}"
        deklarasi="${deklarasi//$escapeQuest/$sintleslash}"
   elif [[ "$argv_definitation" =~ $regex_bash4 ]]; then
        deklarasi="${BASH_REMATCH[2]}"
   fi

       if [[ -z "$deklarasi" ]]; then
           printf "\e[91m➥\e[00;97m Variable not defined\e[00m"
           return 56
#           throw
       fi
   local variabeltype

   DEBUG "Variable is $argv = $argv_definitation ==== ${BASH_REMATCH[1]}"

   local primitType=${BASH_REMATCH[1]}
   local objektipelangsungke="$argv[__object_type]"

   if [[ "$primitType" =~ [A] && ! -z "${objektipelangsungke}" ]]; then
       DEBUG Log "Object Type $argv[__object_type] = ${!objektipelangsungke}"
       variabeltipe="${!objektipelangsungke}"
   else
        variabeltype=$(Tulis.strN ${flag_type})
        DEBUG "Variable $argv is type of $variabletype"
   fi
}

###############
# return mode #
###############

@return:(){
        local argv="$1"
        local deference="${2:-true}"

    local deklarasi
        sys::var: "$argv"
        echo "$deklarasi"
}

@return.value:(){
  local __lol_value=$@
  @return: __lol_value
}

#	__lol_dev_declare=$(declare -p $__lol__dev_value 2> /dev/null || true)
#	__get_lol_var=$(@get __lol__dev_value)
#	__get_sys_var=$(IO.get: __get_lol_var)
#	IO.get: __get_sys_var
#    local __lol_regex="declare -([a-zA-Z-]+) $__lol__dev_value=\"(.*)\""
#    local __lol_regex_array="declare -([a-zA-Z-]+) $__lol__dev_value='(.*)'"
#    local __lol_regex_bash4="declare -([a-zA-Z-]+) $__lol__dev_value=(.*)"
#
#    local __lol_escape="'\\\'"
#    local __lol_escapeQuest='\\"'
#    local __lol_singgleEscape='\'
#
#    if [[ "$__lol_dev_declare" =~ ${__lol_regex_array} ]]; then
#        __lol_deklarasi="${BASH_REMATCH[2]//$__lol_escape/}"

#    elif [[ "$__lol_dev_declare" =~ ${__lol_deklarasi} ]]; then
 #       __lol_deklarasi="${BASH_REMATCH[2]//$__lol_escape/}"
  #      __lol_deklarasi="${__lol_deklarasi//$__lol_escapeQuest/$__lol_singgleEscape}"
   #     __lol_deklarasi="${__lol_deklarasi//$__lol_escapeQuest/$__lol_singgleEscape}"
    #elif [[ "$__lol_dev_declare" =~ ${__lol_regex_bash4} ]]; then
     #   __lol_deklaeasi="${BASH_REMATCH[2]}"
#    fi
#}

IO.SYSTEM:CAPITAL(){
    local __lol__dev_string
    read -s -r __lol__dev_string

    [[ -z "$__lol__dev_string" ]] && begin: Tulis.strN "None"; __bash__
      while DEBUG; do
	    case $__lol__dev_string in
	                    \<*)__lol__dev_string=${__lol__dev_string#*>} ;;
	                    *\<*) Tulis.str "%s\n" "${__lol__dev_string^<*}"
	                         __lol__dev_string=${__lol__dev_string#*>} ;;
	                      *) [ -n "$__lol__dev_string" ] && Tulis.str "%s\n" "${__lol__dev_string^}"
	                         break ;;
	                   esac
	          done
}

IO.SYSTEM:UPPER(){
	local __lol__dev_string
	read -s -r __lol__dev_string

	[[ -z "$__lol__dev_string" ]] && begin: Tulis.strN "None"; __bash__
      while DEBUG; do
          case $__lol__dev_string in
               						\<*)__lol__dev_string=${__lol__dev_string#*>} ;;
               						*\<*) Tulis.str "%s\n" "${__lol__dev_string^^<*}"
               						     __lol__dev_string=${__lol__dev_string#*>} ;;
               						   *) [ -n "$__lol__dev_string" ] && Tulis.str "%s\n" "${__lol__dev_string^^}"
               						      break ;;
               						   esac
               	done
}

IO.SYSTEM:AS(){
    local __lol__dev_argument="$1"
    local __lol__dev_outagrv="$2"

    if [[ -z "${__lol__dev_argument}" ]]; then
          e="Error Name alias not found"
          return 4
     fi
}

IO.AS_to:(){
	local __lol__dev_argv_one="$1"
	local __lol__dev_argv_two="$3"

    if [[ "$2" == "to" ]]; then
        s=
      else
          Tulis.strN "$(mode.bold: kuning)[$(mode.bold: putih)$2$(mode.bold: kuning)]$(default.color) not defined"
          return 2
     fi
        shopt -s expand_aliases
        IO.SYSTEM:AS "$3" "$1"
        alias $__lol__dev_argv_two="$1"
}
shopt -s expand_aliases

alias IO.write.upper="IO.SYSTEM:UPPER"
alias IO.write.capital="IO.SYSTEM:CAPITAL"
alias IO.AS="IO.AS_to:"
