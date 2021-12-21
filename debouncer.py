import requests, os, threading, time

print("[+]Bulk Valid Mail Checker V1[+]")
time.sleep(1)

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")
print('#  \033[31m8888888b.           888                                                          \033[0m')
print('#  \033[31m888  "Y88b          888                                                          \033[0m')
print('#  \033[31m888    888          888                                                          \033[0m')
print('#  \033[31m888    888  .d88b.  88888b.   .d88b.  888  888 88888b.   .d8888b  .d88b.  888d888\033[0m')
print('#  \033[31m888    888 d8P  Y8b 888 "88b d88""88b 888  888 888 "88b d88P"    d8P  Y8b 888P"  \033[0m')
print('#  \033[31m888    888 88888888 888  888 888  888 888  888 888  888 888      88888888 888    \033[0m')
print('#  \033[31m888  .d88P Y8b.     888 d88P Y88..88P Y88b 888 888  888 Y88b.    Y8b.     888    \033[0m')
print('#  \033[31m8888888P"   "Y8888  88888P"   "Y88P"   "Y88888 888  888  "Y8888P  "Y8888  888    \033[0m\n\n')

def checker(data):
    datas = {"email": data}
    headers1 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
        'Cookie': '__cfduid=d7388b7b2c3df08e9c6dae21fb1ee29581612352407; .AspNetCore.Antiforgery.38G8fUVOpE4=CfDJ8JOdAoeLmM5PtcCdCER4YLc-DP0khUxXzfSsaC2yutkNRWhkAKqLeyl033-ADG943CkBB_fiO6YYhuMl6heGg2yq7TDThZDJNa86aM_VmxzXC2GeKvCjpvA1MsI8Tp5t-tTVGWOWbduaxRGDW4ZZNBc; .EmailHippo.Session=CfDJ8JOdAoeLmM5PtcCdCER4YLeIOlhBXA7evw0hlbusgaG3kCgjxTeT6iNn%2B%2Blwf6NOkqIeq9BEzELGNx8uyZmZWxuZqMmKdVeWnvH64IkoeshP6g97NNAhAfHxZJ0LIViTW%2BlB%2FM5flmvwWE%2FsIhuRAFuFk0UIzSr6bMyizUsPCt7t'}

    response = requests.post("https://tools.verifyemailaddress.io/", headers=headers1, data=datas).text
    if "OK" in response:
        print("\033[32;1mValid\033[0m | " + data)
        with open("Valid.txt", "a") as live:
            live.write(data+'\n')
    else:
        print('\033[31;1mDead\033[0m | ' + data)
        with open("Dead.txt", "a") as die:
            die.write(data+'\n')

while True:
    try:
        list = input("Insert mailist: ")
        break
    except:
        print("Fichier non trouvé...\n")

combo = []

with open(list, "r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.rstrip()
        if line not in combo:
            combo.append(line)

for x in combo:
    try:
        thread = threading.Thread(target=checker, args={x})
        thread.start()
        time.sleep(0.7)
    except:
        pass
