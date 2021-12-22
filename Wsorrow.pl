#!/usr/bin/perl 

# Copyright 2012-2013 Dakota Simonds
# A small portion of this software is from Lilith 6.0A and is Sited.
# sub MatchDirIndex (very modified) Copyright (c) 2003-2005 Michael Hendrickx

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

# VERSION 1.5.0FINAL
# You can't enslave protocals. I dedicate this program to the EFF, anonymous, and all other internet freedom fighters.

BEGIN { # it seems to load faster. plus outputs the name and version faster
		print "\n[+] Web-Sorrow v1.5.0FINAL http enumeration security tool\n";

		use LWP::UserAgent;
		use LWP::ConnCache;
		use HTTP::Request;
		use HTTP::Response;
		use Getopt::Long qw( GetOptions );
		use Socket qw( inet_aton );
		use encoding 'UTF-8';
		
		use strict;
		use warnings;
}


				my $i;
				my $Opt;
				my $Host = "none";
				my $Port = 80;
				my @FoundMatchItems;
				
				my $ua = LWP::UserAgent->new(conn_cache => 1);
				my $cache = LWP::ConnCache->new;
				$ua->conn_cache($cache); # use connection cacheing (faster)
				$ua->timeout(2);         # don't wait longer then 2 secs
				$ua->max_redirect(1);    # if set to 0 it messes up directory indexing
				$ua->agent("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.5) Gecko/20031027");
				
				GetOptions(
						"host=s"    => \$Host,             # host ip or domain
						"port=i"    => \$Port,             # port number
						"S"         => \my $S,             # Standard checks
						"auth"      => \my $auth,          # MEH!!!!!! self explanitory
						"Cp=s"      => \my $cmsPlugins,    # cms plugins
						"I"         => \my $interesting,   # find interesting text
						"Ws"        => \my $Ws,            # Web services
						"e"         => \my $e,             # EVERYTHINGGGGGGGG
						"proxy=s"   => \my $ProxyServer,   # use a proxy
						"Fd"        => \my $Fd,            # files and dirs
						"ninja"     => \my $nin,           # use ancient ninja methods
						"Db"        => \my $DirB,          # use dirbuster database
						"ua=s"      => \my $UserA,         # userAgent
						"Sd"        => \my $SubDom,        # subdomain
						"R"         => \my $RangHeader,    # do range reqs
						"Shadow"    => \my $shdw,          # req from google cache
						"Df=s"      => \my $Df,            # default files
						"d=s"       => \my $Dir,           # scan within this dir
						"dp"        => \my $doPasive,      # do passive
						"fuzzsd"    => \my $fuzzsd,        # fuzz source disclosure
						"Sfd"       => \my $Sfd,           # Small Files dirs Enum
						"Rua"       => \my $randUA,        # random UA
						"gzip"      => \my $Gzip,          # use gzip compression
						"https"     => \my $httpsMode,     # use ssl
						"nr"        => \my $noRespAnal,    # skip responce anal
						"intense"   => \my $intenseScan,   # like -e
						"die"       => \my $DieOnHostCheck,# die! die! die!
						"reject=i"  => \my $RejectCode,    # reject this code
						"flag=s"    => \my $Flag,          # warn user when supplied content is found
						"nyan"      => \my $nyancat,       # a prize for those who read the source
				);

				
				# usage
				if($Host eq "none") {
						usage();
						exit();
				}

				study $Host;
				
				#ssl stuff
				my $URNtype = "http";
				if(defined $httpsMode or $Host =~ m/^https:\/\//i){ # enable ssl

						print "[+] Protocol: HTTPS\n";
						$URNtype = "https";
						$ua->protocols_allowed(['https', 'http']);
						$ua->ssl_opts(verify_hostname => 1);
						
				}
				nossl:
				
				if($Host =~ m/^http:\/\//i) { #check host input
						$Host =~ s/http:\/\///gi;
						$Host =~ s/\/.*//g;
				}
				
				$ua->default_headers->header('Accept' => '*.*, q=0.1');# bug reported by google code user aran.lora
				$ua->default_headers->header('Accept-Encoding' => 'gzip, deflate') if(defined $Gzip);# compresses http responces from host (faster)
				
				if($Host =~ m/;$/){
					chop $Host;
				}
				
				foreach ( split(/;/, $Host) ) { # if imput is more than one host do banner for each
						print "[+] Host: $_\n";
				}
				
				#host noteasions <- my teachers are so proud
				if($Host =~ m/\*/){
				
					if($Host =~ /.*?\*.*\*/){
						print "\n[X] Sorry. you can only use 1 '*' in host\n";
						exit();
					}
				
					my $Count = 0;
					$Host = $Host . ";";
					$Host = $Host x 255;
					chop $Host; # it's not every day that you get to use this function
					
					for($i = 0;$i < 255;$i++){
						$Count = $Count + 1;
						$Host =~ s/\*/$Count/;
					}
					
					$Count = 0;
				}
				
					
				if($Host =~ m/\d-\d/){
					my $Count = 0;
					my $HostRangeR = $Host;
					my $HostRangeL = $Host;
					
					$HostRangeR =~ s/.*(\d|\d\d|\d\d\d)-//;
					$HostRangeR =~ s/\..*//;
					$HostRangeL =~ s/-(\d|\d\d|\d\d\d).*//;
					$HostRangeL =~ s/.*\.//;
					
					my $RangeNum = $HostRangeR - $HostRangeL;
					$RangeNum = $RangeNum + 1; #fixes obo error
					my $baseNum = $HostRangeL;
					
					$Host = $Host . ";";
					$Host = $Host x $RangeNum;
					chop $Host;
					
					for($i = 0;$i < $RangeNum;$i++){
						
						$Count = $Count + 1;
						$Host =~ s/(\d|\d\d|\d\d\d)-(\d\d\d|\d\d|\d|)/$Count/;
						
					}
					
				}
				
				
				print "[+] Proxy: $ProxyServer\n" if(defined $ProxyServer);
				
				print "[+] Start Time: " . localtime() . "\n";
				print "=" x 70 . "\n";

				$ua->agent($UserA) if(defined $UserA) ;
				$ua->proxy(['http', 'https', 'gopher'],"http://$ProxyServer") if(defined $ProxyServer) ; # always make sure to put this first, lest we send un-proxied packets
				$ua->default_headers->header('Range' => 'bytes=0-1') if(defined $RangHeader);
				
				
				if(defined $RangHeader and not defined $noRespAnal){
					print "[*] you might want to use -nr with -R for a cleaner scan\n";
					sleep(3);
				}
				
				
				if(defined $shdw) {
						print "[-] The cached pages MAYBE out of date so the results maynot be perfect\n";
						$Host = ShadowScan();
						if(defined $SubDom) {
								print "[x] -Sd does not work with -Shadow... disabling\n";
								undef($SubDom);
						}
				}
				
				print "[+] All reported items are within $Dir\n" if(defined $Dir) ;
				
				#swiched up my style a bit here
				if($Host =~ ';')
				{
						my @Hosts = split(/;/, $Host); 

						foreach(@Hosts)
						{
								$Host = $_;
								$Host = $Host . ":$Port" unless($Port == 80) ;
								
								print "=" x 70 . "\n[+] Scanning Host: $Host\n";
								print "=" x 70 . "\n";
								if( &checkHostAvailibilty() =~ "faild" and defined $DieOnHostCheck){
									print "[-] Host check failed. canceling scan agianst host\n";
									next;
								}
								startScan();
						}
				}
					else
				{
						$Host = $Host . ":$Port" unless($Port == 80);				
						startScan(); 
				}
				
				
				sub startScan{ #triger scans
						
						if(defined $Dir) {
								chop($Dir) if $Dir =~ m/\/$/;
								$Dir = "/" . $Dir unless $Dir =~ m/^\//;
								$Host = $Host . $Dir;
						}

						
						# in order of aproximate finish times
						if(defined $S)           { Standard()            ;}
						if(defined $nin)         { Ninja()               ;}
						if(defined $auth)        { auth()                ;}
						if(defined $Ws)          { webServices()         ;}
						if(defined $Sfd)         { SmallFdEnum()         ;}
						if(defined $Df)          { defaultFiles()        ;}
						if(defined $cmsPlugins)  { cmsPlugins()          ;}
						if(defined $SubDom)      { SubDomainBF()         ;}
						if(defined $Fd)          { FilesAndDirsGoodies() ;}
						if(defined $DirB)        { Dirbuster()           ;}
						if(defined $e)           { runAll()              ;}
						if(defined $intenseScan) { runIntense()          ;}
						
						
						
						sub runAll{
								print "[!] SCAN EVERTHING!!!!!!!!!!!!!\n";
								Standard();
								auth();
								webServices();
								defaultFiles();
								SubDomainBF();
								cmsPlugins();
								FilesAndDirsGoodies();
								Dirbuster();
						}
						
						sub runIntense{
							my $interesting;
							my $fuzzsd;
							my $doPasive;
							Standard();
							auth();
							webServices();							
							defaultFiles();
						}
				}


				print "=" x 70 . "\n";
				print "[+] Done :'(  -  Finsh Time: " . localtime() . "\n";







