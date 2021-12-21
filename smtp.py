import smtplib, ssl
import os
import sys
import time
from sys import platform
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def clear():
	if platform == "linux":
		os.system('clear')
	else:
		os.system('cls')


banner = """
\033[34;1m███████╗███╗   ███╗████████╗██████╗  \033[31;1m    ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗
\033[34;1m██╔════╝████╗ ████║╚══██╔══╝██╔══██╗ \033[31;1m   ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝
\033[34;1m███████╗██╔████╔██║   ██║   ██████╔╝ \033[31;1m   ██║     ███████║█████╗  ██║     █████╔╝ 
\033[34;1m╚════██║██║╚██╔╝██║   ██║   ██╔═══╝  \033[31;1m   ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ 
\033[34;1m███████║██║ ╚═╝ ██║   ██║   ██║      \033[31;1m   ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗
\033[34;1m╚══════╝╚═╝     ╚═╝   ╚═╝   ╚═╝      \033[31;1m    ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝
\n\t\t\t\033[34m    | \033[37m@f4c3r100 \033[34m| \033[37mv1.2  \033[34m|
\t\t\t\033[34m    | \033[37mSCARLETTA \033[34m| \033[37mTOOLS \033[34m|
\033[0m
"""




def send(smtp, receiver):
	to = receiver
	smtp = smtp
	host = smtp.split('|')[0]
	port = smtp.split('|')[1]
	user = smtp.split('|')[2]
	pssw = smtp.split('|')[3]
	message = f"""
<!DOCTYPE html>
<html>
<head>
</head>
<body>
	<center>
		<h1>📧 SCARLETTA SMTP CHECKER 📧</h1> <br>
		<font color="00c4ff"><h2>SMTP Works</h2></font><br><br></center>
		<font color="black" size="5"><font color="red">Host => </font>{host}<br></font>
		<font color="black" size="5"><font color="red">Port => </font>{port}<br></font>
		<font color="black" size="5"><font color="red">User => </font>{user}<br></font>
		<font color="black" size="5"><font color="red">Pass => </font>{pssw}<br></font>
		<font color="black" size="5"><font color="red">Mailer Format =></font>{host}|{port}|{user}|{pssw}<br></font>
		<br><br><br><center>
		<a href="https://t.me/tutorials_zone">
		<button style="background-color: #4CAF50; border: none; color: white; padding: 14px 32px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer">JOIN CHANNEL</button>
		</a>
		<h6>Made By @f4c3r100</h6>
	<br>
	</center>
	</body>
</html>\r\n
	""".format(host, port, user, pssw, smtp)
	msg = MIMEMultipart('alternative')
	msg['Subject'] = "📧 SMTP CHECKER | SCARLETTA 📧"
	msg['From'] = user
	msg['To'] = to
	eee = MIMEText(message, 'html')
	msg.attach(eee)
	context=ssl.create_default_context()
	if port == "587":
		try:
			smtp = smtplib.SMTP(host, port)
		except Exception as e:
			print(e)
			pass
		check = smtp.noop()
		if check[0] == 250:
			print(f"\033[34m+========================+\033[0m")
			print(f"\033[34m| \033[37m{host}\033[35m|\033[37m{port}\033[35m|\033[37m{user}\033[35m|\033[37m{pssw}\033[0m")
			print(f"\033[34m+========================+\033[0m")
			print("\033[34m[\033[32m*\033[34m] \033[37mSMTP server connected\033[0m")
			try:
				ehlo = smtp.ehlo()
				if ehlo[0] == 250:
					#temp = str(ehlo[0].decode().replace("\n", "|").split("|"))
					print(f"\033[34m[\033[32m*\033[34m] \033[37mSMTP communicated")#\n\033[37m+++ Debug : \033[35m{temp[0]}\033[37m|\033[35m{temp[4]}\033[37m|\033[35m{temp[5]}\033[0m")
					try:
						starttls = smtp.starttls(context=context)
						if starttls[0] == 220:
							print(f"\033[34m[\033[32m*\033[34m] \033[37mSMTP TLS encryption started")#\n\033[37m+++ Debug : \033[35m{starttls[1].decode()}\033[0m")
							try:
								log = smtp.login(user, pssw)
								if log[0] == 235:
									print(f"\033[34m[\033[32m*\033[34m] \033[37mSMTP authentication successfully\033[0m")
									try:
										send = smtp.sendmail(msg['From'], msg['To'], msg.as_string())
										if send == {}:
											print(f"\033[34m[\033[32m*\033[34m] \033[32mMail send to {to}\033[0m")
											print(f"\033[34m+========================+\033[0m")
									except Exception as e:
										#print(e)
										print(f"\033[34m[\033[31m!\033[34m] \033[31mMail failed send to {to}\033[0m")

							except Exception as e:
								print(f"\033[34m[\033[31m!\033[34m] \033[31mSMTP authentication Failed \033[0m")
								pass

					except Exception as e:
						print(e)
						#print(f"\033[34m[\033[31m!\033[34m] \033[31mCan't authenticate | CODE: {log[0]} \033[0m")
						#print(e)
						pass

			except Exception as e:
				#print(e)
				print(f"\033[34m[\033[31m!\033[34m] \033[31mCan't connect EHLO to host. | CODE: {ehlo[0]} \033[0m")
				pass

		else:
			print(f"\033[34m[\033[31m!\033[34m] \033[31mCan't connect to SMTP Host | CODE: {check[0]} \033[0m")

	elif port == "465":
		try:
			smtp = smtplib.SMTP_SSL(host, port)
			check = smtp.noop()
			
		
			if check[0] == 250:
				print(f"\033[34m+========================+\033[0m")
				print(f"\033[34m| \033[37m{host}\033[35m|\033[37m{port}\033[35m|\033[37m{user}\033[35m|\033[37m{pssw}\033[0m")
				print(f"\033[34m+========================+\033[0m")
				print("\033[34m[\033[32m*\033[34m] \033[37mSMTP server connected\033[0m")
				try:
					ehlo = smtp.ehlo()
					if ehlo[0] == 250:
						#temp = str(ehlo[0].decode().replace("\n", "|").split("|"))
						print(f"\033[34m[\033[32m*\033[34m] \033[37mSMTP communicated")#\n\033[37m+++ Debug : \033[35m{temp[0]}\033[37m|\033[35m{temp[4]}\033[37m|\033[35m{temp[5]}\033[0m")
						try:
							log = smtp.login(user, pssw)
							if log[0] == 235:
								print(f"\033[34m[\033[32m*\033[34m] \033[37mSMTP authentication successfully\033[0m")
								try:
									send = smtp.sendmail(msg['From'], msg['To'], msg.as_string())
									if send == {}:
										print(f"\033[34m[\033[32m*\033[34m] \033[32mMail send to {to}\033[0m")
										print(f"\033[34m+========================+\033[0m")
								except Exception as e:
									#print(e)
									print(f"\033[34m[\033[31m!\033[34m] \033[31mMail failed send to {to}\033[0m")

						except Exception as e:
							#print(e)
							print(f"\033[34m[\033[31m!\033[34m] \033[31mSMTP authentication Failed\033[0m")
							pass

				except Exception as e:
					#print(e)
					print(f"\033[34m[\033[31m!\033[34m] \033[31mCan't ehlo server | CODE: {ehlo[0]} \033[0m")
					#print(e)
					pass

			else:
				print(f"\033[34m[\033[31m!\033[34m] \033[31mCan't connect to SMTP Host | CODE: {check[0]} \033[0m")
		except Exception:
			pass

	else:
		smtp = smtplib.SMTP(host, port)
		check = smtp.noop()
		if check[0] == 250:
			print(f"\033[34m+========================+\033[0m")
			print(f"\033[34m| \033[37m{host}\033[35m|\033[37m{port}\033[35m|\033[37m{user}\033[35m|\033[37m{pssw}\033[0m")
			print(f"\033[34m+========================+\033[0m")
			print("\033[34m[\033[32m*\033[34m] \033[37mSMTP server connected\033[0m")
			try:
				ehlo = smtp.ehlo()
				if ehlo[0] == 250:
					#temp = str(ehlo[0].decode().replace("\n", "|").split("|"))
					print(f"\033[34m[\033[32m*\033[34m] \033[37mSMTP communicated")#\n\033[37m+++ Debug : \033[35m{temp[0]}\033[37m|\033[35m{temp[4]}\033[37m|\033[35m{temp[5]}\033[0m")
					try:
						log = smtp.login(user, pssw)
						if log[0] == 235:
							print(f"\033[34m[\033[32m*\033[34m] \033[37mSMTP authentication successfully\033[0m")
							try:
								send = smtp.sendmail(msg['From'], msg['To'], msg.as_string())
								if send == {}:
									print(f"\033[34m[\033[32m*\033[34m] \033[32mMail send to {to}\033[0m")
									print(f"\033[34m+========================+\033[0m")
							except Exception as e:
								#print(e)
								print(f"\033[34m[\033[31m!\033[34m] \033[31mMail failed send to {to}\033[0m")

					except Exception as e:
						#print(e)
						print(f"\033[34m[\033[31m!\033[34m] \033[31mSMTP authentication Failed | CODE: {log[0]} \033[0m")
						pass

			except Exception as e:
				#print(e)
				print(f"\033[34m[\033[31m!\033[34m] \033[31mCan't connect start TLS | CODE: {check[0]} \033[0m")
				#print(e)
				pass

		else:
			print(f"\033[34m[\033[31m!\033[34m] \033[31mCan't connect to SMTP Host | CODE: {check[0]} \033[0m")

def main():
	clear()
	print(banner)
	smtps = input("\033[34m[ \033[37mSCARLETTA\033[34m | \033[37mSMTP\033[34m ] \033[37mInput your SMTPs:\033[32m ")
	receiver = input("\033[34m[ \033[37mSCARLETTA \033[34m| \033[37mSMTP\033[34m ] \033[37mYour Email :\033[32m ")
	
	smtp_ = open(smtps, "r")
	wll = smtp_.readlines()
	for smtp in wll:
		smtp = smtp.replace("\n","")
		send(smtp, receiver)



if __name__ == '__main__':
	main()