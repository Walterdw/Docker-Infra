import os
import redis
from pymongo import MongoClient

def connectionToMongo():
    MONGO_USER = os.environ['MONGO_USER']
    MONGO_PASS = os.environ['MONGO_PASS']
    MONGO_HOST = os.environ['MONGO_HOST']
    MONGO_DB = os.environ['MONGO_DB']
    MONGO_COLLECTION = os.environ['MONGO_COLLECTION']
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