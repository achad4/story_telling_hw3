import sys
import json
import redis
import city_bike_api 
from twitter import Twitter, OAuth, TwitterHTTPError


ACCESS_TOKEN = '4885882060-OPfhKlPKeGIwiGGQgyl5QzIj58v4tZ5JFKUOJli'
ACCESS_SECRET = 'VjXlFKHvDoj7mAcnkdWqMz8UcoTH1gtotIepDHna4uaPr'
CONSUMER_KEY = 'NkSHnhdfiHAhcG0jLeftJAB7m'
CONSUMER_SECRET = 'j0gyjgEsVbcQ2Lm5sETdEjnlsJTfcFOeJIkJZxSJpj7y64sxXG'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

api = Twitter(auth=oauth)
previous_entropy = city_bike_api.entropy()
current_entropy = city_bike_api.entropy()
while True:
	print current_entropy
	# line = sys.stdin.readline()
	# json_data = json.loads(line)
	# avg_tweet_rate = json_data["avg_tweet_rat"]
	# print avg_tweet_rate
	# #observing the stream has shown that people tweet about kanye's album about once every 10 seconds
	# #if it dips below 8, assume he is extram popular 
	# if(avg_tweet_rate < 8 and alert["popularity"] < 1):
	# 	print "TLOP is trending"
	# 	api.statuses.update(status="TLOP is trending")

	# 	alert["popularity"] = 1
	# #if it goes about 12, assume people don't care too much about yeezy at the moment :/
	# if(avg_tweet_rate > 12 and alert["popularity"] > -1):
	# 	print "No one's talking about TLOP :/"
	# 	api.statuses.update(status="No one's talking about TLOP :/")
	# 	alert["popularity"] = -1
	# sys.stdout.flush()
