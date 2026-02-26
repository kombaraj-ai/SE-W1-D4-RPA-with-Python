"""
RPA Web Form Automation using PyAutoGUI
This script automates filling out a contact form by reading data from Excel
"""

import pyautogui
import time
import pandas as pd
import webbrowser
import os

# Set PyAutoGUI safety settings
pyautogui.PAUSE = 1  # Add 1 second pause between actions
pyautogui.FAILSAFE = True  # Move mouse to top-left corner to abort

class FormAutomation:
    """Class to handle automated form filling"""
    
    def __init__(self, excel_file):
        """
        Initialize the automation with data source
        
        Args:
            excel_file (str): Path to Excel file containing form data
        """
        self.excel_file = excel_file
        self.data = None
        
    def load_data(self):
        """Load data from Excel file"""
        try:
            self.data = pd.read_excel(self.excel_file)
            print(f"✓ Loaded {len(self.data)} records from {self.excel_file}")
            return True
        except Exception as e:
            print(f"✗ Error loading Excel file: {e}")
            return False
    
    def open_form_page(self, url):
        """
        Open the form page in default browser
        
        Args:
            url (str): URL of the form to fill
        """
        print(f"\n📋 Opening form page: {url}")
        webbrowser.open(url)
        time.sleep(3)  # Wait for browser to open and page to load
        
        # Maximize browser window for consistent positioning
        pyautogui.hotkey('win', 'up')
        time.sleep(1)
    
    def find_and_click(self, image_path, description, confidence=0.8):
        """
        Find an element by image and click it
        
        Args:
            image_path (str): Path to screenshot of element
            description (str): Description for logging
            confidence (float): Matching confidence (0-1)
        
        Returns:
            bool: True if found and clicked, False otherwise
        """
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=confidence)
            if location:
                center = pyautogui.center(location)
                pyautogui.click(center)
                print(f"✓ Clicked: {description}")
                return True
            else:
                print(f"✗ Could not find: {description}")
                return False
        except Exception as e:
            print(f"✗ Error finding {description}: {e}")
            return False
    
    def type_with_delay(self, text, interval=0.1):
        """
        Type text with delay between keystrokes
        
        Args:
            text (str): Text to type
            interval (float): Delay between keystrokes
        """
        pyautogui.write(str(text), interval=interval)
        time.sleep(0.5)
    
    def fill_form_fields(self, record):
        """
        Fill form fields using TAB navigation
        
        Args:
            record (Series): Pandas series containing form data
        """
        print(f"\n🔄 Processing: {record['Name']}")
        
        # Click in first field or press TAB to start
        pyautogui.press('tab')
        time.sleep(0.3)
        
        # Fill Name field
        print("  → Filling Name...")
        self.type_with_delay(record['Name'])
        pyautogui.press('tab')
        
        # Fill Email field
        print("  → Filling Email...")
        self.type_with_delay(record['Email'])
        pyautogui.press('tab')
        
        # Fill Phone field
        print("  → Filling Phone...")
        self.type_with_delay(record['Phone'])
        pyautogui.press('tab')
        
        # Fill Message field
        print("  → Filling Message...")
        self.type_with_delay(record['Message'])
        
        time.sleep(0.5)
    
    def submit_form(self):
        """Submit the form using keyboard shortcut or button click"""
        print("  → Submitting form...")
        
        # Method 1: Press TAB to reach submit button and ENTER
        pyautogui.press('tab')
        time.sleep(0.3)
        pyautogui.press('enter')
        
        time.sleep(2)  # Wait for submission
        print("✓ Form submitted!")
    
    def automated_fill(self, url, max_records=None):
        """
        Main automation workflow
        
        Args:
            url (str): URL of the form
            max_records (int): Maximum number of records to process
        """
        if not self.load_data():
            return
        
        # Limit records if specified
        records_to_process = self.data if max_records is None else self.data.head(max_records)
        
        print(f"\n🤖 Starting automation for {len(records_to_process)} records...")
        print("⚠️  IMPORTANT: Move mouse to top-left corner to emergency stop!")
        
        # Countdown before starting
        for i in range(3, 0, -1):
            print(f"   Starting in {i}...")
            time.sleep(1)
        
        # Process each record
        for index, record in records_to_process.iterrows():
            try:
                # Open form page for each submission
                self.open_form_page(url)
                
                # Fill and submit
                self.fill_form_fields(record)
                self.submit_form()
                
                print(f"✓ Completed record {index + 1}/{len(records_to_process)}")
                
                # Wait before next iteration
                time.sleep(2)
                
            except pyautogui.FailSafeException:
                print("\n⚠️  EMERGENCY STOP - Mouse moved to corner!")
                break
            except Exception as e:
                print(f"\n✗ Error processing record {index + 1}: {e}")
                continue
        
        print("\n🎉 Automation completed!")

