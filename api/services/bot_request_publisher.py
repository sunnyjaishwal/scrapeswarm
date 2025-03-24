import json
import time
from services.Encoder import GenericJSONEncoder
from connections.db_connections import MongoDBConnection


class BotRequestPublisher:
    '''Bot Request Publisher'''

    def __init__(self, handler):
        self.handler = handler
        self.db = MongoDBConnection()

    def _message_processor(self, message, site):
        # Prepare payload for message broker
        payload = {}
        header = site['bot_request_type']
        payload['body'] = message
        payload["siteId"] = site['siteId']
        payload["siteName"] = site['siteName']
        payload["siteUrl"] = site['siteUrl']
        payload['timestamp'] = time.time()
        payload = json.dumps(payload, cls=GenericJSONEncoder)
        return payload, header

    def request_processor(self, message, site):
        '''bot request process and push to rabbit MQ'''
        # Your request processor logic here
        payload, header = self._message_processor(message, site)
        # send request to message broker
        self.handler.publish(payload, header)
        # Save request to the database for analysis
        self.db.get_collection('BotRequest').insert_one(json.loads(payload))
