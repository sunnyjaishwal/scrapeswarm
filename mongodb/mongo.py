from pymongo import MongoClient

"docker pull mongo"
"docker run -d --name mongodb-container -p 27017:27017 mongo"

# Connect to the MongoDB container
client = MongoClient("mongodb://localhost:27017/")
# Get the database names
#databases = client.list_database_names()
db = client['scrapeswarmdb-dev']
collections = db.list_collection_names()
print("Collections:", collections)

# Iterate through each database and get collection details
# for db_name in databases:
#     db = client[db_name]
#     collections = db.list_collection_names()
#     print(f"Database: {db_name}")
#     print("Collections:", collections)