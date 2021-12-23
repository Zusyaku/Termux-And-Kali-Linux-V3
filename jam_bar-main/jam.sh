#!../usr/bin/bash

    # tclock - Display a clock in a terminal
: '
      Author : Bayu riski
      Team   : Helixs-crew
      github : https://github.com/Bayu12345677
'
    # beground color
    BG_BLUE="$(tput setab 4)"
    FG_BLACK="$(tput setaf 0)"
    FG_WHITE="$(tput setaf 7)"

    terminal_size() {
      
      terminal_cols="$(tput cols)"
      terminal_rows="$(tput lines)"
    }

    banner_size() {

      banner_cols=0
      banner_rows=0
      
      while read; do
        [[ ${#REPLY} -gt $banner_cols ]] && banner_cols=${#REPLY}
        ((++banner_rows))
      done < <(figlet -f slant "12:34 PM")
    }

    display_clock() {
      
      # fungsi $REPLY untuk menampilkan blasan string
      local row=$clock_row
      
      while read; do
        tput cup $row $clock_col
        echo -ne "${BL_BLUE}$REPLY"
        ((++row))
      done < <(figlet -f slant "$(date +'%I:%M %p')")
    }


    trap 'tput sgr0; tput cnorm; tput rmcup || clear; exit 0' SIGINT

    # mengatur height width display
    tput smcup; tput civis

    terminal_size
    banner_size
    clock_row=$(((terminal_rows - banner_rows) / 2))
    clock_col=$(((terminal_cols - banner_cols) / 2))
    progress_row=$((clock_row + banner_rows + 1))
    progress_col=$(((terminal_cols - 60) / 2))

   # untuk effect bayangan progress
    blank_screen=
    for ((i=0; i < (terminal_cols * terminal_rows); ++i)); do
      blank_screen="${blank_screen} "
    done

    echo -n ${BG_BLUE}${FG_WHITE} # display background
    while true; do

      
      if tput bce; then
        clear
      else
        tput home
        echo -n "$blank_screen"
      fi
      tput cup $clock_row $clock_col
      display_clock
      
      tput cup $progress_row $progress_col
       # bayangan effect
      echo -n ${FG_BLACK}
      echo -n "###########################################################"
      tput cup $progress_row $progress_col
      echo -n ${FG_WHITE}

      # logika : jadi setiap 60 detik akan menambahkan string pagar yg di atur oleh sleep
      for ((i = $(date +%S);i < 60; ++i)); do
        echo -n "#"
        sleep 1
      done
    done
