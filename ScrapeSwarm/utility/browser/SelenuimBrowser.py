from selenium import webdriver
from ScrapeSwarm.utility.browser.BrowserInterface import BrowserInterface

class SeleniumBrowser(BrowserInterface):
    def __init__(self):
        self.driver = None

    def get_browser(self):
        return "Selenium"

    def open_url(self, url: str):
        self.driver = webdriver.Chrome()  # Or any other driver like Firefox, Edge, etc.
        self.driver.get(url)
        print(f"Opened URL: {url} in Selenium")

    def close_browser(self):
        if self.driver:
            self.driver.quit()
            print("Closed Selenium browser")

    def take_screenshot(self, file_path: str):
        if self.driver:
            self.driver.save_screenshot(file_path)
            print(f"Took screenshot and saved to {file_path}")

    def execute_script(self, script: str):
        if self.driver:
            result = self.driver.execute_script(script)
            print(f"Executed script: {script}")
            return result
