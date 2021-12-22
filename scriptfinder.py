#!/usr/bin/python
#Usage : python sf-1.1.py /path/to/dir
""" ScriptFinder 1.1 < ditatompel [at] gmail [dot] com >
Searches for file contains dangerous command

Inspired from tools created by d3hydr8[at]gmail[dot]com
greetz to d3hydr8, 5ynL0rd all members of devilzc0de.org,
ex darkc0de.com, all Indonesian c0ders, and all GNU Generation ;-)

PS : Happy Birthday k*t*k, Revres Tanur or whatever nickname gonna be :p
PF : ?? Oct ???? - ?? Oct 2011 """


import sys, re

def halo():
    print "\n" + "-+-"*30 + "\n\tScriptFinder 1.1 < ditatompel [at] gmail [dot] com >"
    print "\tSearches for file contains dangerous command"
    print "\tGreetz to all members of devilzc0de.org, ex darkc0de.com, all Indonesian c0ders,"
    print "\tand all GNU Generation ;-)\n" + "-+-"*30+"\n"

def usage():
    print "\tUsage: python " + sys.argv[0] + " <dir>"
    print "\tExample: python " + sys.argv[0] + " /home/ditatompel/public_html\n"
    sys.exit(1)

#Original from d3hydr8[at]gmail[dot]com
def Walk( root, recurse=0, pattern='*', return_folders=0 ):
    import fnmatch, os, string

    result = []

    try:
        names = os.listdir(root)
    except os.error:
        return result

    pattern = pattern or '*'
    pat_list = string.splitfields( pattern , ';' )

    for name in names:
        fullname = os.path.normpath(os.path.join(root, name))

        for pat in pat_list:
            if fnmatch.fnmatch(name, pat):
                if os.path.isfile(fullname) or (return_folders and os.path.isdir(fullname)):
                    result.append(fullname)
                continue
        if recurse:
            if os.path.isdir(fullname) and not os.path.islink(fullname):
                result = result + Walk( fullname, recurse, pattern, return_folders )
        
    return result

def search(files, auto=0):
    
    if auto:
        searchstring = danger
    else:
        searchstring = specificstring
    
    print "\n[+] Searching:", len(files), "files"
    print "\n" + "-+-"*20 + "\n[+] files containing '" + searchstring + "' under " + sys.argv[1] + "\n"+"-+-"*20+"\n"
    love.write("\n"+"-+-"*20)
    love.write("\n[+] files containing '%s' under '%s' \n" % (searchstring, sys.argv[1]) )
    love.write("-+-"*20+"\n")
    
    for file in files:
        num = 0
        
        try:
            text = open(file, "r").readlines()
            
            for line in text:
                num +=1
                if re.search(searchstring.lower(), line.lower()):
                    print "[!] File:",file,"on Line:",num,"\n[!] Code:",line
                    love.write("""[!] File: %s on Line %s \n[!] Code: %s \n""" % (file, num, line.replace("\t","")) )
        
        except(IOError):
            pass
    
    print "[+] Done\n"

halo()

actions = [
    "base64_decode", # many php shell use this but may generate false positive result, remove this if necessary. Especially when using recursive scan.
    "exec",
    "eval", # may generate false positive result, remove this if necessary. Especially when using recursive scan.
    "escapeshellarg",
    "escapeshellcmd",
    "fpaththru",
    "getmy", # getmypid, getmygid, getmyuid, etc
    "gzinflate",
    "gzuncompress",
    "ini_alter",
    "leak",
    "mDbl8VndvJj2", # encoded devshell.asp
    "php_uname",
    "posix_", # any posix_* function
    "proc_", # any proc_* function
    "popen",
    "passthru",
    "pcntl_exec",
    "socket_accept",
    "socket_bind",
    "socket_clear_error",
    "socket_close",
    "socket_connect",
    "set_time_limit",
    "shell_exec",
    "system", # may generate false positive result, remove this if necessary. Especially when using recursive scan.
    "show_source",
    "xrunexploit" # source function on devshell.*
    ]

minus_r = 1

if len(sys.argv) < 2:
    usage()

recdir = raw_input("Recursive ? ( Y/n ): ")
mode = raw_input("Full scan Mode (Y/n): ")

if mode.lower() != "y":
    specificstring = raw_input("String to search: ")

ext = raw_input("Specific File extension to scan ( <return> to scan all extension ) : ")
filelog = raw_input("logfile ( default sf.log ): ")

if filelog == "":
    filelog = "sf.log"

if recdir.lower() != "y":
    minus_r = 0

love = open(filelog, "w")
love.write("-+-"*30 + "\n\tScriptFinder 1.1 < ditatompel [at] gmail [dot] com >\n")
love.write("\tGreetz for all members of devilzc0de.org, ex darkc0de.com, all Indonesian c0ders,\n\tand all GNU Generation ;-)\n"+"-+-"*30+"\n")

if mode.lower() == "y":
    print "\n[+] FULL SCAN MODE ENABLED...\n[+]", len(actions),"dangerous commands loaded\n[+] Target Dir:",sys.argv[1]
    print "[+] Logfile will be saved to: " + filelog
    love.write("""
    [+] FULL SCAN MODE ENABLED...
    [+] %s danger commands loaded
    [+] Target Dir: %s\n""" % (len(actions), sys.argv[1]) )
    for danger in actions :
        if ext == "":
            files = Walk(sys.argv[1], minus_r, '*', 1)
        else:
            files = Walk(sys.argv[1], minus_r, '*.'+ext+';')
        search(files, 1)
    print "[+] Logfile saved to " + filelog

else:
    print "\n[+] Target Dir: " + sys.argv[1] + "\n[+] String to search: " + specificstring
    print "[+] Logfile will be saved to: " + filelog
    love.write("""
    [+] Target Dir: %s
    [+] String to search %s\n""" % (sys.argv[1], specificstring ) )
    if ext == "":
        files = Walk(sys.argv[1], minus_r, '*', 1)
    else:
        files = Walk(sys.argv[1], minus_r, '*.'+ext+';')
    search(files)
    print "[+] Logfile saved to " + filelog