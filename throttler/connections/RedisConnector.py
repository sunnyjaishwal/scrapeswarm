import redis
import os
from dotenv import load_dotenv # type: ignore


class RedisConnector:
    '''
    RedisConnector class is responsible for creating a connection to the Redis server.
    '''

    def __init__(self):
        load_dotenv()
        self.host = os.getenv('REDIS_HOST')
        self.port = int(os.getenv('REDIS_PORT'))
        self.connection = None

    def get_connection(self):
        self.connection = redis.StrictRedis(host=self.host, port=self.port)
        return self.connection

    def close(self):
        self.connection.close()


# Below code is only required for testing the RedisConnector class
# Not required for microservices
# if __name__ == "__main__":
#     redis_connector = RedisConnector()
#     redis_connector.connect()
#     connection = redis_connector.get_connection()
#     print(connection)
#     redis_connector.close()