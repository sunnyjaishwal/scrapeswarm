"""Cache Service Module"""
import json
from connections.RedisConnector import RedisConnector

class CacheProcessor:
    '''
    CacheProcessor is a class that handles cache related processing
    '''
    def __init__(self):
        self.client = RedisConnector().get_connection()

    def get_response_from_cache(self, key):
        '''
        Get response from cache server
        '''
        cached_data = self.client.get(key)
        if cached_data:
            return json.loads(cached_data)
        return False

    def set_response_to_cache(self, key, value, expiration: int =None):
        '''
        Set cache value to redis
        '''
        self.client.set(key, json.dumps(value), ex=expiration)
        return True
