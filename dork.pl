#!/usr/bin/perl

use LWP::Simple;
use LWP::UserAgent;
use HTTP::Request;

print "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n";
print "+          PHP Shell Scanner          +\n";
print "+      Coded by Erm... AKA H4k3r      +\n";
print "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+";
print "\nInsert Shell Finding Dork > ";
chomp($dork = <STDIN>);
print "\nTotal Query Pages 10 Links/Page > ";
chomp($page = <STDIN>);
print "\n[+]@#~Result~#@[+]\n\n";
for ($start = 0;$start != $page*10;$start += 10)
   {
   $search = "http://www.google.com/search?hl=en&q=".$dork."&btnG=Search&start=".$start;
   $ua = LWP::UserAgent->new(agent => 'Mozilla 5.0');
   $resp = $ua->get($search);
   if ($resp -> is_success)
      {
      $cont = $resp -> content;
      @linkz0r = split (/<a href=/, $cont);
      foreach $line(@linkz0r)
         {
         if ($line =~ /(.*) class=l/ig)
            {
            $click = $1;
            $ua = LWP::UserAgent->new(agent => 'Mozilla 5.0');
            $resp = $ua -> get($click);
            $shelld0m = $resp->content();
            if ($shelld0m =~m/uname -a/)
               {
               print "$click has a shell present\n";
               }
            }
         }
      }
   }