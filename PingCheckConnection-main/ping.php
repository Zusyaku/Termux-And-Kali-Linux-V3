<?php
date_default_timezone_set("Asia/Jakarta");
error_reporting(0);
//Warna
function col($str,$color){
	if($color==5){$color=['rw','ry','rt','rg','rr','rp1','rp2'][array_rand(['h','k','b','u','m'])];}
	$war=array('rw'=>"\033[107m\033[1;31m",'rt'=>"\033[106m\033[1;31m",'ht'=>"\033[0;30m",'p'=>"\033[1;37m",'a'=>"\033[1;30m",'m'=>"\033[1;31m",'h'=>"\033[1;32m",'k'=>"\033[1;33m",'b'=>"\033[1;34m",'u'=>"\033[1;35m",'c'=>"\033[1;36m",'rr'=>"\033[101m\033[1;37m",'rg'=>"\033[102m\033[1;34m",'ry'=>"\033[103m\033[1;30m",'rp1'=>"\033[104m\033[1;37m",'rp2'=>"\033[105m\033[1;37m");return $war[$color].$str."\033[0m";}

//Ping
function ping($host, $port=80, $timeout=10) {
	$tB = microtime(true);
	$fP = fSockOpen($host, $port, $errno, $errstr, $timeout);
	if (!$fP) { return "down"; }
	$tA = microtime(true);
	return round((($tA - $tB)*10), 0)." ms";
}

//lambat
function Slow($msg){$slow = str_split($msg);
	foreach( $slow as $slowmo ){ echo $slowmo; usleep(10000);}}

//Lain-lain
$n = "\n";$n2 = "\n\n";$t = "\t";$r="\r                              \r";

system('clear');
echo Slow(col("Script by ","h")."iewil \n\n");

$data='CheckPing9Des2021';

$tes=array(
'google.com',
'stop'
);

$te=current($tes);

while(true){
	if($te=="stop"){
		//$res=file_get_contents($data);
		str_repeat('~',55).'\n';$te=reset($tes);
		}
		
		//respon($te);
		if(ping($te)=="down"){
		$base="[".date('H:i:s')."] $te => Link Down \n";
		echo Slow(col("[".date('H:i:s')."] ","b").col('from','k').' '.col($te,'p').col(" time",'k').'='.col(ping($te)."\n",'m'));
		$file=fopen($data,"a");
		fwrite($file,$base);
		fclose($file);
		}else{
			echo Slow(col("[".date('H:i:s')."] ","b").col('from','k').' '.col($te,'p').col(" time",'k').'='.col(ping($te)."\n",'h'));
			}
		sleep(2);$te=next($tes);
	}


