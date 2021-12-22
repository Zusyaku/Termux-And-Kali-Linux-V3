<?php
$res = check("username", "password", $info);
if($res){
    echo "Account working: ".$info;
}

function check($logLogin, $logPassword, &$info)
    $url = "https://signup.netflix.com/Login";
    $content = curl($url,"",0,1);
    $token = get_between($content, 'name="authURL" value="', '"');
    $url = "https://signup.netflix.com/Login";
    $data = "authURL=".$token."&email=".urlencode(trim($logLogin))."&password=".urlencode(trim($logPassword));
    $content = curl($url,$data,0,1,"","",0);
    if(preg_match('%does not match an account in our records%', $content)) {
        return 0;
    }else{
        $url = "https://www.netflix.com/YourAccount?lnkctr=mhSS";
        $content = curl($url,"",0,1,"","",0);
        $info = get_between($content, 'plandesc"><strong>', '</strong>');
        return 1;
    }
}

function get_between($string, $start, $end) {
    $string = " ".$string;
    $ini = strpos($string,$start);
    if ($ini == 0) return "";
    $ini += strlen($start);
    $len = strpos($string,$end,$ini) - $ini;
    return substr($string,$ini,$len);
}

function curl($url, $fields="", $ssl = 0, $followLocation = 0, $referer = '', $optUrl = '',  $deleteOldCookies=1) {
    $ch = curl_init($url);
    $header = array();
    $header[0]  = "Accept: text/xml,application/xml,application/xhtml+xml,";
    $header[0] .= "text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5";
    $header[]   = "Cache-Control: max-age=0";
    $header[]   = "Connection: keep-alive";
    $header[]   = "Keep-Alive: 300";
    $header[]   = "Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7";
    $header[]   = "Accept-Language: en-us,en;q=0.5";
    $header[]   = "Pragma: "; // browsers keep this blank.
    curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.1.7) Gecko/20070914 Firefox/2.0.0.7');
    curl_setopt($ch, CURLOPT_HTTPHEADER, $header);
    if($deleteOldCookies){
        file_put_contents("cookie.txt", "");    //Try to delete the preview cookie
    }
    curl_setopt($ch, CURLOPT_COOKIEJAR, "cookie.txt");
    curl_setopt($ch, CURLOPT_COOKIEFILE, "cookie.txt");
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_AUTOREFERER, true);
    if($followLocation){
        curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
    }
    curl_setopt($ch, CURLOPT_URL, $url);
    if($fields){
        curl_setopt($ch, CURLOPT_POST, true);
        curl_setopt($ch, CURLOPT_POSTFIELDS, $fields);
    }else{
        curl_setopt($ch, CURLOPT_POST, false);
    }
    if($referer){
        curl_setopt($ch, CURLOPT_REFERER, $referer);
    }else{
        curl_setopt($ch, CURLOPT_REFERER, $url);
    }
    if($ssl){
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, true);
    }else{
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    }
    if($optUrl){
        curl_setopt ($ch, CURLOPT_URL, $optUrl);
    }
    return curl_exec($ch);
}
?>