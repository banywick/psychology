from pymongo.mongo_client import MongoClient


def mongo_save(doc, id, link):
    cluster = MongoClient(
        "mongodb+srv://definit:MongoDefInit2023@cluster0.5tujig4.mongodb.net/?retryWrites=true&w=majority")
    db = cluster["psycho_data"]
    collection = db["link"]
    collection.insert_one( {f"{doc}": {f"{id}": f"{link}"}})
    # query = {"doc.5": {"$exists": True}}  # Удаление документа у которогого ключ = 5
    # result = collection.delete_many(query)
# mylist = ['alex', 'den', '15', 'dog']
# mydict = {str(i): v for i, v in enumerate(mylist, 1)}
# collection.insert_one(mydict)
# print('ok')

# print([doc for doc in collection.find({1: {$exists : True}})])
# print(collection.find({"2": {"$exists": True}}))
# for i in collection.find_one({'3': {"$exists": True}}):
#
#     print(i)
# #
# doc = collection.find_one({"link": {"1": {"$regex": "^asf"}}})
# query = {"link": {"1": {"$regex": "^asf"}}}
# document = collection.find_one(query)

# print(document)
