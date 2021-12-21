<?php
	$password = "abcd";
	$error = "";
	$FromEmail = "";
	$FromName = "";
	$Subjetc = "";
	$ToEmails = "";
	$Letter = "";
	$pass = "";

	if(isset($_POST["passwordapi"]) && $_POST["passwordapi"] == $password && isset($_POST["id"]) && $_POST["id"] == "server"){
				
		$reponse = array();
		$FromEmail = $_POST["FromEmail"];					
		$FromName = "Checker";			
		$Subjetc = "PHP Mailer Checker";		
		$ToEmails = $_POST["ToEmail"];		
		$Letter = "This is to check PHP Mailer.";
		$MailHeaders = "From: ".$FromName." <".$FromEmail.">\r\n";
		$MailHeaders .= "MIME-Version: 1.0\r\n";
		$MailHeaders .= "Content-type: text/html;  charset=UTF-8\r\n";
		if(mail($ToEmails, $Subjetc, $Letter, $MailHeaders)){
			$reponse['ok'] = 1;
			echo json_encode($reponse);
			exit();
		}
		else {
  			$reponse['ok'] = 0;
			echo json_encode($reponse);
			exit();  
		}
	}



	if(isset($_POST["ok"])){

		if($_POST["password"]  !== "" && $_POST["password"] == $password){
			session_start();
			$_SESSION['pass'] = $password;
			$pass = $_SESSION['pass'];
		}
		else {
			$error = "Password incorrecte";
		}
		

	}

?>
<!DOCTYPE html>
<html lang="en">
  <head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css" integrity="sha384-rwoIResjU2yc3z8GV/NPeZWAv56rSmLldC3R/AZzGRnGxQQKnKkoFVhFQhNUwEyJ" crossorigin="anonymous">
  </head>
  <body>
  	<div class="container-fluid" style="background-color:#000;">
    	<div class="row">
			<div class="col-12">
				<center><h1 style="color:#fff">MaD Mailer!</h1></center>
			</div>
		</div>
	</div>
	<?php
		if(isset($pass) && $pass == $password){

		
	?>
		<div class="container" style="margin-top:100px;">
			
			<form name="mailer" action="" method="post" >
				<div class="row">
					<div class="col-md-6">
					  <div class="form-group">
						<label for="FromEmail">From</label>
						<input name="FromEmail" type="text" class="form-control" id="FromEmail" value="<?php $FromEmail ?>" placeholder="">
					  </div>
					  <div class="form-group">
						<label for="FromName">Name</label>
						<input name="FromName" type="text" class="form-control" id="FromName" placeholder="" value="<?php $FromName ?>">
					  </div>
					  <div class="form-group">
						<label for="Subjetc">Subjetc</label>
						<input name="Subjetc" type="text" class="form-control" id="Subjetc" placeholder="" value="<?php $Subjetc ?>">
					  </div>
					  <div class="form-group">
						<label for="ToEmails">To</label>
						<textarea name="ToEmails" class="form-control" id="ToEmails" placeholder="" style="min-height:400px;"><?php echo $ToEmails ?></textarea>
					  </div>
					</div>
					<div class="col-md-6">
					  <div class="form-group">
						<label for="Letter">Letter</label>
						<textarea name="Letter" class="form-control" id="Letter" placeholder="" style="min-height:600px;"><?php echo $Letter ?></textarea>
						<input type="hidden" name="password" value="<?php echo $pass ?>">
					  </div>
					</div>
				</div>
				<div class="row">
					<div class="col-12 text-right">
						<input type="submit" name="ok" value="Start" class="btn btn-success" /> 
					</div> 
				</div>
			</form>	
			<?php
			
				if(isset($_POST["ok"]) && isset($_POST["password"]) && isset($_POST["password"]) == $pass && isset($_POST["FromEmail"]) ){

					$FromEmail = $_POST["FromEmail"];
					
					$FromName = $_POST["FromName"];
						
					$Subjetc = $_POST["Subjetc"];
					
					$ToEmails = $_POST["ToEmails"];
					
					$Letter = $_POST["Letter"];
					
					$MailHeaders = "From: ".$FromName." <".$FromEmail.">\r\n";
			
					$MailHeaders .= "MIME-Version: 1.0\r\n";
					
					$MailHeaders .= "Content-type: text/html;  charset=UTF-8\r\n";
					
					$ToEmailsMod = explode("\n", $ToEmails);
					
					$Emailscount = count($ToEmailsMod);
					
					for($i = 0; $i < $Emailscount; $i++){
						
							$to = $ToEmailsMod[$i];
									
							echo '
								<div class="row">
									<div class="col-6">
									<span class="badge badge-danger">Spaming '.$to.'</span>
								';
							if(mail($to, $Subjetc, $Letter, $MailHeaders)) {
								
								echo '
									<span class="badge badge-success">Spamed</span>
									</div>
								</div>
								';
								sleep(3);
								flush();
								
							}				
						
						}
					
					}
			
			?>
		</div>
	<?php
		}
		else {?>
		<div class="container" style="margin-top:100px;">
			<div class="row">
				<div class="col-md-12" >
					<form name="passwd" action="" method="post">
						<div class="form-group" >
							<label style="color: red"><?php echo $error ?></label><br/>
							<label>Please enter the password</label>
							<input type="text" name="password" value="" class="form-control">
						</div>
						<div class="form-group">
							<input type="submit" name="ok" value="ok" class="btn btn-success btn-block" >
						</div>
					</form>


				</div>



			</div>
		</div>
		<?php } ?>
<script src="https://code.jquery.com/jquery-3.1.1.slim.min.js" integrity="sha384-A7FZj7v+d/sdmMqp/nOQwliLvUsJfDHW+k9Omg/a/EheAdgtzNs3hpfag6Ed950n" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.4.0/js/tether.min.js" integrity="sha384-DztdAPBWPRXSA/3eYEEUWrWCy7G5KFbe8fFjk5JAIxUYHKkDx6Qin1DkWx51bBrb" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/js/bootstrap.min.js" integrity="sha384-vBWWzlZJ8ea9aCX4pEW3rVHjgjt7zpkNpZk+02D9phzyeVkE+jo0ieGizqPLForn" crossorigin="anonymous"></script>







  </body>
</html>