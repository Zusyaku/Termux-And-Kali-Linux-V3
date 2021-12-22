#!/usr/bin/env perl

# This perl script generates MD5 Checksums

use strict;
use IO::File;
use Getopt::Long;
use Digest::MD5;

print "\n";
print "##########################################################\n";
print "#                                                        #\n";
print "#             Coded by Infinity ~ MD5 Checker              #\n";
print "#                     [MD5 Checksum]                     #\n";
print "#--------------------------------------------------------#\n";
print "##########################################################\n";
print "#                                                        #\n";
print "#         Usage: md5_check.pl filename.extention         #\n";
print "#             Example: md5_check.pl image.jpg            #\n";
print "#                                                        #\n";
print "#       Note - Use in same directory of the file         #\n";
print "#                    You want to check                   #\n";
print "#                                                        #\n";
print "##########################################################\n";
print "\n";

my $File = $ARGV[0]; 
my $md5 = Digest::MD5->new;
my $check = 1;

open(FILE, $File) or die "Error: Could not open $File for MD5 checksum, please refer to the usage...";
binmode(FILE);
my $md5sum = $md5->addfile(*FILE)->hexdigest; 
close FILE;

print "\n";
print "Finished MD5 Checksum for $File:\n";
print "$md5sum\n";
print "\n";