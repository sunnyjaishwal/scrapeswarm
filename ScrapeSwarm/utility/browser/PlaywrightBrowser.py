from playwright.sync_api import sync_playwright

from ScrapeSwarm.utility.browser.BrowserInterface import BrowserInterface

class PlaywrightBrowser(BrowserInterface):
    def __init__(self):
        self.browser = None
        self.page = None

    def get_browser(self):
        return "Playwright"

    def open_url(self, url: str):
        with sync_playwright() as p:
            self.browser = p.chromium.launch(headless=True)
            self.page = self.browser.new_page()
            self.page.goto(url)
            print(f"Opened URL: {url} in Playwright")

    def close_browser(self):
        if self.browser:
            self.browser.close()
            print("Closed Playwright browser")

    def take_screenshot(self, file_path: str):
        if self.page:
            self.page.screenshot(path=file_path)
            print(f"Took screenshot and saved to {file_path}")

    def execute_script(self, script: str):
        if self.page:
            result = self.page.evaluate(script)
            print(f"Executed script: {script}")
            return result
