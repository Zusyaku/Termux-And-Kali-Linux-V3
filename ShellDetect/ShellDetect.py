#Author: Amit Malik (DouBle_Zer0) - m.amit30@gmail.com
#Copyright - (C) 2011 
#V1.3
#Last Update - 22-6-12

import sys,os,subprocess,time,struct,random,re,binascii
from ctypes import *
from threading import Thread

# Globals
KERNEL32 = windll.kernel32
PROCESS_ALL_ACCESS 		= 0x001F0FFF
PROCESS_TERMINATE		= 0x00000001
ACTIVE					= 0x00000103
global PID
global state
PID = 0
state = 0
FILE = "schandler.exe"


def greet():
	print
	greet = "Author: Amit Malik (m.amit30@gmail.com)"
	print "\t\t"+"*"*(len(greet)+18)
	print "\t\t"+"*\t"+greet+"\t\t*"
	print "\t\t"+"*\t"+"http://www.securityxploded.com"+"\t\t\t*"
	print "\t\t"+"*"*(len(greet)+18)
	

class MonitorProcess:
		def __init__(self):
			self.pid = None
			self._tmp_pid = None
			self.counter = 0
		
		def CheckProcess(self):
			Handle_P = KERNEL32.OpenProcess(PROCESS_ALL_ACCESS, False, int(self.pid))
			if not Handle_P:
				return False
			exit_status = c_ulong(0)
			KERNEL32.GetExitCodeProcess(Handle_P, byref(exit_status))
			
			if exit_status.value == ACTIVE:
				self.counter = self.counter + 1
				return True
				
			return False
		
		def TerminateProcess(self):
			try:
				handle = KERNEL32.OpenProcess(PROCESS_TERMINATE, False, int(self.pid))
				KERNEL32.TerminateProcess(handle,-1)
				KERNEL32.CloseHandle(handle)
				return True
			except:
				return True
		
		def Start(self):
			global PID
			global state
			while True:
				self.pid = PID
				if self._tmp_pid == self.pid:
					status = self.CheckProcess()
					if status:
						if self.counter >= 5:
							self.TerminateProcess()
							self.counter = 0
				else:
					self.counter = 0
				self._tmp_pid = self.pid
				if state:
					sys.exit(0)
				time.sleep(1)
				

				
class ShellDetect(Thread):
		def __init__(self,counter,feed):
					Thread.__init__(self)
					self.counter 	= counter
					self.feed		= feed
					self.size		= os.path.getsize(feed)
		def _unicodetobin(self,data):
					data = data.split("%u")
					data = data[1:]
					j = ''
					for i in data:	
						j += i[-2:]+i[:2]
					j = binascii.unhexlify(j)
					return j
				
		def _shelldetect(self):
					global PID
					global state
					print "\n[*] Total number of bytes: %d\n" % self.size
					ffile = "dump.bin"
					fp = open(self.feed,"rb")
					data = fp.read()
					if re.match("%u",data):
						print "[*] Converting payload to binary\n"
						data = self._unicodetobin(data)
						self.size = len(data)
						print "[*] Total number of bytes to scan: %d\n" % self.size
					i = 0
					prev_byte = 0
					while True:
						c = data[i:]
						if len(c) < 200:
							print "\n[*] Clean Stream!\n"
							break
							
						else:
							fpf = open(ffile,"wb")
							fpf.write(c)
							fpf.close()
							process = subprocess.Popen([FILE],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
							PID = process.pid
							process.communicate(ffile)
							if process.poll() == 0:
								if os.path.exists("Dump_mem.bin") and os.path.getsize("Dump_mem.bin") > 0:
									print "\n[*] Shellcode Detected\n"
									break
								else:
									i = i + 1
							else:
								try:
									fpt = open("track.txt","r")
									inum = fpt.read()
									fpt.close()
									j = struct.unpack('L',inum)[0]
									i = i + j
									if prev_byte == i:
										i = i + 1
									per = (i/float(self.size))*100
									if i > self.size:
										i = self.size
										per = 100
									print "Bytes Scanned: %d  (%.1f" % (i,per)+" %)"
									os.remove(ffile)
									os.remove("track.txt")
									prev_byte = i
								except:
									i = i + 1
									
					try:
						os.remove(ffile)
						os.remove("track.txt")
						fp.close()
					except:
						pass
					state = 1
					sys.exit(0)
					
					
		def run(self):
					if self.counter == 0:
						MonitorProcess().Start()
					self._shelldetect()	
				
				
def main():
		greet()
		if len(sys.argv) < 2:
			print "\n[*] Usage: ShellDetect.py file_name"
			sys.exit(0)
		feed = sys.argv[1]
		if not os.path.exists(feed):
			print "\n[*] File not found.. Aborting!"
			sys.exit(0)
		for counter in range(0,2):
			ShellDetect(counter,feed).start()

if __name__ == '__main__':
		main()