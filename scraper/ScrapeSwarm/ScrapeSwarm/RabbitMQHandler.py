import pika # type: ignore
import logging
import json
from spiders.ApiBasedScrape.EtihadApiRequest import EtihadApiRequest
from spiders.ApiBasedScrape.DeltaApiRequest import DeltaApiRequest
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

    def consume_and_execute_crawler(self, exchange_name):
        try:
            if not self.connection or self.connection.is_closed:
                self.connect()

            def callback(ch, method, properties, body):
                message = json.loads(body.decode('utf-8'))
                # logging.info(f"Received message: {message['body']}")
                print(message["siteName"])
                if message["siteName"] == 'Etihad':
                    print("Etihad Bot Request started...")
                    EtihadApiRequest(message).send_request()
                elif message["siteName"] == 'Delta':
                    print("Delta Bot Request started...")
                    DeltaApiRequest(message).send_request()

            queue_name = ['Etihad','Delta'] # same as siteName
            for queue in queue_name:
                self.channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)
                logging.info(f"Consuming messages from queue: {queue_name}")
                self.channel.start_consuming()
        except KeyboardInterrupt:
            logging.info('Consumption stopped by user')


    def send_message_to_exchange(self, message, exchange_name, routing_key):
        try:
            if not self.connection or self.connection.is_closed:
                self.connect()
            self.channel.exchange_declare(exchange=exchange_name, exchange_type='direct', durable=True)
            self.channel.basic_publish(exchange=exchange_name, routing_key=routing_key, body=message)
            logging.info(f"Sent message to exchange: {exchange_name} with routing key: {routing_key}")
        except Exception as e:
            logging.error(f"Failed to send message to exchange: {e}")
            raise

if __name__ == '__main__':
    host = 'localhost'  # Use the IP address of your Docker host
    port = 5672  # Default RabbitMQ port
    username = 'sunny'
    password = 'sunny'
    virtual_host = '/'
    exchange_name = 'AirlineIn'
    rabbitmq_handler = RabbitMQHandler(host, port, username, password, virtual_host)
    rabbitmq_handler.consume_and_execute_crawler(exchange_name)
