import pika # type: ignore

# Define connection parameters
connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

# Declare the exchange
exchange_name = 'Airline'
channel.exchange_declare(exchange=exchange_name, exchange_type='direct')

# Declare the queues
queues = ['etihad', 'delta', 'american', 'united']

for queue in queues:
    channel.queue_declare(queue=queue)
    channel.queue_bind(exchange=exchange_name, queue=queue)

print(f"Exchange '{exchange_name}' and queues {queues} have been created and bound.")

# Close the connection
connection.close()