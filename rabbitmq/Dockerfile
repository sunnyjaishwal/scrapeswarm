# Use the official RabbitMQ image from the Docker Hub
FROM rabbitmq:3-management

# Expose the default RabbitMQ port
EXPOSE 5672

# Expose the RabbitMQ management plugin port
EXPOSE 15672

# Define environment variables
ENV RABBITMQ_DEFAULT_USER=sunny
ENV RABBITMQ_DEFAULT_PASS=sunny

# Start RabbitMQ server
CMD ["rabbitmq-server"]