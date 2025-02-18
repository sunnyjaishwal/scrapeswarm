import pika  # type: ignore
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

class RabbitMQHandler:
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.connection = None
        self.channel = None

    def connect(self):
        try:
            credentials = pika.PlainCredentials(self.username, self.password)
            parameters = pika.ConnectionParameters(self.host, self.port, '/', credentials)
            self.connection = pika.BlockingConnection(parameters)
            self.channel = self.connection.channel()
            logging.info('Connected to RabbitMQ')
        except pika.exceptions.AMQPConnectionError as e:
            logging.error(f"Failed to connect to RabbitMQ: {e}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            raise

    def close_connection(self):
        if self.connection and not self.connection.is_closed:
            self.connection.close()
            logging.info('Connection closed')

    def send_message_to_exchange(self, payload, exchange_name, routing_key):
        print("Hitting send_message_to_exchange")
        try:
            if not self.connection or self.connection.is_closed:
                self.connect()

            self.channel.exchange_declare(exchange=exchange_name, exchange_type='fanout', durable=True)
            self.channel.basic_publish(exchange=exchange_name, routing_key=routing_key, body=payload)
            logging.info(f"Message sent to exchange: {exchange_name} with routing key: {routing_key}")
        except pika.exceptions.AMQPConnectionError as e:
            print(f"Failed to send message to exchange: {e}")
