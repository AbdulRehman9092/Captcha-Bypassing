const puppeteer = require('puppeteer');

(async () => {
  // Launch a new browser instance
  const browser = await puppeteer.launch({
    headless: false,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  // Open a new page
  const page = await browser.newPage();

  try {
    await page.goto('https://gitlab.com/users/sign_in', { waitUntil: 'networkidle2' });
    await page.waitFor(20000);
    await page.waitForSelector('input[name="user[login]"]', { timeout: 5000 });

  } catch (error) {
    console.error('Error navigating to the page:', error);
  } finally {
    // Close the browser
    await browser.close();
  }
})();
