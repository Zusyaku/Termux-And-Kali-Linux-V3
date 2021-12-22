<?php
/*
name: bing subdomain scanner
author: rieqyns13
usage: php bing.php domain.com
*/
$args = $_SERVER['argv'];
if(!isset($args[1])){
    echo "[+]Penggunaan di terminal/cmd: php bingsubdomainscanner.php site.com";
    exit;
}else $url = $args[1];
scan($url);
function curl($url){
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
    $exec = curl_exec($ch);
    curl_close($ch);
    return $exec;
}
function scan($url){
    $i=1;
    $jum=0;
    $reg = '@^(https?\://)?(www\.)?([a-z0-9]([a-z0-9]|(\-[a-z0-9]))*\.)+[a-z]+$@i';
    if(preg_match($reg, $url)){
        while(1){
            $curl = curl("http://www.bing.com/search?q=domain:".$url."&first=".$i);
            $data = preg_match_all('#\<div class\="sb_meta"\>\<cite\>(.*?)\</cite\>#is', $curl, $m) ? $m[1] : null;
            if($data==null){
                echo "Tidak ada hasil";
                exit;
            }
            foreach($data as $dat){
                $dat_ = preg_match("|/|i", $dat) ? strstr($dat, "/", 1) : $dat ;
                $urls[$i][] = $dat_;
            }
            $count = count($urls[$i]);
            $urls_ = array_unique($urls[$i]);
            sort($urls_);
            foreach($urls_ as $url_){
                echo $url_."\n";
                $jum++;
            }
            $i=$i+10;
            if($count<10){
                echo "\nJumlah subdomain terdeteksi: ".$jum;
                exit;
            }    
        }
    }else{
        echo "URL tidak valid";
        exit;
    }
}
?>