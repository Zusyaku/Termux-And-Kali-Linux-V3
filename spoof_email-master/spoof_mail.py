#!/usr/bin/env python3

import smtplib, readline, dns.resolver, sys


def start():
    domain = sys.argv[1]
    check_mx(domain)

def check_mx(domain):
    d = []
    num = 0
    for x in dns.resolver.query(domain, 'MX'):
        d.append(x.to_text().split(' ')[1][:-1])

    if len(d) == 1:
        print('Using: %s' % d[0])
        send_mail(d[0])
    else:
        pass

    print('Found %i MX records\nPlease, select:' % len(d))

    for i in d:
        print('\t%i) %s' % (int(num), i))
        num +=1
    select = int(input('[#?]: '))
    try:
        s = d[int(select)]
        print('Using: %s' % s)
        send_mail(s)
    except Exception as e:
        print('[ERROR] Invalid option...')

def send_mail(mx):
    fromaddr = input("From: ").strip()
    to  = input("To: ").strip().split()

    body = 'Spoof test'
    subject = 'Hello World!'

    msg = 'Subject: ' + subject + '\n' + body

    server = smtplib.SMTP(mx)
    server.set_debuglevel(1)
    server.sendmail(fromaddr, to, msg)
    server.quit()

start()
