import pika

# Define connection parameters
connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

# Declare the exchange
EXCHANGE_NAME = 'AirlineDev'
channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type='headers')

# Declare the queues
queues = ['APIQueue', 'WebQueue', 'BotResponse']

for queue in queues:
    channel.queue_declare(queue=queue)
    channel.queue_bind(exchange=EXCHANGE_NAME, queue=queue)

print(f"Exchange '{EXCHANGE_NAME}' and queues {queues} have been created and bound.")

# Close the connection
connection.close()
