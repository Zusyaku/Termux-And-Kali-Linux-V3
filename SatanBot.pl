#!/usr/bin/perl 
#Satan bot - illuz1oN 
require IO::Socket::INET; 
use IO::Socket; 
use strict; 
my $server = "irc.nitrousirc.net"; 
my $nick = "Satan`Tezt"; 
my $channel = "\#MD5"; 
my $msg = "Death Will Be Upon j00!\n\r"; 
my $identd = "HELL"; 
my $host = "BlackBook"; 
my $owner = "illuz1oN"; 
my $version = "[illuz1oN's Satan IRCBot V1.0 BETA]\n"; 
my @quits = ("Death Is Near"); 
my $sock = new IO::Socket::INET(PeerAddr => $server, 
											PeerPort => 6667, 
											Proto => 'tcp') or die "Can't connect\n"; 
	print $sock "NICK ".$nick."\r\n"; 
	print "[!]Nick Set: ".$nick."\n"; 
	print $sock "USER ".$identd." 8 * :".$host."\r\n"; 
	print "[!]Identified\n"; 
	print $sock "JOIN ".$channel."\r\n"; 
	print "[!]Joined: ".$channel."\n"; 
	print $sock "PRIVMSG ".$channel." :".$msg."\r\n"; 
 
while (my $input = <$sock>){ 
			print $input; 
			chop $input; 
		if ($input =~ /^PING(.*)$/){ 
			print $sock "PONG ".$owner."\r\n"; 
	} 
		elsif($input =~ m/^\:$owner\!(.*?)\@(.*?) PRIVMSG (.*?) :!nick (.*?)$/){ 
			print $sock "NICK ".$4."\n\r"; 
	} 
		elsif($input =~ m/^\:$owner\!(.*?)\@(.*?) PRIVMSG (.*?) :!kick (.*?) (.*?) 
$/){ 
			print $sock "KICK ".$3." ".$4." ".$5."\n\r"; 
	} 
		elsif($input =~ m/^\:$owner\!(.*?)\@(.*?) PRIVMSG (.*?) :!kickban (.*?) (. 
*?)$/){ 
		    print $sock "MODE ".$3." +b ".$4."\n\r"; 
			print $sock "KICK ".$3." ".$4." ".$5."\n\r"; 
	} 
		elsif($input =~ m/^\:$owner\!(.*?)\@(.*?) PRIVMSG (.*?) :!unban (.*?)$/){ 
			print $sock "MODE ".$3." -b ".$4."\n\r"; 
	} 
		elsif($input =~ m/^\:$owner\!(.*?)\@(.*?) PRIVMSG (.*?) :!voice (.*?)$/){ 
			print $sock "MODE ".$3." +v ".$4."\n\r"; 
	} 
		elsif($input =~ m/^\:$owner\!(.*?)\@(.*?) PRIVMSG (.*?) :!devoice (.*?)$/) 
{ 
			print $sock "MODE ".$3." -v ".$4."\n\r"; 
	} 
		elsif($input =~ m/^\:$owner\!(.*?)\@(.*?) PRIVMSG (.*?) :!op (.*?)$/){ 
			print $sock "MODE ".$3." +o ".$4."\n\r"; 
	} 
		elsif($input =~ m/^\:$owner\!(.*?)\@(.*?) PRIVMSG (.*?) :!deop (.*?)$/){ 
			print $sock "MODE ".$3." -o ".$4."\n\r"; 
	} 
		elsif($input =~ m/^\:$owner\!(.*?)\@(.*?) PRIVMSG (.*?) :!hop (.*?)$/){ 
			print $sock "MODE ".$3." +h ".$4."\n\r"; 
	} 
		elsif($input =~ m/^\:$owner\!(.*?)\@(.*?) PRIVMSG (.*?) :!dehop (.*?)$/){ 
			print $sock "MODE ".$3." -h ".$4."\n\r"; 
	} 
		elsif($input =~ m/^\:$owner\!(.*?)\@(.*?) PRIVMSG (.*?) :!chanmode (.*?)$/ 
){ 
			print $sock "MODE ".$3." ".$4."\n\r"; 
	} 
}