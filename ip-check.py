#!/usr/bin/python3
if 64 - 64: i11iIiiIii
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
if 73 - 73: II111iiii
if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
if 48 - 48: oO0o / OOooOOo / I11i / Ii1I
if 48 - 48: iII111i % IiII + I1Ii111 / ooOoO0o * Ii1I
if 46 - 46: ooOoO0o * I11i - OoooooooOO
if 30 - 30: o0oOOo0O0Ooo - O0 % o0oOOo0O0Ooo - OoooooooOO * O0 * OoooooooOO
import os , sys , re , requests , time
from multiprocessing import Pool
if 60 - 60: iIii1I11I1II1 / i1IIi * oO0o - I1ii11iIi11i + o0oOOo0O0Ooo
ooO0oo0oO0 = """\033[37;1m
\033[37;1m██\033[31;1m╗\033[37;1m██████\033[31;1m╗      \033[37;1m██████\033[31;1m╗\033[37;1m██\033[31;1m╗  \033[37;1m██\033[31;1m╗\033[37;1m███████\033[31;1m╗ \033[37;1m██████\033[31;1m╗\033[37;1m██\033[31;1m╗  \033[37;1m██\033[31;1m╗\033[37;1m███████\033[31;1m╗\033[37;1m██████\033[31;1m╗ 
\033[37;1m██\033[31;1m║\033[37;1m██\033[31;1m╔══\033[37;1m██\033[31;1m╗    \033[37;1m██\033[31;1m╔════╝\033[37;1m██\033[31;1m║  \033[37;1m██\033[31;1m║\033[37;1m██\033[31;1m╔════╝\033[37;1m██\033[31;1m╔════╝\033[37;1m██\033[31;1m║ \033[37;1m██\033[31;1m╔╝\033[37;1m██\033[31;1m╔════╝\033[37;1m██\033[31;1m╔══\033[37;1m██\033[31;1m╗
\033[37;1m██\033[31;1m║\033[37;1m██████\033[31;1m╔╝    \033[37;1m██\033[31;1m║     \033[37;1m███████\033[31;1m║\033[37;1m█████\033[31;1m╗  \033[37;1m██\033[31;1m║     \033[37;1m█████\033[31;1m╔╝ \033[37;1m█████\033[31;1m╗  \033[37;1m██████\033[31;1m╔╝
\033[37;1m██\033[31;1m║\033[37;1m██\033[31;1m╔═══╝     \033[37;1m██\033[31;1m║     \033[37;1m██\033[31;1m╔══\033[37;1m██\033[31;1m║\033[37;1m██\033[31;1m╔══╝  \033[37;1m██\033[31;1m║     \033[37;1m██\033[31;1m╔═\033[37;1m██\033[31;1m╗ \033[37;1m██\033[31;1m╔══╝  \033[37;1m██\033[31;1m╔══\033[37;1m██\033[31;1m╗
\033[37;1m██\033[31;1m║\033[37;1m██\033[31;1m║         \033[31;1m╚\033[37;1m██████\033[31;1m╗\033[37;1m██\033[31;1m║  \033[37;1m██\033[31;1m║\033[37;1m███████\033[31;1m╗╚\033[37;1m██████\033[31;1m╗\033[37;1m██\033[31;1m║  \033[37;1m██\033[31;1m╗\033[37;1m███████\033[31;1m╗\033[37;1m██\033[31;1m║  \033[37;1m██\033[31;1m║
\033[31;1m╚═╝╚═╝          ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

\t\t\033[34;1m C O D E D - B Y - \033[32;1m@ M R B L A C K X
\t\t\033[34;1m V E R S I O N - V1 - \033[32;1m[ B E T A ]

"""
if 100 - 100: i1IIi
I1Ii11I1Ii1i = "live-ips.txt"
Ooo = "valid_ips.txt"
if 56 - 56: I11i - i1IIi
if os . path . isfile ( I1Ii11I1Ii1i ) :
 os . remove ( I1Ii11I1Ii1i )
if os . path . isfile ( Ooo ) :
 os . remove ( Ooo )
 if 64 - 64: I1Ii111 + iII111i
 if 10 - 10: i11iIiiIii / oO0o % II111iiii
def Ooo00O0 ( ip ) :
 ip = ip . replace ( "\n" , "" )
 try :
  oo0 = requests . get ( "http://" + ip , timeout = 3 )
  if oo0 . status_code == 200 :
   print ( "\033[34;1m[\033[32;1m*\033[34;1m] \033[32;1m" + ip + " \033[34;1m| \033[37;1mURL \033[34;1m| \033[32;1m" + oo0 . url + " \033[34;1m| \033[37;1m[\033[33;1m(\033[32;1mLIVE\033[33;1m)\033[37;1m]" )
   open ( "live-ips.txt" , "a+" ) . write ( ip + " " + oo0 . url + "\n" )
  if oo0 . status_code == 503 :
   print ( "\033[34;1m[\033[31;1m!\033[34;1m] \033[31;1m" + ip + " \033[34;1m| \033[37;1m[\033[33;1m(\033[31;1mDEAD\033[33;1m)\033[37;1m]" )
 except Exception as Oooo00OOo000 :
  print ( "\033[34;1m[\033[31;1m!\033[34;1m] \033[31;1m" + ip + " \033[34;1m| \033[37;1m[\033[33;1m(\033[31;1mDEAD\033[33;1m)\033[37;1m]" )
 O0I11i1i11i1I . pop ( 0 )
def Iiii ( ip ) :
 OOO0O = open ( "valid_ips.txt" , "r" )
 O0I11i1i11i1I = OOO0O . readlines ( )
 oo0ooO0oOOOOo = Pool ( 50 )
 oO000OoOoo00o = oo0ooO0oOOOOo . map ( Ooo00O0 , O0I11i1i11i1I )
 if 31 - 31: II111iiii + OoO0O00 . I1Ii111
 if 68 - 68: I1IiiI - i11iIiiIii - OoO0O00 / OOooOOo - OoO0O00 + i1IIi
 if 48 - 48: OoooooooOO % o0oOOo0O0Ooo . I1IiiI - Ii1I % i1IIi % OoooooooOO
if __name__ == '__main__' :
 os . system ( 'clear' )
 print ( ooO0oo0oO0 )
 i1iIIi1 = input ( "Give IP List :\033[35;1m " )
 ii11iIi1I = open ( i1iIIi1 , "r" )
 O0I11i1i11i1I = ii11iIi1I . readlines ( )
 iI111I11I1I1 = "^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$"
 print ( "\033[34;1m[\033[33;1m*\033[34;1m] \033[37;1mChecking Validation...\n\n" )
 for OOooO0OOoo in O0I11i1i11i1I :
  if re . search ( iI111I11I1I1 , OOooO0OOoo ) :
   open ( "valid_ips.txt" , "a+" ) . write ( OOooO0OOoo )
 Iiii ( O0I11i1i11i1I )
 if 29 - 29: o0oOOo0O0Ooo / iIii1I11I1II1
 if 24 - 24: O0 % o0oOOo0O0Ooo + i1IIi + I1Ii111 + I1ii11iIi11i
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
