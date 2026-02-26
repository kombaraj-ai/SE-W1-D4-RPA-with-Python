# PyAutoGUI RPA - Automated Form Filler

A practical Python RPA (Robotic Process Automation) application that automates web form filling using PyAutoGUI for mouse and keyboard operations.

## 📋 Project Overview

This project demonstrates real-world RPA automation by:
- Reading data from an Excel file
- Opening a web browser automatically
- Navigating and filling form fields using keyboard/mouse automation
- Submitting forms automatically
- Processing multiple records in batch

## 🎯 Use Case

Perfect for automating repetitive data entry tasks such as:
- Contact form submissions
- Survey responses
- Registration forms
- Data migration to web-based systems
- Testing web forms with multiple data sets

## 📦 Project Structure

```
form_automation_rpa/
│
├── form_filler.py          # Main automation script
├── sample_data.xlsx        # Sample Excel data file
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🔧 Prerequisites

- **Python 3.7+** installed on Windows
- **pip** package manager
- Web browser (Chrome, Firefox, Edge, etc.)
- Internet connection for form access

## ⚙️ Installation

1. **Extract the ZIP file** to your desired location

2. **Open Command Prompt** in the project directory

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

### Running the Application

Open Command Prompt in the project directory and run:

```bash
python form_filler.py
```

### Menu Options

The application provides three options:

#### **Option 1: Basic PyAutoGUI Demo**
- Demonstrates fundamental mouse and keyboard operations
- Opens Notepad and types sample text
- Shows screen coordinates and mouse movements
- **Perfect for beginners to understand how PyAutoGUI works**

#### **Option 2: Form Automation**
- Reads data from `sample_data.xlsx`
- Automates form filling on a specified URL
- Processes multiple records automatically
- **The main RPA functionality**

#### **Option 3: Screen Information Tool**
- Displays screen resolution
- Shows real-time mouse coordinates
- Useful for positioning elements
- **Helpful for customizing the script**

## 📝 Customizing for Your Form

To use with your own web form:

1. **Prepare your Excel data** following this structure:
   - Column 1: `Name`
   - Column 2: `Email`
   - Column 3: `Phone`
   - Column 4: `Message`

2. **Modify the `fill_form_fields()` method** in `form_filler.py` to match your form's field order

3. **Update the URL** when prompted or hardcode it in the script

4. **Test with 1 record first** before processing in bulk

## ⚠️ Important Notes

### Safety Features

- **FAILSAFE**: Move mouse to top-left corner of screen to emergency stop
- **PAUSE**: 1-second delay between operations (configurable)
- **Countdown**: 3-second countdown before automation starts

### Best Practices

1. **Test on a single record first** to ensure correct field mapping
2. **Keep the browser window maximized** for consistent positioning
3. **Don't move the mouse** during automation
4. **Monitor the first few submissions** to catch any issues
5. **Use on test/demo forms** before production forms

### Limitations

- Requires Windows OS (PyAutoGUI works cross-platform but this demo is Windows-optimized)
- Screen resolution changes may affect positioning
- Works best with keyboard navigation (TAB-based form filling)
- Browser must remain in focus during operation

## 🔍 How It Works (Step-by-Step)

### 1. **Data Loading**
```python
self.data = pd.read_excel(self.excel_file)
```
- Reads Excel file using pandas
- Stores data in DataFrame for processing

### 2. **Browser Opening**
```python
webbrowser.open(url)
pyautogui.hotkey('win', 'up')  # Maximize window
```
- Opens default browser with form URL
- Maximizes window for consistent positioning

### 3. **Form Navigation**
```python
pyautogui.press('tab')        # Move to next field
pyautogui.write(text)         # Type text
```
- Uses TAB key to navigate between fields
- Types text with configurable delay

### 4. **Form Submission**
```python
pyautogui.press('enter')      # Submit form
```
- Submits form using Enter key
- Waits for submission to complete

### 5. **Batch Processing**
- Iterates through all records in Excel
- Opens new form page for each submission
- Handles errors gracefully

## 🎓 Learning Points

### PyAutoGUI Core Functions Used

1. **Mouse Operations:**
   ```python
   pyautogui.moveTo(x, y, duration=1)    # Move to coordinates
   pyautogui.click(x, y)                 # Click at position
   pyautogui.position()                  # Get current position
   ```

2. **Keyboard Operations:**
   ```python
   pyautogui.write('text', interval=0.1)  # Type text
   pyautogui.press('enter')               # Press single key
   pyautogui.hotkey('ctrl', 'c')          # Press key combination
   ```

3. **Screen Operations:**
   ```python
   pyautogui.size()                       # Get screen size
   pyautogui.screenshot()                 # Capture screenshot
   pyautogui.locateOnScreen('image.png') # Find image on screen
   ```

## 🛠️ Troubleshooting

### Issue: Script runs too fast
**Solution:** Increase `pyautogui.PAUSE` value in the script

### Issue: Fields not filling correctly
**Solution:** Adjust TAB navigation order or add `time.sleep()` delays

### Issue: Browser window not maximizing
**Solution:** Manually maximize before starting or adjust the hotkey for your OS

### Issue: Excel file not found
**Solution:** Ensure `sample_data.xlsx` is in the same directory as the script

## 📊 Sample Data Format

The Excel file should have these columns:

| Name          | Email                    | Phone          | Message                      |
|---------------|--------------------------|----------------|------------------------------|
| John Doe      | john.doe@example.com     | (555) 123-4567 | Interested in your products  |
| Jane Smith    | jane.smith@example.com   | (555) 234-5678 | Need more information        |

## 🔐 Security Considerations

- **Never** use this for unauthorized automation
- **Always** get permission before automating third-party websites
- **Don't** include sensitive credentials in the code
- **Be aware** of rate limiting and terms of service

## 🎯 Real-World Applications

1. **Data Migration**: Transfer data from Excel to web-based CRM
2. **Form Testing**: Test forms with multiple data sets
3. **Bulk Registration**: Register multiple users/accounts
4. **Survey Distribution**: Submit surveys with varied responses
5. **Lead Generation**: Submit contact forms to multiple websites

## 📚 Additional Resources

- [PyAutoGUI Documentation](https://pyautogui.readthedocs.io/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Python RPA Best Practices](https://realpython.com/python-gui-automation/)

## 🤝 Contributing

Feel free to modify and extend this project for your specific needs!

## 📄 License

This is a demo project for educational purposes. Use responsibly and ethically.

## ⚡ Quick Start Example

```bash
# Install dependencies
pip install -r requirements.txt

# Run the script
python form_filler.py

# Select Option 1 to see basic demo
# Select Option 2 to run form automation
```

---

**Happy Automating! 🤖**
