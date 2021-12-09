<p align="left">
 <a><img title="Python" src="https://img.shields.io/badge/python-3.0-blue.svg" ></a>
 <a><img title="MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" ></a>
 </p>

# LoginPod 
### Password encrypter + manager
**Stop** using plain text passwords for your online accounts you are making your accounts more prone to a hack.</br>
LoginPod is a password encrypter and password manager written in bash with python3 as supportive backend for encrypting passwords and account password management. Like other encryption algorithm's LoginPod has it's own encryption algorithm which works based on a 5 digit encryption key which is a input from user. Using LoginPod you can encrypt your password's, to make it more strong and store it in password vault.

[Watch tutorial on youtube](https://www.youtube.com/channel/UCAdDJn4yWzQMJyKyRWne3qg)


## Why to use LoginPod and not other password managers ?
+ You don't get flexibility while using other encryption algorithms, but here based on 5 digit encryption key from 00000 to 99999 you get 100000 different encrypted output based on key you entered. 

+ It stores your passwords on your system disk instead of any server keeping you safe in case of any data breach attack.

+ All your password are stored in plain text, passwords are encrypted only at runtime and to get correct password correct 5 digit encryption key must be entered.

+ Stop using online password encrypters as you are giving your passwords to them and they might track you.

+ Really, is there any gurantee that password manager softwares will store your password at their server and never going to peek on them. Better you store them on your system disk.


## Usage
**1.** When you run the script, you are welcomed with this screen where you have to enter 5 digit encryption key on which the encryption algorithm works ranging from 00000 to 99999. For each encryption key entered the algorithm gives different output, so you have to decide a 5 digit encryption key and always use that same encryption key.

<img src="https://user-images.githubusercontent.com/46316908/136668904-d49d80f3-6f80-40a8-8f32-cc0ad7dfbfb6.png" width="100%"></img>

**2.** After entering the encryption key user is welcomed with the main menu, where he can encrypt his passwords and if user wants to store the password for different accounts the password vault can be used.</br>

<img src="https://user-images.githubusercontent.com/46316908/136668907-13b8f6d5-4e69-4bad-a59a-eee2732286e8.png" width="100%"></img>

**3.** Selecting the second option (encrypter) where user can enter his password and get the encrypted value.</br>

<img src="https://user-images.githubusercontent.com/46316908/136668906-27a966f4-e14f-4a7b-a754-e6f8effa1754.png" width="100%"></img>

**4.** Selecting the first option (password vault) will take user to the vault menu, where user can add account name and password, update, retrive saved account passwords and delete an saved account.

<img src="https://user-images.githubusercontent.com/46316908/136668909-8fc4d406-e76e-42be-861c-6a904d9f2d34.png" width="100%"></img>

**5.** Saving account and password: user can save the account and password (passwords are stored in plain text).

<img src="https://user-images.githubusercontent.com/46316908/136668910-8b190d48-3801-4a36-bef6-1c0e3a60a5d4.png" width="100%"></img>

**6.** Retrive password: Added accounts passsword can be retrived.

<img src="https://user-images.githubusercontent.com/46316908/136668912-5ec531db-f4b8-4848-90d3-261e5bbe4363.png" width="100%"></img>


## Installing and requirements
- Python
- Pyhton3
- Linux or Unix-based system

### Installing
```
~ ❯❯❯ git clone https://github.com/3xploitGuy/loginpod.git

~ ❯❯❯ cd loginpod

~/loginpod ❯❯❯ chmod +x loginpod.sh

~/loginpod ❯❯❯ ./loginpod.sh
```


## Contact
[Gmail](mailto:sandeshyadavm46@gmail.com) </br>
[Instagram](https://instagram.com/1n_only_sandy) </br>
[Blog](https://virtualprivacy.blogspot.com) </br>
[Website](https://sandeshyadav.000webhostapp.com) </br>
[YouTube](https://www.youtube.com/channel/UCAdDJn4yWzQMJyKyRWne3qg)


## License

This work by [3xplotGuy](https://github.com/3xploitGuy) is licensed under the terms of the [MIT License](https://www.tldrlegal.com/l/mit).
