#Before Copy Codes, Take Owner Permission or Give a Credits!
# Made by @palahsu

import random
generate_otp = random.randint(000000,100000)
username = input ("username: ")
password = input ("password: ")

print ('Hi,', username)
print ('Hi,', password)

print ('Here is your OTP for login',generate_otp)

passw = input ("Enter the OTP to login: ")

if passw == str (generate_otp):
  print ("Login Successful!")
else:
    passw == str (generate_otp)
    print ("Failed!")

    
