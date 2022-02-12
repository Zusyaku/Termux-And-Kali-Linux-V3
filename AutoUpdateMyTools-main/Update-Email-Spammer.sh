
g="\033[1;32m"
r="\033[1;31m"
b="\033[1;34m"
w="\033[0m"
o="\033[1;33m"

red='\e[1;31m'
default='\e[0m'
yellow='\e[0;33m'
orange='\e[38;5;166m'
green='\033[92m'

echo -e "$yellow  ____ ___            .___                      "
echo -e "$yellow |    |   \______   __| _/____ _/  |_  ____     "
echo -e "$yellow |    |   /\____ \ / __ |\__  \\   __\/ __ \    "
echo -e "$yellow |    |  / |  |_> > /_/ | / __ \|  | \  ___/    "
echo -e "$yellow |______/  |   __/\____ |(____  /__|  \___  >   "
echo -e "$yellow           |__|        \/     \/          \/    "
echo ""

cd
cd
rm -rf Email-Spammer
sleep 2
git clone https://github.com/mishakorzik/Email-Spammer
cd
cd
python Email-Spammer/src/aumt.py
