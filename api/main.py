import json
import time
from dotenv import load_dotenv  # type: ignore
from fastapi import FastAPI  # type: ignore
from models.InputData import InputData
from services.cache_service import CacheProcessor
from services.RabbitMQHandler import RabbitMQHandler
from services.bot_request_publisher import BotRequestPublisher
from connections.RabbitMQConnector import RabbitMQConnector
from logger_service import get_logger

load_dotenv()
logger = get_logger(__name__)

app = FastAPI()

# Middleware configuration here

# Create and reuse a RabbitMQConnector instance with connection details.
connector = RabbitMQConnector()
# Create RabbitMQHandler instance with connection and exchange name
handler = RabbitMQHandler(connector, 'AirlineDev')

# Declare the Queue and bind them to the exchange using the handler
queues = {
    'WebQueue': {'x-match': 'all', 'request-type': 'WEB'},
    'APIQueue': {'x-match': 'all', 'request-type': 'API'},
    'AirlineResponse': {'x-match': 'all', 'request-type': 'RESPONSE'}
}

for queue, header in queues.items():
    handler.declare_queue(queue)
    handler.bind_queue(queue_name=queue, headers=header)

cache = CacheProcessor()
bot_request = BotRequestPublisher(handler)

# Read SiteData from a json file (later will be replaced with a database)
site_data = {}
with open("models/Site.json", "r", encoding="utf-8") as file:
    site_data = json.loads(file.read())

@app.post("/send_requests")
async def send_requests(message: InputData):
    '''
    SendAPI receives the request payload from the client and sends a response back to the client.
    '''
    logger.info("Received request")
    output = []
    for site in site_data:
        parameters = message.parameters
        key = f"{parameters.sourceIata}:{parameters.destinationIata}:{parameters.departureDate}:{site['siteId']}"
        response = cache.get_response_from_cache(key)
        if response:
            output.append({
                "details": response,
                "message": "Response retrieved from cache",
                "siteId": site['siteId'],
            })
        else:
            logger.info("Cache miss")
            # Prepare for BotRequest
            bot_request.request_processor(message, site)
            # Poll to check if the response is available in the cache
            max_wait_time = 15  # Maximum wait time in seconds
            poll_interval = 0.5  # Interval between checks in seconds
            start_time = time.time()
            response = None
            while time.time() - start_time < max_wait_time:
                print(key)
                response = cache.get_response_from_cache(key)
                print("Polling response and getting ", response)
                if response:
                    break
                time.sleep(poll_interval)

            if response:
                output.append({
                    "details": response,
                    "message": "Response from cache",
                    "site": site,
                })
            else:
                output.append({
                    "details": None,
                    "message": "Response not found in cache within the maximum wait time",
                    "site": site,
                })

    return output
