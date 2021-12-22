Dark Mailer - Upped by Worms - www.RuneRevolution.net

Save it as .php and upload to your webserver

=========================================

<html>
<head>
<title>Dark-Mailer</title>
<style type="text/css">
body { color: #c6c6c6; background-color: #2f2f2f; font-weight:bold; font-family:Arial; font-size:120%;}
.mainbox { background-color:#8C8C8C; padding:6px; margin:0px;border: 1px solid #FF0000;text-align:center; }
.txtbox { vertical-align:top;background-color:#A1A1A1; padding:6px; margin:0px;border: 0px solid #FF0000;text-align:center; }
.title {font:italic bold 16px Helvetica;background-color:#A1A1A1; padding:6px; margin:0px;border: 0px solid #FF0000;text-align:center;}
.txt {font:italic bold 12px Helvetica;color:#8B0000}
.sm {font:italic bold 10px Helvetica;text-align:left;}
.button {background-color : #8C8C8C;color : #000000;font-size: 11px; font-family: Verdana, Arial, Helvetica, sans-serif;border: 1px solid #ffffff}
</style>
<script language="javascript"><!--

function expand()
{
if(document.getElementById('About').style.display=='none')
{
document.getElementById('About').style.display='block';
document.getElementById('greetz').innerHTML = 'Simply fill out the form and press the "Send"-Button.<br>You can attach a file, which will be uploaded to the server, encoded for the Email and then be deleted from the server(If PHP Safe-Mode is not active).<br><br>If you wish, you can spam around by inserting a lot of Email-Adresses and let the script pass through this list about 1000 times ;). Depence on PHP execution time if Safe-Mode\'s on!!!!<br><br>If you type "{email}" in the "Subject" or "Message" field the script will exchange it with the Email-Adresse you typed in the "Your Email" field<br><br>You can set the Email to a plain text Email or a HTML-Email(with or without parsing BBCodes)...good for Phishers ;)<br><br>Supported BBCode-Tags: b,i,u,center,img,url,red,blue,yellow,color,size,quote,quote=<br><br>Now you can try out the new E-Mail Grabber. Type an URL and the Grabber will search for E-Mails on the site. The Grabber is Alpha !!!<br><br><br>GreetingZ go out to all DarkenedCore Members. Dedicated to my sweet darling Enigma23-FC ';
}
else
{
document.getElementById('About').style.display='none';
document.getElementById('greetz').innerHTML = '';
}
}
 //--></script>
<script language="JavaScript" type="text/javascript">
var imageTag = false;
var theSelection = false;
var clientPC = navigator.userAgent.toLowerCase();
var clientVer = parseInt(navigator.appVersion);
var is_ie = ((clientPC.indexOf("msie") != -1) && (clientPC.indexOf("opera") == -1));
var is_nav = ((clientPC.indexOf('mozilla')!=-1) && (clientPC.indexOf('spoofer')==-1)
                && (clientPC.indexOf('compatible') == -1) && (clientPC.indexOf('opera')==-1)
                && (clientPC.indexOf('webtv')==-1) && (clientPC.indexOf('hotjava')==-1));
var is_moz = 0;

var is_win = ((clientPC.indexOf("win")!=-1) || (clientPC.indexOf("16bit") != -1));
var is_mac = (clientPC.indexOf("mac")!=-1);
b_help = "Fat Text: [b]Text[/b] (alt+b)";
i_help = "Cursive Text: [i]Text[/i] (alt+i)";
u_help = "Underlined Text: [u]Text[/u] (alt+u)";
q_help = "Quote: [quote]Text[/quote] (alt+q)";
p_help = "Insert an image: [img]http://Image-URL[/img] (alt+p)";
w_help = "Insert an URL: [url]http://URL[/url] (alt+w)";
s_help = "Font-color: [color=red]Text[/color]";
f_help = "Font-Size: [size=x-small]Small text[/size]";
bbcode = new Array();
bbtags = new Array('[b]','[/b]','[i]','[/i]','[u]','[/u]','[quote]','[/quote]','[code]','[/code]','[list]','[/list]','[list=]','[/list]','[img]','[/img]','[url]','[/url]');
imageTag = false;
function helpline(help) {
	document.darkform.helpbox.value = eval(help + "_help");
}
function getarraysize(thearray) {
	for (i = 0; i < thearray.length; i++) {
		if ((thearray[i] == "undefined") || (thearray[i] == "") || (thearray[i] == null))
			return i;
		}
	return thearray.length;
}
function arraypush(thearray,value) {
	thearray[ getarraysize(thearray) ] = value;
}
function arraypop(thearray) {
	thearraysize = getarraysize(thearray);
	retval = thearray[thearraysize - 1];
	delete thearray[thearraysize - 1];
	return retval;
}
function bbfontstyle(bbopen, bbclose) {
	var txtarea = document.darkform.message;

	if ((clientVer >= 4) && is_ie && is_win) {
		theSelection = document.selection.createRange().text;
		if (!theSelection) {
			txtarea.value += bbopen + bbclose;
			txtarea.focus();
			return;
		}
		document.selection.createRange().text = bbopen + theSelection + bbclose;
		txtarea.focus();
		return;
	}
	else if (txtarea.selectionEnd && (txtarea.selectionEnd - txtarea.selectionStart > 0))
	{
		mozWrap(txtarea, bbopen, bbclose);
		return;
	}
	else
	{
		txtarea.value += bbopen + bbclose;
		txtarea.focus();
	}
	storeCaret(txtarea);
}


function bbstyle(bbnumber) {
	var txtarea = document.darkform.message;

	txtarea.focus();
	donotinsert = false;
	theSelection = false;
	bblast = 0;

	if (bbnumber == -1) { 
		while (bbcode[0]) {
			butnumber = arraypop(bbcode) - 1;
			txtarea.value += bbtags[butnumber + 1];
			buttext = eval('document.post.addbbcode' + butnumber + '.value');
			eval('document.post.addbbcode' + butnumber + '.value ="' + buttext.substr(0,(buttext.length - 1)) + '"');
		}
		imageTag = false;
		txtarea.focus();
		return;
	}

	if ((clientVer >= 4) && is_ie && is_win)
	{
		theSelection = document.selection.createRange().text;
		if (theSelection) {
			document.selection.createRange().text = bbtags[bbnumber] + theSelection + bbtags[bbnumber+1];
			txtarea.focus();
			theSelection = '';
			return;
		}
	}
	else if (txtarea.selectionEnd && (txtarea.selectionEnd - txtarea.selectionStart > 0))
	{
		mozWrap(txtarea, bbtags[bbnumber], bbtags[bbnumber+1]);
		return;
	}
	for (i = 0; i < bbcode.length; i++) {
		if (bbcode[i] == bbnumber+1) {
			bblast = i;
			donotinsert = true;
		}
	}

	if (donotinsert) { 
		while (bbcode[bblast]) {
				butnumber = arraypop(bbcode) - 1;
				txtarea.value += bbtags[butnumber + 1];
				buttext = eval('document.darkform.addbbcode' + butnumber + '.value');
				eval('document.darkform.addbbcode' + butnumber + '.value ="' + buttext.substr(0,(buttext.length - 1)) + '"');
				imageTag = false;
			}
			txtarea.focus();
			return;
	} else { 

		if (imageTag && (bbnumber != 14)) {
			txtarea.value += bbtags[15];
			lastValue = arraypop(bbcode) - 1;
			document.post.addbbcode14.value = "Img";
			imageTag = false;
		}

		
		txtarea.value += bbtags[bbnumber];
		if ((bbnumber == 14) && (imageTag == false)) imageTag = 1;
		arraypush(bbcode,bbnumber+1);
		eval('document.darkform.addbbcode'+bbnumber+'.value += "*"');
		txtarea.focus();
		return;
	}
	storeCaret(txtarea);
}

function mozWrap(txtarea, open, close)
{
	var selLength = txtarea.textLength;
	var selStart = txtarea.selectionStart;
	var selEnd = txtarea.selectionEnd;
	if (selEnd == 1 || selEnd == 2)
		selEnd = selLength;

	var s1 = (txtarea.value).substring(0,selStart);
	var s2 = (txtarea.value).substring(selStart, selEnd)
	var s3 = (txtarea.value).substring(selEnd, selLength);
	txtarea.value = s1 + open + s2 + close + s3;
	return;
}
function storeCaret(textEl) {
	if (textEl.createTextRange) textEl.caretPos = document.selection.createRange().duplicate();
}
//-->
</script>

</head>
<body>
<center> <table align="center" class="mainbox" width="70%"><tr><td valign="top">

	<div class="title"><font color="#CD0000">Dark-Mailer V.2.2 &copy by p0LYM0rPH2012 and ZyphoMud DarkenedCore Admin Team</font></div>
<font class="txt">
<?php

function checkmail($a)
{

    $a=explode('@',strtolower($a));

	if(count($a)==2)
  {
			$b=explode('.',$a[1]);
			if(($c=count($b))>1)
        {
            $b[]=$a[0];
            $c++;
				for($i=0;$i<$c;$i++)
            {
							$a=strlen($b[$i]);
							if($a>1)
                    	for($j=0;$j<$a;$j++)
                        {
                        			$d=ord($b[$i]{$j});
											 if(($d>47 && $d<58) || ($d>97 && $d<123));
                        			elseif($j==0) return FALSE;
                       				elseif($d==45 || $d==95);
                        			elseif($i==(count($b)-1) && $d==46);
                        			else           return FALSE;
                        }
                		else    return FALSE;
             }
        }
        else    return FALSE;
   }
    else    return FALSE;

    return TRUE;
    }

function bbcodes($text)
  {
     $new = stripslashes($text);
     $new = preg_replace("/\[img\](.*)\[\/img\]/isU", "<img src=\"$1\" border='0' />", $new);
     $new = preg_replace("/\[center\](.*)\[\/center\]/isU", "<center>$1</center>", $new);
     $new = preg_replace("/\[b\](.*)\[\/b\]/isU", "<b>$1</b>", $new);
     $new = preg_replace("/\[i\](.*)\[\/i\]/isU", "<i>$1</i>", $new);
     $new = preg_replace("/\[u\](.*)\[\/u\]/isU", "<u>$1</u>", $new);
     $new = eregi_replace("([ \r\n])www\\.([^ ,\r\n]*)","\\1http://www.\\2",$new);
     $new = eregi_replace("([ \r\n])http\:\/\/www\\.([^ ,\r\n]*)","\\1http://www.\\2",$new);
     $new = preg_replace("/\[url\]www.(.*)\[\/url\]/isU", "http://www.$1", $new);
     $new = preg_replace("/\[url\](.*)\[\/url\]/isU", "<a href='$1' target='_blank'>$1</a>", $new);
     $new = preg_replace("/\[red\](.*)\[\/red\]/isU", "<font color='red'>$1</font>", $new);
     $new = preg_replace("/\[blue\](.*)\[\/blue\]/isU", "<font color='blue'>$1</font>", $new);
     $new = preg_replace("/\[yellow\](.*)\[\/yellow\]/isU", "<font color='yellow'>$1</font>", $new);
     $new = preg_replace("/\[size=(.*)\](.*)\[\/size\]/isU", "<font size='$1'>$2</font>", $new);
     $new = preg_replace("/\[color=(.*)\](.*)\[\/color\]/isU", "<font color='$1'>$2</font>", $new);
     $new = preg_replace("/\[quote\](.*)\[\/quote\]/isU", "<table border='1' cellspacing='0' cellpadding='2' bgcolor='EFEFEF' width='95%' align='center'><tr><td>$1</tr></td></table>", $new);
     $new = preg_replace("/\[quote=(.*)\](.*)\[\/quote\]/isU", "<table border='1' cellspacing='0' cellpadding='2' bgcolor='EFEFEF' width='95%' align='center'><tr><td><i>Quote from $1:</i><br><br>$2</tr></td></table>", $new);
     $new = nl2br($new); 
	return $new;
  }	
	$to = $_POST['to'];
	$mails = split("\n",$to); 
	$from = $_POST['from'];
	$Reply = $_POST['reply'];
	$subject = $_POST['subject'];
	if(get_magic_quotes_gpc ())
	{
	$Message = stripslashes($_POST['message']);
	}
	else
	{
	$Message = $_POST['message'];
	}
	$sendername = $_POST['sendername'];
	$contenttype = $_POST['ctype'];
	
	if($_POST['ctype'] == "bbhtml"){
		        $contenttype = "html";$Message = bbcodes($Message);}
	else
		        $contenttype = $_POST['ctype'];


	$passthrough = $_POST['count'];
	$Message = str_replace("{email}", $from, $Message); 
	$subject = str_replace("{email}", $from, $subject); 
	
	
	if(isset($_POST['submit']))
	{
	
		if($_FILES["file"]["tmp_name"] != "" &&  $_FILES["file"] != " ")
		{
			$UPLOAD = 1;
			$Filename = $_FILES["file"]["tmp_name"];
			$FilenameMail = $_POST['fakefilename'];
			$FileType= $_FILES["file"]["type"];
			@chmod("./",777);
			move_uploaded_file($Filename, "./$FilenameMail") or die("The file you are trying to upload couldn't be copied to the server. Maybe no R/W Access?"); 
			$content = fread(fopen($FilenameMail,"r"),filesize($FilenameMail)); 
			$content = chunk_split(base64_encode($content)); 
			
		}


	$Header = "From: $sendername <$from>\r\nReply-To: $Reply\r\n";

	$uid = strtoupper(md5(uniqid(time())));
	$header = "From: $sendername <$from>\r\nReply-To: $Reply\r\n"; 
	$header .= "MIME-Version: 1.0\r\n"; 
	If ($UPLOAD) $header .= "Content-Type: multipart/mixed; boundary=$uid\r\n"; 
	If ($UPLOAD) $header .= "--$uid\r\n"; 
	$header .= "Content-Type: text/$contenttype\r\n"; 
	$header .= "Content-Transfer-Encoding: 8bit\r\n\r\n"; 
	$header .= "$Message\r\n"; 
	If ($UPLOAD) $header .= "--$uid\r\n"; 
	If ($UPLOAD) $header .= "Content-Type: $FileType; name=\"$FilenameMail\"\r\n"; 
	If ($UPLOAD) $header .= "Content-Transfer-Encoding: base64\r\n"; 
	If ($UPLOAD) $header .= "Content-Disposition: attachment; filename=\"$FilenameMail\"\r\n\r\n"; 
	If ($UPLOAD) $header .= "$content\r\n"; 
	If ($UPLOAD) $header .= "--$uid--"; 
	@unlink ($FilenameMail);
	$count = 0;

	do
	{
		foreach($mails as $mail)
		{
			@set_time_limit(10);
			if($mail != "" && $mail != " ")
			{
				echo "Sending Mail to ".$mail."...\n\r<br>"; 
				flush();
				mail($mail, $subject, "", $header);

				$count++;
			}
		}
		$passthrough--;
	}while($passthrough != 0);
	echo "<b>".$count." Mail(s) sent</b><br><br>";
	echo "<a href='".$_SERVER['PHP_SELF']."'> Back</a>";
	if(file_exists ("DMPReview.html"))
		@unlink("DMPReview.html");
?>
</font>
</td></tr></table></center> 
<center><font color="white" size="-2">Dark-Mailer V.2.2 by p0LYM0rPH2012 and ZyphoMud from DarkenedCore Admin Team</font></center>
</body>
</html>
<?php
	}
	else
	{
		if(isset($_POST['preview']))
		{
		echo "<br>Preview:<br><br><div style=\"background-color:#ffffff;text-align:left;\"><font color='#000000'>";
		if($_POST['ctype'] == "plain")
			echo nl2br(htmlentities($Message));
		elseif($_POST['ctype'] == "html" || $_POST['ctype'] == "bbhtml")
		{
			if($_POST['ctype'] == "bbhtml") bbcodes($Message);
			if(ini_get('safe_mode') )
				echo $Message;
			else
			{	$fhndl = @fopen("DMPReview.html", "w+");
				if(!$fhndl)
				{
					echo $Message;
				}
				else
				{
					$bytes = @fwrite ($fhndl, $Message);
					if($bytes == false)
					{
						echo $Message;
					}
					else
					{
						fclose($fhndl);
						echo "<center><iframe width=\"700\" height=\"500\" style=\"border:1px solid #000000;\" src=\"DMPReview.html\"></iframe></center>";
					
					}
				}
			}
		
		}
		echo "</font></div><br><br>";
                }
                
    if(isset($_POST['search']))
	{
			$not = '^()<>[\]:;\\\, "@.'.chr(012).chr(015);
			$search = '/['.$not.'](\.{0,1}['.$not.'])*@['.$not.'](\.{0,1}['.$not.'])*(\.[a-z]{2,4})/i';
			//$search = '/[^. @](\.{0,1}[^. @])*@[^. @](\.{0,1}[^. @])*((\.[a-z]{2,4}){1,2}|\.museum)/i';
			$Page = $_POST['sURL'];
			ini_set('default_socket_timeout',    200);
			$Content = strtolower(file_get_contents($Page));
			//echo $Content;
			$blub = preg_match_all( $search, $Content, $matches,PREG_PATTERN_ORDER);
			
			$_POST['to'] = "";
			$ARRAY = array();
			$Search = array("=","href","mailto:","<",">","\"","face","arial","helvetica",",");

			foreach($matches[0] as $Email)
			{
					$Email1 = str_replace($Search,"",$Email);
					if(!in_array($Email1,$ARRAY))
					{
							$_POST['to'] .= $Email1."\n";
							array_push($ARRAY, $Email1);
					}
					//echo $Email1."<br>";
			
			
			}
	}



?><div class="sm"><center>
	<?php
	if( ini_get('safe_mode') )
    		echo "<font color='red'>PHP Safe-Mode is ON</font>";
	else
    		echo "<font color='green'>PHP Safe-Mode is OFF</font>&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;";

	echo "Chmod: <font color='red'>0".substr(sprintf("%o",fileperms(".")),-3)."</font>";
	
		
	?></center>
	</div>
	<form name="darkform" method="post" action="" enctype="multipart/form-data"> 
	<center><table><tr><td class="txtbox">
	<font class="txt">Your Name:</font><br><input name="sendername" value="<? echo $_POST['sendername']; ?>" size="30" >
	</td><td class="txtbox">
	<font class="txt">Your Email:</font><br><input name="from" value="<? echo $_POST['from']; ?>" size="30" >
	</td></tr>
	<tr><td class="txtbox">
	<font class="txt">Reply to:</font><br><input name="reply" value="<? echo $_POST['reply']; ?>" size="30" >
	</td><td class="txtbox">
	<?php
	if( ini_get('safe_mode') )
    	{
		echo "<font class=\"txt\">No attachment possible because of PHP Safe-Mode</font>";
	}
	else
	{
	?>
		<font class="txt">Attachment:</font><br><input type="file" name="file" size="20" >
	<?php
	}
	?>
	
	</td></tr><tr><td class="txtbox">
	<font class="txt">Subject:</font><br><input name="subject" value="<? echo $_POST['subject']; ?>" size="30" >
	</td><td class="txtbox">
	<?php
	if( ini_get('safe_mode') )
    	{
		echo "<font class=\"txt\">No attachment possible because of PHP Safe-Mode</font>";
	}
	else
	{
	?>
		<font class="txt">FakeFileName:</font><br><input name="fakefilename" value="<? echo $_POST['fakefilename']; ?>" size="30" >
	<?php
	}
	?>
	
	</td><tr></table>
	<table><tr><td class="txtbox">
	<font class="txt">Message:</font><br>
	<div>
		<input class="button" accesskey="b" name="addbbcode0" value=" B " style="font-weight: bold; width: 30px;" onclick="bbstyle(0)" onmouseover="helpline('b')" type="button">
		<input class="button" accesskey="i" name="addbbcode2" value=" i " style="font-style: italic; width: 30px;" onclick="bbstyle(2)" onmouseover="helpline('i')" type="button">
		<input class="button" accesskey="u" name="addbbcode4" value=" u " style="text-decoration: underline; width: 30px;" onclick="bbstyle(4)" onmouseover="helpline('u')" type="button">
		<input class="button" accesskey="q" name="addbbcode6" value="Quote" style="width: 50px;" onclick="bbstyle(6)" onmouseover="helpline('q')" type="button">
		<input class="button" accesskey="p" name="addbbcode14" value="Img" style="width: 40px;" onclick="bbstyle(14)" onmouseover="helpline('p')" type="button">
		<input class="button" accesskey="w" name="addbbcode16" value="URL" style="text-decoration: underline; width: 40px;" onclick="bbstyle(16)" onmouseover="helpline('w')" type="button">
		<br><font class="txt">&nbsp;Font color:</font>
		<select name="addbbcode18" onchange="bbfontstyle('[color=' + this.form.addbbcode18.options[this.form.addbbcode18.selectedIndex].value + ']', '[/color]');this.selectedIndex=0;" onmouseover="helpline('s')">
			<option style="color: black; background-color: rgb(250, 250, 250);" value="#444444" class="genmed">Standard</option>
			<option style="color: darkred; background-color: rgb(250, 250, 250);" value="darkred" class="genmed">Darkred</option>
			<option style="color: red; background-color: rgb(250, 250, 250);" value="red" class="genmed">Red</option>

			<option style="color: orange; background-color: rgb(250, 250, 250);" value="orange" class="genmed">Orange</option>
			<option style="color: brown; background-color: rgb(250, 250, 250);" value="brown" class="genmed">Brown</option>
			<option style="color: yellow; background-color: rgb(250, 250, 250);" value="yellow" class="genmed">Yellow</option>
			<option style="color: green; background-color: rgb(250, 250, 250);" value="green" class="genmed">Green</option>
			<option style="color: olive; background-color: rgb(250, 250, 250);" value="olive" class="genmed">Olive</option>
			<option style="color: cyan; background-color: rgb(250, 250, 250);" value="cyan" class="genmed">Cyan</option>

			<option style="color: blue; background-color: rgb(250, 250, 250);" value="blue" class="genmed">Blue</option>
			<option style="color: darkblue; background-color: rgb(250, 250, 250);" value="darkblue" class="genmed">Darkblue</option>
			<option style="color: indigo; background-color: rgb(250, 250, 250);" value="indigo" class="genmed">Indigo</option>
			<option style="color: violet; background-color: rgb(250, 250, 250);" value="violet" class="genmed">Violet</option>
			<option style="color: white; background-color: rgb(250, 250, 250);" value="white" class="genmed">White</option>
			<option style="color: black; background-color: rgb(250, 250, 250);" value="black" class="genmed">Black</option>
		</select> 
		&nbsp;<font class="txt">Font size:</font>
		<select name="addbbcode20" onchange="bbfontstyle('[size=' + this.form.addbbcode20.options[this.form.addbbcode20.selectedIndex].value + ']', '[/size]')" onmouseover="helpline('f')">
			<option value="7" class="genmed">Smaller</option>
			<option value="9" class="genmed">Smal</option>
			<option value="12" selected="selected" class="genmed">Normal</option>
			<option value="18" class="genmed">Big</option>
			<option value="24" class="genmed">Giant</option>
		</select>
	</div><br>
	<center><input class="button" name="helpbox" size="70" maxlength="100" readonly></center>
	<textarea name="message" cols="70" rows="12" onselect="storeCaret(this);" onclick="storeCaret(this);" onkeyup="storeCaret(this);"><? if (get_magic_quotes_gpc()) print stripslashes($_POST['message']);else print $_POST['message'];?></textarea><br>
	<input type="radio" name="ctype" value="plain" <? if($_POST['ctype'] == "plain" || !isset($_POST['ctype'])) echo "checked"; ?>> 
	<font class="txt">Plain</font> 
	<input type="radio" name="ctype" value="html" <? if($_POST['ctype'] == "html") echo "checked"; ?>> 
	<font class="txt">HTML</font> 
	<input type="radio" name="ctype" value="bbhtml" <? if($_POST['ctype'] == "bbhtml") echo "checked"; ?>> 
	<font class="txt">BBCode (HTML)</font> 
	<input type="submit" name="submit" value="Send">
	<input type="submit" name="preview" value="Preview">  	
	</td><td class="txtbox">
	<font class="txt">Emails(each separated by a line break):</font><br>
	<textarea name="to" cols="30" rows="10"><? print $_POST['to']; ?></textarea><br>
	<font class="txt">Pass through list <input name="count" value="1" size="1" > times</font><br><br>
	<font class="txt">Search URL for E-Mails(Alpha-Version) <input name="sURL" value="<? if(isset($_POST['sURL'])) echo $_POST['sURL']; else echo "http://";?>" size="30" ></font><br>
	<input type="submit" name="search" value="Search">	
	</td></tr></table>	
	</center>
<p align="left">
<a href="javascript:expand()" class="txt">READ ME</a></p><div id="About" style="display:none">
<a href="../index.php">Return to vnLoader</a>
<p align="left">
<font class="txt" id="greetz">
</font>
</p>
</div>

</td></tr></table></center> 
<center><font color="white" size="-2">Dark-Mailer V.2.2 powered by p0LYM0rPH2012 aka Nemesis23-FC </font></center>
</body>
</html>
<?php
}
?>

