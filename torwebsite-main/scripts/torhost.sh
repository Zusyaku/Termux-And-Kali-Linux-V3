#!/bin/sh

Green="\e[0;92m"
White="\e[0;97m"
Normal="\e[0m"

alias torhost="echo -e \"${Green}TorHost:${White} `cat /var/lib/tor/hidden_service/hostname`${Normal}\""

torhost
