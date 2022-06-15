# Captcha-Bypassing

## Overview

This repository contains a collection of scripts demonstrating various methods for browser automation and captcha circumvention. It showcases the use of popular automation libraries like SeleniumBase, Playwright, and Puppeteer, combined with techniques such as anti-detect browsers and AI-powered solving via ChatGPT.

## Scripts

This repository includes the following examples:

### 1. `Seleniumbase Chatgpt.py`

This script demonstrates how to solve image-based captchas by leveraging OpenAI's ChatGPT. It uses the `seleniumbase` library to automate the process of:
1.  Navigating to `chatgpt.com` in an undetectable browser mode.
2.  Uploading a local captcha image file.
3.  Sending a detailed prompt instructing ChatGPT on how to analyze and solve a grid-based captcha.
4.  Waiting for the response and parsing the final numeric answer from the chat.

#### Usage
Before running, ensure you have a captcha image saved locally and update the file path in the script:
```python
# In Seleniumbase Chatgpt.py
sb.choose_file("input[type='file']", r"D:\aa.png") # <-- Change this path
```

Run the script from your terminal:
```bash
python "Seleniumbase Chatgpt.py"
```

### 2. `Playwright.py`

This example uses Python's `playwright` library along with `playwright_stealth` and the [GoLogin](https://gologin.com/) anti-detect browser to create a stealthy browsing session. This method is effective for avoiding detection on websites that employ advanced bot-detection mechanisms.

The script connects to a pre-configured GoLogin browser profile and navigates to the Bing captcha challenge page to demonstrate the stealth setup.

#### Configuration
You need a GoLogin account and an active profile. Update the script with your API token and Profile ID:
```python
# In Playwright.py
gl = GoLogin({
    "token": "YOUR_GOLOGIN_API_TOKEN", # <-- Add your token
    "profile_id": "6725a2affe13bd260cc13bc3", # <-- Change to your profile ID
})
```

#### Usage
Run the script:
```bash
python Playwright.py
```

### 3. `Pupeteer.js` (Puppeteer)

A basic Node.js script using `puppeteer` to launch a browser in non-headless mode. It navigates to the GitLab sign-in page, demonstrating a simple browser automation task.

#### Usage
Run the script using Node.js:
```bash
node Pupeteer.js
```

## Installation

### Prerequisites
- Python 3.x
- Node.js and npm

### Python Dependencies
Install the required Python packages using pip:
```bash
pip install seleniumbase gologin-python playwright playwright-stealth
```
You also need to install the browser binaries for Playwright:
```bash
playwright install
```

### Node.js Dependencies
Install Puppeteer using npm:
```bash
npm install puppeteer
```

## Disclaimer
These scripts are intended for educational and research purposes only. Automating interactions with websites may violate their Terms of Service. Please use this code responsibly and ethically. The user assumes all responsibility for any consequences arising from the use of these scripts.
