<?php

error_reporting(0);
include ("func.php");
echo "\e -------------------------------------------------\n";
echo "\e                GOJEK VERSI 1.7.1        \n";
echo "\e SCRIPT GOJEK AUTO REGISTRASI + AUTO CLAIM VOUCHER\n";
echo "\e By : CyberK4nd4s - Bonek1927\n";
echo "\e -------------------------------------------------\n";
echo "\e          
                ⠄⠄⠄⠄⠄⠄⠄⢎⢗⣾⠫⡫⢖⢄⠄⠄⠄⠄⠄⠄⠄⠄⠄
                ⠄⠄⠄⠄⠄⢀⡎⠒⠐⠾⠛⠙⣆⡢⠑⢣⠄⠄⠄⠄⠄⠄⠄⠄ 
                ⠄⠄⠄⠄⢠⢾⡦⢒⡁⣰⣿⣿⣦⡐⣳⣩⢇⠄⠄⠄⠄⠄⠄⠄
                ⠄⠄⠄⠄⡾⣢⢭⠔⣴⠒⢺⣿⣯⠥⠑⠑⡾⡄⠄⠄⠄⠄⠄⠄ 
                ⠄⠄⠄⠄⣷⡡⠁⠣⣿⣿⣿⣿⢿⣶⣠⢪⠒⡟⠄⠄⠄⠄⠄⠄ 
                ⠄⠄⠄⢠⡼⠾⡀⡄⣿⣿⢿⡏⢾⡇⣘⡽⠱⢧⡀⠄⠄⠄⠄⠄ 
                ⠄⠄⠄⠄⠉⠉⠱⢦⣘⢿⣾⣶⢟⣠⡀⡄⢔⠏⠁⠄⠄⠄⠄⠄ 
                ⠄⠄⠄⠄⠄⠄⣠⢼⣿⣷⣶⣾⡷⢸⣗⣯⣿⣶⣿⣶⡄⠄⠄⠄ 
                ⠄⠄⣀⣤⣴⣾⣿⣷⣭⣭⣭⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠄⠄ 
                ⠄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣸⣿⣿⣧⠄⠄ 
                ⠄⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⢻⣿⣿⡄⠄ 
                ⠄⢸⣿⣮⣿⣿⣿⣿⣿⣿⣿⡟⢹⣿⣿⣿⡟⢛⢻⣷⢻⣿⣧⠄
                ⠄⠄⣿⡏⣿⡟⡛⢻⣿⣿⣿⣿⠸⣿⣿⣿⣷⣬⣼⣿⢸⣿⣿⠄
                ⠄⠄⣿⣧⢿⣧⣥⣾⣿⣿⣿⡟⣴⣝⠿⣿⣿⣿⠿⣫⣾⣿⣿⡆
                ⠄⠄⢸⣿⣮⡻⠿⣿⠿⣟⣫⣾⣿⣿⣿⣷⣶⣾⣿⡏⣿⣿⣿⡇ 
                ⠄⠄⢸⣿⣿⣿⡇⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣿⣿⣿⡇ 
                ⠄⠄⢸⣿⣿⣿⡇⠄⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⠄ 
                ⠄⠄⣼⣿⣿⣿⢃⣾⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣿⣿⣿⡇⠄ 
                ⠄⠄⣿⣿⡟⣵⣿⣿⣿⣿⣿⣿⣿⣿⡟⢻⣿⣿⢇⣿⣿⡿⠄⠄\n";
echo "\n";
nope:
echo "\e[?] Masukkan Nomor HP Anda (+62) : ";
$nope = trim(fgets(STDIN));
$cek = cekno($nope);
if ($cek == false)
    {
    echo "\e[x] Nomor Telah Terdaftar\n";
			goto nope;
    }
  else
    {
echo "\e[!] Siapkan OTP Kamu\n";
sleep(5);
$register = register($nope);
if ($register == false)
    {
    echo "\e[x] Failed Get OTP!\n";
    }
  else
    {
    otp:
    echo "\e[!] Masukkan Kode Verifikasi (OTP) : ";
    $otp = trim(fgets(STDIN));
    $verif = verif($otp, $register);
    if ($verif == false)
        {
        echo "\e[x] Kode Verifikasi Salah\n";
        goto otp;
        }
      else
        {
		$h=fopen("newgojek.txt","a");
		fwrite($h,json_encode(array('token' => $verif, 'voc' => 'gofood gak ada'))."\n");
		fclose($h); 
                echo "\e[!] Trying to redeem Reff :G-MPW4WBM\n";
                sleep(3);
            $claim = reff($verif);
            if ($claim == false){
            echo "\e[!] Failed to Claim Voucher, Try to Claim Manually\n";
            }else{
                echo "\e[+] ".$claim."\n";
            }
    }
    }
    }


?>
