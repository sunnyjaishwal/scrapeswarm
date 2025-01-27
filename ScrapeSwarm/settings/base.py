# scrapy_project/scrapy_project/settings/base.py
import os

# Base settings applicable to all environments
BOT_NAME = 'ScrapeSwarm'

SPIDER_MODULES = ['ScrapeSwarm.spiders']
NEWSPIDER_MODULE = 'ScrapeSwarm.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests
CONCURRENT_REQUESTS = 16

# Download delays
DOWNLOAD_DELAY = 1.5

# Retry configuration
RETRY_ENABLED = True
RETRY_TIMES = 3

# Logging configuration
LOG_LEVEL = 'INFO'

# Telnet console configuration
TELNETCONSOLE_ENABLED = False

# Default item pipeline
ITEM_PIPELINES = {
    # Enable the SQLite pipeline
    'ScrapeSwarm.pipelines.SQLitePipeline': 300,
}

# Downloader middlewares
DOWNLOADER_MIDDLEWARES = {
    'ScrapeSwarm.middlewares.middlewares.ScrapeSwarmDownloaderMiddleware': 543,
}

# Spider middlewares
SPIDER_MIDDLEWARES = {
    'ScrapeSwarm.middlewares.logging_middleware.LoggingMiddleware': 543,
    'ScrapeSwarm.middlewares.middlewares.ScrapeSwarmSpiderMiddleware': 543,
}
