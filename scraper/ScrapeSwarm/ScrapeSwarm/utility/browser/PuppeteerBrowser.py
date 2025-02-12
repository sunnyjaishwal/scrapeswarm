from pyppeteer import launch
from ScrapeSwarm.utility.browser.BrowserInterface import BrowserInterface

class PuppeteerBrowser(BrowserInterface):
    def __init__(self):
        self.browser = None
        self.page = None

    async def get_browser(self):
        return "Puppeteer"

    async def open_url(self, url: str):
        self.browser = await launch(headless=True)
        self.page = await self.browser.newPage()
        await self.page.goto(url)
        print(f"Opened URL: {url} in Puppeteer")

    async def close_browser(self):
        if self.browser:
            await self.browser.close()
            print("Closed Puppeteer browser")

    async def take_screenshot(self, file_path: str):
        if self.page:
            await self.page.screenshot({'path': file_path})
            print(f"Took screenshot and saved to {file_path}")

    async def execute_script(self, script: str):
        if self.page:
            result = await self.page.evaluate(script)
            print(f"Executed script: {script}")
            return result
