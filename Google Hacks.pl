#!/usr/bin/perl
require LWP::UserAgent;
use strict;
my($ua,$quote,$goo,$page,$url,$pagestart,$response ,$con,$link);
my($resultfile,$dork,$output);
$ua = LWP::UserAgent->new;
$ua->agent('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.3) Gecko/20070309 Firefox/2.0.0.4');
$ua->timeout(30);

sub usage{
print "\n\n########## Usage ##########\n";
print "[!] GoogleDorker.pl <dork> <result dump> [output (html|txt)]\n";
print "[Eg] GoogleDorker.pl \"powered by phpbb 2.0.12\" results.txt html\n\n";
exit;
}


if(@ARGV<2){
&usage;
}
if($ARGV[2]){$output = $ARGV[2]};
$dork = $ARGV[0];
$resultfile = $ARGV[1];

#Google stuff
$dork =~ s/ /+/g;
$goo = "http://www.google.com.au/search?hl=en&q=";
$pagestart = "&start=";
$url = $goo . $dork . $pagestart;

print "[+] Dork:\t$dork\n[+] Result file:\t$resultfile\n";
request("0");
sub request{
$page = $_[0];
$response = $ua->get($url . $page);
if($response->is_success){
$con = $response->content;
while ($con =~ m/<h2 class=(.*?)><a href=\"(.*?)\" class=(.*?)>/g){
$link = $2;
if($output eq "html"){$link = "<a href=\"$2\">$2</a><br>";}
print "[+] Found link $2\n";
open(LOG,">>$resultfile\n");
print LOG "$link\n";
close(LOG);
}
if ($con =~ m/<td nowrap class=b><a href=(.*?)&hl=en&start=(.*?)&sa=N\">/){
#Recursing
print "[+] Another page: $2\n";
request($2)
}
}
else{
if($response->status_line =~ m/403/){
print "[e] Forbidden request\n";
exit;
}
else{
print "[e] Connection error\n[e] " . $response->status_line . "\n";
exit;
}
}
}