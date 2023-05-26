import pyautogui
import time
import random

def run():
  while True:
    x = random.randint(100, 1800)
    y = random.randint(20, 1060)
    pyautogui.moveTo(x, y)
    time.sleep(1)