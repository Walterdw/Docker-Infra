import os
from Functions.databaseConnection import connectionToMongo

def initMongo():
    try: 
        mongoClient = connectionToMongo()
        mongoData = {"Test": "Writing in Mongo", "Status": "Working"}
        mongoClient.insert_one(mongoData)
        return True
    except Exception as error:
        print(f"Error: {error}")
        return False