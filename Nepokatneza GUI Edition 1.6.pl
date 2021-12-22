#!/usr/bin/perl
#############################
# Nepokatneza GUI Edition 1.6
#
# Coded by Perforin 
#
# www.perforins-software.de.vu
# www.dark-codez.org
#############################

use Tk;
use Tk::NoteBook;
use LWP::UserAgent;
use LWP::Simple;

$version = "1.6";
 
print "=> Nepokatneza gestartet."."\n";
print "=> Versions Check: v$version"."\n";
print "=> GUI wird geladen."."\n";
 
$main = MainWindow->new();
$main->title ("+++ Nepokatneza +++");
$image = 'icon.gif'; # Look at my Site for the Picture
$icon = $main->Photo(-file => $image);
$main->iconimage($icon);
$top = $main->Frame(-background => 'White')->pack('-side' => 'top');
$top->Photo('logo', -file => "logo.gif"); # Look at my Site for the Picture
$top->Label('-image' => 'logo')->pack();
$note = $main->NoteBook()->pack();
$page = $note->add('Notebook-0', -label => ' Start ');
$page1 = $note->add('Notebook-1', -label => ' Lokal ');
$page2 = $note->add('Notebook-2', -label => ' Web ');
$page3 = $note->add('Notebook-3', -label => ' MailGEN ');
$page4 = $note->add('Notebook-4', -label => ' Mail-Duplikate ');
$page5 = $note->add('Notebook-5', -label => ' URL File ');
$intro_message = $page->Label (-text=>"\UNepokatneza [Mail Extractor]\E\n\n Nepokatneza ist ein Mail Spider,\nder komplett in Perl geschrieben wurde.\nPerfekt f?r die Spammer unter euch.",
                               -height=>8,
				               -width=>60)
			               	   ->pack();
$funktionen_message = $page->Label (-text=>"+++++ Funktionen +++++\n-Lokale Anwendung\n-Web Anwendung\n-Mail Generierung\n-Duplikate entfernen\n\n")->pack();
$coded_by = $page->Label(-text=>"Coded by Perforin")->pack(-side=>"bottom",-anchor=>'s');
$entry = $page->pack();
$local_welcome = $page1->Label (-text=>"Nepokatneza zur LOKALEN durchsuchung benutzen!\n" ,
                                -height=>5,
				                -width=>60)
				                ->pack();
$local_pfad_angeben = $page1->Label (-text=>"Bitte Datei Pfad angeben:")->pack (-side=>"left",-anchor=>'n');
$local_pfad = $page1->Entry (-width=>35)->pack();
$local_button= $page1->Button(-text=>"[Nach Mails suchen]",
                              -background=>"green",
				              -command=>[\&local])
				              ->pack(-side=>"bottom",-anchor=>'e');
$web_welcome = $page2->Label (-text=>"Nepokatneza zur WEB durchsuchung benutzen!\n" ,
                              -height=>5,
				              -width=>60)
							  ->pack();
$web_url_angeben = $page2->Label (-text=>"Bitte Adresse angeben:")->pack (-side=>"left",-anchor=>'n');
$web_url = $page2->Entry (-width=>35)->pack();
$web_checkbox = $page2->Checkbutton(-text => "Adressliste benutzen?     ",
                                    -command  => sub { $web_checkbox_true = "ready"; },
                                    -variable => \$web_checkbox_true,
									-onvalue  => "ready",
                                    -offvalue => "noe")
									->pack();
$web_button= $page2->Button(-text=>"[Nach Mails suchen]",
                            -background=>"green",
				            -command=>[\&web])
				            ->pack(-side=>"bottom",-anchor=>'se');
$mailGEN_welcome = $page3->Label (-text=>"Nepokatneza zum Adressen erstellen benutzen!\n" ,
                                  -height=>5,
				                  -width=>60)
				                  ->pack();
$mailGEN_checkbox1 = $page3->Checkbutton(-text => '@hotmail.com     ',
                                         -variable => \$AThotmail)
									     ->pack(-side=>"top");
$mailGEN_checkbox2 = $page3->Checkbutton(-text => '@yahoo.de        ',
                                         -variable => \$ATyahoo)
									     ->pack();
$mailGEN_checkbox3 = $page3->Checkbutton(-text => '@gmail.com       ',
                                         -variable => \$ATgmail)
									     ->pack(-side=>"top");
$mailGEN_checkbox4 = $page3->Checkbutton(-text => '@gmx.com         ',
                                         -variable => \$ATgmx)
									     ->pack(-side=>"top");
