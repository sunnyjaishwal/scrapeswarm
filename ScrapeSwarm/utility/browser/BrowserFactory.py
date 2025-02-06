from ScrapeSwarm.utility.browser.BrowserInterface import BrowserInterface
from ScrapeSwarm.utility.browser.PlaywrightBrowser import PlaywrightBrowser
from ScrapeSwarm.utility.browser.SelenuimBrowser import SeleniumBrowser
from ScrapeSwarm.utility.browser.PuppeteerBrowser import PuppeteerBrowser


class BrowserFactory:
    @staticmethod
    def create_browser(browser_type: str) -> BrowserInterface:
        if browser_type == "Playwright":
            return PlaywrightBrowser()
        elif browser_type == "Selenium":
            return SeleniumBrowser()
        elif browser_type == "Puppeteer":
            return PuppeteerBrowser()
        else:
            raise ValueError("Unsupported browser type")
