#!/usr/bin/env perl
# perl scan.pl -s 220.226.189.101 -o wow.txt
# RitX - Reverse IP Tool v1.3
# Copyright (C) 2011-2012
# r0b10S-12 <r12xr00tu@gmail.com>
# #p0c.cc

# Change Log:
# 1.3:
#   Rename the script to RitX.
#   Rewrite the entire code.
#   Now RitX is command line tool.
#   Better performance.
#   add the multi-threading functions.
#   Now results are more accurate.
#   Fix all broken Regex and bugs.
# 1.2:
#   Added 2 more websites .
#   Removed all dead services . 
#   Fix some bugs.
#   Made some changes.
# 1.0:
#   Rit initial release.

print "\n\t+-----------------------------+\n";
print "\t|           RitX 1.3          |\n";
print "\t|      Coded by r0b10S-12     |\n";
print "\t+-----------------------------+\n\n";

#use threads ( stack_size => 4096 );
#use threads::shared;
use LWP ();
#use warnings;
#use strict;
#use LWP::ConnCache ();
#use Getopt::Long;

# Provide a friendly message for missing modules...
my @Modules = ("threads","threads::shared","Getopt::Long","LWP::ConnCache");

foreach $module (@Modules)
{
    $can = eval "use $module;1;";
    if ($can && $module =~ /threads/)
    {
        # Do processing using threads
        $usethreads = 1;
    }
    elsif(!$can && $module =~ /threads/)
    {
        # Do it without using threads
        $usethreads = 0;
    }
    # The module isn't there
    if ($@ =~ /Can't locate/) {
        die "\n[!!] Seems that some module is missing...:\n".$@."\n";
    }
}

my $in:shared;
my @resx:shared;

$b = $0;
$b =~s/.*\///;
sub usage {
    print <<HELP;
Usage: perl $b [OPTIONS]
Options:
   -s, --target            Server hostname or ip (for best results use IP)
   -t, --timeout=SECONDS   Seconds to wait before timeout connection (default 30)
   -c, --check             Check web sites that are in the same IP address range
   -p, --print             Print results
   -o, --output=FILE       Save results to a file (default IP.txt)
   -h, --help              This message

   Threads:
   --threads=THREADS       Maximum number of concurrent ip checks (default 1) require --check

HELP
    exit;
}


# Process options.
if ( @ARGV > 0 )
{
    GetOptions( 's|target=s'  => \$target,
                't|timeout=i'  => \$timeout,
                'threads=i'  => \$threads,
                'c|check'  => \$check,
                'p|print'  => \$print,
                'o|output=s'  => \$filename,
                'h|help'    => \$help) or usage;
}
else
{
    print "[*] Usage    : perl $b [OPTIONS]\n";
    print "    EXEMPLE  : perl $b -s www.target.com -o result.txt\n\n";
    print "[*] Try 'perl $b -h' for more options.\n";
    exit;
}

$help and usage;
$target or usage;

if ($target =~ m/^([1-9]|1[0-9]{1,2}|2[0-4]\d|25[0-5])(\.([0-9]|1[0-9]{1,2}|2[0-4]\d|25[0-5])){3}$/)
{
    # nice do nothing
}
elsif ($target =~ /([a-z][a-z0-9\-]+(\.|\-*\.))+[a-z]{2,6}$/)
{
    $IP = getIP($target);
    if ($IP)
    {
        $target = $IP;
    }
    else
    {
        die "\n[!!] Unable to Resolve Host $target ! \n";
    }
}
else
{
    die "[-] Invalid Hostname or Ip address .\n";
}

# Global variables
$VERSION = "1.3";
$useragent   ||= 'Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.9.1) Gecko/20090624 Firefox/3.5'; 
$filename    ||= "$target.txt";
$timeout     ||= 30;

