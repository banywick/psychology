from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

cluster = MongoClient("mongodb+srv://definit:MongoDefInit2023@cluster0.5tujig4.mongodb.net/?retryWrites=true&w=majority")
db = cluster["psycho_data"]
collection = db["link"]
x = collection.insert_one({"alex": "bell"})
print('good')


