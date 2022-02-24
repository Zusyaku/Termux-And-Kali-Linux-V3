<?php
error_reporting(0);
const 
a = [
"iewil",
"shortminer",
"https://bit.ly/3GOoZP5",
"https://youtu.be/Dk-v5NiFNJE",
"https://pastebin.com/raw/RZxwy6dr",
"http://ip-api.com/json"
],
b = "\033[1;34m",
c = "\033[1;36m",
d = "\033[0m",
h = "\033[1;32m",
k = "\033[1;33m",
m = "\033[1;31m",
n = "\n",
p = "\033[1;37m",
r = "https://company.shortminer.work/?r=TCtRPwDjCws2Vzb3ZgdBQ63NqU5E5QRt&rc=DGB",
u = "\033[1;35m",
v = "1.0",
hp = "\033[1;7m",
mp = "\033[101m\033[1;37m",
mm = "\033[101m\033[1;31m";
const ht = "https://company.".a[1].".work";
function a($u, $h = 0, $p = 0, $x = 0){
	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, $u);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
	curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
	curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
	curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);
	curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 30);
	curl_setopt($ch, CURLOPT_COOKIE,TRUE);
	curl_setopt($ch, CURLOPT_COOKIEFILE,"cookie.txt");
	curl_setopt($ch, CURLOPT_COOKIEJAR,"cookie.txt");
	if($p){
		curl_setopt($ch, CURLOPT_POST, true);
		curl_setopt($ch, CURLOPT_POSTFIELDS, $p);
	}
	if($h){
		curl_setopt($ch, CURLOPT_HTTPHEADER, $h);
	}if($x){
		curl_setopt($ch, CURLOPT_HTTPPROXYTUNNEL, true);
		curl_setopt($ch, CURLOPT_PROXY, $x);
	}
	curl_setopt($ch, CURLOPT_HEADER, true);
	$r = curl_exec($ch);
	$c = curl_getinfo($ch);
	if(!$c) return "Curl Error : ".curl_error($ch); else{
		$hd = substr($r, 0, curl_getinfo($ch, CURLINFO_HEADER_SIZE));
		$bd = substr($r, curl_getinfo($ch, CURLINFO_HEADER_SIZE));
		curl_close($ch);
		return array($hd,$bd);
	}
}
/*
function b2(){
	c();
	$s = file_get_contents(a[4]);
	$t = e($s,'#'.a[1].':','|',1);
	if($t == "on"){
		$st = ."Online";
	}elseif($status == "off" or $status == null){
		$st = m."Offline";
	}
	$z = trim(strtoupper(a[1]));
	$x = 18;
	$y = strlen($z);
	$l = str_repeat('_',$x-$y);
	echo n.m."[".p."Script".m."]->".k."["..$z.k."]-["..v.k."]".p.$l.".".n.u.".__              .__.__ 	    ".p."| ".n.u."|__| ______  _  _|__|  |   ".$st.u." ".n."|  |/ __ \ \/ \/ /  |  |".n."|  \  ___/\     /|  |  |__".n."|__|\___  >\/\_/ |__|____/".n."        \/".n.mm."[".mp."▶".mm."]".d." ".k."ttps://www.youtube.com/c/iewil".n.c.p." >_".d.b." Team-Function-INDO".n.p."────────────────────────────────────".n.k."Link Regist ".m.": "..a[2].n.n;
}
*/
function b($i=0){
	if(!$i){
		c();
	}
	$s = file_get_contents(a[4]);
	$t = e($s,'#'.a[1].':','|',1);
	if($t == "on"){
		$st = w("Online","h");
	}elseif($status == "off" or $status == null){
		$st = w("Offline","m");
	}
	$z = trim(strtolower(a[1]));
	return p.' Day:'.date("l").'    Date:'.date("d M Y").'    Time:'.date("H:i").n.l().
h." ╔═╗┬ ┬┌┐┌┌─┐┌┬┐┬┌─┐┌┐┌   ╔═╗┌─┐┌┬┐┬┬ ┬ ┬   ╦╔╦╗".n.
k." ╠╣ │ │││││   │ ││ ││││───╠╣ ├─┤│││││ └┬┘───║ ║║".n.
p." ╚  └─┘┘└┘└─┘ ┴ ┴└─┘┘└┘   ╚  ┴ ┴┴ ┴┴┴─┘┴    ╩═╩╝".n.l().
' Script    : '.$z.' '.v.'          '.$st.n.n.
'『』Creator: iewil'.n.'『』Youtube: youtube.com/c/iewil'.n.
'『』support: All-Team-Function & All-Member'.n.
'『』D_TRX  : TK67fkL9EpcoCqP2kxonwMmmwyQ5pJmm'.n.
w('『』NOTE   : THIS SCRIPT FREE NOT FOR SALE','u').n.l();
}

