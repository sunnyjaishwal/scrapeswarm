import json
from dotenv import load_dotenv # type: ignore
from fastapi import FastAPI # type: ignore
from models.InputData import InputData
from services.cache_service import CacheProcessor
from services.RabbitMQHandler import RabbitMQHandler
from services.bot_request_publisher import BotRequestPublisher
from connections.RabbitMQConnector import RabbitMQConnector


from logger_service import get_logger

load_dotenv()
Logger = get_logger(__name__)

app = FastAPI()

# Middleware configuration here

# Create a RabbitMQConnector Instance with connection details.
connector = RabbitMQConnector()
# Create RabbitMQHandler instance with connection and exchange name
handler = RabbitMQHandler(connector,'AirlineDev')
# Declare the Queue and bind them to the exchange using the handler
queues = {
        'WebQueue': {'x-match': 'all', 'request-type': 'WEB'},
        'APIQueue': {'x-match': 'all', 'request-type': 'API'}
    }

for queue, header in queues.items():
    handler.declare_queue(queue)
    handler.bind_queue(queue_name=queue, headers=header)

cache = CacheProcessor()
BotRequest = BotRequestPublisher(handler)

# Read SiteData from a json file(later will be rpelaced with database)
SiteData = {}
with open("models/Site.json", "r", encoding="utf-8") as file:
    SiteData = json.loads(file.read())

@app.post("/send_request")
async def send_request(message: InputData):
    '''
    SendAPI receives the request payload from the client and sends response back to the client.
    '''
    # Logger.info(f"Received request from {data.clientIp} to {data.url}")
    output = []
    for site in SiteData:
        parameters = message.parameters
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
            BotRequest.request_processor(message, site)
            # Poll to check if the response is available in the cache
            response = cache.get_response_from_cache(key)
            output.append ({
                "details":response,
                "message": "Response from cache",
                "site": site,
            })

    return output
