# 🚀 Quick Start Guide - Playwright Automation

## 📥 Installation (3 Steps)

### Step 1: Install Python Packages

Open Command Prompt or Terminal in the project folder:

```bash
cd Assignment2_Playwright
pip install -r requirements.txt
```

### Step 2: Install Playwright Browsers

```bash
playwright install
(OR)
playwright install chromium
```

---

### Launch the Application

```bash
python demo_playwright.py
```

### You'll see this menu:

```
╔══════════════════════════════════════════════════════════╗
║       Playwright Web Automation & Scraping Demo          ║
╚══════════════════════════════════════════════════════════╝

Select a demo to run:
1. Basic Navigation & Screenshots
2. Form Interaction & Search
3. Data Extraction & Web Scraping

Enter your choice (1-3):
```

### First-Time Users: Start with Demo 1

Type `1` and press Enter.

**What happens:**
1. Browser window opens
2. Navigates to example.com
3. Takes a screenshot
4. Shows page information
5. Browser closes automatically

**Output location:**
- Screenshot: `screenshots/example_page.png`

---

## 📚 Demo Walkthrough

### Demo 1: Basic Navigation (Easiest)

**Purpose:** Learn fundamental Playwright operations

**What it does:**
- Opens a browser
- Navigates to example.com
- Captures the page title
- Takes a screenshot
- Shows page content length

**Perfect for:** Understanding basics

**Runtime:** 10 seconds

---

### Demo 2: Form Interaction

**Purpose:** Learn how to interact with web forms

**What it does:**
- Opens DuckDuckGo search engine
- Types a search query
- Submits the form
- Captures search results
- Takes a screenshot

**Perfect for:** Form automation learning

**Runtime:** 15 seconds

---

### Demo 3: Data Extraction

**Purpose:** Learn web scraping basics

**What it does:**
- Visits quotes.toscrape.com
- Extracts quotes and authors
- Saves data to Excel
- Creates `quotes_data.xlsx`

**Perfect for:** Learning data scraping

**Runtime:** 20 seconds

**Output:**
- Excel file with 5 quotes
- Located: `quotes_data.xlsx`

---
