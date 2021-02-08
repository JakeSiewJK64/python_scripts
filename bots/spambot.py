import pyautogui
import time

time.sleep(5)
for i in range (1, 10):
    pyautogui.typewrite("sup")
    pyautogui.press("enter")