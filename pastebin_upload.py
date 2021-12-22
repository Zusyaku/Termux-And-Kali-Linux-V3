#!/usr/bin/python
# passtobin.py v 0.1
# Uploads source file to pastebin.com using pastebin API.
# You may use custom filename, post as guest / user
# with private / public paste option and auto syntax
# highlight for several filetypes, etc.
#
# coded by: ditatompel <ditatompel@gmail.com>
# Thanks to : 5ynL0rd who always inspire me.
# Greetings for all members of devilzc0de.org, all Indonesian c0ders,
# and all GNU Generation ;-)
# I glue you all my regards.

from optparse import OptionParser
import sys, getpass, urllib, string, os.path

# Login as user and get your API http://pastebin.com/api
# But it's ok you use API key below. ;)
APIKEY = "81a5d31a05abe09be32cb6832f6904b9"
URL = "http://pastebin.com"

menu = OptionParser()
menu.add_option("-f", dest="file", help="file you want to upload (Required!) ")
menu.add_option("-u", "--user", dest="user", help="your pastebin username, will be submit as guest if not specified", type="string")
menu.add_option("-n", "--name", dest="name", default='untitled', help="your pastebin file title (optional)")
menu.add_option("-p", "--private", action="store_false", default="0", help="set this param for private paste")
menu.add_option("-t", "--type", dest="type", default='text', help="force format syntax highlight (Default: text)")
menu.add_option("-e", dest="expire_date", default='N', help="Paste expires. Default: Never", metavar="<N|10M|1H|1D|1M>")

ExpOpt = { "N": "never", "10M": "10 minutes", "1H": "1 hour", "1D": "1 day", "1M": "1 month" }

FileType = {
    "4cs": "4CS", "6502acme": "6502 ACME Cross Assembler", "6502kickass": "6502 Kick Assembler",
    "6502tasm": "6502 TASM/64TASS", "abap": "ABAP", "actionscript": "ActionScript",
    "actionscript3": "ActionScript 3", "ada": "Ada", "algol68": "ALGOL 68", "apache": "Apache Log",
    "applescript": "AppleScript", "apt_sources": "APT Sources", "asm": "ASM (NASM)", "asp" : "ASP",
    "autoconf": "autoconf", "autohotkey": "Autohotkey", "autoit": "AutoIt", "avisynth": "Avisynth",
    "awk": "Awk", "bascomavr": "BASCOM AVR", "bash": "Bash", "basic4gl": "Basic4GL",
    "bibtex": "BibTeX", "blitzbasic": "Blitz Basic", "bnf": "BNF", "boo": "BOO", "bf": "BrainFuck",
    "c": "C", "c_mac": "C for Macs", "cil": "C Intermediate Language", "csharp": "C#",
    "cpp": "C++", "cpp-qt": "C++ (with QT extensions)", "c_loadrunner": "C: Loadrunner",
    "caddcl": "CAD DCL", "cadlisp": "CAD Lisp", "cfdg": "CFDG", "chaiscrip": "ChaiScript",
    "clojure": "Clojure", "klonec": "Clone C", "klonecpp": "Clone C++", "cmake": "CMake",
    "cobol": "COBOL", "coffeescript": "CoffeeScript", "cfm": "ColdFusion", "css": "CSS",
    "cuesheet": "Cuesheet", "d": "D", "dcs": "DCS", "delphi": "Delphi",
    "oxygene": "Delphi Prism (Oxygene)", "diff": "Diff", "div": "DIV", "dos": "DOS",
    "dot": "DOT", "e": "E", "ecmascript": "ECMAScript", "eiffel": "Eiffel", "email": "Email",
    "epc": "EPC", "erlang": "Erlang", "fsharp": "F#", "falcon": "Falcon", "fo": "FO Language",
    "f1": "Formula One", "fortran": "Fortran", "freebasic": "FreeBasic", "freeswitch": "FreeSWITCH",
    "gambas": "GAMBAS", "gml": "Game Maker", "gdb": "GDB", "genero": "Genero", "genie": "Genie",
    "gettext": "GetText", "go": "Go", "groovy": "Groovy", "gwbasic": "GwBasic", "haskell": "Haskell",
    "hicest": "HicEst", "hq9plus": "HQ9 Plus", "html4strict": "HTML", "html5": "HTML 5", "icon": "Icon",
    "idl": "IDL", "ini": "INI file", "inno": "Inno Script", "intercal": "INTERCAL", "io": "IO", "j": "J",
    "java": "Java", "java5": "Java 5", "javascript": "JavaScript", "jquery": "jQuery",
    "kixtart": "KiXtart", "latex": "Latex", "lb": "Liberty BASIC", "lsl2": "Linden Scripting",
    "lisp": "Lisp", "llvm": "LLVM", "locobasic": "Loco Basic", "logtalk": "Logtalk",
    "lolcode": "LOL Code", "lotusformulas": "Lotus Formulas", "lotusscript": "Lotus Script",
    "lscript": "LScript", "lua": "Lua", "m68k": "M68000 Assembler", "magiksf": "MagikSF", "make": "Make",
    "mapbasic": "MapBasic", "matlab": "MatLab", "mirc": "mIRC", "mmix": "MIX Assembler",
    "modula2": "Modula 2", "modula3": "Modula 3", "68000devpac": "Motorola 68000 HiSoft Dev",
    "mpasm": "MPASM", "mxml": "MXML", "mysql": "MySQL", "newlisp": "newLISP", "text": "None",
    "nsis": "NullSoft Installer", "oberon2": "Oberon 2", "objeck": "Objeck Programming Langua",
    "objc": "Objective C", "ocaml-brief": "OCalm Brief", "ocaml": "OCaml", "pf": "OpenBSD PACKET FILTER",
    "glsl": "OpenGL Shading", "oobas": "Openoffice BASIC", "oracle11": "Oracle 11", "oracle8": "Oracle 8",
    "oz": "Oz", "pascal": "Pascal", "pawn": "PAWN", "pcre": "PCRE", "per": "Per", "perl": "Perl",
    "perl6": "Perl 6", "php": "PHP", "php-brief": "PHP Brief", "pic16": "Pic 16", "pike": "Pike",
    "pixelbender": "Pixel Bender", "plsql": "PL/SQL", "postgresql": "PostgreSQL", "povray": "POV-Ray",
    "powershell": "Power Shell", "powerbuilder": "PowerBuilder", "proftpd": "ProFTPd",
    "progress": "Progress", "prolog": "Prolog", "properties": "Properties", "providex": "ProvideX",
    "purebasic": "PureBasic", "pycon": "PyCon", "python": "Python", "q": "q/kdb+", "qbasic": "QBasic",
    "rsplus": "R", "rails": "Rails", "rebol": "REBOL", "reg": "REG", "robots": "Robots",
    "rpmspec": "RPM Spec", "ruby": "Ruby", "gnuplot": "Ruby Gnuplot", "sas": "SAS", "scala": "Scala",
    "scheme": "Scheme", "scilab": "Scilab", "sdlbasic": "SdlBasic", "smalltalk": "Smalltalk",
    "smarty": "Smarty", "sql": "SQL", "systemverilog": "SystemVerilog", "tsql": "T-SQL", "tcl": "TCL",
    "teraterm": "Tera Term", "thinbasic": "thinBasic", "typoscript": "TypoScript", "unicon": "Unicon",
    "uscript": "UnrealScript", "vala": "Vala", "vbnet": "VB.NET", "verilog": "VeriLog", "vhdl": "VHDL",
    "vim": "VIM", "visualprolog": "Visual Pro Log", "vb": "VisualBasic", "visualfoxpro": "VisualFoxPro",
    "whitespace": "WhiteSpace", "whois": "WHOIS", "winbatch": "Winbatch", "xbasic": "XBasic", "xml": "XML",
    "xorg_conf": "Xorg Config", "xpp": "XPP", "yaml": "YAML", "z80": "Z80 Assembler", "zxbasic": "ZXBasic"
}

