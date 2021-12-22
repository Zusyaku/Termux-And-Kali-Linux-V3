use Digest::SHA1 sha1_hex;
use Digest::MD5 md5_hex;
use strict;
use warnings;

#
# BR00TALL-Revision 3
# Created by G-Brain
# http://g-brain.sesoyo.com
#

# Print standard information

print "[G] Message--> BR00TALL - The Perl Password Hash Brute-Forcer\n";
print "[-] Message--> Revision 3\n";
print "[B] Message--> Created by G-Brain\n";
print "[R] Message--> Happy brute-forcing...\n";
print "[A]\n";

# Check whether the amount of arguments is lower than the amount of arguments required and print usage message if not

if ($#ARGV != 5) {
	print "[I] Error--> Not enough arguments. Aborting...\n";
	print "[N] Usage--> perl $0 -e <md5|sha1> -h <hash to be bruteforced> -r <range of lengths>\n";
	exit;
}

# Declare some stuff
# $n = number used in argument assignment
# $a = argument used in argument assignment
# $e = encryption type
# $l = location of the given hash
# $r = range
# $q = query used in brute-force loop
# @rng = range, in numerical form
# $i = number used in brute-force loop

my ($n, $a, $e, $l, $r, $q, @rng, $i);

# Assign all arguments to their appropriate values

$n = -1;

foreach $a (@ARGV) {
	$n++;
	if ($a eq '-e') {
		$e = $ARGV[($n+1)];
	}
	if ($a eq '-h') {
		$l = ($n+1);
	}
	if ($a eq '-r') {
		$r = $ARGV[($n+1)];
	}
}

# Check for a valid encryption type and exit on error

if ($e ne 'md5' && $e ne 'sha1') {
	print "[I] Error--> Invalid encryption type. Aborting...\n";
	print "[N] Usage--> perl $0 -e <md5|sha1> -h <hash to be bruteforced> -r <range of lengths>\n";
	exit;
}

# Assign the input hash to $q

chomp($q=$ARGV[$l]);

# Check input hash length and exit if incorrect

if ($e eq 'md5') {
	if (length($q) != 32) { print "[I] Error--> Wrong hash length. Aborting...\n[N]\n"; exit; }
}
if ($e eq 'sha1') {
	if (length($q) != 40) { print "[I] Error--> Wrong hash length. Aborting...\n[N]\n"; exit; }
}

# Define range in numerical form, this causes the start number to be assigned to $rng[0] and the end number to $rng[1]

@rng = split("-",$r);

# Check for a valid start and end, exit on error

if ($rng[1] > 10) { print "[I] Error--> Range ending number over 10, aborting...\n[N]\n"; exit; }
if ($rng[0] < 1) { print "[I] Error--> Range starting number below 1, aborting...\n[N]\n"; exit; }

# Print input information

print "[I] Input----> $q using ";
if ($e eq 'md5') { print "MD5 "; }
elsif ($e eq 'sha1') {print "SHA-1"; }
print "encryption and range $rng[0] to $rng[1]\n";
print "[N]\n";

# Check the encryption type and assign numerical value to $e, numbers are managed more easily than strings, faster too

if ($e eq 'sha1') {
	$e = 0;
}

elsif ($e eq 'md5') {
	$e = 1;
}

# Start the brute-force loop

