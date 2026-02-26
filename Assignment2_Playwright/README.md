# 🎭 Playwright Web Automation & Scraping

A comprehensive Python project demonstrating **real-world web automation** and **web scraping** using Playwright - the modern automation framework by Microsoft.

## 📋 Project Overview

This project showcases practical automation scenarios including:
- 🔍 **Web scraping** - Extract data from e-commerce sites
- 📝 **Form automation** - Fill and submit web forms automatically
- 🔐 **Login workflows** - Automate authentication processes
- 📊 **Data extraction** - Scrape and save data to Excel
- 🌐 **Network monitoring** - Intercept and analyze HTTP requests
- 📸 **Screenshot capture** - Document automation steps

## 🎯 Real-World Use Cases

### 1. **Price Tracking**
Monitor product prices across multiple e-commerce sites:
- Track price changes over time
- Get alerts when prices drop
- Compare prices across competitors
- Export data to Excel for analysis

### 2. **Form Automation**
Automate repetitive form submissions:
- Contact forms
- Registration forms
- Survey submissions
- Data entry tasks

### 3. **Web Scraping**
Extract valuable data from websites:
- Product information
- News articles
- Social media posts
- Research data

### 4. **Testing & QA**
Automated website testing:
- Functional testing
- Regression testing
- UI/UX validation
- Cross-browser testing

## 🚀 Why Playwright?

Playwright is superior to older tools like Selenium because:

✅ **Faster** - Native browser automation, no WebDriver
✅ **More Reliable** - Auto-waits for elements, fewer flaky tests
✅ **Modern** - Supports async/await, handles SPAs perfectly
✅ **Multi-browser** - Chromium, Firefox, and WebKit support
✅ **Network Control** - Intercept, modify, or mock network requests
✅ **Auto-screenshots** - Built-in screenshot and video recording

## 📦 Project Structure

```
playwright_automation/
│
├── price_tracker.py          # Main automation script
├── requirements.txt           # Dependencies
├── README.md                 # This file
├── CODE_EXPLANATION.md       # Detailed code walkthrough
├── QUICK_START.md            # Installation guide
│
├── screenshots/              # Auto-generated screenshots
│   ├── homepage.png
│   ├── search_results.png
│   └── form_filled.png
│
└── output/                   # Generated data files
    ├── tracker_results.xlsx
    ├── quotes_data.xlsx
    └── network_requests.json
```

## 🔧 Prerequisites

- **Python 3.8+** (Playwright requires Python 3.8 or higher)
- **pip** package manager
- **10 GB disk space** (for browser binaries)
- **Internet connection** (for browser downloads)

## ⚙️ Installation

### Step 1: Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Install Playwright Browsers

**This is critical!** Playwright needs to download browser binaries:

```bash
playwright install
```

This downloads Chromium, Firefox, and WebKit (~300MB each).

**Or install only Chromium:**
```bash
playwright install chromium
```

### Step 3: Verify Installation

```bash
python -c "from playwright.sync_api import sync_playwright; print('Playwright ready!')"
```

## 🎬 Running the Demos

### Launch the Application

```bash
python price_tracker.py
```

### Available Demos

#### **Demo 1: Basic Navigation & Screenshots**
- Opens example.com
- Captures screenshots
- Demonstrates page navigation
- Shows title extraction

**Perfect for:** Understanding Playwright basics

---

#### **Demo 2: Form Interaction & Search**
- Opens DuckDuckGo
- Performs a search
- Captures search results
- Demonstrates form filling

**Perfect for:** Learning form automation

---

#### **Demo 3: Data Extraction & Web Scraping**
- Scrapes quotes from quotes.toscrape.com
- Extracts text and author information
- Saves data to Excel
- Demonstrates selector usage

**Perfect for:** Learning web scraping

---

#### **Demo 4: Complete Price Tracker**
- Scrapes product data from e-commerce site
- Searches Wikipedia for information
- Saves all results to Excel
- Demonstrates multiple automation tasks

**Perfect for:** Seeing everything in action

---

#### **Demo 5: Login Workflow Automation**
- Automates login process
- Fills username and password
- Handles authentication
- Captures before/after screenshots

