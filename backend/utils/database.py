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
    def insert(type: str, data: Dict)
        if(type == 'users'){
            USERS.insert_one(data)
        }else if(type == 'photos'){
            PHOTOS.insert_one(data)
        }

    @staticmethod
    def insertMany(data: [Dict], photos: [str]){
        for i in range(0, len(photos)-1){
            data[i]['_id'] = FILESYSTEM.put(photoData)
        }

        PHOTOS.insert_many(data)
    }

    @staticmethod
    def update(type: str, dataFilter: Dict, data: Dict){
        if(type == 'users'){
            USERS.update(dataFilter, {'$set' : data})
        }else if(type == 'photos'){
            PHOTOS.update(dataFilter, {'$set' : data})
        }
    }

    @staticmethod
    def delete(type: str, data: Dict){
        if(type == 'users'){
            USERS.delete_one(data)
        }else if(type == 'photos'){
            PHOTOS.delete_one(data)
        }
    }

    @staticmethod
    def find(type: str, dataFilter: Dict){
        if(type == 'users'){
            return USERS.find(dataFilter)
        }else if(type == 'photos'){
            return PHOTOS.find(dataFilter)
        }
    }
