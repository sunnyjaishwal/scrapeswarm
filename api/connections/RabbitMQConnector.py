import pika
import os
from dotenv import load_dotenv

class RabbitMQConnector:
    ''' Message broker connector '''
    def __init__(self):
        load_dotenv()
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
        except pika.exceptions.AMQPConnectionError as e:
            print("connection Error", e)
            

    def get_channel(self):
        ''' get a channel '''
        if self.connection is None or not self.connection.is_open:
            self._connect()
        return self.connection.channel()


    def close_connection(self):
        ''' close the connection '''
        if self.connection and not self.connection.is_closed:
            self.connection.close()
    