import os

from pymongo import MongoClient
from dotenv import load_dotenv # type: ignore


class MongoConnector:
    def __init__(self):
        load_dotenv()
        self.client = MongoClient(os.getenv('MONGODB_URI'))
        self.database = self.client[os.getenv('MONGODB_NAME')]

    def get_collection(self, collection_name):
        return self.database[collection_name]

    def close_connection(self):
        self.client.close()

# Example usage:
if __name__ == "__main__":
    connector = MongoConnector()
    if connector:
        print("connection established...")
        collection = connector.get_collection("site")
        print(collection)

    connector.close_connection()