#!/usr/bin/python
# Thanks To StarSkyGeminid
# Author ? gada bosque
# Cuma percobaan wkwk nanti di banyakin dah biar agak kerenan diki awokawok
# yang terpenting adalah:
#     ___  ____  _____ _   _ ____   ___  _   _ ____   ____ _____
#    / _ \|  _ \| ____| \ | / ___| / _ \| | | |  _ \ / ___| ____|
#   | | | | |_) |  _| |  \| \___ \| | | | | | | |_) | |   |  _|
#   | |_| |  __/| |___| |\  |___) | |_| | |_| |  _ <| |___| |___
#    \___/|_|   |_____|_| \_|____/ \___/ \___/|_| \_\\____|_____|

import os
try:
    import time
    import random
    import re

except ImportError:
    os.system("pip install re")

# -----[ Color ]-----
m = '\x1b[1;31m'
p = '\x1b[1;37m'
# -------------------

# ----------[ Banner ]----------
banner = f'''
{m}╦═╗{p}┌─┐┌─┐┌┬┐┌─┐┬─┐
{m}╠╦╝{p}├┤ ├┤ │││├─┤├┬┘
{m}╩╚═{p}└─┘└─┘┴ ┴┴ ┴┴└─
  {m}╔═╗{p}┬─┐┌─┐ ┬┌─┐┌─┐┌┬┐
  {m}╠═╝{p}├┬┘│ │ │├┤ │   │
  {m}╩  {p}┴└─└─┘└┘└─┘└─┘ ┴ '''

###-------------------------[ Array Data ]-------------------------###
bantuan = ['reemar -help', '-help', 'help', 'bantuan']
kumpulan_perintah = ['saya butuh hiburan',
                     'cuaca [ kota ]',
                     'siapa yang menciptakanmu reemar',
                     'install bahan'
                     ]

kata_orang = ["saya", "kamu", "aku", "dia", "mereka", "anda"]
kata_kerja = ["hiburan", "butuh", "menciptakanmu", "install"]
kata_benda = ["bahan"]
kata_cuaca  = ["info", "cuaca", "hari", "ini"]

perintah_cuaca = ["cuaca hari ini",
                  "info cuaca", "info cuaca hari ini", "cuaca"]
perintah_hiburan = ["hibur saya", "saya butuh hiburan", "saya gabut"]

perintah_gombal = ["gombalin", "gombalin saya",
                   "gombalin dong", "gombalin saya reemar"]
perintah_musik = ["putarkan saya musik",
                  "musik", "play musik", "putarkan musik", "putar musik"]

perintah_install = ["install bahan", "install"]

ya = ["ya", "yes", "y", "ok"]
tidak = ["tidak", "no", "enggak", "n", "t"]


class Front_End():
    def __init__(self):
        os.system('clear')
        print(banner)
        self.Start_Chat()

    def Start_Chat(self):
        try:
                while True:
                    chat_input = str(input(f'{m}[{p}?{m}]{p}Reemar _{m}>{p} '))
                    if chat_input.lower() in kumpulan_perintah:
                        Chat_Respod(chat_input)
                    elif chat_input.lower() in perintah_hiburan:
                        Chat_Respod.Hibur("Hibur")
                    elif chat_input.lower() in perintah_musik:
                        Back_end(hibur="musik")
                    elif chat_input.lower() in bantuan:
                        Help()
                    elif chat_input.split()[0] in kata_cuaca or chat_input.split()[1] in kata_cuaca:
                        Back_end.Cuaca(chat_input)
                    elif chat_input.lower() in ['', ' ']:
                        print(f'{m}type : {p}-help {m}for show all command')
                    else:
                        if 'cuaca' in chat_input.split() and len(chat_input.split()) > 1:
                                Back_end.Cuaca(chat_input)
                        else:
                                print(f'{p}[{m}!{p}] Salah {m}!!')
        except (IndexError,KeyboardInterrupt,EOFError):
                exit(f'{m}[{p}!{m}]{p}Error {m}!!')

