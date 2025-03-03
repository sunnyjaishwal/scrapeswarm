""" Rabbit Message Queue Handler for scraper"""
import json
from connections.RabbitMQConnector import RabbitMQConnector

class QueueHandler:
    ''' Class to handle Publishing message to Rabbit MQ'''
    def __init__(self,payload):
        self.payload = payload
        self.connetion = RabbitMQConnector()
        self.chanel = self