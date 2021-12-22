#!/usr/bin/perl
use Socket;
system('cls');
system('title Port Scanner [C]oded by Gl4di4t0r      ');
print q
{
#Port Scanner
[+]---------Port Scanner By GlaDiaT0R-------[+]
[+]-------------Coded By GlaDiat0R----------[+]
[+]--------Tunisian Hacker -----------------[+]
[+]------------Greetz to Allah--------------[+]
-----------------------------------------------
My Home Page: DarkGh0st.com

  ____ _       ____  _      _____ ___       
/ ___| | __ _|  _ \(_) __ |_   _/ _ \ _ __
| |  _| |/ _` | | | | |/ _` || || | | | '__|
| |_| | | (_| | |_| | | (_| || || |_| | |   
\____|_|\__,_|____/|_|\__,_||_| \___/|_|   
                                           


};
print "Enter IP: ";
my $x;
my $servip = <STDIN>;
chop $servip;

for($a=0;$a<=65000;$a++) {
    $ip_addr = sockaddr_in($a, inet_aton($servip));
    $protocol = getprotobyname("tcp");
socket(SOCK, PF_INET, SOCK_STREAM, $protocol);
if(connect(SOCK, $ip_addr))
    {
         print "[#] Port " . $a . " open\n";
         $x++;
        }
         else {
         close(SOCK);
          }
   
}

sub Services
{
    @open_ports = ($a);
   
    foreach $openports(@open_ports) {
    $ipaddr = sockaddr_in($openports, inet_aton($servip));
    $prot2 = getprotobyname("tcp");
    socket(SCK2, PF_INET, SOCK_STREAM, $prot2);
    connect(SCK2, $ipaddr);
    recv(SCK2, $buff, 750, 0); #recv information

    print($buff);

    }
}
    print "[+] Scan Finished!\n";
    print "\nResults:\n===================\n";
    print "Number of open ports: " . $x . "\n";

&Services;