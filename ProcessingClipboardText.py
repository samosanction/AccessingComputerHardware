import pyautogui
import paperclip

position = pyautogui.position()
print(position)

pyautogui.doubleClick(126, 231)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')

text = pyautogui.paste()
pyautogui.alert(text)
print(text)