**Perfect for:** Authentication automation

---

#### **Demo 6: Network Request Monitoring**
- Intercepts all HTTP requests
- Logs request methods and URLs
- Saves network data to JSON
- Demonstrates network interception

**Perfect for:** API monitoring and debugging

## 🎓 Key Features Demonstrated

### 1. **Browser Control**

```python
# Launch browser
browser = await playwright.chromium.launch(
    headless=False,  # Show browser window
    slow_mo=500      # Slow down by 500ms
)

# Create new page
page = await browser.new_page()
```

### 2. **Navigation**

```python
# Navigate to URL
await page.goto('https://example.com', wait_until='networkidle')

# Get current URL
url = page.url

# Go back/forward
await page.go_back()
await page.go_forward()
```

### 3. **Element Interaction**

```python
# Click elements
await page.click('button#submit')

# Fill text inputs
await page.fill('input#email', 'user@example.com')

# Press keys
await page.press('input#search', 'Enter')

# Select dropdown options
await page.select_option('select#country', 'USA')
```

### 4. **Data Extraction**

```python
# Get text content
text = await element.inner_text()

# Get HTML content
html = await element.inner_html()

# Get attribute
value = await element.get_attribute('href')

# Query all matching elements
products = await page.query_selector_all('.product')
```

### 5. **Waiting Strategies**

```python
# Wait for selector
await page.wait_for_selector('.product', timeout=5000)

# Wait for navigation
await page.wait_for_load_state('networkidle')

# Wait for specific time
await asyncio.sleep(2)

# Wait for URL
await page.wait_for_url('**/success')
```

### 6. **Screenshots & Video**

```python
# Full page screenshot
await page.screenshot(path='screenshot.png')

# Element screenshot
element = await page.query_selector('.header')
await element.screenshot(path='header.png')

# PDF generation
await page.pdf(path='page.pdf')
```

## 📊 Sample Output

### Excel Output Example

| Product Name | Price | Description | Timestamp | Source |
|--------------|-------|-------------|-----------|--------|
| Laptop Pro | $1299 | High-performance... | 2024-02-26 10:30:00 | Demo Site |
| Smartphone X | $899 | Latest model... | 2024-02-26 10:30:05 | Demo Site |

### Network Request JSON

```json
[
  {
    "url": "https://example.com/api/data",
    "method": "GET",
    "resource_type": "fetch"
  },
  {
    "url": "https://example.com/styles.css",
    "method": "GET",
    "resource_type": "stylesheet"
  }
]
```

## 🎯 Customization Guide

### Modifying for Your Own Website

1. **Change the URL:**
```python
await page.goto('https://your-target-site.com')
```

2. **Update Selectors:**
```python
# Find the right selector using browser DevTools (F12)
products = await page.query_selector_all('your-selector')
```

3. **Adjust Wait Times:**
```python
await page.wait_for_selector('.products', timeout=10000)  # 10 seconds
```

4. **Customize Data Extraction:**
```python
name = await element.query_selector('.product-name')
price = await element.query_selector('.product-price')
```

## ⚠️ Important Notes

### Headless vs Headed Mode

**Headless (no GUI):**
```python
bot = PriceTrackerBot(headless=True)
```
- Faster execution
- Lower resource usage
- Good for production/servers

**Headed (with GUI):**
```python
bot = PriceTrackerBot(headless=False)
```
- See what's happening
- Better for development/debugging
- Easier troubleshooting

### Best Practices

1. **Always respect robots.txt**
2. **Add delays between requests** (be polite)
3. **Handle errors gracefully**
4. **Use User-Agent headers**
5. **Don't overwhelm servers**
6. **Check website Terms of Service**

### Legal Considerations

⚖️ **Before scraping any website:**
- ✅ Read the website's Terms of Service
- ✅ Check robots.txt file
- ✅ Use reasonable request rates
- ✅ Respect copyright and data ownership
- ❌ Don't scrape personal/private data
- ❌ Don't bypass authentication illegally

## 🐛 Troubleshooting

