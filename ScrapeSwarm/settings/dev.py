from ScrapeSwarm.settings.base import *

# Development-specific overrides
DEBUG = True
DOWNLOAD_DELAY = 0.5
LOG_LEVEL = 'DEBUG'

# Dev-specific configurations
PROXY_POOL_ENABLED = False
ROTATING_PROXY_ENABLED = False

USER_AGENT = "ScrapeSwarm - Development Server"
# Database or external service configurations
DATABASE_URL = 'postgresql://localhost/dev_database'
