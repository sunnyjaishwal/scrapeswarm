"""Bot(Scraper) Response Consumer"""

import logging
import json
from connections.RabbitMQConnector import RabbitMQConnector
from services.cache_service import CacheProcessor



# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ResponseConsumer:
    '''Response consumer class'''
    def __init__(self):
        self.connection = RabbitMQConnector()
        self.channel = self.connection.get_channel()
        self.cache_processor = CacheProcessor()

    def get_queues(self):
        ''' This method will get queue name from the site table'''
        # Assuming the queue name is static, otherwise, 
        # implement dynamic fetching from the site table 
        return 'AirlineResponse'

    def callback(self, ch, method, properties, body):
        ''' callback method for RabbitMQ'''
        try:
            message = json.loads(body)
            # If message is a JSON-encoded string, decode it again
            if isinstance(message, str):
                data = json.loads(message)
                parameters = data['request']['body']['parameters']
                key = f"{parameters['sourceIata']}:{parameters['destinationIata']}:{parameters['departureDate']}:{data['request']['siteId']}"
                self.cache_processor.set_response_to_cache(key=key, value=data)
                print("Data set to cache")
                # Add this in Cache with unique Key
        except json.JSONDecodeError as e:
            logger.error("Failed to decode message: %s, error: %s", body, e)
        except Exception as e:
            logger.error("Exception occurred: %s", e, exc_info=True)


    def consume_and_process(self):
        '''consume and process the message'''
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(
            queue=self.get_queues(),
            on_message_callback=self.callback,
            auto_ack=True  # Set auto_ack to False to manually acknowledge after processing
        )
        logger.info("[X] Started consuming")
        self.channel.start_consuming()


if __name__ == '__main__':
    try:
        consumer = ResponseConsumer()
        consumer.consume_and_process()
    except KeyboardInterrupt:
        logger.info("Stopped consuming")
