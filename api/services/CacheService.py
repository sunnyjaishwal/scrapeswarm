import json
from api.connections.RedisConnector import RedisConnector

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

    # def get_response_from_cache(self, data):
    #     output = []
    #     for site in SITELIST:
    #         key = f"{data.sourceIATA}:{data.destinationIATA}:{data.departureDate}:{data.site}"
    #         cached_response = self.client.get(key)
    #         if cached_response:
    #             output.append(cached_response)
    #         else:
    #             print("cache miss")
    #             # Send request to MessageProcessor
    #             MessageProcessor().process(data)


    def set_response_to_cache(self, key, value, expiration: int =None):
        '''
        Set cache value to redis
        '''
        self.client.set(key, json.dumps(value), ex=expiration)
        return True



# key = f"{data.sourceIATA}:{data.destinationIATA}:{data.departureDate}:{site}"
# value = {"sourceIATA": data.sourceIATA, "destinationIATA": data.destinationIATA, "departureDate": data.departureDate, "siteId": site}
# cache.set_response_to_cache(key, value, expiration=60)
# output.append ({
#     "details":value,
#     "message": "Response added to cache",
#     "siteId": site
# })
# cache will send the response to the client
# Add value to the Database(mongodb)
