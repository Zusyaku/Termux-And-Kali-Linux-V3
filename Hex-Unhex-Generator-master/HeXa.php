<?php
// Codex By Rands@22XploiterCrew
if(isset($_POST["ubah"])){
	$text1 = $_POST["hex"];
	$hex 	 = bin2hex($text1);
if($text1 == ""){
	echo "<script>alert('Tidak Ada Karakter Yang Di Inputkan')</script>";
	}else{
		$hex = $hex;
	}
}else if(isset($_POST["str"])){
	$has 	 = $_POST["strl"];
	$hex1  = pack("H*", $has);
if($has == 1){
		$hex1 = $hex1;
	}
}

?>
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=0.75, shrink-to-fit=no">
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
    <title>HexCode Tools</title>
  </head>
  <body>
  	
    <div class="container mt-4">
    <h2 class="text-center">< HexCode Tools /></h2>
<form method="post" >
	<textarea name="hex" class="form-control mb-3" rows="10"><?= $hex1; ?></textarea>
	<center>
	<button type="submit" name="ubah" class="btn btn-primary">Hex</button>
		&nbsp;
	<button type="submit" name="str" class="btn btn-primary">Unhex</button>
	</center>
	<textarea class="form-control mt-3" rows="10" name="strl"><?= $hex; ?></textarea>
</form>
    </div>
    
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+-965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+-8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+-2+-9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+-MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
  </body>
</html>
