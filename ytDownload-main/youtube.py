import pytube,pyfiglet,os

print('Loading Downloads')

os.system('clear')

print(' * Download youtube videos with Python!\n')
link = input('[?] Link Videonya ➡ ')
print('\n[^] Mengcek data dan mendownload video...')

try:
   judul = pytube.YouTube(link).title
except:
   exit('[×] Video tidak ditemukan')
print('[=] Judul Videonya: '+judul)

pytube.YouTube(link).streams.get_highest_resolution().download('/storage/emulated/0/download')
print('[✓] Succes Cek Folder Download Anda!\n')
