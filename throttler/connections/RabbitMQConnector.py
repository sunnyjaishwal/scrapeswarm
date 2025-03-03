import pika
import os
import json
from dotenv import load_dotenv # type: ignore
from logger_service import get_logger

class RabbitMQConnector:
    '''Rabbit MQ Connector class '''
    def __init__(self):
        load_dotenv()
        self.logger = get_logger(__name__)
        self.credentials = pika.PlainCredentials(str(os.getenv('RABBITMQ_PASSWORD')), str(os.getenv('RABBITMQ_PASSWORD')))
        self.parameters = pika.ConnectionParameters(
            host = str(os.getenv('RABBITMQ_HOST')),
            port = int(os.getenv('RABBITMQ_PORT')),
            credentials= self.credentials
        )
        self.connection = None
        self._connect()

    def _connect(self):
        try:
            self.connection = pika.BlockingConnection(self.parameters)
            self.logger.info('Connected to RabbitMQ')
        except pika.exceptions.AMQPConnectionError as e:
            self.logger.error("Failed to connect to RabbitMQ: %s", e)
        except Exception as e:
            self.logger.error(f"Unexpected error: {e}")
            

    def get_channel(self):
        if self.connection is None or not self.connection.is_open:
            self._connect()
        return self.connection.channel()


    def close_connection(self):
        if self.connection and not self.connection.is_closed:
            self.connection.close()
            self.logger.info('Connection closed')
    