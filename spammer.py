import pyautogui
import time
time.sleepd(5)
f = open("script.txt", 'r')
for word in f:
    pyautogui.typewrite(word)
    #time.sleep(1)
    pyautogui.press("enter")

