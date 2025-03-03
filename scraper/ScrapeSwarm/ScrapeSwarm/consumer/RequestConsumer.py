"""
This module will consume the request from the RabbitMQ.
It will be based on MultiThreading/or processing to read form both 
(APIRequest and WebRequest) the queue.
This will then strat the spider from here.
"""

import threading
from connections.RabbitMQConnector import RabbitMQConnector
class RequestConsumer:
    '''
    Consumer class
    '''
    def __init__(self):
        self.connector = RabbitMQConnector()
        self.channel = None

    def _get_queues(self):
        queues : dict
        return []

    def consume_request(self):
        '''
        consume request from MQ based on queues
        ''' 

    def crawler_executer(self):
        '''
        The list of spider and run with execute method
        '''

    def _execute(self, spider):
        '''
        Run the spider and push the response to BotResponse
        '''
