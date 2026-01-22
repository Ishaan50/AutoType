import pyautogui as s
import time

s.press("win")
time.sleep(1)

s.write ("notepad" , interval=0.2)
s.press("enter")

time.sleep(1)

s.write("Hello world", interval=0.2)
