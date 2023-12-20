from pymongo.mongo_client import MongoClient


def connect_mongo_db():
    cluster = MongoClient(
        "mongodb+srv://definit:MongoDefInit2023@cluster0.5tujig4.mongodb.net/?retryWrites=true&w=majority")
    db = cluster["psycho_data"]
    collection = db["link"]
    return collection


def mongo_save(*args, **kwargs):
    connect_mongo_db().insert_one({f"{args}": {f"{id}": f"{kwargs}"}})


def get_one_link():
    connect = connect_mongo_db()
    one_link = connect.find_one({"doc.1": {"$exists": True}})
    return one_link["doc"]['1']



