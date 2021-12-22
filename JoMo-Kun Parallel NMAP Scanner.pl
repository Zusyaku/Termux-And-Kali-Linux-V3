#!/usr/bin/perl
#
# nmap_spawn.pl
#
#####################################################################
#    JoMo-Kun Parallel NMAP Scanner
#
#####################################################################
#
#
# This program will read in a list of IPs from a text file (or specified
# range) and then spawn X number of parallel nmap processes to scan 
# those addresses.
# 

use Getopt::Long;
use NetAddr::IP;
use POSIX ":sys_wait_h";

my $VERSION = "0.9.8.2";
my $TSTART, $TSTOP;

print "\nJoMo-Kun Parallel NMAP Scanner\n\n";

GetOptions (
  'threads=i'      => \$PARALLEL,
  'iplist=s'       => \$inFile,
  'start_index=s'  => \$startIndex,
  'stop_index=s'   => \$stopIndex,
  'iprange=s'      => \$ipRange,
  'output=s'       => \$outFile,
  'sS'             => sub { $NMAP_OPTIONS = "-sS "; $ChkRoot = 1; },
  'sT'             => sub { $NMAP_OPTIONS = $NMAP_OPTIONS . "-sT "; $ChkRoot = 1; },
  'sP'             => sub { $NMAP_OPTIONS = $NMAP_OPTIONS . "-sP "; $ChkRoot = 1; },
  'O'              => sub { $NMAP_OPTIONS = $NMAP_OPTIONS . "-O "; $ChkRoot = 1; },
  'sV'             => sub { $NMAP_OPTIONS = $NMAP_OPTIONS . "-sV "; },
  'p=s'            => sub { $NMAP_OPTIONS = $NMAP_OPTIONS . "-@_ "; },
  'P0'             => sub { $NMAP_OPTIONS = $NMAP_OPTIONS . "-P0 "; },
  'T=s'            => sub { $NMAP_OPTIONS = $NMAP_OPTIONS . "-@_ "; },
);
 
if ( !defined($PARALLEL) || !(defined($inFile) xor defined($ipRange)) || !defined($outFile) ) {
  print "NMAP SPAWN V. $VERSION\n";
  print "Usage:\n";
  print " $0\n";
  print "   --threads <number of threads>\n";
  print "   --iplist <ip list file>\n";
  print "   --iprange <ip range>\n";
  print "   --output <output file>\n";
  print "   --start_index <list start index> [OPTIONAL, 0 = FIRST]\n";
  print "   --stop_index <list stop index> [OPTIONAL]\n";
  print "   NMAP Options (-sS, -sT, -sP, -O, -p, -P0, -T)\n";
  exit(1);
}
elsif ( ($ChkRoot) && ($>) ) {
  print "\n** NMAP FINGERPRINTING REQUIRES ROOT PRIVILEGES **\n\n";
  exit(1);
}

#####################################################################
#  MISC VARIABLES:
#
# $pidMap{} is keyed on the pid of the child process in charge
#   of executing the nmap commands.
#  
$PROCCOUNT = 0;
$p_read = 'PREAD00';
$p_write = 'PWRITE00';
$myPid = $$;
$NMAP = "/usr/bin/nmap";

$SIG{'CHLD'} = \&reaper;
$SIG{'INT'} = \&doSummary;
#$SIG{'QUIT'} = \&doSummary;

