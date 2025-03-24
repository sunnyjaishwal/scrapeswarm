"""This is response queue handler for scraper response data"""
import json
from pika import BasicProperties
from connections.RabbitMQConnector import RabbitMQConnector

class ResponsePublisher:
    '''This class will handle the the processing and configuration logc of the queue'''
    def __init__(self, ):
        self.exchange:str = 'AirlineDev'
        self.queue:str = 'AirlineResponse'
        self.header:dict = {'x-match': 'all', 'request-type': 'response'}
        self.exchange_type:str = 'headers'
        self.connection = RabbitMQConnector()
        self.channel = self.connection.get_channel()
        self._declare_exchange()

    def _declare_exchange(self):
        self.channel.exchange_declare(
            exchange=self.exchange,
            exchange_type=self.exchange_type,
            auto_delete=True,
            durable=True
        )
        self._declare_queue()

    def _declare_queue(self):
        self.channel.queue_declare(
            queue=self.queue,
            durable=True,
        )
        self._bind_queue()

    def _bind_queue(self):
        arguments = {
            'x-match':'all'
        }
        arguments.update(self.header)
        self.channel.queue_bind(
            queue=self.queue,
            exchange=self.exchange,
            arguments=arguments
        )

    def publish(self, message):
        '''Publish the message in the response queue'''
        message_body = json.dumps(message).encode('utf-8')
        properties = BasicProperties(
            content_type='application/json',
            headers=self.header
        )
        self.channel.basic_publish(
            exchange=self.exchange,
            routing_key='',
            body=message_body,
            properties=properties
        )
        print("One Message pushed to the MQ service!")
