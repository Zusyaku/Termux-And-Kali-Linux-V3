#!/usr/bin/perl
#coded by rui ©

use LWP::UserAgent;
my $ua = LWP::UserAgent->new( agent => 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)' );
my $url = 'http://google.com/';

if ((@ARGV < 2) or (@ARGV > 3)) {
usage();
} elsif(@ARGV eq 3) {
print "[+] Google searcher tool by rui\n";
loadf($ARGV[0], $ARGV[1], $ARGV[2]);
} else {
print "[+] Google searcher tool by rui\n";
load($ARGV[0], $ARGV[1]);
}

sub usage() {
print "[+] Google searcher tool by rui\n";
print "[+] Usage: perl google.pl keyword(s) pages [output]\n\n";
print "\t\t-keyword(s) = the keyword(s) you want to search\n";
print "\t\t please put quotes for keywords more than one\n";
print "\t\t-pages = the number of pages you want the tool to include\n";
print "\t\t-output = (optional) the file where you want to put your results\n";
print "[+] Examples: perl google.pl programming 10\n";
print " perl google.pl \"perl programming\" 10\n";
print " perl google.pl perl 10 perl.txt\n";
}

sub load($$) {
my $keyword = $_[0];
my $page = $_[1];
my $pg = 0;
my $i = 0;
print "[+] Keyword(s): " . $keyword . "\n";
print "[+] Page(s): " . $page . "\n";
print "[+] Initializing query, Please wait..\n";
$pg = ($page) * 10;
while($i < $pg) {
my $res = $ua->get($url . 'search?hl=en&q=' . $keyword . '&start=' . $i . '&sa=N');
#print $url . 'search?hl=en&q=' . $keyword . '&start=' . $i . '&sa=N\n';
if($res->is_error) {
die "[-] Connection Error! - " . $res->status_line . "\n";
} else {
my $content = $res->content;
while ($content =~ m/<h3 class=(.*?)><a href=\"(.*?)\" class=(.*?)>/g) {
my $url2 = $2;
print $url2. "\n";
}
}
$i = $i +10;
}
}

sub loadf($$$) {
my $keyword = $_[0];
my $page = $_[1];
my $file = $_[2];
my $pg = 0;
my $i = 0;
print "[+] Keyword(s): " . $keyword . "\n";
print "[+] Page(s): " . $page . "\n";
print "[+] Output: " . $file . "\n";
print "[+] Initializing query, Please wait..\n";
$pg = ($page) * 10;
while($i < $pg) {
my $res = $ua->get($url . 'search?hl=en&q=' . $keyword . '&start=' . $i . '&sa=N');
#print $url . 'search?hl=en&q=' . $keyword . '&start=' . $i . '&sa=N\n';
if($res->is_error) {
die "[-] Connection Error! - " . $res->status_line . "\n";
} else {
my $content = $res->content;
while ($content =~ m/<h3 class=(.*?)><a href=\"(.*?)\" class=(.*?)>/g) {
my $url2 = $2;
print $url2. "\n";
open(LOG,">>" . $file);
print LOG $url2 . "\n";
close(LOG);
}
}
$i = $i +10;
}
}