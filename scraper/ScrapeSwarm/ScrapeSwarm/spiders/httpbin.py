import scrapy
from ScrapeSwarm.utility.browser.BrowserManager import BrowserManager

class HttpBinSpider(scrapy.Spider):
    name = "httpbin"
    def start_requests(self):
        browser = BrowserManager("Playwright").get_browser()
        # Use a sample API endpoint for testing purposes
        sample_endpoint = 'https://httpbin.org/get'
        
        # Use the browser object to open the URL and handle the response
        response = browser.open_url(sample_endpoint)
        yield self.parse(response)
        
    def parse(self, response):
        self.log("Accessed httpbin.org successfully!")
        self.log(f"URL: {response.url}")
        self.log(f"Headers: {response.headers}")
        self.log(f"Body: {response.text}")  # Display the first 100 characters of the body
