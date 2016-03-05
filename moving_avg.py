import sys
import json
import time
import redis

connection = redis.Redis()

while True:
    pipe = connection.pipeline()
    keys = connection.keys()

    #get the data from redis
    values = connection.mget(keys)

    try:
        deltas = [float(v) for v in values]
    except TypeError:
        continue

    if len(deltas):
        rate = sum(deltas)/float(len(deltas))
    else:
        rate = 0

    conn.conn.setex("movingAvgRate", rate, 200)

    time.sleep(2)