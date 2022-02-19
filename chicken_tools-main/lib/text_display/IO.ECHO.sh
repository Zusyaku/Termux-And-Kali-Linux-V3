#!/bin/bash

sys::valid(){
    if type -a echo>/dev/null 2>&1; then
         return 0
      else
          return 1
    fi
 }

Keyboard::Exit(){
	local status=$?
	
echo "
[**] Error
         <Keyboard stoped>
         <Keyboard Signal Sigint>
         <Keyboadd INT>
         
[Keyboard Exit]
"
exit 1
}

shopt -s expand_aliases

Tulis.strN(){
	{
		printf "${@}"
		echo
	}
};

Tulis.str(){
	{
		printf "$@"
	}
};

Tulis.length(){
	local jumlah=$(echo "$@" | awk '{print length}')
	echo $((jumlah-1+1))
}

#trap "Keyboard::Exit" INT SIGINT
