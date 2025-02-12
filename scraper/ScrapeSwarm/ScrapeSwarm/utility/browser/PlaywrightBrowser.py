from playwright.sync_api import sync_playwright

from ScrapeSwarm.utility.browser.BrowserInterface import BrowserInterface
from ScrapeSwarm.utility.browser.data.fingerprint import FingerPrint

import random
import logging
class PlaywrightBrowser(BrowserInterface):
    def __init__(self):
        self.browser = None
        self.page = None

    def get_browser(self):
        return "Playwright"

    def open_url(self, url: str):
        with sync_playwright() as p:
            self.browser = p.chromium.launch(headless=True)
            self.context = self.browser.new_context()
            fingerprint_data = random.choice(FingerPrint.FINGER_PRINT_LIST)
            self.context.set_extra_http_headers({
                'User-Agent':fingerprint_data['userAgent'],    
            })
            self.page = self.context.new_page()
            response = self.page.goto(url)
            print(f"Opened URL: {url} in Playwright")
            print(response.all_headers())
        return response
    
    def open_api_url_post(self, url: str, custom_header: dict):
        with sync_playwright() as p:
            self.browser = p.chromium.launch(headless=True)
            self.context = self.browser.new_context()
            fingerprint_data = random.choice(FingerPrint.FINGER_PRINT_LIST)

            if custom_header:
                self.context.set_extra_http_headers({
                    'User-Agent':custom_header['userAgent'],    
                })
            else:
                self.context.set_extra_http_headers({
                    'User-Agent':fingerprint_data['userAgent'],    
                })

            self.page = self.context.new_page()
            response = self.page.request.post(url)
            print(f"Opened URL: {url} in Playwright")
            print(response.all_headers())
        return response

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
