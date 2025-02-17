class MessageProcessor:

    def process(self, data):
        # get the data for MQ processing
        # rabbitmq_handler.send_message_to_exchange(data.json(), "Airline", site)
        # print("Request sent to message broker")
        # message broker will send the request to the spider
        # spider will send the response to the message broker
        # message broker will send the response to the cache
        payload = {
            'body': data,
            'exchange': 'Airline',
            'routing_key': 'site'
        }
        # Prepare Request for spider to execute using BotRequest

        # Send the RequestData to the message broker

        return self.data