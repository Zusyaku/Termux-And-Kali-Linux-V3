Set wshShell =wscript.CreateObject("WScript.Shell")
do
wscript.sleep 10
WshShell.Run "notepad.exe", 2
loop