#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------


# non scanning subs for clean code and speed 'n stuff

sub usage{

print q{
Remember to check for updates http://web-sorrow.googlecode.com/
also it would be a good idea to read readme.txt lots if tips and info in there

Usage: perl Wsorrow.pl [HOST OPTIONS] [SCAN(s)] [SCAN SETTING(s)]

HOST OPTIONS:
    -host [host]     --  Defines host to scan, a list separated by
                         semicolons, 1.1.1.30-100 type ranges, and
                         1.1.1.* type ranges. You can also use the
                         1.1.1.30-100 type ranges for domains
                         like www1-10.site.com
    -port [port num] --  Defines port number to use (Default is 80)
    -proxy [ip:port] --  Use an HTTP, HTTPS, or gopher proxy server


SCANS:
    -S          --  Standard set of scans including: agresive directory indexing,
                    Banner grabbing, Language detection, robots.txt,
                    HTTP 200 response testing, Apache user enum, SSL cert,
                    Mobile page testing, sensitive items scanning,
                    thumbs.db scanning, content negotiation, and non port 80
                    HTTP port sweeps
    -auth       --  Scan for login pages, admin consoles, and email webapps
    -Cp [dp | jm | wp | all] scan for cms plugins.
                    dp = drupal, jm = joomla, wp = wordpress 
    -Fd         --  Scan for common interesting files and dirs (Bruteforce)
    -Sfd        --  Very small files and dirs enum (for the sake of time)
    -Sd         --  BruteForce Subdomains (host given must be a domain. Not an IP)
    -Ws         --  Scan for Web Services on host such as: cms version info, 
                    blogging services, favicon fingerprints, and hosting provider
    -Db         --  BruteForce Directories with the big dirbuster Database
    -Df [option]    Scan for default files. platfroms/options: Apache,
                    Frontpage, IIS, Oracle9i, Weblogic, Websphere,
                    MicrosoftCGI, all (enables all)
    -ninja      --  A light weight and undetectable scan that uses bits and
                    peices from other scans (it is not recomended to use with any
                    other scans if you want to be stealthy. See readme.txt)
    -fuzzsd     --  Fuzz every found file for Source Disclosure
    -e          --  Everything. run all scans
    -intense    --  like -e but no bruteforce
    -I          --  Passively scan interesting strings in responses such as:
                    emails, wordpress dirs, cgi dirs, SSI, facebook fbids,
                    and much more (results may Contain partial html)
    -dp         --  Do passive tests on requests: banner grabbing, Dir indexing,
                    Non 200 http status, strings in error pages,
                    Passive Web services
    -flag [txt] --  report when this text shows up on the responces.

SCAN SETTINGS:
    -ua [ua] --  Useragent to use. put it in quotes. (default is firefox linux)
    -Rua     --  Generate a new random UserAgent per request
    -R       --  Only request HTTP headers via ranges requests.
                 This is much faster but some features and capabilitises
                 May not work with this option. But it's perfect when
                 You only want to know if something exists or not.
                 Like in -auth or -Fd
    -gzip    --  Compresses http responces from host for speed. Some Banner
                 Grabbing will not work
    -d [dir] --  Only scan within this directory
    -https   --  Use https (ssl) instead of http
    -nr      --  Don't do responce analisis IE. False positive testing,
                 Iteresting headers (other than banner grabbing) if
                 you want your scan to be less verbose use -nr
    -Shadow  --  Request pages from Google cache instead of from the Host.
                 (mostly for just -I otherwise it's unreliable)
    -die     --  Stop scanning host if it appears to be offline
    -reject  --  Treat this http status code as a 404 error

EXAMPLES:
    perl Wsorrow.pl -host scanme.nmap.org -S
    perl Wsorrow.pl -host nyan.cat -Fd -fuzzsd
    perl Wsorrow.pl -host nationalcookieagency.mil -Cp dp,jm -ua "script w/ the munchies"
    perl Wsorrow.pl -host chatrealm.us -d /wordpress -Cp wp
    perl Wsorrow.pl -host 66.11.227.35 -port 8080 -proxy 129.255.1.17:3128 -S -Ws -I
};

}

sub checkHostAvailibilty{
		my $CheckHost = $ua->get("$URNtype://$Host/");
		my $out;
		
				analyzeResponse($CheckHost->decoded_content, "/") unless(defined $noRespAnal);
				interesting($CheckHost->decoded_content,"/") if(defined $interesting);
				
				if($CheckHost->is_success or $CheckHost->code == 401 or $CheckHost->code == 403) {
						$out = "passed";
				} else {
					$out = "faild";
				}
	
	return($out);
}

sub PromtUser{ # Yes or No?
		my $PromtMSG = shift; # i find the shift is much sexyer then then @_
		
				print $PromtMSG;
				$Opt = <stdin>;
				return $Opt;
}

sub analyzeResponse{ # heres were most of the smart is...
		my $CheckResp = shift;
		my $checkURL = shift;
		
				unless($checkURL =~ m/^\//) {
						$checkURL = "/" . $checkURL; # makes for good output
				}
				
				
				my $FoundErrors = 0;
				#False Positive checking based on page content
				my @PosibleErrorStrings = (
											'404 error',
											'404 page',
											'error 404', 
											'not found',
											'cannot be found',
											'could not find',
											'can\'t find',
											'cannot found', # incorrect english but i'v seen it before
											'could not be found',
											'bad request',
											'server error',
											'temporarily unavailable',
											'not exist',
											'unable to open',
											'check your spelling',
											'an error has occurred',
											'an error occurred',
											'request has been blocked',
											'an automated process',
											'nothing found',
											'Request aborted',
											'no such page',
											'no se encontr.',# spanish
											'pas trouv.e',# french
											'nicht gefunden',# german
											'no text in this page',
											'just calm down. 420',
				);
				
				my @ErrorStringsFound;
				foreach my $errorCheck (@PosibleErrorStrings) {
						if($CheckResp =~ m/$errorCheck/i) {
								push(@ErrorStringsFound, "\"$errorCheck\" ");
								$FoundErrors = 1;
						}
				}
				if($FoundErrors) { # if the page contains multi error just put em into the same string
						print "[-] Item \"$checkURL\" Contains text(s): @ErrorStringsFound MAYBE a False Positive!\n";
				}
				undef(@ErrorStringsFound); # emty array. saves the above if for the next go around
						
						
				# Login Page detection
				unless(defined $auth) { # that would make me a SAD panda :(
						my @PosibleLoginPageStrings = ('login','log-in','sign( |)in','logon',);
						foreach my $loginCheck (@PosibleLoginPageStrings) {
								if($CheckResp =~ m/<title>.*$loginCheck.*<\/title>/i) {
										print "[+] Item \"$checkURL\" Contains text: \"$loginCheck\" in the title MAYBE a Login page\n";
								}
						}
				}
				
				
				
				foreach my $analHString ( getHeaders($CheckResp) ) {
						study $analHString;
						#the page is empty?
						if($analHString =~ m/Content-Length:( |)(0|1|2|3|4|5|6)$/i) {  print "[-] Item \"$checkURL\" contains header: \"$analHString\" MAYBE a False Positive or is empty!\n\n" unless $checkURL eq "/java-sys/";  }
						
						#auth page checking
						if($analHString =~ m/www-authenticate:/i) {  print "[+] Item \"$checkURL\" uses HTTP basic auth (www-authenticate)\n\n";  }
						
						#a hash?
						if($analHString =~ m/Content-MD5:/i) {  print "[+] Item \"$checkURL\" contains header: \"$analHString\" Hmmmm\n\n";  }
						
						#redircted me?
						if($analHString =~ m/refresh:( |)\D/i) {  print "[-] Item \"$checkURL\" looks like it redirects. header: \"$analHString\"\n\n";  }
						
						if($analHString =~ m/HTTP\/1\.(1|0) 30(1|2|7)/i) { print "[-] Item \"$checkURL\" looks like it redirects. header: \"$analHString\"\n\n"; }
								
						if($analHString =~ m/location:/i) {
								my ($dontkare, $lactionEnd) = split(/:/,$analHString);
								unless($lactionEnd =~ m/($checkURL|index\.)/i) {
										print "[-] Item \"$analHString\" does not match the requested page: \"$checkURL\" MAYBE a redirect?\n\n";
								}
						}
				}
				
				undef($CheckResp);
}

sub genErrorString{
		my $errorStringGGG = "";
		for($i = 0;$i < 20;$i++) {
				$errorStringGGG .= chr((int(rand(93)) + 33)); # random 20 bytes to invoke 404 sometimes 400
		}
		
		$errorStringGGG =~ s/(#|&|\?|\/|\[|\])//g; #strip anchors and q stings and such
		return $errorStringGGG;
}

sub getHeaders{ #simply extract http headers
		my $rawFullPage = shift;
		
				my @headersChop = split(/\n\n/, $rawFullPage);
				my @HeadersRetu = split(/\n/, $headersChop[0]);
				
				undef($rawFullPage);
				undef(@headersChop);
				
				return(@HeadersRetu);
}

sub RandomUA{
		
		my @UAlist = (
					"Mozilla/3.0 (compatible; Opera/3.0; Windows 3.1) v3.1",
					"Mozilla/3.0 (compatible; Opera/3.0; Windows 95/NT4) 3.2",
					"Mozilla/3.01 (compatible; Netbox/3.5 R92; Linux 2.2)",
					"Mozilla/4.0 (compatible; MSIE 4.01; Windows 95)",
					"Mozilla/4.05 (Macintosh; I; 68K Nav)",
					"Mozilla/4.05 (Macintosh; I; PPC Nav)",
					"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/xxx.x (KHTML like Gecko) Safari/12x.x",
					"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:x.x.x) Gecko/20041107 Firefox/x.x",
					"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:x.xx) Gecko/20030504 Mozilla Firebird/0.6",
					"Opera/9.0 (Windows NT 5.1; U; en)",
					"Opera/9.00 (Windows NT 5.1; U; de)",
					"Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)",
					"Mozilla/5.0 (X11; U; Linux 2.4.2-2 i586; en-US; m18) Gecko/20010131 Netscape6/6.01",
					"Mozilla/5.0 (X11; U; Linux i686; de-AT; rv:1.8.0.2) Gecko/20060309 SeaMonkey/1.0",
					"Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.7.6) Gecko/20050405 Epiphany/1.6.1 (Ubuntu) (Ubuntu package 1.0.2)",
					"Mozilla/5.0 (X11; U; Linux i686; en-US; Nautilus/1.0Final) Gecko/20020408",
					"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.3) Gecko/20010801",
				);
				
				return( $UAlist[( int( rand(6) + rand( (rand(6) + rand(5)) )  ) )] ); #random UserAgent
}

sub oddHttpStatus{ # Detect when there an odd HTTP status also other headers
		my $StatusToMine = shift;
		my $StatusFrom = shift;
				
				unless($StatusFrom =~ m/^\//) {
						$StatusFrom = "/" . $StatusFrom; # makes for good output
				}
				
				my @StatMine = split("\n",$StatusToMine);
				my $StatCode = $StatMine[0];
				study $StatCode;
				
				if($StatCode =~ m/HTTP\/1\.(0|1) 401/i) {
						print "[*] \"$StatusFrom\" HTTP status: \"401 authentication required\"\n";
				}
				if($StatCode =~ m/HTTP\/1\.(0|1) 403/i) {
						print "[*] Item \"$StatusFrom\" HTTP status: \"403 Forbiden\" (exists but denied access)\n"; 
				}
				if($StatCode =~ m/HTTP\/1\.(0|1) 424/i) {
						print "[-] Item \"$StatusFrom\" responded with HTTP status: \"424 Locked\"\n"; 
				}
				if($StatCode =~ m/HTTP\/1\.(0|1) 429/i) {
						print "[-] Item \"$StatusFrom\" responded with HTTP status: \"429 Too Many Requests\" Try -ninja\n"; 
				}
				if($StatCode =~ m/HTTP\/1\.(0|1) 509/i) {
						print "[-] Item \"$StatusFrom\" responded with HTTP status: \"509 Bandwidth Limit Exceeded\" Try -ninja\n"; 
				}
				if($StatCode =~ m/HTTP\/1\.(1|0) 30(1|2|7)/i) { print "[-] Item \"$StatusFrom\" redirects to something. header: \"$StatCode\"\n"; }
				
				ErrorStrings($StatusToMine, $StatusFrom);
				
				undef(@StatMine); undef($StatusToMine);
}

sub dataBaseScan{ # use a database for scanning.
		my $DataFromDB = shift;
		my $MatchFromCon = shift;
		my $scanMSG = shift;
		my $databaseContext = shift;
		my $FoundBefor = 0;
		chomp($DataFromDB, $scanMSG);
						
						if($databaseContext eq "nonSynt" or $databaseContext eq "Synt") {# send req and validate
								
								if ($databaseContext eq "Synt") {
										my ($JustDirDB, $MSG) = split(';',$DataFromDB) ;
										unless($JustDirDB =~ m/^\//) {
												$JustDirDB = "/" . $JustDirDB unless $databaseContext eq "match";
										}
										makeRequest($JustDirDB, $MSG, $scanMSG, $databaseContext); # if i put this code elswere it breaks WFT? vars are being kidnaped!
								} elsif($databaseContext eq "nonSynt") {
										my $JustDirDB = $DataFromDB;
										unless($JustDirDB =~ m/^\//) {
												$JustDirDB = "/" . $JustDirDB unless $databaseContext eq "match";
										}
										makeRequest($JustDirDB, $MSG, $scanMSG, $databaseContext); # if i put this code elswere it breaks WFT? vars are being kidnaped!
								}
						}
				
				
		
				
				if($databaseContext eq "match") {
						my ($MatchDataFromDB, $MSG) = split(';',$DataFromDB);
						
						if($MatchFromCon =~ m/$MatchDataFromDB/i) {
								 foreach my $MatchItemFound (@FoundMatchItems) {
										if($MatchItemFound eq $MSG) {
												$FoundBefor = 1; # set true
										}
								}
								push(@FoundMatchItems, $MSG);
						
								unless($FoundBefor) { #prevents double output
										unless($scanMSG eq "") {
												print "[+] $scanMSG $MSG\n";
										} else {
												print "[+] $MSG\n";
										}
								}
						}
				}
		
		undef($DataFromDB); undef($MatchFromCon); undef($scanMSG);
}

sub makeRequest{
		my $JustDirDBB = shift; #to lazy to makeup new var names
		my $MSGG = shift;
		my $scanMSGG = shift;
		my $databaseContextt = shift;
						
				$ua->agent( RandomUA() ) if(defined $randUA);
				
				$JustDirDBB = $JustDirDBB . "/" unless $JustDirDBB =~ m/(\.|\/$)/; # make dir proper format
				my $Testreq = $ua->get("$URNtype://$Host" . $JustDirDBB);
				my $responceCode = $Testreq->code; #only needs to be calulated once.
				
				if(defined $RejectCode and $responceCode == $RejectCode){
					goto nocigar;
				}
				
				if($Testreq->code == 401 or $responceCode == 403) {
						print "HTTP CODE: " . $responceCode . " -> "; #I LOVE ALL CAPPS!!!!
				}
				
				if($Testreq->is_success or $responceCode == 401 or $responceCode == 403) {
						if($databaseContextt eq "Synt") {
								
								print "[+] $MSGG: $JustDirDBB\n";

						} else {

								unless($scanMSGG eq "") {
								
										print "[+] $scanMSGG $JustDirDBB\n";
								
								} else {
								
										print "[+] $JustDirDBB\n";
										
								}
						
						}
						
						analyzeResponse($Testreq->as_string, $JustDirDBB) unless(defined $noRespAnal);
						sourceDiscolsure($JustDirDBB) if (defined $fuzzsd or defined $e);
						PassiveTests($Testreq->as_string, $JustDirDBB);
				}
				
				if(defined $Flag and $Testreq->decoded_content =~ m/$Flag/i and length $Testreq->decoded_content > 1){
					print "[+] FLAG: http $responceCode -> $JustDirDBB\n";
				}
				
				nocigar:
				oddHttpStatus($Testreq->as_string, $JustDirDBB) if(defined $doPasive); # can't put in repsonceAnalysis cuz of ->is_success
		
		undef($DataFromDBB); undef($scanMSGG);
}

sub bannerGrab{
		my $resP = shift;
		$FoundBefor = 0;

				my @checkHeaders = (
									'server:',
									'x-powered-by:',
									'x-meta-generator:',
									'x-meta-framework:',
									'x-meta-originator:',
									'x-aspnet-version:',
									'via:',
									'MIME-Version:',
									);
				

				foreach my $HString ( getHeaders($resP) ) {
		
						foreach my $checkSingleHeader (@checkHeaders) {
						
										if($HString =~ m/$checkSingleHeader/i) {
												foreach my $MatchItemFound (@FoundMatchItems) {
														if($MatchItemFound eq $HString) {
																$FoundBefor = 1; # set true
														}
												}
												push(@FoundMatchItems, $HString);
										
												unless($FoundBefor) { #prevents double output
														print "[+] Server Info in Header: \"$HString\"\n";
												}
										}
						}
				}
				undef($resP);
}

sub MatchDirIndex{
		my $IndexConFind = shift;
		my $dirr = shift;

				# Apache
				if($IndexConFind =~ m/<H1>Index of \/.*<\/H1>/i) {
						print "[+] Directory indexing found in \"$dirr\"\n";
				}

				# Tomcat
				if($IndexConFind =~ m/<title>Directory Listing For \/.*<\/title>/i and $IndexConFind =~ m/<body><h1>Directory Listing For \/.*<\/h1>/i) {
						print "[+] Directory indexing found in \"$dirr\"\n";
				}

				# iis
				if($IndexConFind =~ m/<body><H1>$Host - $dirr/i) {
						print "[+] Directory indexing found in \"$dirr\"\n";
				}
				
		undef($IndexConFind); undef($dirr);
}

sub Robots{
		my $roboTXT = $ua->get("$URNtype://$Host/robots.txt");
		unless($roboTXT->is_error) {
				my $Opt = PromtUser("[+] robots.txt found! This could be interesting!\n[?] would you like me to display it? (y/n) ? ");

				if($Opt =~ m/y/i) {
						print "[+] robots.txt Contents: \n";
						my $roboContent = $roboTXT->decoded_content;
						while ($roboContent =~ /(\n\n|\t)/) {		$roboContent =~ s/(\n\n|\t)/\n/g;		} # cleaner. some robots have way to much white space
						chomp $roboContent; #prevents duble newlines
								
						if($roboContent =~ /(<!DOCTYPE|<html)/i) {
								print "[x] robots.txt contains HTML. canceling display\n";
						} else {
								print $roboContent . "\n";
						}
				}
		}
		
		undef($roboTXT); undef($roboContent);
}

sub sourceDiscolsure{
		my $PathToSDis = shift;
				
				my @SDisAttackPatterns = (
										"?-s",
										"%70",
										".%E2%73%70",
										"%2e0",
										"%2e",
										".",
										"\\",
										"/",
										"?*",
										"%20",
										".%20",
										"+",
										"%00",
										"%2f",
										"%5c",
										"+.htr",
										"::DATA\$",
										"::\$DATA",
										"..%255c",
										".%5c../..%5c",
										"/..%c0%9v../",
										"/..%c0%af../",
										"/..%255c..%255c",
				);
				
				foreach my $SDisAP (@SDisAttackPatterns) {
						$ua->agent( RandomUA() ) if defined $randUA;
						my $SDisReq = $ua->get("$URNtype://$Host"."$PathToSDis"."$SDisAP");
						if($SDisReq->is_success and $SDisReq->decoded_content =~ /(<\?php|&lt;\?php|#include <|#!\/usr|#!\/bin|import java\.|public class .+\{|<\%.+\%>|<asp:|package\s.+\;.*)/i) {
								print "[+] Source Disclosure Found in script \"$PathToSDis$SDisAP\"\n";
						}
				}
				
				if($PathToDis =~ /asp$/) { # special asp test
						$PathToDis =~ s/asp/%61%73%70/;
						$ua->agent( RandomUA() ) if defined $randUA;
						$SDisReq = $ua->get("$URNtype://$Host"."$PathToSDis");
						if($SDisReq->decoded_content =~ /<asp:/) {
								print "[+] Source Disclosure Found in script \"$PathToSDis\"\n";
						}
						$PathToDis =~ s/%61%73%70/asp/;
				}
				
				foreach my $BeforPattern ("/...", "/", "/..%c0%9v.." ,"/..%c0%af..", ".%5c../..%5c", "/..%255c..%255c") {
						$ua->agent( RandomUA() ) if defined $randUA;
						$SDisReq = $ua->get("$URNtype://$Host".$BeforPattern."$PathToSDis");
						if($SDisReq->decoded_content =~ /(<\?php|&lt;\?php|#include <|#!\/usr|#!\/bin|import java\.|public class .+\{|<\%.+\%>|<asp:|package\s.+\;.*)/i) {
								print "[+] Source Disclosure Found in script \"$BeforPattern$PathToSDis\"\n";
						}
				}
				
				$SDisReq = undef;
}

sub PassiveTests{
		my $PassiveCon = shift;
		my $PassiveURL = shift;
				
				interesting($PassiveCon,$PassiveURL) if(defined $interesting or defined $nin or defined $e); # anything intsting here?
				MatchDirIndex($PassiveCon,$PassiveURL) if(defined $doPasive);
				WScontent($PassiveCon) if(defined $Ws);
				bannerGrab($PassiveCon) if(defined $doPasive);
}

if(defined $nyancat){

print q{
                      +             *            /\_/\            *
        +       *              +        ========( ^ ^ )    +
*     ---------           ----------- || .. . .||  w  
------------------------------------- ||. . . .||
-------------------------------------   ========              *
------------------------------------- 88    *  88      +
-----   +       ---------    *                                       +
  *               *     +        *         +        *
};

}


#---------------------------------------------------------------------------------------------------------------
# scanning subs



sub Standard{ #some standard stuff
				$ua->agent( RandomUA() ) if defined $randUA;
				bannerGrab($ua->get("$URNtype://$Host/")->as_string);
				
				sourceDiscolsure("/") if defined $fuzzsd or defined $e;
				foreach my $getTitle( getHeaders($ua->get("$URNtype://$Host/")->as_string) ) {
						if($getTitle =~ m/Title:/i) {
								$getTitle =~ s/Title://i;
								print "[+] HTTP Title: $getTitle\n";
						}
						if($getTitle =~ m/^Date:/i) {
								$getTitle =~ s/Date://i;
								print "[+] HTTP Date: $getTitle\n";
						}
				}
				
				#robots.txt
				Robots(); #for clean code
				
				my @findDirIndexing = ( # very common dirs to check for dir indexing
									'/images/',
									'/imgs/',
									'/img/',
									'/icons/',
									'/home/',
									'/pictures/',
									'/main/',
									'/css/',
									'/style/',
									'/styles/',
									'/docs/',
									'/doc/',
									'/pics/',
									'/pic/',
									'/thumbnails/',
									'/thumbs/',
									'/scripts/',
									'/script/',
									'/files/',
									'/js/',
									'/javascript/',
									'/javascripts/',
									'/site/',
									'/uploads/',
									'/downloads/',
									'/download/',
									'/ajax/',
									'/videos/',
									'/porn/',
									'/music/',
				);
				
				
				foreach my $IndexDir (@findDirIndexing) {
						$ua->agent( RandomUA() ) if defined $randUA;
						
						my $Getind = $ua->get("$URNtype://$Host" . $IndexDir);
						MatchDirIndex($Getind->decoded_content, $IndexDir);
				}
				
				$Getind = undef;
				undef(@findDirIndexing);
		
				
				# laguage checks
				
				foreach my $lineIDK ( split(/ /, $ua->get("$URNtype://$Host/")->decoded_content) ) {
						if($lineIDK =~ /lang=('|").*?('|")/i) {
								$lineIDK =~ s/(\t|\n)//g; $lineIDK =~ s/(<.*|>.*)//g; #make pretty
								
								print "[+] Page Laguage found: $lineIDK\n"; last; # somtimes pages have like 4 or 5 so just find one
						}
				}
				
				# Some servers just give you a 200 with every req. lets see
				my $ThereIsBadExt = 0; my @badexts;
				
				foreach my $Extention ('.php','.html','.htm','.aspx','.asp','.jsp','.cgi','.pl','.cfm','.txt','.larywall','.') {
						$ua->agent( RandomUA() ) if defined $randUA;
						my $check200 = $ua->get("$URNtype://$Host/$testErrorString" . \&genErrorString());
						
						unless($check200->code =~ m/(404|301|502)/) {
								push(@badexts, "\"$Extention\" ");
								$ThereIsBadExt = 1;
						}
				}
				if($ThereIsBadExt) { # if the page contains multi error just put em into the same string
						print "[-] INTENTIONALLY bad requests sent with the file Extention(s) @badexts responded with odd status codes. any results from this server with those files extention(s) may be void\n";
				}
				$check200 = undef;
				undef(@badexts);
				
				
				# mobile site test
				my @mobiTest;
				foreach ("Mozilla/5.0 (iPhone; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0" , "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.3) Gecko/20010801") {
						$ua->agent($_);
						push( @mobiTest, $ua->get("$URNtype://$Host/")->decoded_content );
				}
				$mobiTest[0] =~ s/<--.*-->//g; $mobiTest[1] =~ s/<--.*-->//g; # some servers have time stamps in comments
				
				unless($mobiTest[0] eq $mobiTest[1]) {
						print "[+] Index page reqested with an Iphone UserAgent is diferent then with a regular UserAgent. This Host may have a mobile site\n";
				}
				
				if(defined $UserA) { # sets back to defined useragent
						$ua->agent($UserA);
				}
				$mobilePage = undef; $regularPage = undef;
				
				# is ssl stuff
				$ua->ssl_opts(verify_hostname => 1);
				
				$ua->agent( RandomUA() ) if defined $randUA;
				my $sslreq = $ua->get("https://$Host/");
				if($sslreq->is_success) {
						print "[+] $Host is SSL capable\n";
						
						my @parseSSL = getHeaders($sslreq->as_string);
						foreach my $SSLheader (@parseSSL) {
								chomp($SSLheader);
								
								if($SSLheader =~ /client-ssl-cipher:/i) { $SSLheader =~ s/client-ssl-cipher://i; print "[+] SSL Cipher: $SSLheader\n"; }
								if($SSLheader =~ /client-ssl-cert-issuer:/i) { # extract
										$SSLheader =~ s/client-ssl-cert-issuer://i;
										$SSLheader =~ s/.*\/O=//i;
										$SSLheader =~ s/\/.*//;
										
										print "[+] SSL Certificate vendor: $SSLheader\n";
								}
						}
						
				}
				$sslreq = undef; undef(@parseSSL);


				
				#Apache account name
				my @apcheUserNames = (
									'web',
									'user',
									'guest',
									'root',
									'admin',
									'apache',
									'adminstrator',
									'netadmin',
									'sysadmin',
									'webadmin',
									'manager',
									'system',
									'test',
									'twighlighsparkle',
									);
				
				foreach my $usrnm (@apcheUserNames) {
						$ua->agent( RandomUA() ) if defined $randUA;
						my $ApcheUseNmTest = $ua->get("$URNtype://$Host/~" . $usrnm);
						
						if($ApcheUseNmTest->code == 403) {
								print  "[+] This server has Apache user accounts enabled. Found User: ~$usrnm\n";
								analyzeResponse($ApcheUseNmTest->as_string() ,"/~$usrnm") unless(defined $noRespAnal);
						}
				}
				$ApcheUseNmTest = undef; undef(@apcheUserNames);
				
				
				# thumbs.db test
				my @imageDirs = (
								'/images/',
								'/img/',
								'/imgs/',
								'/pics/',
								'/pictures/',
								'/icons/',
								'/thumbs/',
								'/thumbnails/',
								'/wallpapers/',
								'/iconset/',
								'/',
				);
				
				foreach my $imageDir (@imageDirs) {
						foreach my $CapTumbs("thumbs.db","Thumbs.db") {
								$ua->agent( RandomUA() ) if defined $randUA;
								my $getThumbs = $ua->get("$URNtype://$Host".$imageDir.$CapTumbs);
						
								if($getThumbs->is_success) {
										print "[+] $CapTumbs found. This suggests the host is running Windows\n";
										analyzeResponse($getThumbs->as_string() ,$CapTumbs) unless(defined $noRespAnal);
										goto doneThumbs;
								}
						}
				}
				doneThumbs:
				undef($getThumbs); undef(@imageDirs);
				
				#Apache content negotiation
				foreach my $negoTest ("robots", "index", "favicon", "_ndex") {
						$ua->agent( RandomUA() ) if defined $randUA;
						
						@NegoHeaders = getHeaders($ua->get("$URNtype://$Host/$negoTest")->as_string);
						foreach (@NegoHeaders) {
								if($_ =~ /vary:( |)negotiate/i) {
										print "[+] $Host allows Apache content negotiation\n";
										goto lastNego;
								}
						}
				}
				lastNego:
				undef(@NegoHeaders);
				
				# common sensitive shtuff
				open(FilesAndDirsDBFileS, "<", "DB/small-tests.db");
				
				while(<FilesAndDirsDBFileS>) {
						dataBaseScan($_,'',"",'Synt') unless $_ =~ /^#/;
				}
				
				close(FilesAndDirsDBFileS);
				

				# portscan.... kinda
				my @httpPorts =(
								66,
								81,
								631,
								445,
								457,
								1080,
								1100,
								1241,
								1352,
								1433,
								1434,
								1521,
								1944,
								2301,
								3128,
								4000,
								4001,
								4002,
								4100,
								5000,
								5432,
								5800,
								5801,
								5802,
								6346,
								6347,
								7001,
								7002,
								8080,
								8180,
								8888,
								30821,
				);
				
				foreach (@httpPorts){
					my $portGet = $ua->get("$URNtype://$Host:$_/");
					if($portGet->code == 200 or $portGet->code == 401 or $portGet->code == 403){
						print "[+] OPEN HTTP server on port: $_\n";
					}
				}
}




sub defaultFiles{ #thanks to FuzzDB for most of the DB's
		my @Platfroms;
		
		push(@Platfroms, 'DB/Apache.db')                if($Df =~ m/apache/i);
		push(@Platfroms, 'DB/Frontpage.fuzz.txt')       if($Df =~ m/Frontpage/i);
		push(@Platfroms, 'DB/IIS.fuzz.txt')             if($Df =~ m/IIS/i);
		push(@Platfroms, 'DB/Oracle9i.fuzz.txt')        if($Df =~ m/Oracle9i/i);
		push(@Platfroms, 'DB/Weblogic.fuzz.txt')        if($Df =~ m/Weblogic/i);
		push(@Platfroms, 'DB/Websphere.fuzz.txt')       if($Df =~ m/Websphere/i);
		push(@Platfroms, 'DB/CGI_Microsoft.fuzz.txt')   if($Df =~ m/MicrosoftCGI/i);
		
		
		if($Df =~ m/all/i or defined $e or defined $intenseScan) {
				@Platfroms = (
								'DB/Apache.db',
								'DB/Frontpage.fuzz.txt',
								'DB/IIS.fuzz.txt',
								'DB/Oracle9i.fuzz.txt',
								'DB/Weblogic.fuzz.txt',
								'DB/Websphere.fuzz.txt',
								'DB/CGI_Microsoft.fuzz.txt',
				);
		}
		
		print "\n[*] _______DEFAULT FILES_______ [*]\n";
		
		foreach my $Platform (@Platfroms) {
				open(defaultFilesDB, "<", "$Platform");
				
				# make for pretty output per platform
				my $PlatformOutput = $Platform;
				$PlatformOutput =~ s/(\..*\..*|\..*)$//;
				$PlatformOutput =~ s/DB\///;
				
				while(<defaultFilesDB>) {
						dataBaseScan($_,'',"$PlatformOutput Default File Found:",'nonSynt') unless $_ =~ m/^#/;
				}

				close(defaultFilesDB);
		}
}




sub auth{ # pazzaz acquired
		open(authDB, "<", "DB/login.db");
		print "\n[*] _______ATHENTICATION AREAS_______ [*]\n";
		
		while(<authDB>) {
				dataBaseScan($_,'','','Synt') unless $_ =~ /^#/;
		}

		close(authDB);
}




sub cmsPlugins{ # parts of Plugin databases provided by: Chris Sullo from cirt.net
		print "[-] -Cp takes awhile....\n";
		print "\n[*] _______CMS PLUGINS_______ [*]\n";
		
		my @cmsPluginDBlist;
		
		push(@cmsPluginDBlist, 'DB/drupal_plugins.db')  if($cmsPlugins =~ m/dp/i);
		push(@cmsPluginDBlist, 'DB/joomla_plugins.db')  if($cmsPlugins =~ m/jm/i);
		push(@cmsPluginDBlist, 'DB/wp_plugins.db')      if($cmsPlugins =~ m/wp/i);
		
		
		if($cmsPlugins =~ m/all/i or defined $e) {
				@cmsPluginDBlist = ('DB/drupal_plugins.db', 'DB/joomla_plugins.db', 'DB/wp_plugins.db');
		}
		
		foreach my $cmsPluginDB (@cmsPluginDBlist) {
				print "[+] Testing Plugins with Database: $cmsPluginDB\n";
						
				open(cmsPluginDBFile, "<", "$cmsPluginDB");
				
				while(<cmsPluginDBFile>) {
						dataBaseScan($_,'','CMS Plugin Found:','nonSynt') unless $_ =~ /^#/;
				}

				close(cmsPluginDBFile);

		}


}




sub FilesAndDirsGoodies{ # databases provided by: raft team

		print "\n[-] -Fd takes awhile....\n";
		my @FilesAndDirsDBlist = ('DB/raft-medium-files.db','DB/raft-medium-directories.db',);
		
		print "\n[*] _______INTERESTING FILES AND DIRS BRUTEFORCE_______ [*]\n";
		foreach my $FilesAndDirsDB (@FilesAndDirsDBlist) {
				
				open(FilesAndDirsDBFile, "<", "$FilesAndDirsDB");
				
				while(<FilesAndDirsDBFile>) {
						dataBaseScan($_,'','','nonSynt') unless $_ =~ /^#/;
				}

				close(FilesAndDirsDBFile);

		}

}




sub webServices{
		# match page content with known services related
		print "\n[*] _______WEB SERVICES_______ [*]\n";
		
		sub WScontent{
				my $webServicesTestPage = shift;
						
				open(webServicesDB, "<", "DB/web-services.db");
				
				
				while(<webServicesDB>) {
						dataBaseScan($_,"$webServicesTestPage",'Found service or widget:','match') unless $_ =~ /^#/;
				}

				close(webServicesDB);
				
				undef($webServicesTestPage);
		}
		
		WScontent($ua->get("$URNtype://$Host")->decoded_content);
		faviconMD5();
		
		
		sub faviconMD5{
				require Digest::MD5;
				my $smartFav = 0;
				
				my @favArry = (
								'favicon.ico',
								'Favicon.ico',
								'images/favicon.ico',
								'images/Favicon.ico',
				);
				
				open(faviconMD5DB, "<", "DB/favicon.db");
				my @faviconMD5db = <faviconMD5DB>;
				
				@favHeadTest = getHeaders( $ua->get("$URNtype://$Host/")->as_string );
				foreach (@favHeadTest){ # here we try to smatly get the favicon
						if( $_ =~ m/Link/i and $_ =~ m/\.ico/i ){
								$_ =~ s/link:.*<//i;
								$_ =~ s/>.*//i;
								
								favHash( $ua->get("$URNtype://$Host/$_")->content );
						}
				}
				
				# find favicon location in the headers
				foreach my $favLocation (@favArry) {
						my $favicon = $ua->get("$URNtype://$Host/$favLocation");
						
						if($favicon->is_success) {
								favHash( $favicon->content );
						}
						
				}
				
				
				sub favHash{
						my $faviconCont = shift;
						
						my $MD5 = Digest::MD5->new;
						my $checksum = $MD5->add($faviconCont)->hexdigest; # make checksum
						
						foreach my $faviconMD5String (@faviconMD5db) {
								dataBaseScan($faviconMD5String, $checksum, 'Server information found via favicon fingerprint:', 'match');
						}
				}
				close(faviconMD5DB);
				undef(@faviconMD5db);
				no Digest::MD5; # unload this module
		}
		
		
		open(cmsDB, "<", "DB/CMS.db");
		
		while(<cmsDB>) {
				dataBaseScan($_,'','','Synt') unless $_ =~ /^#/; #this func can only be called when the DB uses the /dir;msg format
		}
		
		close(cmsDB);
}




sub interesting{ # emails, plugins and such
		my $mineShaft = shift;
		my $mineUrl = shift;
		my $FoundInter = 0;
		my $FoundBefor = 0;
				
				my @InterestingStringsFound;
				my @IndexData;

				my @interestingStings = (
										'\/cgi-bin;CGI Dir',
										'\/wp-content\/plugins\/;WordPress Plugin',
										'\/wp-includes\/;Wordpress include',
										'\/wp-content\/themes\/;Wordpress theme',
										'\/components\/;Possible Drupal Plugin',
										'\/modules\/;Drupal Plugin',
										'\/templates\/;template',
										'\/_vti_;IIS Default Dir/File',
										'$Host\/~;Apache User Dir', # Apache Account
										'\@.*?\.(com|org|net|tv|uk|au|ro|ca|xxx|edu|mil|gov|biz|info|int|tel|jobs|co|pro);Email', #emails
										'(\t| )@.*?\.(com|uk|au);maybe Twitter Account',
										'<!--#;Server Side Include', #SSI
										'fb:admins;Facebook fbids',
										'\/.\/cpanel\/.*?\/images\/logo.gif\?service=mail;google mail',
										'\/_layouts;Sharepoint',
										'It works!;maybe default apache splash screen',
										'var\/www;linux web dir',
										);

				foreach my $checkInterestingSting (@interestingStings) {
						my ($checkInterestingSting, $InMSG) = split(/;/, $checkInterestingSting);
						

						foreach my $splitIndex ( split(">", $mineShaft) ) {
						
								if($splitIndex =~ m/$checkInterestingSting/i) {
								
										while($splitIndex =~ /(\n|\t|  )/) { $splitIndex =~ s/(\n|\t|  )/ /g; }
										
										foreach my $MatchItemFound (@FoundMatchItems) {
												if($MatchItemFound eq $splitIndex) {
													$FoundBefor = 1; # set true
											}
										}
										push(@FoundMatchItems, $splitIndex);
										
										unless($FoundBefor) { #prevents double output
													
											if(length($splitIndex) > 200) { # too big for output
													print "[+] Interesting text ($InMSG) found in \"$mineUrl\" You should manualy review it\n";
													last;
											} else {
													push(@InterestingStringsFound, " \n\n  ($InMSG) \"$splitIndex\"");
													$FoundInter = 1;
											}
										}
										
								}
						
						}


						
						if($FoundInter) { # if the page contains multi error just put em into the same string
								print "[+] Interesting text found in \"$mineUrl\": @InterestingStringsFound\n";
								last;
						}
						
						undef(@InterestingStringsFound); # saves the above if for the next go around
				
				}
				
				undef $mineShaft;
}




sub ErrorStrings{ #failing is the key here
		my $CheckCont = shift;
		my $ErrorURI = shift;
		my $FoundBefor = 0;

				my @oddErrStrs = (
									'mysql_error \(( |).*?( |)\);contains a mySQL error',
									'The requested URL \/.* was not found on this server;contains requested URI (possibly vunerable to XSS)',
									'<span><H1>Server Error in .* Application<.*><\/H1>;contains .NET Framework or ASP.NET version info',
									'<hr>.*Apache\/;contains Apache version info NOTE: probably all 404 pages from this server contain this',
									'<hr>.*nginx\/;contains nginx version info NOTE: probably all 404 pages from this server contain this',
									);
				
				foreach my $errorstringMsgandMatch (@oddErrStrs) {
						my ($matchErrorSTR, $reportMessage) = split(/;/, $errorstringMsgandMatch);
						
						if($CheckCont =~ m/$matchErrorSTR/i) {
								
								foreach my $MatchItemFound (@FoundMatchItems) {
										if($MatchItemFound eq $reportMessage) {
												$FoundBefor = 1; # set true
										}
								}
								push(@FoundMatchItems, $reportMessage);
						
								unless($FoundBefor) {
										print "[+] Error page: \"$ErrorURI\" $reportMessage\n";
								}
						}
				}
				
		undef($CheckCont);
}
 



sub Ninja{ # total number of reqs sent: 6
		my $ninjaTestPagee = $ua->get("$URNtype://$Host/");
		bannerGrab($ninjaTestPagee->as_string);
		sleep(int((rand(3)+2))); # pause for a random amount of time
		
		my @tit = getHeaders($ninjaTestPagee->as_string);
		foreach my $getTitle(@tit) {
				if($getTitle =~ m/Title:/i) {
						$getTitle =~ s/Title://i;
						print "[+] HTTP Title: $getTitle\n";
				}
				if($getTitle =~ m/^Date:/i) {
						$getTitle =~ s/Date://i;
						print "[+] HTTP Date: $getTitle\n";
				}
		}
		
		faviconMD5();
		sleep(int((rand(3)+2)));
		Robots();
		sleep(int((rand(3)+2)));
		WScontent($ninjaTestPagee->decoded_content);
}




# directory-list-2.3-big.db is under Copyright 2007 James Fisher
# see Original file in Dirbuster for link to licence
# I did not aid or assist in the creation or production of directory-list-2.3-big.db
sub Dirbuster{

		print "\n[-] -Db takes awhile.... No joke. Go to the movies or something\n";

		open(DirbustDBFile, "<", "DB/directory-list-2.3-big.db");
		print "\n[*]  _______DIRBUSTER DIRECTORY BRUTEFORCE_______  [*]\n";
		
		while(<DirbustDBFile>) {
				dataBaseScan($_,'','',"nonSynt") unless $_ =~ /^#/;
		}
		
		close(DirbustDBFile);
}




sub SubDomainBF{ #thanks to deepmagic.com [mubix] and Knock for a lot of the DB/SubDomain.db
		print "[-] -Sd takes awhile...\n";
		
		my $DomainOnly = $Host;
		my $FindCount = 0;
		
		if($Host =~ /^(\d\d\d|\d\d|\d)\.(\d\d\d|\d\d|\d)\.(\d\d\d|\d\d|\d)\.(\d\d\d|\d\d|\d)$/) {
				my $Opt = PromtUser("[-] Host appears to be an IP Address\n[?] would you like me to Cancel subdomain scaning (y/n) ? ");

				if($Opt =~ /y/i) {
						goto cancelSD;
				}
		}
		
		if($DomainOnly =~ m/.*?\..*?\./i) { # if subdomain
				my $Opt = PromtUser("[?] It looks like the host you supplied allready has a subdomain. would you like me to srip it (y/n) ? ");
				
				if($Opt =~ m/y/i) {
						$DomainOnly =~ s/.*?\.//; #remove subdomain: blah.ws.com -> ws.com
				}
		}
		
		open(SubDomainDB, "<", "DB/SubDomain.db");
		print "\n[*] _______SUBDOMAIN BRUTEFORCE_______ [*]\n";
		
		while(<SubDomainDB>) {
				chomp $_;
				my $SubDomainToRequest = $_.'.'.$DomainOnly;
				my $TestSubDomain = inet_aton($SubDomainToRequest); # much more relieable then http requests for example smtp.blah.com will not respond with http 
				
				unless($TestSubDomain eq "") {
						print "[+] $SubDomainToRequest\n";
						$FindCount++;
				}
				
		}

		close(SubDomainDB);
		
		if($FindCount > 1000) {
				print "[-] The host may have the DNS wildcard configuration which would render those results null and void.\n";
		}
		if($FindCount == 0) {
				print "[-] Could not find any SubDomains on this host\n";
		} else {
				print "[*] $FindCount SubDomains Found\n";
		}
		
		cancelSD:
}




sub ShadowScan{
		my $HostMutate = "webcache.googleusercontent.com/search?q=cache:" . "$Host";
		return($HostMutate);
}




sub SmallFdEnum{
		open(SmallFDEnum, "<", "DB/small-files-dirs-enum.db");
		print "\n[*]  _______QUICK FILES AND DIRS ENUM_______  [*]\n";
		
		while(<SmallFDEnum>) {
				dataBaseScan($_,'',"","nonSynt") unless $_ =~ /^#/;
		}
		
		close(SmallFDEnum);
}