# read in ip address list
#
my @ip_list;
if (defined($inFile)) {
   open(FILE, $inFile) || die("Unable to open: $inFile $!");
   my @ip_list_tmp=<FILE>;
  foreach(@ip_list_tmp) {
    if (/\//) {    # range
       my $ip = new NetAddr::IP "$_";
       push @ip_list, $ip->hostenum;
    }
    else { push @ip_list, $_; }
     foreach (@ip_list) { s/\/\d+//; }
  }
   close(FILE);
} else {
   my $ip = new NetAddr::IP "$ipRange";
   #push @ip_list, $ip->network;
   push @ip_list, $ip->hostenum;
   #push @ip_list, $ip->broadcast;
   foreach (@ip_list) { s/\/\d+//; }
}

#####################################################################
#  MAIN:
#
my $total_addr = $#ip_list + 1;
my $current_addr = 0;
$TSTART = time();

if (!defined($startIndex)) { $startIndex = 0; }
if (!defined($stopIndex)) { $stopIndex = $#ip_list; }

for ($i = $startIndex; $i <= $stopIndex; $i++) {
  $address = $ip_list[$i];  
  chomp $address;
  $current_addr++;
  ADD: {
    ($p_name ,$pid) = &addChild($address);
    if ($pid == 0) {
      sleep 1;
      #print STDERR "Redoing add\n";
      redo ADD;
    } elsif ($pi>d == -1) {
      print "PARENT [$$] failed $address.\n";
    } else {
      # Success
      # print "PARENT [$$] added child $status.\n";
      $pidMap{$pid}{'PIPE'} = $p_name;
    }
  } # ADD
}

while ($PROCCOUNT > 0) { sleep 1; }

$TSTOP = time();
doSummary();
exit(0);


#####################################################################
# Subroutines

# Add a child, return the pid of the child process if successful, -1 if the
#   fork failed, 0 if there are no available slots.
#
sub addChild($) {
  my $address = $_[0];
  my $pid;
  chomp $address;
  return 0 if ($PROCCOUNT >= $PARALLEL);
  #print STDERR "PROCCOUNT is $PROCCOUNT, forking a child\n";
  pipe($p_read, $p_write) || die "Can't open a pair of pipes: $!";
  FORK: {
    if ($pid = fork()) {
      # ********* Parent Process **********
      $PROCCOUNT++;
      $pidMap{$pid} = $address;
      close($p_write);
      $hold = $p_read;
      $p_read++;
      $p_write++;
      return($hold, $pid);
      # ********* Parent Process **********
    } elsif (defined($pid)) {
      # ********** Child Process **********
       close($p_read);
      my $temp_current_addr =  $current_addr + $startIndex;
      print STDERR "Starting NMAP: $address\t($temp_current_addr of $total_addr)\n";
       $data = `$NMAP $NMAP_OPTIONS $address`;
      print $p_write $data;
      close($p_write);
      print STDERR "Stopping NMAP: $address\n";
      exit(0);
      # ********** Child Process **********
    } elsif ($! =~ /no more process/i) {
      # recoverable fork error?
      sleep 5;
      redo FORK;
    } else {
      # can't fork
      return -1;
    }
  } # FORK
} # addChild


# handle the exit of a child process.  return the output of the child's
#   nmap scan.
#
sub reaper() {
  my $pid;
  while (($pid = waitpid(-1, &WNOHANG)) > 0) {
    # If this pid is not in the pid map, then we are harvesting one of
    #   our grandchildren, ignore it. 
    if (! defined ($pidMap{$pid})) {
      return;
    }

    $PROCCOUNT--;
  
    local($pipe) = $pidMap{$pid}{'PIPE'};
    @{ $res{ $pidMap{$pid} } } = <$pipe>;
    print "\n--> FINISHED: $pidMap{$pid} <--\n @{ $res{ $pidMap{$pid} } }\n\n";
    close($pipe);

    delete $pidMap{$pid} if $pidMap{$pid}; # Keep track of only what is running.
  }
} # reaper


# print the results from the scans
#
sub doSummary {
  # display results for parent only
  if ($$ == $myPid) {
    open (OUT, ">$outFile") || die("Unable to open: $outFile: $!"); 
    foreach $ip (sort byIP keys %res) { 
      next if !defined( @{ $res{$ip} } );
      foreach (@{ $res{$ip} }) {
        s/^ //;
        next if /Starting nmap /;
        next if /Nmap run completed --/;
        if (/Note: Host seems down/) { print OUT "Host seems down: $ip\n\n"; }
        else { print OUT; }
      } 
    }
    
    $sTSTART = scalar localtime($TSTART);
    $sTSTOP = scalar localtime($TSTOP);
    $mDiff = int(($TSTOP - $TSTART) / 60);
    $sDiff = sprintf("%02d", ($TSTOP - $TSTART) - 60 * $mDiff);
    print "(STATS) START: $sTSTART STOP: $sTSTOP DIFF: $mDiff\:$sDiff\n";
    print OUT "(STATS) START: $sTSTART STOP: $sTSTOP DIFF: $mDiff\:$sDiff\n";
    close(OUT);
  }
  #exit(0);
} #doSummary

# sort by IP address
#
sub byIP {
  my @oct_a = split /\./, $a;
  my @oct_b = split /\./, $b;

  $oct_a[0] <=> $oct_b[0] or
  $oct_a[1] <=> $oct_b[1] or
  $oct_a[2] <=> $oct_b[2] or
  $oct_a[3] <=> $oct_b[3] or
  $a cmp $b
} # byIP
