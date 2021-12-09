#!/bin/bash



printf "└─: ";
printf "└─How many mail you have: ";
read -p ">>>>>>>>>>>>>>> " count

same=$count
count=$(( count-1 ))


for (( i = 0; i <= count; i++ )); do
        printf "└─Enter Mail Address: ";
        read -p ">>>>>>>>>>>> " Mail[i]
        printf "└─Enter Mail Password: ";
        read -p ">>>>>>>>>>> " Password[i]
        printf "└─Enter Mail host: ";
        read -p ">>>>>>>>>>>>>>> " host[i]
        printf "└─Enter Mail Port: ";
        read -p ">>>>>>>>>>>>>>> " Port[i]
        printf "\n";
        printf "\n";
done


for (( i = 0; i < same; i++ )); do
        echo ${Mail[i]} >> email.conf
        echo ${Password[i]} >> pass.conf
        echo ${host[i]} >> hosts.conf
        echo ${Port[i]} >> ports.conf
done

python3 Vaim-Emsg.py