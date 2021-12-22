<?php if (isset($_GET['xss'])) {
   $xss = htmlspecialchars($_GET['xss']);
   $filter = array(")","("); 
   $filteredVector = str_replace($filter,"",$_POST["xss"]);
   die("<img src=$filteredVector>");} ?>
<!DOCTYPE html>
<html><head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
<style>

.code {
resize: none;
width: 500px;
height: 100px;
}

.container {
width: 400px;
margin: auto;
}

.cheatson {
font-size: 12px;
margin: 5px;
}

</style>
</head>
<body>
<div class="container">

<fieldset>
<legend>PHP code to bypass:</legend>
<textarea class="code">if (isset($_GET['xss'])) {
   $xss = htmlspecialchars($_GET['xss']);
   $filter = array(")","("); 
   $filteredVector = str_replace($filter,"",$_POST["xss"]);
   echo("&lt;img src=$filteredVector&gt;");
}</textarea>
</fieldset>

<fieldset>
<legend>create image URL:</legend>
<form action="" method="GET">
<input value="" name="xss" type="text">
</form>
</fieldset>

<p class="cheatson">To filter or not to filter, that is the question!</p>
</div>





<!-- End Of Analytics Code -->
</body></html>
<!-- Hosting24 Analytics Code -->