def get_screen_info():
    """Display screen information for positioning"""
    screen_width, screen_height = pyautogui.size()
    current_x, current_y = pyautogui.position()
    
    print("="*50)
    print("SCREEN INFORMATION")
    print("="*50)
    print(f"Screen Size: {screen_width} x {screen_height}")
    print(f"Current Mouse Position: X={current_x}, Y={current_y}")
    print("="*50)

def demo_mouse_keyboard():
    """Demonstrate basic PyAutoGUI mouse and keyboard operations"""
    print("\n" + "="*50)
    print("PyAutoGUI DEMO - Basic Operations")
    print("="*50)
    
    # Get screen info
    get_screen_info()
    
    print("\n📍 Mouse Operations Demo:")
    print("  Moving mouse to center of screen...")
    screen_width, screen_height = pyautogui.size()
    pyautogui.moveTo(screen_width/2, screen_height/2, duration=1)
    
    print("  Moving mouse relatively (+100, +100)...")
    pyautogui.move(100, 100, duration=0.5)
    
    print("\n⌨️  Keyboard Operations Demo:")
    print("  Opening Notepad to demonstrate typing...")
    pyautogui.press('win')
    time.sleep(0.5)
    pyautogui.write('notepad', interval=0.1)
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(1)
    # Press Ctrl+N (Create New File)
    pyautogui.hotkey('ctrl', 'n')

    print("  Typing sample text...")
    pyautogui.write('Hello from PyAutoGUI!', interval=0.1)
    pyautogui.press('enter')
    pyautogui.write('This is automated typing.', interval=0.1)
    
    time.sleep(2)
    print("\n  Closing Notepad...")
    pyautogui.hotkey('alt', 'f4')
    time.sleep(0.5)
    #pyautogui.press('n')  # Don't save
    
    print("\n✓ Demo completed!")

if __name__ == "__main__":
    print("""
    ╔════════════════════════════════════════════════════╗
    ║     PyAutoGUI RPA - Form Automation Demo           ║
    ║                                                    ║
    ║  This script demonstrates automated form filling   ║
    ║  using mouse and keyboard automation.              ║
    ╚════════════════════════════════════════════════════╝
    """)
    
    # Menu
    print("\nSelect an option:")
    print("1. Run Basic PyAutoGUI Demo")
    print("2. Run Form Automation (requires sample_data.xlsx and form URL)")
    print("3. Display Screen Information Only")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice == "1":
        demo_mouse_keyboard()
        
    elif choice == "2":
        # Check if Excel file exists
        excel_file = "sample_data.xlsx"
        if not os.path.exists(excel_file):
            print(f"\n✗ Error: {excel_file} not found!")
            print("  Please ensure the Excel file is in the same directory.")
        else:
            # Example form URL - Replace with your actual form URL
            form_url = input("\nEnter form URL (or press Enter for demo URL): ").strip()
            if not form_url:
                form_url = "https://docs.google.com/forms/d/e/YOUR_FORM_ID/viewform"
                print(f"Using demo URL: {form_url}")
            
            # Create automation instance
            bot = FormAutomation(excel_file)
            
            # Run automation (process only first record for demo)
            max_records = int(input("How many records to process? (default 1): ") or "1")
            bot.automated_fill(form_url, max_records=max_records)
    
    elif choice == "3":
        get_screen_info()
        
        # Display mouse position tracking
        print("\n📍 Mouse Position Tracker (Press Ctrl+C to stop)")
        print("Move your mouse around to see coordinates:\n")
        try:
            while True:
                x, y = pyautogui.position()
                print(f"\rX: {x:4d}  Y: {y:4d}", end='', flush=True)
                time.sleep(0.1)
        except KeyboardInterrupt:
            print("\n\nTracker stopped.")
    
    else:
        print("\n✗ Invalid choice!")
