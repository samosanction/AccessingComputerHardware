import pyautogui
import time

position = pyautogui.position()
print(position)

pyautogui.doubleClick(132, 200)
time.sleep(1)
pyautogui.press('down')
pyautogui.press('enter')
pyautogui.write('Python is a good language! \n')

pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')
pyautogui.press(5 * ['down'])
pyautogui.hotkey('ctrl', 'v')