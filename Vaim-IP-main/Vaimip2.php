<?php

$data = @unserialize(file_get_contents("http://ip-api.com/php/"));
$FCL="\033[01;33m";
$MCL="\033[01;37m>\033[01;32m";
$NCL="\033[00m";
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