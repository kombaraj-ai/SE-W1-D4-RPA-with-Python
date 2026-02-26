"""
E-Commerce Price Tracker using Playwright
This script demonstrates web scraping and automation with Playwright
Real-world use case: Track product prices across multiple websites
"""

import asyncio
from playwright.async_api import async_playwright
import pandas as pd
from datetime import datetime
import json
import os

class PriceTrackerBot:
    """
    Automated price tracking bot using Playwright
    Monitors product prices and saves results to Excel
    """
    
    def __init__(self, headless=False):
        """
        Initialize the bot
        
        Args:
            headless (bool): Run browser in headless mode (no GUI)
        """
        self.headless = headless
        self.browser = None
        self.context = None
        self.page = None
        self.results = []
        
    async def initialize(self):
        """Start the browser and create a new page"""
        print("🚀 Initializing Playwright browser...")
        
        # Launch browser
        playwright = await async_playwright().start()
        self.browser = await playwright.chromium.launch(
            headless=self.headless,
            slow_mo=500  # Slow down by 500ms for visibility
        )
        
        # Create browser context (like an incognito session)
        self.context = await self.browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        )
        
        # Create a new page
        self.page = await self.context.new_page()
        
        print("✓ Browser initialized successfully!")
        
    async def close(self):
        """Clean up and close the browser"""
        if self.browser:
            await self.browser.close()
            print("✓ Browser closed")
    
    async def search_amazon_demo(self, product_name):
        """
        Demo: Search Amazon-like product page
        
        Args:
            product_name (str): Product to search for
        """
        print(f"\n🔍 Searching for: {product_name}")
        
        try:
            # Navigate to demo e-commerce site (using a test site)
            print("  → Navigating to demo e-commerce site...")
            await self.page.goto('https://demo.playwright.dev/ecommerce/', 
                                 wait_until='networkidle',
                                 timeout=30000)
            
            print("  → Page loaded successfully")
            
            # Take a screenshot
            await self.page.screenshot(path='screenshots/homepage.png')
            print("  → Screenshot saved: screenshots/homepage.png")
            
            # Wait for page to be ready
            await self.page.wait_for_load_state('networkidle')
            
            return True
            
        except Exception as e:
            print(f"  ✗ Error: {e}")
            return False
    
    async def scrape_demo_products(self):
        """
        Scrape products from demo e-commerce site
        Demonstrates various Playwright selectors and interactions
        """
        print("\n📊 Scraping product information...")
        
        try:
            # Visit demo shopping site
            await self.page.goto('https://webscraper.io/test-sites/e-commerce/static', 
                                 wait_until='networkidle')
            
            print("  → Analyzing page structure...")
            
            # Wait for products to load
            await self.page.wait_for_selector('.product-wrapper', timeout=10000)
            
            # Get all product elements
            products = await self.page.query_selector_all('.product-wrapper')
            
            print(f"  → Found {len(products)} products")
            
            # Extract data from each product
            for idx, product in enumerate(products[:5], 1):  # Limit to 5 for demo
                try:
                    # Extract product name
                    name_element = await product.query_selector('.title')
                    name = await name_element.inner_text() if name_element else "N/A"
                    
                    # Extract price
                    price_element = await product.query_selector('.price')
                    price = await price_element.inner_text() if price_element else "N/A"
                    
                    # Extract description
                    desc_element = await product.query_selector('.description')
                    description = await desc_element.inner_text() if desc_element else "N/A"
                    
                    # Store result
                    product_data = {
                        'Product Name': name.strip(),
                        'Price': price.strip(),
                        'Description': description.strip()[:50] + "...",
                        'Timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        'Source': 'Demo E-Commerce Site'
                    }
                    
                    self.results.append(product_data)
                    print(f"  ✓ Product {idx}: {name.strip()} - {price.strip()}")
                    
                except Exception as e:
                    print(f"  ⚠ Error extracting product {idx}: {e}")
                    continue
            
            return True
            
        except Exception as e:
            print(f"  ✗ Error during scraping: {e}")
            return False
    
    async def search_wikipedia(self, search_term):
        """
        Search Wikipedia and extract information
        Demonstrates form filling and data extraction
        
        Args:
            search_term (str): Term to search
        """
        print(f"\n🔍 Searching Wikipedia for: {search_term}")
        
        try:
            # Go to Wikipedia
            print("  → Navigating to Wikipedia...")
            await self.page.goto('https://www.wikipedia.org/', wait_until='networkidle')
            
            # Find search box and type
            print("  → Filling search form...")
            search_box = await self.page.wait_for_selector('#searchInput', timeout=5000)
            await search_box.fill(search_term)
            
            # Click search button or press Enter
            await search_box.press('Enter')
            
            # Wait for results page
            await self.page.wait_for_load_state('networkidle')
            
            print("  → Extracting article information...")
            
            # Get the title
            title_element = await self.page.query_selector('#firstHeading')
            title = await title_element.inner_text() if title_element else "N/A"
            
            # Get first paragraph
            first_para = await self.page.query_selector('.mw-parser-output > p')
            content = await first_para.inner_text() if first_para else "N/A"
            
            # Take screenshot
            await self.page.screenshot(path=f'screenshots/wikipedia_{search_term.replace(" ", "_")}.png')
            
            result = {
                'Search Term': search_term,
                'Article Title': title,
                'First Paragraph': content[:200] + "...",
                'URL': self.page.url,
                'Timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            
            self.results.append(result)
            
            print(f"  ✓ Found: {title}")
            print(f"  ✓ URL: {self.page.url}")
            
            return True
            
        except Exception as e:
            print(f"  ✗ Error: {e}")
            return False
    
    async def fill_contact_form_demo(self, form_data):
        """
        Fill out a contact form automatically
        Demonstrates form interaction capabilities
        
        Args:
            form_data (dict): Dictionary containing form field values
        """
        print("\n📝 Filling contact form demo...")
        
        try:
            # Navigate to a demo form (using httpbin for testing)
            print("  → Loading demo form...")
            await self.page.goto('https://demoqa.com/automation-practice-form', 
                                 wait_until='networkidle')
            
            # Fill First Name
            print("  → Filling First Name...")
            await self.page.fill('#firstName', form_data.get('firstName', ''))
            
            # Fill Last Name
            print("  → Filling Last Name...")
            await self.page.fill('#lastName', form_data.get('lastName', ''))
            
            # Fill Email
            print("  → Filling Email...")
            await self.page.fill('#userEmail', form_data.get('email', ''))
            
            # Select Gender (click radio button)
            print("  → Selecting Gender...")
            gender = form_data.get('gender', 'Male')
            await self.page.click(f'label[for="gender-radio-{1 if gender == "Male" else 2}"]')
            
            # Fill Mobile
            print("  → Filling Mobile...")
            await self.page.fill('#userNumber', form_data.get('mobile', ''))
            
            # Take screenshot of filled form
            await self.page.screenshot(path='screenshots/form_filled.png')
            print("  ✓ Form filled successfully!")
            print("  ✓ Screenshot saved: screenshots/form_filled.png")
            
            # Note: Not actually submitting to avoid spam
            print("  ℹ Note: Skipping submission (demo mode)")
            
            return True
            
        except Exception as e:
            print(f"  ✗ Error filling form: {e}")
            return False
    
    async def test_login_workflow(self, username, password):
        """
        Demonstrate login workflow automation
        
        Args:
            username (str): Username for login
            password (str): Password for login
        """
        print("\n🔐 Testing login workflow...")
        
        try:
            # Go to demo login page
            print("  → Navigating to login page...")
            await self.page.goto('https://the-internet.herokuapp.com/login', 
                                 wait_until='networkidle')
            
            # Fill username
            print("  → Entering username...")
            await self.page.fill('#username', username)
            
            # Fill password
            print("  → Entering password...")
            await self.page.fill('#password', password)
            
            # Take screenshot before login
            await self.page.screenshot(path='screenshots/before_login.png')
            
            # Click login button
            print("  → Clicking login button...")
            await self.page.click('button[type="submit"]')
            
            # Wait for navigation
            await self.page.wait_for_load_state('networkidle')
            
            # Check if login was successful
            try:
                success_message = await self.page.wait_for_selector('.flash.success', timeout=3000)
                message_text = await success_message.inner_text()
                print(f"  ✓ Login successful!")
                print(f"  → Message: {message_text}")
                
                # Take screenshot after login
                await self.page.screenshot(path='screenshots/after_login.png')
                
                return True
                
            except:
                error_message = await self.page.query_selector('.flash.error')
                if error_message:
                    message_text = await error_message.inner_text()
                    print(f"  ✗ Login failed: {message_text}")
                return False
            
        except Exception as e:
            print(f"  ✗ Error during login: {e}")
            return False
    
    async def intercept_network_requests(self):
        """
        Demonstrate network request interception
        Useful for monitoring API calls, blocking resources, etc.
        """
        print("\n🌐 Setting up network monitoring...")
        
        captured_requests = []
        
        # Listen to all requests
        async def handle_request(request):
            captured_requests.append({
                'url': request.url,
                'method': request.method,
                'resource_type': request.resource_type
            })
            print(f"  📡 Request: {request.method} {request.resource_type} - {request.url[:80]}")
        
        self.page.on('request', handle_request)
        
        # Visit a page to capture requests
        print("  → Loading page to capture network traffic...")
        await self.page.goto('https://socialeagle.ai', wait_until='networkidle')
        
        print(f"\n  ✓ Captured {len(captured_requests)} network requests")
        
        # Save to JSON
        with open('network_requests.json', 'w') as f:
            json.dump(captured_requests, f, indent=2)
        
        print("  ✓ Network data saved to: network_requests.json")
        
        return captured_requests
    
    def save_results_to_excel(self, filename='price_tracker_results.xlsx'):
        """
        Save scraped results to Excel file
        
        Args:
            filename (str): Output filename
        """
        if not self.results:
            print("\n⚠ No results to save")
            return False
        
        try:
            print(f"\n💾 Saving {len(self.results)} results to Excel...")
            
            df = pd.DataFrame(self.results)
            df.to_excel(filename, index=False, engine='openpyxl')
            
            print(f"  ✓ Results saved to: {filename}")
            print(f"\n📊 Summary:")
            print(df.to_string(index=False))
            
            return True
            
        except Exception as e:
            print(f"  ✗ Error saving to Excel: {e}")
            return False


async def demo_basic_navigation():
    """
    Demo 1: Basic Navigation and Screenshot
    Shows fundamental Playwright operations
    """
    print("\n" + "="*60)
    print("DEMO 1: Basic Navigation and Screenshots")
    print("="*60)
    
    async with async_playwright() as p:
        # Launch browser
        browser = await p.chromium.launch(headless=False, slow_mo=500)
        page = await browser.new_page()
        
        # Navigate to a page
        print("\n→ Navigating to socialeagle.ai...")
        await page.goto('https://socialeagle.ai')
        
        # Get page title
        title = await page.title()
        print(f"→ Page title: {title}")
        
        # Take screenshot
        os.makedirs('screenshots', exist_ok=True)
        await page.screenshot(path='screenshots/example_page.png')
        print("→ Screenshot saved: screenshots/example_page.png")
        
        # Get page content
        content = await page.content()
        print(f"→ Page HTML length: {len(content)} characters")
        
        # Wait a bit to see the browser
        await asyncio.sleep(2)
        
        await browser.close()
        print("✓ Demo 1 completed!")


async def demo_form_interaction():
    """
    Demo 2: Form Interaction
    Shows how to interact with web forms
    """
    print("\n" + "="*60)
    print("DEMO 2: Form Interaction")
    print("="*60)
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=500)
        page = await browser.new_page()
        
        # Go to DuckDuckGo (search engine)
        print("\n→ Opening DuckDuckGo...")
        await page.goto('https://duckduckgo.com')
        
        # Find search box and type
        print("→ Typing search query...")
        await page.fill('input[name="q"]', 'Social Eagle AI Gen AI')
        
        # Press Enter
        print("→ Submitting search...")
        await page.press('input[name="q"]', 'Enter')
        
        # Wait for results
        await page.wait_for_load_state('networkidle')
        
        # Get search results
        print("→ Analyzing search results...")
        results = await page.query_selector_all('.result')
        print(f"→ Found {len(results)} search results")
        
        # Take screenshot
        await page.screenshot(path='screenshots/search_results.png')
        print("→ Screenshot saved: screenshots/search_results.png")
        
        await asyncio.sleep(2)
        await browser.close()
        print("✓ Demo 2 completed!")