#-------------------------------------------------------------------------------#
$ua = LWP::UserAgent->new(agent => $useragent);
$ua->timeout($timeout);
$ua->max_redirect(0);
$ua->conn_cache(LWP::ConnCache->new());
print "\n[*] This operation will take little time ,Please wait...\n\n";
#-------------------------------------------------------------------------------#
print "[*] Processing:\n";
@R = (
    {
        SITE    =>    "Myipneighbors.net",
        URL        =>    "http://www.myipneighbors.net/?s=%s",
        REGEX    =>    '<\/tr><tr><td><a href="\/\?s\=.*?">(.*?)<\/a><\/td>',
    },
    {
        SITE    =>    "My-ip-neighbors.com",
        URL        =>    "http://www.my-ip-neighbors.com/?domain=%s",
        REGEX    =>    '<td class="action"\starget="\_blank"><a\shref="http\:\/\/whois\.domaintools\.com\/(.*?)"\starget="\_blank"\sclass="external">Whois<\/a><\/td>',
    },
    {
        SITE    =>    "Yougetsignal.com",
        DATA    =>    'remoteAddress',
        URL        =>    "http://www.yougetsignal.com/tools/web-sites-on-web-server/php/get-web-sites-on-web-server-json-data.php",
        SP        =>    'Yougetsignal()',
    },
    {
        SITE    =>    "Myiptest.com",
        URL        =>    "http://www.myiptest.com/staticpages/index.php/Reverse-IP/%s",
        REGEX    =>    "<td style='width:200px;'><a href='http:\/\/www.myiptest.com\/staticpages\/index.php\/Reverse-IP\/.*?'>(.*?)<\/a><\/td>",
    },
    {
        SITE    =>    "Whois.WebHosting.info",
        URL        =>    "http://whois.webhosting.info/%s",
        SP        =>    'Whoiswebhosting()',
    },
    {
        SITE    =>    "Ksasecurity.net",
        URL        =>    'http://www.ksasecurity.net/results-reverse.php?url=%s',
        REGEX    =>    "<a href='.*?' target='_blank'>http:\/\/(.*?)<\/a><\/li>",
    },
    {
        SITE    =>    'Domainsbyip.com',
        URL        =>    'http://domainsbyip.com/%s/', 
        REGEX    =>    '<li class="site.*?"><a href="http\:\/\/domainsbyip.com\/domaintoip\/(.*?)/">.*?<\/a>',
    },
    {
        SITE    =>    "Ip-adress.com",
        URL        =>    "http://www.ip-adress.com/reverse_ip/%s",
        REGEX    =>    '\[<a href="\/whois\/(.*?)">Whois<\/a>\]',
    },
    {
        SITE    =>    "Bing.com",
        URL        =>    "http://www.bing.com/search?q=ip:%s&filt=all",
        SP        =>    'Bing()',
    },
    {
        SITE    =>    "Sameip.org",
        URL        =>    "http://sameip.org/ip/%s/",
        REGEX    =>    '<a href="http:\/\/.*?" rel=\'nofollow\' title="visit .*?" target="_blank">(.*?)<\/a>',
    },
    {
        SITE    =>    "Robtex.com",
        URL        =>    "http://www.robtex.com/ajax/dns/%s.html",
        REGEX    =>    '<a href="\/dns\/.*?\.html" >(([a-z][a-z0-9\-]+(\.|\-*\.))+[a-z]{2,6})<\/a><br \/>',
    },
    {
        SITE    =>    "Reverseip.us",
        URL        =>    "http://www.reverseip.us/?url=%s",
        REGEX    =>    '<td bgcolor="\#EAEAEA" align="left">&nbsp;&nbsp;<a target="_blank" href="http\:\/\/.*?">(.*?)<\/a><\/td>',
    },
    {
        SITE    =>    "Tools.web-max.ca",
        URL        =>    "http://ip2web.web-max.ca/?byip=1&ip=%s",
        REGEX    =>    '<a href="http:\/\/.*?" target="_blank">(.*?)<\/a>',
    }
);

### Functions
sub add
{
    $x = lc($_[0]);
    ($x =~ /\:|freecellphonetracer|reversephonedetective|americanhvacparts|freephonetracer|p ​ hone\.addresses|reversephone\.theyellowpages|\.in-addr\.arpa|^\d+(\.|-)\d+(\.|-)/) ? return:0;
    $x =~ s/http:\/\/|\*\.|^www\.|\///;
    push(@JUNK,$x);
}
sub getIP
{
    @ip = unpack("C4",(gethostbyname($_[0]))[4]) or return;
    return join(".", @ip);
}