$mailGEN_checkbox5 = $page3->Checkbutton(-text => '@web.de           ',
                                         -variable => \$ATweb)
									     ->pack(-side=>"top");
$mailGEN_button= $page3->Button(-text=>"[Generiere Mails]",
                                -background=>"green",
				                -command=>[\&mailgen])
				                ->pack(-side=>"bottom",-anchor=>'se');
$duplikate_welcome = $page4->Label (-text=>"Nepokatneza zum Duplikate suchen benutzen!\n" ,
                                    -height=>5,
				                    -width=>60)
				                    ->pack();
$duplikate_erklaerung = $page4->Label (-text=>"Duplikate sind doppelt vorhandene E-Mail Adressen.\nDiese werden hiermit gesucht und gel?scht,\nso dass nur noch ein Exemplar jeder E-Mail Adresse vorliegt!")->pack();
$dublikate_button = $page4->Button(-text=>"[Suche Duplikate]",
                                   -background=>"green",
				                   -command=>[\&duplikate])
				                   ->pack(-side=>"bottom",-anchor=>'e');
$dublikate_welcome = $page5->Label (-text=>"Nepokatneza zum Searchfile erstellen benutzen!\n" ,
                                    -height=>5,
				                    -width=>60)
				                    ->pack();
$searchfile_einfugen = $page5->Label (-text=>"Bitte Adressen eingeben:  ")->pack (-side=>"left",-anchor=>'n');
$searchfile_button = $page5->Button(-text=>"[Suchdatei erstellen]",
                                    -background=>"green",
				                    -command=>[\&url_file])
				                    ->pack(-side=>"bottom",-anchor=>'e');
$input = $page5->Text(-height=>5,
                      -width=>30)
					  ->pack(-side => 'left');
