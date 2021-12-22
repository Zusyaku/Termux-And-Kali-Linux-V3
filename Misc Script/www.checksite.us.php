<?php

include_once("flood_check.php");

//$agent = $_SERVER['HTTP_USER_AGENT'];

//if ($agent == "Opera/9.80 (Windows NT 6.2; Win64; x64) Presto/2.12.388 Version/12.15") {
  //  header('Location: http://checksite.us/cgi-bin/');
	//exit();
//}

?>



<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>CheckSite.us - Check to see if a website is down for you or for everyone.</title>
<link rel="shortcut icon" href="favicon.ico" />
<meta name="description" content="Check if a website is down for you or for everyone - free and quick service let's you check a site to see if it really is down." />
<meta name="keywords" content="checksite, down, check, url, domain, service, specific, down, http, attempt, accessing, report, website, addresses, similar, problems, monitoring, down" />
<meta name="robots" content="noindex, nofollow" />
<script src="http://www.checksite.us/src/prototype.js" type="text/javascript"></script>
<script src="http://www.checksite.us/src/scriptaculous.js" type="text/javascript"></script>
<script src="http://www.checksite.us/src/functions.js" type="text/javascript"></script>
<link href="http://www.checksite.us/style.css" rel="stylesheet" type="text/css"/>
<meta name="google-site-verification" content="2ofhlsqSlkWkcABkao59BgtnDuanoh4US-T_MLRAMK0" />
</head>

<body>
<div id="container">
<div id="search">
<h1><a href="http://www.checksite.us">CheckSite.us</a> - Site Check</h1>
<?PHP

$www = trim($_GET["url"]);

if (isset($url)) {

require('functions.php');



$url=preg_replace("/(http:\/\/|https:\/\/|ftp:\/\/)/i",'',$www);

echo "<form method=\"get\" action=\"\" name=\"form\">\n";
echo "<fieldset>\n";
echo "<label for=\"url\">http://</label>\n";
echo "<input type=\"text\" name=\"url\" value=\"$url\" style=\"width: 31em;\" />\n";
echo "<input type=\"submit\" value=\"Check This Site\" />\n";
echo "</fieldset>\n";
echo "</form>\n";


if (preg_match("/^[A-Za-z0-9\-_]+\\.+[A-Za-z0-9\.\/~%:&=\?\-_]+$/i", $url)) { 



//$myFile = "/home/check/public_html/log/www-log.txt";
//$fh = fopen($myFile, 'a') or die("can't open file");
//$stringData = "$url\n";
//fwrite($fh, $stringData);
//fclose($fh);

$domain = get_domain($url);
$domain_status = checkdomain($domain);
$status = $domain_status['available'];


//if($status == "1") {
  //  echo "\n\n";
	//echo "<div class=\"results\">The domain <em>$domain</em> is not registered.<br /><br /><div id=\"displayText\"><a href='http://www.namecheap.com/?aff=52919' target='_blank' title='Cheap Domains through NameCheap'>Register it today with free WhoisGuard Privacy Protection through Namecheap.com! <br /><br />
  // </div>\n";
//echo "\n\n";
//	echo "</div><p>&nbsp;</p>\n";
if ($url == "checksite.us" | $url == "www.checksite.us" | $url == "www.Checksite.us" | $url == "downforeveryone.net" | $url == "www.downforeveryone.net") {
         echo "\n\n";
	echo "<div class=\"results\">Yea.. our site is working...<br />(did you really just try checking our own site?)</div>\n";
	echo "\n\n";
	echo "</div><p>&nbsp;</p>\n";
	
} elseif ($url =="127.0.0.1") {
  echo "\n\n";
	echo "<div class=\"results\">Tsk..tsk..tsk.. 127.0.0.1 points back to us!</div>\n";
	echo "\n\n";
	echo "</div><p>&nbsp;</p>\n";
} else {
	echo "\n\n";
	echo check_url($url);
        echo "\n\n";
	echo "</div><p>&nbsp;</p>\n";
}

}elseif (empty($url)) {
    echo "\n\n";
	echo "<div class=\"results\">You didn't enter a URL. We can't check invisible URLs!</div>\n";
	echo "\n\n";
	echo "</div><p>&nbsp;</p>\n";
} else {
   echo "\n\n";
	echo "<div class=\"results\">Hmm.. <u>$www</u> does not appear to be properly formatted.<br /><br />Please try again.</div>\n";
	echo "\n\n";
	echo "</div><p>&nbsp;</p>\n";
  }

} else {

?>
<form method="get" action="/" name="form">
              <fieldset>
				<label for="url">http://</label>
					<input type="text" name="url" id="url" value="www.google.com" onfocus="if (this.value == 'www.google.com') {this.value = '';}" onblur="if (this.value == '') {this.value = 'www.google.com';}" style="width: 31em;" />
					<input type="submit" value="Check This Site"  />
				</fieldset>
			</form>

</div>
<div id="about">
<h3>About This Service</h3>
CheckSite.us is a simple service that allows a user to check to see if a site is actually down, or if it is just the user's machine or network. If you are experiencing problems accessing a specific website, simply enter the website's URL in the form above, and CheckSite.us will attempt to access the URL provided and report back on whether it was able to access the website or not. <br /><br /> Unlike other similar services, our service allows you to enter a domain (i.e. checksite.us), a full length URL (i.e. checksite.us/test.htm), or a domain with a specific port (i.e. checksite.us:2082). We also allow IP addresses to  be used in place of a domain name (i.e. 209.41.89.150:2082). <br /><br /> For websites that we cannot access, we'll continue trying the website every 15 minutes for up to 3 days. If we are successful at accessing the website, we'll send you an e-mail. We also offer SMS Notifications (still in beta. Standard text message rates apply). <br /><br /> 
<strong>NEW!</strong>: You can now be notified through your Twitter account. Just enter your Twitter handle and we'll let you know when we can access the site.
<p>&nbsp;</p>
</div>

<?php
} // end if
?>