sub Req
{
    #print "$_[0]\n";
    $data = $_[1];
    if(!$data)
    {
        $res = $ua->get($_[0]);
    }
    else
    {
        $res = $ua->post($_[0], 
        {
            $data => $target,
        });
    }
    if($res->is_success)
    {
        #print $res->status_line."\n$_[0]\n";
    }
    else
    {
        print "[!] Error: ".$res->status_line."\n";
    }
    return $res->content;
}

sub Yougetsignal
{
    $resu = Req(sprintf($TARGET->{URL},$target),$TARGET->{DATA});
    while ($resu =~ m/\[([^\]]*)\]/g)
    {
        $s1 = $1;
        $s1 =~ m/\"(.*?)\", \"?\"/g;
        #push(@{$TARGET->{"$TARGET->{SITE}"}{DATOS}},$1);
        add($1);
        $n{$y}++;
    }
    if ($resu =~ m/"message":"Daily reverse IP check limit reached for .*\."/)
    {
        $n{$y} = "E1";
    }
}
sub Whoiswebhosting
{
    $resu = Req(sprintf($TARGET->{URL},$target));
    if ($resu =~ m/<\/a>&nbsp;&nbsp;&nbsp;<a href="\/.*?\?pi=(.*?)&ob=SLD&oo=ASC">&nbsp;&nbsp;Last&nbsp;&gt;&gt;<\/a><\/td>/g)
    {
        $nb = $1;
        for ($i=1;$i<=$nb;$i++)
        {
            $resu = Req(sprintf($TARGET->{URL},$target).'?pi='.$i.'&ob=SLD&oo=ASC');
            while ($resu =~ m/<td><a href="http:\/\/whois.webhosting.info\/.*?\.">(.*?)\.<\/a><\/td>/g )
            {
                #push(@{$TARGET->{"$TARGET->{SITE}"}{DATOS}},$1);
                add(lc($1));
                $n{$y}++;
            }
            if ($resu =~ m/The security key helps us prevent automated searches/i)
            { 
                $n{$y} = "E2";
                last;
            }
        }
    }
    else
    {
        while ($resu =~ m/<td><a href="http:\/\/whois.webhosting.info\/.*?\.">(.*?)\.<\/a><\/td>/g )
        {
            #push(@{$TARGET->{"$TARGET->{SITE}"}{DATOS}},$1);
            add(lc($1));
            $n{$y}++;
        }
        if ($resu =~ m/The security key helps us prevent automated searches/i)
        { 
            $n{$y} = "E2";
        }
    }
}

