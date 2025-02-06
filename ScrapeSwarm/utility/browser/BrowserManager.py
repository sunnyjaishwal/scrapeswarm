import asyncio

from ScrapeSwarm.utility.browser.BrowserFactory import BrowserFactory


class BrowserManager:
    def __init__(self, browser_type: str):
        self.browser = BrowserFactory.create_browser(browser_type)

    def get_browser(self):
        return self.browser

# Example usage
# manager = BrowserManager("Playwright")
# browser = manager.get_browser()
# browser.open_url("http://example.com")
# browser.take_screenshot("playwright_screenshot.png")
# browser.execute_script("console.log('Hello from Playwright')")
# browser.close_browser()

# # Selenium example
# manager = BrowserManager("Selenium")
# browser = manager.get_browser()
# browser.open_url("http://example.com")
# browser.take_screenshot("selenium_screenshot.png")
# browser.execute_script("console.log('Hello from Selenium')")
# browser.close_browser()

# # Puppeteer example
# async def puppeteer_example():
#     manager = BrowserManager("Puppeteer")
#     browser = manager.get_browser()
#     await browser.open_url("http://example.com")
#     await browser.take_screenshot("puppeteer_screenshot.png")
#     await browser.execute_script("console.log('Hello from Puppeteer')")
#     await browser.close_browser()

# asyncio.run(puppeteer_example())
