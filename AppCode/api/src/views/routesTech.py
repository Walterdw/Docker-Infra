from flask import Blueprint,jsonify
from bson.json_util import dumps

from functions.common.databaseConnection import connectionToMongo
from functions.common.databaseConnection import connectionToRedis

tech = Blueprint("tech", __name__)

@tech.route('', strict_slashes=False)
def healthcheck():
    return "Ok"

@tech.route('redis', strict_slashes=False)
def redisData():
    mongoCredentials = getCredentialsFromRedis()
    return mongoCredentials

@tech.route('mongo', strict_slashes=False)
def mongoData():
    mongoCredentials = getCredentialsFromRedis()
    mongoClient = connectionToMongo(mongoCredentials)
    mongoData = mongoClient.find()
    mongoDataJson = dumps(mongoData)
    return jsonify(mongoDataJson)

def getCredentialsFromRedis():
    redisClient = connectionToRedis()
    redisData = redisClient.keys()
    mongoCredentials = {}
    for key in redisData:
        keyName = key.decode()
        keyValue = redisClient.get(keyName).decode()
        mongoCredentials[keyName] = keyValue
    return mongoCredentials