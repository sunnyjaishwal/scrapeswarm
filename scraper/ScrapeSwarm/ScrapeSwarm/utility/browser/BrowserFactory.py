from ScrapeSwarm.utility.browser.BrowserInterface import BrowserInterface
from ScrapeSwarm.utility.browser.PlaywrightBrowser import PlaywrightBrowser
from ScrapeSwarm.utility.browser.SelenuimBrowser import SeleniumBrowser
from ScrapeSwarm.utility.browser.PuppeteerBrowser import PuppeteerBrowser


class BrowserFactory:
    """
    BrowserFactory is a factory class responsible for creating instances of different browser automation interfaces.

    Methods
    -------
    create_browser(browser_type: str) -> BrowserInterface
        Creates and returns an instance of a browser automation interface based on the specified browser type.
        Supported browser types are "Playwright", "Selenium", and "Puppeteer".

        Parameters
        ----------
        browser_type : str
            The type of browser automation interface to create. Must be one of "Playwright", "Selenium", or "Puppeteer".

        Returns
        -------
        BrowserInterface
            An instance of the specified browser automation interface.

        Raises
        ------
        ValueError
            If the specified browser type is not supported.
    """
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
