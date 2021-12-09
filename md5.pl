#!/usr/bin/perl

$blue="\033[1;34";
$cyan="\033[1;36m";
$green="\033[1;34m";
$okegreen="\033[92m";
$lightgreen="\033[1;32m";
$white="\033[1;37m";
$purple="\033[1;35m";
$red="\033[1;31m";
$yellow="\033[1;33m";

$dbgtmr = "1";

use Digest::MD5 qw(md5_hex);
use Time::HiRes qw(gettimeofday);

if ($ARGV[0]=~"a") {
  $alpha = "abcdefghijklmnopqrstuvwxyz";}
if ($ARGV[0]=~"A") {
  $alpha = $alpha. "ABCDEFGHIJKLMNOPQRSTUVWXYZ";}
if ($ARGV[0]=~"0") {
  $alpha = $alpha."1234567890";}
if ($ARGV[0]=~"!") {
  $alpha = $alpha. "!\"\$%&/()=?-.:\\*'-_:.;,";}

$min = $ARGV[1];
$max = $ARGV[2];
$md5 = $ARGV[3];

$text = "Charset : $alpha";

if ($alpha eq "" or $md5 eq "") {
  $text = "No Charset or hash detected";
  usage();
};
if (length($md5) != 32) {
  banner();
  die "\n$yellow //$white $md5 not valid\n";
};

sub banner {
  system("clear");
  print "\n$white";
  print "\n   ▄▀▀▀▄";
  print "\n   █───█";
  print "\n  ███████$cyan   Simple MD5 Decryptor$white";
  print "\n  ██─▀─██   $text";
  print "\n  ███▄███\n\n";
}

banner();
print "\n$yellow //$white Start Bruteforcing $md5\n";
sleep(1);

for (my $x=$min;$x<=$max;$x++){
  crack ($x);
}

sub usage {
  banner();
  print "\n$cyan Charset$red :$white aA0!";
  print "\n$white ~$cyan   a$red   :$white abcdefghijklmnopqrstuvwxyz";
  print "\n$white ~$cyan   A$red   :$white ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  print "\n$white ~$cyan   0$red   :$white 1234567890";
  print "\n$white ~$cyan   !$red   :$white !\"\$%&/()=?-.:\\*'-_:.;,\n";
  print "\n$cyan Usage$red   :$white ./md5.pl <charset> <min> <max> <MD5>";
  print "\n$cyan example$red :$white ./md5.pl a0 1 8 ae2b1fca515949e5d54fb22b8ed95575\n\n";
  die;
}

sub crack{
  $CharSet = shift;
  @RawString = ();
  for (my $i =0;$i<$CharSet;$i++){ $RawString[i] = 0;}
  $Start = gettimeofday();
  do{
    for (my $i =0;$i<$CharSet;$i++){
      if ($RawString[$i] > length($alpha)-1){
        if ($i==$CharSet-1){
          print "\n$yellow //$white Bruteforcing done with max $CharSet Chars";
          print "\n$yellow //$white No results\n\n";
          return false;
        }
        $RawString[$i+1]++;
        $RawString[$i]=0;
      }
    }
    $ret = "";
    for (my $i =0;$i<$CharSet;$i++){ $ret = $ret . substr($alpha,$RawString[$i],1);}
    $hash = md5_hex($ret);
    $cnt++;
    $Stop = gettimeofday();
    if ($Stop-$Start>$dbgtmr){
      $cnt = int($cnt/$dbgtmr);
      print "\n$yellow //$white $cnt hashes/sec";
      print "\n$yellow //$white Last Text : $ret\n\n";
      $cnt=0;
      $Start = gettimeofday();
    }
    print "$cyan $hash$white [$red $ret$white ]\n";
    if ($md5 eq $hash){
      die "\n$cyan [+]$white Text$red :$white $ret\n";
    }
    $RawString[0]++;
  } while ($RawString[$CharSet-1]<length($alpha));

}