sub Bing
{
    for ($i=1;;$i+=10)
    {
        $resu = Req(sprintf($TARGET->{URL},$target).'&first='.$i);
        $resux = $resu;
        if ($resux =~ m/FORM=PORE" class="sb_pagN" onmousedown="return si_T\(.*?\)">.*?<\/a><\/li><\/ul>/g)
        {
            while ($resu =~ m/<\/p><div class="sb_meta"><cite>(.*?)<\/cite>/g)
            {
                $b = $1;
                $b =~ s/\/.*+// if ($b =~ /\//);
                #push(@{$TARGET->{"$TARGET->{SITE}"}{DATOS}},$b);
                add($b);
                $n{$y}++;
            }
        }
        else
        {
            while ($resu =~ m/<\/p><div class="sb_meta"><cite>(.*?)<\/cite>/g)
            {
                $b = $1;
                $b =~ s/\/.*+// if ($b =~ /\//);
                #push(@{$TARGET->{"$TARGET->{SITE}"}{DATOS}},$b);
                add($b);
                $n{$y}++;
            }
            last;
        }
    }
}
sub check
{
    if((getIP('www.'.$_[0])==$target)or(getIP($_[0])==$target))
    {
        $in++;
        print "    Found : $_[0]\n";
        #$resx[$in+1]=$_[0];
        push(@resx,$_[0]);
    }
    #else
    #{
    #    print "\r    Try $_[0]\t\t\t";
    #}
}

#-------------------------------------------------------------------------------#
foreach $TARGET (@R)
{
    $y++;
    syswrite(STDOUT,"   -> $TARGET->{SITE}\n");
    if(!$TARGET->{SP})
    {
        $res=Req(sprintf($TARGET->{URL},$target),$TARGET->{DATA});
    }
    else
    {
        eval($TARGET->{SP});
        next;
    }
    $match = $TARGET->{REGEX};
    while($res =~ m/$match/gi)
    {
        #push(@{$TARGET->{"$TARGET->{SITE}"}{DATOS}},$1);
        add($1);
        $n{$y}++;
    }
}

#foreach $TARGET (@R)
#{
#    syswrite(STDOUT,"  + $TARGET->{SITE}\n");
#    foreach $aaa (@{$TARGET->{"$TARGET->{SITE}"}{DATOS}})
#    {
#        syswrite(STDOUT,"    - $aaa\n");
#    }
#}
#-------------------------------------------------------------------------------#
@result = sort(grep { ++$R12{$_} < 2 } @JUNK);

if ($check)
{
    print "\n[x] Checking and cleaning the results\n";
    if ($threads && $usethreads)
    {
        foreach $tr (@result) 
        {
            $t++;
            threads->create(\&check,$tr)->detach();
            if($t=$threads)
            {
                while(threads->list()>0)
                {
                    sleep 2;
                }
                $t=0;
            }
        }
    }
    elsif ($threads && !$usethreads)
    {
        print "[-] Sorry your PERL installation doesn't support threads!\n";
        &check($_) foreach @result;
    }
    elsif (!$threads)
    {
        &check($_) foreach @result;
    }
    sleep 2;
    @result = @resx;
    print "[+] Done\n";
}
print "\n[x] Result of $target : \n\n";
open (F,">$filename") or die ("\n[!] Can't create the file ($filename)\n");
print F "# Genereted By RitX $VERSION\n";
print F "# Those are the domains hosted on the same web server as ($target).\n\n";
foreach $RD (@result) 
{
    print F "$RD\n" if ($RD);
    $ny++;
}
close(F);

for ($i=0;$i<=14;$i++)
{
        $n{$i} = 0 if (!$n{$i});
}

print "                        +------+\n";
print "                        |  NB  |\n";
print "+-----------------------+------+\n";
print "| Myipneighbors.net     |  $n{1}\n";
print "|------------------------------|\n";
print "| My-ip-neighbors.com   |  $n{2}\n";
print "|------------------------------|\n";
print "| Yougetsignal.com      |  $n{3}\n";
print "|------------------------------|\n";
print "| Myiptest.com          |  $n{4}\n";
print "|------------------------------|\n";
print "| Whois.webhosting.info |  $n{5}\n";
print "|------------------------------|\n";
print "| Ksasecurity.net       |  $n{6}\n";
print "|------------------------------|\n";
print "| Domainbyip.com        |  $n{7}\n";
print "|------------------------------|\n";
print "| Ip-adress.com         |  $n{8}\n";
print "|------------------------------|\n";
print "| Bing.com              |  $n{9}\n";
print "|------------------------------|\n";
print "| Sameip.org            |  $n{10}\n";
print "|------------------------------|\n";
print "| Robtex.com            |  $n{11}\n";
print "|------------------------------|\n";
print "| Reverseip.us          |  $n{12}\n";
print "|------------------------------|\n";
print "| Tools.web-max.ca      |  $n{13}\n";
print "+-------------+----------------+\n";
print "              | Total   |  $ny\n";
print "              +----------------+\n";
if (($n{5} or $n{3}) =~ /E/)
{
    print "+--Keys------------------------------------+\n";
    print "|E1: Daily reverse IP check limit reached .|\n";
    print "|E2: Some Security Measures (Captcha) .    |\n";
    print "+------------------------------------------+\n";
}
if ($ny != 0 and $print)
{
    print "[+] Results:\n";
    foreach $RD (@result) 
    {
        $v++;
        print "  $RD\n";
        if($v==20){<STDIN>;$v=0;};
    }
}
print "[+]  Scan Finished, have a nice hacking :p\n\n";
#-------------------------------------------------------------------------------#