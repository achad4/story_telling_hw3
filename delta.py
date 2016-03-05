import json
import sys

last = 0
while True:
	line = sys.stdin.readline()
	data = json.loads(line)
	#if there is no previous tweet set the last time to the current time
	if last == 0:
		last = data["t"]
		continue
	
	#find the difference in tweet times
	delta = data["t"] - last
	print json.dumps( 
		{ 
			"delta": delta, 
			"t" : data["t"]
		})
	sys.stdout.flush()
	last = data["t"]