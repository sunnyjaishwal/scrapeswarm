import logging
from ScrapeSwarm.utility.logger_config import setup_logging

class LoggingMiddleware:
    def __init__(self):
        setup_logging()
        self.logger = logging.getLogger(__name__)

    def process_spider_input(self, response, spider):
        self.logger.debug(f"Processing spider input for {spider.name}")
        return None

    def process_spider_output(self, response, result, spider):
        self.logger.debug(f"Processing spider output for {spider.name}")
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        self.logger.debug(f"Processing spider exception for {spider.name}")
        pass

    def process_start_requests(self, start_requests, spider):
        self.logger.debug(f"Processing start requests for {spider.name}")
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        self.logger.debug(f"Spider opened {spider.name}")
