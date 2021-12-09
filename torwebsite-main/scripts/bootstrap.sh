#!/bin/sh

openrc default

FILE=/var/lib/tor/hidden_service/hostname
while [[ ! -f "$FILE" ]]
do 
  sleep 0.3
done

sh -l
