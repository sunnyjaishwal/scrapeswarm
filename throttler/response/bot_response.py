""" prepare Bot Response"""
import json
from response.encoder import GenericJSONEncoder
from response.queue_publisher import ResponsePublisher
from response.response_cache import CacheProcessor


cache = CacheProcessor()
class BotResponse:
    '''BotResponse'''
    def __init__(self):
        self.payload = {}
        self.response_publisher = ResponsePublisher()

    def _get_site_data(self):
        '''Get the sites data from the database for response processor'''

    def response_processor(self, response, request_payload):
        '''response processor'''
        print("Jai Hind", dir(response))
        if response.status_code == 200:
            self.payload['request'] = request_payload
            self.payload['response'] = response.json()
            self.payload['status'] = 200
            bot_response = json.dumps(self.payload)
            return bot_response
        else:
            self.payload['request'] = request_payload
            self.payload['response'] = str(response.content)
            # self.payload['status'] = str(response['status_code'])
            bot_response = json.dumps(self.payload)

    def send_response(self, response, request_payload):
        '''send error message'''
        # Process the data
        payload = self.response_processor(response, request_payload)
        # Add response to the cache
        # cache.set_response_to_cache(payload)
        # Publish message to the AirlineResponse Queue
        self.response_publisher.publish(payload)
