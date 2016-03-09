import sys
import json
import time
import redis

conn = redis.Redis()

while True:
    deltas = []

    keys = conn.keys()
    for key in keys:
        try:
            r = conn.hget(key, "delta")
            deltas.append(float(r))
        except Exception as e:
            #there might not yet be a delta for this time
            continue


    if len(deltas):
        rate = sum(deltas)/float(len(deltas))
    else:
        rate = 0

    conn.set("movingAvgRate", rate)
    print rate

    time.sleep(5)