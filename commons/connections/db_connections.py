"""
This module contains the connection classes for different databases.
"""

from pymongo import MongoClient

class MongoDBConnection:
    '''
    Connetcion class for MongoDB
    '''
    def __init__(
            self,
            host='localhost',
            port=27017,
            database_name='scrapeswarmdb-dev',
            username=None,
            password=None
        ):
        self.host = host
        self.port = port
        self.database_name = database_name
        self.username = username
        self.password = password
        self.client = None
        self.db = None

    def connect(self):
        '''
        Connect to the MongoDB
        '''
        if self.username and self.password:
            uri = f"mongodb://{self.username}:{self.password}@{self.host}:{self.port}/{self.database_name}"
        else:
            uri = f"mongodb://{self.host}:{self.port}/{self.database_name}"
        self.client = MongoClient(uri)
        self.db = self.client[self.database_name]
        return self.db

    def disconnect(self):
        '''
        Disconnect from the MongoDB
        '''
        if self.client:
            self.client.close()
            self.client = None
            self.db = None

    def get_collection(self, collection_name):
        '''
        Get the collection
        '''
        if not self.db:
            self.connect()
        return self.db[collection_name]

# if __name__ == "__main__":
#     # Connect to the MongoDB container
#     mongo = MongoDBConnection()
#     collections = mongo.get_collection('BotResponse')
#     documents = collections.find()
#     for doc in documents:
#         print(doc)
#     mongo.disconnect()
