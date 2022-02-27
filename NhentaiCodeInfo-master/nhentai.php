<?php
system("clear");
echo "######################################\n";
echo "#         Nhentai Code Info          #\n";
echo "# Coded By LoliC0d3    t.me/LoliC0d3 #\n";
echo "######################################\n";
echo "Masukan Code Nuklir: ";
$input = fopen("php://stdin","r");
$code = trim(fgets($input));
function curl($url){
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    $output = curl_exec($ch);
    curl_close($ch);
    return $output;
}

$send = curl("https://apis.nhent.ai/g/".$code);
$data = json_decode($send, TRUE);
$b = $data['title'];
echo "Judul   : ".$b;
echo "\n";
$b = $data['details']['tags'][0];
echo "Genre   : ".$b;
echo "\n";
$b = $data["details"]["artists"][0];
echo "Artis   : ".$b;
echo "\n";
$b = $data["details"]["parodies"][0];
$b = $data["details"]["groups"][0];
echo "Groups  : ".$b;
echo "\n";
$b = $data["details"]["languages"][0];
echo "Bahasa  : ".$b;
echo "\n";
$b = $data["details"]["categories"][0];
echo "Kategori: ".$b;
echo "\n";
$b = $data["link"];
echo "Link    : ".$b;
echo "\n";
?>
