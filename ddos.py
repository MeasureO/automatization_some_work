import pyautogui
import webbrowser as wb
import ctypes
import detect_layout as layout
from datetime import datetime
from time_now import get_hour
import time


x, y = pyautogui.size()
cx, cy = pyautogui.position()
print(cx, cy)
i = 1
#while True:
# wb.open(input())
#pyautogui.alert('This is an alert box.')
#name = input("Input name: ")
#text = input("Input text: ")
#number = input("Number of messages: ")
while True:
    hour = get_hour()
    if hour == 5:
        pyautogui.moveTo(460, 1057)
        pyautogui.click()

        # pyautogui.moveTo(423, 75)
        # pyautogui.hotkey('ctrl', 't')  
        # pyautogui.click()
        # pyautogui.write(text, interval=0.01)
        # pyautogui.click()

        # pyautogui.hotkey('alt', 'shift')
        # pyautogui.write('rfhnbyrb c rjnznfvb ,tp cvc b htubcnhfwbb', interval=0.01)
        # pyautogui.hotkey('alt', 'shift')
        # pyautogui.keyDown('enter')
        # pyautogui.moveTo(329, 318)
        # pyautogui.keyDown('enter')
        pyautogui.moveTo(16, 30)
        pyautogui.click()
        pyautogui.moveTo(223, 414)
        pyautogui.click()
        if layout.get_keyboard_language() != 'Russian':
            pyautogui.hotkey('alt', 'shift')
        #pyautogui.write(name, interval=0.01)
        pyautogui.write('gjcnjhjyybv', interval=0.01)
        pyautogui.moveTo(358, 596)
        pyautogui.click()
        pyautogui.moveTo(1035, 970)
        pyautogui.click()

        pyautogui.write("Jncencnde.obt&", interval=0.01)
        pyautogui.hotkey('alt', 'shift')
        pyautogui.moveTo(1866, 977)
        # for i in range(10):
        #     pyautogui.write("C yjdsv ujljv! ", interval=0.01)
    #if hour == 0:
    #    b = False
    time.sleep(10)
