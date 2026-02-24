

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
