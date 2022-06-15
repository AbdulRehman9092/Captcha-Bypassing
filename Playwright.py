import asyncio
from playwright.async_api import async_playwright
from playwright_stealth import stealth_sync
from gologin import GoLogin

async def main():
    gl = GoLogin({
        "token": "YOUR_GOLOGIN_API_TOKEN",
        "profile_id": "6725a2affe13bd260cc13bc3",
    })

    debugger_address = gl.start()

    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp(f"http://{debugger_address}")
        default_context = browser.contexts[0]
        page = default_context.pages[0]
        stealth_sync(page)
        await page.goto('https://www.bing.com/turing/captcha/challenge')
        # Wait for 30 seconds to observe the page
        # You can perform any task here if needed
        await asyncio.sleep(30)
        await page.close()
    gl.stop()
asyncio.run(main())
