 <?
        # Checking joomla 1.6 - 1.7 Registration Exploit
        # Coded By : xSecurity
        # Skype : b0x-sa
        # 4u : Mr.Dm4r - Lov3rDNS - DamaneDz - r0kin - b0x - FoX HaCkEr
        @set_time_limit(0);
        echo "<form method='POST'>
        <style>
        textarea
        {
                font-size: 15px;
                font-family: Tahoma;
                color: #0078AA;
                border: dashed 1pt #0078AA;
        }
        input
        {
                color: #0078AA;
                border: dotted 1pt #0078AA;
        }
        </style>
        <title>Checking joomla 1.6 - 1.7 Registration Exploit</title>
        <body text='#808080' bgcolor='#FFFFFF'>
        <p align='center' dir='ltr'><b><br>
        <font face='Tahoma' size='7' color='#0078AA'>C</font><font face='Tahoma' size='5'>hecking</font><font face='Tahoma' size='7'>
        <font color='#0078AA'>R</font></font><font face='Tahoma' size='5'>egistration</font><font face='Tahoma' size='7'>
        <font color='#0078AA'>E</font></font><font face='Tahoma' size='5'>xploit</font></b></p><center>
        <textarea name='sites' cols='50' rows='10'></textarea><br>
        <input type='submit' name='scan' value='Scan Sites'><br>
        </form>";
       
        if($_POST['scan'])
                {
        $site = explode("\r\n",$_POST['sites']);
        foreach($site as $sites)
        {
                $curl = curl_init("{$sites}/index.php?option=com_users&view=registration");
                curl_setopt($curl, CURLOPT_FAILONERROR, true);
                curl_setopt($curl, CURLOPT_FOLLOWLOCATION, true);
                curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
                $result = curl_exec($curl);
                        if(eregi("jform_email2-lbl",$result))
                        {
                                echo "<font face='Comic Sans MS'>
                                <a href='{$sites}/index.php?option=com_users&view=registration' style='text-decoration: none'>{$sites}</a>
                                <font color='green'>Infected</font></font><br>";
                        }
                        else
                        {
                                echo "<font face='Comic Sans MS'>{$sites}
                                <font color='red'>Not Infected</font></font><br>";
                        }
        }
                }
        echo "<p dir='ltr' align='center'><font face='Verdana' size='2'>Coded By : <font color='#0078AA'>xSecurity</font> - Skype : <font color='#0078AA'>b0x-sa </font> <br>
        <span lang='en-us'><b><a href='http://sec4ever.com/'>
        <img border='0' src='http://www.sec4ever.com/home/sec4ever_2.0/images/statusicon/forum_new.png' width='60' height='65'></a><a href='http://is-sec.com/'><img src='http://is-sec.com/vb/images/Is/images/logo-is.png' width='132' height='69'></a></b></span><br>
        4u : <font color='#0078AA'>Mr.Dm4r</font> - <font color='#0078AA'>Lov3rDNS</font> -&nbsp;<font color='#0078AA'>DamaneDz</font> -
        <font color='#0078AA'>r0kin</font> - <font color='#0078AA'>b0x</font> -<font color='#0078AA'> FoX HaCkEr</font></font></p></body>";
?> 