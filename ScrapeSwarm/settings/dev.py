from ScrapeSwarm.settings.base import *

# Development-specific overrides
DEBUG = True
DOWNLOAD_DELAY = 0.5
LOG_LEVEL = 'DEBUG'

# Dev-specific configurations
PROXY_POOL_ENABLED = False
ROTATING_PROXY_ENABLED = False


print("*" * 50)
print("*" * 50)
print("*" * 50)
print("*" * 50)
print("ScrapeSwarm - Development Server")
print("*" * 50)
print("*" * 50)
print("*" * 50)
# Database or external service configurations
DATABASE_URL = 'postgresql://localhost/dev_database'
