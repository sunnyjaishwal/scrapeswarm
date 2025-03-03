"""This will prepare response for client and push in the cache"""
class BotResponse:
    ''' BotResponse class '''
    def __init__(self, response):
        self.response = response
        self.response_processor()

    def response_processor(self):
        '''Method to prepare bot response'''
