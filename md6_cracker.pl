#!/usr/bin/perl
# MD6 Cracker
$dbgtmr = "1";
use Digest::MD6 qw(md6_hex);
use Time::HiRes qw(gettimeofday);
if ($ARGV[0]=~"a") { $alpha = "abcdefghijklmnopqrstuvwxyz";}
if ($ARGV[0]=~"A") { $alpha = $alpha. "ABCDEFGHIJKLMNOPQRSTUVWXYZ"; }
if ($ARGV[0]=~"d") { $alpha = $alpha."1234567890";}
if ($ARGV[0]=~"x") { $alpha = $alpha. "!\"\$%&/()=?-.:\\*'-_:.;,"; }
if ($alpha eq "" or $ARGV[3] eq "") { usage(); } ;
print "Selected charset for attack: '$alpha\'\n";
print "Going to crack '$ARGV[3]'...\n"; for (my $t=$ARGV[1];$t<=$ARGV[2];$t++){ crack ($t); }


sub usage {
print "USAGE\n";
print "./md6crack [charset] [min length] [max length] [hash] \n";
print " Charset can be: [aAdx]\n";
print " a = {'a','b','c',...}\n";
print " A = {'A','B','C',...}\n";
print " d = {'1','2','3',...}\n";
print " x = {'!','\"',' ',...}\n";
}

sub crack{
$CharSet = shift;
@RawString = ();
for (my $i =0;$i<$CharSet;$i++){ $RawString[i] = 0;}
$Start = gettimeofday();
do{
for (my $i =0;$i length($alpha)-1){
if ($i==$CharSet-1){
print "Bruteforcing done with $CharSet Chars. No Results.\n";
$cnt=0;
return false;
}
$RawString[$i+1]++; $RawString[$i]=0;
}
}
$ret = "";
for (my $i =0;$i$dbgtmr){
$cnt = int($cnt/$dbgtmr);
print "$cnt hashes\\second.\tLast Pass '$ret\'\n";
$cnt=0;
$Start = gettimeofday();
}
if ($ARGV[3] eq $hash){
die "\n**** Password Cracked! => $ret\n";
}
$RawString[0]++;
}
while($RawString[$CharSet-1]<length($alpha));
}