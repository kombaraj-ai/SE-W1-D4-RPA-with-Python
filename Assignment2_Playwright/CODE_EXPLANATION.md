# 📘 Playwright Code Explanation - Step by Step

This document provides a comprehensive breakdown of how Playwright automation works in Python.

## 📚 Table of Contents
1. [Understanding Async/Await](#understanding-asyncawait)
2. [Browser Initialization](#browser-initialization)
3. [Page Navigation](#page-navigation)
4. [Element Selection](#element-selection)
5. [Form Interaction](#form-interaction)
6. [Data Extraction](#data-extraction)
7. [Error Handling](#error-handling)
8. [Network Monitoring](#network-monitoring)

---

## 1. Understanding Async/Await

### What is Async Programming?

```python
async def my_function():
    await some_async_operation()
```

**async**: Declares that a function is asynchronous
**await**: Waits for an async operation to complete

### Why Playwright Uses Async?

**Traditional (Synchronous):**
```python
page.goto('https://example.com')  # Blocks until loaded
page.click('button')              # Blocks until clicked
```

**Playwright (Asynchronous):**
```python
await page.goto('https://example.com')  # Non-blocking
await page.click('button')              # Non-blocking
```

**Benefits:**
- Better performance
- Can handle multiple pages simultaneously
- More efficient resource usage
- Modern Python standard

### Running Async Code

```python
# Method 1: asyncio.run() (Python 3.7+)
import asyncio

async def main():
    # Your async code here
    pass

asyncio.run(main())

# Method 2: Event loop (older style)
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

---

## 2. Browser Initialization

### Step-by-Step Browser Launch

```python
async def initialize(self):
    # Step 1: Start Playwright
    playwright = await async_playwright().start()
```

**What happens:**
- Starts the Playwright server
- Prepares browser automation capabilities
- Returns a playwright instance

```python
    # Step 2: Launch Browser
    self.browser = await playwright.chromium.launch(
        headless=False,  # Show browser window
        slow_mo=500      # Slow down by 500ms
    )
```

**Browser Options Explained:**

**headless=False:**
- `True`: No GUI, runs in background (faster, less memory)
- `False`: Shows browser window (better for debugging)

**slow_mo=500:**
- Adds 500ms delay after each action
- Makes automation visible and easier to follow
- Set to 0 for production (faster)

**Other useful options:**
```python
browser = await playwright.chromium.launch(
    headless=True,
    args=['--start-maximized'],
    downloads_path='./downloads'
)
```

```python
    # Step 3: Create Browser Context
    self.context = await self.browser.new_context(
        viewport={'width': 1920, 'height': 1080},
        user_agent='Mozilla/5.0...'
    )
```

**What is Browser Context?**
- Think of it as an "incognito session"
- Isolated cookies, localStorage, cache
- Can have multiple contexts in one browser
- Each context = separate user session

**Why set viewport?**
- Consistent rendering across machines
- Responsive design testing
- Predictable element positions

**Why set user_agent?**
- Some sites block automated tools
- Appears as regular browser
- Better for scraping

```python
    # Step 4: Create Page
    self.page = await self.context.new_page()
```

**Page Object:**
- Represents a browser tab
- Where you do all interactions
- Can have multiple pages per context

---

## 3. Page Navigation

### Basic Navigation

```python
await page.goto('https://example.com')
```

**What happens internally:**
1. Sends HTTP request to URL
2. Waits for server response
3. Loads HTML, CSS, JavaScript
4. Executes JavaScript
5. Waits for page to be ready

### Wait Strategies

```python
await page.goto(url, wait_until='networkidle')
```

**wait_until options:**

**'load'** (default):
- Waits for window.onload event
- Page and resources loaded
- Fastest option

**'domcontentloaded':**
- Waits for DOMContentLoaded event
- HTML parsed, but resources may still load
- Good for most cases

**'networkidle':**
- Waits until no network requests for 500ms
- Most reliable for dynamic sites
- Slowest option

**Example:**
```python
# Fast, but might miss dynamic content
await page.goto(url, wait_until='load')

# Balanced approach
await page.goto(url, wait_until='domcontentloaded')

# Wait for everything (SPAs, AJAX)
await page.goto(url, wait_until='networkidle')
```

### Navigation with Timeout

```python
try:
    await page.goto(url, timeout=30000)  # 30 seconds
except TimeoutError:
    print("Page took too long to load")
```

**Default timeout:** 30 seconds
**Why increase timeout?**
- Slow websites
- Poor internet connection
- Heavy pages with lots of resources

---

## 4. Element Selection

### CSS Selectors (Most Common)

```python
# By ID
element = await page.query_selector('#username')

# By class
element = await page.query_selector('.product-card')

# By tag
element = await page.query_selector('button')

# Combined
element = await page.query_selector('button.submit')

# Nested
element = await page.query_selector('div.container > p.text')
```

### Getting Multiple Elements

```python
# Get all matching elements
products = await page.query_selector_all('.product')

# Iterate through them
for product in products:
    name = await product.query_selector('.name')
    price = await product.query_selector('.price')
```

### Playwright-Specific Selectors

```python
# By text content
await page.click('text=Login')

# By partial text
await page.click('text="Sign"')  # Matches "Sign Up", "Sign In", etc.

# By regex
await page.click('text=/Log.*/')

# By test ID (recommended for testing)
await page.click('[data-testid="submit-button"]')
```

### XPath Selectors

```python
# Find by XPath
element = await page.query_selector('xpath=//div[@class="product"]')

# Or use shorthand
element = await page.query_selector('//div[@class="product"]')
```

### Waiting for Selectors

```python
# Wait up to 5 seconds for element to appear
try:
    element = await page.wait_for_selector('.product', timeout=5000)
    print("Element found!")
except TimeoutError:
    print("Element not found within 5 seconds")
```

**When to use wait_for_selector:**
- Element loads dynamically (AJAX)
- Waiting for animation to complete
- Page renders progressively

---

## 5. Form Interaction

### Text Input

```python
# Method 1: fill() - Clears then types
await page.fill('input#username', 'john_doe')
```

**fill() behavior:**
1. Clears existing text
2. Types new text
3. Triggers input events

```python
# Method 2: type() - Types character by character
await page.type('input#search', 'playwright', delay=100)
```

**type() vs fill():**
- `fill()`: Faster, sets value directly
- `type()`: Slower, simulates real typing
- Use `type()` when you need realistic behavior

### Clicking Elements

```python
# Basic click
await page.click('button#submit')

# Click with options
await page.click('button', 
    button='right',      # Right-click
    click_count=2,       # Double-click
    delay=100            # Hold for 100ms
)

# Force click (even if obscured)
await page.click('button', force=True)
```

### Keyboard Input

```python
# Press single key
await page.press('input#search', 'Enter')

# Key combinations
await page.keyboard.press('Control+A')  # Select all
await page.keyboard.press('Control+C')  # Copy
```

**Common keys:**
- `Enter`, `Tab`, `Escape`
- `ArrowDown`, `ArrowUp`, `ArrowLeft`, `ArrowRight`
- `Backspace`, `Delete`
- `Control`, `Alt`, `Shift`, `Meta` (Command on Mac)

### Dropdown Selection

```python
# Select by value
await page.select_option('select#country', value='USA')

# Select by label
await page.select_option('select#country', label='United States')

# Select by index
await page.select_option('select#country', index=0)

# Multiple selection
await page.select_option('select#skills', ['Python', 'JavaScript'])
```

### Checkboxes and Radio Buttons

```python
# Check a checkbox
await page.check('input#agree-terms')

# Uncheck
await page.uncheck('input#agree-terms')

# Select radio button
await page.check('input#gender-male')
```

### File Upload

```python
# Upload single file
await page.set_input_files('input#file-upload', 'document.pdf')

# Upload multiple files
await page.set_input_files('input#files', ['file1.pdf', 'file2.pdf'])

# Clear file input
await page.set_input_files('input#file-upload', [])
```

---

## 6. Data Extraction

### Getting Text Content

```python
# Method 1: inner_text() - Visible text
element = await page.query_selector('.product-name')
text = await element.inner_text()
print(text)  # "Laptop Pro"
```

**inner_text():**
- Returns visible text only
- Respects CSS (display:none won't appear)
- Includes line breaks as displayed

```python
# Method 2: text_content() - All text
text = await element.text_content()
```

**text_content():**
- Returns all text, including hidden
- Ignores CSS styling
- Faster than inner_text()

### Getting HTML

```python
# Get inner HTML
html = await element.inner_html()
print(html)  # "<span>Price: $99</span>"

# Get outer HTML (includes the element itself)
html = await element.eval('element => element.outerHTML')
```

### Getting Attributes

```python
# Get single attribute
href = await element.get_attribute('href')
src = await element.get_attribute('src')
value = await element.get_attribute('value')

# Check if attribute exists
has_class = await element.get_attribute('class') is not None
```

### Extracting Structured Data

```python
async def scrape_products(page):
    products = []
    
    # Get all product elements
    product_elements = await page.query_selector_all('.product')
    
    for element in product_elements:
        # Extract name
        name_elem = await element.query_selector('.name')
        name = await name_elem.inner_text() if name_elem else "N/A"
        
        # Extract price
        price_elem = await element.query_selector('.price')
        price = await price_elem.inner_text() if price_elem else "N/A"
        
        # Extract image URL
        img_elem = await element.query_selector('img')
        image_url = await img_elem.get_attribute('src') if img_elem else "N/A"
        
        products.append({
            'name': name,
            'price': price,
            'image': image_url
        })
    
    return products
```

### Evaluating JavaScript

```python
# Execute JavaScript and get result
title = await page.evaluate('() => document.title')

# Pass parameters
result = await page.evaluate('(x, y) => x + y', 5, 3)
print(result)  # 8

# Complex evaluation
data = await page.evaluate('''
    () => {
        const items = Array.from(document.querySelectorAll('.item'));
        return items.map(item => item.textContent);
    }
''')
```

---

## 7. Error Handling

### Try-Except Pattern

```python
async def safe_scraping():
    try:
        await page.goto('https://example.com')
        await page.click('button#submit')
        
    except TimeoutError:
        print("Operation timed out")
        
    except Exception as e:
        print(f"Unexpected error: {e}")
        
    finally:
        await browser.close()  # Always cleanup
```

### Handling Missing Elements

```python
# Method 1: Check before accessing
element = await page.query_selector('.optional-element')
if element:
    text = await element.inner_text()
else:
    print("Element not found")

# Method 2: Try-except
try:
    element = await page.wait_for_selector('.element', timeout=5000)
    text = await element.inner_text()
except TimeoutError:
    print("Element didn't appear")
```

### Graceful Degradation

```python
async def extract_with_fallback(page):
    results = []
    products = await page.query_selector_all('.product')
    
    for product in products:
        try:
            name = await (await product.query_selector('.name')).inner_text()
        except:
            name = "N/A"
        
        try:
            price = await (await product.query_selector('.price')).inner_text()
        except:
            price = "N/A"
        
        results.append({'name': name, 'price': price})
    
    return results
```

### Retry Logic

```python
async def retry_operation(operation, max_attempts=3):
    for attempt in range(max_attempts):
        try:
            return await operation()
        except Exception as e:
            if attempt == max_attempts - 1:
                raise  # Re-raise on last attempt
            print(f"Attempt {attempt + 1} failed, retrying...")
            await asyncio.sleep(2)  # Wait before retry

# Usage
await retry_operation(lambda: page.click('button#submit'))
```

---

## 8. Network Monitoring

### Listening to Requests

```python
def handle_request(request):
    print(f"Request: {request.method} {request.url}")

page.on('request', handle_request)
```

**What you can do:**
- Log all requests
- Filter by type (XHR, image, script)
- Monitor API calls
- Detect tracking scripts

### Listening to Responses

```python
def handle_response(response):
    print(f"Response: {response.status} {response.url}")
    
page.on('response', handle_response)
```

### Intercepting and Modifying

```python
# Block images (faster loading)
async def block_images(route, request):
    if request.resource_type == 'image':
        await route.abort()
    else:
        await route.continue_()

await page.route('**/*', block_images)
```

**Resource types:**
- `document` - HTML pages
- `stylesheet` - CSS files
- `image` - Images
- `script` - JavaScript
- `xhr` - AJAX requests
- `fetch` - Fetch API calls

### Capturing API Responses

```python
api_data = []

async def capture_api(response):
    if '/api/' in response.url:
        data = await response.json()
        api_data.append(data)

page.on('response', capture_api)
await page.goto('https://example.com')

# Now api_data contains all API responses
print(f"Captured {len(api_data)} API calls")
```

---

## 9. Advanced Patterns

### Context Manager Pattern

```python
async def scrape_with_cleanup():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        try:
            await page.goto('https://example.com')
            # Do scraping...
        finally:
            await browser.close()  # Automatic cleanup
```

### Multiple Pages

```python
async def scrape_multiple_pages():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        
        # Create multiple pages
        page1 = await browser.new_page()
        page2 = await browser.new_page()
        page3 = await browser.new_page()
        
        # Navigate simultaneously
        await asyncio.gather(
            page1.goto('https://site1.com'),
            page2.goto('https://site2.com'),
            page3.goto('https://site3.com')
        )
        
        # All pages loaded in parallel!
```

### Pagination Handling

```python
async def scrape_all_pages():
    page_num = 1
    all_data = []
    
    while True:
        # Load page
        await page.goto(f'https://example.com/products?page={page_num}')
        
        # Extract data
        products = await page.query_selector_all('.product')
        if not products:
            break  # No more products
        
        # Process products
        for product in products:
            data = extract_product_data(product)
            all_data.append(data)
        
        # Check for next button
        next_button = await page.query_selector('a.next')
        if not next_button:
            break  # Last page
        
        # Click next
        await next_button.click()
        await page.wait_for_load_state('networkidle')
        page_num += 1
    
    return all_data
```

### Infinite Scroll

```python
async def scroll_to_bottom():
    previous_height = 0
    
    while True:
        # Get current scroll height
        current_height = await page.evaluate('document.body.scrollHeight')
        
        if current_height == previous_height:
            break  # No more content loading
        
        # Scroll to bottom
        await page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
        
        # Wait for new content
        await asyncio.sleep(2)
        
        previous_height = current_height
```

---

## 10. Best Practices

### 1. Always Use Waits

**Bad:**
```python
await page.goto(url)
await page.click('button')  # Might fail if page not ready
```

**Good:**
```python
await page.goto(url, wait_until='networkidle')
await page.wait_for_selector('button')
await page.click('button')
```

### 2. Handle Errors Gracefully

**Bad:**
```python
text = await page.query_selector('.price').inner_text()  # Crashes if missing
```

**Good:**
```python
element = await page.query_selector('.price')
text = await element.inner_text() if element else "N/A"
```

### 3. Clean Up Resources

**Bad:**
```python
browser = await playwright.chromium.launch()
# ... do stuff ...
# Forgot to close!
```

**Good:**
```python
browser = await playwright.chromium.launch()
try:
    # ... do stuff ...
finally:
    await browser.close()
```

### 4. Use Specific Selectors

**Bad:**
```python
await page.click('button')  # Which button?
```

**Good:**
```python
await page.click('button#submit')  # Specific button
await page.click('[data-testid="submit-btn"]')  # Even better
```

### 5. Add Rate Limiting

**Bad:**
```python
for url in urls:
    await page.goto(url)  # Hammers the server
```

**Good:**
```python
for url in urls:
    await page.goto(url)
    await asyncio.sleep(2)  # Be polite
```

---

## 11. Performance Optimization

### Disable Unnecessary Features

```python
context = await browser.new_context(
    java_script_enabled=False,  # If you don't need JS
    bypass_csp=True,            # Bypass content security policy
    ignore_https_errors=True    # Ignore SSL errors
)
```

### Block Resources

```python
await page.route('**/*.{png,jpg,jpeg,gif,svg,ico}', lambda route: route.abort())
await page.route('**/*.{css}', lambda route: route.abort())
```

**Speed improvement:** 2-5x faster page loads

### Use Browser Context Pool

```python
contexts = []
for i in range(5):
    context = await browser.new_context()
    contexts.append(context)

# Reuse contexts instead of creating new ones
```

---

## 12. Debugging Tips

### 1. Take Screenshots

```python
await page.screenshot(path='debug.png')
```

### 2. Pause Execution

```python
await page.pause()  # Opens inspector
```

### 3. Slow Down Actions

```python
browser = await playwright.chromium.launch(slow_mo=1000)
```

### 4. Verbose Logging

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### 5. Print Page Content

```python
html = await page.content()
print(html)
```

---

## Summary of Key Methods

### Navigation
- `page.goto(url)` - Navigate to URL
- `page.go_back()` - Go back
- `page.go_forward()` - Go forward
- `page.reload()` - Refresh page

### Selection
- `page.query_selector(selector)` - Find first match
- `page.query_selector_all(selector)` - Find all matches
- `page.wait_for_selector(selector)` - Wait for element

### Interaction
- `page.click(selector)` - Click element
- `page.fill(selector, text)` - Fill input
- `page.type(selector, text)` - Type text
- `page.press(selector, key)` - Press key
- `page.select_option(selector, value)` - Select dropdown

### Data Extraction
- `element.inner_text()` - Get visible text
- `element.text_content()` - Get all text
- `element.inner_html()` - Get HTML
- `element.get_attribute(name)` - Get attribute

### Waiting
- `page.wait_for_load_state(state)` - Wait for page state
- `page.wait_for_selector(selector)` - Wait for element
- `page.wait_for_url(url)` - Wait for URL
- `asyncio.sleep(seconds)` - Wait for time

---

This completes the comprehensive code explanation! 🎉
