import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client['fm-database']
userCollection = db['users']
photoCollection = db['photos']