foreach $i ($rng[0]..$rng[1]) {
	print "[ ] Message--> Attempting $i letter passwords...\n";
	foreach $1 ('a'..'z','A'..'Z',0..9) {
		if ($i == 1) {
			if ($e == 0) { if (sha1_hex($1) eq $q) { print "[!] Solution-> $1\n"; exit; } } else { if (md5_hex($1) eq $q) { print "[!] Solution-> $1\n"; exit; } }
		}
		else {
			foreach $2 ('a'..'z','A'..'Z',0..9) {
				if ($i == 2) {
					if ($e == 0) { if (sha1_hex($1.$2) eq $q) { print "[!] Solution-> $1$2\n"; exit; } } else { if (md5_hex($1.$2) eq $q) { print "[!] Solution-> $1$2\n"; exit; } }
				}
				else {
					foreach $3 ('a'..'z','A'..'Z',0..9) {
						if ($i == 3) {
							if ($e == 0) { if (sha1_hex($1.$2.$3) eq $q) { print "[!] Solution-> $1$2$3\n"; exit; } } else { if (md5_hex($1.$2.$3) eq $q) { print "[!] Solution-> $1$2$3\n";	exit; } }
						}
						else {
							foreach $4 ('a'..'z','A'..'Z',0..9) {
								if ($i == 4) {
									if ($e == 0) { if (sha1_hex($1.$2.$3.$4) eq $q) { print "[!] Solution-> $1$2$3$4\n"; exit; } } else { if (md5_hex($1.$2.$3.$4) eq $q) { print "[!] Solution-> $1$2$3$4\n"; exit; } }
								}
								else {
									foreach $5 ('a'..'z','A'..'Z',0..9) {
										if ($i == 5) {
											if ($e == 0) { if (sha1_hex($1.$2.$3.$4.$5) eq $q) { print "[!] Solution-> $1$2$3$4$5\n"; exit; } } else { if (md5_hex($1.$2.$3.$4.$5) eq $q) { print "[!] Solution-> $1$2$3$4$5\n"; exit; } }
										}
										else {
											foreach $6 ('a'..'z','A'..'Z',0..9) {
												if ($i == 6) {
													if ($e == 0) { if (sha1_hex($1.$2.$3.$4.$5.$6) eq $q) { print "[!] Solution-> $1$2$3$4$5$6\n"; exit; } } else { if (md5_hex($1.$2.$3.$4.$5.$6) eq $q) { print "[!] Solution-> $1$2$3$4$5$6\n"; exit; } }
												}
												else {
													foreach $7 ('a'..'z','A'..'Z',0..9) {
														if ($i == 7) {
															if ($e == 0) { if (sha1_hex($1.$2.$3.$4.$5.$6.$7) eq $q) { print "[!] Solution-> $1$2$3$4$5$6$7\n"; exit; } } else { if (md5_hex($1.$2.$3.$4.$5.$6.$7) eq $q) { print "[!] Solution-> $1$2$3$4$5$6$7\n"; exit; } }
														}
														else {
															foreach $8 ('a'..'z','A'..'Z',0..9) {
																if ($i == 8) {
																	if ($e == 0) { if (sha1_hex($1.$2.$3.$4.$5.$6.$7.$8) eq $q) { print "[!] Solution-> $1$2$3$4$5$6$7$8\n"; exit; } } else { if (md5_hex($1.$2.$3.$4.$5.$6.$7.$8) eq $q) { print "[!] Solution-> $1$2$3$4$5$6$7$8\n"; exit; } }
																}
																else {
																	foreach $9 ('a'..'z','A'..'Z',0..9) {
																		if ($i == 9) {
																			if ($e == 0) { if (sha1_hex($1.$2.$3.$4.$5.$6.$7.$8.$9) eq $q) { print "[!] Solution-> $1$2$3$4$5$6$7$8$9\n"; exit; } } else { if (md5_hex($1.$2.$3.$4.$5.$6.$7.$8.$9) eq $q) { print "[!] Solution-> $1$2$3$4$5$6$7$8$9\n"; exit; } }
																		}
																		else {
																			if ($i == 10) {
																				foreach $10 ('a'..'z','A'..'Z',0..9) {
																					if ($e == 0) { if (sha1_hex($1.$2.$3.$4.$5.$6.$7.$8.$9.$10) eq $q) { print "[!] Solution-> $1$2$3$4$5$6$7$8$9$10\n"; exit; } } else { if (md5_hex($1.$2.$3.$4.$5.$6.$7.$8.$9.$10) eq $q) { print "[!] Solution-> $1$2$3$4$5$6$7$8$9$10\n"; exit; } }
																				}
																			}
																			else {
																				print "[!] Error-> Brute-force failed. Please either increase the range or replace your alphabet\n";
																				exit;
																			}
																		}
																	}
																}
															}
														}
													}
												}
											}
										}
									}
								}
							}
						}
					}
				}
			}
		}
	}
}
