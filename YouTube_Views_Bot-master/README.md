# YouTube_Views_Bot v1.4
Increase views of your YouTube videos by this bot. Most accurate views. A bot scripted in python codes. Added [setup.sh](https://github.com/AbirHasan2005/YouTube_Views_Bot/blob/master/setup.sh) script Easy to use. Must join Telegram Group: http://t.me/linux_repo

**NOTE:** If you want to use Tor, be aware that YouTube can flag your video and delete the views after a while.

---

## Compatible with:
- Mac OS X
- Ubuntu Linux
- Debian Linux
- Arch Linux
- Kali Linux

## Important Words:
**If you want, you can install tor and privoxy. One thing, selenium does not work very well with socks proxy. Must run the setup script. Not desgined for Termux/Windows !**

### Termux & Windows users ask in [Telegram Group](http://t.me/linux_repo) for using this.

## Install Tor, git and Python3 on Mac OS X:
```sh
brew install tor
```
```sh
brew install python3
```
```sh
brew install git
```

## Install Tor, git and Python3 on Debian/Ubuntu:
```sh
sudo apt-get install tor
```
```sh
sudo apt-get install python3
```
```sh
sudo apt-get install git
```

## Install Tor, git and Python3 on ArchLinux:
```sh
sudo pacman install -Sy tor
```
```sh
sudo pacman install -Sy python3
```
```sh
sudo pacman install -Sy git
```

## Requirements:
This tool needs a Linux environment. This tool depends on python3 and uses some libraries. In order to install them, you can use `pip3` command. To update the tool I made a `update.sh` script.

- PIP packages:
	- requests
	- selenium
	- urllib3
	- colorama

- Commands to download and setup:
```sh
git clone https://github.com/AbirHasan2005/YouTube_Views_Bot
```
```sh
cd YouTube_Views_Bot
```

```sh
sudo pip3 install -r requirements.txt
```

### Optional:
Run [setup.sh](https://github.com/AbirHasan2005/YouTube_Views_Bot/blob/master/setup.sh) script to run properly.
```sh
bash setup.sh
```

## Usage:
```
python3 bot.py --help
usage: bot.py [--visits VISITS] [--url URL] [--proxy PROXY] [--enable-tor]
              [-v] [-h]

Tool to increase YouTube views

Main Arguments:
  --visits VISITS  Amount of visits per video, default: 1
  --url URL        YouTube video url
  --proxy PROXY    Set the proxy server to be used. e.g: 127.0.0.1:8080
  --enable-tor     Enable TOR support (You must have installed TOR at your
                   system)

Optional Arguments:
  -v, --verbose    Show more output
  -h, --help       Show this help message and exit
```

## Example
```sh
python3 bot.py --visits 100 --url https://www.youtube.com/watch?v=IamNOOB --verbose
```

### For more help, details, chat and feedback join [Telegram Group](http://t.me/linux_repo)

## Follow on:
### GitHub: https://github.com/AbirHasan2005
### Twitter: https://twitter.com/AbirHasan2005
### Facebook: https://facebook.com/AbirHasan2005
### Instagram: https://instagram.com/AbirHasan2005

## Donate me if you want to help me:

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://paypal.me/AbirHasan2005)

---

## Codes from [bot.py](https://github.com/AbirHasan2005/YouTube_Views_Bot/blob/master/bot.py)
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# A Bot to increase YouTube video views
# This python script was coded by AbirHasan2005
# If you use any codes from here than must give me credits
# Read README.md file
# Telegram Group: http://t.me/linux_repo

# Python Bot script starts:
import sys
import time
from random import randrange
from modules.youtube import YouTube
from modules import utils


class Bot:
    # Bot to increase YouTube video views
    # Coded by AbirHasan2005

    def __init__(self, options):
        # init variables

        self.opts = options

    @staticmethod
    def player_status(value):
        # Returns the status based one the input code

        status = {
            -1: 'unstarted',
            0: 'ended',
            1: 'playing',
            2: 'paused',
            3: 'buffering',
            5: 'video cued',
        }
        return status[value] if value in status else 'unknown'

    def run(self):
        # run

        count = 1
        ipaddr = None
        while count <= self.opts.visits:
            if self.opts.enable_tor:
                ipaddr = utils.get_new_tor_ipaddr(proxy=self.opts.proxy)
            if not ipaddr:
                ipaddr = utils.get_ipaddr(proxy=self.opts.proxy)
            youtube = YouTube(
                url=self.opts.url,
                proxy=self.opts.proxy,
                verbose=self.opts.verbose
            )
            title = youtube.get_title()
            if not title:
                if self.opts.verbose:
                    print('There was a problem while loading this page. Retrying ...')
                    youtube.disconnect()
                    continue
            if self.opts.visits:
                length = (len(title) + 4 - len(str(count)))
                print('[{0}] {1}'.format(count, '-' * length))
            if ipaddr:
                print('External IP address:', ipaddr)
            channel_name = youtube.get_channel_name()
            if channel_name:
                print('Channel name:', channel_name)
            subscribers = youtube.get_subscribers()
            if subscribers:
                print('Subscribers:', subscribers)
            print('Title:', title)
            views = youtube.get_views()
            if views:
                print('Views:', views)
            # youtube.play_video()
            youtube.skip_ad()
            if self.opts.verbose:
                status = youtube.get_player_state()
                print('Video status:', self.player_status(status))
            video_duration = youtube.time_duration()
            seconds = 30
            if video_duration:
                print('Video duration time:', video_duration)
                seconds = utils.to_seconds(duration=video_duration.split(':'))
                if seconds:
                    if self.opts.verbose:
                        print('Video duration time in seconds:', seconds)
            sleep_time = randrange(seconds)
            print('Vtopping video in %s seconds' % sleep_time)
            time.sleep(sleep_time)
            youtube.disconnect()
            count += 1


def _main():
    """ main """

    try:
        cli_args = utils.get_cli_args()
        bot = Bot(cli_args)
        bot.run()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    sys.exit(_main())

# Python Bot script coding done
# If you find any mistake in this script than please report in my Telegram Group: http://t.me/linux_repo
```

#### If you find any mistakes, problem or if you want to give any suggetion than must join my Telegram Group.
#### Telegram Group: http://t.me/linux_repo
