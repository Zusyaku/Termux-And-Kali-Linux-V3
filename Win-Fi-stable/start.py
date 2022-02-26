import subprocess

print("")
print("Wi-Fi Router Names & Passwords:")
print("")

########## Main Code ############# Main Code ############# Main Code ##########

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
router = [line.split(':')[1][1:-1] for line in data if "All User Profile" in line]


for name in router:
    info = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', name, 'key=clear']).decode('utf-8').split('\n')
    passwrd = [line.split(':')[1][1:-1] for line in info if "Key Content" in line]
    net = [line.split(':')[1][1:-1] for line in info if "Network type" in line]
    version = [line.split(':')[1][1:-1] for line in info if "Version" in line]
    sec = [line.split(':')[1][1:-1] for line in info if "Authentication" in line]
    try:
        # Output with Password
        print(f' Router   : {name} \n Password : {passwrd[0]} \n Network  : {net[0]} \n Version  : {version[0]} \n Security : {sec[0]} \n')
    except IndexError:
        # Output without Password
        print(f' Router   : {name} \n Password : Not Found! \n Network  : {net[0]} \n Version  : {version[0]} \n Security : {sec[0]} \n')

########## Main Code ############# Main Code ############# Main Code ##########

print("      Coded By AbirHasan2005      ")
