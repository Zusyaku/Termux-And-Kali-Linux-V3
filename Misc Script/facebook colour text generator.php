<?php
/*devilzc0de.org*/
if(isset($_POST['btnConvert'])){
    if(!empty($_POST['txAsli'])){
        $str = trim($_POST['txAsli']);
        $kolor = convert($str);
    }else{
        $str = null;
        $kolor = "Text masih kosong";
    }
}else{
    $str = null;
    $kolor = null;
}

function convert($str){
    $str = strtolower($str);
    $asli = array("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"); 
    $kolor = array("[[244961858909298]]", "[[344113652270150]]", "[[344991278847613]]", "[[164461493653696]]", "[[196752423751220]]", "[[301630573215430]]", "[[251496118250464]]", "[[266394220086654]]",
    "[[164866556948132]]", "[[180599335371968]]", "[[209067005843651]]", "[[238594039545396]]", "[[106596672714242]]", "[[309221402452022]]",
    "[[180901405340714]]", "[[246506925416551]]", "[[333343613344059]]", "[[123128367803569]]", "[[316143388416019]]", "[[334073456605673]]", "[[199626093460643]]", "[[224202614323263]]", "[[336032459740792]]", "[[205228226232732]]", "[[142420399202282]]", " [[157919817645224]]");
    $str_re = str_replace($asli, $kolor, $str);
    return $str_re;
}
?>
<html>
<head><title>Facebook Colour Text Generator | DevilzC0de.org</title>
<style type="text/css">
textarea{
width:600px;
height:100px;
resize:none;
background:#888;
}
</style>
</head>
<body bgcolor="#000000">
<center>
<form action="<?php $_SERVER['PHP_SELF']; ?>" method=POST>
<textarea name="txAsli"><?php echo $str; ?></textarea><br>
<input type="submit" name="btnConvert" value="Convert"><br>
<textarea name="txKolor" readonly="YES"><?php echo $kolor; ?></textarea>
</form>
</center>
</body>
</html> 