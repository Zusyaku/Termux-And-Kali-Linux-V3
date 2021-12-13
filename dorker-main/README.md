# Dorker

## Better Google Dorking with Dorker :) 


## Example usage

```
python3 dorker.py -d 'WHATEVER-DORK' -o output.txt

python3 dorker.py -f 'FILE-WITH-DORKS' -o output.txt
```

```text
This script by default runs in headless mode, but in the below gif script is run in headless=False mode,
if want to change that go to Line 48 in the script and change it
```

> If you dont want banner every time just comment the Line 116

## Usage gif

![Example usage gif](dorker.gif)

# Installation

* Needs Python3
* Install firefox

```bash
chmod +x install.sh
sudo ./install.sh
```
* get the latest geckodriver from [here](https://github.com/mozilla/geckodriver/releases)

## Example tool chain

```
python3 dorker.py -d 'DORK FOR XSS PARAMS' | dalfox
```

## Command-line options

```
  -h, --help   show this help message and exit
  -f DORKFILE, --dorkfile DORKFILE
  -d DORK,     --dork     DORK
  -o OUTPUT,   --output   OUTPUT
```

## Features

```

1) Custom Dork Support

2) Maybe Slow because we tried to bypass Google Captcha therefore more accurate Results

```

> Note: Google Might block You after dorking x amount of times using this tool. Use a vpn
