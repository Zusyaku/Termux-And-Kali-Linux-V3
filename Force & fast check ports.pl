#!/usr/bin/perl
use strict;use IO::Socket;my$port1=$ARGV[0];my$port2=$ARGV[1];my$proto=$ARGV[2];my$t="tcp";my$u="udp";my$wanted="0";my$deadline="1024";my$port;
sub header{print qq~
Test *REAL OPEN* ports
UDP or TCP protocols
for incoming and outgoing connections 
Netstat & rootkits goto hell
Usage: $0 [port from] [port to] [proto]
Tested on FreeBSD, OpenBSD and Linux\n\n~;}
sub header2{print qq~
Force & fast check ports 
Idea and C code author is rash
http://anarchy.blackhat.ru
Gr33tz: blf, 1dt.w0lf, edisan
(c)oded x97Rang, RST/GHC 2005
http://rst.void.ru
http://ghc.ru\n\n~;}
sub usage{&header;exit;}sub check{&header2;if($>ne$wanted){if($port1<$deadline){print"You are not root, and ports < 1024 not yours :)\n";exit;}}
if($port2>65535||$port1>$port2||$port1<1){print"Error in arguments, check range ports\n";exit}
if($proto eq $t){print"Let's begin:\n";print"Ports for $proto\n";print"From $port1 to $port2\n";print"Wait...\n";for($port=$port1;$port!=$port2;$port++){my$serv=IO::Socket::INET->new(Proto=>"$proto",LocalPort=>"$port",Type=>SOCK_STREAM,Reuse=>1,Listen=>10)or print"	$port	OPEN\n";}}
elsif($proto eq $u){print"Let's begin:\n";print"Ports for $proto\n";print"From $port1 to $port2\n";print"Wait...\n";for($port = $port1;$port!=$port2;$port++){my$serv=IO::Socket::INET->new(Proto=>"$proto",LocalPort=>"$port")or print"	$port	OPEN\n";}}else{print"Check for tcp or udp protocols ONLY!\n";exit}}if(@ARGV!=3){&usage;}else{&check;print"Done.\n";}
		





 



