import json

from utility.GenericJSONEncoder import GenericJSONEncoder

class BotResponse:
    def __init__(self):
        self.payload = {}
        self.host = 'localhost'
        self.port = 5672
        self.username = 'sunny'
        self.password = 'sunny'

    def response_processor(self, data, message):
        self.payload['request'] = message
        self.payload['response'] = data
        self.payload = json.dumps(self.payload, cls=GenericJSONEncoder)
        self.send_success_response(self.payload)

    def send_error_response(self, data, message):
        from RabbitMQHandler import RabbitMQHandler
        self.payload['request'] = message
        self.payload['error'] = data
        self.payload = json.dumps(self.payload, cls=GenericJSONEncoder)
        self.rabbitmq_handler = RabbitMQHandler(self.host, self.port, self.username, self.password)
        self.rabbitmq_handler.send_message_to_exchange(self.payload, "Airline", "AirlineOut")

    def send_success_response(self, data):
        from RabbitMQHandler import RabbitMQHandler
        # Your request processor logic here
        payload = self.message_processor(data)
        # send request to message broker
        self.rabbitmq_handler = RabbitMQHandler(self.host, self.port, self.username, self.password)
        self.rabbitmq_handler.send_message_to_exchange(payload, "Airline", "AirlineOut")
       