async def demo_data_extraction():
    """
    Demo 3: Data Extraction
    Shows how to scrape data from web pages
    """
    print("\n" + "="*60)
    print("DEMO 3: Data Extraction")
    print("="*60)
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=500)
        page = await browser.new_page()
        
        # Visit quotes website
        print("\n→ Visiting quotes website...")
        await page.goto('http://quotes.toscrape.com/')
        
        # Extract quotes
        print("→ Extracting quotes...")
        quotes = await page.query_selector_all('.quote')
        
        extracted_data = []
        for i, quote in enumerate(quotes[:5], 1):  # First 5 quotes
            text_elem = await quote.query_selector('.text')
            author_elem = await quote.query_selector('.author')
            
            text = await text_elem.inner_text() if text_elem else "N/A"
            author = await author_elem.inner_text() if author_elem else "N/A"
            
            extracted_data.append({
                'Quote': text,
                'Author': author
            })
            
            print(f"  {i}. {text[:50]}... - {author}")
        
        # Save to Excel
        df = pd.DataFrame(extracted_data)
        df.to_excel('quotes_data.xlsx', index=False)
        print(f"\n→ Saved {len(extracted_data)} quotes to: quotes_data.xlsx")
        
        await asyncio.sleep(2)
        await browser.close()
        print("✓ Demo 3 completed!")


