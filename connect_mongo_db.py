from pymongo import collection
from pymongo.mongo_client import MongoClient


def connect_mongo_db():
    cluster = MongoClient(
        "mongodb+srv://definit:MongoDefInit2023@cluster0.5tujig4.mongodb.net/?retryWrites=true&w=majority")
    db = cluster["psycho_data"]
    return db


def connect_mongo_collection(args):
    return connect_mongo_db()[args]  # в args передается название колекции


def mongo_save(doc, article_link_id, link):
    connect_mongo_collection("link").insert_one({f"{doc}": {f"{article_link_id}": f"{link}"}})


def get_all_link():  # Достаю из монго все ссылки помещаю их в список
    data = []
    for i in connect_mongo_collection("link").find():
        x = str(i['doc'])
        data.append(x[12:-2])
    return data
