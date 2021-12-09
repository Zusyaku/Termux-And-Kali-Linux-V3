#!/bin/bash 

clear
banner () {
echo -e "$(tput setaf 2) \033[1m
██╗      ██████╗  ██████╗ ██╗███╗   ██╗██████╗  ██████╗ ██████╗ 
██║     ██╔═══██╗██╔════╝ ██║████╗  ██║██╔══██╗██╔═══██╗██╔══██╗
██║     ██║   ██║██║  ███╗██║██╔██╗ ██║██████╔╝██║   ██║██║  ██║
██║     ██║   ██║██║   ██║██║██║╚██╗██║██╔═══╝ ██║   ██║██║  ██║
███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║██║     ╚██████╔╝██████╔╝
╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ ╚═════╝$(tput setaf 3) 
   /─────────────────────────────────────────────────────\ 
   [=>]  Protect your accounts with strong passwords  [<=]
   [=>]      Created by: Sandesh (3xploitGuy)         [<=]
   \_____________________________________________________/        
$(tput setaf 1)             
"
}  
requirements () {
if [ $(dpkg-query -W -f='${Status}' python 2>/dev/null | grep -c "ok installed") -eq 0 ];
then
echo -e "$(tput setaf 1)Installing requirements....$(tput setaf 7)"
sudo apt-get install python;
fi
if [ $(dpkg-query -W -f='${Status}' python3 2>/dev/null | grep -c "ok installed") -eq 0 ];
then
echo -e "$(tput setaf 1)Installing requirements....$(tput setaf 7)"
sudo apt-get install python3;
fi
if [ ! -d ".add_account" ] 
then
mkdir .add_account
touch .add_account/account
echo 1 > .add_account/count
echo LOGINPOD > .add_account/password
touch .add_account/serial_no
fi
}
scan_key () { 
unset key
prompt_key="Enter Your 5'digit Encryption Key To Begin: "
while IFS= read -p "$prompt_key" -r -s -n 1 char
do
if [[ $char == $'\0' ]]
then
break
fi
prompt_key='*'
key+="$char"
done
if [[ -n ${key//[0-9]/} ]]; then
echo -e "$(tput setaf 7)\nerror: input Contains letters (integer expected)\n$(tput setaf 1)"
scan_key
fi
if [ ${#key} -gt 5 -o ${#key} -lt 5 ]; then
echo -e "$(tput setaf 7)\nerror: length of key is 5 digit's\n$(tput setaf 1)"
scan_key
fi                                                   
}
encrypter () {
clear
banner
echo -e "$(tput setaf 1)        Enter your password and get encrypt Value$(tput setaf 7)\n\n"
unset password
prompt="Enter Password > "
while IFS= read -p "$prompt" -r -s -n 1 char
do
if [[ $char == $'\0' ]]
then
break
fi
prompt='*'
password+="$char"
done
if [ ${#password} -eq 0 ]; then
echo -e "$(tput setaf 1)\n\nerror: wrong input exiting...."
echo -e "$(tput setaf 3)"
read -p "Press enter to go back..." update_enter
menu_one
else
python3 encryption.py ${key:0:1} ${key:1:1} ${key:2:1} ${key:3:1} ${key:4:1} $password
echo -e "$(tput setaf 3)"
read -p "Press enter to go back..." encrypter_enter
menu_one
fi
}
menu_one () {
clear
banner
echo -e "$(tput setaf 1)              (M) (A) (I) (N)   (M) (E) (N) (U)\n\n"
echo -e "      $(tput setaf 1)[$(tput setaf 4)1$(tput setaf 1)] $(tput setaf 2)Password Vault\n"
echo -e "      $(tput setaf 1)[$(tput setaf 4)2$(tput setaf 1)] $(tput setaf 2)Encrypter\n"
echo -e "      $(tput setaf 1)[$(tput setaf 4)3$(tput setaf 1)] $(tput setaf 2)Exit\n\n$(tput setaf 7)"
read -p "Enter option: " menu_one_option
case $menu_one_option in
  1) menu_two
    ;;
  2) encrypter
    ;;
  3) echo -e "$(tput setaf 1)\nAll safe....\n"
     exit
     ;;
  *) echo -e "$(tput setaf 1)\nPlease select correct input....\n$(tput setaf 7)"
     sleep 0.6
     banner
     menu_one
    ;;
esac
}
error_msg () {
echo -e "$(tput setaf 1)\nerror: wrong input exiting...."
echo -e "$(tput setaf 3)"
read -p "Press enter to go back..." press_enter
menu_two
}
add_acc () {
clear
banner
echo -e "$(tput setaf 1)                 A_D_D   A_C_C_O_U_N_T\n\n"
read -p "$(tput setaf 1)Account name: $(tput setaf 7)" account
echo ""
if [ ${#account} -eq 0 ]; then
error_msg
fi
read -p "$(tput setaf 1)Enter password: $(tput setaf 7)" text_pas
if [ ${#text_pas} -eq 0 ]; then
error_msg
fi
counter=`cat .add_account/count`
echo [$counter] >> .add_account/serial_no
echo $account >> .add_account/account
echo $text_pas >> .add_account/password
count=$((counter+1))
echo $count > .add_account/count
echo -e "\nAccount added successfully...."
echo -e "$(tput setaf 3)"
read -p "Press enter to go back..." add_acc_enter
banner
menu_two
}
update_passwd () {
clear
banner
echo -e "$(tput setaf 1)            S_E_L_E_C_T   A_C_C_O_U_N_T"
echo -e "$(tput setaf 1)                 (Update Password)\n\n"
echo -e "$(tput setaf 2)"
echo -e "$(tput setaf 1)No.     Account$(tput setaf 2)"
paste .add_account/serial_no .add_account/account
echo -e "$(tput setaf 7)\n" 
read -p "Enter account number: " update_number
if [[ -n ${update_number//[0-9]/} ]]; then
echo -e "$(tput setaf 7)\nerror: input Contains letters (integer expected)\n$(tput setaf 1)"
error_msg
fi
count_value1=`cat .add_account/count`
if [ ${#update_number} -eq 0 ]; then
error_msg
fi
if [ $update_number -ge $count_value1 -o $update_number == 0 ]; then
error_msg
else
echo -e "\n"
read -p "Enter new password: " update_password
if [ ${#update_password} -eq 0 ]; then
error_msg
fi
python update_password/update.py $update_number $update_password > temp2
cat temp2 > .add_account/password
rm temp2
echo -e "\nPassword updated successfully...."
echo -e "$(tput setaf 3)"
read -p "Press enter to go back..." update_enter
menu_two
fi
}
retrive_passwd () {
clear
banner
echo -e "$(tput setaf 1)            S_E_L_E_C_T   A_C_C_O_U_N_T"
echo -e "$(tput setaf 1)                (Retrive Password)\n\n"
echo -e "$(tput setaf 2)"
echo -e "$(tput setaf 1)No.     Account$(tput setaf 2)"
paste .add_account/serial_no .add_account/account
echo -e "$(tput setaf 7)\n" 
read -p "Enter account number: " retrive_number
if [[ -n ${retrive_number//[0-9]/} ]]; then
echo -e "$(tput setaf 7)\nerror: input Contains letters (integer expected)\n$(tput setaf 1)"
error_msg
fi
if [ ${#retrive_number} -eq 0 ]; then
error_msg
fi
count_value2=`cat .add_account/count`
if [ $retrive_number -ge $count_value2 -o $retrive_number == 0 ]; then
echo -e "\n$(tput setaf 1)error: wrong input exiting...."
else
python retrive_password/retrive.py $retrive_number > temp1
retrived=`cat temp1`
rm temp1
python3 encryption.py ${key:0:1} ${key:1:1} ${key:2:1} ${key:3:1} ${key:4:1} $retrived
fi
echo -e "$(tput setaf 3)"
read -p "Press enter to go back..." retrive_enter
menu_two
}
delete_account () {
clear
banner
echo -e "$(tput setaf 1)            S_E_L_E_C_T   A_C_C_O_U_N_T"
echo -e "$(tput setaf 1)                 (Delete Account)\n\n"
echo -e "$(tput setaf 2)"
echo -e "$(tput setaf 1)No.     Account$(tput setaf 2)"
paste .add_account/serial_no .add_account/account
echo -e "$(tput setaf 7)\n" 
read -p "Enter account number: " delete_number
if [[ -n ${delete_number//[0-9]/} ]]; then
echo -e "$(tput setaf 7)\nerror: input Contains letters (integer expected)\n$(tput setaf 1)"
error_msg
fi
if [ ${#delete_number} -eq 0 ]; then
error_msg
fi
count_value=`cat .add_account/count`
if [ $delete_number -ge $count_value -o $delete_number == 0 ]; then
echo -e "\n$(tput setaf 1)error: wrong input exiting...."
else
python delete_account/delete_acc.py $delete_number > temp3
cat temp3 > .add_account/account
rm temp3
python delete_account/delete_pass.py $delete_number > temp4
cat temp4 > .add_account/password
rm temp4
python delete_account/delete_serial.py > temp5
cat temp5 > .add_account/serial_no
rm temp5
counter1=`cat .add_account/count`
count1=$((counter1-1))
echo $count1 > .add_account/count
echo -e "$(tput setaf 7)\nAccount deleted successfully...."
fi
echo -e "$(tput setaf 3)"
read -p "Press enter to go back..." retrive_enter
menu_two
}
menu_two () {
clear
banner
echo -e "$(tput setaf 1)            (V) (A) (U) (L) (T)   (M) (E) (N) (U)\n\n"
echo -e "      $(tput setaf 1)[$(tput setaf 4)1$(tput setaf 1)] $(tput setaf 2)Add account and password\n"
echo -e "      $(tput setaf 1)[$(tput setaf 4)2$(tput setaf 1)] $(tput setaf 2)Update password for a account\n"
echo -e "      $(tput setaf 1)[$(tput setaf 4)3$(tput setaf 1)] $(tput setaf 2)Retrive password for a account\n"
echo -e "      $(tput setaf 1)[$(tput setaf 4)4$(tput setaf 1)] $(tput setaf 2)Delete a account\n"
echo -e "      $(tput setaf 1)[$(tput setaf 4)5$(tput setaf 1)] $(tput setaf 2)Main Menu\n\n$(tput setaf 7)"
read -p "Enter option: " menu_two_option
case $menu_two_option in
  1) add_acc
    ;;
  2) update_passwd 
    ;;
  3) retrive_passwd
    ;;
  4)delete_account
    ;;
  5) banner
     menu_one
    ;;
  *) echo -e "$(tput setaf 1)\nPlease select correct input....\n$(tput setaf 7)"
     sleep 0.6
     menu_two
    ;;
esac
}
requirements
banner
scan_key
menu_one
