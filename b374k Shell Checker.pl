#!/usr/bin/perl -U
#
# k4mpr3t toolz (c) 2013
# req : Active Perl

use HTTP::Request;
use LWP::UserAgent;
use IO::Select;
use HTTP::Response;
sub do_visit()
{
  $useragen=LWP::UserAgent->new;
  $useragent="Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)";
  $useragen->agent($useragent);
  $useragen->timeout(10);
  our $response=$useragen->get($url);
  our $content=$response->content;
}
$file=$ARGV[0];
open(SHELL, "<$file");
         my(@line) = <SHELL>;
         @line = sort(@line);
         my($http);
         foreach $http (@line)
           {
           chomp($http);
           $http =~ s/^\s+//;
           $http =~ s/\s+$//;
                
          if($http=~/http/)
          {
              our $url=$http;
              do_visit();
         if($content=~/b374k/ || $content=~/b374k/)
              {
              print "HIDUP -> checking : $url \n";    
              } else {
              print "MATI! -> checking : $url \n";
              }  
          }
            }
close(SHELL);