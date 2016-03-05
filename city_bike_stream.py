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
        time_string = m["lastCommunicationTime"]
        #parse the date based on the format the stream gives it in
        t = time.strptime(time_string, "%Y-%m-%d %H:%M:%S %p")
        #convert to epoch time for easier manipulation
        t = int(time.mktime(t))
        if t < 0:
            #sometimes the date comes back as negative-- ignore this
            continue
        relevant_data = { "station" : m["stationName"], 
        				  "availableBikes" : m["availableBikes"], 
        				  "t" : t 
        				}

        print json.dumps(relevant_data)

        stdout.flush()
    time.sleep(2)

