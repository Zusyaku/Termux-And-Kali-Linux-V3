#!/usr/bin/perl
# Copyright 2012 Dakota Simonds
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

BEGIN {
	print "+ Web-Sorrow (extra tool) Simple Host Discovery v2\n";
	
	use Net::Ping;
	use IO::Socket::INET;
	use Getopt::Long;
	use threads;
	use threads::shared;

	use warnings;
	use strict;
}
my $Host = "none";
GetOptions("host=s" => \$Host);


# usage
if($Host eq "none"){
	print "Usage: perl hdt.pl -host example.com\n\t-host  -  domain or ip ADDR\n";
	exit();
}


my $Stat :shared = "Host is DOWN";

my @ports = (7, 23, 25, 53, 54, 80, 443, 3128, 6669, 8008, 8080); # common ports
my @thrdsArryS;

#full connect
push(@thrdsArryS, threads->new( sub {
	foreach my $port (@ports) {
		
		
		my $SockTest = IO::Socket::INET->new(
			PeerAddr => $Host,
			PeerPort => $port,
			Proto => 'tcp',
			Timeout => 0,
		) or next;
		
		print "+ Successful probe -> OPEN $port/tcp\n" and $Stat = "Host Is UP";
		close($SockTest);
	}
}));


# pings a plenty
my @Methods = ('tcp','icmp','udp');
my @thrdsArry;

	foreach my $Meth (@Methods){
		push(@thrdsArry, threads->new( sub {
			foreach my $port (@ports) {
				sexysexyPingTime($Meth, $port, $Host);
			}
		}));
		
	}

sub sexysexyPingTime{
	my $Method = shift;
	my $portt = shift;
	my $Hostt = shift;
	
	my $ping = Net::Ping->new($Method, 0, 24);
	$ping->port_number($portt);
	
	print "+ Successful probe -> OPEN $portt/$Method (ping)\n" and $Stat = "Host Is UP" if $ping->ping($Hostt);
}


foreach my $threadd (@thrdsArryS){
	$threadd->join();
}
foreach my $thread (@thrdsArry){
	$thread->join();
}
print "+ $Stat\n+ Scan finished :'(";