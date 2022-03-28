<h1 align="center">CiberSec Discord Bot - Discord Hack Week 2019</h1>

![alt text](https://github.com/WodxTV/CiberSec/blob/master/resources/CyberSec-logo-transparent.png)
*Logo designed and made by WodX - Made in panic.*

**CiberSec** is a simple bot that is mainly focused on cyber security. The bot works like a command shell - You simply type in a Linux shell command, and the bot will return the output from the executed command.

If I had more time, I'd develop something more advanced than a built-in command shell for Discord servers.

# Installation
In order to clone GitHub repositories, it's necessary to install git.

**Install git via:**
```bash
$ sudo apt update
$ sudo apt install git
```

**Clone the repository via:**
```bash
$ git clone https://github.com/WodxTV/CiberSec.git
```

Python 3 has to be installed, in order to be able to run the code.

**Install Python 3.7 via:**
```bash
$ sudo apt update
$ sudo apt install python3.7
```
PIP (a package-management system) for Python 3.7 also has to be installed, in order to install the Discord API/module for Python.

**Install PIP via:**
```bash
$ sudo apt update
$ sudo apt install python3-pip
```
discord.py, which is an API/a module for bot development in Python, is needed in order to make the bot run.

**Install discord.py via:**
```bash
$ pip3 install discord
```

After installing Python 3, discord.py and PIP, create a new client bot by using [this link](https://discordapp.com/developers/applications/).

Copy the client ID of the bot you have created, and paste [this link](https://discordapp.com/oauth2/authorize?client_id=CLIENT_ID_HERE&scope=bot&permissions=8) into your browser and change 'CLIENT_ID_HERE' in the URL to your new bot's client ID, to invite it to your Discord server.

# Running the bot
I recommend you running the bot on a penetration testing Linux distribution like **Kali Linux** or **Parrot OS**, as they have a lot of pre-installed penetration testing/hacking tools installed.

1. Create two text channels named 'Terminal' and 'Command-History'

2. Edit the config in ``./config/config.json``

3. Start the bot via ``$ python3 cibersec.py``

4. Create a new role named 'CiberSec User' and assign the role to users who should be able to use the bot

# Developer
**WodX**
* Github: [WodXTV](https://github.com/wodxtv)
* Discord: [wodx#6724](https://prfl.es/profile/621044372951269417)
* Twitter: [@wodsex](https://twitter.com/wodxsex)
