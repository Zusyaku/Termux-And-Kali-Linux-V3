####using python2######
import pyautogui
import time
time.sleep(5)
f = open(‘list.txt’,’r’)
for word in f:
pyautogui.typewrite(word)
pyautogui.press(‘enter’)
