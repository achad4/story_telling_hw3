import json
import sys
import redis
import time

conn = redis.Redis()

while True:
    line = sys.stdin.readline()
    data = json.loads(line)
    station = data["station"]
    availableBikes = data["availableBikes"]
    #put the data into redis
    conn.hincrby("stationHash", station)
    sys.stdout.flush()