$entry->focus();
print "=> GUI geladen."."\n";
MainLoop();
sub local {
print "=> Lokale Benutzung."."\n";
$mailcount = 0;
$pfad = $local_pfad->get;
open(FILE,"<", "$pfad"); 
open(SORTED,">", "sorted.txt");
foreach $word (<FILE>) { 
$word =~ tr/ 	/\n/;
$word =~ s/_at_/@/i;
$word =~ s/_dot_/./i;
$word =~ s/<at>/@/i;
$word =~ s/<dot>/./i;
if ($word =~ m/([at])/i) {
$word =~ tr/[]//d;
$word =~ s/at/@/i;
}
if ($word =~ m/([dot])/i) {
$word =~ tr/[]//d;
$word =~ s/dot/./i;
}
print SORTED $word;
}
close(FILE);
close(SORTED);
open(SORTED,"<","sorted.txt");
open(MAILS,">>", "nepokatneza-mails.txt");
foreach $line (<SORTED>) {
if ($line =~ m/(@)/) {
if ($line =~ m/\.\w\w\w?/) {
$mailcount++;
print MAILS "$line"; 
}
}
}
close(SORTED);
close(MAILS);
unlink "sorted.txt";
$page1->messageBox (-message=>"$mailcount Mails gefunden!");
}
sub web {
$mailcount = 0;
if ($web_checkbox_true =~ m/ready/i) {
print "=> Web Benutzung mit URL File."."\n";
open(SF,"<","nepokatneza-sf.txt");
foreach $addy (<SF>) {
chop($getTHEmails = "$addy");
$agent = new LWP::UserAgent;
$request = HTTP::Request->new('GET',$getTHEmails);
$result = $agent->request($request);
$getTHEmails =~ s/.*\///;
$getTHEmails = "temp1.txt";
open(lookME, ">>", "temp1.txt") || die print "Datei konnte nicht erstellt werden!\n";
print lookME $result->content();
close(lookME);
}
close(SF);
open(IP,"<","temp1.txt") || die print "Datei konnte nicht geoeffnet werden!\n";
foreach $line (<IP>) {
$line =~ s/<//;
$line =~ s/>//;
$line =~ s/\///;
$line =~ s/"/\n/g;
$line =~ s/mailto:/\n/g;
push(@temp2,"$line");
}
close(IP);
unlink "temp1.txt" || die print "Datei konnte nicht geloescht werden!\n";
open(temp2, ">", "temp2.txt") || die print "Datei konnte nicht erstellt werden!\n";
print temp2 @temp2;
close(temp2);
open(temp3, "<", "temp2.txt") || die print "Datei konnte nicht geoeffnet werden!\n";
for $mails (<temp3>) {
if ($mails =~ m/.@/) {
if ($mails =~ m/\.\w\w\w?/) {
$mailcount++;
push(@mails,"$mails");
}
}
}
close(temp3);
unlink "temp2.txt" || die print "Datei konnte nicht geloescht werden!\n";
open(output, ">>", "nepokatneza-mails.txt") || die print "Datei konnte nicht erstellt werden!\n";
print output @mails;
close(output);
$page2->messageBox (-message=>"$mailcount Mails gefunden!");
} else {
print "=> Web Benutzung ohne URL File."."\n";
$pfad = $web_url->get;
$getTHEmails = "$pfad";
$agent = new LWP::UserAgent;
$request = HTTP::Request->new('GET',$getTHEmails);
$result = $agent->request($request);
$getTHEmails =~ s/.*\///;
$getTHEmails = "temp1.txt";
open(lookME, ">", "temp1.txt") || die print "Datei konnte nicht erstellt werden!\n";
print lookME $result->content();
close(lookME);
open(IP,"<","temp1.txt") || die print "Datei konnte nicht geoeffnet werden!\n";
foreach $line (<IP>) {
$line =~ s/<//;
$line =~ s/>//;
$line =~ s/\///;
$line =~ s/"//g;
$line =~ s/mailto:/\n/g;
push(@temp2,"$line");
}
close(IP);
unlink "temp1.txt" || die print "Datei konnte nicht geloescht werden!\n";
open(temp2, ">", "temp2.txt") || die print "Datei konnte nicht erstellt werden!\n";
print temp2 @temp2;
close(temp2);
open(temp3, "<", "temp2.txt") || die print "Datei konnte nicht geoeffnet werden!\n";
for $mails (<temp3>) {
if ($mails =~ m/.@/) {
if ($mails =~ m/\.\w\w\w?/) {
$mailcount++;
push(@mails,"$mails");
}
}
}
close(temp3);
unlink "temp2.txt" || die print "Datei konnte nicht geloescht werden!\n";
open(output, ">>", "nepokatneza-mails.txt") || die print "Datei konnte nicht erstellt werden!\n";
print output @mails;
close(output);
$page2->messageBox (-message=>"$mailcount Mails gefunden!");
}
}
sub mailgen {
print "=> Mails generieren."."\n";
print "=> Wordlist runterladen."."\n";
$content=getstore('http://www.milw0rm.com/mil-dic.php','mil-dic.txt');
open(mille,"<","mil-dic.txt");
print "=> Wordlist runtergeladen."."\n";
open(gen,">","nepokatneza-mgen.txt");
foreach $string (<mille>) {
$string =~ s/\n//;
print gen $AThotmail?"$string".'@hotmail.com'."\n":"";
print gen $ATyahoo?"$string".'@yahoo.de'."\n":"";
print gen $ATgmail?"$string".'@gmail.com'."\n":"";
print gen $ATgmx?"$string".'@gmx.com'."\n":"";
print gen $ATweb?"$string".'@web.de'."\n":"";
}
close(mille);
close(gen);
unlink "mil-dic.txt";
$page3->messageBox (-message=>"Mails erstellt!");
print "=> Mails erstellt."."\n";
}
sub duplikate {
print "=> Duplikate loeschen."."\n";
open(duplikate, "<", "nepokatneza-mails.txt") || die print "Datei konnte nicht geoeffnet werden!\n";
$count_dups = 0;
%hash = ();
for (<duplikate>) {
$hash{$_} = 1;
$count_dups++;
}
close(duplikate);
open(dupfrei, ">", "nepokatneza-mails.txt") || die print "Datei konnte nicht erstellt werden!\n";
@dups = keys(%hash);
@sorted_dups = sort(@dups);
$sorted_dups = int(@sorted_dups);
$anzahl_dups = $count_dups-$sorted_dups;
print dupfrei @sorted_dups;
close(dupfrei);
if ($anzahl_dups =~ 0) {
$page4->messageBox (-message=>"Keine Duplikate gefunden!");
} elsif ($anzahl_dups =~ 1) {
$page4->messageBox (-message=>"$anzahl_dups Duplikat entfernt!");
} else {
$page4->messageBox (-message=>"$anzahl_dups Duplikate entfernt!");
}
print "=> Duplikate geloescht."."\n";
}
sub url_file {
print "=> URL File erstellen."."\n";
open(SF,">","nepokatneza-sf.txt");
print SF $input->get('1.0', 'end');;
close(SF);
$page5->messageBox (-message=>"URL File erstellt!");
print "=> URL File erstellt."."\n";
}