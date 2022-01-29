<?php
function Run($url, $httpheader = 0, $post = 0, $proxy = 0){
	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, $url);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
	curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
	curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
	curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);
	curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 30);
	curl_setopt($ch, CURLOPT_COOKIE,TRUE);
	if($post){
		curl_setopt($ch, CURLOPT_POST, true);
		curl_setopt($ch, CURLOPT_POSTFIELDS, $post);
	}
	if($httpheader){
		curl_setopt($ch, CURLOPT_HTTPHEADER, $httpheader);
	}
	if($proxy){
		curl_setopt($ch, CURLOPT_HTTPPROXYTUNNEL, true);
		curl_setopt($ch, CURLOPT_PROXY, $proxy);
	}
	curl_setopt($ch, CURLOPT_HEADER, true);
	$response = curl_exec($ch);
	$httpcode = curl_getinfo($ch);
	if(!$httpcode) return "Curl Error : ".curl_error($ch); else{
		$header = substr($response, 0, curl_getinfo($ch, CURLINFO_HEADER_SIZE));
		$body = substr($response, curl_getinfo($ch, CURLINFO_HEADER_SIZE));
		curl_close($ch);
		return array($header, $body)[1];
	}
}

$url = "https://bestautofaucet.com/session/autofaucet";

$header = [
"user-agent: Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.51 Mobile Safari/537.36",
"cookie: _data_cpc=724-1-1643192040;_gat_gtag_UA_70132428_1=1;HstPt4531111=70;HstPn4531111=25;HstCla4531111=1643188418411;panoramaId_expiry=1643793046659;_data_html=1-1_93-1;HstCns4531111=10;auto={%22email%22:%22purna.iera@gmail.com%22%2C%22coins%22:[%22doge%22%2C%22ltc%22%2C%22dgb%22%2C%22trx%22%2C%22usdt%22%2C%22fey%22%2C%22zec%22%2C%22sol%22]%2C%22mode%22:%22multi%22%2C%22boost%22:%221%22%2C%22payout_mode%22:%22fp%22};HstCnv4531111=6;_gid=GA1.2.31548842.1643186131;session_ok=true;_pk_ses.9.68ce=1;panoramaId=740139e365ce1576fea29ea9ff7516d53938ca1db8c8c3f371a12028e422b41f;__gads=ID=7084fb2207257fdf-22bc7bc2d6cf00ed:T=1641993990:RT=1641993990:S=ALNI_MbJLrkEQztypcjVRXMm2qFQQxLxcQ;_cc_id=9dd80667e3f0c0617c23815b7aec0c39;__dtsu=104016393287892061F867E3E393252C;HstCmu4531111=1641992563903;HstCfa4531111=1641992563903;_ga=GA1.2.2123226202.1641992564;session_new_id=35fd31a80e147ca4ee337c2b20b926fe;session_new=purna.iera@gmail.com;_pk_id.9.68ce=d6aa9d3959910068.1641992458."
];

while(true){
$result = Run($url,$header,$post=true);
$coin1 = explode('<i class="fas fa-coins"></i>',$result)[1];
$coin2 = explode('</div>',$coin1)[0];

echo trim($coin2)."\n";

preg_match_all('#<div class="AutoACell AAC-success">(.*?)<a#is',$result,$hasil);

for($x=0;$x<count($hasil[1]);$x++){
	$has=$hasil[1][$x];
	echo trim($has)."\n";
}
echo str_repeat('~',56)."\n";
for($i=60;$i>0;$i--){
	echo "\r".$i;
	sleep(1);
	echo "\r";
}
}

