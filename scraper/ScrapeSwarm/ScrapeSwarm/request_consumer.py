import pika
import logging

from scraper.ScrapeSwarm.ScrapeSwarm.spiders.ApiBasedScrape.EtihadApiRequest import EtihadApiRequest
# Configure logging
logging.basicConfig(level=logging.INFO)

def execute_crawler(message):
    # Your crawler logic here
    logging.info(f"Executing crawler with message: {message}")

class RabbitMQHandler:
    def __init__(self, host, port, username, password, virtual_host='/'):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.virtual_host = virtual_host
        self.connection = None
        self.channel = None


    def connect(self):
        try:
            credentials = pika.PlainCredentials(self.username, self.password)
            parameters = pika.ConnectionParameters(
                self.host, self.port, self.virtual_host, credentials
            )
            self.connection = pika.BlockingConnection(parameters)
            self.channel = self.connection.channel()
            logging.info('Connected to RabbitMQ')
        except pika.exceptions.AMQPConnectionError as e:
            logging.error(f"Failed to connect to RabbitMQ: {e}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            raise

    def close_connection(self):
        if self.connection and not self.connection.is_closed:
            self.connection.close()
            logging.info('Connection closed')

    def consume_and_execute_crawler(self, queue_name):
        try:
            if not self.connection or self.connection.is_closed:
                self.connect()

            def callback(ch, method, properties, body):
                message = body.decode()
                logging.info(f"Received message: {message}")
                if message.siteName == 'Etihad':
                    # Prepare request for spider
                    # Send request to spider
                    EtihadApiRequest(message)

            self.channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
            logging.info('Waiting for messages. To exit press CTRL+C')
            self.channel.start_consuming()
        except KeyboardInterrupt:
            logging.info('Consumption stopped by user')
        finally:
            self.close_connection()

# Usage example
host = '127.0.0.1'  # Use the IP address of your Docker host
port = 5672  # Default RabbitMQ port
username = 'sunny'
password = 'sunny'
virtual_host = '/'

rabbitmq_handler = RabbitMQHandler(host, port, username, password, virtual_host)

# Declare exchange and queue
exchange_name = 'Airline'
queue_name = 'my_queue'
routing_key = 'my_routing_key'
rabbitmq_handler.declare_exchange_and_queue(exchange_name, queue_name, routing_key)

# Publish a message (for testing)
message = 'Hello, RabbitMQ!'
rabbitmq_handler.publish_message(exchange_name, routing_key, message)

# Consume messages and execute crawler
rabbitmq_handler.consume_and_execute_crawler(queue_name)
