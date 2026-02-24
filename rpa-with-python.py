import pyautogui
import time
import subprocess

# Type a message
##pyautogui.typewrite("Hello, RPA World!", interval=0.05)

# Move mouse to coordinates (500, 300) and click
##pyautogui.moveTo(500, 300, duration=1)
##pyautogui.click()


# Open Notepad
subprocess.Popen(["notepad.exe"])
time.sleep(1)  # Wait for Notepad to open
pyautogui.hotkey("ctrl", "n")  
# Type into Notepad
pyautogui.typewrite("This text was typed by a Python RPA bot.", interval=0.05)
pyautogui.hotkey("ctrl", "s")
pyautogui.typewrite("Test.txt", interval=0.05)
# Press Enter
pyautogui.press("enter")