#!/usr/bin/perl


# * DMZScan - Simple Connect Port Scanner using PERL, Phil Robinson, IRMPLC 2005
# *
# * Useful if a Windows box is compromised and you don't want to 
# * reboot it, or haven't got administrator privileges (Hint: use PERL2EXE)
# *
# * This code is free software; you can redistribute it and/or
# * modify it under the terms of the GNU General Public License
# * as published by the Free Software Foundation; either version 2
# * of the License, or (at your option) any later version.
# *
# * This code is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# * GNU General Public License for more details.
# *
# * You should have received a copy of the GNU General Public License
# * along with this program; if not, write to the Free Software
# * Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
# * Or, point your browser to http://www.gnu.org/copyleft/gpl.html

use Getopt::Std;
use IO::Socket;

sub parse_octet
{
  $octet = shift;
  my @retlist;

  if ( $octet =~ /,/ || $octet =~ /-/ ) 
  {
    @elements = split(/,/, $octet);
    foreach $element (@elements)
    {
      if ( $element =~ /-/ )
      {
        ($lower, $upper) = split(/-/, $element);
        if ($lower > $upper) { die "Incorrect IP Range"; }
        for ($x = $lower ; $x <= $upper ; $x++ ) { push @retlist, $x }
      }
      else
      { push @retlist, $element }
    }      
  }
  else { push @retlist, $octet }

  return @retlist;
}

sub parse_ip
{
  my $ip = shift;
  my @scanip;
  ($first, $second, $third, $fourth) = split(/\./,$ip);

  @firstlist = &parse_octet($first);
  @secondlist = &parse_octet($second);
  @thirdlist = &parse_octet($third);
  @fourthlist = &parse_octet($fourth);

  foreach $a (@firstlist)
  {
    foreach $b (@secondlist)
    {
      foreach $c (@thirdlist)
      {
        foreach $d (@fourthlist)
        {
          push @scanip, "$a.$b.$c.$d";
        }
      }
    }
  }
  
  return @scanip;
}
   
sub parse_ports
{
  my $p = shift;
  @plist = &parse_octet($p);
  return (@plist);
}

  
$Usage = qq{
IRM DMZ Scanner v0.1 - by Morfsta 2003

Usage: $0 [options] -h <IP Address / Range>

Options:
         -h IP Address/Range e.g. 10.0.244-246.0,5,6,9
	 -l Print list of IP addresses that will be scanned and exit
	 -p Port list e.g. 1-1024,3128,8080
	    (default 21, 22, 23, 53, 80, 111, 135, 139, 445)
	 -t Connect timeout - e.g. 0.1 (100ms - default 0.1)
	    (default 50ms)
	 -o Output file (outputs open ports only)
};

die $Usage if (!getopts('h:p:t:o:lc'));
$ip = $opt_h || die "$Usage Need to specify an IP address range";
$print = $opt_l || 0;
$ports = $opt_p || 0;
$timeout = $opt_t || 0.1;
$logfile = $opt_o || "";
@iplist = &parse_ip($ip);

if ($print)
{
  foreach $ipaddress (@iplist)
  {
    print "$ipaddress\n";
  }
  exit 0;
}

if ($ports)
{
  @portlist = &parse_ports($ports);
}
else { @portlist = (21,22,23,53,80,111,135,139,445) }

if ($logfile)
{
  open(LOG, ">$logfile") || die "Cannot write to logfile";
}

print "IRM DMZ Scanner v0.2 - by Morfsta 2004\n\n";

foreach $host (@iplist)
{
   foreach $port (@portlist)
   {
     if ($port =~ /\D/) { $port = getservbyname($port, tcp) }
       $iaddr   = inet_aton($host); 
       $paddr   = sockaddr_in($port, $iaddr);
       $proto   = getprotobyname('tcp');
       socket(SOCK, PF_INET, SOCK_STREAM, $proto)  || die "socket: $!";
       $sock = new IO::Socket::INET (PeerAddr => $host, 
				     PeerPort => $port,
				     Proto => 'tcp', 
				     Timeout => $timeout);
       if ( $sock ) 
       { 
	 print "$host:$port -> open\n"; 
	 if ( $logfile )
	 {
	   print LOG "$host:$port\n";
           close ($sock) || die "close: $!";
	 }
       }
   }
}
close(LOG);
print "\nFinished..\n";
