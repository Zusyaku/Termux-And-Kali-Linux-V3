#!/usr/bin/perl
###########################
#
#  +++++++++[+] ScRiPt [+]+++++++++
#
#  Nepokatneza [ Email Extractor ] 
#  
#  +++++++++[+] CoDeR [+]++++++++++
#
#  Perforin
#
#  ++++++++[+] WeBsItEs [+]++++++++
#
#  Dark-Codez.org | perforins-script-labor.dl.am
#
############################

print <<EOF;

  _   _                  _         _                       
 | \\ | | ___ _ __   ___ | | ____ _| |_ _ __   ___ ______ _ 
 |  \\| |/ _ \\ '_ \\ / _ \\| |/ / _` | __| '_ \\ / _ \\_  / _` |
 | |\\  |  __/ |_) | (_) |   < (_| | |_| | | |  __// / (_| |
 |_| \\_|\\___| .__/ \\___/|_|\\_\\__,_|\\__|_| |_|\\___/___\\__,_|
            |_|

 coded by Perforin	

 
		   
EOF

if (@ARGV < 1) {
print qq {
 ++++++++++[+] SyNtAx [+]++++++++++
 
 Um eine Datei nach Mail-Adressen
 zu durchsuchen muss man folgendes
 eingeben:

 nepokatneza.exe file.txt

 ++++++++++[+] SyNtAx [+]++++++++++
 
};
exit;
}

$pfad = $ARGV[0];

open(FILE,"<$pfad") || die print "Datei konnte nicht geoeffnet werden!\n"; 
open(SORTED,">sorted.txt") || die print "Datei konnte nicht ertsellt werden!\n";

print " --> $pfad wird durchsucht!"."\n";

foreach $word (<FILE>) { 
$word =~ tr/ /\n/;
print SORTED $word;
}
close(FILE);
close(SORTED);

open(SORTED,"<sorted.txt") || die print "Datei konnte nicht eingelesen werden!\n";
@SORTED = <SORTED>;
close(SORTED);

unlink "sorted.txt" || die print "Datei konnte nicht geloescht werden!\n";

open(MAILS,">>mails.txt");
foreach $line (@SORTED) {
if ($line =~ m/(@)/) {
print MAILS "$line\n"; 
}
}
close(MAILS);

print " --> Mails wurden kopiert!"."\n";