try:
    (options, args) = menu.parse_args()
    
    if options.file:
        f = open(options.file, 'r')
        fileU = f.read()
    else:
        menu.print_help()
        sys.exit(1)
    
    if options.user:
        password = getpass.getpass("pastebin Password:")
        user = options.user
    else:
        user = "guest"
    
    if options.private:
        private = "0"
    else:
        private = "1"
    
    if options.expire_date:
        if options.expire_date not in ExpOpt:
            print "invalid paste expires argument!\nUse following syntax :"
            for Opts in ExpOpt:
                print Opts + " \t=> " + ExpOpt[Opts]
            sys.exit(1)

except IOError, err:
    if "directory" in str(err[1]):
        print "[!]\tCan't open file " + options.file
        sys.exit(1)
    else:
        print "[!]\t" + err[1]
        sys.exit(1)

def getCodeType():
    ext = os.path.splitext(options.file)[1]
    syntax = "text"
    AutoExts = {
        ".4cs": "4cs", ".abap": "abap", ".as": "actionscript", ".asm": "asm",
        ".asp": "asp", ".sh": "bash", ".cs": "csharp", ".c": "c", ".cpp": "cpp",
        ".css": "css", ".html": "html4strict", ".h": "c", ".java": "java",
        ".js": "javascript", ".LUA": "lua", ".php": "php", ".pl": "perl",
        ".py": "python", ".sql": "sql"
        }
    for AutoExt in AutoExts:
        if AutoExt == ext:
            syntax = AutoExts[AutoExt]
    
    return syntax

def PasteIt(paste_name, paste_format, paste_code, paste_private, paste_expire):
    if user != "guest":
        LoginParam = urllib.urlencode({'api_dev_key': APIKEY,
        'api_user_name': user,
        'api_user_password': password
        })
        PostLogin = urllib.urlopen(URL + '/api/api_login.php',LoginParam)
        try:
            LoginRespond = PostLogin.read()
            if "Bad API" in LoginRespond:
                print "[!] Error : " + LoginRespond
                sys.exit(1)
            else:
                PasteParam = urllib.urlencode({'api_option': 'paste',
                'api_user_key': LoginRespond,
                'api_dev_key': APIKEY,
                'api_paste_name': paste_name,
                'api_paste_format': paste_format,
                'api_paste_code': paste_code,
                'api_paste_private': paste_private,
                'api_paste_expire_date': paste_expire
                })
        finally:
            PostLogin.close()
    
    else:
        PasteParam = urllib.urlencode({'api_option': 'paste',
        'api_dev_key': APIKEY,
        'api_paste_name': paste_name,
        'api_paste_format': paste_format,
        'api_paste_code': paste_code,
        'api_paste_private': paste_private,
        'api_paste_expire_date': paste_expire
        })
    
    PostPaste = urllib.urlopen(URL + '/api/api_post.php',PasteParam)
    try :
        response = PostPaste.read()
        print response
    finally:
        PostPaste.close()

if __name__ == "__main__":
    if options.type != "text":
        if options.type not in FileType:
            print options.type + " syntax is not available on pastebin, using default filetype syntax.."
            UsedSyntax = getCodeType()
        else:
            UsedSyntax = options.type
    else:
        UsedSyntax = getCodeType()
    print "[+] File : " + options.file
    print "[+] Syntax : " + UsedSyntax
    print "[+] post as : " + user
    print "[+] Expires : " + ExpOpt[options.expire_date]
    PasteIt(options.name, UsedSyntax, fileU, private, options.expire_date)