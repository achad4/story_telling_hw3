Motivation:  New Yorkers love city bikes, and I was just curious as to where bike rentals are concentrated and how consistent this concentration is-- which is why the system alerts on changes in the entropy of the categorical distribution of rentals across the city.  Run it for yourself with the instructions provided and check out how New Yorkers are using their city bikes.  

This program takes in a stream of city bike  data from www.citibikenyc.com and looks for changes in the
number of available bikes (bike rental events).  Using the API, the website displays a histogram of the different
stations across the city and how many rentals have occured at each one in the past 10 minutes.

1. Start the local redis server: ```redis-server /usr/local/etc/redis.conf```
	Note: if restarting the application, run ```redis-cli flushdb``` to clear old data
2. Run the pipeline or manually start the programs ```cd <path to story_telling_3>/bin; ./pipeline.sh```
3. Start the API server ```python bin/city_bike_api.py```
4. Start the alerting system ```python bin/city_bike_alert_bot.py```
5. Start the website```python -m SimpleHTTPServer 8080```

Sources:
1. https://developers.google.com/chart/interactive/docs/gallery/histogram
2. https://github.com/mikedewar/RealTimeStorytelling/tree/master/3