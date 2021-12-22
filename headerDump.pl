#!/usr/bin/perl

# Copyright 2012 Dakota Simonds
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
use strict;
use warnings;
use LWP::UserAgent;
use HTTP::Response;

print "Web-Sorrow (extra tool) headerDump v2\n\nURL: ";

my $site=<stdin>;
unless($site =~ m/http:/){
	$site = "http://$site";
}
my $ua = LWP::UserAgent->new;
$ua->agent("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.5) Gecko/20031027");
my $raw = $ua->get($site);
my $head = $raw->as_string();

my @headers = split(/\n\n/,$head);
print "\n\n";
print $headers[0];