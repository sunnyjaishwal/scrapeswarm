"""Bot(Scraper) Response Consumer"""

from connections.RabbitMQConnector import RabbitMQConnector


class ResponseConsumer:
    '''Response consumer class'''
    def __init__(self):
        self.connection = RabbitMQConnector()
        self.chanel = self.connection.get_channel()

    def consume_and_process(self):
        pass