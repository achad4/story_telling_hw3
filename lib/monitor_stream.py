import requests
import json
import time
import redis
import sys

conn = redis.Redis()
availableBikesDict = {}

while True:
    line = sys.stdin.readline()
    data = json.loads(line)

    stationName = data["station"]
    availableBikes = int(data["availableBikes"])
    t = time.time()
    
    # for each station, initialise the store if necessary
    if stationName not in availableBikesDict:
        availableBikesDict[stationName] = availableBikes
        continue
    delta = availableBikes - availableBikesDict[stationName]


    if delta != 0:
        conn.hset(t, "stationName", stationName)
        print json.dumps({'t' : t, 'stationName': stationName})
        sys.stdout.flush()

    availableBikesDict[stationName] = availableBikes
    time.sleep(0.05)