<?php
error_reporting(E_ALL^E_NOTICE);
@session_start();
@set_time_limit(0);

//PASSWORD CONFIGURATION

@$passwordlogin = $_POST['pass'];
$chk_login = true;
$passwordloginword = "binushackerfamily";

//END CONFIGURATION

if($passwordlogin == $passwordloginword)
{
 $_SESSION['binushackersfamily'] = "$passwordlogin";
}

if($chk_login == true)
{
 if(!isset($_SESSION['binushackersfamily']) or $_SESSION['binushackersfamily'] != $passwordloginword)
 {
 die("
 <title>.:| Www.BinusHacker.Net - Mass Mailer |:.</title>
 <center>
 <table border=0 cellpadding=0 cellspacing=0 width=100% height=100%>
 <tr><td valign=middle align=center>
 <table width=100 bgcolor=black border=6 bordercolor=#444444>
   <tr><td>
 <font size=1 face=verdana><center>
 <b></font></a><br></b>
 </center>
 <form method=post>
 <font size=1 face=verdana
color=red><strong><center>Mailer</center></strong><br>
 <input type=password name=pass size=30>
 </form>
 <b>Host:</b> ".$_SERVER["HTTP_HOST"]."<br>
 <b>IP:</b> ".gethostbyname($_SERVER["HTTP_HOST"])."<br>
 <b>Your ip:</b> ".$_SERVER["REMOTE_ADDR"]."
 </td></tr></table>
 </td></tr></table>
 ");
 }
}
if(isset($_POST['action'] ) ){
$action=$_POST['action'];
$message=$_POST['message'];
$emaillist=$_POST['emaillist'];
$from=$_POST['from'];
$replyto=$_POST['replyto'];
$subject=$_POST['subject'];
$realname=$_POST['realname'];
$file_name=$_POST['file'];
$contenttype=$_POST['contenttype'];

       $message = urlencode($message);
       $message = preg_replace('/\"/', '"', $message);
       $message = urldecode($message);
       $message = stripslashes($message);
       $subject = stripslashes($subject);
}
?>
<html>
<head>
<title>.:: Mass Mailer | Www.BinusHacker.Net ::.</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">

<style type="text/css">
<!--
.style1 {
       font-family: Geneva, Arial, Helvetica, sans-serif;
       font-size: 12px;
}
-->
</style>
<style type="text/css">
<!--
.style1 {
       font-size: 20px;
       font-family: Geneva, Arial, Helvetica, sans-serif;
}
body {
   background-color: #000000;
}
.style2 {font-family: Georgia, "Times New Roman", Times, serif}
.style3 {
   color: #FF0000;
   font-weight: bold;
}
.style4 {color: #999999}
-->
</style>
</head>
<body text="#ffffff">
<span class="style1">
<center><br>
<img src="http://farm9.staticflickr.com/8185/8377088218_4af8c23105_b.jpg">
</center>
<br></span></p>
<form name="form1" method="post" action="" enctype="multipart/form-data">
       <input type="hidden" name="action" value="send">
       <br>
 <table width="100%" border="0">
   <tr>
     <td width="10%">
       <div align="right"><font size="-3" face="Verdana, Arial,
Helvetica, sans-serif">Email:</font></div>
     </td>
     <td width="18%"><font size="-3" face="Verdana, Arial, Helvetica,
sans-serif">
       <input type="text" name="from" value="<?php print $from; ?>"
size="30">
       </font></td>
     <td width="31%">
       <div align="right"><font size="-3" face="Verdana, Arial,
Helvetica, sans-serif">Nama:</font></div>
     </td>
     <td width="41%"><font size="-3" face="Verdana, Arial, Helvetica,
sans-serif">
       <input type="text" name="realname" value="<?php print $realname;
?>" size="30">
       </font></td>
   </tr>
   <tr>
     <td width="10%">
       <div align="right"><font size="-3" face="Verdana, Arial,
Helvetica, sans-serif">Reply:</font></div>
     </td>
     <td width="18%"><font size="-3" face="Verdana, Arial, Helvetica,
sans-serif">
       <input type="text" name="replyto" value="<?php print $replyto;
?>" size="30">
       </font></td>
     <td width="31%">
       <div align="right"><font size="-3" face="Verdana, Arial,
Helvetica, sans-serif">Attach
         File:</font></div>
     </td>
     <td width="41%"><font size="-3" face="Verdana, Arial, Helvetica,
sans-serif">
       <input type="file" name="file" size="30">
       </font></td>
   </tr>
   <tr>
     <td width="10%">
       <div align="right"><font size="-3" face="Verdana, Arial,
Helvetica, sans-serif">Subject:</font></div>
     </td>
     <td colspan="3"><font size="-3" face="Verdana, Arial, Helvetica,
sans-serif">
       <input type="text" name="subject" value="<?php print $subject;
?>" size="66">
       </font></td>
   </tr>
   <tr>
     <td width="10%" valign="top">
       <div align="right"><font size="-3" face="Verdana, Arial,
Helvetica, sans-serif">Mail:</font></div>
     </td>
     <td width="18%" valign="top"><font size="-3" face="Verdana,
Arial, Helvetica,
sans-serif">
       <textarea name="message" cols="50" rows="10"><?php print
$message; ?></textarea>
       <br>
       <input type="radio" name="contenttype" value="plain">
       Text
       <input name="contenttype" type="radio" value="html" checked>
       HTML
       <input type="submit" value="Send to Inbox">
       </font></td>
     <td width="31%" valign="top">
       <div align="right">
         <font face="Verdana, Arial,
Helvetica, sans-serif" size="-3">Mail  to:</font></div>
     </td>
     <td width="41%" valign="top"><font size="-3" face="Verdana,
Arial, Helvetica, sans-serif">
       <textarea name="emaillist" cols="30" rows="10"><?php print
$emaillist; ?></textarea></font></td>
   </tr>
 </table>
</form>
<?php
if ($action){
       if (!$from && !$subject && !$message && !$emaillist){
       print "Please complete all fields before sending your message.";
       exit;
   }
   $allemails = split("\n", $emaillist);
           $numemails = count($allemails);

         for($x=0; $x<$numemails; $x++){
               $to = $allemails[$x];
               if ($to){
               $to = preg_replace('//', '', $to);
               $message = preg_replace('&email&', $to, $message);
               $subject = preg_replace('&email&', $to, $subject);
               print " $to.......";
               flush();
               $header = "From: $realname <$from>\r\nReply-To: $replyto\r\n";
               $header .= "MIME-Version: 1.0\r\n";
           If ($file_name) $header .= "Content-Type: multipart/mixed;
boundary=$uid\r\n";
             If ($file_name) $header .= "--$uid\r\n";
               $header .= "Content-Type: text/$contenttype\r\n";
               $header .= "Content-Transfer-Encoding: 8bit\r\n\r\n";
               $header .= "$message\r\n";
           If ($file_name) $header .= "--$uid\r\n";
           If ($file_name) $header .= "Content-Type: $file_type;
name=\"$file_name\"\r\n";
           If ($file_name) $header .= "Content-Transfer-Encoding: base64\r\n";
           If ($file_name) $header .= "Content-Disposition:
attachment; filename=\"$file_name\"\r\n\r\n";
           If ($file_name) $header .= "$content\r\n";
           If ($file_name) $header .= "--$uid--";
               mail($to, $subject, "", $header);
               print "Email Terkirim!<br>";
               flush();
               }
               }
}


?>
<style type="text/css">
<!--
.style1 {
   font-size: 20px;
   font-family: Geneva, Arial, Helvetica, sans-serif;
}
-->
</style><center>
<p class="style1 style2 style3 style4"><p class="style1">PHP Mailer<br>
 &copy Www.BinusHacker.Net<br>
     </p>  </p>
</center>
<?php
if(isset($_POST['action']) && $numemails !==0 ){echo
"<script>alert('Sending Completed\\r\\nTotal Email
$numemails\\r\\n-Thanks To BinusHacker Family');
</script>";}
?>
</body>
</html>