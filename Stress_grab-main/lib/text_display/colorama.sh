#!/bin/bash

Namespace.self: text_display/colorama

mode.bold:(){
	local color=$1

	  case $color in
	            merah){ (Tulis.str "\e[1;91m") }
	                   return 0 ;;
	            hijau){ (Tulis.str "\e[1;92m") }
	                   return 0 ;;
	            kuning){ (Tulis.str "\e[1;93m") }
	                   return 0 ;;
	            biru){ (Tulis.str "\e[1;94m") }
	                  return 0 ;;
	            pink){ (Tulis.str "\e[1;95m") }
	                   return 0 ;;
	            cyan){ (Tulis.str "\e[1;96m") }
	                  return 0 ;;
	            putih){ (Tulis.str "\e[1;97m") }
	                  return 0 ;;
	            ungu){ (Tulis.str "\033[1;38;5;99m") }
	                   return 0 ;;
	            *)e="[**] Error $1 \n\tsepertinya argument tidak ada di daftar list\n\t\t[Index error] "
	              Tulis.strN "$e" ;;
	           esac
}

mode.normal:(){
      local color=$1

          case $color in
                    hitam)Tulis.str "\e[90m" ;;
                    merah){ (Tulis.str "\e[91m") }
                           return 0 ;;
                    hijau){ (Tulis.str "\e[92m") }
                           return 0 ;;
                    kuning){ (Tulis.str "\e[93m") }
                           return 0 ;;
                    biru){ (Tulis.str "\e[94m") }
                          return 0 ;;
                    pink){ (Tulis.str "\e[95m") }
                           return 0 ;;
                    cyan){ (Tulis.str "\e[96m") }
                          return 0 ;;
                    putih){ (Tulis.str "\e[97m") }
                          return 0 ;;
                    ungu){ Tulis.str "\e[38;5;99m"; }
                         return 0 ;;
                    *)e="[**] Error $1 \n\tsepertinya argument tidak ada di daftar list\n\t\t[Index error] "
                      Tulis.strN "$e" ;;
                   esac
           }

default.color(){
	Tulis.str "\e[00m"
}

shopt -s expand_aliases

alias mode::bg.merah='Tulis.str "\033[1;41m"'
alias mode::bg.hijau='Tulis.str "\033[1;42m"'
alias mode::bg.kuning='Tulis.str "\033[1;43m"'
alias mode::bg.biru='Tulis.str "\033[1;44m"'
alias mode::bg.pink='Tulis.str "\033[1;45m"'
alias mode::bg.cyan='Tulis.str "\033[1;46m"'
alias mode::bg.putih='Tulis.str "\033[1;47m"'
alias mode::bg.ungu="Tulis.str '\033[1;48;5;99m'"
alias mode::Source.bold='Tulis.str "\033[1m"'
alias mode::Source.invis='Tulis.str "\033[8m"'
alias mode::Source.dim='Tulis.str "\033[2m"'
alias mode::Source.italic='Tulis.str "\033[3m"'
alias mode::Source.bawahline='Tulis.str "\033[4m"'
alias mode::Source.invert='Tulis.str "\033[7m"'

# Counter

alias anti.bold="Tulis.str '\033[21m'"
alias anti.dim="Tulis.str '\033[22m'"
alias anti.italic="Tulis.str '\033[23m'"
alias anti.bawahline="Tulis.str '\033[24m'"
alias anti.invert="Tulis.str '\033[27m'"
alias anti.invis="Tulis.str '\033[28m'"

# bg mode merah

alias mode::bg.merah.hijau="mode::bg.merah; mode::bold hijau"
alias mode::bg.merah.merah="mode::bg.merah; mode::bold merah"
alias mode::bg.merah.kuning="mode::bg.merah; mode::bold kuning"
alias mode::bg.merah.biru="mode::bg.merah; mode::bold biru"
alias mode::bg.merah.pink="mode::bg.merah; mode::bold pink"
alias mode::bg.merah.cyan="mode::bg.merah; mode::bold cyan"
alias mode::bg.merah.putih="mode::bg.merah; mode::bold putih"

# bg mode hijau

alias mode::bg.hijau.merah="mode::bg.hijau; mode::bold merah"
alias mode::bg.hijau.hijau="mode::bg.hijau; mode::bold hijau"
alias mode::bg.hijau.kuning="mode::bg.hijau; mode::bold kuning"
alias mode::bg.hijau.biru="mode::bg.hijau; mode::bold biru"
alias mode::bg.hijau.pink="mode::bg.hijau; mode::bold pink"
alias mode::bg.hijau.cyan="mode::bg.hijau; mode::bold cyan"

: '
<comming soon>'
