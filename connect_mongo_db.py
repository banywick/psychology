from pymongo.mongo_client import MongoClient


def connect_mongo_db():
    cluster = MongoClient(
        "mongodb+srv://definit:MongoDefInit2023@cluster0.5tujig4.mongodb.net/?retryWrites=true&w=majority")
    db = cluster["psycho_data"]
    collection = db["link"]
    return collection


def mongo_save(doc, article_link_id ,link):
    connect_mongo_db().insert_one({f"{doc}": {f"{article_link_id}": f"{link}"}})



def get_one_link(): # Достаю из монго все ссылки помещаю их в список
    data = []
    all_link = connect_mongo_db().find()
    for i in all_link:
        x = str(i['doc'])
        data.append(x[12:-2])
        return data

