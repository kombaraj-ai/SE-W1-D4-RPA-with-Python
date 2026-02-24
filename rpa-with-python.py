import pyautogui
import time

# Type a message
pyautogui.typewrite("Hello, RPA World!", interval=0.05)

# Move mouse to coordinates (500, 300) and click
pyautogui.moveTo(500, 300, duration=1)
pyautogui.click()