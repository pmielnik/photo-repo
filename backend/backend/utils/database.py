import pymongo
from pymongo import MongoClient
from typing import Dict
from gridfs import GridFS

# URI = "mongodb://127.0.0.1:27017"
# django: http://127.0.0.1:8000

class database:

    DB_NAME = 'photorepo'
    CLIENT = MongoClient()
    DATABASE = CLIENT[DB_NAME]
    USERS = DATABASE['users']
    PHOTOS = DATABASE['photos']
    FILESYSTEM = GridFS(DATABASE)

    @staticmethod
    def insertPhoto(data, filename, photoId=None):
        if photoId is None:
            return database.FILESYSTEM.put(data, filename=filename)
        return database.FILESYSTEM.put(data, filename=filename, _id=photoId)
    
    @staticmethod
    def findPhoto(photoId):
        return database.FILESYSTEM.find_one(filter={'_id': photoId})


    @staticmethod
    def insert(collection: str, data: Dict):
        if collection == 'users':
            database.USERS.insert_one(data)
        elif collection == 'photos':
            database.PHOTOS.insert_one(data)


    @staticmethod
    def insertMany(data: [Dict], photos: [str]):
        for i in range(0, len(photos)-1):
            data[i]['_id'] = database.FILESYSTEM.put(photos)

        database.PHOTOS.insert_many(data)

    @staticmethod
    def update(collection: str, dataFilter: Dict, data: Dict):
        if collection == 'users':
            database.USERS.update(dataFilter, {'$set' : data})
        elif collection == 'photos':
            database.PHOTOS.update(dataFilter, {'$set' : data})

    @staticmethod
    def delete(collection: str, data: Dict):
        if collection == 'users':
            database.USERS.delete_one(data)
        elif collection == 'photos':
            database.PHOTOS.delete_one(data)

    @staticmethod
    def find(collection: str, dataFilter: Dict):
        if collection == 'users' :
            return database.USERS.find(dataFilter)
        elif collection == 'photos':
            return database.PHOTOS.find(dataFilter)
