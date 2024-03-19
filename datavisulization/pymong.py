
import pymongo
import json


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["data"]
collection=db['dataitems']


file_name = 'jsondata.json'

with open(file_name, 'r', encoding='utf-8') as f:
    data = json.load(f)
    if isinstance(data,list):
        collection.insert_many(data)
        print("Multiple data insert done")
    else:
        collection.insert_one(data)
        print("one data insert done")


