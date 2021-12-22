#!/usr/bin/perl
use strict;
use LWP::Simple qw($ua get);
		$ua = LWP::UserAgent->new;
		$ua->agent('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.3) Gecko/20070309 Firefox/2.0.0.9');
my @found;

&usage unless @ARGV==3;
my $url = $ARGV[0];
my $dirlist = $ARGV[1];
my $results = $ARGV[2];

open(ifile, "<$dirlist") || die "Couldn't open file\n";
my @dirs =<ifile>;
close("ifile");
&search;

sub usage{
	print "Usage:\n";
	print "DirSpider.pl <url> <file of directories> <result file>\n";
	print "DirSpider.pl http://www.google.com dirs.txt found.txt\n";
	exit;
}

sub search{
		foreach my $dir(@dirs){
			print "$url/$dir";
			my $response = $ua->get("$url/$dir");
			if($response->status_line !~ m/^404/){
				push(@found,"$url/$dir");
			}
		}
}