<div id="ads">
<!--/* OpenX Javascript Tag v2.8.11 */-->


<script type='text/javascript'><!--//<![CDATA[
   var m3_u = (location.protocol=='https:'?'https://ads.yourip.us/www/delivery/ajs.php':'http://ads.yourip.us/www/delivery/ajs.php');
   var m3_r = Math.floor(Math.random()*99999999999);
   if (!document.MAX_used) document.MAX_used = ',';
   document.write ("<scr"+"ipt type='text/javascript' src='"+m3_u);
   document.write ("?zoneid=3");
   document.write ('&amp;cb=' + m3_r);
   if (document.MAX_used != ',') document.write ("&amp;exclude=" + document.MAX_used);
   document.write (document.charset ? '&amp;charset='+document.charset : (document.characterSet ? '&amp;charset='+document.characterSet : ''));
   document.write ("&amp;loc=" + escape(window.location));
   if (document.referrer) document.write ("&amp;referer=" + escape(document.referrer));
   if (document.context) document.write ("&context=" + escape(document.context));
   if (document.mmm_fo) document.write ("&amp;mmm_fo=1");
   document.write ("'><\/scr"+"ipt>");
//]]>--></script><noscript><a href='http://ads.yourip.us/www/delivery/ck.php?n=a79644b8&amp;cb=INSERT_RANDOM_NUMBER_HERE' target='_blank'><img src='http://ads.yourip.us/www/delivery/avw.php?zoneid=3&amp;cb=INSERT_RANDOM_NUMBER_HERE&amp;n=a79644b8' border='0' alt='' /></a></noscript>
<br />
<br />
</div>

<div id="footer"><a href="http://www.checksite.us">Home</a> &bull;
<a href="contact.ch">Contact</a>  	&bull; 
<a href="http://www.yourip.us">YourIP.us</a> &bull; <a href="http://www.reverseip.us">ReverseIP.us</a> &bull; 
<a href="javascript:addProvider('http://www.checksite.us/search.xml')">Add to Firefox/IE Search Bar</a>
<p>
<a href="https://twitter.com/share" class="twitter-share-button" data-url="http://www.checksite.us" data-text="Checkout this Website! It will check if a website is down and notify you once it comes back online!" data-via="ChecksiteUS">Tweet</a>
<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');</script><su:badge layout="2"></su:badge><script type="text/javascript">
  (function() {
    var li = document.createElement('script'); li.type = 'text/javascript'; li.async = true;
    li.src = ('https:' == document.location.protocol ? 'https:' : 'http:') + '//platform.stumbleupon.com/1/widgets.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(li, s);
  })();
</script></p>

</div>

<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-43682029-2', 'checksite.us');
  ga('send', 'pageview');

</script>

<!-- Start Quantcast tag -->
<script type="text/javascript">
_qoptions={
qacct:"p-64lh4C0KuT_ME"
};
</script>
<script type="text/javascript" src="http://edge.quantserve.com/quant.js"></script>
<noscript>
<img src="http://pixel.quantserve.com/pixel/p-64lh4C0KuT_ME.gif" style="display: none;" border="0" height="1" width="1" alt="Quantcast"/>
</noscript>
<!-- End Quantcast tag -->

</div>


</html>