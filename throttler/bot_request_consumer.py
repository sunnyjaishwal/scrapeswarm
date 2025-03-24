"""API request consumer on service for further processing"""

import json
import logging
from connections.RabbitMQConnector import RabbitMQConnector
from ApiBasedScraper.EtihadScraper import EtihadScraper
from ApiBasedScraper.DeltaScraper import DeltaScraper

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BotRequestConsumer:
    ''' Rabbit MQ consumer'''
    def __init__(self):
        self.connection = RabbitMQConnector()
        self.channel = self.connection.get_channel()

    def get_queues(self):
        ''' This method will get queue name from the site table'''
        # Assuming the queue name is static, otherwise, 
        # implement dynamic fetching from the site table 
        return 'APIQueue'

    def callback(self, ch, method, properties, body):
        ''' callback method for RabbitMQ'''
        try:
            message = json.loads(body)
            # If message is a JSON-encoded string, decode it again
            if isinstance(message, str):
                message = json.loads(message)

            site_name = message.get("siteName")
            print("One request received for ", site_name)
            if site_name == 'Etihad':
                EtihadScraper(message).send_request()
            elif site_name == 'Delta':
                DeltaScraper(message).send_request()
            else:
                logger.warning("Unknown site name: %s", site_name)
        except json.JSONDecodeError as e:
            logger.error("Failed to decode message: %s, error: %s", body, e)
        except Exception as e:
            logger.error("Exception occurred: %s", e, exc_info=True)
        finally:
            ch.basic_ack(delivery_tag=method.delivery_tag)

    def consume_and_process(self):
        '''consume and process the message'''
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(
            queue=self.get_queues(),
            on_message_callback=self.callback,
            auto_ack=False  # Set auto_ack to False to manually acknowledge after processing
        )
        logger.info("[X] Started consuming")
        self.channel.start_consuming()

if __name__ == '__main__':
    try:
        consumer = BotRequestConsumer()
        consumer.consume_and_process()
    except KeyboardInterrupt:
        logger.info("Stopped consuming")
