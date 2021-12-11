<?php
require 'func.php';
error_reporting(0);
print "\nMENU : \n";
print "\n1. Voc";
print "\n2. Mission";
print "\n\nPilih Nomor Menu : ";
$menuk = trim(fgets(STDIN));
if($menuk == "1")
{
	awal:
	echo "Input FIle Token : ";
	@$fileakun = trim(fgets(STDIN));

	if(empty(@file_get_contents($fileakun)))
	{
		print PHP_EOL."File Token Tidak Ditemukan.. Silahkan Input Ulang".PHP_EOL;
		goto awal;
	}

	print PHP_EOL."Total Ada : ".count(explode("\n", str_replace("\r","",@file_get_contents($fileakun))))." Token, Letsgo..";

	foreach(explode("\n", str_replace("\r", "", @file_get_contents($fileakun))) as $c => $akon)
	{	
$iki = voc($akon);
if ($iki['data'] == false){
print "\n[".$akon."] info : Token Expired/gak ada Voc";
}else{
foreach ($iki['data'] as $items) {
$decs = $items['title'];
$reward = $items['configs'][0]['key'].' '.$items['configs'][0]['value'];
$exp = $items['expiry_date'];
print "\n[".$akon."] Desc: ".$decs." | Info: ".$reward." - Exp:".$exp."";
fwrite(fopen("voc.txt", "a"), "[".$akon."] Desc: ".$decs." | Info: ".$reward." - Exp:".$exp."\n");
}
	}
	}
}elseif($menuk == "2"){
		awal1:
	echo "Input FIle Token : ";
	@$fileakun = trim(fgets(STDIN));

	if(empty(@file_get_contents($fileakun)))
	{
		print PHP_EOL."File Token Tidak Ditemukan.. Silahkan Input Ulang".PHP_EOL;
		goto awal1;
	}

	print PHP_EOL."Total Ada : ".count(explode("\n", str_replace("\r","",@file_get_contents($fileakun))))." Token, Letsgo..";

	foreach(explode("\n", str_replace("\r", "", @file_get_contents($fileakun))) as $c => $akon)
	{	
$iki = misi($akon);
if ($iki['data']['new_journeys'] == false){
print "\n[".$akon."] info : Token Expired/gak ada mission";
}else{
foreach ($iki['data']['new_journeys'] as $items) {
$decs = $items['description'];
$reward = $items['total_reward_info'];
$exp = $items['journey_config_end_date'];
print "\n[".$akon."] Desc: ".$decs." | Info: ".$reward." - Exp:".$exp."";
fwrite(fopen("mission.txt", "a"), "[".$akon."] Desc: ".$decs." | Info: ".$reward." - Exp:".$exp."\n");
}
}
	}
}else{
	print "\nNgentot";
	exit;
}
