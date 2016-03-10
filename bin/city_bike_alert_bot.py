import sys
import json
import redis
import urllib
import urllib2
import time 
from twitter import Twitter, OAuth, TwitterHTTPError


ACCESS_TOKEN = '4885882060-OPfhKlPKeGIwiGGQgyl5QzIj58v4tZ5JFKUOJli'
ACCESS_SECRET = 'VjXlFKHvDoj7mAcnkdWqMz8UcoTH1gtotIepDHna4uaPr'
CONSUMER_KEY = 'NkSHnhdfiHAhcG0jLeftJAB7m'
CONSUMER_SECRET = 'j0gyjgEsVbcQ2Lm5sETdEjnlsJTfcFOeJIkJZxSJpj7y64sxXG'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

api = Twitter(auth=oauth)
response = json.loads(urllib2.urlopen("http://127.0.0.1:5000/entropy").read())
previous_entropy = response['entropy']
current_entropy = response['entropy']
while True:
	delta = current_entropy - previous_entropy
	print delta
	# if(abs(delta) > 0.01):
	if(True):
		data = urllib.urlencode({'message' : 'Entropy changed'})
		u = urllib2.urlopen('http://127.0.0.1:5000/post_alert', data)

	response = json.loads(urllib2.urlopen("http://127.0.0.1:5000/entropy").read())
	previous_entropy = current_entropy
	current_entropy = response['entropy']
	time.sleep(5)
	


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
	
