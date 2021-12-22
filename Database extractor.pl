#!/usr/bin/perl
use strict;
my($db_database,$db_prefix,$db_rowumbers,$db_splitter,$db_resultfile,$line,$realnum,$list,$dumplist,$x,@db_rowumbers,@fulldb,@rowdata);
sub usage{
	print "USAGE: <database>\tdb dump
	<prefix>\tPrefix of the table you're dumping
	<rows>\tNumbers pointing to the data you want, seperate by commas
	<delimiter>\tWhat to split the resulting data by. 
	\t\tIf you want spaces then enclose with quotes
	<resultfile>\tFile to dump the data to\n";
	print "EX: dump_gamers.sql e107_users 2,5 : gamerdump.txt\n";
	exit;
}


&usage unless @ARGV==5;
$db_database=$ARGV[0];
$db_prefix=$ARGV[1];
$db_rowumbers=$ARGV[2];
$db_splitter=$ARGV[3];
$db_resultfile =$ARGV[4];
@db_rowumbers = split(/,/,$db_rowumbers);
open(xfile, "<$db_database") || die "Couldn't open $list\n";
@fulldb = <xfile>;
close(xfile);
chomp(@fulldb);

foreach $line(@fulldb){
	if(($line =~ m/INSERT INTO \'$db_prefix\'\((.*?)\)/i) || ($line =~ m/INSERT INTO \`$db_prefix\`\((.*?)\)/i)  || ($line =~ m/^INSERT INTO $db_prefix(.*?)\((.*?)\)/i)){
			$line =~ s/INSERT INTO \'$db_prefix\'/INSERT INTO \`$db_prefix\`/;
		@rowdata = split(/\'/,$line);
		open(DBLOG,">>$db_resultfile") || die "Couldn't open uname-$dumplist\n";
		print "[+] ";
		for($x=0;$x<=$#db_rowumbers;$x++){
			$realnum = $db_rowumbers[$x]*2-1;
			if($x==$#db_rowumbers){
				print "$rowdata[$realnum]\n";
				print DBLOG "$rowdata[$realnum]\n";
			}
			else{
				print "$rowdata[$realnum]$db_splitter";
				print DBLOG "$rowdata[$realnum]$db_splitter";
			}
		}
	}
}
		close(DBLOG);
		print "[+] Parsing & dumping completed\n";