#!/usr/bin/perl -w
#Dork Scann
#By
#Senhor Li
 
 use LWP::UserAgent; 
 
print q{
+----------------------[Dork Scan]----------------------+
|                                                       |
|                      By Senhor Li                     |
|                      By MrBlackx                      |
|                         v1.6                          |
+-------------------------------------------------------+
 
};
print "\nPut Your Dork:";
print "\n(Ex: inurl:home.php?id= )\n";
print "=>";
$dork = <STDIN>; 
chomp($dork); 
 
print "Scan Started!";
 
for ($i = 0; $i < 1000; $i += 10) { 
 
$b = LWP::UserAgent->new(agent => 'Mozilla/4.8 [en] (Windows NT 6.0; U)'); 
$b->timeout(30); 
$b->env_proxy; 
$c = $b->get('http://www.bing.com/search?q=' . $dork . '&first=' . $i . '&FORM=PERE')->content; 
$check = index($c, 'sb_pagN'); 

while (1) { 
$n = index($c, '<h3><a href="'); 

if ($n == -1) { 
last; 
} 

print "$s\n";
$c = substr($c, $n + 13); 
$s = substr($c, 0, index($c, '"'));
open(txt,">>scanned.txt"); 
print txt $s,"\n"; 
close(txt);

} 
if ($check == -1) { 
last; 
} 
}
print "Scan Finalizado!";
exit;