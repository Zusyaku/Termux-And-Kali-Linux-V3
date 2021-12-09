<?php
$black = "\e[30m\e[1m";
$yellow = "\e[93m";
$orange = "\e[38;5;208m";
$blue   = "\e[34m";
$RR="\033[1;31m";
$lblue  = "\e[36m";
$cln    = "\e[0;94m";
$green  = "\e[92m";
$fgreen = "\e[32m";
$red    = "\e[91m";
$magenta = "\e[35m";
$bluebg = "\e[44m";
$lbluebg = "\e[106m";
$greenbg = "\e[42m";
$lgreenbg = "\e[102m";
$yellowbg = "\e[43m";
$lyellowbg = "\e[103m";
$BgRed = "\e[101m";
$grey = "\e[37m";
$cyan = "\e[36m";
$bold   = "\e[1m";
$nbold = "\e[1;97m";
$FCL="\033[01;33m";
$MCL="\033[01;37m>\033[01;32m";
$NCL="\033[00m";
echo "$red"."└─".$grey."Enter IP/Domain: ". "$red";
$ip = readline();
$data = @unserialize(file_get_contents("http://ip-api.com/php/".$ip));
date_default_timezone_set($data['timezone']);
system("clear");

if($data['status'] == 'success') {
echo "\n ".$FCL."IP Address    ".$MCL."   ".$data['query'];
echo "\n ".$FCL."Country code  ".$MCL."   ".$data['countryCode'];
echo "\n ".$FCL."Country       ".$MCL."   ".$data['country'];
echo "\n ".$FCL."Date & Time   ".$MCL."   ".date("F j, Y, g:i a");
echo "\n ".$FCL."Region code   ".$MCL."   ".$data['region'];
echo "\n ".$FCL."Region        ".$MCL."   ".$data['regionName'];
echo "\n ".$FCL."City          ".$MCL."   ".$data['city'];
echo "\n ".$FCL."Zip code      ".$MCL."   ".$data['zip'];
echo "\n ".$FCL."Time zone     ".$MCL."   ".$data['timezone'];
echo "\n ".$FCL."ISP           ".$MCL."   ".$data['isp'];
echo "\n ".$FCL."Organization  ".$MCL."   ".$data['org'];
echo "\n ".$FCL."ASN           ".$MCL."   ".$data['as'];
echo "\n ".$FCL."Latitude      ".$MCL."   ".$data['lat'];
echo "\n ".$FCL."Longtitude    ".$MCL."   ".$data['lon'];
echo "\n ".$FCL."Location      ".$MCL."   ".$data['lat'].",".$data['lon'];
echo "\n\n$NCL";

}

?>