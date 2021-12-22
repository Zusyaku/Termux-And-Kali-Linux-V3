<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
   <title>Cloudflare Resolver</title>
 
 
   <style type="text/css">
   
      body
      {
         color: #F60;
         text-shadow: 2px 1px #333;
         background-color: #000;
         font-family: Arial, Helvetica, sans-serif;
      }
     
      input
      {
         font-family: Arial, Helvetica, sans-serif;
      }
     
      .Button
      {
         padding: 5px 10px;
         background: #333;
         border: solid #101010 2px;
         color: #F60;
         cursor: pointer;
         font-weight: bold;
         border-radius: 5px;
         -moz-border-radius: 5px;
         -webkit-border-radius: 5px;
         text-shadow: 1px 1px #000;
      }
     
      .Input
      {
         border: solid #101010 1px;
         color: white;
         font-weight: bold;
         padding: 3px;
         background-color: #252525;
      }
    </style>
</head>
<body>
<div align="center">
<pre>
_________ .__                   .___ _____.__                         __________                    .__                    
\_   ___ \|  |   ____  __ __  __| _// ____\  | _____ _______   ____   \______   \ ____   __________ |  |___  __ ___________
/    \  \/|  |  /  _ \|  |  \/ __ |\   __\|  | \__  \\_  __ \_/ __ \   |       _// __ \ /  ___/  _ \|  |\  \/ // __ \_  __ \
\     \___|  |_(  <_> )  |  / /_/ | |  |  |  |__/ __ \|  | \/\  ___/   |    |   \  ___/ \___ (  <_> )  |_\   /\  ___/|  | \/
 \______  /____/\____/|____/\____ | |__|  |____(____  /__|    \___  >  |____|_  /\___  >____  >____/|____/\_/  \___  >__|  
        \/                       \/                 \/            \/          \/     \/     \/                     \/      
Coded By WazabiHD                                                                                       http://bigbang.m-hs.net
</pre>
<form method="POST" action="">
Enter URL :
<input type="text" name="url" class="Input" value="<?php if(isset($_POST['url'])){ echo htmlentities($_POST['url']); } else { echo 'http://example.com';}?>" />
<input type="submit" name="submit" class="Button" value="Resolve" />
</form>
<>
<div align="left">
<?php
 
 
//Cloudflare Resolver coded by WazabiHD

 
 
class Cloudflareresolve
{
   private $arr = array(  'mail.',
                         'direct.',
                         'direct-connect.',
                         'cpanel.',
                         'ftp.',
                         'forum.',
                         'blog.',
                         'm.',
                         'dev.',
                         'webmail.',
                         'record.',
                         'ssl.',
                         'dns.',
                         'help.',
                         'www.');
   
   private function is_valid($url)
   {
      if(filter_var($url, FILTER_VALIDATE_URL))
          return true;
      return false;
   }
   
   private function is_ip($url)
   {
      if(filter_var($url, FILTER_VALIDATE_IP))
          return true;
      return false;
   }
   
   private function detect_cloudflare($url)
   {
      $headers = @get_headers($url);
      if(strstr($headers[1],"cloudflare"))
          return true;
      return false;
   }
   
   private function getip($url)
   {
      return gethostbyname($url);
   }
   
   public function resolve($url)
   {
      if(!$this->is_valid($url))
      {
          echo '<span style="color: #F60;">The entered URL is not a vaild URL</span>';
         exit();
      }
      if(!$this->detect_cloudflare($url))
      {
      $urll = parse_url($url);
      $url = $urll['host'];
      $ip = $this->getip($url);
         echo '<span style="color: #F60;">No cloudflare detected<br /><br />';
         echo 'IP of '.htmlentities($url).' is ';
      if($this->is_ip($ip))
      {
          echo $ip.'</span>';
      }
      else
      {
          echo 'N/A</span>';
      }
         exit();
      }
      echo '<span style="color: #F60;">Cloudflare detected! Trying to resolve<br /><br /></span>';
        $url_p = parse_url($url);
      $url_h = $url_p['host'];
      if(strstr($url_h,'www.'))
      {
         $temp = explode('www.',$url_h);
         $url_h = $temp[1];
      }
      foreach($this->arr as $val)
      {
         $check_url = $val.$url_h;
         echo '<span style="color: #F60;">IP for : '.htmlentities($check_url).' is : ';
         $ip = $this->getip($check_url);
         if($this->is_ip($ip))
         {
             echo $ip;
         }
         else
         {
             echo 'N/A';
         }
         echo '<br /></span>';
      }
   }
}
 
 
if(isset($_POST['url'],$_POST['submit']))
{
   $obj = new Cloudflareresolve();
   $obj->resolve($_POST['url']);
}
?>
<>
</body>
</html>!