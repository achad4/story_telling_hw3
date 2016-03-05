import json
import sys
import redis
import time

conn = redis.Redis()

while True:
    line = sys.stdin.readline()
    data = json.loads(line)
    station = data["station"]
    t = data["t"]
    #put the data into redis
    conn.setex(t, station, 120)
    sys.stdout.flush()
