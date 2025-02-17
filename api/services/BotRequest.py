from services.QueueService import RabbitMQHandler

class BotRequest:

    def __init__(self):
        self.host = 'localhost'
        self.port = 5672
        self.username = 'sunny'
        self.password = 'sunny'
    
    def message_processor(self, data, site):
        # Prepare payload for message broker
        payload = {}
        routing_key = f"{site['siteName']}"
        payload['body'] = data
        payload["siteId"] = site['siteId']
        payload["siteName"] = routing_key
        payload["siteUrl"] = site['siteUrl']

        return str(payload), routing_key

    def request_processor(self, data, site):
        # Your request processor logic here
        payload, routing_key = self.message_processor(data, site)
        # send request to message broker
        self.rabbitmq_handler = RabbitMQHandler(self.host, self.port, self.username, self.password)
        self.rabbitmq_handler.send_message_to_exchange(payload, "Airline", routing_key)
