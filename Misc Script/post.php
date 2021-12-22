<?php
$msg = $_GET['w'];
$logfile= 'data.txt';
$fp = fopen($logfile, "a");
fwrite($fp, $msg);
fclose($fp);
?>