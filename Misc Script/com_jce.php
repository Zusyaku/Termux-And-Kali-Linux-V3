<body>
<html>

<p style="text-align: left;">
<img alt="http://up.hotm-il.com/uploads/13483169531.png" class="decoded" src="http://up.hotm-il.com/uploads/13483169531.png" /></p>
<p style="text-align: left;">
    &nbsp;</p>
<div style="text-align: left;">
    <font color="FF0000" size="4">These tool to develop ideas and not attack or penetration, we are here to develop the ethical hacker </font></div>
<br>
<html>
<head>
<style css="text/css">
body {background-color: black}
</style>
</head>
<body>

</body>
</html>

<?php

set_time_limit(0);
function checke($url){
    $login = $url;
    $ch = curl_init();
    curl_setopt($ch,CURLOPT_URL,$login);
    curl_setopt($ch,CURLOPT_USERAGENT,'Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1');
    curl_setopt($ch,CURLOPT_RETURNTRANSFER,true);
    $result = curl_exec($ch);
    curl_close($ch);
    return $result;
    }
function scan($ip)
{
    $dork = "/index.php?option=com";
    $num = 1;
    for($i=1;$i<=10;$i++)
    {
        $text = file_get_contents("http://www.bing.com/search?q=ip%3a{$ip}+{$dork}&go=&qs=ds&filt=all&first={$num}");
        $num = $num + 10;
        preg_match_all('#(<div class="sb_tlst">.*<h3>.*<a href="(.*)".*>(.*)</a>.*</h3>.*</div>)#siU',$text,$m);
        foreach($m[2] as $s)
        {
            $array[] = check($s);
            $dd = array_unique($array);
        }
    }
    return $dd;
}
function check($url)
{
    $url = explode("/index.php?option=com",$url);
    $url = str_replace("www.","",$url);
    $url = str_replace("http://","http://www.",$url);
    return $url[0]."/";
}
if($_POST['ip'])
{
    foreach(scan($_POST['ip']) as $url)
    {
        $dork = "index.php?option=com_jce&task=plugin&plugin=imgmanager&file=imgmanager&method=form&cid=20&6bc427c8a7981f4fe1f5ac65c1246b5f=9d09f693c63c1988a9f8a564e0da7743";
        $text = checke($url.$dork);
        if(eregi('{"result":null,"error":"No function call specified!"}',$text) or eregi('{"result":null,"error":"Cannot call function . Function not registered!"}',$text))
        {
            echo "<a href='{$url}'><font color=green><b>{$url}</b></font></a><br />";
            flush();
        }else{
            echo "<a href='{$url}'><font color=white><b>{$url}</b></font></a><br />";
            flush();
        }
    }
}else{



    echo "<font color=red><b>please enter ip address :</b></font></a><br /><form action='?' method='POST'><input name='ip' type='text' ><br><input type='submit' value='check'></form>";


}
?>
