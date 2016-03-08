import json
import sys
import redis
conn = redis.Redis()

last = 0.0
while True:
	line = sys.stdin.readline()
	data = json.loads(line)
	t = float(data["t"])
	#if there is no previous event set the last time to the current time
	if last == 0.0:
		last = t
		continue
	
	#find the difference in rental times
	delta = abs(t - last)

	conn.hset(t, "delta", delta)

	print json.dumps( 
		{ 
			"delta": delta, 
			"t" : t
		})
	sys.stdout.flush()
	last = t