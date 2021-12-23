import os,sys,time

def tsl():
     banner = (f"""\033[1;32m

              ███        ▄████████  ▄█       
          ▀█████████▄   ███    ███ ███       
             ▀███▀▀██   ███    █▀  ███       
              ███   ▀   ███        ███       
              ███     ▀███████████ ███       
              ███              ███ ███       
              ███        ▄█    ███ ███▌    ▄ 
             ▄████▀    ▄████████▀  █████▄▄██ 
                         ▀         
            \033[1;32m--\033[1;31m[ \033[1;37mToken Security Login \033[1;31m]\033[1;32m--

\033[1;31m● \033[1;37mLink Token \033[31m: \033[1;31m[ \033[1;32;4mSubscribe Kenzi Ganzz\033[0m \033[1;31m]
     """)
     os.system("clear")
     print(banner)
     token = input("\033[1;31m➤ \033[1;37mInput Token \033[31m: \033[1;37m")
     if token == 'Subscribe Kenzi Ganzz':
          print ("\n\033[1;31m➤ \033[1;37mToken Benar \033[1;32m√√ \033[31m")
          time.sleep(2)
          os.system("clear")
          os.system("xdg-open https://youtube.com/channel/UC7ygjAbDjuiN76PqOlJm40A")
          print("\033[1;32m√ \033[1;37mSubscibe dulu Dong Bang \033[1;36m>_<")
          time.sleep(4)
          os.system("clear")
          print ("\033[1;31m═══════════════════════════════════════════════════")
          print ("\033[1;31m!\033[1;33m Note \033[1;31m: \033[1;37mDecompile Support Python2")
          print ("\033[1;31m! \033[1;37mJanggan Recode Mulu bre Oke \033[1;32m>_<")
          print ("\033[1;31m═══════════════════════════════════════════════════")
          time.sleep(1)
          mar = input("\n\033[1;31m➤ \033[1;37mMau Install Marbase \033[1;32my\033[1;33m/\033[1;30mt \033[1;31m:\033[1;32m ")
          if mar == '':
              print ("\n\033[1;31m➤ \033[1;37mJanggan Kosong Sayang \033[1;31m!!")
          elif mar == 'y' or mar == 'Y':
              print ("\n\033[1;31m➤ \033[1;37mSedang Mengginstall Marbase \033[1;31m!!")
              time.sleep(3)
              os.system('python2 __run__.py')
              print ("\n\033[1;31m➤ \033[1;37mBerhasil Mengginstall Marbase \033[1;32m√√ \033[31m")
          elif mar == 't' or mar == 'T':
              print ("\n\033[1;31m➤ \033[1;37mMakasih Sudah Memggunakan Tools Kami \033[1;31m!! \033[31m")
          else:
              print ("\n\033[1;31m➤ \033[1;37mPilih Yang bener dong \033[1;32m!! \033[31m")
     else:
          print ("\n\033[1;31m▶ \033[1;37mToken Salah \033[1;31m!! \033[31m")
          time.sleep(2)
          tsl()

tsl()

