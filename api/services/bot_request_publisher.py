import json
from services.RabbitMQHandler import RabbitMQHandler
from services.Encoder import GenericJSONEncoder
from services.RabbitMQHandler import RabbitMQHandler


class BotRequestPublisher(RabbitMQHandler):

    def __init__(self, handler):
        self.handler = handler

    
    def _message_processor(self, message, site):
        # Prepare payload for message broker
        payload = {}
        header = site['bot_request_type']
        payload['body'] = message
        payload["siteId"] = site['siteId']
        payload["siteName"] = site['siteName']
        payload["siteUrl"] = site['siteUrl']
        payload = json.dumps(payload, cls=GenericJSONEncoder)
        return payload, header

    def request_processor(self, message, site):
        # Your request processor logic here
        payload, header = self._message_processor(message, site)
        # send request to message broker
        self.handler.publish(payload, header)
