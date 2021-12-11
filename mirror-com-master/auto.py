# coding=utf-8
#!/data/data/com.termux/files/usr/bin/python2
# Mirroring From : https://raw.githubusercontent.com/Datez-Kun/Mirror-Comz/master/pirmansx.py
# © Copyright Datez-Kun (2020)
# Time : Sun Jul  5 01:26:47 WIB 2020
import re
from sys import argv
from os import system,remove,rename

class Mirror(object):
	def __init__(self,file,out,mode):
		self.file = file
		self.out = out
		self.mode = mode
		self.wrote = '65203d2027270a692c6a203d2028302c30290a0a7768696c6520313a0a2020202069662069203e3d206c656e2864293a20627265616b0a202020206966206a203e3d206c656e286b293a206a203d20300a2020202065202b3d2063687228645b695d205e206b5b6a5d290a2020202069202b3d20310a202020206a202b3d20310a696d706f7274206d61727368616c0a65786563286d61727368616c2e6c6f61647328652929'.decode("hex")
		self.peyec = '77697468206f70656e28276f75742e707963272c277762272920617320663a0a20202020662e7772697465282230336633306430613764636566653565222e6465636f6465282768657827292b6529'.decode("hex")
		if self.mode == '1':
			self.disAssemble(self.file)
			self.get_list('tmp.dis')
			self.disAssemble('tmp.py')
			self.get_list('tmp.dis')
			self.Write_Pyc('tmp.py')
		elif self.mode == '2':
			self.disAssemble(self.file)
			self.get_list('tmp.dis')
			self.disAssemble('tmp.py')
			self.get_list('tmp.dis')
			self.disAssemble('tmp.py')
			self.get_list('tmp.dis')
			self.Write_Pyc('tmp.py')
		elif self.mode == '3':
			self.disAssemble(self.file)
			self.get_list('tmp.dis')
			self.disAssemble('tmp.py')
			self.get_list('tmp.dis')
			self.disAssemble('tmp.py')
			self.get_list('tmp.dis')
			self.disAssemble('tmp.py')
			self.get_list('tmp.dis')
			self.Write_Pyc('tmp.py')
		else:
			exit('[*] List Mode : 1.(cepat), 2.(sedang), 3.(lambat)')
	def disAssemble(self,ofset):
		print '[*] disassemble file!'
		ope = open(ofset).read()
		if 'exec' and 'marshal.loads' in ope:
			xis = ope.replace('exec','exe=')
			f = open('tmp.py','w')
			f.write('import dis,marshal\n%s\ndis.dis(exe)'%(xis))
			f.close()
			system('py2 tmp.py > tmp.dis')
		else:
			if '.pyc' in ofset:
				system('pycdc %s > %s'%(ofset,ofset.replace('.pyc','.py')))
			else:
				rename(ofset,'%sc'%(ofset))
				system('pycdc %sc > %s'%(ofset,ofset))
			fox = open(ofset.replace(".pyc",".py")).read()
			cok = fox.replace("exec","exe=")
			f = open('tmp.py','w')
			f.write('import dis,marshal\n%s\ndis.dis(exe)'%(cok))
			f.close()
			system('py2 tmp.py > tmp.dis')
	def get_list(self,fel_):
		print '[*] searching list !'
		dat_d = []
		dat_k = []
		data_ = []
		value = 1
		var = 0
		ope = open(fel_).read()
		kons = re.findall(r"\((\d+)\)",ope)
		max = len(kons)-3
		cuk = kons[:max]
		buil = re.findall('BUILD_LIST.*?(.*\d)',ope)
		for i in range(int(buil[0])):
			dat_d.append(cuk[var])
			var +=1
		for o in range(int(buil[1])):
			dat_k.append(cuk[-value])
			value +=1
		data_.append('d = '+repr(dat_d).replace("'",""))
		data_.append('k = '+repr(dat_k[::-1]).replace("'",""))
		f = open('tmp.py','w')
		f.write('%s\n%s\n%s'%(data_[0],data_[1],self.wrote))
		f.close()
		del dat_k[:]
		del dat_d[:]
		del data_[:]
		var = 0
		value = 1
	def Write_Pyc(self,target):
		print '[*] writing to bytecode!'
		fi = open(target).read()
		go = fi.replace('exe','#exe')
		wr = open('tmp.py','w')
		wr.write('%s\n%s'%(go,self.peyec))
		wr.close()
		system('python2 tmp.py')
		system('mv out.pyc %s'%(self.out))
		print '[*] saved bytecode to file >> ``%s``'%(self.out)

if __name__=="__main__":
	if len(argv) < 3:
		exit('usage : py2 %s <file> <out> <mode>'%(argv[0]))
	else:
		Mirror(argv[1],argv[2],argv[3])
