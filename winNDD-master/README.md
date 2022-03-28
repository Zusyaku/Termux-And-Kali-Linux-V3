<h1 align="center">winNDD - Windows Network Device Discovery Tool</h1>

![alt text](https://github.com/WodxTV/winNDD/blob/master/resources/NDD.PNG)
**winNDD** is a simple local area network scanner for Windows to discover other devices. It uses the [ARP protocol](https://en.wikipedia.org/wiki/Address_Resolution_Protocol) in order to get the devices IPv4 and MAC address. It will return network interface, IPv4 address, MAC address and MAC Vendor of every device on the local network, in a easily readable list.

# Installation
In order to run the script, you need to have Python 3 installed. Download the latest version of Python 3 via [this link](https://www.python.org/downloads/)

When Python has been installed on your machine, you need to install the external Python modules.
**Install the modules via:**
```bash
$ cd .\winNDD\
$ python -m pip install -r requirements.txt
```

# Running winNDD
To run the script, you simply use the Python command:
```bash
$ python ndd.py
```

# Developer
**WodX**
* Github: [WodXTV](https://github.com/wodxtv)
* Discord: [wodx#6724](https://prfl.es/profile/621044372951269417)
* Twitter: [@wodsex](https://twitter.com/wodsex)
