import argparse
import os
import sys
import requests
import time

try:
        os.system("python lib/version.py")
        time.sleep(1)
        os.system("python etc/nmap.py")
except KeyboardInterrupt:
        sys.exit()