function c(){
	return system('clear');
}
function d($m){
	$s = str_split($m);
	foreach($s as $t){
		echo $t;
		usleep(70000);
	}
}
function e($a,$b,$c,$d){
	return explode($c,explode($b,$a)[$d])[0];
}
function f($a){
	return http_build_query($a);
}
function i($array, $position, $insertArray){
	$ret = [];
	if($position == count($array)){
		$ret = $array + $insertArray;
	}else{
		$i = 0;
		foreach($array as $key => $value){
			if($position == $i++){
				$ret += $insertArray;
			}
		$ret[$key] = $value;
		}
	}
	return $ret;
}
function l(){
	$l = 50;
	return str_repeat('─',$l).n;
}
function s($n){
	if(file_exists($n)){
		$d = file_get_contents($n);
	}else{
		$d = readline(w("Input ".$n,"m").w(" > ","k").h.n);
		echo n;
		file_put_contents($n,$d);
	}
	return $d;
}
function r($t,$s){
	$l = 50;
	if($t <= null){
		return $t;
	}
	$u = strlen($t);
	if($s == "tg"){
		$a = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48];
		if(in_array($u,$a)){
			$v = ($l-$u)/2;
			return str_repeat(' ',$v).$t;
		}else{
			$v = ($l-$u+1)/2;
			return str_repeat(' ',$v).$t;
		}
	}elseif($s == "kn"){
		$v = $l-$u;
		echo str_repeat(' ',$v).$t;
	}
}
function t(){
	$t = json_decode(file_get_contents(a[5]),1)["timezone"];
	if($t){
		date_default_timezone_set($t);
	}
}
function w($s,$c){
	if($c == "r"){
		$w = ['h','k','b','u','m'];
		$c = $w[array_rand($w)];
	}
	$w = ['h'=>h,'k'=>k,'b'=>b,'u'=>u,'m'=>m,'p'=>p];
	return $w[$c].$s.d;
}
function x(){
	error_reporting(0);
	if(strpos(b(1),"iewil") == ""){
		c();
		echo 'Warning: Undefined variable $a on line 115'.n;
		exit;
	}
}
function h(){
	return [
	"Host: company.shortminer.work",
	"user-agent: Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36",
	"referer: ".r
	];
}
function _l($w){
	$d = ["r"=>"TCtRPwDjCws2Vzb3ZgdBQ63NqU5E5QRt","rc"=>"DGB","microwallet"=>"FaucetPay","id1"=>$w,"currency"=>"DGB","startclaim"=>"Start claiming"];
	return a(ht."/verify.php",h(),f($d));
}
function _gl($w){
	return a($w,h());
}
function _m(){
	$wa = file("Wallet");
	foreach($wa as $w){
		$n = $n+1;
		if(file_exists("cookie.txt")){
			system("rm cookie.txt");
		}
		$r = _l(trim($w));
		$u = e($r[1],'var url = "','"',1);
		$g = _gl($u);
		$s = e($g[1],'You had get ','<br>',1);
		echo m.'['.k.'Wallet'.m.']->['.p.$n.m.']'.n;
		if($s){
			echo w(' Success','h').w(' ~> ','p').w($s,'k').n;
		}else{
			echo w(' Error','m').w('   ~> ','p').m."Cooldown Claim".n;
		}
		echo w(' Wallet','h').w('  ~> ','p').w(trim($w),'k').n;
		print l();
	}
	$n = 0;
	echo strtoupper(r("reset wallet","tg")).n;
	print l();
}
function _g(){
	$c = s('Cookie Faucetpay');
	$u = s('User_Agent');
	
	$ua[] = "user-agent: ".$u;
	$ua[] = "content-type: application/x-www-form-urlencoded; charset=UTF-8";
	$ua[] = "x-requested-with: XMLHttpRequest";

	$uas[] = "user-agent: ".$u;
	$uas[] = "cookie: ".$c;

	if(file_exists('Wallet')){
		$data=file_get_contents('Wallet');
	}

	while(true){
		$data = "utf8=✓&gp_address_coin[card]=single&gp_address_coin[coin]=litecoin&button=";
		$generate = a('https://generate.plus/en/address/coin',$ua,$data)[1];
		$wal = explode('</p>',explode('<u>Wallet Key:</u> ',$generate)[1])[0];
		
		system("rm cookie.txt");
		$fp = a("https://faucetpay.io/page/user-admin/linked-addresses",$uas);
		$token = explode('"',explode('type="hidden" name="token" value="',$fp[1])[1])[0];

		$data = "token=".$token."&address=".$wal."&label=&coin=5&submit=true";
		$link = a('https://faucetpay.io/page/user-admin/linked-addresses',$uas,$data);
		if(preg_match('/Your address has been linked/',$link[1])){
			$linked=$wal.n;
			$save = fopen("Wallet", "a");
			fwrite($save, $linked);
			fclose($save);
			sleep(5);
			echo h.'Success ~> '.k.$wal.n;
		}else{
			echo w("Bot lelah!, Coba update cookie",'m');sleep(10);
			echo "\r                                           \r";
		}
	}
}
function _r(){
	t();
	system("xdg-open ".a[3]."?sub_confirmation=1");x();
	print b();
	echo "1 ".m."> ".k."Linked Wallet".n;
	echo p."2 ".m."> ".k."Run Bot ".a[1].n;
	$p = readline(h."Input Number ".m."> ".p);
	print l();
	if($p==1){
		if(file_exists('Cookie Faucetpay')){
			unlink('Cookie Faucetpay');
		}
		s('Cookie Faucetpay');
		s('User_Agent');
		print b();
		_g();
	}elseif($p==2){
		_m();
	}
}
_r();



