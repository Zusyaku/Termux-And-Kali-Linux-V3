#Network Device Discover by WodX
#Github: https://github.com/WodXTV/
#Twitter: https://twitter.com/wodsex/
#Discord: wodx#6724

import os, subprocess, ctypes, re, socket, requests, json
from colorama import Fore, init

devices = {}

def print_banner():
    subprocess.call('cls' if os.name == 'nt' else 'clear', shell=True)
    print(r'''{0}
   .               .
 .´  ·  .     .  ·  `.  NDD 2.0.0
 :  :  :  {1}(¯){0}  :  :  :  {1}Discover devices on local area network{0}
 `.  ·  ` {1}/¯\{0} ´  ·  .´  {2}Developed by WodX{0}
   `     {1}/¯¯¯\{0}     ´{3}
    '''.format(Fore.GREEN, Fore.WHITE, Fore.CYAN, Fore.RESET))

def main():
    init(convert=True)
    
    if os.name != 'nt':
        print(f'{Fore.RED}[-] {Fore.RESET}Please run NDD.py on a Windows machine')
        return
    
    ctypes.windll.kernel32.SetConsoleTitleW('NDD by WodX')
    
    print_banner()
    print(f'{Fore.GREEN}Scanning for local network devices ...{Fore.RESET}')
    
    subprocess.Popen('ping %s -n 1' % socket.gethostbyname(socket.gethostname()), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    process = subprocess.Popen('arp -a', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = (process.stdout.read() + process.stderr.read()).decode()
    output_split = output.split('\n')

    d_num = 0
    i_addr = ''
    
    for line in output_split:
        line = line.strip()
        
        regex = re.search(r'Interface: (.+?) ---', line)
        if regex:
            i_addr = regex.group(1)
            continue

        regex = re.search(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}\s+.{3}-.{3}', line)
        if regex:
            d_num += 1
            d_addr = re.search(r'(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})', line).group(0)
            d_mac = re.search(r'(.{2}-.{2}-.{2}-.{2}-.{2}-.{2})', line).group(0).replace('-', ':').upper()
            
            try:
                d_vendor = json.loads(requests.get('http://macvendors.co/api/' + d_mac).text)['result']['company']
            except:
                d_vendor = ''

            devices.update({d_addr:{'num': d_num, 'address': d_addr, 'mac': d_mac, 'vendor': d_vendor, 'interface': i_addr}})
    
    print_banner()
    print('    ID         Interface              IPv4 address           MAC address              Vendor')
    print('    ---        ---------------        ---------------        -----------------        ---------------')
    
    for device in devices.values():
        d_num = device['num']
        d_addr = device['address']
        d_mac = device['mac']
        d_vendor = device['vendor']
        i_addr = device['interface']

        id_spaces = ' ' * (11 - len(str(d_num)))
        interface_spaces = ' ' * (23 - len(i_addr))
        address_spaces = ' ' * (23 - len(d_addr))
        mac_spaces = ' ' * (25 - len(d_mac))
    
        print(f'    {Fore.RED}{d_num}{id_spaces}{Fore.WHITE}{i_addr}{interface_spaces}{Fore.CYAN}{d_addr}{address_spaces}{Fore.YELLOW}{d_mac}{mac_spaces}{Fore.GREEN}{d_vendor}')
    
    print()
    
if __name__ == '__main__':
    main()