### Issue: "playwright not found"
**Solution:**
```bash
pip install playwright
playwright install
```

### Issue: "Timeout waiting for element"
**Solution:**
```python
# Increase timeout
await page.wait_for_selector('.element', timeout=30000)

# Or check if selector is correct
```

### Issue: "Browser binary not found"
**Solution:**
```bash
playwright install chromium
```

### Issue: "Page didn't load"
**Solution:**
```python
# Try different wait strategies
await page.goto(url, wait_until='domcontentloaded')
# or
await page.goto(url, wait_until='networkidle')
```

### Issue: Script runs too fast
**Solution:**
```python
# Add slow_mo parameter
browser = await playwright.chromium.launch(slow_mo=1000)
```

## 🔐 Security Tips

1. **Never hardcode credentials** in scripts
2. **Use environment variables** for sensitive data
3. **Don't commit** screenshots with personal info
4. **Be careful** with network interception
5. **Sanitize** extracted data before storage

## 📈 Performance Tips

### Speed Optimization

```python
# Block unnecessary resources
await page.route('**/*.{png,jpg,jpeg,gif}', lambda route: route.abort())

# Disable CSS
await context.add_init_script("delete window.CSS")

# Use headless mode
browser = await playwright.chromium.launch(headless=True)
```

### Memory Management

```python
# Close pages when done
await page.close()

# Clear context
await context.clear_cookies()

# Proper cleanup
await browser.close()
```

## 🎓 Learning Resources

### Official Documentation
- [Playwright Python Docs](https://playwright.dev/python/)
- [API Reference](https://playwright.dev/python/docs/api/class-playwright)
- [Examples Gallery](https://playwright.dev/python/docs/examples)

### Selectors Guide
- **CSS Selectors**: `.class`, `#id`, `tag`
- **Text Selectors**: `text=Login`, `text=/regex/`
- **XPath**: `//div[@class="product"]`
- **Custom**: `data-testid=submit-button`

## 🚀 Next Steps

### Beginner Level
- [x] Run all 6 demos
- [x] Understand async/await
- [x] Learn basic selectors
- [x] Practice with test sites

### Intermediate Level
- [x] Customize for your own sites
- [x] Handle pagination
- [x] Implement error recovery
- [x] Add data validation

### Advanced Level
- [x] Concurrent scraping (multiple pages)
- [x] Proxy rotation
- [x] CAPTCHA handling
- [x] Database integration
- [x] Scheduling with cron/Task Scheduler

## 📚 Additional Features to Explore

### Mobile Emulation
```python
iphone = playwright.devices['iPhone 12']
context = await browser.new_context(**iphone)
```

### Geolocation
```python
context = await browser.new_context(
    geolocation={'latitude': 40.7128, 'longitude': -74.0060},
    permissions=['geolocation']
)
```

### File Downloads
```python
async with page.expect_download() as download_info:
    await page.click('a#download-link')
download = await download_info.value
await download.save_as('downloaded_file.pdf')
```

## 🎯 Real-World Project Ideas

1. **Job Board Scraper** - Collect job listings
2. **Real Estate Monitor** - Track property listings
3. **Stock Price Tracker** - Monitor financial data
4. **News Aggregator** - Collect articles from multiple sources
5. **Social Media Analyzer** - Extract public posts
6. **Competitor Analysis** - Monitor competitor websites
7. **SEO Checker** - Analyze website metadata
8. **Availability Checker** - Monitor product stock

## ✅ Success Checklist

Before running on production:
- [ ] Tested with demo sites
- [ ] Verified selectors are correct
- [ ] Added error handling
- [ ] Implemented rate limiting
- [ ] Read target site's ToS
- [ ] Set up proper logging
- [ ] Have data storage plan
- [ ] Tested with different scenarios

## 🤝 Contributing

This is a learning project. Feel free to:
- Modify for your use cases
- Add new demos
- Improve error handling
- Share your experiences

## 📄 License

Educational project for learning purposes. Use responsibly and ethically.

---

**Ready to automate? Start with Demo 1!** 🎭

```bash
python price_tracker.py
# Select: 1
```

**Happy Automating!** 🚀
