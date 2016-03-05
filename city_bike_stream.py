import requests
import json
import time
from sys import stdout

while True:
    
    # get the citibike response from their API
    r = requests.get("https://www.citibikenyc.com/stations/json")
    
    for m in r.json()["stationBeanList"]:
    	#when a bike is rented extract which station it comes from and how many bikes are
    	#free for renting
        relevant_data = { "station" : m["stationName"], 
        				  "availableBikes" : m["availableBikes"], 
        				  "t" : str(time.time()) 
        				}

        print json.dumps(relevant_data)

    stdout.flush()
    time.sleep(2)

