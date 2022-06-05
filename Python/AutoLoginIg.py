import pyautogui
import time

# Buka Browser
pyautogui.moveTo(33, 127, 1)
pyautogui.doubleClick(33, 127, button='left')
pyautogui.moveTo(246, 77, 1)

# Ketik Keywoard
time.sleep(1)
pyautogui.typewrite('instagram\n', interval=0.20)

# Hasil
time.sleep(1)
pyautogui.moveTo(98, 317, 2)
pyautogui.click(98, 317, button='left')

# Login Akun Ig
pyautogui.moveTo(320, 296, 2)
pyautogui.click()
pyautogui.typewrite('munirrr48', interval=0.20)
pyautogui.moveTo(290, 338, 2)
pyautogui.click()
pyautogui.typewrite('Munir_2002', interval=0.20)

# Klik Masuk
time.sleep(1)
pyautogui.moveTo(366, 387, 2)
pyautogui.click(366, 387, button='left')

time.sleep(1)
pyautogui.moveTo(361, 461, 2)
pyautogui.click(361, 461, button='left')

# Scroll
while True:
    pyautogui.scroll(-50)

