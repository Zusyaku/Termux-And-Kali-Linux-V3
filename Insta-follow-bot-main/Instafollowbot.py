from selenium import webdriver
import datetime
import random
import time
from webdriver_manager.chrome import ChromeDriverManager #1st changer

driver = webdriver.Chrome(ChromeDriverManager().install()) #2nd change
driver.get('https://www.instagram.com')

time.sleep(1)

#auto login information
def login():
    driver.find_element_by_name('username').send_keys(username)
    time.sleep(1)
    driver.find_element_by_name('password').send_keys(password)
    time.sleep(1)
    driver.find_element_by_class_name('L3NKy   ').click()
    time.sleep(random.randint(3, 4))

#Search Tags
def search(tag):
    address = 'https://www.instagram.com/explore/tags/'
    driver.get(address + tag)
    time.sleep(random.randint(3, 4))
    driver.find_elements_by_class_name('_9AhH0')[10].click()
    time.sleep(random.randint(3, 4))

#Make Auto Likes
def like():
    global like_cnt
    #Exception handling
    try:
        driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
        time.sleep(random.randint(3, 4))
        driver.find_element_by_class_name('fr66n').click()
        time.sleep(random.randint(1, 2))
        like_cnt += 1
    except:
        print('Error')
        time.sleep(5)
        return 

if __name__ == '__main__':

#Write Username and password
    username = 'your_username'
    password = 'your_password'

    #Tag Setting
    tags = ['car','bikelover','nickiminaj','arianagrande']

    like_cnt = 0
    begin = datetime.datetime.today()
    tag = random.choice(tags)

    login()
    search(tag)

    #Like Number Count
    while like_cnt < 100:  #Please, dont use over!
        like()

    driver.quit()
    end = datetime.datetime.today()

    print('Start：' + str(begin))
    print('Finish：' + str(end))
    print('Tag is ' + tag + ' Number of Likes：' + str(like_cnt))

