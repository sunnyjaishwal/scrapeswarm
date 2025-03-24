"""This module will process cache for bot response """
import json
from connections.RedisConnector import RedisConnector

class CacheProcessor:
    ''' cache processor for bot response '''
    def __init__(self):
        self.client = RedisConnector().get_connection()

    def set_response_to_cache(self, message, expiration: int =30):
        '''
        Set cache value to redis
        '''
        # If message is a JSON-encoded string, decode it again
        if isinstance(message, str):
            message = json.loads(message)
        parameters = message['request']['body']['parameters']
        key = f"{parameters['sourceIata']}:{parameters['destinationIata']}:{parameters['departureDate']}:{message['request']['siteId']}"
        print(message['request']['siteId'])
        print("Data set to cache", key)
        self.client.set(key, json.dumps(message), ex=expiration)
        return True
