# Week 1 -> Day 4 -> RPA with Python  

## Table of Contents

*   [Create a RPA Python App with Virtual Environment](#create-a-rpa-python-app-with-virtual-environment)
*   [Python RPA: Robotic Process Automation](#python-rpa-robotic-process-automation)
    *   [Module 1: PyAutoGUI](#module-1-pyautogui)
        *   [PyAutoGUI Core Operations](#pyautogui-core-operations)
            *   [1. Get Screen Coordinates](#1-get-screen-coordinates)
            *   [2. Mouse Operations](#2-mouse-operations)
            *   [3. Keyboard Operations](#3-keyboard-operations)
            *   [4. Image Recognition](#4-image-recognition)
    *   [Module 2: Playwright](#module-2-playwright)
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
