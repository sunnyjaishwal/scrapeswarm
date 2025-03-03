"""Bot Response"""
import json
from response.encoder import GenericJSONEncoder
from response.queue_handler import QueueHandler


class BotResponse:
    '''BotResponse'''
    def __init__(self):
        self.payload = {}
        self.queue_handler = QueueHandler()

    def _get_site_data(self):
        '''Get the sites data from the database for response processor'''

    def response_processor(self, data):
        '''response processor'''
        self.payload['response'] = data.json()
        self.payload['status'] = str(data.status_code)
        if data.status_code == 200:
            self.payload['success']= True # False if error
        else:
            self.payload['success']= False
        print(self.payload)
        bot_response = json.dumps(self.payload)
        return bot_response

    def send_response(self, data):
        '''send error message'''
        # Process the data
        payload = self.response_processor(data)
        self.queue_handler.publish(payload)
