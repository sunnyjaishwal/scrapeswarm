# scrapy_project/scrapy_project/spiders/base_spider.py
import scrapy
from scrapy.exceptions import CloseSpider
from ScrapeSwarm.utility.anti_bot import AntiBot, ProxyManager

class BaseSpider(scrapy.Spider):
    """
    Base spider with common functionalities and anti-bot mechanisms
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.anti_bot = AntiBot()
        self.proxy_manager = ProxyManager()
        
    def start_requests(self):
        """
        Custom start_requests with proxy and user-agent rotation
        """
        for url in self.start_urls:
            proxy = self.proxy_manager.get_random_proxy()
            yield scrapy.Request(
                url, 
                callback=self.parse, 
                meta={
                    'proxy': proxy,
                    'handle_httpstatus_list': [403, 429, 503]
                },
                headers={
                    'User-Agent': self.anti_bot.get_random_user_agent()
                }
            )
    
    def parse(self, response):
        """
        Base parse method with error handling
        """
        if response.status in [403, 429, 503]:
            self.logger.warning(f"Rate limit or blocking detected: {response.url}")
            return None
        
        # Implement base parsing logic or override in child spiders
        raise NotImplementedError("Parsing method must be implemented")
    
    def closed(self, reason):
        """
        Log spider closing details
        """
        self.logger.info(f"Spider closed: {reason}")