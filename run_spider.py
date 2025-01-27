# run_spider.py
import os
import sys
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from ScrapeSwarm.spiders.httpbin import httpbin_spider

def run_spider(spider_name, env='dev'):
    """
    Run a specific spider with environment-specific settings
    """
    # Dynamically load settings based on environment
    settings_module = f'scrapy_project.settings.{env}'
    os.environ['SCRAPY_SETTINGS_MODULE'] = settings_module
    
    # Load settings
    settings = Settings()
    settings.setmodule(settings_module)
    
    # Find and run the spider
    spider_cls = httpbin_spider.get(spider_name)
    if not spider_cls:
        print(f"Spider {spider_name} not found!")
        sys.exit(1)
    
    # Create crawler process
    process = CrawlerProcess(settings)
    process.crawl(spider_cls)
    process.start()

if __name__ == '__main__':
    # Example usage
    run_spider('example_spider', env='dev')