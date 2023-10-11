import os
from Functions.databaseConnection import connectionToRedis

def initRedis():
    try: 
        redisClient = connectionToRedis()
        mongoCredentials = {
            "MONGO_USER": f"{os.environ['MONGO_USER']}",
            "MONGO_PASS": f"{os.environ['MONGO_PASS']}",
            "MONGO_HOST": f"{os.environ['MONGO_HOST']}",
            "MONGO_DB": f"{os.environ['MONGO_DB']}",
            "MONGO_COLLECTION": f"{os.environ['MONGO_COLLECTION']}"
            }
        print(mongoCredentials)
        for credential in mongoCredentials:
            redisClient.set(credential, mongoCredentials[credential])
        return True
    except Exception as error:
        print(f"Error: {error}")
        return False