from pymongo import MongoClient
import datetime
from bson import ObjectId


client = MongoClient(host='db')


class MongoAPI:
    def __init__(self, document):
        cursor = client["polls"]
        self.collection = cursor[document]

    def read(self):
        documents = self.collection.find()
        output = [{item: data[item] for item in data}
                  for data in documents]
        return output

    def find_byid(self, id):
        return self.collection.find_one({"_id": ObjectId(id)})

    def write(self, data):
        new_document = data
        new_document["created_at"] = datetime.datetime.now()
        result = self.collection.insert_one(new_document)
        return str(result.inserted_id)

    def delete_all(self):
        self.collection.delete_many({})
