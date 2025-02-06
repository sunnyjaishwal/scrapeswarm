import scrapy
from ScrapeSwarm.utility.browser.BrowserManager import BrowserManager
class HttpBinSpider(scrapy.Spider):
    name = "httpbin"
    start_urls = ['https://httpbin.org/']
    browser = BrowserManager("Puppeteer").get_browser()


    def parse(self, response):
        self.log("Accessed httpbin.org successfully!")
        
        # Extract some basic information from the response
        url = response.url
        headers = response.headers
        body = response.text

        # Print or log the extracted information
        self.log(f"URL: {url}")
        self.log(f"Headers: {headers}")
        self.log(f"Body: {body[:100]}...")  # Display the first 100 characters of the body

        # Use a sample API endpoint for testing purposes
        sample_endpoint = 'https://httpbin.org/get'
        yield scrapy.Request(sample_endpoint, callback=self.parse_endpoint)

    def parse_endpoint(self, response):
        self.log("Accessed httpbin.org/get successfully!")
        
        data = response.json()
        
        # Print or log the response data
        self.log(f"Response Data: {data}")
