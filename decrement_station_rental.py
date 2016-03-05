import redis
import time

conn = redis.Redis()
while True:
    stations = conn.hkeys("stationHash")
    for station in stations:
        str_count = conn.hget("stationHash", station)
        
        try: 
            count = int(str_count) 
        except ValueError as e: 
            #if there is no count skip it 
            continue 

        if(count > 0):
            conn.hincrby("stationHash", station, -1)
            
    time.sleep(2)