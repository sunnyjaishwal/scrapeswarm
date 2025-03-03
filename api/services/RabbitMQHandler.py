"""Rabbiit MQ Handler"""
import logging
import json
from pika import BasicProperties

# Configure logging
logging.basicConfig(level=logging.DEBUG)

class RabbitMQHandler:
    ''' Rabbit MQ handler class '''
    def __init__(self, connector, exchange, exchange_type='headers'):
        self.connector = connector
        self.exchange = exchange
        self.exchange_type = exchange_type
        self.channel = self.connector.get_channel()
        self._declare_exchange()

    def _declare_exchange(self):
        self.channel.exchange_declare(
            exchange=self.exchange,
            exchange_type=self.exchange_type,
            auto_delete=True,
            durable=True
        )

    def declare_queue(self, queue_name):
        ''' declare queue to the exchange'''
        self.channel.queue_declare(queue=queue_name, durable=True)

    def bind_queue(self, queue_name, headers, match_type="all"):
        '''Binding the queue'''
        arguments = {
            'x-match': match_type
        }
        arguments.update(headers)
        self.channel.queue_bind(
            queue=queue_name,
            exchange=self.exchange,
            arguments=arguments
        )

    def publish(self, message, headers):
        '''Publish message to the queue'''
        message_body = json.dumps(message).encode('utf-8')
        properties = BasicProperties(
            content_type='application/json',
            headers=headers
        )
        self.channel.basic_publish(
            exchange=self.exchange,
            routing_key='',
            body=message_body,
            properties=properties
        )
