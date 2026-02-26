# Week 1 -> Day 4 -> RPA with Python  

## Table of Contents

*   [Create a RPA Python App with Virtual Environment](#create-a-rpa-python-app-with-virtual-environment)
*   [Assignment 1: pyAutoGUI RPA Automation](Assignment1_pyAutoGUI/PROJECT_SUMMARY.md)
    *   [Run Assignment 1 Demo](Assignment1_pyAutoGUI/QUICK_START.md)
*   [Assignment 2: Playwright Automation](Assignment2_Playwright/PROJECT_SUMMARY.md)
    *   [Run Assignment 2 Demo](Assignment2_Playwright/QUICK_START.md)
*   [Python RPA: Robotic Process Automation](#python-rpa-robotic-process-automation)
    *   [Module 1: PyAutoGUI](#module-1-pyautogui)
        *   [PyAutoGUI Core Operations](#pyautogui-core-operations)
            *   [1. Get Screen Coordinates](#1-get-screen-coordinates)
            *   [2. Mouse Operations](#2-mouse-operations)
            *   [3. Keyboard Operations](#3-keyboard-operations)
            *   [4. Image Recognition](#4-image-recognition)
    *   [Module 2: Playwright](#module-2-playwright)
        *   [1. Browser Context](#1-browser-context)
        *   [2. Pages](#2-pages)
        *   [3. Selectors](#3-selectors)
        *   [4. Async](#4-async)                    
    *   [Module 3: Selenium](#module-3-selenium)        


## Create a RPA Python App with Virtual Environment

Now let's create a simple Python project with a virtual environment — a best practice for keeping project dependencies isolated.

### Step 1: Create a Project Folder

1. Open **File Explorer** and navigate to where you want to create your project (e.g., `Documents`).
2. Create a new folder named `W1-D4-RPA-with-Python`.
3. Open **VS Code**.
4. Go to **File → Open Folder**, select `W1-D4-RPA-with-Python`, and click **Select Folder**.

### Step 2: Open the Integrated Terminal in VS Code

1. In VS Code, press `Ctrl + `` ` `` (backtick) to open the integrated terminal.
2. The terminal should open at the bottom of the screen, pointing to your `W1-D4-RAP-with-Python` folder.

### Step 3: Create a Virtual Environment

A virtual environment creates an isolated space for your project's Python packages.

In the VS Code terminal, run:

```bash
python -m venv .venv
```

This creates a folder called `.venv` inside your project directory.

Create a file '.gitignore'
```bash
# Virtual environment directory
.venv/

# Ignore the .gitignore file itself (for local use only)
.gitignore
```

### Step 4: Activate the Virtual Environment

Still in the VS Code terminal, run:

```bash
.\.venv\Scripts\activate
```

After activation, your terminal prompt will change to show `(venv)` at the beginning, like:

```
(venv) C:\Users\YourName\Documents\W1-D4-RAP-with-Python>
```

> 💡 **Note:** If you get a script execution error, run this first:
> ```bash
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```
> Then try the activate command again.

### Step 5: Create Python requirements.txt file

1. In VS Code, click the **New File** icon in the Explorer sidebar (or press `Ctrl+N`).
2. Name the file `requirements.txt`.
3. Add the following code:

```python
pyautogui
```
In terminal:
```bash
pip install -r .\requirements.txt
python.exe -m pip install --upgrade pip
```

4. Save the file with `Ctrl+S`.

### Step 6: Create the Hello World Python File

1. In VS Code, click the **New File** icon in the Explorer sidebar (or press `Ctrl+N`).
2. Name the file `rpa-with-python.py`.
3. Add the following code:

```python
import pyautogui
import time

# Type a message
pyautogui.typewrite("Hello, RPA World!", interval=0.05)

# Move mouse to coordinates (500, 300) and click
pyautogui.moveTo(500, 300, duration=1)
pyautogui.click()
```

4. Save the file with `Ctrl+S`.

### Step 7: Run the Python File

In the VS Code terminal (make sure `(venv)` is still showing), run:

```bash
python rpa-with-python.py
```

You should see the following output:

```
Hello, RPA World!
```

✅ Your first Python application is running successfully!

### Step 8: Deactivate the Virtual Environment (When Done)

When you're finished working, deactivate the virtual environment by running:

```bash
deactivate
```

The `(venv)` prefix will disappear from your terminal prompt.

### OPTIONAL: Create GitHub Repo and Push the code

Create a new GitHub Repository 'SE-W1-D4-RPA-with-Python' 

```bash
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/kombaraj-ai/SE-W1-D4-RPA-with-Python.git
git push -u origin main
```
---

# Python RPA (Robotic Process Automation)

## What is Python RPA?

**Robotic Process Automation (RPA)** is the use of software "robots" to automate repetitive, rule-based digital tasks that humans normally perform — such as clicking buttons, filling forms, copying data, and navigating websites.

**Python RPA** refers to using Python and its ecosystem of libraries to build these automation bots. Python is one of the most popular languages for RPA because of its:

- Simple, readable syntax
- Rich library ecosystem (PyAutoGUI, Selenium, Playwright, etc.)
- Strong community support
- Cross-platform compatibility (Windows, macOS, Linux)

### Common Use Cases

- Web scraping and data extraction
- Automated form filling and submission
- GUI automation (desktop apps)
- File and folder management
- Automated testing of web and desktop applications
- Report generation and email automation

---

## Module 1: PyAutoGUI

### What is PyAutoGUI?

`PyAutoGUI` is a Python library for **GUI (Graphical User Interface) automation**. It controls the mouse and keyboard programmatically to interact with desktop applications — anything you can click or type, PyAutoGUI can do.

### Installation

```bash
pip install pyautogui
```

### Key Features

- Mouse movement and clicks
- Keyboard input simulation
- Screenshot and image recognition
- Message boxes and alerts

### Example: Automate Mouse & Keyboard

```python
import pyautogui
import time

# Move mouse to coordinates (500, 300) and click
pyautogui.moveTo(500, 300, duration=1)
pyautogui.click()

# Type a message
pyautogui.typewrite("Hello, RPA World!", interval=0.05)

# Press Enter
pyautogui.press("enter")

# Take a screenshot and save it
screenshot = pyautogui.screenshot()
screenshot.save("screen.png")

print("Automation complete!")
```

### Example: Open Notepad and Type Text (Windows)

```python
import pyautogui
import time
import subprocess

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
```

### When to Use PyAutoGUI

Use PyAutoGUI when you need to automate **desktop applications** (like MS Office, Notepad, or any GUI app) where there is no API available.

## PyAutoGUI Core Operations

## 1. Get Screen Coordinates

### Screen Size
Get the dimensions of your primary monitor:

```python
import pyautogui

# Get screen width and height
screen_width, screen_height = pyautogui.size()
print(f"Screen size: {screen_width}x{screen_height}")
# Output example: Screen size: 1920x1080
```

### Current Mouse Position
Get the current position of the mouse cursor:

```python
# Get current mouse position
x, y = pyautogui.position()
print(f"Current mouse position: X={x}, Y={y}")
# Output example: Current mouse position: X=500, Y=300
```

### Display Mouse Position in Real-Time
Useful for finding coordinates for automation:

```python
import time

print("Move your mouse to the desired position...")
print("Press Ctrl+C to stop")

try:
    while True:
        x, y = pyautogui.position()
        print(f"X: {x:4d}  Y: {y:4d}", end='\r')
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nProgram stopped")
```

### Check if Coordinates are On Screen

```python
# Check if a point is within screen bounds
x, y = 2000, 1500
is_on_screen = pyautogui.onScreen(x, y)
print(f"Is ({x}, {y}) on screen? {is_on_screen}")
```

---

## 2. Mouse Operations

### Basic Mouse Movement

```python
import pyautogui
import time

# Move mouse to absolute position (x=100, y=200)
pyautogui.moveTo(100, 200)

# Move mouse relative to current position (50 pixels right, 100 pixels down)
pyautogui.move(50, 100)

# Move with duration (smooth movement over 2 seconds)
pyautogui.moveTo(500, 500, duration=2)
```

### Mouse Clicks

```python
# Single left click at current position
pyautogui.click()

# Click at specific coordinates
pyautogui.click(100, 200)

# Double click
pyautogui.doubleClick(300, 400)

# Triple click (useful for selecting text)
pyautogui.tripleClick()

# Click with duration (move to position over 1 second, then click)
pyautogui.click(500, 500, duration=1)

# Multiple clicks
pyautogui.click(clicks=3)  # Click 3 times
```

### Right Click and Middle Click

```python
# Right click
pyautogui.rightClick()
pyautogui.rightClick(200, 300)  # Right click at specific position

# Middle click
pyautogui.middleClick()
pyautogui.middleClick(400, 500)
```

### Mouse Button Operations (Press and Release)

```python
# Press and hold the left mouse button
pyautogui.mouseDown()

# Release the left mouse button
pyautogui.mouseUp()

# Press and hold at specific position with specific button
pyautogui.mouseDown(button='left', x=100, y=200)
pyautogui.mouseUp(button='left')

# Right button press and release
pyautogui.mouseDown(button='right')
pyautogui.mouseUp(button='right')
```

### Drag Operations

```python
# Drag from current position to (300, 400) over 2 seconds
pyautogui.dragTo(300, 400, duration=2, button='left')

# Drag relative to current position (100 pixels right, 50 pixels down)
pyautogui.drag(100, 50, duration=1, button='left')

# Example: Draw a square
pyautogui.moveTo(100, 100)
pyautogui.drag(100, 0, duration=0.5)    # Right
pyautogui.drag(0, 100, duration=0.5)    # Down
pyautogui.drag(-100, 0, duration=0.5)   # Left
pyautogui.drag(0, -100, duration=0.5)   # Up
```

### Scrolling

```python
# Scroll up (positive value) or down (negative value)
pyautogui.scroll(10)   # Scroll up 10 "clicks"
pyautogui.scroll(-10)  # Scroll down 10 "clicks"

# Scroll at specific position
pyautogui.scroll(5, x=500, y=500)

# Horizontal scrolling (if supported)
pyautogui.hscroll(10)  # Scroll right
pyautogui.hscroll(-10) # Scroll left
```

### Complete Mouse Example - Drawing Program

```python
import pyautogui
import time

# Wait for user to open Paint or drawing program
print("Open your drawing program and position the cursor...")
time.sleep(5)

# Get starting position
start_x, start_y = pyautogui.position()
print(f"Starting at: {start_x}, {start_y}")

# Draw a smiley face
# Draw circle (face)
pyautogui.moveTo(start_x, start_y)
for i in range(360):
    angle = i * 3.14159 / 180
    x = start_x + 50 * pyautogui.cos(angle)
    y = start_y + 50 * pyautogui.sin(angle)
    pyautogui.dragTo(x, y, duration=0.01)

time.sleep(0.5)

# Draw left eye
pyautogui.click(start_x - 15, start_y - 15)
pyautogui.drag(5, 0, duration=0.2)

# Draw right eye
pyautogui.click(start_x + 15, start_y - 15)
pyautogui.drag(5, 0, duration=0.2)

# Draw smile
pyautogui.moveTo(start_x - 20, start_y + 15)
for i in range(40):
    pyautogui.drag(1, 0.5, duration=0.01)
```

---

## 3. Keyboard Operations

### Typing Text

```python
# Type a string (simulates pressing keys one by one)
pyautogui.typewrite('Hello World!')

# Type with interval between keystrokes (0.1 seconds)
pyautogui.typewrite('Slow typing...', interval=0.1)

# For special characters and international text, use write()
pyautogui.write('Hello! This works with special chars: @#$%')
```

### Pressing Individual Keys

```python
# Press and release a single key
pyautogui.press('enter')
pyautogui.press('esc')
pyautogui.press('tab')
pyautogui.press('space')

# Press multiple keys in sequence
pyautogui.press(['tab', 'tab', 'enter'])
```

### Key Combinations (Hotkeys)

```python
# Press Ctrl+C (Copy)
pyautogui.hotkey('ctrl', 'c')

# Press Ctrl+V (Paste)
pyautogui.hotkey('ctrl', 'v')

# Press Ctrl+Alt+Delete
pyautogui.hotkey('ctrl', 'alt', 'delete')

# Press Ctrl+Shift+S (Save As)
pyautogui.hotkey('ctrl', 'shift', 's')

# Press Alt+Tab (Switch windows)
pyautogui.hotkey('alt', 'tab')

# Press Windows Key + D (Show desktop)
pyautogui.hotkey('win', 'd')
```

### Key Down and Key Up

```python
# Hold down a key
pyautogui.keyDown('shift')
pyautogui.press('a')  # Types 'A'
pyautogui.keyUp('shift')

# Hold multiple keys
pyautogui.keyDown('ctrl')
pyautogui.keyDown('shift')
pyautogui.press('esc')
pyautogui.keyUp('shift')
pyautogui.keyUp('ctrl')
```

### Available Key Names

```python
# Get list of all available key names
print(pyautogui.KEYBOARD_KEYS)

# Common key names:
# 'enter', 'esc', 'tab', 'space', 'backspace', 'delete'
# 'up', 'down', 'left', 'right'
# 'home', 'end', 'pageup', 'pagedown'
# 'f1' through 'f12'
# 'shift', 'ctrl', 'alt', 'win' (Windows key)
# 'a' through 'z', '0' through '9'
```

### Complete Keyboard Example - Text Editor Automation

```python
import pyautogui
import time

# Open Notepad (Windows example)
print("Opening Notepad...")
pyautogui.press('win')
time.sleep(0.5)
pyautogui.typewrite('notepad', interval=0.1)
pyautogui.press('enter')
time.sleep(2)

# Type some text
pyautogui.write('This is an automated message.')
pyautogui.press('enter')
pyautogui.press('enter')

# Type with formatting
pyautogui.write('Here are some bullet points:')
pyautogui.press('enter')
for i in range(3):
    pyautogui.write(f'- Point number {i+1}')
    pyautogui.press('enter')

# Select all text (Ctrl+A)
time.sleep(0.5)
pyautogui.hotkey('ctrl', 'a')

# Copy text (Ctrl+C)
time.sleep(0.2)
pyautogui.hotkey('ctrl', 'c')

# Move to end (Ctrl+End)
time.sleep(0.2)
pyautogui.hotkey('ctrl', 'end')
pyautogui.press('enter')
pyautogui.press('enter')

# Paste text (Ctrl+V)
pyautogui.write('Copied text:')
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 'v')
```

---

## 4. Image Recognition

PyAutoGUI can locate images on the screen using computer vision. This requires the **Pillow** library and **OpenCV**.

**Installation:**
```bash
pip install pillow opencv-python
```

### Locate Image on Screen

```python
import pyautogui

# Find the first occurrence of an image on screen
# Returns a Box object (left, top, width, height) or None if not found
try:
    location = pyautogui.locateOnScreen('button.png')
    if location:
        print(f"Image found at: {location}")
        # Output example: Image found at: Box(left=100, top=200, width=50, height=30)
    else:
        print("Image not found")
except pyautogui.ImageNotFoundException:
    print("Image not found on screen")
```

### Get Center Point of Located Image

```python
# Find image and get its center coordinates
try:
    location = pyautogui.locateOnScreen('button.png')
    if location:
        center_x, center_y = pyautogui.center(location)
        print(f"Image center: ({center_x}, {center_y})")
        
        # Click on the center of the image
        pyautogui.click(center_x, center_y)
except pyautogui.ImageNotFoundException:
    print("Image not found")
```

### Locate on Screen with Center (Shortcut)

```python
# Find image and get center in one step
try:
    x, y = pyautogui.locateCenterOnScreen('button.png')
    print(f"Found image center at: ({x}, {y})")
    pyautogui.click(x, y)
except pyautogui.ImageNotFoundException:
    print("Image not found")
```

### Locate All Occurrences of an Image

```python
# Find all instances of an image on screen
try:
    locations = list(pyautogui.locateAllOnScreen('icon.png'))
    print(f"Found {len(locations)} instances")
    
    for i, location in enumerate(locations):
        print(f"Instance {i+1}: {location}")
        x, y = pyautogui.center(location)
        # Do something with each instance
        
except pyautogui.ImageNotFoundException:
    print("Image not found")
```

### Confidence and Grayscale Parameters

```python
# Use confidence parameter for fuzzy matching (0.0 to 1.0)
# Requires OpenCV
try:
    location = pyautogui.locateOnScreen('button.png', confidence=0.8)
    # 0.8 = 80% match required
    if location:
        print(f"Found with 80% confidence: {location}")
except pyautogui.ImageNotFoundException:
    print("Image not found with 80% confidence")

# Use grayscale for faster searching
try:
    location = pyautogui.locateOnScreen('button.png', grayscale=True)
    if location:
        print(f"Found using grayscale: {location}")
except pyautogui.ImageNotFoundException:
    print("Image not found")
```

### Region-Based Search (Search in Specific Area)

```python
# Search only in a specific region of the screen
# region=(left, top, width, height)
try:
    location = pyautogui.locateOnScreen(
        'button.png',
        region=(0, 0, 500, 500),  # Search only in top-left 500x500 area
        confidence=0.9
    )
    if location:
        print(f"Found in region: {location}")
except pyautogui.ImageNotFoundException:
    print("Image not found in specified region")
```

### Screenshot and Image Operations

```python
# Take a screenshot of entire screen
screenshot = pyautogui.screenshot()
screenshot.save('full_screen.png')

# Take screenshot of specific region
region_screenshot = pyautogui.screenshot(region=(0, 0, 300, 400))
region_screenshot.save('region_screen.png')

# Get pixel color at specific position
pixel_color = pyautogui.pixel(100, 200)
print(f"RGB color at (100, 200): {pixel_color}")
# Output example: RGB color at (100, 200): (255, 255, 255)

# Check if pixel matches a specific color
matches = pyautogui.pixelMatchesColor(100, 200, (255, 255, 255))
print(f"Pixel matches white: {matches}")

# With tolerance (0-255, how much variation is acceptable)
matches = pyautogui.pixelMatchesColor(100, 200, (255, 255, 255), tolerance=10)
```

### Complete Image Recognition Example - Automated Button Clicking

```python
import pyautogui
import time

def click_button_by_image(image_path, max_attempts=5, wait_time=2):
    """
    Attempt to find and click a button by its image
    """
    for attempt in range(max_attempts):
        try:
            print(f"Attempt {attempt + 1}: Searching for {image_path}...")
            
            # Search for the button
            button_location = pyautogui.locateCenterOnScreen(
                image_path,
                confidence=0.8
            )
            
            if button_location:
                x, y = button_location
                print(f"Button found at ({x}, {y})")
                
                # Move to button and click
                pyautogui.moveTo(x, y, duration=0.5)
                time.sleep(0.2)
                pyautogui.click()
                print("Button clicked successfully!")
                return True
            else:
                print(f"Button not found, waiting {wait_time} seconds...")
                time.sleep(wait_time)
                
        except pyautogui.ImageNotFoundException:
            print(f"Image not found, waiting {wait_time} seconds...")
            time.sleep(wait_time)
    
    print(f"Failed to find button after {max_attempts} attempts")
    return False

# Usage example
click_button_by_image('submit_button.png')
```

### Wait for Image to Appear

```python
import pyautogui
import time

def wait_for_image(image_path, timeout=30, check_interval=1):
    """
    Wait for an image to appear on screen
    """
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)
            if location:
                print(f"Image appeared after {time.time() - start_time:.1f} seconds")
                return pyautogui.center(location)
        except pyautogui.ImageNotFoundException:
            pass
        
        time.sleep(check_interval)
    
    print(f"Image did not appear within {timeout} seconds")
    return None

# Usage
position = wait_for_image('loading_complete.png', timeout=60)
if position:
    pyautogui.click(position)
```

---

## Safety Features

### Fail-Safe

```python
# Move mouse to top-left corner to abort program
# Enabled by default
pyautogui.FAILSAFE = True

# Disable fail-safe (not recommended)
pyautogui.FAILSAFE = False
```

### Pause Between Actions

```python
# Add a pause after each PyAutoGUI call (in seconds)
pyautogui.PAUSE = 1  # 1 second pause

# Now each action will wait 1 second
pyautogui.click()    # Executes, then waits 1 second
pyautogui.press('a') # Executes, then waits 1 second
```

### Message Box Alerts

```python
# Show alert box
pyautogui.alert('This is an alert message!')

# Show confirm box (OK/Cancel)
result = pyautogui.confirm('Do you want to continue?')
print(result)  # 'OK' or 'Cancel'

# Show input box
answer = pyautogui.prompt('What is your name?')
print(f"User entered: {answer}")

# Show password input box
password = pyautogui.password('Enter password:')
```

---

## Best Practices and Tips

### 1. Add Delays
Always add small delays between actions to ensure the system can keep up:

```python
import time

pyautogui.click(100, 200)
time.sleep(0.5)  # Wait half a second
pyautogui.typewrite('Hello')
```

### 2. Use Try-Except Blocks
Wrap automation code in try-except to handle errors gracefully:

```python
try:
    pyautogui.click(button_location)
except Exception as e:
    print(f"Error occurred: {e}")
```

### 3. Verify Before Acting
Check if elements exist before interacting:

```python
location = pyautogui.locateOnScreen('button.png')
if location:
    pyautogui.click(pyautogui.center(location))
else:
    print("Button not found, skipping action")
```

### 4. Save Reference Images Properly
- Use high-quality PNG images
- Ensure images are taken at the same screen resolution
- Crop images to show only the unique part
- Avoid images with gradients or animations

### 5. Use Confidence Parameter
When using image recognition, adjust confidence based on need:

```python
# Strict matching (0.95-1.0)
pyautogui.locateOnScreen('button.png', confidence=0.95)

# Flexible matching (0.7-0.8)
pyautogui.locateOnScreen('button.png', confidence=0.75)
```

---

## Complete Example: Form Automation

```python
import pyautogui
import time

def fill_web_form():
    """
    Example: Automated form filling
    """
    # Safety: Give user time to switch to the form
    print("Switch to your form window...")
    time.sleep(3)
    
    # Click first field (using image recognition)
    try:
        first_field = pyautogui.locateCenterOnScreen('first_name_field.png')
        if first_field:
            pyautogui.click(first_field)
    except:
        # Fallback: Tab to first field
        pyautogui.press('tab')
    
    time.sleep(0.5)
    
    # Fill in name
    pyautogui.typewrite('John', interval=0.1)
    pyautogui.press('tab')
    
    # Fill in last name
    time.sleep(0.3)
    pyautogui.typewrite('Doe', interval=0.1)
    pyautogui.press('tab')
    
    # Fill in email
    time.sleep(0.3)
    pyautogui.typewrite('john.doe@example.com', interval=0.1)
    pyautogui.press('tab')
    
    # Select dropdown option (press down arrow 3 times)
    time.sleep(0.3)
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('enter')
    
    # Check a checkbox (using image recognition)
    try:
        checkbox = pyautogui.locateCenterOnScreen('checkbox.png', confidence=0.8)
        if checkbox:
            pyautogui.click(checkbox)
    except:
        print("Checkbox not found")
    
    time.sleep(0.5)
    
    # Click submit button
    try:
        submit_btn = pyautogui.locateCenterOnScreen('submit_button.png')
        if submit_btn:
            pyautogui.click(submit_btn)
            print("Form submitted successfully!")
    except:
        print("Submit button not found")

# Run the automation
if __name__ == "__main__":
    fill_web_form()
```

---

## Troubleshooting

### Image Not Found
- Verify the image file path is correct
- Check screen resolution matches the screenshot resolution
- Lower the confidence parameter
- Use grayscale=True for faster/more reliable matching
- Ensure the image is visible and not obscured

### Actions Too Fast
- Increase `pyautogui.PAUSE` value
- Add `time.sleep()` between actions
- Use `duration` parameter for mouse movements

### Coordinates Off-Screen
- Check screen resolution with `pyautogui.size()`
- Use `pyautogui.onScreen()` to verify coordinates
- Account for multiple monitors

### Special Characters Not Typing
- Use `pyautogui.write()` instead of `typewrite()`
- Consider using clipboard operations as alternative

---

## Summary

PyAutoGUI is a powerful tool for GUI automation that provides:
- **Screen coordinate detection** for precise positioning
- **Mouse operations** for clicking, dragging, and scrolling
- **Keyboard operations** for typing and hotkeys
- **Image recognition** for finding and interacting with screen elements

Remember to always test your automation scripts carefully and include appropriate error handling and delays!

---

## Module 2: Playwright

### What is Playwright?

`Playwright` is a modern Python library developed by **Microsoft** for **browser automation**. It supports Chromium, Firefox, and WebKit and is known for its speed, reliability, and support for modern web apps (SPAs, dynamic content, etc.).

### Installation

```bash
pip install playwright
playwright install  # Downloads browser binaries
```

### Key Features

- Supports multiple browsers (Chrome, Firefox, Safari)
- Handles async and sync APIs
- Auto-waits for elements (no manual `time.sleep` needed)
- Supports headless and headed mode
- Handles JavaScript-heavy pages, iframes, and file downloads

### Example: Take a Screenshot of a Website (Sync API)

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    
    page.goto("https://example.com")
    print(page.title())  # Output: Example Domain
    
    page.screenshot(path="example.png")
    browser.close()
```

### Example: Fill a Form and Submit

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # headless=False shows the browser
    page = browser.new_page()
    
    page.goto("https://www.google.com")
    
    # Type in the search box and submit
    page.fill("textarea[name='q']", "Python RPA Playwright")
    page.press("textarea[name='q']", "Enter")
    
    # Wait for results to load
    page.wait_for_load_state("networkidle")
    print("Search results loaded!")
    
    browser.close()
```

### When to Use Playwright

Use Playwright when automating **modern web applications**, especially those with dynamic content, JavaScript rendering, or when you need fast and reliable test automation.


## 1. Browser Context

A **Browser Context** is an isolated, incognito-like session within a browser instance. Each context has its own cookies, cache, and local storage. This is perfect for testing multiple user sessions simultaneously or testing in isolation.

### Why Use Browser Contexts?

- **Isolation**: Each context is independent (separate cookies, storage, cache)
- **Efficiency**: Faster than launching multiple browser instances
- **Parallel Testing**: Run multiple test scenarios simultaneously
- **User Simulation**: Simulate different users in the same browser

### Creating a Browser Context (Sync API)

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch browser
    browser = p.chromium.launch(headless=False)
    
    # Create a new browser context
    context = browser.new_context()
    
    # Create a page in this context
    page = context.new_page()
    page.goto('https://example.com')
    
    # Close context
    context.close()
    browser.close()
```

### Multiple Browser Contexts

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    
    # Create first context (User 1)
    context1 = browser.new_context()
    page1 = context1.new_page()
    page1.goto('https://example.com')
    page1.fill('input[name="username"]', 'user1')
    
    # Create second context (User 2)
    context2 = browser.new_context()
    page2 = context2.new_page()
    page2.goto('https://example.com')
    page2.fill('input[name="username"]', 'user2')
    
    # Both users are logged in separately in the same browser
    print(f"User 1 is on: {page1.url}")
    print(f"User 2 is on: {page2.url}")
    
    # Cleanup
    context1.close()
    context2.close()
    browser.close()
```

### Browser Context Options

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    
    # Create context with custom options
    context = browser.new_context(
        viewport={'width': 1920, 'height': 1080},
        user_agent='Custom User Agent String',
        locale='en-US',
        timezone_id='America/New_York',
        permissions=['geolocation'],
        geolocation={'latitude': 40.7128, 'longitude': -74.0060},
        color_scheme='dark',  # 'light', 'dark', or 'no-preference'
        device_scale_factor=2,
        has_touch=True,
        is_mobile=False,
        ignore_https_errors=True,
        accept_downloads=True
    )
    
    page = context.new_page()
    page.goto('https://example.com')
    
    context.close()
    browser.close()
```

### Mobile Emulation with Context

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    
    # Emulate iPhone 12
    iphone_12 = p.devices['iPhone 12']
    context = browser.new_context(**iphone_12)
    
    page = context.new_page()
    page.goto('https://example.com')
    
    # Take screenshot
    page.screenshot(path='mobile_view.png')
    
    context.close()
    browser.close()
```

### Available Device Descriptors

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # List all available devices
    print("Available devices:")
    for device_name in p.devices:
        print(f"  - {device_name}")
    
    # Common devices:
    # 'iPhone 12', 'iPhone 13', 'iPhone 13 Pro', 'iPhone 14'
    # 'Pixel 5', 'Galaxy S9+', 'Galaxy S21'
    # 'iPad Pro', 'iPad Mini'
    # 'Desktop Chrome', 'Desktop Firefox', 'Desktop Safari'
```

### Authentication and Cookies in Context

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    
    # Create context with HTTP authentication
    context = browser.new_context(
        http_credentials={
            'username': 'admin',
            'password': 'secret123'
        }
    )
    
    page = context.new_page()
    page.goto('https://example.com/admin')
    
    # Add cookies to context
    context.add_cookies([
        {
            'name': 'session_id',
            'value': 'abc123xyz',
            'domain': 'example.com',
            'path': '/'
        }
    ])
    
    # Get cookies from context
    cookies = context.cookies()
    print(f"Current cookies: {cookies}")
    
    # Clear cookies
    context.clear_cookies()
    
    context.close()
    browser.close()
```

### Persistent Context (Save Session)

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch persistent context (saves user data)
    context = p.chromium.launch_persistent_context(
        user_data_dir='./user_data',  # Directory to save session data
        headless=False,
        viewport={'width': 1920, 'height': 1080}
    )
    
    page = context.pages[0]  # Use existing page
    page.goto('https://example.com')
    
    # Login and session will be saved
    # Next time, user will be logged in automatically
    
    context.close()
```

### Context Events and Tracing

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context()
    
    # Start tracing (for debugging)
    context.tracing.start(screenshots=True, snapshots=True)
    
    # Listen to context events
    context.on('page', lambda page: print(f'New page created: {page.url}'))
    context.on('close', lambda: print('Context closed'))
    
    page = context.new_page()
    page.goto('https://example.com')
    
    # Stop tracing and save
    context.tracing.stop(path='trace.zip')
    
    context.close()
    browser.close()
```

### Complete Example: Multiple User Sessions

```python
from playwright.sync_api import sync_playwright
import time

def simulate_user(context, username, user_num):
    """Simulate a user session in a separate context"""
    page = context.new_page()
    page.goto('https://example.com/login')
    
    # Login
    page.fill('input[name="username"]', username)
    page.fill('input[name="password"]', 'password123')
    page.click('button[type="submit"]')
    
    # Navigate to dashboard
    page.wait_for_url('**/dashboard')
    print(f"User {user_num} ({username}) logged in successfully")
    
    # Perform some actions
    page.click('a[href="/profile"]')
    time.sleep(2)
    
    return page

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    
    # Simulate 3 different users
    users = ['alice', 'bob', 'charlie']
    contexts = []
    pages = []
    
    for i, username in enumerate(users, 1):
        # Create isolated context for each user
        context = browser.new_context(
            viewport={'width': 1280, 'height': 720}
        )
        contexts.append(context)
        
        # Simulate user session
        page = simulate_user(context, username, i)
        pages.append(page)
    
    # All users are now logged in simultaneously
    print(f"\n{len(users)} users are active in separate contexts")
    input("Press Enter to close all sessions...")
    
    # Cleanup
    for context in contexts:
        context.close()
    browser.close()
```

---

## 2. Pages

A **Page** represents a single tab or window in the browser context. Pages are where you interact with web content.

### Creating and Managing Pages

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    
    # Create a new page
    page = context.new_page()
    
    # Navigate to URL
    page.goto('https://example.com')
    
    # Get page title
    title = page.title()
    print(f"Page title: {title}")
    
    # Get page URL
    url = page.url
    print(f"Current URL: {url}")
    
    # Close page
    page.close()
    
    context.close()
    browser.close()
```

### Multiple Pages (Tabs)

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    
    # Create multiple pages (tabs)
    page1 = context.new_page()
    page1.goto('https://google.com')
    
    page2 = context.new_page()
    page2.goto('https://github.com')
    
    page3 = context.new_page()
    page3.goto('https://stackoverflow.com')
    
    # Get all pages in context
    all_pages = context.pages
    print(f"Total pages: {len(all_pages)}")
    
    # Switch between pages
    page1.bring_to_front()
    page1.fill('input[name="q"]', 'Playwright')
    
    page2.bring_to_front()
    print(f"Page 2 title: {page2.title()}")
    
    # Close specific page
    page2.close()
    
    context.close()
    browser.close()
```

### Page Navigation

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    # Navigate to URL
    page.goto('https://example.com')
    
    # Navigate and wait for specific state
    page.goto('https://example.com', wait_until='networkidle')
    # Options: 'load', 'domcontentloaded', 'networkidle'
    
    # Navigate with timeout
    page.goto('https://example.com', timeout=30000)  # 30 seconds
    
    # Navigate back
    page.go_back()
    
    # Navigate forward
    page.go_forward()
    
    # Reload page
    page.reload()
    
    # Wait for navigation
    with page.expect_navigation():
        page.click('a[href="/next-page"]')
    
    browser.close()
```

### Page Content and Evaluation

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('https://example.com')
    
    # Get page content (HTML)
    content = page.content()
    print(f"HTML length: {len(content)}")
    
    # Set content directly
    page.set_content('<h1>Hello World</h1><p>This is a test</p>')
    
    # Evaluate JavaScript
    result = page.evaluate('() => document.title')
    print(f"Title via JS: {result}")
    
    # Evaluate with arguments
    result = page.evaluate('(x, y) => x + y', 5, 10)
    print(f"5 + 10 = {result}")
    
    # Execute complex JavaScript
    dimensions = page.evaluate('''() => {
        return {
            width: document.documentElement.clientWidth,
            height: document.documentElement.clientHeight,
            devicePixelRatio: window.devicePixelRatio
        }
    }''')
    print(f"Page dimensions: {dimensions}")
    
    browser.close()
```

### Page Screenshots and PDFs

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('https://example.com')
    
    # Take full page screenshot
    page.screenshot(path='screenshot_full.png', full_page=True)
    
    # Take viewport screenshot
    page.screenshot(path='screenshot_viewport.png')
    
    # Screenshot with options
    page.screenshot(
        path='screenshot_custom.png',
        type='png',  # 'png' or 'jpeg'
        quality=80,  # For JPEG only (0-100)
        full_page=False,
        clip={'x': 0, 'y': 0, 'width': 800, 'height': 600}
    )
    
    # Screenshot as bytes
    screenshot_bytes = page.screenshot()
    
    # Generate PDF (Chromium only)
    page.pdf(
        path='page.pdf',
        format='A4',
        print_background=True,
        margin={'top': '1cm', 'right': '1cm', 'bottom': '1cm', 'left': '1cm'}
    )
    
    browser.close()
```

### Page Events and Listeners

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    
    # Listen to console messages
    page.on('console', lambda msg: print(f'Console [{msg.type}]: {msg.text}'))
    
    # Listen to page errors
    page.on('pageerror', lambda err: print(f'Page error: {err}'))
    
    # Listen to requests
    page.on('request', lambda req: print(f'Request: {req.method} {req.url}'))
    
    # Listen to responses
    page.on('response', lambda res: print(f'Response: {res.status} {res.url}'))
    
    # Listen to dialogs (alert, confirm, prompt)
    page.on('dialog', lambda dialog: dialog.accept())
    
    # Listen to downloads
    def handle_download(download):
        print(f'Download started: {download.suggested_filename}')
        download.save_as(f'./downloads/{download.suggested_filename}')
    
    page.on('download', handle_download)
    
    # Listen to popup (new window/tab)
    def handle_popup(popup):
        print(f'Popup opened: {popup.url}')
        popup.close()
    
    page.on('popup', handle_popup)
    
    page.goto('https://example.com')
    
    browser.close()
```

### Page Viewport and Emulation

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    
    # Set viewport size
    page.set_viewport_size(width=1920, height=1080)
    
    # Get viewport size
    viewport = page.viewport_size
    print(f"Viewport: {viewport['width']}x{viewport['height']}")
    
    # Emulate media (CSS media queries)
    page.emulate_media(media='print')  # 'screen' or 'print'
    
    # Emulate color scheme
    page.emulate_media(color_scheme='dark')  # 'light', 'dark', 'no-preference'
    
    # Emulate geolocation
    context = page.context
    context.set_geolocation(latitude=40.7128, longitude=-74.0060)
    context.grant_permissions(['geolocation'])
    
    page.goto('https://example.com')
    
    browser.close()
```

### Page Waiting Methods

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('https://example.com')
    
    # Wait for selector
    page.wait_for_selector('h1')
    
    # Wait for selector with state
    page.wait_for_selector('button', state='visible')
    # States: 'attached', 'detached', 'visible', 'hidden'
    
    # Wait for URL
    page.wait_for_url('**/dashboard')
    
    # Wait for load state
    page.wait_for_load_state('networkidle')
    # States: 'load', 'domcontentloaded', 'networkidle'
    
    # Wait for timeout
    page.wait_for_timeout(3000)  # Wait 3 seconds
    
    # Wait for function
    page.wait_for_function('() => document.readyState === "complete"')
    
    # Wait for custom condition
    page.wait_for_function('() => document.querySelectorAll(".item").length > 5')
    
    browser.close()
```

### Complete Example: Multi-Page Scraping

```python
from playwright.sync_api import sync_playwright
import json

def scrape_page(page, url):
    """Scrape data from a single page"""
    page.goto(url)
    page.wait_for_load_state('networkidle')
    
    # Extract data
    data = page.evaluate('''() => {
        const items = [];
        document.querySelectorAll('.product').forEach(product => {
            items.push({
                title: product.querySelector('h2')?.textContent,
                price: product.querySelector('.price')?.textContent,
                rating: product.querySelector('.rating')?.textContent
            });
        });
        return items;
    }''')
    
    return data

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    
    # URLs to scrape
    urls = [
        'https://example.com/category1',
        'https://example.com/category2',
        'https://example.com/category3'
    ]
    
    all_data = []
    
    # Create a page for each URL
    for i, url in enumerate(urls, 1):
        print(f"Scraping page {i}/{len(urls)}: {url}")
        page = context.new_page()
        data = scrape_page(page, url)
        all_data.extend(data)
        page.close()
    
    # Save results
    with open('scraped_data.json', 'w') as f:
        json.dump(all_data, f, indent=2)
    
    print(f"Total items scraped: {len(all_data)}")
    
    context.close()
    browser.close()
```

---

## 3. Selectors

Playwright supports multiple selector engines (CSS, XPath, Text, etc) to locate elements on a page.

### CSS Selectors

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('https://example.com')
    
    # Basic CSS selectors
    page.click('button')                    # Tag name
    page.click('#submit-btn')               # ID
    page.click('.btn-primary')              # Class
    page.click('button.btn-primary')        # Tag + class
    page.click('div > button')              # Direct child
    page.click('div button')                # Descendant
    page.click('button[type="submit"]')     # Attribute
    page.click('button[data-id="123"]')     # Data attribute
    
    # Advanced CSS selectors
    page.click('button:nth-child(2)')       # nth-child
    page.click('input:first-of-type')       # First of type
    page.click('button:last-child')         # Last child
    page.click('div:not(.disabled)')        # Not selector
    page.click('input[type="text"]:focus')  # Pseudo-class
    
    # Multiple selectors (OR)
    page.click('button.submit, button.send, input[type="submit"]')
    
    browser.close()
```

### XPath Selectors

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('https://example.com')
    
    # XPath selectors (use xpath= prefix)
    page.click('xpath=//button')                          # Basic XPath
    page.click('xpath=//button[@id="submit"]')            # Attribute
    page.click('xpath=//button[@class="btn-primary"]')    # Class attribute
    page.click('xpath=//div[@data-testid="container"]//button')  # Nested
    
    # XPath text matching
    page.click('xpath=//button[text()="Submit"]')         # Exact text
    page.click('xpath=//button[contains(text(), "Submit")]')  # Contains text
    page.click('xpath=//button[starts-with(text(), "Sub")]')  # Starts with
    
    # XPath axes
    page.click('xpath=//button/following-sibling::a')     # Following sibling
    page.click('xpath=//button/parent::div')              # Parent
    page.click('xpath=//button/ancestor::form')           # Ancestor
    
    # XPath predicates
    page.click('xpath=(//button)[1]')                     # First button
    page.click('xpath=(//button)[last()]')                # Last button
    page.click('xpath=//button[@type="submit"][1]')       # First submit button
    
    browser.close()
```

### Text Selectors

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('https://example.com')
    
    # Text selectors (use text= prefix)
    page.click('text=Submit')                    # Exact text match
    page.click('text="Submit Form"')             # Exact text with spaces
    
    # Case-insensitive text matching
    page.click('text=/submit/i')                 # Regex, case-insensitive
    
    # Partial text matching
    page.click('text=Sub')                       # Substring match
    
    # Text with regex
    page.click('text=/^Submit.*/')               # Starts with "Submit"
    page.click('text=/.*button$/i')              # Ends with "button"
    
    browser.close()
```

### Role Selectors (Accessible)

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('https://example.com')
    
    # Role-based selectors (accessible)
    page.click('role=button')                              # Any button
    page.click('role=button[name="Submit"]')               # Button with name
    page.click('role=textbox[name="Username"]')            # Textbox
    page.click('role=link[name="Home"]')                   # Link
    page.click('role=checkbox[name="Accept"]')             # Checkbox
    
    # Common roles:
    # button, link, textbox, checkbox, radio, combobox, 
    # listbox, menuitem, tab, heading, img, table, row, cell
    
    # Role with additional attributes
    page.click('role=button[name="Submit"][disabled=false]')
    page.click('role=textbox[name=/email/i]')  # Case-insensitive regex
    
    browser.close()
```

### Data-testid Selectors

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('https://example.com')
    
    # Using data-testid (common in React/Vue apps)
    page.click('[data-testid="submit-button"]')
    page.fill('[data-testid="username-input"]', 'john_doe')
    page.click('[data-testid="login-form"] button')
    
    # Using data-cy (Cypress convention)
    page.click('[data-cy="submit-btn"]')
    
    # Using data-qa (QA convention)
    page.click('[data-qa="submit"]')
    
    browser.close()
```

### Chaining Selectors

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('https://example.com')
    
    # Chain CSS selectors with >>
    page.click('div.container >> button.submit')
    
    # Chain different selector types
    page.click('css=div.form >> text=Submit')
    page.click('xpath=//div[@class="modal"] >> css=button.close')
    
    # Complex chaining
    page.click('div#main >> ul.menu >> li:nth-child(2) >> a')
    
    browser.close()
```

### Getting Multiple Elements

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('https://example.com')
    
    # Get all matching elements
    buttons = page.locator('button').all()
    print(f"Found {len(buttons)} buttons")
    
    # Iterate through elements
    links = page.locator('a').all()
    for link in links:
        href = link.get_attribute('href')
        text = link.text_content()
        print(f"Link: {text} -> {href}")
    
    # Get element count
    count = page.locator('button').count()
    print(f"Total buttons: {count}")
    
    # Get nth element
    first_button = page.locator('button').nth(0)
    second_button = page.locator('button').nth(1)
    last_button = page.locator('button').nth(-1)
    
    browser.close()
```

### Locator Methods

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('https://example.com')
    
    # Create locator
    submit_button = page.locator('button[type="submit"]')
    
    # Click locator
    submit_button.click()
    
    # Get text content
    text = submit_button.text_content()
    print(f"Button text: {text}")
    
    # Get inner text
    inner_text = submit_button.inner_text()
    
    # Get inner HTML
    html = submit_button.inner_html()
    
    # Get attribute
    button_id = submit_button.get_attribute('id')
    data_value = submit_button.get_attribute('data-value')
    
    # Check visibility
    is_visible = submit_button.is_visible()
    is_hidden = submit_button.is_hidden()
    
    # Check state
    is_enabled = submit_button.is_enabled()
    is_disabled = submit_button.is_disabled()
    is_checked = submit_button.is_checked()  # For checkboxes/radios
    
    # Wait for locator
    submit_button.wait_for(state='visible')
    submit_button.wait_for(state='hidden')
    
    browser.close()
```

### Filtering Locators

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('https://example.com')
    
    # Filter by text
    submit_btn = page.locator('button').filter(has_text='Submit')
    submit_btn.click()
    
    # Filter by regex
    email_input = page.locator('input').filter(has_text=r'.*email.*')
    
    # Filter by child element
    form = page.locator('form').filter(has=page.locator('button[type="submit"]'))
    
    # Filter by NOT
    active_items = page.locator('.item').filter(has_not=page.locator('.disabled'))
    
    # Combine filters
    specific_button = page.locator('button').filter(
        has_text='Submit'
    ).filter(
        has_not=page.locator('.disabled')
    )
    
    browser.close()
```

### Complete Selector Example

```python
from playwright.sync_api import sync_playwright

def test_login_with_different_selectors(page):
    """Demonstrate different ways to select the same elements"""
    
    # Username field - Multiple approaches
    # Approach 1: CSS ID
    page.fill('#username', 'john_doe')
    
    # Approach 2: CSS attribute
    page.fill('input[name="username"]', 'john_doe')
    
    # Approach 3: CSS class
    page.fill('input.username-field', 'john_doe')
    
    # Approach 4: XPath
    page.fill('xpath=//input[@name="username"]', 'john_doe')
    
    # Approach 5: Data attribute
    page.fill('[data-testid="username-input"]', 'john_doe')
    
    # Approach 6: Role (accessible)
    page.fill('role=textbox[name="Username"]', 'john_doe')
    
    # Password field
    page.fill('input[type="password"]', 'SecurePass123')
    
    # Submit button - Multiple approaches
    # Approach 1: CSS ID
    page.click('#submit-btn')
    
    # Approach 2: Text content
    page.click('text=Login')
    
    # Approach 3: Role
    page.click('role=button[name="Login"]')
    
    # Approach 4: XPath with text
    page.click('xpath=//button[contains(text(), "Login")]')

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('https://example.com/login')
    
    test_login_with_different_selectors(page)
    
    browser.close()
```

---

## 4. Async

Playwright supports both **synchronous** and **asynchronous** APIs. The async API is useful for concurrent operations and integrates well with modern Python async frameworks.

### Why Use Async?

- **Better Performance**: Run multiple operations concurrently
- **Non-blocking**: Don't wait for slow operations
- **Scalability**: Handle multiple browsers/pages simultaneously
- **Integration**: Works with async frameworks (FastAPI, aiohttp, etc.)

### Basic Async Example

```python
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('https://example.com')
        
        title = await page.title()
        print(f"Page title: {title}")
        
        await browser.close()

# Run async function
asyncio.run(main())
```

### Async vs Sync Comparison

```python
# SYNCHRONOUS (Blocking)
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('https://example.com')
    page.click('button')
    browser.close()

# ASYNCHRONOUS (Non-blocking)
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('https://example.com')
        await page.click('button')
        await browser.close()

asyncio.run(main())
```

### Concurrent Page Operations

```python
import asyncio
from playwright.async_api import async_playwright

async def scrape_page(page, url):
    """Scrape a single page"""
    await page.goto(url)
    title = await page.title()
    content = await page.content()
    return {'url': url, 'title': title, 'length': len(content)}

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        
        # Create multiple pages
        page1 = await browser.new_page()
        page2 = await browser.new_page()
        page3 = await browser.new_page()
        
        # Scrape concurrently (all at once)
        results = await asyncio.gather(
            scrape_page(page1, 'https://example.com'),
            scrape_page(page2, 'https://github.com'),
            scrape_page(page3, 'https://stackoverflow.com')
        )
        
        for result in results:
            print(f"{result['url']}: {result['title']} ({result['length']} bytes)")
        
        await browser.close()

asyncio.run(main())
```

### Async with Multiple Browsers

```python
import asyncio
from playwright.async_api import async_playwright

async def test_in_browser(browser_type, url):
    """Run test in specific browser"""
    async with async_playwright() as p:
        if browser_type == 'chromium':
            browser = await p.chromium.launch()
        elif browser_type == 'firefox':
            browser = await p.firefox.launch()
        elif browser_type == 'webkit':
            browser = await p.webkit.launch()
        
        page = await browser.new_page()
        await page.goto(url)
        
        title = await page.title()
        print(f"{browser_type}: {title}")
        
        await browser.close()
        return browser_type

async def main():
    # Test in all browsers concurrently
    results = await asyncio.gather(
        test_in_browser('chromium', 'https://example.com'),
        test_in_browser('firefox', 'https://example.com'),
        test_in_browser('webkit', 'https://example.com')
    )
    print(f"Tested in: {results}")

asyncio.run(main())
```

### Async Error Handling

```python
import asyncio
from playwright.async_api import async_playwright, TimeoutError

async def safe_navigation(page, url):
    """Navigate with error handling"""
    try:
        await page.goto(url, timeout=5000)
        print(f"Successfully loaded: {url}")
    except TimeoutError:
        print(f"Timeout loading: {url}")
    except Exception as e:
        print(f"Error loading {url}: {e}")

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        # Try loading multiple URLs
        urls = [
            'https://example.com',
            'https://invalid-domain-xyz123.com',
            'https://github.com'
        ]
        
        for url in urls:
            await safe_navigation(page, url)
        
        await browser.close()

asyncio.run(main())
```

### Async with Context Manager

```python
import asyncio
from playwright.async_api import async_playwright

class BrowserManager:
    """Context manager for browser"""
    def __init__(self, playwright):
        self.playwright = playwright
        self.browser = None
    
    async def __aenter__(self):
        self.browser = await self.playwright.chromium.launch()
        return self.browser
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.browser:
            await self.browser.close()

async def main():
    async with async_playwright() as p:
        async with BrowserManager(p) as browser:
            page = await browser.new_page()
            await page.goto('https://example.com')
            print(f"Title: {await page.title()}")
            # Browser automatically closes after this block

asyncio.run(main())
```

### Async Tasks and Scheduling

```python
import asyncio
from playwright.async_api import async_playwright

async def monitor_page(page, interval=5):
    """Monitor page changes every N seconds"""
    while True:
        title = await page.title()
        url = page.url
        print(f"[{asyncio.get_event_loop().time():.0f}s] {title} - {url}")
        await asyncio.sleep(interval)

async def interact_with_page(page):
    """Interact with page while monitoring"""
    await page.goto('https://example.com')
    await asyncio.sleep(3)
    
    await page.click('a')
    await asyncio.sleep(3)
    
    await page.go_back()
    await asyncio.sleep(3)

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        
        # Run monitor and interactions concurrently
        monitor_task = asyncio.create_task(monitor_page(page, interval=2))
        
        try:
            await interact_with_page(page)
        finally:
            monitor_task.cancel()
        
        await browser.close()

asyncio.run(main())
```

### Async Waiting Operations

```python
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('https://example.com')
        
        # Wait for selector (async)
        await page.wait_for_selector('h1')
        
        # Wait for multiple conditions concurrently
        await asyncio.gather(
            page.wait_for_selector('.content'),
            page.wait_for_load_state('networkidle'),
            page.wait_for_function('() => document.readyState === "complete"')
        )
        
        # Wait with timeout
        try:
            await asyncio.wait_for(
                page.wait_for_selector('.slow-element'),
                timeout=5.0
            )
        except asyncio.TimeoutError:
            print("Element did not appear in 5 seconds")
        
        # Wait for any of multiple conditions (first to complete)
        done, pending = await asyncio.wait(
            [
                asyncio.create_task(page.wait_for_selector('.option1')),
                asyncio.create_task(page.wait_for_selector('.option2')),
                asyncio.create_task(page.wait_for_selector('.option3'))
            ],
            return_when=asyncio.FIRST_COMPLETED
        )
        
        # Cancel pending tasks
        for task in pending:
            task.cancel()
        
        await browser.close()

asyncio.run(main())
```

### Complete Async Example: Concurrent Web Scraping

```python
import asyncio
import json
from playwright.async_api import async_playwright

async def scrape_product(page, url):
    """Scrape a single product page"""
    try:
        await page.goto(url, wait_until='networkidle')
        
        # Extract product data
        data = await page.evaluate('''() => {
            return {
                title: document.querySelector('h1')?.textContent,
                price: document.querySelector('.price')?.textContent,
                description: document.querySelector('.description')?.textContent,
                rating: document.querySelector('.rating')?.textContent,
                availability: document.querySelector('.stock')?.textContent
            };
        }''')
        
        data['url'] = url
        print(f"✓ Scraped: {data['title']}")
        return data
        
    except Exception as e:
        print(f"✗ Error scraping {url}: {e}")
        return None

async def scrape_category(context, category_url, max_products=10):
    """Scrape all products from a category"""
    page = await context.new_page()
    await page.goto(category_url)
    
    # Get product links
    product_links = await page.evaluate(f'''() => {{
        const links = Array.from(document.querySelectorAll('.product-link'));
        return links.slice(0, {max_products}).map(a => a.href);
    }}''')
    
    print(f"Found {len(product_links)} products in {category_url}")
    
    # Create tasks for concurrent scraping
    tasks = []
    for link in product_links:
        product_page = await context.new_page()
        task = asyncio.create_task(scrape_product(product_page, link))
        tasks.append(task)
    
    # Wait for all scraping to complete
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    # Filter out None and exceptions
    valid_results = [r for r in results if r and not isinstance(r, Exception)]
    
    await page.close()
    return valid_results

async def main():
    async with async_playwright() as p:
        # Launch browser
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        
        # Categories to scrape
        categories = [
            'https://example.com/electronics',
            'https://example.com/books',
            'https://example.com/clothing'
        ]
        
        # Scrape all categories concurrently
        all_results = []
        
        category_tasks = [
            scrape_category(context, cat_url, max_products=5)
            for cat_url in categories
        ]
        
        category_results = await asyncio.gather(*category_tasks)
        
        # Flatten results
        for results in category_results:
            all_results.extend(results)
        
        # Save to file
        with open('products.json', 'w') as f:
            json.dump(all_results, f, indent=2)
        
        print(f"\n✓ Total products scraped: {len(all_results)}")
        print(f"✓ Saved to products.json")
        
        await context.close()
        await browser.close()

# Run the scraper
if __name__ == '__main__':
    asyncio.run(main())
```

### Async with Rate Limiting

```python
import asyncio
from playwright.async_api import async_playwright

class RateLimiter:
    """Simple rate limiter for async operations"""
    def __init__(self, rate, per):
        self.rate = rate  # Number of operations
        self.per = per    # Per time period (seconds)
        self.allowance = rate
        self.last_check = asyncio.get_event_loop().time()
    
    async def acquire(self):
        current = asyncio.get_event_loop().time()
        time_passed = current - self.last_check
        self.last_check = current
        self.allowance += time_passed * (self.rate / self.per)
        
        if self.allowance > self.rate:
            self.allowance = self.rate
        
        if self.allowance < 1.0:
            sleep_time = (1.0 - self.allowance) * (self.per / self.rate)
            await asyncio.sleep(sleep_time)
            self.allowance = 0.0
        else:
            self.allowance -= 1.0

async def scrape_with_rate_limit(page, url, limiter):
    """Scrape with rate limiting"""
    await limiter.acquire()
    await page.goto(url)
    title = await page.title()
    print(f"Scraped: {title}")
    return title

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        # Rate limiter: 2 requests per second
        limiter = RateLimiter(rate=2, per=1.0)
        
        urls = [f'https://example.com/page{i}' for i in range(10)]
        
        tasks = [
            scrape_with_rate_limit(page, url, limiter)
            for url in urls
        ]
        
        await asyncio.gather(*tasks)
        
        await browser.close()

asyncio.run(main())
```

---

## Best Practices

### 1. Use Appropriate Selectors
```python
# Prefer stable selectors
# ✓ Good: Data attributes
page.click('[data-testid="submit-btn"]')

# ✓ Good: Role-based (accessible)
page.click('role=button[name="Submit"]')

# ✗ Bad: Fragile class names
page.click('.MuiButton-root-123')
```

### 2. Always Use Explicit Waits
```python
# ✓ Good: Wait for element
await page.wait_for_selector('button')
await page.click('button')

# ✗ Bad: No waiting
await page.click('button')  # May fail if button not ready
```

### 3. Use Async for Concurrent Operations
```python
# ✓ Good: Concurrent operations
results = await asyncio.gather(
    scrape_page(page1, url1),
    scrape_page(page2, url2),
    scrape_page(page3, url3)
)

# ✗ Bad: Sequential operations
result1 = await scrape_page(page1, url1)
result2 = await scrape_page(page2, url2)
result3 = await scrape_page(page3, url3)
```

### 4. Use Browser Context for Isolation
```python
# ✓ Good: Isolated contexts
context1 = await browser.new_context()
context2 = await browser.new_context()

# ✗ Bad: Shared state
page1 = await browser.new_page()
page2 = await browser.new_page()  # Shares cookies/storage
```

---

## Summary

Playwright provides a powerful and modern approach to browser automation:

- **Browser Context**: Isolated sessions for parallel testing and user simulation
- **Pages**: Individual tabs/windows for interaction with web content
- **Selectors**: Multiple strategies (CSS, XPath, text, role) for locating elements
- **Async/Await**: Efficient concurrent operations for better performance

The combination of these features makes Playwright ideal for web scraping, testing, and automation tasks.

---

## Module 3: Selenium

### What is Selenium?

`Selenium` is one of the **oldest and most widely used** web automation frameworks. It allows you to control a web browser programmatically using Python (and other languages). It works with Chrome, Firefox, Edge, and Safari via WebDriver.

### Installation

```bash
pip install selenium
```

You also need the appropriate **WebDriver** for your browser. With Selenium 4+, you can use `webdriver-manager`:

```bash
pip install webdriver-manager
```

### Key Features

- Cross-browser support
- Large community and documentation
- Integration with test frameworks (pytest, unittest)
- Support for waits (implicit, explicit, fluent)
- Works with legacy and modern web apps

### Example: Open a Browser and Search Google

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open Google
driver.get("https://www.google.com")
print("Title:", driver.title)

# Find the search box, type a query, and press Enter
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Python RPA Selenium")
search_box.send_keys(Keys.RETURN)

time.sleep(3)  # Wait for results

print("Current URL:", driver.current_url)
driver.quit()
```

### Example: Login Automation

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://example-login-site.com/login")

# Fill in login form
driver.find_element(By.ID, "username").send_keys("my_username")
driver.find_element(By.ID, "password").send_keys("my_password")
driver.find_element(By.ID, "login-button").click()

print("Login attempted!")
driver.quit()
```

### When to Use Selenium

Use Selenium when working with **web automation and testing** on well-established websites, especially in enterprise environments or when you need broad browser compatibility.

---

## Comparison Summary

| Feature            | PyAutoGUI        | Playwright              | Selenium               |
|--------------------|------------------|--------------------------|------------------------|
| Target             | Desktop GUI      | Web browsers             | Web browsers           |
| Speed              | Moderate         | Fast                     | Moderate               |
| Auto-wait          | No               | Yes                      | Manual (explicit wait) |
| Browser Support    | N/A              | Chrome, Firefox, WebKit  | Chrome, Firefox, Edge  |
| JS-heavy pages     | N/A              | Excellent                | Good                   |
| Ease of Use        | Easy             | Moderate                 | Moderate               |
| Best For           | Desktop apps     | Modern web apps          | Web testing & scraping |

---

## Summary

- **PyAutoGUI** → Automate desktop GUIs (mouse, keyboard, screen)
- **Playwright** → Automate modern web apps with speed and reliability
- **Selenium** → Automate and test web browsers across different environments

Together, these three libraries cover a wide range of RPA use cases in Python, from desktop automation to complex web workflows.
