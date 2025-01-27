from ScrapeSwarm.settings.base import *

# Development specific settings
CONCURRENT_REQUESTS = 8
DOWNLOAD_DELAY = 1
AUTOTHROTTLE_ENABLED = True
USER_AGENT = "ScrapeSwarm - UAT Server"
HTTPCACHE_IGNORE_HTTP_CODES = []
# Enable and configure HTTP caching (disabled by default)

HTTPCACHE_ENABLED = False