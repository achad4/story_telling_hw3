import sys
import json
import redis
import urllib
import urllib2
import time 

#use the api to get the current entropy of the rental distribution
response = json.loads(urllib2.urlopen("http://127.0.0.1:5000/entropy").read())
previous_entropy = response['entropy']
current_entropy = response['entropy']
while True:
	delta = current_entropy - previous_entropy
	print delta
	#if the entropy has changed a significant amount, then create an alert using the API
	if(abs(delta) > 0.01):
		data = urllib.urlencode({'message' : 'Entropy changed'})
		u = urllib2.urlopen('http://127.0.0.1:5000/post_alert', data)

	response = json.loads(urllib2.urlopen("http://127.0.0.1:5000/entropy").read())
	previous_entropy = current_entropy
	current_entropy = response['entropy']
	time.sleep(5)
	