async def main():
    """Main execution function with menu"""
    
    print("""
    ╔══════════════════════════════════════════════════════════╗
    ║       Playwright Web Automation & Scraping Demo         ║
    ║                                                          ║
    ║  Real-world automation examples using Playwright        ║
    ╚══════════════════════════════════════════════════════════╝
    """)
    
    # Create screenshots directory
    os.makedirs('screenshots', exist_ok=True)
    
    print("\nSelect a demo to run:")
    print("1. Basic Navigation & Screenshots")
    print("2. Form Interaction & Search")
    print("3. Data Extraction & Web Scraping")
    #print("4. Complete Price Tracker Demo (All Features)")
    #print("5. Login Workflow Automation")
    #print("6. Network Request Monitoring")
    
    choice = input("\nEnter your choice (1-6): ").strip()
    
    if choice == "1":
        await demo_basic_navigation()
        
    elif choice == "2":
        await demo_form_interaction()
        
    elif choice == "3":
        await demo_data_extraction()
        
    elif choice == "4":
        print("\n→ Running complete price tracker demo...")
        
        # Initialize bot
        bot = PriceTrackerBot(headless=False)
        await bot.initialize()
        
        try:
            # Demo 1: Scrape products
            await bot.scrape_demo_products()
            
            await asyncio.sleep(2)
            
            # Demo 2: Wikipedia search
            await bot.search_wikipedia('Python programming')
            
            await asyncio.sleep(2)
            
            # Save results
            bot.save_results_to_excel('tracker_results.xlsx')
            
        finally:
            await bot.close()
        
        print("\n✓ Complete demo finished!")
        
    elif choice == "5":
        print("\n→ Running login workflow demo...")
        
        bot = PriceTrackerBot(headless=False)
        await bot.initialize()
        
        try:
            # Test login with demo credentials
            await bot.test_login_workflow('tomsmith', 'SuperSecretPassword!')
            
            await asyncio.sleep(3)
            
        finally:
            await bot.close()
        
        print("\n✓ Login demo completed!")
        
    elif choice == "6":
        print("\n→ Running network monitoring demo...")
        
        bot = PriceTrackerBot(headless=False)
        await bot.initialize()
        
        try:
            await bot.intercept_network_requests()
            await asyncio.sleep(2)
            
        finally:
            await bot.close()
        
        print("\n✓ Network monitoring completed!")
        
    else:
        print("\n✗ Invalid choice!")
        return
    
    print("\n" + "="*60)
    print("Thank you for trying Playwright automation!")
    print("Check the 'screenshots' folder for captured images")
    print("="*60)


if __name__ == "__main__":
    # Run the main async function
    asyncio.run(main())
