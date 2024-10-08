import pyautogui
import time
import random

print("Aguarde 5 segundos para iniciar...")
time.sleep(5)

for _ in range(4):
    for _ in range(4):
        pyautogui.write(str(random.randint(1, 5)))
        pyautogui.press('enter')
        pyautogui.write(str(random.randint(0, 59)))
        pyautogui.press('enter')

    time.sleep(.5)

print("Autofill finalizado!")