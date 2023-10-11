import os
import redis
from pymongo import MongoClient

def connectionToMongo(credentials):
    MONGO_USER = credentials['MONGO_USER']
    MONGO_PASS = credentials['MONGO_PASS']
    MONGO_HOST = credentials['MONGO_HOST']
    MONGO_DB = credentials['MONGO_DB']
    MONGO_COLLECTION = credentials['MONGO_COLLECTION']
    MONGO_CONNECTION_STRING = f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}"
    mongoClient = MongoClient(MONGO_CONNECTION_STRING)
    
    mongoDB = mongoClient[f"{MONGO_DB}"]
    mongoCollection = mongoDB[f"{MONGO_COLLECTION}"]
    mongoDBClient = mongoCollection
    return mongoDBClient

def connectionToRedis():
    REDIS_PASS = os.environ['REDIS_PASS']
    redisClient = redis.Redis(host='istea-redis', port=6379, db=0, password=f"{REDIS_PASS}")
    return redisClient