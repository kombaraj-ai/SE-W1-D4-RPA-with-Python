# 🚀 Quick Start Guide

Follow these steps to get started with the PyAutoGUI RPA Form Automation project.

---

### Step 1: Go to the Assignment 1 folder
```bash
cd Assignment1_pyAutoGUI
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Application
```bash
python form_filler.py
```

### Step 4: Choose Option
- **Option 1**: See basic demo (recommended for first time)
- **Option 2**: Run form automation
- **Option 3**: View screen information

---

## 🎯 First Run - Demo Mode

### Step 1: Start the Application
```bash
python form_filler.py
```

### Step 2: Select Option 1
```
Enter your choice (1-3): 1
```

### Step 3: Watch the Demo
The demo will:
1. Display your screen information
2. Move the mouse to screen center
3. Open Notepad automatically
4. Type sample text
5. Close Notepad

**What to Learn:**
- How PyAutoGUI controls mouse
- How keyboard automation works
- Timing and delays

---

## 📝 Testing Form Automation

#### Step 1: Open Test Form
- Double-click `test_form.html` in the project folder
- It opens in your default browser
- Keep the browser window open

#### Step 2: Get the File Path
- In browser address bar, you'll see something like:
  ```
  file:///C:/Users/YourName/form_automation_rpa/test_form.html
  ```
- Copy this entire URL

#### Step 3: Run Automation
```bash
python form_filler.py
```
- Select Option 2
- Paste the file:/// URL when prompted
- Enter `1` for number of records (test with one first)

#### Step 4: Watch It Work
- The script will:
  - Open the form in browser
  - Fill in Name, Email, Phone, Message
  - Submit the form
  - Show success message

---


## 🔧 Troubleshooting

### Problem: "No module named 'pyautogui'"
**Solution:**
```bash
pip install pyautogui
```

### Problem: "Permission denied" on pip install
**Solution:**
```bash
pip install --user -r requirements.txt
```

### Problem: Script types too fast
**Solution:**
Edit `form_filler.py`, change:
```python
pyautogui.PAUSE = 1  # Change to 2 or 3
```

### Problem: Form fields not filling correctly
**Solution:**
1. Maximize browser window manually
2. Check if TAB order matches your form
3. Increase delays: add more `time.sleep()` calls

### Problem: Can't find test_form.html
**Solution:**
The file should be in the same folder as `form_filler.py`. Open it by:
```bash
start test_form.html
```

---

## 📚 Additional Resources

### Documentation
- `README.md` - Project overview
- `CODE_EXPLANATION.md` - Detailed code walkthrough
- [PyAutoGUI Docs](https://pyautogui.readthedocs.io/)

---

