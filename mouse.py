import pyautogui

position = pyautogui.position()

pyautogui.moveTo(139, 280, duration=1)

pyautogui.click(clicks=2)

# Alternative code for doubleclicking

pyautogui.doubleClick()

# Clicking a specific location
pyautogui.click(139, 280)

# to perform a right-click on windows

pyautogui.click(139, 280, button='right')
