from selenium import webdriver
from getpass import getpass
from selenium.webdriver.common import keys
import time
import sys
import re
from colorama import Fore
print(Fore.GREEN + '''  
 _   _     _                           _         _        
| | | | __| | ___ _ __ ___  _   _     / \  _   _| |_ ___  
| | | |/ _` |/ _ \ '_ ` _ \| | | |   / _ \| | | | __/ _ \ 
| |_| | (_| |  __/ | | | | | |_| |  / ___ \ |_| | || (_) |
 \___/ \__,_|\___|_| |_| |_|\__, | /_/   \_\__,_|\__\___/ 
                            |___/                         
 _____                 _ _           
| ____|_ __  _ __ ___ | | | ___ _ __ 
|  _| | '_ \| '__/ _ \| | |/ _ \ '__|
| |___| | | | | | (_) | | |  __/ |   
|_____|_| |_|_|  \___/|_|_|\___|_|   


  Github : https://github.com/the-avengersz\n
  TG : https://t.me/the_avengersz
                                     
                                      
     ''')

emailid=input(Fore.RED+ 'Enter Email Address: ')
passwordd=getpass()
browser = webdriver.Chrome()


def login():
    browser.get('https://www.udemy.com/join/login-popup/')
    time.sleep(5)
    mail=browser.find_elements_by_xpath('//*[@id="email--1"]')
    mail[0].send_keys(emailid)
    passs=browser.find_elements_by_css_selector('#id_password')
    passs[0].send_keys(passwordd)
    browser.find_element_by_xpath('//*[@id="submit-id-submit"]').click()

def auth():
    browser.get('https://www.udemy.com/')
    time.sleep(10)
    try:
        browser.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/nav/ul/li[2]/div/a')

    except:
        print(Fore.RED + 'Invalid Email/Password Recheck and Rerun Once. ')
        browser.quit()
        sys. exit()   
        
    else:
       print(Fore.GREEN + 'Login Sucess, Enrolling Now')       
        


def Enrolled():    
    with open('courses.txt','r')as courses:
        for line in courses:
            if re.search("https://www.udemy.com/", line):
                browser.get(line)
                time.sleep(15)
                try:
                    enroll=browser.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div[3]/div/div/div/div[1]/div/div[1]/div[2]/div/div[1]/div/div[5]/div/button')
                    browser.execute_script("arguments[0].click();", enroll)
                    time.sleep(15)
                    enrollnow=browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div[2]/form/div[2]/div/div[4]/button')
                    browser.execute_script("arguments[0].click();", enrollnow)
                    print('Sucesfully Enrolled '+line)
                except:
                    print(Fore.RED + "Course Not Free or Coupan expired. So Trying to enroll Next one from the list ")
            else:
                print(Fore.RED + "PLease Enter a valid URL. Trying to enroll Next one from the list.") 

login()
auth()
Enrolled()