class Chat_Respod():
    def __init__(self, chat_input):
        for x in range(len(kumpulan_perintah)):
            if str(chat_input) == kumpulan_perintah[x]:
                array_exist = x

        if array_exist == 0:
            self.Hibur()
        elif array_exist == 1:
            self.Pencipta_reemar()
        elif array_exist == 2:
            self.Install_bahan()

    def Hibur(self):
        print(f'\n\t{m}------------------------{p}')
        print('\t - putarkan saya musik')
        print('\t - gombalin saya reemar')
        print(f'\t{m}-------------------------{p}')
        while True:
            chat_input = str(input(f'{m}[{p}?{m}]{p}Reemar _{m}>{p} '))
            if chat_input in perintah_musik:
                os.system('termux-tts-speak -r 1.2 Baiklah')
                return Back_end.Hibur(hibur="musik")
                break
            elif chat_input in perintah_gombal:
                return Back_end.Hibur(hibur="gombal")
                break
            else:
                print("Perintah Tidak tersedia")

    def Pencipta_reemar(self):
        print("\nSaya diciptakan oleh Orang yang bernama Muhamad Royyani. Dia Hanyalah Seorang anak, yang masih berumur 16 tahun")

    def Install_bahan(self):
        os.system("\npkg install termux-api")


class Back_end():
    class Hibur():
        def __init__(self, **data):
            if data["hibur"] == "musik":
                return Back_end.Hibur.musik("musik")
            elif data["hibur"] == "gombal":
                return Back_end.Hibur.gombal("gombal")

        def musik(self):
            lokasi_f = str(
                input(f'{m}[{p}?{m}]{p}Masukkan nama folder ex : /sdcard/Music/ _{m}>{p} '))
            os.system('mpv '+lokasi_f)

        def gombal(self):
            # didapat dari https://katasiana.com/kata-kata-gombal/
            ###==---------------------=[ Penggombalan ]=---------------------==###
            kalimat_gombal_awal = ["Kamulah bulan bagi matahariku...",
                                   "Tahu nggak kenapa menara pisa miring?",
                                   "Sejak mengenalmu bawaannya aku pengen belajar terus",
                                   "Bagaimana kalau kita berdua jadi komplotan perampok?",
                                   "Kamu tau gak? Kenapa kalau aku menghafal lihatnya ke atas?",
                                   "Orang kurus itu setia",
                                   "Maksud hati memeluk gunung",
                                   "Kamu tu kayak warteg",
                                   "Aku gak sedih kok kalo besok hari senin",
                                   ]
            kalimat_gombal_akhir = ["Cahaya kemilau dirimu menerangi malamku yang sunyi",
                                    "Soalnya ketarik sama senyuman kamu",
                                    "Belajar menjadi yang terbaik buat kamu.",
                                    "Aku merampok hatimu dan kamu merampas hatiku.",
                                    "soalnya kalau merem langsung kebanyang wajahmu.",
                                    "makan aja tidak pernah nambah apalagi pasangan.",
                                    "apalah daya aku lebih suka memeluk kamu.",
                                    "sederhana namun berkualitas.",
                                    "aku sedihnya kalau gak ketemu kamu",
                                    ]
            total_kalimat_gombal = (len(kalimat_gombal_awal))-1

            while True:
                random_kata = random.randint(0, total_kalimat_gombal)
                os.system('termux-tts-speak -r 1.2 '+kalimat_gombal_awal[random_kata])
                #print("     "+kalimat_gombal_awal[random_kata]+",")
                time.sleep(1)
                os.system('termux-tts-speak -r 1.2 '+kalimat_gombal_akhir[random_kata])
                #print("     "+kalimat_gombal_akhir[random_kata])

                tanya = str(
                    input(f'{m}[{p}?{m}]{p}Apakah anda ingin mendengarkan lagi? : '))
                if tanya.lower() in ya:
                    time.sleep(1)
                elif tanya.lower() in tidak:
                    print("Oke")
                    break
                else:
                    print("Pilihan tidak tersedia")
                    break

    class Cuaca():
        def __init__(self, chat_input):
            for x in range(len(chat_input.split())):
                if chat_input.split()[x] not in kata_cuaca:
                    #Saya sengaja pakai curl, bisa diganti request tapi saya coba nggak ada warnanya(beda kode)
                    os.system("curl -s  http://wttr.in/"+chat_input.split()[x]+" | sed -n \"1,7p\"")
                    break


class Help():
    def __init__(self):
        print('\n\t[ List command ]')
        print(*kumpulan_perintah, sep="\n")


if __name__ == "__main__":
    try:
        Front_End()
    except KeyboardInterrupt:
        print("\n")
        pass

