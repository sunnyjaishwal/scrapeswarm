# Docker setup and Configurations

## Build Dockerfile

-> docker build -t production-redis .

## Run Docker Image

-> docker run -d --name production-redis-server -p 6379:6379 -v redis-data:/data production-redis
