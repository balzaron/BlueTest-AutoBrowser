from mioAuto.common.utils import dict2obj
from pymongo import MongoClient

def buildMongoClient(host:str, port:int=27017):
    return MongoClient(host=host,
                       port = port,
                       maxPoolSize = 150,
                       minPoolSize = 10,
                       maxIdleTimeMS = 600) if (host != None or host != '') and port != None else None

collection = MongoClient('127.0.0.1:27017').get_database('gsy').get_collection('fort')
data = collection.find()
for i in data:
    print(type(i))
