import sys

from Functions.initMongo import initMongo
from Functions.initRedis import initRedis

def select_job_to_run(jobToRun):
    match jobToRun:
        case "initMongo":
            initMongo()
            
        case "initRedis":
            initRedis()

        case _:
            print("No job type selected, options: initMongo, initRedis")
            return False

if len(sys.argv) > 1:
    jobName = sys.argv[1]
    select_job_to_run(jobName)
    
else:
    print("No job type selected, options: initMongo, initRedis")