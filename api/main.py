import json

from typing import Union
from constants import SITELIST
from fastapi import FastAPI # type: ignore

from models.InputData import InputData
from services.CacheService import CacheProcessor
from services.QueueService import RabbitMQHandler
from services.BotRequest import BotRequest

app = FastAPI()

# Usage example
host = 'localhost'
port = 5672  # default RabbitMQ port
username = 'sunny'
password = 'sunny'
rabbitmq_handler = RabbitMQHandler(host, port, username, password)
cache = CacheProcessor()
BotRequest = BotRequest()

# Read SiteData from a json file(later will be rpelaced with database)
SiteData = {}
with open("models/Site.json", "r") as file:
    SiteData = json.loads(file.read())


@app.post("/send_request")
async def send_request(data: InputData):
    output = []
    for site in SiteData:
        parameters = data.parameters
        key = f"{parameters.sourceIata}:{parameters.destinationIata}:{parameters.departureDate}:{site['siteId']}"
        response = cache.get_response_from_cache(key)
        if response:
            output.append ({
                "details":response,
                "message": "Response retrieved from cache",
                "siteId": site['siteId'],
            })
        else:
            print("cache miss")
            # Prepare for BotRequest
            BotRequest.request_processor(data, site)
            # Poll to check if the response is available in the cache
            response = cache.get_response_from_cache(key)
            output.append ({
                "details":response,
                "message": "Response added to cache",
                "site": site,
            })

    return output
