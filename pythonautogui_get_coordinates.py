import pyautogui
from ctypes import *

screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX,',' ,currentMouseY, sep='')
