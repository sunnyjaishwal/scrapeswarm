import redis
import json

from constants import SITELIST
from services.MessageProcessor import MessageProcessor

class CacheProcessor:
    def __init__(self, host='localhost', port=8084, db=0):
        self.client = redis.Redis(host=host, port=port, db=db, decode_responses=True)

    def get_response_from_cache(self, key):
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