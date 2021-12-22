<?php
//Coded by Nofear1999
error_reporting(0);
$host = $_SERVER['REMOTE_ADDR'];
echo PHP_VERSION;
$check = fsockopen($host,'80',$errno,$errstr,1);
$check2 = fsockopen($host,'8080',$errno,$errstr,1);
$check3 = fsockopen($host,'3128',$errno,$errstr,1);
if($check or $check2 or $check3)
{
fclose($check);
fclose($check2);
fclose($check3);
die("You cannot do this function because you're accessing this webpage via a proxy."); //Replace this with your no access code.
}

Echo("Access granted");

?>