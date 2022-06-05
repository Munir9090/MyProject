import pyautogui
import time

# Klik Start
pyautogui.moveTo(22, 746, 2)
pyautogui.click(22, 746, button='left')

# Tombol Start
time.sleep(1)
pyautogui.moveTo(26, 700, 1)
pyautogui.click(26, 700, button='left')

# Shut Down
pyautogui.moveTo(67, 620, 1)
pyautogui.doubleClick(67, 620, button='left')